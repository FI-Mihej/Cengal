---
title: thread_workers_pool
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.multithreading<wbr>.thread_workers_pool    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-thread_workers_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-thread_workers_pool-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="sd">Module Docstring</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Type</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">import</span> <span class="nn">queue</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">import</span> <span class="nn">threading</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">ExceptionInfo</span> <span class="o">=</span> <span class="n">Tuple</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">class</span> <span class="nc">RequestToThread</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="k">class</span> <span class="nc">Command</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>        <span class="n">request</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">command_type</span><span class="p">:</span> <span class="s1">&#39;Command&#39;</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">command_type</span> <span class="o">=</span> <span class="n">command_type</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">request</span> <span class="o">=</span> <span class="n">request</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="k">class</span> <span class="nc">ResponseFromThread</span><span class="p">:</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">has_response</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ExceptionInfo</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_response</span> <span class="o">=</span> <span class="n">has_response</span>  <span class="c1"># type: bool</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">response</span>          <span class="c1"># type: Any</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="o">=</span> <span class="n">exception</span>        <span class="c1"># type: Optional[ExceptionInfo]</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="n">ThreadWorker</span> <span class="o">=</span> <span class="n">Callable</span><span class="p">[[</span><span class="n">RequestToThread</span><span class="p">],</span> <span class="n">ResponseFromThread</span><span class="p">]</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="n">TypeOfThreadWorker</span> <span class="o">=</span> <span class="n">Type</span><span class="p">[</span><span class="n">ThreadWorker</span><span class="p">]</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="k">class</span> <span class="nc">ServiceThread</span><span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">):</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ServiceThread</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>  <span class="c1"># type: queue.Queue</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>   <span class="c1"># type: queue.Queue</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker</span> <span class="o">=</span> <span class="n">worker_type</span><span class="p">()</span>    <span class="c1"># type: ThreadWorker</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="n">shut_down</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>            <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>            <span class="k">if</span> <span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">command_type</span><span class="p">:</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>                <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">worker</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="n">ResponseFromThread</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">())</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="nf">put_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">get_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">()</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="k">class</span> <span class="nc">ServiceThreadPool</span><span class="p">:</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">,</span> <span class="n">number_of_threads</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_type</span> <span class="o">=</span> <span class="n">worker_type</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="n">number_of_threads</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">threads</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>                 <span class="c1"># type: List[ServiceThread]</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[ServiceThread, int]</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>  <span class="c1"># type: List[RequestToThread]</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init</span><span class="p">()</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">put_synchronous</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_best_thread</span><span class="p">()</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">put_into_pending_queue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">put_pending_queue_into_work</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="n">buff_pending_requests_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="p">)()</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">for</span> <span class="n">pending_request</span> <span class="ow">in</span> <span class="n">buff_pending_requests_queue</span><span class="p">:</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_impl</span><span class="p">(</span><span class="n">pending_request</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pending_request</span><span class="p">)</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="nf">get_results</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="k">for</span> <span class="n">thread</span><span class="p">,</span> <span class="n">pending_responses</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>            <span class="k">if</span> <span class="n">pending_responses</span><span class="p">:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>                    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>                        <span class="n">responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">thread</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">())</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>                <span class="k">except</span> <span class="n">queue</span><span class="o">.</span><span class="n">Empty</span><span class="p">:</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>                    <span class="k">pass</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="k">return</span> <span class="n">responses</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">RequestToThread</span><span class="p">(</span><span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_results</span><span class="p">()</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">_init</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span><span class="p">):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ServiceThread</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">worker_type</span><span class="p">))</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">_get_best_thread</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceThread</span><span class="p">:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="n">thread_load</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="n">thread_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="n">thread</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>            <span class="n">thread_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="n">thread_load</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">unfinished_tasks</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="n">sorted_by_value</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">thread_load</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">kv</span><span class="p">:</span> <span class="n">kv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">[</span><span class="n">sorted_by_value</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]]</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">_get_threads_list</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">ServiceThread</span><span class="p">]]:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="n">thread_load</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="n">thread_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="n">thread</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="n">thread_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="n">thread_load</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">unfinished_tasks</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="n">sorted_by_value</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">thread_load</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">kv</span><span class="p">:</span> <span class="n">kv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="k">return</span> <span class="n">sorted_by_value</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="nf">_put_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="n">is_ok</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="k">for</span> <span class="n">thread_index</span><span class="p">,</span> <span class="n">thread_qsize</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_threads_list</span><span class="p">():</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                <span class="n">thread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                <span class="n">thread</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>                <span class="n">is_ok</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>                <span class="k">break</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>            <span class="k">except</span> <span class="n">queue</span><span class="o">.</span><span class="n">Full</span><span class="p">:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>                <span class="k">pass</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="n">is_ok</span>
</span></pre></div>


            </section>
                <section id="ExceptionInfo">
                    <div class="attr variable">
            <span class="name">ExceptionInfo</span>        =
<span class="default_value">typing.Tuple</span>

        
    </div>
    <a class="headerlink" href="#ExceptionInfo"></a>
    
    

                </section>
                <section id="RequestToThread">
                            <input id="RequestToThread-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RequestToThread</span>:

                <label class="view-source-button" for="RequestToThread-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RequestToThread"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RequestToThread-49"><a href="#RequestToThread-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">RequestToThread</span><span class="p">:</span>
</span><span id="RequestToThread-50"><a href="#RequestToThread-50"><span class="linenos">50</span></a>    <span class="k">class</span> <span class="nc">Command</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="RequestToThread-51"><a href="#RequestToThread-51"><span class="linenos">51</span></a>        <span class="n">request</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RequestToThread-52"><a href="#RequestToThread-52"><span class="linenos">52</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="RequestToThread-53"><a href="#RequestToThread-53"><span class="linenos">53</span></a>
</span><span id="RequestToThread-54"><a href="#RequestToThread-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">command_type</span><span class="p">:</span> <span class="s1">&#39;Command&#39;</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="RequestToThread-55"><a href="#RequestToThread-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">command_type</span> <span class="o">=</span> <span class="n">command_type</span>
</span><span id="RequestToThread-56"><a href="#RequestToThread-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">request</span> <span class="o">=</span> <span class="n">request</span>
</span></pre></div>


    

                            <div id="RequestToThread.__init__" class="classattr">
                                        <input id="RequestToThread.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">RequestToThread</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">command_type</span><span class="p">:</span> <span class="n"><a href="#RequestToThread.Command">RequestToThread.Command</a></span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n">Any</span></span>)</span>

                <label class="view-source-button" for="RequestToThread.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RequestToThread.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RequestToThread.__init__-54"><a href="#RequestToThread.__init__-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">command_type</span><span class="p">:</span> <span class="s1">&#39;Command&#39;</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="RequestToThread.__init__-55"><a href="#RequestToThread.__init__-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">command_type</span> <span class="o">=</span> <span class="n">command_type</span>
</span><span id="RequestToThread.__init__-56"><a href="#RequestToThread.__init__-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">request</span> <span class="o">=</span> <span class="n">request</span>
</span></pre></div>


    

                            </div>
                            <div id="RequestToThread.command_type" class="classattr">
                                <div class="attr variable">
            <span class="name">command_type</span>

        
    </div>
    <a class="headerlink" href="#RequestToThread.command_type"></a>
    
    

                            </div>
                            <div id="RequestToThread.request" class="classattr">
                                <div class="attr variable">
            <span class="name">request</span>

        
    </div>
    <a class="headerlink" href="#RequestToThread.request"></a>
    
    

                            </div>
                </section>
                <section id="RequestToThread.Command">
                            <input id="RequestToThread.Command-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">RequestToThread.Command</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="RequestToThread.Command-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#RequestToThread.Command"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="RequestToThread.Command-50"><a href="#RequestToThread.Command-50"><span class="linenos">50</span></a>    <span class="k">class</span> <span class="nc">Command</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="RequestToThread.Command-51"><a href="#RequestToThread.Command-51"><span class="linenos">51</span></a>        <span class="n">request</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="RequestToThread.Command-52"><a href="#RequestToThread.Command-52"><span class="linenos">52</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="mi">1</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="RequestToThread.Command.request" class="classattr">
                                <div class="attr variable">
            <span class="name">request</span>        =
<span class="default_value">&lt;Command.request: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#RequestToThread.Command.request"></a>
    
    

                            </div>
                            <div id="RequestToThread.Command.shut_down" class="classattr">
                                <div class="attr variable">
            <span class="name">shut_down</span>        =
<span class="default_value">&lt;Command.shut_down: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#RequestToThread.Command.shut_down"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="RequestToThread.Command.name" class="variable">name</dd>
                <dd id="RequestToThread.Command.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ResponseFromThread">
                            <input id="ResponseFromThread-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ResponseFromThread</span>:

                <label class="view-source-button" for="ResponseFromThread-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResponseFromThread"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResponseFromThread-59"><a href="#ResponseFromThread-59"><span class="linenos">59</span></a><span class="k">class</span> <span class="nc">ResponseFromThread</span><span class="p">:</span>
</span><span id="ResponseFromThread-60"><a href="#ResponseFromThread-60"><span class="linenos">60</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">has_response</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ExceptionInfo</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResponseFromThread-61"><a href="#ResponseFromThread-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_response</span> <span class="o">=</span> <span class="n">has_response</span>  <span class="c1"># type: bool</span>
</span><span id="ResponseFromThread-62"><a href="#ResponseFromThread-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">response</span>          <span class="c1"># type: Any</span>
</span><span id="ResponseFromThread-63"><a href="#ResponseFromThread-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="o">=</span> <span class="n">exception</span>        <span class="c1"># type: Optional[ExceptionInfo]</span>
</span></pre></div>


    

                            <div id="ResponseFromThread.__init__" class="classattr">
                                        <input id="ResponseFromThread.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ResponseFromThread</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">has_response</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">response</span><span class="p">:</span> <span class="n">Any</span>,</span><span class="param">	<span class="n">exception</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ResponseFromThread.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResponseFromThread.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResponseFromThread.__init__-60"><a href="#ResponseFromThread.__init__-60"><span class="linenos">60</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">has_response</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">response</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">exception</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ExceptionInfo</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResponseFromThread.__init__-61"><a href="#ResponseFromThread.__init__-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">has_response</span> <span class="o">=</span> <span class="n">has_response</span>  <span class="c1"># type: bool</span>
</span><span id="ResponseFromThread.__init__-62"><a href="#ResponseFromThread.__init__-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">response</span>          <span class="c1"># type: Any</span>
</span><span id="ResponseFromThread.__init__-63"><a href="#ResponseFromThread.__init__-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">exception</span> <span class="o">=</span> <span class="n">exception</span>        <span class="c1"># type: Optional[ExceptionInfo]</span>
</span></pre></div>


    

                            </div>
                            <div id="ResponseFromThread.has_response" class="classattr">
                                <div class="attr variable">
            <span class="name">has_response</span>

        
    </div>
    <a class="headerlink" href="#ResponseFromThread.has_response"></a>
    
    

                            </div>
                            <div id="ResponseFromThread.response" class="classattr">
                                <div class="attr variable">
            <span class="name">response</span>

        
    </div>
    <a class="headerlink" href="#ResponseFromThread.response"></a>
    
    

                            </div>
                            <div id="ResponseFromThread.exception" class="classattr">
                                <div class="attr variable">
            <span class="name">exception</span>

        
    </div>
    <a class="headerlink" href="#ResponseFromThread.exception"></a>
    
    

                            </div>
                </section>
                <section id="ThreadWorker">
                    <div class="attr variable">
            <span class="name">ThreadWorker</span>        =
<input id="ThreadWorker-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="ThreadWorker-view-value"></label><span class="default_value">typing.Callable[[<a href="#RequestToThread">RequestToThread</a>], <a href="#ResponseFromThread">ResponseFromThread</a>]</span>

        
    </div>
    <a class="headerlink" href="#ThreadWorker"></a>
    
    

                </section>
                <section id="TypeOfThreadWorker">
                    <div class="attr variable">
            <span class="name">TypeOfThreadWorker</span>        =
<input id="TypeOfThreadWorker-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="TypeOfThreadWorker-view-value"></label><span class="default_value">typing.Type[typing.Callable[[<a href="#RequestToThread">RequestToThread</a>], <a href="#ResponseFromThread">ResponseFromThread</a>]]</span>

        
    </div>
    <a class="headerlink" href="#TypeOfThreadWorker"></a>
    
    

                </section>
                <section id="ServiceThread">
                            <input id="ServiceThread-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ServiceThread</span><wbr>(<span class="base">threading.Thread</span>):

                <label class="view-source-button" for="ServiceThread-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread-70"><a href="#ServiceThread-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">ServiceThread</span><span class="p">(</span><span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">):</span>
</span><span id="ServiceThread-71"><a href="#ServiceThread-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">):</span>
</span><span id="ServiceThread-72"><a href="#ServiceThread-72"><span class="linenos"> 72</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ServiceThread</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="ServiceThread-73"><a href="#ServiceThread-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>  <span class="c1"># type: queue.Queue</span>
</span><span id="ServiceThread-74"><a href="#ServiceThread-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>   <span class="c1"># type: queue.Queue</span>
</span><span id="ServiceThread-75"><a href="#ServiceThread-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker</span> <span class="o">=</span> <span class="n">worker_type</span><span class="p">()</span>    <span class="c1"># type: ThreadWorker</span>
</span><span id="ServiceThread-76"><a href="#ServiceThread-76"><span class="linenos"> 76</span></a>
</span><span id="ServiceThread-77"><a href="#ServiceThread-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ServiceThread-78"><a href="#ServiceThread-78"><span class="linenos"> 78</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ServiceThread-79"><a href="#ServiceThread-79"><span class="linenos"> 79</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="n">shut_down</span><span class="p">:</span>
</span><span id="ServiceThread-80"><a href="#ServiceThread-80"><span class="linenos"> 80</span></a>            <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="ServiceThread-81"><a href="#ServiceThread-81"><span class="linenos"> 81</span></a>
</span><span id="ServiceThread-82"><a href="#ServiceThread-82"><span class="linenos"> 82</span></a>            <span class="k">if</span> <span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">command_type</span><span class="p">:</span>
</span><span id="ServiceThread-83"><a href="#ServiceThread-83"><span class="linenos"> 83</span></a>                <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ServiceThread-84"><a href="#ServiceThread-84"><span class="linenos"> 84</span></a>
</span><span id="ServiceThread-85"><a href="#ServiceThread-85"><span class="linenos"> 85</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ServiceThread-86"><a href="#ServiceThread-86"><span class="linenos"> 86</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">worker</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThread-87"><a href="#ServiceThread-87"><span class="linenos"> 87</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="ServiceThread-88"><a href="#ServiceThread-88"><span class="linenos"> 88</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="n">ResponseFromThread</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">())</span>
</span><span id="ServiceThread-89"><a href="#ServiceThread-89"><span class="linenos"> 89</span></a>
</span><span id="ServiceThread-90"><a href="#ServiceThread-90"><span class="linenos"> 90</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</span><span id="ServiceThread-91"><a href="#ServiceThread-91"><span class="linenos"> 91</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="ServiceThread-92"><a href="#ServiceThread-92"><span class="linenos"> 92</span></a>
</span><span id="ServiceThread-93"><a href="#ServiceThread-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThread-94"><a href="#ServiceThread-94"><span class="linenos"> 94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThread-95"><a href="#ServiceThread-95"><span class="linenos"> 95</span></a>
</span><span id="ServiceThread-96"><a href="#ServiceThread-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="nf">put_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThread-97"><a href="#ServiceThread-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThread-98"><a href="#ServiceThread-98"><span class="linenos"> 98</span></a>
</span><span id="ServiceThread-99"><a href="#ServiceThread-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ServiceThread-100"><a href="#ServiceThread-100"><span class="linenos">100</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="ServiceThread-101"><a href="#ServiceThread-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="ServiceThread-102"><a href="#ServiceThread-102"><span class="linenos">102</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="ServiceThread-103"><a href="#ServiceThread-103"><span class="linenos">103</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="ServiceThread-104"><a href="#ServiceThread-104"><span class="linenos">104</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ServiceThread-105"><a href="#ServiceThread-105"><span class="linenos">105</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="ServiceThread-106"><a href="#ServiceThread-106"><span class="linenos">106</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ServiceThread-107"><a href="#ServiceThread-107"><span class="linenos">107</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span><span id="ServiceThread-108"><a href="#ServiceThread-108"><span class="linenos">108</span></a>
</span><span id="ServiceThread-109"><a href="#ServiceThread-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="nf">get_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ServiceThread-110"><a href="#ServiceThread-110"><span class="linenos">110</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">()</span>
</span><span id="ServiceThread-111"><a href="#ServiceThread-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="ServiceThread-112"><a href="#ServiceThread-112"><span class="linenos">112</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="ServiceThread-113"><a href="#ServiceThread-113"><span class="linenos">113</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="ServiceThread-114"><a href="#ServiceThread-114"><span class="linenos">114</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ServiceThread-115"><a href="#ServiceThread-115"><span class="linenos">115</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="ServiceThread-116"><a href="#ServiceThread-116"><span class="linenos">116</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ServiceThread-117"><a href="#ServiceThread-117"><span class="linenos">117</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span></pre></div>


            <div class="docstring"><p>A class that represents a thread of control.</p>

<p>This class can be safely subclassed in a limited fashion. There are two ways
to specify the activity: by passing a callable object to the constructor, or
by overriding the run() method in a subclass.</p>
</div>


                            <div id="ServiceThread.__init__" class="classattr">
                                        <input id="ServiceThread.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ServiceThread</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">worker_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n"><a href="#RequestToThread">RequestToThread</a></span><span class="p">],</span> <span class="n"><a href="#ResponseFromThread">ResponseFromThread</a></span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="ServiceThread.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.__init__-71"><a href="#ServiceThread.__init__-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">):</span>
</span><span id="ServiceThread.__init__-72"><a href="#ServiceThread.__init__-72"><span class="linenos">72</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ServiceThread</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">daemon</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="ServiceThread.__init__-73"><a href="#ServiceThread.__init__-73"><span class="linenos">73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>  <span class="c1"># type: queue.Queue</span>
</span><span id="ServiceThread.__init__-74"><a href="#ServiceThread.__init__-74"><span class="linenos">74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">Queue</span><span class="p">()</span>   <span class="c1"># type: queue.Queue</span>
</span><span id="ServiceThread.__init__-75"><a href="#ServiceThread.__init__-75"><span class="linenos">75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker</span> <span class="o">=</span> <span class="n">worker_type</span><span class="p">()</span>    <span class="c1"># type: ThreadWorker</span>
</span></pre></div>


            <div class="docstring"><p>This constructor should always be called with keyword arguments. Arguments are:</p>

<p><em>group</em> should be None; reserved for future extension when a ThreadGroup
class is implemented.</p>

<p><em>target</em> is the callable object to be invoked by the run()
method. Defaults to None, meaning nothing is called.</p>

<p><em>name</em> is the thread name. By default, a unique name is constructed of
the form "Thread-N" where N is a small decimal number.</p>

<p><em>args</em> is the argument tuple for the target invocation. Defaults to ().</p>

<p><em>kwargs</em> is a dictionary of keyword arguments for the target
invocation. Defaults to {}.</p>

<p>If a subclass overrides the constructor, it must make sure to invoke
the base class constructor (Thread.__init__()) before doing anything
else to the thread.</p>
</div>


                            </div>
                            <div id="ServiceThread.requests" class="classattr">
                                <div class="attr variable">
            <span class="name">requests</span>

        
    </div>
    <a class="headerlink" href="#ServiceThread.requests"></a>
    
    

                            </div>
                            <div id="ServiceThread.results" class="classattr">
                                <div class="attr variable">
            <span class="name">results</span>

        
    </div>
    <a class="headerlink" href="#ServiceThread.results"></a>
    
    

                            </div>
                            <div id="ServiceThread.worker" class="classattr">
                                <div class="attr variable">
            <span class="name">worker</span>

        
    </div>
    <a class="headerlink" href="#ServiceThread.worker"></a>
    
    

                            </div>
                            <div id="ServiceThread.run" class="classattr">
                                        <input id="ServiceThread.run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThread.run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.run-77"><a href="#ServiceThread.run-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ServiceThread.run-78"><a href="#ServiceThread.run-78"><span class="linenos">78</span></a>        <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ServiceThread.run-79"><a href="#ServiceThread.run-79"><span class="linenos">79</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="n">shut_down</span><span class="p">:</span>
</span><span id="ServiceThread.run-80"><a href="#ServiceThread.run-80"><span class="linenos">80</span></a>            <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="ServiceThread.run-81"><a href="#ServiceThread.run-81"><span class="linenos">81</span></a>
</span><span id="ServiceThread.run-82"><a href="#ServiceThread.run-82"><span class="linenos">82</span></a>            <span class="k">if</span> <span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span> <span class="o">==</span> <span class="n">request</span><span class="o">.</span><span class="n">command_type</span><span class="p">:</span>
</span><span id="ServiceThread.run-83"><a href="#ServiceThread.run-83"><span class="linenos">83</span></a>                <span class="n">shut_down</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ServiceThread.run-84"><a href="#ServiceThread.run-84"><span class="linenos">84</span></a>
</span><span id="ServiceThread.run-85"><a href="#ServiceThread.run-85"><span class="linenos">85</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ServiceThread.run-86"><a href="#ServiceThread.run-86"><span class="linenos">86</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">worker</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThread.run-87"><a href="#ServiceThread.run-87"><span class="linenos">87</span></a>            <span class="k">except</span><span class="p">:</span>
</span><span id="ServiceThread.run-88"><a href="#ServiceThread.run-88"><span class="linenos">88</span></a>                <span class="n">response</span> <span class="o">=</span> <span class="n">ResponseFromThread</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">())</span>
</span><span id="ServiceThread.run-89"><a href="#ServiceThread.run-89"><span class="linenos">89</span></a>
</span><span id="ServiceThread.run-90"><a href="#ServiceThread.run-90"><span class="linenos">90</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">response</span><span class="p">)</span>
</span><span id="ServiceThread.run-91"><a href="#ServiceThread.run-91"><span class="linenos">91</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Method representing the thread's activity.</p>

<p>You may override this method in a subclass. The standard run() method
invokes the callable object passed to the object's constructor as the
target argument, if any, with sequential and keyword arguments taken
from the args and kwargs arguments, respectively.</p>
</div>


                            </div>
                            <div id="ServiceThread.put" class="classattr">
                                        <input id="ServiceThread.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n"><a href="#RequestToThread">RequestToThread</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThread.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.put-93"><a href="#ServiceThread.put-93"><span class="linenos">93</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThread.put-94"><a href="#ServiceThread.put-94"><span class="linenos">94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThread.put_nowait" class="classattr">
                                        <input id="ServiceThread.put_nowait-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_nowait</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n"><a href="#RequestToThread">RequestToThread</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThread.put_nowait-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.put_nowait"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.put_nowait-96"><a href="#ServiceThread.put_nowait-96"><span class="linenos">96</span></a>    <span class="k">def</span> <span class="nf">put_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThread.put_nowait-97"><a href="#ServiceThread.put_nowait-97"><span class="linenos">97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThread.get" class="classattr">
                                        <input id="ServiceThread.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="ServiceThread.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.get-99"><a href="#ServiceThread.get-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ServiceThread.get-100"><a href="#ServiceThread.get-100"><span class="linenos">100</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="ServiceThread.get-101"><a href="#ServiceThread.get-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="ServiceThread.get-102"><a href="#ServiceThread.get-102"><span class="linenos">102</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="ServiceThread.get-103"><a href="#ServiceThread.get-103"><span class="linenos">103</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="ServiceThread.get-104"><a href="#ServiceThread.get-104"><span class="linenos">104</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ServiceThread.get-105"><a href="#ServiceThread.get-105"><span class="linenos">105</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="ServiceThread.get-106"><a href="#ServiceThread.get-106"><span class="linenos">106</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ServiceThread.get-107"><a href="#ServiceThread.get-107"><span class="linenos">107</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThread.get_nowait" class="classattr">
                                        <input id="ServiceThread.get_nowait-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_nowait</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="ServiceThread.get_nowait-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThread.get_nowait"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThread.get_nowait-109"><a href="#ServiceThread.get_nowait-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="nf">get_nowait</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ServiceThread.get_nowait-110"><a href="#ServiceThread.get_nowait-110"><span class="linenos">110</span></a>        <span class="n">response</span><span class="p">:</span> <span class="n">ResponseFromThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">()</span>
</span><span id="ServiceThread.get_nowait-111"><a href="#ServiceThread.get_nowait-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">task_done</span><span class="p">()</span>
</span><span id="ServiceThread.get_nowait-112"><a href="#ServiceThread.get_nowait-112"><span class="linenos">112</span></a>        <span class="k">if</span> <span class="n">response</span><span class="o">.</span><span class="n">has_response</span><span class="p">:</span>
</span><span id="ServiceThread.get_nowait-113"><a href="#ServiceThread.get_nowait-113"><span class="linenos">113</span></a>            <span class="k">return</span> <span class="n">response</span><span class="o">.</span><span class="n">response</span>
</span><span id="ServiceThread.get_nowait-114"><a href="#ServiceThread.get_nowait-114"><span class="linenos">114</span></a>        <span class="k">elif</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ServiceThread.get_nowait-115"><a href="#ServiceThread.get_nowait-115"><span class="linenos">115</span></a>            <span class="k">raise</span> <span class="n">response</span><span class="o">.</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="ServiceThread.get_nowait-116"><a href="#ServiceThread.get_nowait-116"><span class="linenos">116</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ServiceThread.get_nowait-117"><a href="#ServiceThread.get_nowait-117"><span class="linenos">117</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>threading.Thread</dt>
                                <dd id="ServiceThread.start" class="function">start</dd>
                <dd id="ServiceThread.join" class="function">join</dd>
                <dd id="ServiceThread.name" class="variable">name</dd>
                <dd id="ServiceThread.ident" class="variable">ident</dd>
                <dd id="ServiceThread.is_alive" class="function">is_alive</dd>
                <dd id="ServiceThread.isAlive" class="function">isAlive</dd>
                <dd id="ServiceThread.daemon" class="variable">daemon</dd>
                <dd id="ServiceThread.isDaemon" class="function">isDaemon</dd>
                <dd id="ServiceThread.setDaemon" class="function">setDaemon</dd>
                <dd id="ServiceThread.getName" class="function">getName</dd>
                <dd id="ServiceThread.setName" class="function">setName</dd>
                <dd id="ServiceThread.native_id" class="variable">native_id</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ServiceThreadPool">
                            <input id="ServiceThreadPool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ServiceThreadPool</span>:

                <label class="view-source-button" for="ServiceThreadPool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool-120"><a href="#ServiceThreadPool-120"><span class="linenos">120</span></a><span class="k">class</span> <span class="nc">ServiceThreadPool</span><span class="p">:</span>
</span><span id="ServiceThreadPool-121"><a href="#ServiceThreadPool-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">,</span> <span class="n">number_of_threads</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="ServiceThreadPool-122"><a href="#ServiceThreadPool-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_type</span> <span class="o">=</span> <span class="n">worker_type</span>
</span><span id="ServiceThreadPool-123"><a href="#ServiceThreadPool-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="n">number_of_threads</span>
</span><span id="ServiceThreadPool-124"><a href="#ServiceThreadPool-124"><span class="linenos">124</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="ServiceThreadPool-125"><a href="#ServiceThreadPool-125"><span class="linenos">125</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-126"><a href="#ServiceThreadPool-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">threads</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>                 <span class="c1"># type: List[ServiceThread]</span>
</span><span id="ServiceThreadPool-127"><a href="#ServiceThreadPool-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[ServiceThread, int]</span>
</span><span id="ServiceThreadPool-128"><a href="#ServiceThreadPool-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>  <span class="c1"># type: List[RequestToThread]</span>
</span><span id="ServiceThreadPool-129"><a href="#ServiceThreadPool-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init</span><span class="p">()</span>
</span><span id="ServiceThreadPool-130"><a href="#ServiceThreadPool-130"><span class="linenos">130</span></a>
</span><span id="ServiceThreadPool-131"><a href="#ServiceThreadPool-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">put_synchronous</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThreadPool-132"><a href="#ServiceThreadPool-132"><span class="linenos">132</span></a>        <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_best_thread</span><span class="p">()</span>
</span><span id="ServiceThreadPool-133"><a href="#ServiceThreadPool-133"><span class="linenos">133</span></a>        <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThreadPool-134"><a href="#ServiceThreadPool-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-135"><a href="#ServiceThreadPool-135"><span class="linenos">135</span></a>
</span><span id="ServiceThreadPool-136"><a href="#ServiceThreadPool-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">put_into_pending_queue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThreadPool-137"><a href="#ServiceThreadPool-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThreadPool-138"><a href="#ServiceThreadPool-138"><span class="linenos">138</span></a>
</span><span id="ServiceThreadPool-139"><a href="#ServiceThreadPool-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">put_pending_queue_into_work</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ServiceThreadPool-140"><a href="#ServiceThreadPool-140"><span class="linenos">140</span></a>        <span class="n">buff_pending_requests_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span>
</span><span id="ServiceThreadPool-141"><a href="#ServiceThreadPool-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="p">)()</span>
</span><span id="ServiceThreadPool-142"><a href="#ServiceThreadPool-142"><span class="linenos">142</span></a>        <span class="k">for</span> <span class="n">pending_request</span> <span class="ow">in</span> <span class="n">buff_pending_requests_queue</span><span class="p">:</span>
</span><span id="ServiceThreadPool-143"><a href="#ServiceThreadPool-143"><span class="linenos">143</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_impl</span><span class="p">(</span><span class="n">pending_request</span><span class="p">):</span>
</span><span id="ServiceThreadPool-144"><a href="#ServiceThreadPool-144"><span class="linenos">144</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pending_request</span><span class="p">)</span>
</span><span id="ServiceThreadPool-145"><a href="#ServiceThreadPool-145"><span class="linenos">145</span></a>
</span><span id="ServiceThreadPool-146"><a href="#ServiceThreadPool-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">get_results</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="ServiceThreadPool-147"><a href="#ServiceThreadPool-147"><span class="linenos">147</span></a>        <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ServiceThreadPool-148"><a href="#ServiceThreadPool-148"><span class="linenos">148</span></a>        <span class="k">for</span> <span class="n">thread</span><span class="p">,</span> <span class="n">pending_responses</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="ServiceThreadPool-149"><a href="#ServiceThreadPool-149"><span class="linenos">149</span></a>            <span class="k">if</span> <span class="n">pending_responses</span><span class="p">:</span>
</span><span id="ServiceThreadPool-150"><a href="#ServiceThreadPool-150"><span class="linenos">150</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="ServiceThreadPool-151"><a href="#ServiceThreadPool-151"><span class="linenos">151</span></a>                    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="ServiceThreadPool-152"><a href="#ServiceThreadPool-152"><span class="linenos">152</span></a>                        <span class="n">responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">thread</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">())</span>
</span><span id="ServiceThreadPool-153"><a href="#ServiceThreadPool-153"><span class="linenos">153</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-154"><a href="#ServiceThreadPool-154"><span class="linenos">154</span></a>                <span class="k">except</span> <span class="n">queue</span><span class="o">.</span><span class="n">Empty</span><span class="p">:</span>
</span><span id="ServiceThreadPool-155"><a href="#ServiceThreadPool-155"><span class="linenos">155</span></a>                    <span class="k">pass</span>
</span><span id="ServiceThreadPool-156"><a href="#ServiceThreadPool-156"><span class="linenos">156</span></a>        <span class="k">return</span> <span class="n">responses</span>
</span><span id="ServiceThreadPool-157"><a href="#ServiceThreadPool-157"><span class="linenos">157</span></a>
</span><span id="ServiceThreadPool-158"><a href="#ServiceThreadPool-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="ServiceThreadPool-159"><a href="#ServiceThreadPool-159"><span class="linenos">159</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool-160"><a href="#ServiceThreadPool-160"><span class="linenos">160</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">RequestToThread</span><span class="p">(</span><span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="ServiceThreadPool-161"><a href="#ServiceThreadPool-161"><span class="linenos">161</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool-162"><a href="#ServiceThreadPool-162"><span class="linenos">162</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="ServiceThreadPool-163"><a href="#ServiceThreadPool-163"><span class="linenos">163</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_results</span><span class="p">()</span>
</span><span id="ServiceThreadPool-164"><a href="#ServiceThreadPool-164"><span class="linenos">164</span></a>
</span><span id="ServiceThreadPool-165"><a href="#ServiceThreadPool-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="nf">_init</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ServiceThreadPool-166"><a href="#ServiceThreadPool-166"><span class="linenos">166</span></a>        <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span><span class="p">):</span>
</span><span id="ServiceThreadPool-167"><a href="#ServiceThreadPool-167"><span class="linenos">167</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ServiceThread</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">worker_type</span><span class="p">))</span>
</span><span id="ServiceThreadPool-168"><a href="#ServiceThreadPool-168"><span class="linenos">168</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool-169"><a href="#ServiceThreadPool-169"><span class="linenos">169</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ServiceThreadPool-170"><a href="#ServiceThreadPool-170"><span class="linenos">170</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="ServiceThreadPool-171"><a href="#ServiceThreadPool-171"><span class="linenos">171</span></a>
</span><span id="ServiceThreadPool-172"><a href="#ServiceThreadPool-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">_get_best_thread</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ServiceThread</span><span class="p">:</span>
</span><span id="ServiceThreadPool-173"><a href="#ServiceThreadPool-173"><span class="linenos">173</span></a>        <span class="n">thread_load</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="ServiceThreadPool-174"><a href="#ServiceThreadPool-174"><span class="linenos">174</span></a>        <span class="n">thread_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="ServiceThreadPool-175"><a href="#ServiceThreadPool-175"><span class="linenos">175</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool-176"><a href="#ServiceThreadPool-176"><span class="linenos">176</span></a>            <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="n">thread</span>
</span><span id="ServiceThreadPool-177"><a href="#ServiceThreadPool-177"><span class="linenos">177</span></a>            <span class="n">thread_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-178"><a href="#ServiceThreadPool-178"><span class="linenos">178</span></a>            <span class="n">thread_load</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">unfinished_tasks</span>
</span><span id="ServiceThreadPool-179"><a href="#ServiceThreadPool-179"><span class="linenos">179</span></a>        <span class="n">sorted_by_value</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">thread_load</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">kv</span><span class="p">:</span> <span class="n">kv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="ServiceThreadPool-180"><a href="#ServiceThreadPool-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">[</span><span class="n">sorted_by_value</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]]</span>
</span><span id="ServiceThreadPool-181"><a href="#ServiceThreadPool-181"><span class="linenos">181</span></a>
</span><span id="ServiceThreadPool-182"><a href="#ServiceThreadPool-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">_get_threads_list</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">ServiceThread</span><span class="p">]]:</span>
</span><span id="ServiceThreadPool-183"><a href="#ServiceThreadPool-183"><span class="linenos">183</span></a>        <span class="n">thread_load</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="ServiceThreadPool-184"><a href="#ServiceThreadPool-184"><span class="linenos">184</span></a>        <span class="n">thread_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="ServiceThreadPool-185"><a href="#ServiceThreadPool-185"><span class="linenos">185</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool-186"><a href="#ServiceThreadPool-186"><span class="linenos">186</span></a>            <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="n">thread</span>
</span><span id="ServiceThreadPool-187"><a href="#ServiceThreadPool-187"><span class="linenos">187</span></a>            <span class="n">thread_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-188"><a href="#ServiceThreadPool-188"><span class="linenos">188</span></a>            <span class="n">thread_load</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">thread</span><span class="o">.</span><span class="n">requests</span><span class="o">.</span><span class="n">unfinished_tasks</span>
</span><span id="ServiceThreadPool-189"><a href="#ServiceThreadPool-189"><span class="linenos">189</span></a>        <span class="n">sorted_by_value</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">thread_load</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">kv</span><span class="p">:</span> <span class="n">kv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="ServiceThreadPool-190"><a href="#ServiceThreadPool-190"><span class="linenos">190</span></a>        <span class="k">return</span> <span class="n">sorted_by_value</span>
</span><span id="ServiceThreadPool-191"><a href="#ServiceThreadPool-191"><span class="linenos">191</span></a>
</span><span id="ServiceThreadPool-192"><a href="#ServiceThreadPool-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">_put_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ServiceThreadPool-193"><a href="#ServiceThreadPool-193"><span class="linenos">193</span></a>        <span class="n">is_ok</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ServiceThreadPool-194"><a href="#ServiceThreadPool-194"><span class="linenos">194</span></a>        <span class="k">for</span> <span class="n">thread_index</span><span class="p">,</span> <span class="n">thread_qsize</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_threads_list</span><span class="p">():</span>
</span><span id="ServiceThreadPool-195"><a href="#ServiceThreadPool-195"><span class="linenos">195</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ServiceThreadPool-196"><a href="#ServiceThreadPool-196"><span class="linenos">196</span></a>                <span class="n">thread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">[</span><span class="n">thread_index</span><span class="p">]</span>
</span><span id="ServiceThreadPool-197"><a href="#ServiceThreadPool-197"><span class="linenos">197</span></a>                <span class="n">thread</span><span class="o">.</span><span class="n">put_nowait</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThreadPool-198"><a href="#ServiceThreadPool-198"><span class="linenos">198</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool-199"><a href="#ServiceThreadPool-199"><span class="linenos">199</span></a>                <span class="n">is_ok</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ServiceThreadPool-200"><a href="#ServiceThreadPool-200"><span class="linenos">200</span></a>                <span class="k">break</span>
</span><span id="ServiceThreadPool-201"><a href="#ServiceThreadPool-201"><span class="linenos">201</span></a>            <span class="k">except</span> <span class="n">queue</span><span class="o">.</span><span class="n">Full</span><span class="p">:</span>
</span><span id="ServiceThreadPool-202"><a href="#ServiceThreadPool-202"><span class="linenos">202</span></a>                <span class="k">pass</span>
</span><span id="ServiceThreadPool-203"><a href="#ServiceThreadPool-203"><span class="linenos">203</span></a>        <span class="k">return</span> <span class="n">is_ok</span>
</span></pre></div>


    

                            <div id="ServiceThreadPool.__init__" class="classattr">
                                        <input id="ServiceThreadPool.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ServiceThreadPool</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">worker_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n"><a href="#RequestToThread">RequestToThread</a></span><span class="p">],</span> <span class="n"><a href="#ResponseFromThread">ResponseFromThread</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">number_of_threads</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span></span>)</span>

                <label class="view-source-button" for="ServiceThreadPool.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.__init__-121"><a href="#ServiceThreadPool.__init__-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker_type</span><span class="p">:</span> <span class="n">TypeOfThreadWorker</span><span class="p">,</span> <span class="n">number_of_threads</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="ServiceThreadPool.__init__-122"><a href="#ServiceThreadPool.__init__-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">worker_type</span> <span class="o">=</span> <span class="n">worker_type</span>
</span><span id="ServiceThreadPool.__init__-123"><a href="#ServiceThreadPool.__init__-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="n">number_of_threads</span>
</span><span id="ServiceThreadPool.__init__-124"><a href="#ServiceThreadPool.__init__-124"><span class="linenos">124</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="ServiceThreadPool.__init__-125"><a href="#ServiceThreadPool.__init__-125"><span class="linenos">125</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">number_of_threads</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool.__init__-126"><a href="#ServiceThreadPool.__init__-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">threads</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>                 <span class="c1"># type: List[ServiceThread]</span>
</span><span id="ServiceThreadPool.__init__-127"><a href="#ServiceThreadPool.__init__-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[ServiceThread, int]</span>
</span><span id="ServiceThreadPool.__init__-128"><a href="#ServiceThreadPool.__init__-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>  <span class="c1"># type: List[RequestToThread]</span>
</span><span id="ServiceThreadPool.__init__-129"><a href="#ServiceThreadPool.__init__-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThreadPool.worker_type" class="classattr">
                                <div class="attr variable">
            <span class="name">worker_type</span>

        
    </div>
    <a class="headerlink" href="#ServiceThreadPool.worker_type"></a>
    
    

                            </div>
                            <div id="ServiceThreadPool.number_of_threads" class="classattr">
                                <div class="attr variable">
            <span class="name">number_of_threads</span>

        
    </div>
    <a class="headerlink" href="#ServiceThreadPool.number_of_threads"></a>
    
    

                            </div>
                            <div id="ServiceThreadPool.threads" class="classattr">
                                <div class="attr variable">
            <span class="name">threads</span>

        
    </div>
    <a class="headerlink" href="#ServiceThreadPool.threads"></a>
    
    

                            </div>
                            <div id="ServiceThreadPool.thread_pending_results" class="classattr">
                                <div class="attr variable">
            <span class="name">thread_pending_results</span>

        
    </div>
    <a class="headerlink" href="#ServiceThreadPool.thread_pending_results"></a>
    
    

                            </div>
                            <div id="ServiceThreadPool.pending_requests_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">pending_requests_queue</span>

        
    </div>
    <a class="headerlink" href="#ServiceThreadPool.pending_requests_queue"></a>
    
    

                            </div>
                            <div id="ServiceThreadPool.put_synchronous" class="classattr">
                                        <input id="ServiceThreadPool.put_synchronous-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_synchronous</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n"><a href="#RequestToThread">RequestToThread</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThreadPool.put_synchronous-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.put_synchronous"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.put_synchronous-131"><a href="#ServiceThreadPool.put_synchronous-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">put_synchronous</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThreadPool.put_synchronous-132"><a href="#ServiceThreadPool.put_synchronous-132"><span class="linenos">132</span></a>        <span class="n">thread</span><span class="p">:</span> <span class="n">ServiceThread</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_best_thread</span><span class="p">()</span>
</span><span id="ServiceThreadPool.put_synchronous-133"><a href="#ServiceThreadPool.put_synchronous-133"><span class="linenos">133</span></a>        <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="ServiceThreadPool.put_synchronous-134"><a href="#ServiceThreadPool.put_synchronous-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThreadPool.put_into_pending_queue" class="classattr">
                                        <input id="ServiceThreadPool.put_into_pending_queue-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_into_pending_queue</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">request</span><span class="p">:</span> <span class="n"><a href="#RequestToThread">RequestToThread</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThreadPool.put_into_pending_queue-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.put_into_pending_queue"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.put_into_pending_queue-136"><a href="#ServiceThreadPool.put_into_pending_queue-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">put_into_pending_queue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">:</span> <span class="n">RequestToThread</span><span class="p">):</span>
</span><span id="ServiceThreadPool.put_into_pending_queue-137"><a href="#ServiceThreadPool.put_into_pending_queue-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThreadPool.put_pending_queue_into_work" class="classattr">
                                        <input id="ServiceThreadPool.put_pending_queue_into_work-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put_pending_queue_into_work</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ServiceThreadPool.put_pending_queue_into_work-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.put_pending_queue_into_work"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.put_pending_queue_into_work-139"><a href="#ServiceThreadPool.put_pending_queue_into_work-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">put_pending_queue_into_work</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ServiceThreadPool.put_pending_queue_into_work-140"><a href="#ServiceThreadPool.put_pending_queue_into_work-140"><span class="linenos">140</span></a>        <span class="n">buff_pending_requests_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span>
</span><span id="ServiceThreadPool.put_pending_queue_into_work-141"><a href="#ServiceThreadPool.put_pending_queue_into_work-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="p">)()</span>
</span><span id="ServiceThreadPool.put_pending_queue_into_work-142"><a href="#ServiceThreadPool.put_pending_queue_into_work-142"><span class="linenos">142</span></a>        <span class="k">for</span> <span class="n">pending_request</span> <span class="ow">in</span> <span class="n">buff_pending_requests_queue</span><span class="p">:</span>
</span><span id="ServiceThreadPool.put_pending_queue_into_work-143"><a href="#ServiceThreadPool.put_pending_queue_into_work-143"><span class="linenos">143</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_put_impl</span><span class="p">(</span><span class="n">pending_request</span><span class="p">):</span>
</span><span id="ServiceThreadPool.put_pending_queue_into_work-144"><a href="#ServiceThreadPool.put_pending_queue_into_work-144"><span class="linenos">144</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">pending_requests_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pending_request</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThreadPool.get_results" class="classattr">
                                        <input id="ServiceThreadPool.get_results-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_results</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ServiceThreadPool.get_results-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.get_results"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.get_results-146"><a href="#ServiceThreadPool.get_results-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">get_results</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="ServiceThreadPool.get_results-147"><a href="#ServiceThreadPool.get_results-147"><span class="linenos">147</span></a>        <span class="n">responses</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ServiceThreadPool.get_results-148"><a href="#ServiceThreadPool.get_results-148"><span class="linenos">148</span></a>        <span class="k">for</span> <span class="n">thread</span><span class="p">,</span> <span class="n">pending_responses</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="ServiceThreadPool.get_results-149"><a href="#ServiceThreadPool.get_results-149"><span class="linenos">149</span></a>            <span class="k">if</span> <span class="n">pending_responses</span><span class="p">:</span>
</span><span id="ServiceThreadPool.get_results-150"><a href="#ServiceThreadPool.get_results-150"><span class="linenos">150</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="ServiceThreadPool.get_results-151"><a href="#ServiceThreadPool.get_results-151"><span class="linenos">151</span></a>                    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="ServiceThreadPool.get_results-152"><a href="#ServiceThreadPool.get_results-152"><span class="linenos">152</span></a>                        <span class="n">responses</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">thread</span><span class="o">.</span><span class="n">get_nowait</span><span class="p">())</span>
</span><span id="ServiceThreadPool.get_results-153"><a href="#ServiceThreadPool.get_results-153"><span class="linenos">153</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">thread_pending_results</span><span class="p">[</span><span class="n">thread</span><span class="p">]</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="ServiceThreadPool.get_results-154"><a href="#ServiceThreadPool.get_results-154"><span class="linenos">154</span></a>                <span class="k">except</span> <span class="n">queue</span><span class="o">.</span><span class="n">Empty</span><span class="p">:</span>
</span><span id="ServiceThreadPool.get_results-155"><a href="#ServiceThreadPool.get_results-155"><span class="linenos">155</span></a>                    <span class="k">pass</span>
</span><span id="ServiceThreadPool.get_results-156"><a href="#ServiceThreadPool.get_results-156"><span class="linenos">156</span></a>        <span class="k">return</span> <span class="n">responses</span>
</span></pre></div>


    

                            </div>
                            <div id="ServiceThreadPool.stop" class="classattr">
                                        <input id="ServiceThreadPool.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ServiceThreadPool.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ServiceThreadPool.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ServiceThreadPool.stop-158"><a href="#ServiceThreadPool.stop-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]:</span>
</span><span id="ServiceThreadPool.stop-159"><a href="#ServiceThreadPool.stop-159"><span class="linenos">159</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool.stop-160"><a href="#ServiceThreadPool.stop-160"><span class="linenos">160</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">RequestToThread</span><span class="p">(</span><span class="n">RequestToThread</span><span class="o">.</span><span class="n">Command</span><span class="o">.</span><span class="n">shut_down</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="ServiceThreadPool.stop-161"><a href="#ServiceThreadPool.stop-161"><span class="linenos">161</span></a>        <span class="k">for</span> <span class="n">thread</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">threads</span><span class="p">:</span>
</span><span id="ServiceThreadPool.stop-162"><a href="#ServiceThreadPool.stop-162"><span class="linenos">162</span></a>            <span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="ServiceThreadPool.stop-163"><a href="#ServiceThreadPool.stop-163"><span class="linenos">163</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_results</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>