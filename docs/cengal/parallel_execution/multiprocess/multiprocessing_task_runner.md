---
title: multiprocessing_task_runner
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.multiprocess<wbr>.multiprocessing_task_runner    </h1>

                
                        <input id="mod-multiprocessing_task_runner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-multiprocessing_task_runner-view-source"><span>View Source</span></label>

                        <div class="pdoc-code codehilite"><pre><span></span><span id="L-1"><a href="#L-1"><span class="linenos">  1</span></a><span class="ch">#!/usr/bin/env python</span>
</span><span id="L-2"><a href="#L-2"><span class="linenos">  2</span></a><span class="c1"># coding=utf-8</span>
</span><span id="L-3"><a href="#L-3"><span class="linenos">  3</span></a>
</span><span id="L-4"><a href="#L-4"><span class="linenos">  4</span></a><span class="c1"># Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;</span>
</span><span id="L-5"><a href="#L-5"><span class="linenos">  5</span></a><span class="c1"># </span>
</span><span id="L-6"><a href="#L-6"><span class="linenos">  6</span></a><span class="c1"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span>
</span><span id="L-7"><a href="#L-7"><span class="linenos">  7</span></a><span class="c1"># you may not use this file except in compliance with the License.</span>
</span><span id="L-8"><a href="#L-8"><span class="linenos">  8</span></a><span class="c1"># You may obtain a copy of the License at</span>
</span><span id="L-9"><a href="#L-9"><span class="linenos">  9</span></a><span class="c1"># </span>
</span><span id="L-10"><a href="#L-10"><span class="linenos"> 10</span></a><span class="c1">#     http://www.apache.org/licenses/LICENSE-2.0</span>
</span><span id="L-11"><a href="#L-11"><span class="linenos"> 11</span></a><span class="c1"># </span>
</span><span id="L-12"><a href="#L-12"><span class="linenos"> 12</span></a><span class="c1"># Unless required by applicable law or agreed to in writing, software</span>
</span><span id="L-13"><a href="#L-13"><span class="linenos"> 13</span></a><span class="c1"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span>
</span><span id="L-14"><a href="#L-14"><span class="linenos"> 14</span></a><span class="c1"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>
</span><span id="L-15"><a href="#L-15"><span class="linenos"> 15</span></a><span class="c1"># See the License for the specific language governing permissions and</span>
</span><span id="L-16"><a href="#L-16"><span class="linenos"> 16</span></a><span class="c1"># limitations under the License.</span>
</span><span id="L-17"><a href="#L-17"><span class="linenos"> 17</span></a>
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;SubprocessIsNotInitiatedError&#39;</span><span class="p">,</span> <span class="s1">&#39;SubprocessIsNotReadyError&#39;</span><span class="p">,</span> <span class="s1">&#39;SubprocessTerminatedError&#39;</span><span class="p">,</span> <span class="s1">&#39;Empty&#39;</span><span class="p">,</span> <span class="s1">&#39;Full&#39;</span><span class="p">,</span> <span class="s1">&#39;SendableDataType&#39;</span><span class="p">,</span> <span class="s1">&#39;Transport&#39;</span><span class="p">,</span> <span class="s1">&#39;SubprocessWorkerSettings&#39;</span><span class="p">,</span> <span class="s1">&#39;SubprocessWorker&#39;</span><span class="p">,</span> <span class="s1">&#39;_subprocess_wrapper_profile&#39;</span><span class="p">,</span> <span class="s1">&#39;ExternalPipe&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">import</span> <span class="nn">cProfile</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="c1"># import multiprocessing</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">multiprocessing</span> <span class="kn">import</span> <span class="n">Process</span><span class="p">,</span> <span class="n">Queue</span><span class="p">,</span> <span class="n">Pipe</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">threading</span> <span class="kn">import</span> <span class="n">Thread</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">import</span> <span class="nn">traceback</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">queue</span> <span class="kn">import</span> <span class="n">Empty</span><span class="p">,</span> <span class="n">Full</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">import</span> <span class="nn">marshal</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">import</span> <span class="nn">pickle</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.front_triggerable_variable</span> <span class="kn">import</span> <span class="n">FrontTriggerableVariable</span><span class="p">,</span> <span class="n">FrontTriggerableVariableType</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">cengal.base.classes</span> <span class="kn">import</span> <span class="n">BaseClassSettings</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.load_best_timer</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">pdi</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Dict</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="c1"># import time</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="sd">Module Docstring</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="k">class</span> <span class="nc">SubprocessIsNotInitiatedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="k">pass</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="k">class</span> <span class="nc">SubprocessIsNotReadyError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="k">pass</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="k">class</span> <span class="nc">SubprocessTerminatedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="k">pass</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">class</span> <span class="nc">SendableDataType</span><span class="p">:</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="n">pickable</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="n">marshalable</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="n">custom</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="k">class</span> <span class="nc">Transport</span><span class="p">:</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="n">queue</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="n">pipe</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="n">tcp</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="k">class</span> <span class="nc">SubprocessWorkerSettings</span><span class="p">(</span><span class="n">BaseClassSettings</span><span class="p">):</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiation_function</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.data_shelf = self.settings.initiation_function(</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="c1">#   self.initialization_data)</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">working_function</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># 1) &#39;answer = self.settings.working_function(input_data)&#39;</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="c1">#       if initiation_function is None;</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="c1">#   2) &#39;answer = self.settings.working_function(self.data_shelf, input_data)&#39; if initiation_function</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="c1">#       is not None.</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">stopping_function</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.on_input_queue_is_too_big(self.data_shelf,</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="c1">#   average_input_size_trigger_result) where: average_input_size_trigger_result =</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="c1">#   self.input_queue_average_size_trigger.test_trigger(average_input_size)</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.on_another_bunch_of_data_was_processed(</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="c1">#   self.data_shelf)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_exit</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># on process exit; self.on_exit(self.data_shelf)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_multithreading</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will use multithread mode if True; and multiprocess else.</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># str()</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">profile</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will start worker in profiling mode</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initialization_data</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># any pickable Python data</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span> <span class="n">Transport</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Transport()</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># tcp_link.TCPSettings(). Is used when (self.transport == Transport.tcp)</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_internal_subprocess_input_buffer</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will be able to get input data in nonblocking mode</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data_type</span><span class="p">:</span> <span class="n">SendableDataType</span> <span class="o">=</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data__encoder</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Will be in use when sendable_data_type == SendableDataType.custom.</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="c1">#   Function will encode data in to bytes()</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data__decoder</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Will be in use when sendable_data_type == SendableDataType.custom.</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="c1">#   Function will decode data from bytes()</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># only needed if you want to directly connect this worker with another.</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="c1">#   For example to connect output from this worker to input of another worker.</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># only needed if you want to directly connect this worker with another.</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="c1">#   For example to connect output from this worker to input of another worker.</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger_limit</span> <span class="o">=</span> <span class="mi">30</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_polling_timeout</span> <span class="o">=</span> <span class="mf">0.0</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_reading_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_invalidation_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">working_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;working_function cannot be None!&#39;</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;transport can</span><span class="se">\&#39;</span><span class="s1">t be None&#39;</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">tcp</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;tcp_settings can</span><span class="se">\&#39;</span><span class="s1">t be None while (Transport.tcp == self.transport)&#39;</span><span class="p">)</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="k">class</span> <span class="nc">SubprocessWorker</span><span class="p">:</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; </span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        :param settings: SubprocessWorkerSettings(); you should use copy.copy(SubprocessWorkerSettings(...)) by your </span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="sd">            self if you want</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="sd">        :return: </span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span> <span class="o">=</span> <span class="n">settings</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span> <span class="o">=</span> <span class="mi">500</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="c1"># self.last_log_print_time = time.time()</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span> <span class="o">=</span> <span class="n">FrontTriggerableVariable</span><span class="p">(</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="n">FrontTriggerableVariableType</span><span class="o">.</span><span class="n">bigger_or_equal</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">input_queue_average_size_trigger_limit</span><span class="p">)</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">_encode_sendable_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>                <span class="k">pass</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__encoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__encoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">_decode_sendable_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>                <span class="k">pass</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__decoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__decoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    <span class="k">def</span> <span class="nf">_parsing_worker_wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;0&#39;)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;1&#39;)</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;2&#39;)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>                <span class="k">if</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="s1">&#39;Stopped&#39;</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>                    <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">working_function</span><span class="p">(</span><span class="n">input_data</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;3&#39;)</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;4&#39;)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>                <span class="k">if</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="s1">&#39;Stopped&#39;</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                    <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">working_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span> <span class="n">input_data</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>            <span class="c1"># # print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;6&#39;)</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="c1"># exception = sys.exc_info()</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="c1"># formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="c1"># exception = exception[:2] + (formatted_traceback,)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="c1"># answer = (input_data[0], None)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="c1"># # print(self.settings.process_name)</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="c1"># # print(input_data)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="c1"># # print(exception)</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">())</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;7&#39;)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">answer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;8&#39;)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">answer</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="c1"># print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;)</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">_subprocess_wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="c1"># input_from_parent_process_queue = self.queue_to_subprocess</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="c1"># output_to_parent_process_queue = self.queue_from_subprocess</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>            <span class="c1"># print(&#39; STARTED:&#39;, self.settings.process_name, &#39;; PID:&#39;, os.getpid())</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>            <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="p">(</span><span class="s1">&#39;Started&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>                    <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                    <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initialization_data</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;0&#39;)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;1&#39;, &#39;qsize:&#39;,</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="c1">#       input_from_parent_process_queue.qsize())</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>                <span class="c1"># input_size = input_from_parent_process_queue.qsize()</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="c1"># if input_size &gt; 3:</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;input_size:&#39;, input_size)</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="c1"># output_size = output_to_parent_process_queue.qsize()</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                <span class="c1"># if output_size &gt; 3:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_size:&#39;, output_size)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">use_internal_subprocess_input_buffer</span><span class="p">:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>                        <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>                            <span class="k">if</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">():</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>                                <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>                                <span class="k">break</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                            <span class="k">if</span> <span class="ow">not</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                                <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                                <span class="k">break</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                        
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                        <span class="k">if</span> <span class="n">another_chunk_of_data</span><span class="p">:</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">another_chunk_of_data</span><span class="p">)</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                    <span class="n">input_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">)</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">+=</span> <span class="n">input_size</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span><span class="p">:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                        <span class="n">average_input_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>                        <span class="n">average_input_size_trigger_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span><span class="o">.</span><span class="n">test_trigger</span><span class="p">(</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>                            <span class="n">average_input_size</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                        <span class="k">if</span> <span class="n">average_input_size_trigger_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                            <span class="c1"># if average_input_size_trigger_result:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                            <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size:&#39;, average_input_size)</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>                            <span class="c1"># else:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                            <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size is OK:&#39;, average_input_size)</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>                            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>                                <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span> <span class="n">average_input_size_trigger_result</span><span class="p">)</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>                    <span class="c1"># data = input_from_parent_process_queue.get(block=False, timeout=self.settings.subprocess_reading_timeout)</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;input_data:&#39;, data)</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                        <span class="k">continue</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                    <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>                        <span class="n">data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>                    <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>                        <span class="n">input_size</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">qsize</span><span class="p">()</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">+=</span> <span class="n">input_size</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span><span class="p">:</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>                            <span class="n">average_input_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                            <span class="n">average_input_size_trigger_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span><span class="o">.</span><span class="n">test_trigger</span><span class="p">(</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                                <span class="n">average_input_size</span><span class="p">)</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                            <span class="k">if</span> <span class="n">average_input_size_trigger_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                                <span class="c1"># if average_input_size_trigger_result:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size for Queue:&#39;,</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>                                <span class="c1">#         average_input_size)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                                <span class="c1"># else:</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>                                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size for Queue is OK:&#39;,</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>                                <span class="c1">#         average_input_size)</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                                
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>                                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>                                                                            <span class="n">average_input_size_trigger_result</span><span class="p">)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>                        <span class="k">try</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>                            <span class="n">data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>                        <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>                            <span class="k">pass</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;2&#39;)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>                <span class="c1"># current_time = time.time()</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>                <span class="c1"># if (current_time - self.last_log_print_time) &gt; 2:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                <span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                    <span class="k">continue</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>                <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>                <span class="n">is_worker_is_finalized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>                <span class="n">is_need_to_break_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>                <span class="c1"># data = marshal.loads(data)</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>                <span class="n">continue_processing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>                <span class="k">if</span> <span class="n">continue_processing</span><span class="p">:</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;3&#39;)</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>                    <span class="n">data_with_exception</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                    <span class="n">data_only</span> <span class="o">=</span> <span class="n">data_with_exception</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parsing_worker_wrapper</span><span class="p">(</span><span class="n">data_only</span><span class="p">)</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>                    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_result:&#39;, result)</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>                        <span class="c1"># result = marshal.dumps(result)</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>                        <span class="c1"># output_to_parent_process_queue.put(result)</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>                        <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;6&#39;)</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>                    <span class="n">data_only</span> <span class="o">=</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_parsing_worker_wrapper</span><span class="p">(</span><span class="n">data_only</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>                    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_result:&#39;, result)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>                        <span class="c1"># result = marshal.dumps(result)</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>                        <span class="c1"># output_to_parent_process_queue.put(result)</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>                        <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>                    <span class="n">is_worker_is_finalized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>                    <span class="n">is_need_to_break_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>                    <span class="c1"># break</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>                <span class="k">if</span> <span class="n">continue_processing</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">is_result_was_send</span><span class="p">:</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>                <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_exit</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">is_worker_is_finalized</span><span class="p">:</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_exit</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>                <span class="k">if</span> <span class="n">is_need_to_break_loop</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>                    <span class="k">break</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>                <span class="c1"># print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>                <span class="c1"># if (current_time - self.last_log_print_time) &gt; 2:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>                <span class="c1">#     print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>                <span class="c1">#     self.last_log_print_time = current_time</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="c1"># print(&#39; ENDED:&#39;, self.settings.process_name, &#39;; PID:&#39;, os.getpid())</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="c1"># print(&#39;&lt;&lt;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="k">except</span> <span class="ne">BrokenPipeError</span><span class="p">:</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>            <span class="k">pass</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="k">pass</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>            <span class="k">pass</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>            
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>            
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>            <span class="n">target</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>            <span class="n">arguments</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">profile</span><span class="p">:</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="n">_subprocess_wrapper_profile</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="p">,)</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subprocess_wrapper</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">need_multithreading</span><span class="p">:</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Process</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>            
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="k">if</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>    
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>    <span class="k">def</span> <span class="nf">wait_for_subprocess_readines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>            <span class="k">return</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>                <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>                    <span class="k">raise</span> <span class="n">SubprocessIsNotReadyError</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>                <span class="k">raise</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">_close_connections</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>            <span class="k">return</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>        <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>        
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>        <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>            <span class="k">pass</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>        <span class="k">except</span> <span class="n">SubprocessTerminatedError</span><span class="p">:</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>            <span class="k">pass</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_close_connections</span><span class="p">()</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>    
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>    <span class="k">def</span> <span class="nf">_invalidate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_close_connections</span><span class="p">()</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_invalidation_timeout</span><span class="p">)</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>    <span class="k">def</span> <span class="nf">send_data_to_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a><span class="sd">        :param input_data:</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a><span class="sd">        :return:</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>        
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="p">(</span><span class="n">input_data</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>        <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>        <span class="k">while</span> <span class="n">need_to_retry</span><span class="p">:</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>            <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>                
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>            <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>            <span class="k">except</span> <span class="n">Full</span><span class="p">:</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="n">block</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>            
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>            <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>                <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>    <span class="k">def</span> <span class="nf">is_input_queue_is_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>        
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">)</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>            <span class="c1"># result = self.queue_to_subprocess.empty()</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>        
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>    <span class="k">def</span> <span class="nf">wait_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_input_queue_is_empty</span><span class="p">():</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>            <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>                    <span class="k">break</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>    <span class="k">def</span> <span class="nf">get_answer_from_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a><span class="sd">        Will raise Empty() in non-blocking mode when queue is empty</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a><span class="sd">        :param block:</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a><span class="sd">        :param time_out:  None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a><span class="sd">        :return:</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>        
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>        <span class="n">subprocess_continue_working</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>        <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>                <span class="k">if</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>                    <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>                    <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>                    <span class="k">if</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">):</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>                        <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>                        <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>                        <span class="k">raise</span> <span class="n">Empty</span><span class="p">()</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_reading_timeout</span><span class="p">)</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>                <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>                <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>            
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">subprocess_continue_working</span><span class="p">:</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>        
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">exception</span><span class="p">)</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>            <span class="c1"># print(self.settings.process_name)</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>            <span class="c1"># print(result)</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>            <span class="c1"># print(exception)</span>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>            <span class="c1"># print()</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>            <span class="c1"># print(&#39; &lt;&lt;&lt; SUBPROCESS EXCEPTION:&#39;)</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>            <span class="c1"># trace = &#39;&#39;</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>            <span class="c1"># for line in exception[2]:</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>            <span class="c1">#     trace += line</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>            <span class="c1"># print(trace, file=sys.stderr)</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>            <span class="c1"># print(exception[0])</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>            <span class="c1"># print(exception[1])</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>            <span class="c1"># print(&#39; &gt;&gt;&gt;&#39;)</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>            <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_value</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>            <span class="k">raise</span> <span class="n">exc_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>        
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a><span class="k">def</span> <span class="nf">_subprocess_wrapper_profile</span><span class="p">(</span><span class="n">process_data</span><span class="p">):</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>    <span class="n">printable_name</span> <span class="o">=</span> <span class="n">process_data</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">process_name</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">,</span> <span class="s1">&#39;_&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;.prof&#39;</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>    <span class="n">cProfile</span><span class="o">.</span><span class="n">runctx</span><span class="p">(</span><span class="s1">&#39;process_data._subprocess_wrapper()&#39;</span><span class="p">,</span> <span class="nb">globals</span><span class="p">(),</span> <span class="nb">locals</span><span class="p">(),</span> <span class="n">printable_name</span><span class="p">)</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a><span class="k">class</span> <span class="nc">ExternalPipe</span><span class="p">:</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pipe</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">inverted_pipe</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pipe</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipe</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span></pre></div>


            </section>
                <section id="SubprocessIsNotInitiatedError">
                            <input id="SubprocessIsNotInitiatedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubprocessIsNotInitiatedError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="SubprocessIsNotInitiatedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessIsNotInitiatedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessIsNotInitiatedError-58"><a href="#SubprocessIsNotInitiatedError-58"><span class="linenos">58</span></a><span class="k">class</span> <span class="nc">SubprocessIsNotInitiatedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="SubprocessIsNotInitiatedError-59"><a href="#SubprocessIsNotInitiatedError-59"><span class="linenos">59</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SubprocessIsNotInitiatedError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SubprocessIsNotInitiatedError.with_traceback" class="function">with_traceback</dd>
                <dd id="SubprocessIsNotInitiatedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SubprocessIsNotReadyError">
                            <input id="SubprocessIsNotReadyError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubprocessIsNotReadyError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="SubprocessIsNotReadyError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessIsNotReadyError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessIsNotReadyError-62"><a href="#SubprocessIsNotReadyError-62"><span class="linenos">62</span></a><span class="k">class</span> <span class="nc">SubprocessIsNotReadyError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="SubprocessIsNotReadyError-63"><a href="#SubprocessIsNotReadyError-63"><span class="linenos">63</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SubprocessIsNotReadyError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SubprocessIsNotReadyError.with_traceback" class="function">with_traceback</dd>
                <dd id="SubprocessIsNotReadyError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SubprocessTerminatedError">
                            <input id="SubprocessTerminatedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubprocessTerminatedError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="SubprocessTerminatedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessTerminatedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessTerminatedError-66"><a href="#SubprocessTerminatedError-66"><span class="linenos">66</span></a><span class="k">class</span> <span class="nc">SubprocessTerminatedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="SubprocessTerminatedError-67"><a href="#SubprocessTerminatedError-67"><span class="linenos">67</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="SubprocessTerminatedError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="SubprocessTerminatedError.with_traceback" class="function">with_traceback</dd>
                <dd id="SubprocessTerminatedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Empty">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Empty</span><wbr>(<span class="base">builtins.Exception</span>):

        
    </div>
    <a class="headerlink" href="#Empty"></a>
    
            <div class="docstring"><p>Exception raised by Queue.get(block=0)/get_nowait().</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="Empty.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="Empty.with_traceback" class="function">with_traceback</dd>
                <dd id="Empty.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Full">
                            <input id="Full-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Full</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="Full-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Full"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Full-23"><a href="#Full-23"><span class="linenos">23</span></a><span class="k">class</span> <span class="nc">Full</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="Full-24"><a href="#Full-24"><span class="linenos">24</span></a>    <span class="s1">&#39;Exception raised by Queue.put(block=0)/put_nowait().&#39;</span>
</span><span id="Full-25"><a href="#Full-25"><span class="linenos">25</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Exception raised by Queue.put(block=0)/put_nowait().</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="Full.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="Full.with_traceback" class="function">with_traceback</dd>
                <dd id="Full.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SendableDataType">
                            <input id="SendableDataType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SendableDataType</span>:

                <label class="view-source-button" for="SendableDataType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SendableDataType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SendableDataType-70"><a href="#SendableDataType-70"><span class="linenos">70</span></a><span class="k">class</span> <span class="nc">SendableDataType</span><span class="p">:</span>
</span><span id="SendableDataType-71"><a href="#SendableDataType-71"><span class="linenos">71</span></a>    <span class="n">pickable</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SendableDataType-72"><a href="#SendableDataType-72"><span class="linenos">72</span></a>    <span class="n">marshalable</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="SendableDataType-73"><a href="#SendableDataType-73"><span class="linenos">73</span></a>    <span class="n">custom</span> <span class="o">=</span> <span class="mi">2</span>
</span></pre></div>


    

                            <div id="SendableDataType.pickable" class="classattr">
                                <div class="attr variable">
            <span class="name">pickable</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#SendableDataType.pickable"></a>
    
    

                            </div>
                            <div id="SendableDataType.marshalable" class="classattr">
                                <div class="attr variable">
            <span class="name">marshalable</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#SendableDataType.marshalable"></a>
    
    

                            </div>
                            <div id="SendableDataType.custom" class="classattr">
                                <div class="attr variable">
            <span class="name">custom</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#SendableDataType.custom"></a>
    
    

                            </div>
                </section>
                <section id="Transport">
                            <input id="Transport-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Transport</span>:

                <label class="view-source-button" for="Transport-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Transport"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Transport-76"><a href="#Transport-76"><span class="linenos">76</span></a><span class="k">class</span> <span class="nc">Transport</span><span class="p">:</span>
</span><span id="Transport-77"><a href="#Transport-77"><span class="linenos">77</span></a>    <span class="n">queue</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Transport-78"><a href="#Transport-78"><span class="linenos">78</span></a>    <span class="n">pipe</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Transport-79"><a href="#Transport-79"><span class="linenos">79</span></a>    <span class="n">tcp</span> <span class="o">=</span> <span class="mi">2</span>
</span></pre></div>


    

                            <div id="Transport.queue" class="classattr">
                                <div class="attr variable">
            <span class="name">queue</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#Transport.queue"></a>
    
    

                            </div>
                            <div id="Transport.pipe" class="classattr">
                                <div class="attr variable">
            <span class="name">pipe</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#Transport.pipe"></a>
    
    

                            </div>
                            <div id="Transport.tcp" class="classattr">
                                <div class="attr variable">
            <span class="name">tcp</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#Transport.tcp"></a>
    
    

                            </div>
                </section>
                <section id="SubprocessWorkerSettings">
                            <input id="SubprocessWorkerSettings-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubprocessWorkerSettings</span><wbr>(<span class="base">cengal.base.classes.versions.v_0.classes.BaseClassSettings</span>):

                <label class="view-source-button" for="SubprocessWorkerSettings-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorkerSettings-82"><a href="#SubprocessWorkerSettings-82"><span class="linenos"> 82</span></a><span class="k">class</span> <span class="nc">SubprocessWorkerSettings</span><span class="p">(</span><span class="n">BaseClassSettings</span><span class="p">):</span>
</span><span id="SubprocessWorkerSettings-83"><a href="#SubprocessWorkerSettings-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorkerSettings-84"><a href="#SubprocessWorkerSettings-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiation_function</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.data_shelf = self.settings.initiation_function(</span>
</span><span id="SubprocessWorkerSettings-85"><a href="#SubprocessWorkerSettings-85"><span class="linenos"> 85</span></a>        <span class="c1">#   self.initialization_data)</span>
</span><span id="SubprocessWorkerSettings-86"><a href="#SubprocessWorkerSettings-86"><span class="linenos"> 86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">working_function</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># 1) &#39;answer = self.settings.working_function(input_data)&#39;</span>
</span><span id="SubprocessWorkerSettings-87"><a href="#SubprocessWorkerSettings-87"><span class="linenos"> 87</span></a>        <span class="c1">#       if initiation_function is None;</span>
</span><span id="SubprocessWorkerSettings-88"><a href="#SubprocessWorkerSettings-88"><span class="linenos"> 88</span></a>        <span class="c1">#   2) &#39;answer = self.settings.working_function(self.data_shelf, input_data)&#39; if initiation_function</span>
</span><span id="SubprocessWorkerSettings-89"><a href="#SubprocessWorkerSettings-89"><span class="linenos"> 89</span></a>        <span class="c1">#       is not None.</span>
</span><span id="SubprocessWorkerSettings-90"><a href="#SubprocessWorkerSettings-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">stopping_function</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorkerSettings-91"><a href="#SubprocessWorkerSettings-91"><span class="linenos"> 91</span></a>
</span><span id="SubprocessWorkerSettings-92"><a href="#SubprocessWorkerSettings-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.on_input_queue_is_too_big(self.data_shelf,</span>
</span><span id="SubprocessWorkerSettings-93"><a href="#SubprocessWorkerSettings-93"><span class="linenos"> 93</span></a>        <span class="c1">#   average_input_size_trigger_result) where: average_input_size_trigger_result =</span>
</span><span id="SubprocessWorkerSettings-94"><a href="#SubprocessWorkerSettings-94"><span class="linenos"> 94</span></a>        <span class="c1">#   self.input_queue_average_size_trigger.test_trigger(average_input_size)</span>
</span><span id="SubprocessWorkerSettings-95"><a href="#SubprocessWorkerSettings-95"><span class="linenos"> 95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># self.on_another_bunch_of_data_was_processed(</span>
</span><span id="SubprocessWorkerSettings-96"><a href="#SubprocessWorkerSettings-96"><span class="linenos"> 96</span></a>        <span class="c1">#   self.data_shelf)</span>
</span><span id="SubprocessWorkerSettings-97"><a href="#SubprocessWorkerSettings-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">on_exit</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># on process exit; self.on_exit(self.data_shelf)</span>
</span><span id="SubprocessWorkerSettings-98"><a href="#SubprocessWorkerSettings-98"><span class="linenos"> 98</span></a>
</span><span id="SubprocessWorkerSettings-99"><a href="#SubprocessWorkerSettings-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">need_multithreading</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will use multithread mode if True; and multiprocess else.</span>
</span><span id="SubprocessWorkerSettings-100"><a href="#SubprocessWorkerSettings-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># str()</span>
</span><span id="SubprocessWorkerSettings-101"><a href="#SubprocessWorkerSettings-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">profile</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will start worker in profiling mode</span>
</span><span id="SubprocessWorkerSettings-102"><a href="#SubprocessWorkerSettings-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initialization_data</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># any pickable Python data</span>
</span><span id="SubprocessWorkerSettings-103"><a href="#SubprocessWorkerSettings-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span> <span class="n">Transport</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Transport()</span>
</span><span id="SubprocessWorkerSettings-104"><a href="#SubprocessWorkerSettings-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># tcp_link.TCPSettings(). Is used when (self.transport == Transport.tcp)</span>
</span><span id="SubprocessWorkerSettings-105"><a href="#SubprocessWorkerSettings-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">use_internal_subprocess_input_buffer</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"># will be able to get input data in nonblocking mode</span>
</span><span id="SubprocessWorkerSettings-106"><a href="#SubprocessWorkerSettings-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data_type</span><span class="p">:</span> <span class="n">SendableDataType</span> <span class="o">=</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span>
</span><span id="SubprocessWorkerSettings-107"><a href="#SubprocessWorkerSettings-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data__encoder</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Will be in use when sendable_data_type == SendableDataType.custom.</span>
</span><span id="SubprocessWorkerSettings-108"><a href="#SubprocessWorkerSettings-108"><span class="linenos">108</span></a>        <span class="c1">#   Function will encode data in to bytes()</span>
</span><span id="SubprocessWorkerSettings-109"><a href="#SubprocessWorkerSettings-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sendable_data__decoder</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># Will be in use when sendable_data_type == SendableDataType.custom.</span>
</span><span id="SubprocessWorkerSettings-110"><a href="#SubprocessWorkerSettings-110"><span class="linenos">110</span></a>        <span class="c1">#   Function will decode data from bytes()</span>
</span><span id="SubprocessWorkerSettings-111"><a href="#SubprocessWorkerSettings-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># only needed if you want to directly connect this worker with another.</span>
</span><span id="SubprocessWorkerSettings-112"><a href="#SubprocessWorkerSettings-112"><span class="linenos">112</span></a>        <span class="c1">#   For example to connect output from this worker to input of another worker.</span>
</span><span id="SubprocessWorkerSettings-113"><a href="#SubprocessWorkerSettings-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="kc">None</span>  <span class="c1"># only needed if you want to directly connect this worker with another.</span>
</span><span id="SubprocessWorkerSettings-114"><a href="#SubprocessWorkerSettings-114"><span class="linenos">114</span></a>        <span class="c1">#   For example to connect output from this worker to input of another worker.</span>
</span><span id="SubprocessWorkerSettings-115"><a href="#SubprocessWorkerSettings-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger_limit</span> <span class="o">=</span> <span class="mi">30</span>
</span><span id="SubprocessWorkerSettings-116"><a href="#SubprocessWorkerSettings-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_polling_timeout</span> <span class="o">=</span> <span class="mf">0.0</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorkerSettings-117"><a href="#SubprocessWorkerSettings-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_reading_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorkerSettings-118"><a href="#SubprocessWorkerSettings-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorkerSettings-119"><a href="#SubprocessWorkerSettings-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_invalidation_timeout</span> <span class="o">=</span> <span class="mf">0.1</span>  <span class="c1"># None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorkerSettings-120"><a href="#SubprocessWorkerSettings-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorkerSettings-121"><a href="#SubprocessWorkerSettings-121"><span class="linenos">121</span></a>
</span><span id="SubprocessWorkerSettings-122"><a href="#SubprocessWorkerSettings-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorkerSettings-123"><a href="#SubprocessWorkerSettings-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">working_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-124"><a href="#SubprocessWorkerSettings-124"><span class="linenos">124</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;working_function cannot be None!&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings-125"><a href="#SubprocessWorkerSettings-125"><span class="linenos">125</span></a>
</span><span id="SubprocessWorkerSettings-126"><a href="#SubprocessWorkerSettings-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-127"><a href="#SubprocessWorkerSettings-127"><span class="linenos">127</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;transport can</span><span class="se">\&#39;</span><span class="s1">t be None&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings-128"><a href="#SubprocessWorkerSettings-128"><span class="linenos">128</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-129"><a href="#SubprocessWorkerSettings-129"><span class="linenos">129</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">tcp</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-130"><a href="#SubprocessWorkerSettings-130"><span class="linenos">130</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-131"><a href="#SubprocessWorkerSettings-131"><span class="linenos">131</span></a>                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;tcp_settings can</span><span class="se">\&#39;</span><span class="s1">t be None while (Transport.tcp == self.transport)&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings-132"><a href="#SubprocessWorkerSettings-132"><span class="linenos">132</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings-133"><a href="#SubprocessWorkerSettings-133"><span class="linenos">133</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="SubprocessWorkerSettings.initiation_function" class="classattr">
                                <div class="attr variable">
            <span class="name">initiation_function</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.initiation_function"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.working_function" class="classattr">
                                <div class="attr variable">
            <span class="name">working_function</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.working_function"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.stopping_function" class="classattr">
                                <div class="attr variable">
            <span class="name">stopping_function</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.stopping_function"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.on_input_queue_is_too_big" class="classattr">
                                <div class="attr variable">
            <span class="name">on_input_queue_is_too_big</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.on_input_queue_is_too_big"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.on_another_bunch_of_data_was_processed" class="classattr">
                                <div class="attr variable">
            <span class="name">on_another_bunch_of_data_was_processed</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.on_another_bunch_of_data_was_processed"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.on_exit" class="classattr">
                                <div class="attr variable">
            <span class="name">on_exit</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.on_exit"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.need_multithreading" class="classattr">
                                <div class="attr variable">
            <span class="name">need_multithreading</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.need_multithreading"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.process_name" class="classattr">
                                <div class="attr variable">
            <span class="name">process_name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.process_name"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.profile" class="classattr">
                                <div class="attr variable">
            <span class="name">profile</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.profile"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.initialization_data" class="classattr">
                                <div class="attr variable">
            <span class="name">initialization_data</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.initialization_data"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.transport" class="classattr">
                                <div class="attr variable">
            <span class="name">transport</span><span class="annotation">: <a href="#Transport">Transport</a></span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.transport"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.tcp_settings" class="classattr">
                                <div class="attr variable">
            <span class="name">tcp_settings</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.tcp_settings"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.use_internal_subprocess_input_buffer" class="classattr">
                                <div class="attr variable">
            <span class="name">use_internal_subprocess_input_buffer</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.use_internal_subprocess_input_buffer"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.sendable_data_type" class="classattr">
                                <div class="attr variable">
            <span class="name">sendable_data_type</span><span class="annotation">: <a href="#SendableDataType">SendableDataType</a></span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.sendable_data_type"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.sendable_data__encoder" class="classattr">
                                <div class="attr variable">
            <span class="name">sendable_data__encoder</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.sendable_data__encoder"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.sendable_data__decoder" class="classattr">
                                <div class="attr variable">
            <span class="name">sendable_data__decoder</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.sendable_data__decoder"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.queue_to_subprocess" class="classattr">
                                <div class="attr variable">
            <span class="name">queue_to_subprocess</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.queue_to_subprocess"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.queue_from_subprocess" class="classattr">
                                <div class="attr variable">
            <span class="name">queue_from_subprocess</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.queue_from_subprocess"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.input_queue_average_size_trigger_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">input_queue_average_size_trigger_limit</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.input_queue_average_size_trigger_limit"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.subprocess_polling_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_polling_timeout</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.subprocess_polling_timeout"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.subprocess_reading_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_reading_timeout</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.subprocess_reading_timeout"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.subprocess_writing_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_writing_timeout</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.subprocess_writing_timeout"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.subprocess_invalidation_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_invalidation_timeout</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.subprocess_invalidation_timeout"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.indicate_subprocess_readyness" class="classattr">
                                <div class="attr variable">
            <span class="name">indicate_subprocess_readyness</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.indicate_subprocess_readyness"></a>
    
    

                            </div>
                            <div id="SubprocessWorkerSettings.check" class="classattr">
                                        <input id="SubprocessWorkerSettings.check-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorkerSettings.check-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorkerSettings.check"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorkerSettings.check-122"><a href="#SubprocessWorkerSettings.check-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">check</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorkerSettings.check-123"><a href="#SubprocessWorkerSettings.check-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">working_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-124"><a href="#SubprocessWorkerSettings.check-124"><span class="linenos">124</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;working_function cannot be None!&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings.check-125"><a href="#SubprocessWorkerSettings.check-125"><span class="linenos">125</span></a>
</span><span id="SubprocessWorkerSettings.check-126"><a href="#SubprocessWorkerSettings.check-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-127"><a href="#SubprocessWorkerSettings.check-127"><span class="linenos">127</span></a>            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;transport can</span><span class="se">\&#39;</span><span class="s1">t be None&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings.check-128"><a href="#SubprocessWorkerSettings.check-128"><span class="linenos">128</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-129"><a href="#SubprocessWorkerSettings.check-129"><span class="linenos">129</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">tcp</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-130"><a href="#SubprocessWorkerSettings.check-130"><span class="linenos">130</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-131"><a href="#SubprocessWorkerSettings.check-131"><span class="linenos">131</span></a>                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s1">&#39;tcp_settings can</span><span class="se">\&#39;</span><span class="s1">t be None while (Transport.tcp == self.transport)&#39;</span><span class="p">)</span>
</span><span id="SubprocessWorkerSettings.check-132"><a href="#SubprocessWorkerSettings.check-132"><span class="linenos">132</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorkerSettings.check-133"><a href="#SubprocessWorkerSettings.check-133"><span class="linenos">133</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tcp_settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="SubprocessWorker">
                            <input id="SubprocessWorker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">SubprocessWorker</span>:

                <label class="view-source-button" for="SubprocessWorker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker-136"><a href="#SubprocessWorker-136"><span class="linenos">136</span></a><span class="k">class</span> <span class="nc">SubprocessWorker</span><span class="p">:</span>
</span><span id="SubprocessWorker-137"><a href="#SubprocessWorker-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span><span class="p">):</span>
</span><span id="SubprocessWorker-138"><a href="#SubprocessWorker-138"><span class="linenos">138</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; </span>
</span><span id="SubprocessWorker-139"><a href="#SubprocessWorker-139"><span class="linenos">139</span></a><span class="sd">        :param settings: SubprocessWorkerSettings(); you should use copy.copy(SubprocessWorkerSettings(...)) by your </span>
</span><span id="SubprocessWorker-140"><a href="#SubprocessWorker-140"><span class="linenos">140</span></a><span class="sd">            self if you want</span>
</span><span id="SubprocessWorker-141"><a href="#SubprocessWorker-141"><span class="linenos">141</span></a><span class="sd">        :return: </span>
</span><span id="SubprocessWorker-142"><a href="#SubprocessWorker-142"><span class="linenos">142</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker-143"><a href="#SubprocessWorker-143"><span class="linenos">143</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="SubprocessWorker-144"><a href="#SubprocessWorker-144"><span class="linenos">144</span></a>        
</span><span id="SubprocessWorker-145"><a href="#SubprocessWorker-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span> <span class="o">=</span> <span class="n">settings</span>
</span><span id="SubprocessWorker-146"><a href="#SubprocessWorker-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="SubprocessWorker-147"><a href="#SubprocessWorker-147"><span class="linenos">147</span></a>
</span><span id="SubprocessWorker-148"><a href="#SubprocessWorker-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-149"><a href="#SubprocessWorker-149"><span class="linenos">149</span></a>
</span><span id="SubprocessWorker-150"><a href="#SubprocessWorker-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-151"><a href="#SubprocessWorker-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-152"><a href="#SubprocessWorker-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-153"><a href="#SubprocessWorker-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker-154"><a href="#SubprocessWorker-154"><span class="linenos">154</span></a>
</span><span id="SubprocessWorker-155"><a href="#SubprocessWorker-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="SubprocessWorker-156"><a href="#SubprocessWorker-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-157"><a href="#SubprocessWorker-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-158"><a href="#SubprocessWorker-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span> <span class="o">=</span> <span class="mi">500</span>
</span><span id="SubprocessWorker-159"><a href="#SubprocessWorker-159"><span class="linenos">159</span></a>        <span class="c1"># self.last_log_print_time = time.time()</span>
</span><span id="SubprocessWorker-160"><a href="#SubprocessWorker-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-161"><a href="#SubprocessWorker-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span> <span class="o">=</span> <span class="n">FrontTriggerableVariable</span><span class="p">(</span>
</span><span id="SubprocessWorker-162"><a href="#SubprocessWorker-162"><span class="linenos">162</span></a>            <span class="n">FrontTriggerableVariableType</span><span class="o">.</span><span class="n">bigger_or_equal</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">input_queue_average_size_trigger_limit</span><span class="p">)</span>
</span><span id="SubprocessWorker-163"><a href="#SubprocessWorker-163"><span class="linenos">163</span></a>
</span><span id="SubprocessWorker-164"><a href="#SubprocessWorker-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">_encode_sendable_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="SubprocessWorker-165"><a href="#SubprocessWorker-165"><span class="linenos">165</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="SubprocessWorker-166"><a href="#SubprocessWorker-166"><span class="linenos">166</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-167"><a href="#SubprocessWorker-167"><span class="linenos">167</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="SubprocessWorker-168"><a href="#SubprocessWorker-168"><span class="linenos">168</span></a>                <span class="k">pass</span>
</span><span id="SubprocessWorker-169"><a href="#SubprocessWorker-169"><span class="linenos">169</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="SubprocessWorker-170"><a href="#SubprocessWorker-170"><span class="linenos">170</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-171"><a href="#SubprocessWorker-171"><span class="linenos">171</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="SubprocessWorker-172"><a href="#SubprocessWorker-172"><span class="linenos">172</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__encoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-173"><a href="#SubprocessWorker-173"><span class="linenos">173</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-174"><a href="#SubprocessWorker-174"><span class="linenos">174</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="SubprocessWorker-175"><a href="#SubprocessWorker-175"><span class="linenos">175</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-176"><a href="#SubprocessWorker-176"><span class="linenos">176</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="SubprocessWorker-177"><a href="#SubprocessWorker-177"><span class="linenos">177</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-178"><a href="#SubprocessWorker-178"><span class="linenos">178</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="SubprocessWorker-179"><a href="#SubprocessWorker-179"><span class="linenos">179</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__encoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-180"><a href="#SubprocessWorker-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="SubprocessWorker-181"><a href="#SubprocessWorker-181"><span class="linenos">181</span></a>
</span><span id="SubprocessWorker-182"><a href="#SubprocessWorker-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">_decode_sendable_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="SubprocessWorker-183"><a href="#SubprocessWorker-183"><span class="linenos">183</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="SubprocessWorker-184"><a href="#SubprocessWorker-184"><span class="linenos">184</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-185"><a href="#SubprocessWorker-185"><span class="linenos">185</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="SubprocessWorker-186"><a href="#SubprocessWorker-186"><span class="linenos">186</span></a>                <span class="k">pass</span>
</span><span id="SubprocessWorker-187"><a href="#SubprocessWorker-187"><span class="linenos">187</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="SubprocessWorker-188"><a href="#SubprocessWorker-188"><span class="linenos">188</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-189"><a href="#SubprocessWorker-189"><span class="linenos">189</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="SubprocessWorker-190"><a href="#SubprocessWorker-190"><span class="linenos">190</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__decoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-191"><a href="#SubprocessWorker-191"><span class="linenos">191</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-192"><a href="#SubprocessWorker-192"><span class="linenos">192</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">pickable</span><span class="p">:</span>
</span><span id="SubprocessWorker-193"><a href="#SubprocessWorker-193"><span class="linenos">193</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-194"><a href="#SubprocessWorker-194"><span class="linenos">194</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">marshalable</span><span class="p">:</span>
</span><span id="SubprocessWorker-195"><a href="#SubprocessWorker-195"><span class="linenos">195</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-196"><a href="#SubprocessWorker-196"><span class="linenos">196</span></a>            <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data_type</span> <span class="o">==</span> <span class="n">SendableDataType</span><span class="o">.</span><span class="n">custom</span><span class="p">:</span>
</span><span id="SubprocessWorker-197"><a href="#SubprocessWorker-197"><span class="linenos">197</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">sendable_data__decoder</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-198"><a href="#SubprocessWorker-198"><span class="linenos">198</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="SubprocessWorker-199"><a href="#SubprocessWorker-199"><span class="linenos">199</span></a>
</span><span id="SubprocessWorker-200"><a href="#SubprocessWorker-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="nf">_parsing_worker_wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="SubprocessWorker-201"><a href="#SubprocessWorker-201"><span class="linenos">201</span></a>        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;0&#39;)</span>
</span><span id="SubprocessWorker-202"><a href="#SubprocessWorker-202"><span class="linenos">202</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-203"><a href="#SubprocessWorker-203"><span class="linenos">203</span></a>        <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-204"><a href="#SubprocessWorker-204"><span class="linenos">204</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-205"><a href="#SubprocessWorker-205"><span class="linenos">205</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-206"><a href="#SubprocessWorker-206"><span class="linenos">206</span></a>            <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;1&#39;)</span>
</span><span id="SubprocessWorker-207"><a href="#SubprocessWorker-207"><span class="linenos">207</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-208"><a href="#SubprocessWorker-208"><span class="linenos">208</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;2&#39;)</span>
</span><span id="SubprocessWorker-209"><a href="#SubprocessWorker-209"><span class="linenos">209</span></a>                <span class="k">if</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="SubprocessWorker-210"><a href="#SubprocessWorker-210"><span class="linenos">210</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-211"><a href="#SubprocessWorker-211"><span class="linenos">211</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span><span class="p">()</span>
</span><span id="SubprocessWorker-212"><a href="#SubprocessWorker-212"><span class="linenos">212</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-213"><a href="#SubprocessWorker-213"><span class="linenos">213</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="s1">&#39;Stopped&#39;</span>
</span><span id="SubprocessWorker-214"><a href="#SubprocessWorker-214"><span class="linenos">214</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-215"><a href="#SubprocessWorker-215"><span class="linenos">215</span></a>                    <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">working_function</span><span class="p">(</span><span class="n">input_data</span><span class="p">)</span>
</span><span id="SubprocessWorker-216"><a href="#SubprocessWorker-216"><span class="linenos">216</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;3&#39;)</span>
</span><span id="SubprocessWorker-217"><a href="#SubprocessWorker-217"><span class="linenos">217</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-218"><a href="#SubprocessWorker-218"><span class="linenos">218</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;4&#39;)</span>
</span><span id="SubprocessWorker-219"><a href="#SubprocessWorker-219"><span class="linenos">219</span></a>                <span class="k">if</span> <span class="n">stop</span><span class="p">:</span>
</span><span id="SubprocessWorker-220"><a href="#SubprocessWorker-220"><span class="linenos">220</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-221"><a href="#SubprocessWorker-221"><span class="linenos">221</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">stopping_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="SubprocessWorker-222"><a href="#SubprocessWorker-222"><span class="linenos">222</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-223"><a href="#SubprocessWorker-223"><span class="linenos">223</span></a>                        <span class="n">answer</span> <span class="o">=</span> <span class="s1">&#39;Stopped&#39;</span>
</span><span id="SubprocessWorker-224"><a href="#SubprocessWorker-224"><span class="linenos">224</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-225"><a href="#SubprocessWorker-225"><span class="linenos">225</span></a>                    <span class="n">answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">working_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span> <span class="n">input_data</span><span class="p">)</span>
</span><span id="SubprocessWorker-226"><a href="#SubprocessWorker-226"><span class="linenos">226</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="SubprocessWorker-227"><a href="#SubprocessWorker-227"><span class="linenos">227</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="SubprocessWorker-228"><a href="#SubprocessWorker-228"><span class="linenos">228</span></a>            <span class="c1"># # print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;6&#39;)</span>
</span><span id="SubprocessWorker-229"><a href="#SubprocessWorker-229"><span class="linenos">229</span></a>            <span class="c1"># exception = sys.exc_info()</span>
</span><span id="SubprocessWorker-230"><a href="#SubprocessWorker-230"><span class="linenos">230</span></a>            <span class="c1"># formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])</span>
</span><span id="SubprocessWorker-231"><a href="#SubprocessWorker-231"><span class="linenos">231</span></a>            <span class="c1"># exception = exception[:2] + (formatted_traceback,)</span>
</span><span id="SubprocessWorker-232"><a href="#SubprocessWorker-232"><span class="linenos">232</span></a>            <span class="c1"># answer = (input_data[0], None)</span>
</span><span id="SubprocessWorker-233"><a href="#SubprocessWorker-233"><span class="linenos">233</span></a>            <span class="c1"># # print(self.settings.process_name)</span>
</span><span id="SubprocessWorker-234"><a href="#SubprocessWorker-234"><span class="linenos">234</span></a>            <span class="c1"># # print(input_data)</span>
</span><span id="SubprocessWorker-235"><a href="#SubprocessWorker-235"><span class="linenos">235</span></a>            <span class="c1"># # print(exception)</span>
</span><span id="SubprocessWorker-236"><a href="#SubprocessWorker-236"><span class="linenos">236</span></a>            <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-237"><a href="#SubprocessWorker-237"><span class="linenos">237</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">())</span>
</span><span id="SubprocessWorker-238"><a href="#SubprocessWorker-238"><span class="linenos">238</span></a>
</span><span id="SubprocessWorker-239"><a href="#SubprocessWorker-239"><span class="linenos">239</span></a>        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;7&#39;)</span>
</span><span id="SubprocessWorker-240"><a href="#SubprocessWorker-240"><span class="linenos">240</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">answer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="SubprocessWorker-241"><a href="#SubprocessWorker-241"><span class="linenos">241</span></a>            <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;, &#39;8&#39;)</span>
</span><span id="SubprocessWorker-242"><a href="#SubprocessWorker-242"><span class="linenos">242</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">answer</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="SubprocessWorker-243"><a href="#SubprocessWorker-243"><span class="linenos">243</span></a>
</span><span id="SubprocessWorker-244"><a href="#SubprocessWorker-244"><span class="linenos">244</span></a>        <span class="c1"># print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_parsing_worker_wrapper&#39;)</span>
</span><span id="SubprocessWorker-245"><a href="#SubprocessWorker-245"><span class="linenos">245</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="SubprocessWorker-246"><a href="#SubprocessWorker-246"><span class="linenos">246</span></a>
</span><span id="SubprocessWorker-247"><a href="#SubprocessWorker-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="nf">_subprocess_wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker-248"><a href="#SubprocessWorker-248"><span class="linenos">248</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-249"><a href="#SubprocessWorker-249"><span class="linenos">249</span></a>            <span class="c1"># input_from_parent_process_queue = self.queue_to_subprocess</span>
</span><span id="SubprocessWorker-250"><a href="#SubprocessWorker-250"><span class="linenos">250</span></a>            <span class="c1"># output_to_parent_process_queue = self.queue_from_subprocess</span>
</span><span id="SubprocessWorker-251"><a href="#SubprocessWorker-251"><span class="linenos">251</span></a>
</span><span id="SubprocessWorker-252"><a href="#SubprocessWorker-252"><span class="linenos">252</span></a>            <span class="c1"># print(&#39; STARTED:&#39;, self.settings.process_name, &#39;; PID:&#39;, os.getpid())</span>
</span><span id="SubprocessWorker-253"><a href="#SubprocessWorker-253"><span class="linenos">253</span></a>
</span><span id="SubprocessWorker-254"><a href="#SubprocessWorker-254"><span class="linenos">254</span></a>            <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-255"><a href="#SubprocessWorker-255"><span class="linenos">255</span></a>            <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-256"><a href="#SubprocessWorker-256"><span class="linenos">256</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-257"><a href="#SubprocessWorker-257"><span class="linenos">257</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-258"><a href="#SubprocessWorker-258"><span class="linenos">258</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-259"><a href="#SubprocessWorker-259"><span class="linenos">259</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-260"><a href="#SubprocessWorker-260"><span class="linenos">260</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-261"><a href="#SubprocessWorker-261"><span class="linenos">261</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker-262"><a href="#SubprocessWorker-262"><span class="linenos">262</span></a>
</span><span id="SubprocessWorker-263"><a href="#SubprocessWorker-263"><span class="linenos">263</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span>
</span><span id="SubprocessWorker-264"><a href="#SubprocessWorker-264"><span class="linenos">264</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="p">(</span><span class="s1">&#39;Started&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="SubprocessWorker-265"><a href="#SubprocessWorker-265"><span class="linenos">265</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-266"><a href="#SubprocessWorker-266"><span class="linenos">266</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-267"><a href="#SubprocessWorker-267"><span class="linenos">267</span></a>                    <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-268"><a href="#SubprocessWorker-268"><span class="linenos">268</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-269"><a href="#SubprocessWorker-269"><span class="linenos">269</span></a>                    <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-270"><a href="#SubprocessWorker-270"><span class="linenos">270</span></a>
</span><span id="SubprocessWorker-271"><a href="#SubprocessWorker-271"><span class="linenos">271</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-272"><a href="#SubprocessWorker-272"><span class="linenos">272</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initiation_function</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">initialization_data</span><span class="p">)</span>
</span><span id="SubprocessWorker-273"><a href="#SubprocessWorker-273"><span class="linenos">273</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="SubprocessWorker-274"><a href="#SubprocessWorker-274"><span class="linenos">274</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;0&#39;)</span>
</span><span id="SubprocessWorker-275"><a href="#SubprocessWorker-275"><span class="linenos">275</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;1&#39;, &#39;qsize:&#39;,</span>
</span><span id="SubprocessWorker-276"><a href="#SubprocessWorker-276"><span class="linenos">276</span></a>                <span class="c1">#       input_from_parent_process_queue.qsize())</span>
</span><span id="SubprocessWorker-277"><a href="#SubprocessWorker-277"><span class="linenos">277</span></a>
</span><span id="SubprocessWorker-278"><a href="#SubprocessWorker-278"><span class="linenos">278</span></a>                <span class="c1"># input_size = input_from_parent_process_queue.qsize()</span>
</span><span id="SubprocessWorker-279"><a href="#SubprocessWorker-279"><span class="linenos">279</span></a>                <span class="c1"># if input_size &gt; 3:</span>
</span><span id="SubprocessWorker-280"><a href="#SubprocessWorker-280"><span class="linenos">280</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;input_size:&#39;, input_size)</span>
</span><span id="SubprocessWorker-281"><a href="#SubprocessWorker-281"><span class="linenos">281</span></a>                <span class="c1"># output_size = output_to_parent_process_queue.qsize()</span>
</span><span id="SubprocessWorker-282"><a href="#SubprocessWorker-282"><span class="linenos">282</span></a>                <span class="c1"># if output_size &gt; 3:</span>
</span><span id="SubprocessWorker-283"><a href="#SubprocessWorker-283"><span class="linenos">283</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_size:&#39;, output_size)</span>
</span><span id="SubprocessWorker-284"><a href="#SubprocessWorker-284"><span class="linenos">284</span></a>
</span><span id="SubprocessWorker-285"><a href="#SubprocessWorker-285"><span class="linenos">285</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-286"><a href="#SubprocessWorker-286"><span class="linenos">286</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">use_internal_subprocess_input_buffer</span><span class="p">:</span>
</span><span id="SubprocessWorker-287"><a href="#SubprocessWorker-287"><span class="linenos">287</span></a>                    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="SubprocessWorker-288"><a href="#SubprocessWorker-288"><span class="linenos">288</span></a>                        <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-289"><a href="#SubprocessWorker-289"><span class="linenos">289</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-290"><a href="#SubprocessWorker-290"><span class="linenos">290</span></a>                            <span class="k">if</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">():</span>
</span><span id="SubprocessWorker-291"><a href="#SubprocessWorker-291"><span class="linenos">291</span></a>                                <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker-292"><a href="#SubprocessWorker-292"><span class="linenos">292</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-293"><a href="#SubprocessWorker-293"><span class="linenos">293</span></a>                                <span class="k">break</span>
</span><span id="SubprocessWorker-294"><a href="#SubprocessWorker-294"><span class="linenos">294</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-295"><a href="#SubprocessWorker-295"><span class="linenos">295</span></a>                            <span class="k">if</span> <span class="ow">not</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">empty</span><span class="p">():</span>
</span><span id="SubprocessWorker-296"><a href="#SubprocessWorker-296"><span class="linenos">296</span></a>                                <span class="n">another_chunk_of_data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="SubprocessWorker-297"><a href="#SubprocessWorker-297"><span class="linenos">297</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-298"><a href="#SubprocessWorker-298"><span class="linenos">298</span></a>                                <span class="k">break</span>
</span><span id="SubprocessWorker-299"><a href="#SubprocessWorker-299"><span class="linenos">299</span></a>                        
</span><span id="SubprocessWorker-300"><a href="#SubprocessWorker-300"><span class="linenos">300</span></a>                        <span class="k">if</span> <span class="n">another_chunk_of_data</span><span class="p">:</span>
</span><span id="SubprocessWorker-301"><a href="#SubprocessWorker-301"><span class="linenos">301</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">another_chunk_of_data</span><span class="p">)</span>
</span><span id="SubprocessWorker-302"><a href="#SubprocessWorker-302"><span class="linenos">302</span></a>
</span><span id="SubprocessWorker-303"><a href="#SubprocessWorker-303"><span class="linenos">303</span></a>                    <span class="n">input_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">)</span>
</span><span id="SubprocessWorker-304"><a href="#SubprocessWorker-304"><span class="linenos">304</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="SubprocessWorker-305"><a href="#SubprocessWorker-305"><span class="linenos">305</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">+=</span> <span class="n">input_size</span>
</span><span id="SubprocessWorker-306"><a href="#SubprocessWorker-306"><span class="linenos">306</span></a>                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span><span class="p">:</span>
</span><span id="SubprocessWorker-307"><a href="#SubprocessWorker-307"><span class="linenos">307</span></a>                        <span class="n">average_input_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span>
</span><span id="SubprocessWorker-308"><a href="#SubprocessWorker-308"><span class="linenos">308</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-309"><a href="#SubprocessWorker-309"><span class="linenos">309</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-310"><a href="#SubprocessWorker-310"><span class="linenos">310</span></a>                        <span class="n">average_input_size_trigger_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span><span class="o">.</span><span class="n">test_trigger</span><span class="p">(</span>
</span><span id="SubprocessWorker-311"><a href="#SubprocessWorker-311"><span class="linenos">311</span></a>                            <span class="n">average_input_size</span><span class="p">)</span>
</span><span id="SubprocessWorker-312"><a href="#SubprocessWorker-312"><span class="linenos">312</span></a>                        <span class="k">if</span> <span class="n">average_input_size_trigger_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-313"><a href="#SubprocessWorker-313"><span class="linenos">313</span></a>                            <span class="c1"># if average_input_size_trigger_result:</span>
</span><span id="SubprocessWorker-314"><a href="#SubprocessWorker-314"><span class="linenos">314</span></a>                            <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size:&#39;, average_input_size)</span>
</span><span id="SubprocessWorker-315"><a href="#SubprocessWorker-315"><span class="linenos">315</span></a>                            <span class="c1"># else:</span>
</span><span id="SubprocessWorker-316"><a href="#SubprocessWorker-316"><span class="linenos">316</span></a>                            <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size is OK:&#39;, average_input_size)</span>
</span><span id="SubprocessWorker-317"><a href="#SubprocessWorker-317"><span class="linenos">317</span></a>
</span><span id="SubprocessWorker-318"><a href="#SubprocessWorker-318"><span class="linenos">318</span></a>                            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-319"><a href="#SubprocessWorker-319"><span class="linenos">319</span></a>                                <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span> <span class="n">average_input_size_trigger_result</span><span class="p">)</span>
</span><span id="SubprocessWorker-320"><a href="#SubprocessWorker-320"><span class="linenos">320</span></a>
</span><span id="SubprocessWorker-321"><a href="#SubprocessWorker-321"><span class="linenos">321</span></a>                    <span class="c1"># data = input_from_parent_process_queue.get(block=False, timeout=self.settings.subprocess_reading_timeout)</span>
</span><span id="SubprocessWorker-322"><a href="#SubprocessWorker-322"><span class="linenos">322</span></a>                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="SubprocessWorker-323"><a href="#SubprocessWorker-323"><span class="linenos">323</span></a>                        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-324"><a href="#SubprocessWorker-324"><span class="linenos">324</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;input_data:&#39;, data)</span>
</span><span id="SubprocessWorker-325"><a href="#SubprocessWorker-325"><span class="linenos">325</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="SubprocessWorker-326"><a href="#SubprocessWorker-326"><span class="linenos">326</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-327"><a href="#SubprocessWorker-327"><span class="linenos">327</span></a>                        <span class="k">continue</span>
</span><span id="SubprocessWorker-328"><a href="#SubprocessWorker-328"><span class="linenos">328</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-329"><a href="#SubprocessWorker-329"><span class="linenos">329</span></a>                    <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-330"><a href="#SubprocessWorker-330"><span class="linenos">330</span></a>                        <span class="n">data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker-331"><a href="#SubprocessWorker-331"><span class="linenos">331</span></a>                    <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-332"><a href="#SubprocessWorker-332"><span class="linenos">332</span></a>                        <span class="n">input_size</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">qsize</span><span class="p">()</span>
</span><span id="SubprocessWorker-333"><a href="#SubprocessWorker-333"><span class="linenos">333</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="SubprocessWorker-334"><a href="#SubprocessWorker-334"><span class="linenos">334</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">+=</span> <span class="n">input_size</span>
</span><span id="SubprocessWorker-335"><a href="#SubprocessWorker-335"><span class="linenos">335</span></a>                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span><span class="p">:</span>
</span><span id="SubprocessWorker-336"><a href="#SubprocessWorker-336"><span class="linenos">336</span></a>                            <span class="n">average_input_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span>
</span><span id="SubprocessWorker-337"><a href="#SubprocessWorker-337"><span class="linenos">337</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-338"><a href="#SubprocessWorker-338"><span class="linenos">338</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker-339"><a href="#SubprocessWorker-339"><span class="linenos">339</span></a>                            <span class="n">average_input_size_trigger_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span><span class="o">.</span><span class="n">test_trigger</span><span class="p">(</span>
</span><span id="SubprocessWorker-340"><a href="#SubprocessWorker-340"><span class="linenos">340</span></a>                                <span class="n">average_input_size</span><span class="p">)</span>
</span><span id="SubprocessWorker-341"><a href="#SubprocessWorker-341"><span class="linenos">341</span></a>                            <span class="k">if</span> <span class="n">average_input_size_trigger_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-342"><a href="#SubprocessWorker-342"><span class="linenos">342</span></a>                                <span class="c1"># if average_input_size_trigger_result:</span>
</span><span id="SubprocessWorker-343"><a href="#SubprocessWorker-343"><span class="linenos">343</span></a>                                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size for Queue:&#39;,</span>
</span><span id="SubprocessWorker-344"><a href="#SubprocessWorker-344"><span class="linenos">344</span></a>                                <span class="c1">#         average_input_size)</span>
</span><span id="SubprocessWorker-345"><a href="#SubprocessWorker-345"><span class="linenos">345</span></a>                                <span class="c1"># else:</span>
</span><span id="SubprocessWorker-346"><a href="#SubprocessWorker-346"><span class="linenos">346</span></a>                                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;average_input_size for Queue is OK:&#39;,</span>
</span><span id="SubprocessWorker-347"><a href="#SubprocessWorker-347"><span class="linenos">347</span></a>                                <span class="c1">#         average_input_size)</span>
</span><span id="SubprocessWorker-348"><a href="#SubprocessWorker-348"><span class="linenos">348</span></a>                                
</span><span id="SubprocessWorker-349"><a href="#SubprocessWorker-349"><span class="linenos">349</span></a>                                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-350"><a href="#SubprocessWorker-350"><span class="linenos">350</span></a>                                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_input_queue_is_too_big</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">,</span>
</span><span id="SubprocessWorker-351"><a href="#SubprocessWorker-351"><span class="linenos">351</span></a>                                                                            <span class="n">average_input_size_trigger_result</span><span class="p">)</span>
</span><span id="SubprocessWorker-352"><a href="#SubprocessWorker-352"><span class="linenos">352</span></a>
</span><span id="SubprocessWorker-353"><a href="#SubprocessWorker-353"><span class="linenos">353</span></a>                        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-354"><a href="#SubprocessWorker-354"><span class="linenos">354</span></a>                            <span class="n">data</span> <span class="o">=</span> <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-355"><a href="#SubprocessWorker-355"><span class="linenos">355</span></a>                        <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="SubprocessWorker-356"><a href="#SubprocessWorker-356"><span class="linenos">356</span></a>                            <span class="k">pass</span>
</span><span id="SubprocessWorker-357"><a href="#SubprocessWorker-357"><span class="linenos">357</span></a>
</span><span id="SubprocessWorker-358"><a href="#SubprocessWorker-358"><span class="linenos">358</span></a>                <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;2&#39;)</span>
</span><span id="SubprocessWorker-359"><a href="#SubprocessWorker-359"><span class="linenos">359</span></a>
</span><span id="SubprocessWorker-360"><a href="#SubprocessWorker-360"><span class="linenos">360</span></a>                <span class="c1"># current_time = time.time()</span>
</span><span id="SubprocessWorker-361"><a href="#SubprocessWorker-361"><span class="linenos">361</span></a>                <span class="c1"># if (current_time - self.last_log_print_time) &gt; 2:</span>
</span><span id="SubprocessWorker-362"><a href="#SubprocessWorker-362"><span class="linenos">362</span></a>                <span class="c1">#     print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="SubprocessWorker-363"><a href="#SubprocessWorker-363"><span class="linenos">363</span></a>
</span><span id="SubprocessWorker-364"><a href="#SubprocessWorker-364"><span class="linenos">364</span></a>                <span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-365"><a href="#SubprocessWorker-365"><span class="linenos">365</span></a>                    <span class="k">continue</span>
</span><span id="SubprocessWorker-366"><a href="#SubprocessWorker-366"><span class="linenos">366</span></a>
</span><span id="SubprocessWorker-367"><a href="#SubprocessWorker-367"><span class="linenos">367</span></a>                <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-368"><a href="#SubprocessWorker-368"><span class="linenos">368</span></a>                <span class="n">is_worker_is_finalized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-369"><a href="#SubprocessWorker-369"><span class="linenos">369</span></a>                <span class="n">is_need_to_break_loop</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-370"><a href="#SubprocessWorker-370"><span class="linenos">370</span></a>
</span><span id="SubprocessWorker-371"><a href="#SubprocessWorker-371"><span class="linenos">371</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker-372"><a href="#SubprocessWorker-372"><span class="linenos">372</span></a>                <span class="c1"># data = marshal.loads(data)</span>
</span><span id="SubprocessWorker-373"><a href="#SubprocessWorker-373"><span class="linenos">373</span></a>                <span class="n">continue_processing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-374"><a href="#SubprocessWorker-374"><span class="linenos">374</span></a>                <span class="k">if</span> <span class="n">continue_processing</span><span class="p">:</span>
</span><span id="SubprocessWorker-375"><a href="#SubprocessWorker-375"><span class="linenos">375</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;3&#39;)</span>
</span><span id="SubprocessWorker-376"><a href="#SubprocessWorker-376"><span class="linenos">376</span></a>                    <span class="n">data_with_exception</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-377"><a href="#SubprocessWorker-377"><span class="linenos">377</span></a>                    <span class="n">data_only</span> <span class="o">=</span> <span class="n">data_with_exception</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-378"><a href="#SubprocessWorker-378"><span class="linenos">378</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_parsing_worker_wrapper</span><span class="p">(</span><span class="n">data_only</span><span class="p">)</span>
</span><span id="SubprocessWorker-379"><a href="#SubprocessWorker-379"><span class="linenos">379</span></a>                    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-380"><a href="#SubprocessWorker-380"><span class="linenos">380</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_result:&#39;, result)</span>
</span><span id="SubprocessWorker-381"><a href="#SubprocessWorker-381"><span class="linenos">381</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="SubprocessWorker-382"><a href="#SubprocessWorker-382"><span class="linenos">382</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-383"><a href="#SubprocessWorker-383"><span class="linenos">383</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-384"><a href="#SubprocessWorker-384"><span class="linenos">384</span></a>                        <span class="c1"># result = marshal.dumps(result)</span>
</span><span id="SubprocessWorker-385"><a href="#SubprocessWorker-385"><span class="linenos">385</span></a>                        <span class="c1"># output_to_parent_process_queue.put(result)</span>
</span><span id="SubprocessWorker-386"><a href="#SubprocessWorker-386"><span class="linenos">386</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-387"><a href="#SubprocessWorker-387"><span class="linenos">387</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-388"><a href="#SubprocessWorker-388"><span class="linenos">388</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-389"><a href="#SubprocessWorker-389"><span class="linenos">389</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-390"><a href="#SubprocessWorker-390"><span class="linenos">390</span></a>
</span><span id="SubprocessWorker-391"><a href="#SubprocessWorker-391"><span class="linenos">391</span></a>                        <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-392"><a href="#SubprocessWorker-392"><span class="linenos">392</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="SubprocessWorker-393"><a href="#SubprocessWorker-393"><span class="linenos">393</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-394"><a href="#SubprocessWorker-394"><span class="linenos">394</span></a>                    <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;6&#39;)</span>
</span><span id="SubprocessWorker-395"><a href="#SubprocessWorker-395"><span class="linenos">395</span></a>
</span><span id="SubprocessWorker-396"><a href="#SubprocessWorker-396"><span class="linenos">396</span></a>                    <span class="n">data_only</span> <span class="o">=</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="SubprocessWorker-397"><a href="#SubprocessWorker-397"><span class="linenos">397</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_parsing_worker_wrapper</span><span class="p">(</span><span class="n">data_only</span><span class="p">,</span> <span class="n">stop</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-398"><a href="#SubprocessWorker-398"><span class="linenos">398</span></a>                    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-399"><a href="#SubprocessWorker-399"><span class="linenos">399</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;output_result:&#39;, result)</span>
</span><span id="SubprocessWorker-400"><a href="#SubprocessWorker-400"><span class="linenos">400</span></a>                        <span class="c1"># print(&#39;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;, &#39;5&#39;)</span>
</span><span id="SubprocessWorker-401"><a href="#SubprocessWorker-401"><span class="linenos">401</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-402"><a href="#SubprocessWorker-402"><span class="linenos">402</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-403"><a href="#SubprocessWorker-403"><span class="linenos">403</span></a>                        <span class="c1"># result = marshal.dumps(result)</span>
</span><span id="SubprocessWorker-404"><a href="#SubprocessWorker-404"><span class="linenos">404</span></a>                        <span class="c1"># output_to_parent_process_queue.put(result)</span>
</span><span id="SubprocessWorker-405"><a href="#SubprocessWorker-405"><span class="linenos">405</span></a>                        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-406"><a href="#SubprocessWorker-406"><span class="linenos">406</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-407"><a href="#SubprocessWorker-407"><span class="linenos">407</span></a>                        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-408"><a href="#SubprocessWorker-408"><span class="linenos">408</span></a>                            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="SubprocessWorker-409"><a href="#SubprocessWorker-409"><span class="linenos">409</span></a>
</span><span id="SubprocessWorker-410"><a href="#SubprocessWorker-410"><span class="linenos">410</span></a>                        <span class="n">is_result_was_send</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-411"><a href="#SubprocessWorker-411"><span class="linenos">411</span></a>
</span><span id="SubprocessWorker-412"><a href="#SubprocessWorker-412"><span class="linenos">412</span></a>                    <span class="n">is_worker_is_finalized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-413"><a href="#SubprocessWorker-413"><span class="linenos">413</span></a>                    <span class="n">is_need_to_break_loop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-414"><a href="#SubprocessWorker-414"><span class="linenos">414</span></a>                    <span class="c1"># break</span>
</span><span id="SubprocessWorker-415"><a href="#SubprocessWorker-415"><span class="linenos">415</span></a>
</span><span id="SubprocessWorker-416"><a href="#SubprocessWorker-416"><span class="linenos">416</span></a>                <span class="k">if</span> <span class="n">continue_processing</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">is_result_was_send</span><span class="p">:</span>
</span><span id="SubprocessWorker-417"><a href="#SubprocessWorker-417"><span class="linenos">417</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_another_bunch_of_data_was_processed</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="SubprocessWorker-418"><a href="#SubprocessWorker-418"><span class="linenos">418</span></a>
</span><span id="SubprocessWorker-419"><a href="#SubprocessWorker-419"><span class="linenos">419</span></a>                <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_exit</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="n">is_worker_is_finalized</span><span class="p">:</span>
</span><span id="SubprocessWorker-420"><a href="#SubprocessWorker-420"><span class="linenos">420</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">on_exit</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span><span class="p">)</span>
</span><span id="SubprocessWorker-421"><a href="#SubprocessWorker-421"><span class="linenos">421</span></a>
</span><span id="SubprocessWorker-422"><a href="#SubprocessWorker-422"><span class="linenos">422</span></a>                <span class="k">if</span> <span class="n">is_need_to_break_loop</span><span class="p">:</span>
</span><span id="SubprocessWorker-423"><a href="#SubprocessWorker-423"><span class="linenos">423</span></a>                    <span class="k">break</span>
</span><span id="SubprocessWorker-424"><a href="#SubprocessWorker-424"><span class="linenos">424</span></a>
</span><span id="SubprocessWorker-425"><a href="#SubprocessWorker-425"><span class="linenos">425</span></a>                <span class="c1"># print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="SubprocessWorker-426"><a href="#SubprocessWorker-426"><span class="linenos">426</span></a>
</span><span id="SubprocessWorker-427"><a href="#SubprocessWorker-427"><span class="linenos">427</span></a>                <span class="c1"># if (current_time - self.last_log_print_time) &gt; 2:</span>
</span><span id="SubprocessWorker-428"><a href="#SubprocessWorker-428"><span class="linenos">428</span></a>                <span class="c1">#     print(&#39;&lt;&lt;===&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="SubprocessWorker-429"><a href="#SubprocessWorker-429"><span class="linenos">429</span></a>                <span class="c1">#     self.last_log_print_time = current_time</span>
</span><span id="SubprocessWorker-430"><a href="#SubprocessWorker-430"><span class="linenos">430</span></a>
</span><span id="SubprocessWorker-431"><a href="#SubprocessWorker-431"><span class="linenos">431</span></a>            <span class="c1"># print(&#39; ENDED:&#39;, self.settings.process_name, &#39;; PID:&#39;, os.getpid())</span>
</span><span id="SubprocessWorker-432"><a href="#SubprocessWorker-432"><span class="linenos">432</span></a>            <span class="c1"># print(&#39;&lt;&lt;===&gt;&gt;&#39;, self.settings.process_name, &#39;_subprocess_wrapper&#39;)</span>
</span><span id="SubprocessWorker-433"><a href="#SubprocessWorker-433"><span class="linenos">433</span></a>        <span class="k">except</span> <span class="ne">BrokenPipeError</span><span class="p">:</span>
</span><span id="SubprocessWorker-434"><a href="#SubprocessWorker-434"><span class="linenos">434</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker-435"><a href="#SubprocessWorker-435"><span class="linenos">435</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker-436"><a href="#SubprocessWorker-436"><span class="linenos">436</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker-437"><a href="#SubprocessWorker-437"><span class="linenos">437</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker-438"><a href="#SubprocessWorker-438"><span class="linenos">438</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker-439"><a href="#SubprocessWorker-439"><span class="linenos">439</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="SubprocessWorker-440"><a href="#SubprocessWorker-440"><span class="linenos">440</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-441"><a href="#SubprocessWorker-441"><span class="linenos">441</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-442"><a href="#SubprocessWorker-442"><span class="linenos">442</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-443"><a href="#SubprocessWorker-443"><span class="linenos">443</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-444"><a href="#SubprocessWorker-444"><span class="linenos">444</span></a>                <span class="n">input_from_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-445"><a href="#SubprocessWorker-445"><span class="linenos">445</span></a>                <span class="n">output_to_parent_process_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker-446"><a href="#SubprocessWorker-446"><span class="linenos">446</span></a>            
</span><span id="SubprocessWorker-447"><a href="#SubprocessWorker-447"><span class="linenos">447</span></a>            <span class="n">input_from_parent_process_queue</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-448"><a href="#SubprocessWorker-448"><span class="linenos">448</span></a>            <span class="n">output_to_parent_process_queue</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-449"><a href="#SubprocessWorker-449"><span class="linenos">449</span></a>            
</span><span id="SubprocessWorker-450"><a href="#SubprocessWorker-450"><span class="linenos">450</span></a>
</span><span id="SubprocessWorker-451"><a href="#SubprocessWorker-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker-452"><a href="#SubprocessWorker-452"><span class="linenos">452</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-453"><a href="#SubprocessWorker-453"><span class="linenos">453</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-454"><a href="#SubprocessWorker-454"><span class="linenos">454</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-455"><a href="#SubprocessWorker-455"><span class="linenos">455</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="SubprocessWorker-456"><a href="#SubprocessWorker-456"><span class="linenos">456</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-457"><a href="#SubprocessWorker-457"><span class="linenos">457</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="SubprocessWorker-458"><a href="#SubprocessWorker-458"><span class="linenos">458</span></a>
</span><span id="SubprocessWorker-459"><a href="#SubprocessWorker-459"><span class="linenos">459</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-460"><a href="#SubprocessWorker-460"><span class="linenos">460</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-461"><a href="#SubprocessWorker-461"><span class="linenos">461</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="SubprocessWorker-462"><a href="#SubprocessWorker-462"><span class="linenos">462</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-463"><a href="#SubprocessWorker-463"><span class="linenos">463</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="SubprocessWorker-464"><a href="#SubprocessWorker-464"><span class="linenos">464</span></a>
</span><span id="SubprocessWorker-465"><a href="#SubprocessWorker-465"><span class="linenos">465</span></a>            <span class="n">target</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-466"><a href="#SubprocessWorker-466"><span class="linenos">466</span></a>            <span class="n">arguments</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-467"><a href="#SubprocessWorker-467"><span class="linenos">467</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">profile</span><span class="p">:</span>
</span><span id="SubprocessWorker-468"><a href="#SubprocessWorker-468"><span class="linenos">468</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="n">_subprocess_wrapper_profile</span>
</span><span id="SubprocessWorker-469"><a href="#SubprocessWorker-469"><span class="linenos">469</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="p">,)</span>
</span><span id="SubprocessWorker-470"><a href="#SubprocessWorker-470"><span class="linenos">470</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-471"><a href="#SubprocessWorker-471"><span class="linenos">471</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subprocess_wrapper</span>
</span><span id="SubprocessWorker-472"><a href="#SubprocessWorker-472"><span class="linenos">472</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="SubprocessWorker-473"><a href="#SubprocessWorker-473"><span class="linenos">473</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-474"><a href="#SubprocessWorker-474"><span class="linenos">474</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">need_multithreading</span><span class="p">:</span>
</span><span id="SubprocessWorker-475"><a href="#SubprocessWorker-475"><span class="linenos">475</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-476"><a href="#SubprocessWorker-476"><span class="linenos">476</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-477"><a href="#SubprocessWorker-477"><span class="linenos">477</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Process</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-478"><a href="#SubprocessWorker-478"><span class="linenos">478</span></a>            
</span><span id="SubprocessWorker-479"><a href="#SubprocessWorker-479"><span class="linenos">479</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="SubprocessWorker-480"><a href="#SubprocessWorker-480"><span class="linenos">480</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-481"><a href="#SubprocessWorker-481"><span class="linenos">481</span></a>        
</span><span id="SubprocessWorker-482"><a href="#SubprocessWorker-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span>
</span><span id="SubprocessWorker-483"><a href="#SubprocessWorker-483"><span class="linenos">483</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-484"><a href="#SubprocessWorker-484"><span class="linenos">484</span></a>    
</span><span id="SubprocessWorker-485"><a href="#SubprocessWorker-485"><span class="linenos">485</span></a>    <span class="k">def</span> <span class="nf">wait_for_subprocess_readines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker-486"><a href="#SubprocessWorker-486"><span class="linenos">486</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-487"><a href="#SubprocessWorker-487"><span class="linenos">487</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker-488"><a href="#SubprocessWorker-488"><span class="linenos">488</span></a>        
</span><span id="SubprocessWorker-489"><a href="#SubprocessWorker-489"><span class="linenos">489</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span>
</span><span id="SubprocessWorker-490"><a href="#SubprocessWorker-490"><span class="linenos">490</span></a>            <span class="k">return</span>
</span><span id="SubprocessWorker-491"><a href="#SubprocessWorker-491"><span class="linenos">491</span></a>
</span><span id="SubprocessWorker-492"><a href="#SubprocessWorker-492"><span class="linenos">492</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span>
</span><span id="SubprocessWorker-493"><a href="#SubprocessWorker-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-494"><a href="#SubprocessWorker-494"><span class="linenos">494</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-495"><a href="#SubprocessWorker-495"><span class="linenos">495</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-496"><a href="#SubprocessWorker-496"><span class="linenos">496</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker-497"><a href="#SubprocessWorker-497"><span class="linenos">497</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-498"><a href="#SubprocessWorker-498"><span class="linenos">498</span></a>                <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="SubprocessWorker-499"><a href="#SubprocessWorker-499"><span class="linenos">499</span></a>                    <span class="k">raise</span> <span class="n">SubprocessIsNotReadyError</span>
</span><span id="SubprocessWorker-500"><a href="#SubprocessWorker-500"><span class="linenos">500</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="SubprocessWorker-501"><a href="#SubprocessWorker-501"><span class="linenos">501</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-502"><a href="#SubprocessWorker-502"><span class="linenos">502</span></a>                <span class="k">raise</span>
</span><span id="SubprocessWorker-503"><a href="#SubprocessWorker-503"><span class="linenos">503</span></a>    
</span><span id="SubprocessWorker-504"><a href="#SubprocessWorker-504"><span class="linenos">504</span></a>    <span class="k">def</span> <span class="nf">_close_connections</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker-505"><a href="#SubprocessWorker-505"><span class="linenos">505</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-506"><a href="#SubprocessWorker-506"><span class="linenos">506</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-507"><a href="#SubprocessWorker-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-508"><a href="#SubprocessWorker-508"><span class="linenos">508</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-509"><a href="#SubprocessWorker-509"><span class="linenos">509</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-510"><a href="#SubprocessWorker-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-511"><a href="#SubprocessWorker-511"><span class="linenos">511</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="SubprocessWorker-512"><a href="#SubprocessWorker-512"><span class="linenos">512</span></a>
</span><span id="SubprocessWorker-513"><a href="#SubprocessWorker-513"><span class="linenos">513</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker-514"><a href="#SubprocessWorker-514"><span class="linenos">514</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-515"><a href="#SubprocessWorker-515"><span class="linenos">515</span></a>            <span class="k">return</span>
</span><span id="SubprocessWorker-516"><a href="#SubprocessWorker-516"><span class="linenos">516</span></a>        
</span><span id="SubprocessWorker-517"><a href="#SubprocessWorker-517"><span class="linenos">517</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-518"><a href="#SubprocessWorker-518"><span class="linenos">518</span></a>
</span><span id="SubprocessWorker-519"><a href="#SubprocessWorker-519"><span class="linenos">519</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="SubprocessWorker-520"><a href="#SubprocessWorker-520"><span class="linenos">520</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker-521"><a href="#SubprocessWorker-521"><span class="linenos">521</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="SubprocessWorker-522"><a href="#SubprocessWorker-522"><span class="linenos">522</span></a>
</span><span id="SubprocessWorker-523"><a href="#SubprocessWorker-523"><span class="linenos">523</span></a>        <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-524"><a href="#SubprocessWorker-524"><span class="linenos">524</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-525"><a href="#SubprocessWorker-525"><span class="linenos">525</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-526"><a href="#SubprocessWorker-526"><span class="linenos">526</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-527"><a href="#SubprocessWorker-527"><span class="linenos">527</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-528"><a href="#SubprocessWorker-528"><span class="linenos">528</span></a>
</span><span id="SubprocessWorker-529"><a href="#SubprocessWorker-529"><span class="linenos">529</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-530"><a href="#SubprocessWorker-530"><span class="linenos">530</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker-531"><a href="#SubprocessWorker-531"><span class="linenos">531</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-532"><a href="#SubprocessWorker-532"><span class="linenos">532</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker-533"><a href="#SubprocessWorker-533"><span class="linenos">533</span></a>        
</span><span id="SubprocessWorker-534"><a href="#SubprocessWorker-534"><span class="linenos">534</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-535"><a href="#SubprocessWorker-535"><span class="linenos">535</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker-536"><a href="#SubprocessWorker-536"><span class="linenos">536</span></a>        <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="SubprocessWorker-537"><a href="#SubprocessWorker-537"><span class="linenos">537</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker-538"><a href="#SubprocessWorker-538"><span class="linenos">538</span></a>        <span class="k">except</span> <span class="n">SubprocessTerminatedError</span><span class="p">:</span>
</span><span id="SubprocessWorker-539"><a href="#SubprocessWorker-539"><span class="linenos">539</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker-540"><a href="#SubprocessWorker-540"><span class="linenos">540</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="SubprocessWorker-541"><a href="#SubprocessWorker-541"><span class="linenos">541</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_close_connections</span><span class="p">()</span>
</span><span id="SubprocessWorker-542"><a href="#SubprocessWorker-542"><span class="linenos">542</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-543"><a href="#SubprocessWorker-543"><span class="linenos">543</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="SubprocessWorker-544"><a href="#SubprocessWorker-544"><span class="linenos">544</span></a>    
</span><span id="SubprocessWorker-545"><a href="#SubprocessWorker-545"><span class="linenos">545</span></a>    <span class="k">def</span> <span class="nf">_invalidate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker-546"><a href="#SubprocessWorker-546"><span class="linenos">546</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_close_connections</span><span class="p">()</span>
</span><span id="SubprocessWorker-547"><a href="#SubprocessWorker-547"><span class="linenos">547</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-548"><a href="#SubprocessWorker-548"><span class="linenos">548</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_invalidation_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker-549"><a href="#SubprocessWorker-549"><span class="linenos">549</span></a>
</span><span id="SubprocessWorker-550"><a href="#SubprocessWorker-550"><span class="linenos">550</span></a>    <span class="k">def</span> <span class="nf">send_data_to_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker-551"><a href="#SubprocessWorker-551"><span class="linenos">551</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="SubprocessWorker-552"><a href="#SubprocessWorker-552"><span class="linenos">552</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="SubprocessWorker-553"><a href="#SubprocessWorker-553"><span class="linenos">553</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="SubprocessWorker-554"><a href="#SubprocessWorker-554"><span class="linenos">554</span></a><span class="sd">        :param input_data:</span>
</span><span id="SubprocessWorker-555"><a href="#SubprocessWorker-555"><span class="linenos">555</span></a><span class="sd">        :return:</span>
</span><span id="SubprocessWorker-556"><a href="#SubprocessWorker-556"><span class="linenos">556</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker-557"><a href="#SubprocessWorker-557"><span class="linenos">557</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-558"><a href="#SubprocessWorker-558"><span class="linenos">558</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker-559"><a href="#SubprocessWorker-559"><span class="linenos">559</span></a>
</span><span id="SubprocessWorker-560"><a href="#SubprocessWorker-560"><span class="linenos">560</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker-561"><a href="#SubprocessWorker-561"><span class="linenos">561</span></a>        
</span><span id="SubprocessWorker-562"><a href="#SubprocessWorker-562"><span class="linenos">562</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="p">(</span><span class="n">input_data</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="SubprocessWorker-563"><a href="#SubprocessWorker-563"><span class="linenos">563</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker-564"><a href="#SubprocessWorker-564"><span class="linenos">564</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="SubprocessWorker-565"><a href="#SubprocessWorker-565"><span class="linenos">565</span></a>        <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-566"><a href="#SubprocessWorker-566"><span class="linenos">566</span></a>        <span class="k">while</span> <span class="n">need_to_retry</span><span class="p">:</span>
</span><span id="SubprocessWorker-567"><a href="#SubprocessWorker-567"><span class="linenos">567</span></a>            <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-568"><a href="#SubprocessWorker-568"><span class="linenos">568</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-569"><a href="#SubprocessWorker-569"><span class="linenos">569</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-570"><a href="#SubprocessWorker-570"><span class="linenos">570</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-571"><a href="#SubprocessWorker-571"><span class="linenos">571</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-572"><a href="#SubprocessWorker-572"><span class="linenos">572</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-573"><a href="#SubprocessWorker-573"><span class="linenos">573</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-574"><a href="#SubprocessWorker-574"><span class="linenos">574</span></a>
</span><span id="SubprocessWorker-575"><a href="#SubprocessWorker-575"><span class="linenos">575</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-576"><a href="#SubprocessWorker-576"><span class="linenos">576</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker-577"><a href="#SubprocessWorker-577"><span class="linenos">577</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-578"><a href="#SubprocessWorker-578"><span class="linenos">578</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker-579"><a href="#SubprocessWorker-579"><span class="linenos">579</span></a>                
</span><span id="SubprocessWorker-580"><a href="#SubprocessWorker-580"><span class="linenos">580</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-581"><a href="#SubprocessWorker-581"><span class="linenos">581</span></a>            <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker-582"><a href="#SubprocessWorker-582"><span class="linenos">582</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-583"><a href="#SubprocessWorker-583"><span class="linenos">583</span></a>            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker-584"><a href="#SubprocessWorker-584"><span class="linenos">584</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-585"><a href="#SubprocessWorker-585"><span class="linenos">585</span></a>            <span class="k">except</span> <span class="n">Full</span><span class="p">:</span>
</span><span id="SubprocessWorker-586"><a href="#SubprocessWorker-586"><span class="linenos">586</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="n">block</span>
</span><span id="SubprocessWorker-587"><a href="#SubprocessWorker-587"><span class="linenos">587</span></a>            
</span><span id="SubprocessWorker-588"><a href="#SubprocessWorker-588"><span class="linenos">588</span></a>            <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker-589"><a href="#SubprocessWorker-589"><span class="linenos">589</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker-590"><a href="#SubprocessWorker-590"><span class="linenos">590</span></a>                <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="SubprocessWorker-591"><a href="#SubprocessWorker-591"><span class="linenos">591</span></a>
</span><span id="SubprocessWorker-592"><a href="#SubprocessWorker-592"><span class="linenos">592</span></a>    <span class="k">def</span> <span class="nf">is_input_queue_is_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker-593"><a href="#SubprocessWorker-593"><span class="linenos">593</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-594"><a href="#SubprocessWorker-594"><span class="linenos">594</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker-595"><a href="#SubprocessWorker-595"><span class="linenos">595</span></a>
</span><span id="SubprocessWorker-596"><a href="#SubprocessWorker-596"><span class="linenos">596</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="SubprocessWorker-597"><a href="#SubprocessWorker-597"><span class="linenos">597</span></a>        
</span><span id="SubprocessWorker-598"><a href="#SubprocessWorker-598"><span class="linenos">598</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-599"><a href="#SubprocessWorker-599"><span class="linenos">599</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-600"><a href="#SubprocessWorker-600"><span class="linenos">600</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-601"><a href="#SubprocessWorker-601"><span class="linenos">601</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-602"><a href="#SubprocessWorker-602"><span class="linenos">602</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-603"><a href="#SubprocessWorker-603"><span class="linenos">603</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-604"><a href="#SubprocessWorker-604"><span class="linenos">604</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-605"><a href="#SubprocessWorker-605"><span class="linenos">605</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker-606"><a href="#SubprocessWorker-606"><span class="linenos">606</span></a>
</span><span id="SubprocessWorker-607"><a href="#SubprocessWorker-607"><span class="linenos">607</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-608"><a href="#SubprocessWorker-608"><span class="linenos">608</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">)</span>
</span><span id="SubprocessWorker-609"><a href="#SubprocessWorker-609"><span class="linenos">609</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-610"><a href="#SubprocessWorker-610"><span class="linenos">610</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
</span><span id="SubprocessWorker-611"><a href="#SubprocessWorker-611"><span class="linenos">611</span></a>
</span><span id="SubprocessWorker-612"><a href="#SubprocessWorker-612"><span class="linenos">612</span></a>            <span class="c1"># result = self.queue_to_subprocess.empty()</span>
</span><span id="SubprocessWorker-613"><a href="#SubprocessWorker-613"><span class="linenos">613</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker-614"><a href="#SubprocessWorker-614"><span class="linenos">614</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-615"><a href="#SubprocessWorker-615"><span class="linenos">615</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker-616"><a href="#SubprocessWorker-616"><span class="linenos">616</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-617"><a href="#SubprocessWorker-617"><span class="linenos">617</span></a>        
</span><span id="SubprocessWorker-618"><a href="#SubprocessWorker-618"><span class="linenos">618</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker-619"><a href="#SubprocessWorker-619"><span class="linenos">619</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker-620"><a href="#SubprocessWorker-620"><span class="linenos">620</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="SubprocessWorker-621"><a href="#SubprocessWorker-621"><span class="linenos">621</span></a>
</span><span id="SubprocessWorker-622"><a href="#SubprocessWorker-622"><span class="linenos">622</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="SubprocessWorker-623"><a href="#SubprocessWorker-623"><span class="linenos">623</span></a>
</span><span id="SubprocessWorker-624"><a href="#SubprocessWorker-624"><span class="linenos">624</span></a>    <span class="k">def</span> <span class="nf">wait_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="SubprocessWorker-625"><a href="#SubprocessWorker-625"><span class="linenos">625</span></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="SubprocessWorker-626"><a href="#SubprocessWorker-626"><span class="linenos">626</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_input_queue_is_empty</span><span class="p">():</span>
</span><span id="SubprocessWorker-627"><a href="#SubprocessWorker-627"><span class="linenos">627</span></a>            <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-628"><a href="#SubprocessWorker-628"><span class="linenos">628</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="SubprocessWorker-629"><a href="#SubprocessWorker-629"><span class="linenos">629</span></a>                    <span class="k">break</span>
</span><span id="SubprocessWorker-630"><a href="#SubprocessWorker-630"><span class="linenos">630</span></a>
</span><span id="SubprocessWorker-631"><a href="#SubprocessWorker-631"><span class="linenos">631</span></a>    <span class="k">def</span> <span class="nf">get_answer_from_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker-632"><a href="#SubprocessWorker-632"><span class="linenos">632</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="SubprocessWorker-633"><a href="#SubprocessWorker-633"><span class="linenos">633</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="SubprocessWorker-634"><a href="#SubprocessWorker-634"><span class="linenos">634</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="SubprocessWorker-635"><a href="#SubprocessWorker-635"><span class="linenos">635</span></a><span class="sd">        Will raise Empty() in non-blocking mode when queue is empty</span>
</span><span id="SubprocessWorker-636"><a href="#SubprocessWorker-636"><span class="linenos">636</span></a><span class="sd">        :param block:</span>
</span><span id="SubprocessWorker-637"><a href="#SubprocessWorker-637"><span class="linenos">637</span></a><span class="sd">        :param time_out:  None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorker-638"><a href="#SubprocessWorker-638"><span class="linenos">638</span></a><span class="sd">        :return:</span>
</span><span id="SubprocessWorker-639"><a href="#SubprocessWorker-639"><span class="linenos">639</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker-640"><a href="#SubprocessWorker-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker-641"><a href="#SubprocessWorker-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker-642"><a href="#SubprocessWorker-642"><span class="linenos">642</span></a>
</span><span id="SubprocessWorker-643"><a href="#SubprocessWorker-643"><span class="linenos">643</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker-644"><a href="#SubprocessWorker-644"><span class="linenos">644</span></a>        
</span><span id="SubprocessWorker-645"><a href="#SubprocessWorker-645"><span class="linenos">645</span></a>        <span class="n">subprocess_continue_working</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-646"><a href="#SubprocessWorker-646"><span class="linenos">646</span></a>        <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker-647"><a href="#SubprocessWorker-647"><span class="linenos">647</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker-648"><a href="#SubprocessWorker-648"><span class="linenos">648</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker-649"><a href="#SubprocessWorker-649"><span class="linenos">649</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-650"><a href="#SubprocessWorker-650"><span class="linenos">650</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-651"><a href="#SubprocessWorker-651"><span class="linenos">651</span></a>                <span class="k">if</span> <span class="n">block</span><span class="p">:</span>
</span><span id="SubprocessWorker-652"><a href="#SubprocessWorker-652"><span class="linenos">652</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker-653"><a href="#SubprocessWorker-653"><span class="linenos">653</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker-654"><a href="#SubprocessWorker-654"><span class="linenos">654</span></a>                    <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker-655"><a href="#SubprocessWorker-655"><span class="linenos">655</span></a>                    <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker-656"><a href="#SubprocessWorker-656"><span class="linenos">656</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-657"><a href="#SubprocessWorker-657"><span class="linenos">657</span></a>                    <span class="k">if</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">):</span>
</span><span id="SubprocessWorker-658"><a href="#SubprocessWorker-658"><span class="linenos">658</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker-659"><a href="#SubprocessWorker-659"><span class="linenos">659</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker-660"><a href="#SubprocessWorker-660"><span class="linenos">660</span></a>                        <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker-661"><a href="#SubprocessWorker-661"><span class="linenos">661</span></a>                        <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker-662"><a href="#SubprocessWorker-662"><span class="linenos">662</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker-663"><a href="#SubprocessWorker-663"><span class="linenos">663</span></a>                        <span class="k">raise</span> <span class="n">Empty</span><span class="p">()</span>
</span><span id="SubprocessWorker-664"><a href="#SubprocessWorker-664"><span class="linenos">664</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker-665"><a href="#SubprocessWorker-665"><span class="linenos">665</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker-666"><a href="#SubprocessWorker-666"><span class="linenos">666</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_reading_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker-667"><a href="#SubprocessWorker-667"><span class="linenos">667</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker-668"><a href="#SubprocessWorker-668"><span class="linenos">668</span></a>                <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker-669"><a href="#SubprocessWorker-669"><span class="linenos">669</span></a>                <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker-670"><a href="#SubprocessWorker-670"><span class="linenos">670</span></a>            
</span><span id="SubprocessWorker-671"><a href="#SubprocessWorker-671"><span class="linenos">671</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">subprocess_continue_working</span><span class="p">:</span>
</span><span id="SubprocessWorker-672"><a href="#SubprocessWorker-672"><span class="linenos">672</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-673"><a href="#SubprocessWorker-673"><span class="linenos">673</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker-674"><a href="#SubprocessWorker-674"><span class="linenos">674</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-675"><a href="#SubprocessWorker-675"><span class="linenos">675</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker-676"><a href="#SubprocessWorker-676"><span class="linenos">676</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker-677"><a href="#SubprocessWorker-677"><span class="linenos">677</span></a>        
</span><span id="SubprocessWorker-678"><a href="#SubprocessWorker-678"><span class="linenos">678</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker-679"><a href="#SubprocessWorker-679"><span class="linenos">679</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker-680"><a href="#SubprocessWorker-680"><span class="linenos">680</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="SubprocessWorker-681"><a href="#SubprocessWorker-681"><span class="linenos">681</span></a>        
</span><span id="SubprocessWorker-682"><a href="#SubprocessWorker-682"><span class="linenos">682</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker-683"><a href="#SubprocessWorker-683"><span class="linenos">683</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker-684"><a href="#SubprocessWorker-684"><span class="linenos">684</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker-685"><a href="#SubprocessWorker-685"><span class="linenos">685</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">exception</span><span class="p">)</span>
</span><span id="SubprocessWorker-686"><a href="#SubprocessWorker-686"><span class="linenos">686</span></a>            <span class="c1"># print(self.settings.process_name)</span>
</span><span id="SubprocessWorker-687"><a href="#SubprocessWorker-687"><span class="linenos">687</span></a>            <span class="c1"># print(result)</span>
</span><span id="SubprocessWorker-688"><a href="#SubprocessWorker-688"><span class="linenos">688</span></a>            <span class="c1"># print(exception)</span>
</span><span id="SubprocessWorker-689"><a href="#SubprocessWorker-689"><span class="linenos">689</span></a>            <span class="c1"># print()</span>
</span><span id="SubprocessWorker-690"><a href="#SubprocessWorker-690"><span class="linenos">690</span></a>            <span class="c1"># print(&#39; &lt;&lt;&lt; SUBPROCESS EXCEPTION:&#39;)</span>
</span><span id="SubprocessWorker-691"><a href="#SubprocessWorker-691"><span class="linenos">691</span></a>            <span class="c1"># trace = &#39;&#39;</span>
</span><span id="SubprocessWorker-692"><a href="#SubprocessWorker-692"><span class="linenos">692</span></a>            <span class="c1"># for line in exception[2]:</span>
</span><span id="SubprocessWorker-693"><a href="#SubprocessWorker-693"><span class="linenos">693</span></a>            <span class="c1">#     trace += line</span>
</span><span id="SubprocessWorker-694"><a href="#SubprocessWorker-694"><span class="linenos">694</span></a>            <span class="c1"># print(trace, file=sys.stderr)</span>
</span><span id="SubprocessWorker-695"><a href="#SubprocessWorker-695"><span class="linenos">695</span></a>            <span class="c1"># print(exception[0])</span>
</span><span id="SubprocessWorker-696"><a href="#SubprocessWorker-696"><span class="linenos">696</span></a>            <span class="c1"># print(exception[1])</span>
</span><span id="SubprocessWorker-697"><a href="#SubprocessWorker-697"><span class="linenos">697</span></a>            <span class="c1"># print(&#39; &gt;&gt;&gt;&#39;)</span>
</span><span id="SubprocessWorker-698"><a href="#SubprocessWorker-698"><span class="linenos">698</span></a>
</span><span id="SubprocessWorker-699"><a href="#SubprocessWorker-699"><span class="linenos">699</span></a>            <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_value</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="SubprocessWorker-700"><a href="#SubprocessWorker-700"><span class="linenos">700</span></a>            <span class="k">raise</span> <span class="n">exc_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="SubprocessWorker-701"><a href="#SubprocessWorker-701"><span class="linenos">701</span></a>        
</span><span id="SubprocessWorker-702"><a href="#SubprocessWorker-702"><span class="linenos">702</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="SubprocessWorker.__init__" class="classattr">
                                        <input id="SubprocessWorker.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">SubprocessWorker</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">settings</span><span class="p">:</span> <span class="n"><a href="#SubprocessWorkerSettings">SubprocessWorkerSettings</a></span></span>)</span>

                <label class="view-source-button" for="SubprocessWorker.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.__init__-137"><a href="#SubprocessWorker.__init__-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span><span class="p">):</span>
</span><span id="SubprocessWorker.__init__-138"><a href="#SubprocessWorker.__init__-138"><span class="linenos">138</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot; </span>
</span><span id="SubprocessWorker.__init__-139"><a href="#SubprocessWorker.__init__-139"><span class="linenos">139</span></a><span class="sd">        :param settings: SubprocessWorkerSettings(); you should use copy.copy(SubprocessWorkerSettings(...)) by your </span>
</span><span id="SubprocessWorker.__init__-140"><a href="#SubprocessWorker.__init__-140"><span class="linenos">140</span></a><span class="sd">            self if you want</span>
</span><span id="SubprocessWorker.__init__-141"><a href="#SubprocessWorker.__init__-141"><span class="linenos">141</span></a><span class="sd">        :return: </span>
</span><span id="SubprocessWorker.__init__-142"><a href="#SubprocessWorker.__init__-142"><span class="linenos">142</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker.__init__-143"><a href="#SubprocessWorker.__init__-143"><span class="linenos">143</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="SubprocessWorker.__init__-144"><a href="#SubprocessWorker.__init__-144"><span class="linenos">144</span></a>        
</span><span id="SubprocessWorker.__init__-145"><a href="#SubprocessWorker.__init__-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="p">:</span> <span class="n">SubprocessWorkerSettings</span> <span class="o">=</span> <span class="n">settings</span>
</span><span id="SubprocessWorker.__init__-146"><a href="#SubprocessWorker.__init__-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">check</span><span class="p">()</span>
</span><span id="SubprocessWorker.__init__-147"><a href="#SubprocessWorker.__init__-147"><span class="linenos">147</span></a>
</span><span id="SubprocessWorker.__init__-148"><a href="#SubprocessWorker.__init__-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_shelf</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.__init__-149"><a href="#SubprocessWorker.__init__-149"><span class="linenos">149</span></a>
</span><span id="SubprocessWorker.__init__-150"><a href="#SubprocessWorker.__init__-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.__init__-151"><a href="#SubprocessWorker.__init__-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.__init__-152"><a href="#SubprocessWorker.__init__-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker.__init__-153"><a href="#SubprocessWorker.__init__-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker.__init__-154"><a href="#SubprocessWorker.__init__-154"><span class="linenos">154</span></a>
</span><span id="SubprocessWorker.__init__-155"><a href="#SubprocessWorker.__init__-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">list_of_subprocess_input_data</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="SubprocessWorker.__init__-156"><a href="#SubprocessWorker.__init__-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_sum</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker.__init__-157"><a href="#SubprocessWorker.__init__-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="SubprocessWorker.__init__-158"><a href="#SubprocessWorker.__init__-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_size_print_counter_limit</span> <span class="o">=</span> <span class="mi">500</span>
</span><span id="SubprocessWorker.__init__-159"><a href="#SubprocessWorker.__init__-159"><span class="linenos">159</span></a>        <span class="c1"># self.last_log_print_time = time.time()</span>
</span><span id="SubprocessWorker.__init__-160"><a href="#SubprocessWorker.__init__-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.__init__-161"><a href="#SubprocessWorker.__init__-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_queue_average_size_trigger</span> <span class="o">=</span> <span class="n">FrontTriggerableVariable</span><span class="p">(</span>
</span><span id="SubprocessWorker.__init__-162"><a href="#SubprocessWorker.__init__-162"><span class="linenos">162</span></a>            <span class="n">FrontTriggerableVariableType</span><span class="o">.</span><span class="n">bigger_or_equal</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">input_queue_average_size_trigger_limit</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>:param settings: SubprocessWorkerSettings(); you should use copy.copy(SubprocessWorkerSettings(...)) by your 
    self if you want
:return:</p>
</div>


                            </div>
                            <div id="SubprocessWorker.settings" class="classattr">
                                <div class="attr variable">
            <span class="name">settings</span><span class="annotation">: <a href="#SubprocessWorkerSettings">SubprocessWorkerSettings</a></span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.settings"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.data_shelf" class="classattr">
                                <div class="attr variable">
            <span class="name">data_shelf</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.data_shelf"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.subprocess_was_initiated" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_was_initiated</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.subprocess_was_initiated"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.subprocess" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.subprocess"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.queue_to_subprocess" class="classattr">
                                <div class="attr variable">
            <span class="name">queue_to_subprocess</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.queue_to_subprocess"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.queue_from_subprocess" class="classattr">
                                <div class="attr variable">
            <span class="name">queue_from_subprocess</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.queue_from_subprocess"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.list_of_subprocess_input_data" class="classattr">
                                <div class="attr variable">
            <span class="name">list_of_subprocess_input_data</span><span class="annotation">: List</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.list_of_subprocess_input_data"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.input_size_print_sum" class="classattr">
                                <div class="attr variable">
            <span class="name">input_size_print_sum</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.input_size_print_sum"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.input_size_print_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">input_size_print_counter</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.input_size_print_counter"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.input_size_print_counter_limit" class="classattr">
                                <div class="attr variable">
            <span class="name">input_size_print_counter_limit</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.input_size_print_counter_limit"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.subprocess_readyness_indicated" class="classattr">
                                <div class="attr variable">
            <span class="name">subprocess_readyness_indicated</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.subprocess_readyness_indicated"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.input_queue_average_size_trigger" class="classattr">
                                <div class="attr variable">
            <span class="name">input_queue_average_size_trigger</span>

        
    </div>
    <a class="headerlink" href="#SubprocessWorker.input_queue_average_size_trigger"></a>
    
    

                            </div>
                            <div id="SubprocessWorker.start" class="classattr">
                                        <input id="SubprocessWorker.start-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">wait_for_process_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.start-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.start"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.start-451"><a href="#SubprocessWorker.start-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker.start-452"><a href="#SubprocessWorker.start-452"><span class="linenos">452</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-453"><a href="#SubprocessWorker.start-453"><span class="linenos">453</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-454"><a href="#SubprocessWorker.start-454"><span class="linenos">454</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-455"><a href="#SubprocessWorker.start-455"><span class="linenos">455</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-456"><a href="#SubprocessWorker.start-456"><span class="linenos">456</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-457"><a href="#SubprocessWorker.start-457"><span class="linenos">457</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-458"><a href="#SubprocessWorker.start-458"><span class="linenos">458</span></a>
</span><span id="SubprocessWorker.start-459"><a href="#SubprocessWorker.start-459"><span class="linenos">459</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-460"><a href="#SubprocessWorker.start-460"><span class="linenos">460</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-461"><a href="#SubprocessWorker.start-461"><span class="linenos">461</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-462"><a href="#SubprocessWorker.start-462"><span class="linenos">462</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-463"><a href="#SubprocessWorker.start-463"><span class="linenos">463</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span> <span class="o">=</span> <span class="n">Queue</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-464"><a href="#SubprocessWorker.start-464"><span class="linenos">464</span></a>
</span><span id="SubprocessWorker.start-465"><a href="#SubprocessWorker.start-465"><span class="linenos">465</span></a>            <span class="n">target</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.start-466"><a href="#SubprocessWorker.start-466"><span class="linenos">466</span></a>            <span class="n">arguments</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.start-467"><a href="#SubprocessWorker.start-467"><span class="linenos">467</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">profile</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-468"><a href="#SubprocessWorker.start-468"><span class="linenos">468</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="n">_subprocess_wrapper_profile</span>
</span><span id="SubprocessWorker.start-469"><a href="#SubprocessWorker.start-469"><span class="linenos">469</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="p">,)</span>
</span><span id="SubprocessWorker.start-470"><a href="#SubprocessWorker.start-470"><span class="linenos">470</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-471"><a href="#SubprocessWorker.start-471"><span class="linenos">471</span></a>                <span class="n">target</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subprocess_wrapper</span>
</span><span id="SubprocessWorker.start-472"><a href="#SubprocessWorker.start-472"><span class="linenos">472</span></a>                <span class="n">arguments</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-473"><a href="#SubprocessWorker.start-473"><span class="linenos">473</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.start-474"><a href="#SubprocessWorker.start-474"><span class="linenos">474</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">need_multithreading</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-475"><a href="#SubprocessWorker.start-475"><span class="linenos">475</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker.start-476"><a href="#SubprocessWorker.start-476"><span class="linenos">476</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-477"><a href="#SubprocessWorker.start-477"><span class="linenos">477</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span> <span class="o">=</span> <span class="n">Process</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">target</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span> <span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker.start-478"><a href="#SubprocessWorker.start-478"><span class="linenos">478</span></a>            
</span><span id="SubprocessWorker.start-479"><a href="#SubprocessWorker.start-479"><span class="linenos">479</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="SubprocessWorker.start-480"><a href="#SubprocessWorker.start-480"><span class="linenos">480</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.start-481"><a href="#SubprocessWorker.start-481"><span class="linenos">481</span></a>        
</span><span id="SubprocessWorker.start-482"><a href="#SubprocessWorker.start-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="n">wait_for_process_readyness</span><span class="p">:</span>
</span><span id="SubprocessWorker.start-483"><a href="#SubprocessWorker.start-483"><span class="linenos">483</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="SubprocessWorker.wait_for_subprocess_readines" class="classattr">
                                        <input id="SubprocessWorker.wait_for_subprocess_readines-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_for_subprocess_readines</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.wait_for_subprocess_readines-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.wait_for_subprocess_readines"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.wait_for_subprocess_readines-485"><a href="#SubprocessWorker.wait_for_subprocess_readines-485"><span class="linenos">485</span></a>    <span class="k">def</span> <span class="nf">wait_for_subprocess_readines</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-486"><a href="#SubprocessWorker.wait_for_subprocess_readines-486"><span class="linenos">486</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-487"><a href="#SubprocessWorker.wait_for_subprocess_readines-487"><span class="linenos">487</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-488"><a href="#SubprocessWorker.wait_for_subprocess_readines-488"><span class="linenos">488</span></a>        
</span><span id="SubprocessWorker.wait_for_subprocess_readines-489"><a href="#SubprocessWorker.wait_for_subprocess_readines-489"><span class="linenos">489</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-490"><a href="#SubprocessWorker.wait_for_subprocess_readines-490"><span class="linenos">490</span></a>            <span class="k">return</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-491"><a href="#SubprocessWorker.wait_for_subprocess_readines-491"><span class="linenos">491</span></a>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-492"><a href="#SubprocessWorker.wait_for_subprocess_readines-492"><span class="linenos">492</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">indicate_subprocess_readyness</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-493"><a href="#SubprocessWorker.wait_for_subprocess_readines-493"><span class="linenos">493</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-494"><a href="#SubprocessWorker.wait_for_subprocess_readines-494"><span class="linenos">494</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-495"><a href="#SubprocessWorker.wait_for_subprocess_readines-495"><span class="linenos">495</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-496"><a href="#SubprocessWorker.wait_for_subprocess_readines-496"><span class="linenos">496</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-497"><a href="#SubprocessWorker.wait_for_subprocess_readines-497"><span class="linenos">497</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-498"><a href="#SubprocessWorker.wait_for_subprocess_readines-498"><span class="linenos">498</span></a>                <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-499"><a href="#SubprocessWorker.wait_for_subprocess_readines-499"><span class="linenos">499</span></a>                    <span class="k">raise</span> <span class="n">SubprocessIsNotReadyError</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-500"><a href="#SubprocessWorker.wait_for_subprocess_readines-500"><span class="linenos">500</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-501"><a href="#SubprocessWorker.wait_for_subprocess_readines-501"><span class="linenos">501</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_readyness_indicated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.wait_for_subprocess_readines-502"><a href="#SubprocessWorker.wait_for_subprocess_readines-502"><span class="linenos">502</span></a>                <span class="k">raise</span>
</span></pre></div>


    

                            </div>
                            <div id="SubprocessWorker.stop" class="classattr">
                                        <input id="SubprocessWorker.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.stop-513"><a href="#SubprocessWorker.stop-513"><span class="linenos">513</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker.stop-514"><a href="#SubprocessWorker.stop-514"><span class="linenos">514</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-515"><a href="#SubprocessWorker.stop-515"><span class="linenos">515</span></a>            <span class="k">return</span>
</span><span id="SubprocessWorker.stop-516"><a href="#SubprocessWorker.stop-516"><span class="linenos">516</span></a>        
</span><span id="SubprocessWorker.stop-517"><a href="#SubprocessWorker.stop-517"><span class="linenos">517</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker.stop-518"><a href="#SubprocessWorker.stop-518"><span class="linenos">518</span></a>
</span><span id="SubprocessWorker.stop-519"><a href="#SubprocessWorker.stop-519"><span class="linenos">519</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="SubprocessWorker.stop-520"><a href="#SubprocessWorker.stop-520"><span class="linenos">520</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker.stop-521"><a href="#SubprocessWorker.stop-521"><span class="linenos">521</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="SubprocessWorker.stop-522"><a href="#SubprocessWorker.stop-522"><span class="linenos">522</span></a>
</span><span id="SubprocessWorker.stop-523"><a href="#SubprocessWorker.stop-523"><span class="linenos">523</span></a>        <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.stop-524"><a href="#SubprocessWorker.stop-524"><span class="linenos">524</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-525"><a href="#SubprocessWorker.stop-525"><span class="linenos">525</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker.stop-526"><a href="#SubprocessWorker.stop-526"><span class="linenos">526</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-527"><a href="#SubprocessWorker.stop-527"><span class="linenos">527</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker.stop-528"><a href="#SubprocessWorker.stop-528"><span class="linenos">528</span></a>
</span><span id="SubprocessWorker.stop-529"><a href="#SubprocessWorker.stop-529"><span class="linenos">529</span></a>        <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-530"><a href="#SubprocessWorker.stop-530"><span class="linenos">530</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker.stop-531"><a href="#SubprocessWorker.stop-531"><span class="linenos">531</span></a>        <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-532"><a href="#SubprocessWorker.stop-532"><span class="linenos">532</span></a>            <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker.stop-533"><a href="#SubprocessWorker.stop-533"><span class="linenos">533</span></a>        
</span><span id="SubprocessWorker.stop-534"><a href="#SubprocessWorker.stop-534"><span class="linenos">534</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-535"><a href="#SubprocessWorker.stop-535"><span class="linenos">535</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">get_answer_from_subprocess</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="SubprocessWorker.stop-536"><a href="#SubprocessWorker.stop-536"><span class="linenos">536</span></a>        <span class="k">except</span> <span class="n">Empty</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-537"><a href="#SubprocessWorker.stop-537"><span class="linenos">537</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker.stop-538"><a href="#SubprocessWorker.stop-538"><span class="linenos">538</span></a>        <span class="k">except</span> <span class="n">SubprocessTerminatedError</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-539"><a href="#SubprocessWorker.stop-539"><span class="linenos">539</span></a>            <span class="k">pass</span>
</span><span id="SubprocessWorker.stop-540"><a href="#SubprocessWorker.stop-540"><span class="linenos">540</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="SubprocessWorker.stop-541"><a href="#SubprocessWorker.stop-541"><span class="linenos">541</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_close_connections</span><span class="p">()</span>
</span><span id="SubprocessWorker.stop-542"><a href="#SubprocessWorker.stop-542"><span class="linenos">542</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.stop-543"><a href="#SubprocessWorker.stop-543"><span class="linenos">543</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">subprocess</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="SubprocessWorker.send_data_to_subprocess" class="classattr">
                                        <input id="SubprocessWorker.send_data_to_subprocess-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">send_data_to_subprocess</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">input_data</span>, </span><span class="param"><span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.send_data_to_subprocess-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.send_data_to_subprocess"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.send_data_to_subprocess-550"><a href="#SubprocessWorker.send_data_to_subprocess-550"><span class="linenos">550</span></a>    <span class="k">def</span> <span class="nf">send_data_to_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">input_data</span><span class="p">,</span> <span class="n">block</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-551"><a href="#SubprocessWorker.send_data_to_subprocess-551"><span class="linenos">551</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-552"><a href="#SubprocessWorker.send_data_to_subprocess-552"><span class="linenos">552</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-553"><a href="#SubprocessWorker.send_data_to_subprocess-553"><span class="linenos">553</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-554"><a href="#SubprocessWorker.send_data_to_subprocess-554"><span class="linenos">554</span></a><span class="sd">        :param input_data:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-555"><a href="#SubprocessWorker.send_data_to_subprocess-555"><span class="linenos">555</span></a><span class="sd">        :return:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-556"><a href="#SubprocessWorker.send_data_to_subprocess-556"><span class="linenos">556</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-557"><a href="#SubprocessWorker.send_data_to_subprocess-557"><span class="linenos">557</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-558"><a href="#SubprocessWorker.send_data_to_subprocess-558"><span class="linenos">558</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-559"><a href="#SubprocessWorker.send_data_to_subprocess-559"><span class="linenos">559</span></a>
</span><span id="SubprocessWorker.send_data_to_subprocess-560"><a href="#SubprocessWorker.send_data_to_subprocess-560"><span class="linenos">560</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-561"><a href="#SubprocessWorker.send_data_to_subprocess-561"><span class="linenos">561</span></a>        
</span><span id="SubprocessWorker.send_data_to_subprocess-562"><a href="#SubprocessWorker.send_data_to_subprocess-562"><span class="linenos">562</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="p">(</span><span class="n">input_data</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-563"><a href="#SubprocessWorker.send_data_to_subprocess-563"><span class="linenos">563</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_encode_sendable_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-564"><a href="#SubprocessWorker.send_data_to_subprocess-564"><span class="linenos">564</span></a>        <span class="c1"># data = marshal.dumps(data)</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-565"><a href="#SubprocessWorker.send_data_to_subprocess-565"><span class="linenos">565</span></a>        <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-566"><a href="#SubprocessWorker.send_data_to_subprocess-566"><span class="linenos">566</span></a>        <span class="k">while</span> <span class="n">need_to_retry</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-567"><a href="#SubprocessWorker.send_data_to_subprocess-567"><span class="linenos">567</span></a>            <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-568"><a href="#SubprocessWorker.send_data_to_subprocess-568"><span class="linenos">568</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-569"><a href="#SubprocessWorker.send_data_to_subprocess-569"><span class="linenos">569</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-570"><a href="#SubprocessWorker.send_data_to_subprocess-570"><span class="linenos">570</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-571"><a href="#SubprocessWorker.send_data_to_subprocess-571"><span class="linenos">571</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-572"><a href="#SubprocessWorker.send_data_to_subprocess-572"><span class="linenos">572</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-573"><a href="#SubprocessWorker.send_data_to_subprocess-573"><span class="linenos">573</span></a>                    <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-574"><a href="#SubprocessWorker.send_data_to_subprocess-574"><span class="linenos">574</span></a>
</span><span id="SubprocessWorker.send_data_to_subprocess-575"><a href="#SubprocessWorker.send_data_to_subprocess-575"><span class="linenos">575</span></a>                <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-576"><a href="#SubprocessWorker.send_data_to_subprocess-576"><span class="linenos">576</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">send_bytes</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-577"><a href="#SubprocessWorker.send_data_to_subprocess-577"><span class="linenos">577</span></a>                <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-578"><a href="#SubprocessWorker.send_data_to_subprocess-578"><span class="linenos">578</span></a>                    <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_writing_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-579"><a href="#SubprocessWorker.send_data_to_subprocess-579"><span class="linenos">579</span></a>                
</span><span id="SubprocessWorker.send_data_to_subprocess-580"><a href="#SubprocessWorker.send_data_to_subprocess-580"><span class="linenos">580</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-581"><a href="#SubprocessWorker.send_data_to_subprocess-581"><span class="linenos">581</span></a>            <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-582"><a href="#SubprocessWorker.send_data_to_subprocess-582"><span class="linenos">582</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-583"><a href="#SubprocessWorker.send_data_to_subprocess-583"><span class="linenos">583</span></a>            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-584"><a href="#SubprocessWorker.send_data_to_subprocess-584"><span class="linenos">584</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-585"><a href="#SubprocessWorker.send_data_to_subprocess-585"><span class="linenos">585</span></a>            <span class="k">except</span> <span class="n">Full</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-586"><a href="#SubprocessWorker.send_data_to_subprocess-586"><span class="linenos">586</span></a>                <span class="n">need_to_retry</span> <span class="o">=</span> <span class="n">block</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-587"><a href="#SubprocessWorker.send_data_to_subprocess-587"><span class="linenos">587</span></a>            
</span><span id="SubprocessWorker.send_data_to_subprocess-588"><a href="#SubprocessWorker.send_data_to_subprocess-588"><span class="linenos">588</span></a>            <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-589"><a href="#SubprocessWorker.send_data_to_subprocess-589"><span class="linenos">589</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker.send_data_to_subprocess-590"><a href="#SubprocessWorker.send_data_to_subprocess-590"><span class="linenos">590</span></a>                <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span></pre></div>


            <div class="docstring"><p>If (<a href="#Transport.pipe">Transport.pipe</a> == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on
    the OS) may raise a ValueError exception
:param input_data:
:return:</p>
</div>


                            </div>
                            <div id="SubprocessWorker.is_input_queue_is_empty" class="classattr">
                                        <input id="SubprocessWorker.is_input_queue_is_empty-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_input_queue_is_empty</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.is_input_queue_is_empty-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.is_input_queue_is_empty"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.is_input_queue_is_empty-592"><a href="#SubprocessWorker.is_input_queue_is_empty-592"><span class="linenos">592</span></a>    <span class="k">def</span> <span class="nf">is_input_queue_is_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-593"><a href="#SubprocessWorker.is_input_queue_is_empty-593"><span class="linenos">593</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-594"><a href="#SubprocessWorker.is_input_queue_is_empty-594"><span class="linenos">594</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-595"><a href="#SubprocessWorker.is_input_queue_is_empty-595"><span class="linenos">595</span></a>
</span><span id="SubprocessWorker.is_input_queue_is_empty-596"><a href="#SubprocessWorker.is_input_queue_is_empty-596"><span class="linenos">596</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-597"><a href="#SubprocessWorker.is_input_queue_is_empty-597"><span class="linenos">597</span></a>        
</span><span id="SubprocessWorker.is_input_queue_is_empty-598"><a href="#SubprocessWorker.is_input_queue_is_empty-598"><span class="linenos">598</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-599"><a href="#SubprocessWorker.is_input_queue_is_empty-599"><span class="linenos">599</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-600"><a href="#SubprocessWorker.is_input_queue_is_empty-600"><span class="linenos">600</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-601"><a href="#SubprocessWorker.is_input_queue_is_empty-601"><span class="linenos">601</span></a>            <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-602"><a href="#SubprocessWorker.is_input_queue_is_empty-602"><span class="linenos">602</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-603"><a href="#SubprocessWorker.is_input_queue_is_empty-603"><span class="linenos">603</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-604"><a href="#SubprocessWorker.is_input_queue_is_empty-604"><span class="linenos">604</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-605"><a href="#SubprocessWorker.is_input_queue_is_empty-605"><span class="linenos">605</span></a>                <span class="n">output_to_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_to_subprocess</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-606"><a href="#SubprocessWorker.is_input_queue_is_empty-606"><span class="linenos">606</span></a>
</span><span id="SubprocessWorker.is_input_queue_is_empty-607"><a href="#SubprocessWorker.is_input_queue_is_empty-607"><span class="linenos">607</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-608"><a href="#SubprocessWorker.is_input_queue_is_empty-608"><span class="linenos">608</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">)</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-609"><a href="#SubprocessWorker.is_input_queue_is_empty-609"><span class="linenos">609</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-610"><a href="#SubprocessWorker.is_input_queue_is_empty-610"><span class="linenos">610</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">output_to_subprocess_queue</span><span class="o">.</span><span class="n">empty</span><span class="p">()</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-611"><a href="#SubprocessWorker.is_input_queue_is_empty-611"><span class="linenos">611</span></a>
</span><span id="SubprocessWorker.is_input_queue_is_empty-612"><a href="#SubprocessWorker.is_input_queue_is_empty-612"><span class="linenos">612</span></a>            <span class="c1"># result = self.queue_to_subprocess.empty()</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-613"><a href="#SubprocessWorker.is_input_queue_is_empty-613"><span class="linenos">613</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-614"><a href="#SubprocessWorker.is_input_queue_is_empty-614"><span class="linenos">614</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-615"><a href="#SubprocessWorker.is_input_queue_is_empty-615"><span class="linenos">615</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-616"><a href="#SubprocessWorker.is_input_queue_is_empty-616"><span class="linenos">616</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-617"><a href="#SubprocessWorker.is_input_queue_is_empty-617"><span class="linenos">617</span></a>        
</span><span id="SubprocessWorker.is_input_queue_is_empty-618"><a href="#SubprocessWorker.is_input_queue_is_empty-618"><span class="linenos">618</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-619"><a href="#SubprocessWorker.is_input_queue_is_empty-619"><span class="linenos">619</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-620"><a href="#SubprocessWorker.is_input_queue_is_empty-620"><span class="linenos">620</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="SubprocessWorker.is_input_queue_is_empty-621"><a href="#SubprocessWorker.is_input_queue_is_empty-621"><span class="linenos">621</span></a>
</span><span id="SubprocessWorker.is_input_queue_is_empty-622"><a href="#SubprocessWorker.is_input_queue_is_empty-622"><span class="linenos">622</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="SubprocessWorker.wait_for_data" class="classattr">
                                        <input id="SubprocessWorker.wait_for_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wait_for_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.wait_for_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.wait_for_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.wait_for_data-624"><a href="#SubprocessWorker.wait_for_data-624"><span class="linenos">624</span></a>    <span class="k">def</span> <span class="nf">wait_for_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="SubprocessWorker.wait_for_data-625"><a href="#SubprocessWorker.wait_for_data-625"><span class="linenos">625</span></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="SubprocessWorker.wait_for_data-626"><a href="#SubprocessWorker.wait_for_data-626"><span class="linenos">626</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_input_queue_is_empty</span><span class="p">():</span>
</span><span id="SubprocessWorker.wait_for_data-627"><a href="#SubprocessWorker.wait_for_data-627"><span class="linenos">627</span></a>            <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_data-628"><a href="#SubprocessWorker.wait_for_data-628"><span class="linenos">628</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="SubprocessWorker.wait_for_data-629"><a href="#SubprocessWorker.wait_for_data-629"><span class="linenos">629</span></a>                    <span class="k">break</span>
</span></pre></div>


    

                            </div>
                            <div id="SubprocessWorker.get_answer_from_subprocess" class="classattr">
                                        <input id="SubprocessWorker.get_answer_from_subprocess-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_answer_from_subprocess</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">block</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="SubprocessWorker.get_answer_from_subprocess-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#SubprocessWorker.get_answer_from_subprocess"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="SubprocessWorker.get_answer_from_subprocess-631"><a href="#SubprocessWorker.get_answer_from_subprocess-631"><span class="linenos">631</span></a>    <span class="k">def</span> <span class="nf">get_answer_from_subprocess</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-632"><a href="#SubprocessWorker.get_answer_from_subprocess-632"><span class="linenos">632</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-633"><a href="#SubprocessWorker.get_answer_from_subprocess-633"><span class="linenos">633</span></a><span class="sd">        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-634"><a href="#SubprocessWorker.get_answer_from_subprocess-634"><span class="linenos">634</span></a><span class="sd">            the OS) may raise a ValueError exception</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-635"><a href="#SubprocessWorker.get_answer_from_subprocess-635"><span class="linenos">635</span></a><span class="sd">        Will raise Empty() in non-blocking mode when queue is empty</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-636"><a href="#SubprocessWorker.get_answer_from_subprocess-636"><span class="linenos">636</span></a><span class="sd">        :param block:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-637"><a href="#SubprocessWorker.get_answer_from_subprocess-637"><span class="linenos">637</span></a><span class="sd">        :param time_out:  None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-638"><a href="#SubprocessWorker.get_answer_from_subprocess-638"><span class="linenos">638</span></a><span class="sd">        :return:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-639"><a href="#SubprocessWorker.get_answer_from_subprocess-639"><span class="linenos">639</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-640"><a href="#SubprocessWorker.get_answer_from_subprocess-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">subprocess_was_initiated</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-641"><a href="#SubprocessWorker.get_answer_from_subprocess-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="n">SubprocessIsNotInitiatedError</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-642"><a href="#SubprocessWorker.get_answer_from_subprocess-642"><span class="linenos">642</span></a>
</span><span id="SubprocessWorker.get_answer_from_subprocess-643"><a href="#SubprocessWorker.get_answer_from_subprocess-643"><span class="linenos">643</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait_for_subprocess_readines</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-644"><a href="#SubprocessWorker.get_answer_from_subprocess-644"><span class="linenos">644</span></a>        
</span><span id="SubprocessWorker.get_answer_from_subprocess-645"><a href="#SubprocessWorker.get_answer_from_subprocess-645"><span class="linenos">645</span></a>        <span class="n">subprocess_continue_working</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-646"><a href="#SubprocessWorker.get_answer_from_subprocess-646"><span class="linenos">646</span></a>        <span class="n">answer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-647"><a href="#SubprocessWorker.get_answer_from_subprocess-647"><span class="linenos">647</span></a>        <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-648"><a href="#SubprocessWorker.get_answer_from_subprocess-648"><span class="linenos">648</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-649"><a href="#SubprocessWorker.get_answer_from_subprocess-649"><span class="linenos">649</span></a>            <span class="k">if</span> <span class="n">Transport</span><span class="o">.</span><span class="n">pipe</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-650"><a href="#SubprocessWorker.get_answer_from_subprocess-650"><span class="linenos">650</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-651"><a href="#SubprocessWorker.get_answer_from_subprocess-651"><span class="linenos">651</span></a>                <span class="k">if</span> <span class="n">block</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-652"><a href="#SubprocessWorker.get_answer_from_subprocess-652"><span class="linenos">652</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-653"><a href="#SubprocessWorker.get_answer_from_subprocess-653"><span class="linenos">653</span></a>                    <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-654"><a href="#SubprocessWorker.get_answer_from_subprocess-654"><span class="linenos">654</span></a>                    <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-655"><a href="#SubprocessWorker.get_answer_from_subprocess-655"><span class="linenos">655</span></a>                    <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-656"><a href="#SubprocessWorker.get_answer_from_subprocess-656"><span class="linenos">656</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-657"><a href="#SubprocessWorker.get_answer_from_subprocess-657"><span class="linenos">657</span></a>                    <span class="k">if</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">poll</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mf">0.0</span><span class="p">):</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-658"><a href="#SubprocessWorker.get_answer_from_subprocess-658"><span class="linenos">658</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">recv_bytes</span><span class="p">()</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-659"><a href="#SubprocessWorker.get_answer_from_subprocess-659"><span class="linenos">659</span></a>                        <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-660"><a href="#SubprocessWorker.get_answer_from_subprocess-660"><span class="linenos">660</span></a>                        <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-661"><a href="#SubprocessWorker.get_answer_from_subprocess-661"><span class="linenos">661</span></a>                        <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-662"><a href="#SubprocessWorker.get_answer_from_subprocess-662"><span class="linenos">662</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-663"><a href="#SubprocessWorker.get_answer_from_subprocess-663"><span class="linenos">663</span></a>                        <span class="k">raise</span> <span class="n">Empty</span><span class="p">()</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-664"><a href="#SubprocessWorker.get_answer_from_subprocess-664"><span class="linenos">664</span></a>            <span class="k">elif</span> <span class="n">Transport</span><span class="o">.</span><span class="n">queue</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">transport</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-665"><a href="#SubprocessWorker.get_answer_from_subprocess-665"><span class="linenos">665</span></a>                <span class="n">input_from_subprocess_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">queue_from_subprocess</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-666"><a href="#SubprocessWorker.get_answer_from_subprocess-666"><span class="linenos">666</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="n">input_from_subprocess_queue</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">block</span><span class="o">=</span><span class="n">block</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">subprocess_reading_timeout</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-667"><a href="#SubprocessWorker.get_answer_from_subprocess-667"><span class="linenos">667</span></a>                <span class="n">subprocess_answer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_decode_sendable_data</span><span class="p">(</span><span class="n">subprocess_answer</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-668"><a href="#SubprocessWorker.get_answer_from_subprocess-668"><span class="linenos">668</span></a>                <span class="c1"># subprocess_answer = marshal.loads(subprocess_answer)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-669"><a href="#SubprocessWorker.get_answer_from_subprocess-669"><span class="linenos">669</span></a>                <span class="n">subprocess_continue_working</span><span class="p">,</span> <span class="n">answer</span> <span class="o">=</span> <span class="n">subprocess_answer</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-670"><a href="#SubprocessWorker.get_answer_from_subprocess-670"><span class="linenos">670</span></a>            
</span><span id="SubprocessWorker.get_answer_from_subprocess-671"><a href="#SubprocessWorker.get_answer_from_subprocess-671"><span class="linenos">671</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">subprocess_continue_working</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-672"><a href="#SubprocessWorker.get_answer_from_subprocess-672"><span class="linenos">672</span></a>                <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-673"><a href="#SubprocessWorker.get_answer_from_subprocess-673"><span class="linenos">673</span></a>        <span class="k">except</span> <span class="ne">OSError</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-674"><a href="#SubprocessWorker.get_answer_from_subprocess-674"><span class="linenos">674</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-675"><a href="#SubprocessWorker.get_answer_from_subprocess-675"><span class="linenos">675</span></a>        <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-676"><a href="#SubprocessWorker.get_answer_from_subprocess-676"><span class="linenos">676</span></a>            <span class="n">subprocess_disconnected_or_terminated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-677"><a href="#SubprocessWorker.get_answer_from_subprocess-677"><span class="linenos">677</span></a>        
</span><span id="SubprocessWorker.get_answer_from_subprocess-678"><a href="#SubprocessWorker.get_answer_from_subprocess-678"><span class="linenos">678</span></a>        <span class="k">if</span> <span class="n">subprocess_disconnected_or_terminated</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-679"><a href="#SubprocessWorker.get_answer_from_subprocess-679"><span class="linenos">679</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_invalidate</span><span class="p">()</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-680"><a href="#SubprocessWorker.get_answer_from_subprocess-680"><span class="linenos">680</span></a>            <span class="k">raise</span> <span class="n">SubprocessTerminatedError</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-681"><a href="#SubprocessWorker.get_answer_from_subprocess-681"><span class="linenos">681</span></a>        
</span><span id="SubprocessWorker.get_answer_from_subprocess-682"><a href="#SubprocessWorker.get_answer_from_subprocess-682"><span class="linenos">682</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-683"><a href="#SubprocessWorker.get_answer_from_subprocess-683"><span class="linenos">683</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">answer</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-684"><a href="#SubprocessWorker.get_answer_from_subprocess-684"><span class="linenos">684</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-685"><a href="#SubprocessWorker.get_answer_from_subprocess-685"><span class="linenos">685</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">exception</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-686"><a href="#SubprocessWorker.get_answer_from_subprocess-686"><span class="linenos">686</span></a>            <span class="c1"># print(self.settings.process_name)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-687"><a href="#SubprocessWorker.get_answer_from_subprocess-687"><span class="linenos">687</span></a>            <span class="c1"># print(result)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-688"><a href="#SubprocessWorker.get_answer_from_subprocess-688"><span class="linenos">688</span></a>            <span class="c1"># print(exception)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-689"><a href="#SubprocessWorker.get_answer_from_subprocess-689"><span class="linenos">689</span></a>            <span class="c1"># print()</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-690"><a href="#SubprocessWorker.get_answer_from_subprocess-690"><span class="linenos">690</span></a>            <span class="c1"># print(&#39; &lt;&lt;&lt; SUBPROCESS EXCEPTION:&#39;)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-691"><a href="#SubprocessWorker.get_answer_from_subprocess-691"><span class="linenos">691</span></a>            <span class="c1"># trace = &#39;&#39;</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-692"><a href="#SubprocessWorker.get_answer_from_subprocess-692"><span class="linenos">692</span></a>            <span class="c1"># for line in exception[2]:</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-693"><a href="#SubprocessWorker.get_answer_from_subprocess-693"><span class="linenos">693</span></a>            <span class="c1">#     trace += line</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-694"><a href="#SubprocessWorker.get_answer_from_subprocess-694"><span class="linenos">694</span></a>            <span class="c1"># print(trace, file=sys.stderr)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-695"><a href="#SubprocessWorker.get_answer_from_subprocess-695"><span class="linenos">695</span></a>            <span class="c1"># print(exception[0])</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-696"><a href="#SubprocessWorker.get_answer_from_subprocess-696"><span class="linenos">696</span></a>            <span class="c1"># print(exception[1])</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-697"><a href="#SubprocessWorker.get_answer_from_subprocess-697"><span class="linenos">697</span></a>            <span class="c1"># print(&#39; &gt;&gt;&gt;&#39;)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-698"><a href="#SubprocessWorker.get_answer_from_subprocess-698"><span class="linenos">698</span></a>
</span><span id="SubprocessWorker.get_answer_from_subprocess-699"><a href="#SubprocessWorker.get_answer_from_subprocess-699"><span class="linenos">699</span></a>            <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_value</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exception</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-700"><a href="#SubprocessWorker.get_answer_from_subprocess-700"><span class="linenos">700</span></a>            <span class="k">raise</span> <span class="n">exc_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="SubprocessWorker.get_answer_from_subprocess-701"><a href="#SubprocessWorker.get_answer_from_subprocess-701"><span class="linenos">701</span></a>        
</span><span id="SubprocessWorker.get_answer_from_subprocess-702"><a href="#SubprocessWorker.get_answer_from_subprocess-702"><span class="linenos">702</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>If (<a href="#Transport.pipe">Transport.pipe</a> == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on
    the OS) may raise a ValueError exception
Will raise Empty() in non-blocking mode when queue is empty
:param block:
:param time_out:  None - infinite; 0.0 - nonblocking; &gt; 0.0 - timeout in seconds
:return:</p>
</div>


                            </div>
                </section>
                <section id="_subprocess_wrapper_profile">
                            <input id="_subprocess_wrapper_profile-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">_subprocess_wrapper_profile</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">process_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="_subprocess_wrapper_profile-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#_subprocess_wrapper_profile"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="_subprocess_wrapper_profile-705"><a href="#_subprocess_wrapper_profile-705"><span class="linenos">705</span></a><span class="k">def</span> <span class="nf">_subprocess_wrapper_profile</span><span class="p">(</span><span class="n">process_data</span><span class="p">):</span>
</span><span id="_subprocess_wrapper_profile-706"><a href="#_subprocess_wrapper_profile-706"><span class="linenos">706</span></a>    <span class="n">printable_name</span> <span class="o">=</span> <span class="n">process_data</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">process_name</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">,</span> <span class="s1">&#39;_&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;.prof&#39;</span>
</span><span id="_subprocess_wrapper_profile-707"><a href="#_subprocess_wrapper_profile-707"><span class="linenos">707</span></a>    <span class="n">cProfile</span><span class="o">.</span><span class="n">runctx</span><span class="p">(</span><span class="s1">&#39;process_data._subprocess_wrapper()&#39;</span><span class="p">,</span> <span class="nb">globals</span><span class="p">(),</span> <span class="nb">locals</span><span class="p">(),</span> <span class="n">printable_name</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="ExternalPipe">
                            <input id="ExternalPipe-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExternalPipe</span>:

                <label class="view-source-button" for="ExternalPipe-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExternalPipe"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExternalPipe-710"><a href="#ExternalPipe-710"><span class="linenos">710</span></a><span class="k">class</span> <span class="nc">ExternalPipe</span><span class="p">:</span>
</span><span id="ExternalPipe-711"><a href="#ExternalPipe-711"><span class="linenos">711</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ExternalPipe-712"><a href="#ExternalPipe-712"><span class="linenos">712</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pipe</span> <span class="o">=</span> <span class="n">Pipe</span><span class="p">()</span>
</span><span id="ExternalPipe-713"><a href="#ExternalPipe-713"><span class="linenos">713</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">inverted_pipe</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pipe</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">pipe</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span></pre></div>


    

                            <div id="ExternalPipe.pipe" class="classattr">
                                <div class="attr variable">
            <span class="name">pipe</span>

        
    </div>
    <a class="headerlink" href="#ExternalPipe.pipe"></a>
    
    

                            </div>
                            <div id="ExternalPipe.inverted_pipe" class="classattr">
                                <div class="attr variable">
            <span class="name">inverted_pipe</span>

        
    </div>
    <a class="headerlink" href="#ExternalPipe.inverted_pipe"></a>
    
    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>