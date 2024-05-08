---
title: repeat_for_a_time__python
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.time_management<wbr>.repeat_for_a_time<wbr>.versions<wbr>.v_0<wbr>.repeat_for_a_time__python    </h1>

                
                        <input id="mod-repeat_for_a_time__python-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-repeat_for_a_time__python-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">import</span> <span class="nn">time</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">time</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="n">perf_counter</span> <span class="o">=</span> <span class="n">process_time</span> <span class="o">=</span> <span class="n">time</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>    <span class="kn">from</span> <span class="nn">cengal.time_management.cpu_clock_cycles</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>        <span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a>    <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>        <span class="k">pass</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>    <span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">process_time</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>    <span class="k">pass</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="sd">Module Docstring</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="k">class</span> <span class="nc">TimeLimitIsTooSmall</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="n">min_time</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="c1"># TODO: add support for cpu_ticks_count</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="k">class</span> <span class="nc">ClockType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="n">fake</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="n">clock</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="n">perf_counter</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="n">process_time</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="k">def</span> <span class="nf">_fake</span><span class="p">():</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="k">return</span> <span class="mi">0</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="k">class</span> <span class="nc">BaseTracer</span><span class="p">:</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="sd">    Base class of all tracers</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="sd">    Lets assume you have a tracer:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="sd">        tr = Tracer(10.0)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="sd">    Or a fake tracer:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="sd">        tr = TracerCounter(10000, 10.0)</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="sd">    As result you can use next interfaces</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="sd">        tr()  # Will return True if tracer has finished it&#39;s counting and as a result, the specified time was passed.</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="sd">        tr.iter_per_time_unit  # Will return counted time of iterations per second (if time() function uses second</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="sd">            as a time unit)</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="sd">        tr.iterations_made  # Will return number of all iterations made (not including those that were produced after </span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">            the end of the counting)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">        tr.total_number_of_iterations_made  # Will return number of all iterations made (including those that were </span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">            produced after the end of the counting)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="sd">        tr.time_spent  # Will return time spent (not including time that were used after the end of the counting)</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="sd">        tr.total_amount_of_time_spent  # Will return time spent (including time that were used after the end of the </span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="sd">            counting)</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="sd">        tr.clock_type  # Will return used time function type (ClockType enum)</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span> <span class="o">=</span> <span class="n">clock_type</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_clock</span><span class="p">()</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">=</span> <span class="n">run_time</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">_init_clock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">if</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">fake</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">_fake</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">clock</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">time</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">perf_counter</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">process_time</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">process_time</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="nd">@property</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="k">raise</span> <span class="bp">NotImplemented</span><span class="p">()</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="nd">@property</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="nd">@property</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">total_number_of_iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="nd">@property</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="nd">@property</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">total_amount_of_time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="nd">@property</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="nf">clock_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ClockType</span><span class="p">:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    <span class="nd">@clock_type</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="k">def</span> <span class="nf">clock_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">ClockType</span><span class="p">):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_clock</span><span class="p">()</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="k">class</span> <span class="nc">Tracer</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">    Main tracer.</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a><span class="sd">    Example of use:</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">        tr = Tracer(10.0)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">        while tr.iter():</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">            i = &#39;456&#39;</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">            k = int(&#39;1243&#39; + i)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">        print(&#39;{} iter/s; {} seconds; {} iterations&#39;.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_runs</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">/</span> <span class="mi">2</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="nd">@property</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span><span class="p">)</span> \
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>                       <span class="o">/</span> <span class="n">divider</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span><span class="p">)</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span><span class="p">()</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="k">def</span> <span class="nf">_test_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">())</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_time</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="n">delta_time</span> <span class="o">=</span> <span class="n">current_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="k">if</span> <span class="n">delta_time</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span><span class="p">:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>            <span class="n">time_left</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">-</span> <span class="n">delta_time</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>            <span class="c1"># No need to:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="c1"># if time_left &lt; 0:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="c1">#     time_left = 0</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="n">iterations_per_second</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">/</span> <span class="n">delta_time</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="n">iterations_left</span> <span class="o">=</span> <span class="n">iterations_per_second</span> <span class="o">*</span> <span class="n">time_left</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="k">if</span> <span class="n">iterations_left</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+</span> <span class="nb">round</span><span class="p">(</span><span class="n">iterations_left</span><span class="p">)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_sub_run</span><span class="p">(</span><span class="n">current_time</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">*=</span> <span class="mi">2</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="k">def</span> <span class="nf">_last_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_sub_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">())</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">_last_sub_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_time</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a><span class="k">class</span> <span class="nc">GreedyTracer</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a><span class="sd">    Greedy Main tracer.</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a><span class="sd">    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="sd">    The difference is that he checks time every single iteration.</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="sd">    Example of use is the same as for the Tracer()</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span><span class="p">()</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span><span class="p">)</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="nd">@property</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>        <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>        <span class="k">return</span> <span class="mi">0</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="k">class</span> <span class="nc">TracerCounter</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a><span class="sd">    Counting tracer. Pseudo-tracer.</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a><span class="sd">    Its don&#39;t have an overhead of periodic calling time() function.</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a><span class="sd">    Its task is to count down within a given time, using the speed information already counted by the real tracer</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a><span class="sd">    (by the Tracer class).</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a><span class="sd">    Example of use:</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="sd">        trc = TracerCounter(10000, 10.0)</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a><span class="sd">        while trc.iter():</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="sd">            i = &#39;456&#39;</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="sd">            k = int(&#39;1243&#39; + i)</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a><span class="sd">        print(&#39;{} iter/s; {} seconds; {} iters&#39;.format(trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="sd">    or:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="sd">        def made_tests() -&gt; Tracer:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a><span class="sd">            tr = Tracer(0.1)  # Run for about 0.1 of second.</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a><span class="sd">            while tr.iter():</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a><span class="sd">                some_my_code()</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a><span class="sd">            return tr</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a><span class="sd">        def run(run_time: float, tests_result: Tracer):</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a><span class="sd">            trc = TracerCounter(tests_result.iter_per_time_unit, run_time)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="sd">            while trc.iter():</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a><span class="sd">                some_my_code()</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a><span class="sd">            print(&#39;{} iter/s; {} seconds; {} iterations&#39;.format(trc.iter_per_time_unit, trc.time_spent,</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a><span class="sd">                    trc.iterations_made))</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a><span class="sd">        def main():</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a><span class="sd">            tests_result = made_tests()</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a><span class="sd">            ...</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a><span class="sd">            while True:</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="sd">                time_to_rur_str = input(&#39;Enter run time: &#39;)</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a><span class="sd">                if not time_to_run_str:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a><span class="sd">                    break</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a><span class="sd">                run(float(time_to_rur_str), tests_result)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iter_per_time_unit</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">fake</span><span class="p">):</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">=</span> <span class="n">iter_per_time_unit</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations_needed</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">)</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span><span class="p">()</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations_needed</span><span class="p">:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>    <span class="nd">@property</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a><span class="k">class</span> <span class="nc">TracerIterator</span><span class="p">:</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="sd">    An iterator class. It converts any type of given tracer into an iterator.</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">    As result you have an option to use constructions like this:</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">        for i in TracerIterator(Tracer(20.0)):</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">            k = int(&#39;1243&#39;)</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a><span class="sd">    But keep in mind that in this case there will be a bigger overhead. And there will be less CPU time for the payload.</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tracer</span><span class="p">:</span> <span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span> <span class="o">=</span> <span class="n">tracer</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>    <span class="k">def</span> <span class="fm">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iterations_made</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>            <span class="k">raise</span> <span class="ne">StopIteration</span><span class="p">()</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>    <span class="nb">next</span> <span class="o">=</span> <span class="fm">__next__</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>    <span class="nd">@property</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>    <span class="k">def</span> <span class="nf">tracer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span>
</span></pre></div>


            </section>
                <section id="TimeLimitIsTooSmall">
                            <input id="TimeLimitIsTooSmall-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TimeLimitIsTooSmall</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TimeLimitIsTooSmall-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimeLimitIsTooSmall"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimeLimitIsTooSmall-55"><a href="#TimeLimitIsTooSmall-55"><span class="linenos">55</span></a><span class="k">class</span> <span class="nc">TimeLimitIsTooSmall</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TimeLimitIsTooSmall-56"><a href="#TimeLimitIsTooSmall-56"><span class="linenos">56</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TimeLimitIsTooSmall-57"><a href="#TimeLimitIsTooSmall-57"><span class="linenos">57</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="TimeLimitIsTooSmall-58"><a href="#TimeLimitIsTooSmall-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="n">min_time</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div id="TimeLimitIsTooSmall.__init__" class="classattr">
                                        <input id="TimeLimitIsTooSmall.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TimeLimitIsTooSmall</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">min_time</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span></span>)</span>

                <label class="view-source-button" for="TimeLimitIsTooSmall.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TimeLimitIsTooSmall.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TimeLimitIsTooSmall.__init__-56"><a href="#TimeLimitIsTooSmall.__init__-56"><span class="linenos">56</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TimeLimitIsTooSmall.__init__-57"><a href="#TimeLimitIsTooSmall.__init__-57"><span class="linenos">57</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="TimeLimitIsTooSmall.__init__-58"><a href="#TimeLimitIsTooSmall.__init__-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">min_time</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="n">min_time</span>
</span></pre></div>


    

                            </div>
                            <div id="TimeLimitIsTooSmall.min_time" class="classattr">
                                <div class="attr variable">
            <span class="name">min_time</span><span class="annotation">: Union[int, float, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#TimeLimitIsTooSmall.min_time"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.BaseException</dt>
                                <dd id="TimeLimitIsTooSmall.with_traceback" class="function">with_traceback</dd>
                <dd id="TimeLimitIsTooSmall.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ClockType">
                            <input id="ClockType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ClockType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="ClockType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClockType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClockType-62"><a href="#ClockType-62"><span class="linenos">62</span></a><span class="k">class</span> <span class="nc">ClockType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="ClockType-63"><a href="#ClockType-63"><span class="linenos">63</span></a>    <span class="n">fake</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ClockType-64"><a href="#ClockType-64"><span class="linenos">64</span></a>    <span class="n">clock</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="ClockType-65"><a href="#ClockType-65"><span class="linenos">65</span></a>    <span class="n">perf_counter</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="ClockType-66"><a href="#ClockType-66"><span class="linenos">66</span></a>    <span class="n">process_time</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="ClockType.fake" class="classattr">
                                <div class="attr variable">
            <span class="name">fake</span>        =
<span class="default_value">&lt;<a href="#ClockType.fake">ClockType.fake</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#ClockType.fake"></a>
    
    

                            </div>
                            <div id="ClockType.clock" class="classattr">
                                <div class="attr variable">
            <span class="name">clock</span>        =
<span class="default_value">&lt;<a href="#ClockType.clock">ClockType.clock</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#ClockType.clock"></a>
    
    

                            </div>
                            <div id="ClockType.perf_counter" class="classattr">
                                <div class="attr variable">
            <span class="name">perf_counter</span>        =
<span class="default_value">&lt;<a href="#ClockType.perf_counter">ClockType.perf_counter</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#ClockType.perf_counter"></a>
    
    

                            </div>
                            <div id="ClockType.process_time" class="classattr">
                                <div class="attr variable">
            <span class="name">process_time</span>        =
<span class="default_value">&lt;<a href="#ClockType.process_time">ClockType.process_time</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#ClockType.process_time"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="ClockType.name" class="variable">name</dd>
                <dd id="ClockType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="BaseTracer">
                            <input id="BaseTracer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">BaseTracer</span>:

                <label class="view-source-button" for="BaseTracer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer-73"><a href="#BaseTracer-73"><span class="linenos"> 73</span></a><span class="k">class</span> <span class="nc">BaseTracer</span><span class="p">:</span>
</span><span id="BaseTracer-74"><a href="#BaseTracer-74"><span class="linenos"> 74</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="BaseTracer-75"><a href="#BaseTracer-75"><span class="linenos"> 75</span></a><span class="sd">    Base class of all tracers</span>
</span><span id="BaseTracer-76"><a href="#BaseTracer-76"><span class="linenos"> 76</span></a>
</span><span id="BaseTracer-77"><a href="#BaseTracer-77"><span class="linenos"> 77</span></a><span class="sd">    Lets assume you have a tracer:</span>
</span><span id="BaseTracer-78"><a href="#BaseTracer-78"><span class="linenos"> 78</span></a>
</span><span id="BaseTracer-79"><a href="#BaseTracer-79"><span class="linenos"> 79</span></a><span class="sd">        tr = Tracer(10.0)</span>
</span><span id="BaseTracer-80"><a href="#BaseTracer-80"><span class="linenos"> 80</span></a>
</span><span id="BaseTracer-81"><a href="#BaseTracer-81"><span class="linenos"> 81</span></a><span class="sd">    Or a fake tracer:</span>
</span><span id="BaseTracer-82"><a href="#BaseTracer-82"><span class="linenos"> 82</span></a>
</span><span id="BaseTracer-83"><a href="#BaseTracer-83"><span class="linenos"> 83</span></a><span class="sd">        tr = TracerCounter(10000, 10.0)</span>
</span><span id="BaseTracer-84"><a href="#BaseTracer-84"><span class="linenos"> 84</span></a>
</span><span id="BaseTracer-85"><a href="#BaseTracer-85"><span class="linenos"> 85</span></a><span class="sd">    As result you can use next interfaces</span>
</span><span id="BaseTracer-86"><a href="#BaseTracer-86"><span class="linenos"> 86</span></a>
</span><span id="BaseTracer-87"><a href="#BaseTracer-87"><span class="linenos"> 87</span></a><span class="sd">        tr()  # Will return True if tracer has finished it&#39;s counting and as a result, the specified time was passed.</span>
</span><span id="BaseTracer-88"><a href="#BaseTracer-88"><span class="linenos"> 88</span></a>
</span><span id="BaseTracer-89"><a href="#BaseTracer-89"><span class="linenos"> 89</span></a><span class="sd">        tr.iter_per_time_unit  # Will return counted time of iterations per second (if time() function uses second</span>
</span><span id="BaseTracer-90"><a href="#BaseTracer-90"><span class="linenos"> 90</span></a><span class="sd">            as a time unit)</span>
</span><span id="BaseTracer-91"><a href="#BaseTracer-91"><span class="linenos"> 91</span></a>
</span><span id="BaseTracer-92"><a href="#BaseTracer-92"><span class="linenos"> 92</span></a><span class="sd">        tr.iterations_made  # Will return number of all iterations made (not including those that were produced after </span>
</span><span id="BaseTracer-93"><a href="#BaseTracer-93"><span class="linenos"> 93</span></a><span class="sd">            the end of the counting)</span>
</span><span id="BaseTracer-94"><a href="#BaseTracer-94"><span class="linenos"> 94</span></a>
</span><span id="BaseTracer-95"><a href="#BaseTracer-95"><span class="linenos"> 95</span></a><span class="sd">        tr.total_number_of_iterations_made  # Will return number of all iterations made (including those that were </span>
</span><span id="BaseTracer-96"><a href="#BaseTracer-96"><span class="linenos"> 96</span></a><span class="sd">            produced after the end of the counting)</span>
</span><span id="BaseTracer-97"><a href="#BaseTracer-97"><span class="linenos"> 97</span></a>
</span><span id="BaseTracer-98"><a href="#BaseTracer-98"><span class="linenos"> 98</span></a><span class="sd">        tr.time_spent  # Will return time spent (not including time that were used after the end of the counting)</span>
</span><span id="BaseTracer-99"><a href="#BaseTracer-99"><span class="linenos"> 99</span></a>
</span><span id="BaseTracer-100"><a href="#BaseTracer-100"><span class="linenos">100</span></a><span class="sd">        tr.total_amount_of_time_spent  # Will return time spent (including time that were used after the end of the </span>
</span><span id="BaseTracer-101"><a href="#BaseTracer-101"><span class="linenos">101</span></a><span class="sd">            counting)</span>
</span><span id="BaseTracer-102"><a href="#BaseTracer-102"><span class="linenos">102</span></a>
</span><span id="BaseTracer-103"><a href="#BaseTracer-103"><span class="linenos">103</span></a><span class="sd">        tr.clock_type  # Will return used time function type (ClockType enum)</span>
</span><span id="BaseTracer-104"><a href="#BaseTracer-104"><span class="linenos">104</span></a>
</span><span id="BaseTracer-105"><a href="#BaseTracer-105"><span class="linenos">105</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="BaseTracer-106"><a href="#BaseTracer-106"><span class="linenos">106</span></a>
</span><span id="BaseTracer-107"><a href="#BaseTracer-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="BaseTracer-108"><a href="#BaseTracer-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer-109"><a href="#BaseTracer-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="BaseTracer-110"><a href="#BaseTracer-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="BaseTracer-111"><a href="#BaseTracer-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer-112"><a href="#BaseTracer-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer-113"><a href="#BaseTracer-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer-114"><a href="#BaseTracer-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="BaseTracer-115"><a href="#BaseTracer-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span> <span class="o">=</span> <span class="n">clock_type</span>
</span><span id="BaseTracer-116"><a href="#BaseTracer-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer-117"><a href="#BaseTracer-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_clock</span><span class="p">()</span>
</span><span id="BaseTracer-118"><a href="#BaseTracer-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">=</span> <span class="n">run_time</span>
</span><span id="BaseTracer-119"><a href="#BaseTracer-119"><span class="linenos">119</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">:</span>
</span><span id="BaseTracer-120"><a href="#BaseTracer-120"><span class="linenos">120</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="BaseTracer-121"><a href="#BaseTracer-121"><span class="linenos">121</span></a>
</span><span id="BaseTracer-122"><a href="#BaseTracer-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="BaseTracer-123"><a href="#BaseTracer-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span>
</span><span id="BaseTracer-124"><a href="#BaseTracer-124"><span class="linenos">124</span></a>    
</span><span id="BaseTracer-125"><a href="#BaseTracer-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">_init_clock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-126"><a href="#BaseTracer-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">fake</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="BaseTracer-127"><a href="#BaseTracer-127"><span class="linenos">127</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">_fake</span>
</span><span id="BaseTracer-128"><a href="#BaseTracer-128"><span class="linenos">128</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">clock</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="BaseTracer-129"><a href="#BaseTracer-129"><span class="linenos">129</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">time</span>
</span><span id="BaseTracer-130"><a href="#BaseTracer-130"><span class="linenos">130</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="BaseTracer-131"><a href="#BaseTracer-131"><span class="linenos">131</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">perf_counter</span>
</span><span id="BaseTracer-132"><a href="#BaseTracer-132"><span class="linenos">132</span></a>        <span class="k">elif</span> <span class="n">ClockType</span><span class="o">.</span><span class="n">process_time</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span><span class="p">:</span>
</span><span id="BaseTracer-133"><a href="#BaseTracer-133"><span class="linenos">133</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="n">process_time</span>
</span><span id="BaseTracer-134"><a href="#BaseTracer-134"><span class="linenos">134</span></a>
</span><span id="BaseTracer-135"><a href="#BaseTracer-135"><span class="linenos">135</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-136"><a href="#BaseTracer-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-137"><a href="#BaseTracer-137"><span class="linenos">137</span></a>        <span class="k">raise</span> <span class="bp">NotImplemented</span><span class="p">()</span>
</span><span id="BaseTracer-138"><a href="#BaseTracer-138"><span class="linenos">138</span></a>
</span><span id="BaseTracer-139"><a href="#BaseTracer-139"><span class="linenos">139</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-140"><a href="#BaseTracer-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-141"><a href="#BaseTracer-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span>
</span><span id="BaseTracer-142"><a href="#BaseTracer-142"><span class="linenos">142</span></a>
</span><span id="BaseTracer-143"><a href="#BaseTracer-143"><span class="linenos">143</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-144"><a href="#BaseTracer-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">total_number_of_iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-145"><a href="#BaseTracer-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="BaseTracer-146"><a href="#BaseTracer-146"><span class="linenos">146</span></a>
</span><span id="BaseTracer-147"><a href="#BaseTracer-147"><span class="linenos">147</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-148"><a href="#BaseTracer-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-149"><a href="#BaseTracer-149"><span class="linenos">149</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="BaseTracer-150"><a href="#BaseTracer-150"><span class="linenos">150</span></a>
</span><span id="BaseTracer-151"><a href="#BaseTracer-151"><span class="linenos">151</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-152"><a href="#BaseTracer-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">total_amount_of_time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer-153"><a href="#BaseTracer-153"><span class="linenos">153</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="BaseTracer-154"><a href="#BaseTracer-154"><span class="linenos">154</span></a>
</span><span id="BaseTracer-155"><a href="#BaseTracer-155"><span class="linenos">155</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer-156"><a href="#BaseTracer-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">clock_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ClockType</span><span class="p">:</span>
</span><span id="BaseTracer-157"><a href="#BaseTracer-157"><span class="linenos">157</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span>
</span><span id="BaseTracer-158"><a href="#BaseTracer-158"><span class="linenos">158</span></a>
</span><span id="BaseTracer-159"><a href="#BaseTracer-159"><span class="linenos">159</span></a>    <span class="nd">@clock_type</span><span class="o">.</span><span class="n">setter</span>
</span><span id="BaseTracer-160"><a href="#BaseTracer-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">clock_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">ClockType</span><span class="p">):</span>
</span><span id="BaseTracer-161"><a href="#BaseTracer-161"><span class="linenos">161</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="BaseTracer-162"><a href="#BaseTracer-162"><span class="linenos">162</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_clock</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Base class of all tracers</p>

<p>Lets assume you have a tracer:</p>

<pre><code>tr = Tracer(10.0)
</code></pre>

<p>Or a fake tracer:</p>

<pre><code>tr = TracerCounter(10000, 10.0)
</code></pre>

<p>As result you can use next interfaces</p>

<pre><code>tr()  # Will return True if tracer has finished it's counting and as a result, the specified time was passed.

tr.iter_per_time_unit  # Will return counted time of iterations per second (if time() function uses second
    as a time unit)

tr.iterations_made  # Will return number of all iterations made (not including those that were produced after 
    the end of the counting)

tr.total_number_of_iterations_made  # Will return number of all iterations made (including those that were 
    produced after the end of the counting)

tr.time_spent  # Will return time spent (not including time that were used after the end of the counting)

tr.total_amount_of_time_spent  # Will return time spent (including time that were used after the end of the 
    counting)

tr.clock_type  # Will return used time function type (ClockType enum)
</code></pre>
</div>


                            <div id="BaseTracer.__init__" class="classattr">
                                        <input id="BaseTracer.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">BaseTracer</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">clock_type</span><span class="p">:</span> <span class="n"><a href="#ClockType">ClockType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#ClockType.perf_counter">ClockType.perf_counter</a></span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="BaseTracer.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.__init__-107"><a href="#BaseTracer.__init__-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="BaseTracer.__init__-108"><a href="#BaseTracer.__init__-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer.__init__-109"><a href="#BaseTracer.__init__-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="BaseTracer.__init__-110"><a href="#BaseTracer.__init__-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="BaseTracer.__init__-111"><a href="#BaseTracer.__init__-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer.__init__-112"><a href="#BaseTracer.__init__-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer.__init__-113"><a href="#BaseTracer.__init__-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer.__init__-114"><a href="#BaseTracer.__init__-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="BaseTracer.__init__-115"><a href="#BaseTracer.__init__-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span> <span class="o">=</span> <span class="n">clock_type</span>
</span><span id="BaseTracer.__init__-116"><a href="#BaseTracer.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="BaseTracer.__init__-117"><a href="#BaseTracer.__init__-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_clock</span><span class="p">()</span>
</span><span id="BaseTracer.__init__-118"><a href="#BaseTracer.__init__-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">=</span> <span class="n">run_time</span>
</span><span id="BaseTracer.__init__-119"><a href="#BaseTracer.__init__-119"><span class="linenos">119</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">:</span>
</span><span id="BaseTracer.__init__-120"><a href="#BaseTracer.__init__-120"><span class="linenos">120</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.iter" class="classattr">
                                <div class="attr variable">
            <span class="name">iter</span>

        
    </div>
    <a class="headerlink" href="#BaseTracer.iter"></a>
    
    

                            </div>
                            <div id="BaseTracer.iter_per_time_unit" class="classattr">
                                        <input id="BaseTracer.iter_per_time_unit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">iter_per_time_unit</span>

                <label class="view-source-button" for="BaseTracer.iter_per_time_unit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.iter_per_time_unit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.iter_per_time_unit-135"><a href="#BaseTracer.iter_per_time_unit-135"><span class="linenos">135</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.iter_per_time_unit-136"><a href="#BaseTracer.iter_per_time_unit-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer.iter_per_time_unit-137"><a href="#BaseTracer.iter_per_time_unit-137"><span class="linenos">137</span></a>        <span class="k">raise</span> <span class="bp">NotImplemented</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.iterations_made" class="classattr">
                                        <input id="BaseTracer.iterations_made-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">iterations_made</span>

                <label class="view-source-button" for="BaseTracer.iterations_made-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.iterations_made"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.iterations_made-139"><a href="#BaseTracer.iterations_made-139"><span class="linenos">139</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.iterations_made-140"><a href="#BaseTracer.iterations_made-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer.iterations_made-141"><a href="#BaseTracer.iterations_made-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.total_number_of_iterations_made" class="classattr">
                                        <input id="BaseTracer.total_number_of_iterations_made-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">total_number_of_iterations_made</span>

                <label class="view-source-button" for="BaseTracer.total_number_of_iterations_made-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.total_number_of_iterations_made"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.total_number_of_iterations_made-143"><a href="#BaseTracer.total_number_of_iterations_made-143"><span class="linenos">143</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.total_number_of_iterations_made-144"><a href="#BaseTracer.total_number_of_iterations_made-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">total_number_of_iterations_made</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer.total_number_of_iterations_made-145"><a href="#BaseTracer.total_number_of_iterations_made-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.time_spent" class="classattr">
                                        <input id="BaseTracer.time_spent-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">time_spent</span>

                <label class="view-source-button" for="BaseTracer.time_spent-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.time_spent"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.time_spent-147"><a href="#BaseTracer.time_spent-147"><span class="linenos">147</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.time_spent-148"><a href="#BaseTracer.time_spent-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer.time_spent-149"><a href="#BaseTracer.time_spent-149"><span class="linenos">149</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.total_amount_of_time_spent" class="classattr">
                                        <input id="BaseTracer.total_amount_of_time_spent-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">total_amount_of_time_spent</span>

                <label class="view-source-button" for="BaseTracer.total_amount_of_time_spent-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.total_amount_of_time_spent"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.total_amount_of_time_spent-151"><a href="#BaseTracer.total_amount_of_time_spent-151"><span class="linenos">151</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.total_amount_of_time_spent-152"><a href="#BaseTracer.total_amount_of_time_spent-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">total_amount_of_time_spent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseTracer.total_amount_of_time_spent-153"><a href="#BaseTracer.total_amount_of_time_spent-153"><span class="linenos">153</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseTracer.clock_type" class="classattr">
                                        <input id="BaseTracer.clock_type-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">clock_type</span><span class="annotation">: <a href="#ClockType">ClockType</a></span>

                <label class="view-source-button" for="BaseTracer.clock_type-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseTracer.clock_type"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseTracer.clock_type-155"><a href="#BaseTracer.clock_type-155"><span class="linenos">155</span></a>    <span class="nd">@property</span>
</span><span id="BaseTracer.clock_type-156"><a href="#BaseTracer.clock_type-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">clock_type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ClockType</span><span class="p">:</span>
</span><span id="BaseTracer.clock_type-157"><a href="#BaseTracer.clock_type-157"><span class="linenos">157</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock_type</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="Tracer">
                            <input id="Tracer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Tracer</span><wbr>(<span class="base"><a href="#BaseTracer">BaseTracer</a></span>):

                <label class="view-source-button" for="Tracer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Tracer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Tracer-165"><a href="#Tracer-165"><span class="linenos">165</span></a><span class="k">class</span> <span class="nc">Tracer</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="Tracer-166"><a href="#Tracer-166"><span class="linenos">166</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Tracer-167"><a href="#Tracer-167"><span class="linenos">167</span></a><span class="sd">    Main tracer.</span>
</span><span id="Tracer-168"><a href="#Tracer-168"><span class="linenos">168</span></a><span class="sd">    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.</span>
</span><span id="Tracer-169"><a href="#Tracer-169"><span class="linenos">169</span></a>
</span><span id="Tracer-170"><a href="#Tracer-170"><span class="linenos">170</span></a><span class="sd">    Example of use:</span>
</span><span id="Tracer-171"><a href="#Tracer-171"><span class="linenos">171</span></a>
</span><span id="Tracer-172"><a href="#Tracer-172"><span class="linenos">172</span></a><span class="sd">        tr = Tracer(10.0)</span>
</span><span id="Tracer-173"><a href="#Tracer-173"><span class="linenos">173</span></a><span class="sd">        while tr.iter():</span>
</span><span id="Tracer-174"><a href="#Tracer-174"><span class="linenos">174</span></a><span class="sd">            i = &#39;456&#39;</span>
</span><span id="Tracer-175"><a href="#Tracer-175"><span class="linenos">175</span></a><span class="sd">            k = int(&#39;1243&#39; + i)</span>
</span><span id="Tracer-176"><a href="#Tracer-176"><span class="linenos">176</span></a>
</span><span id="Tracer-177"><a href="#Tracer-177"><span class="linenos">177</span></a><span class="sd">        print(&#39;{} iter/s; {} seconds; {} iterations&#39;.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))</span>
</span><span id="Tracer-178"><a href="#Tracer-178"><span class="linenos">178</span></a>
</span><span id="Tracer-179"><a href="#Tracer-179"><span class="linenos">179</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="Tracer-180"><a href="#Tracer-180"><span class="linenos">180</span></a>
</span><span id="Tracer-181"><a href="#Tracer-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="Tracer-182"><a href="#Tracer-182"><span class="linenos">182</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="Tracer-183"><a href="#Tracer-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_runs</span>
</span><span id="Tracer-184"><a href="#Tracer-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">/</span> <span class="mi">2</span>
</span><span id="Tracer-185"><a href="#Tracer-185"><span class="linenos">185</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span><span class="p">:</span>
</span><span id="Tracer-186"><a href="#Tracer-186"><span class="linenos">186</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="Tracer-187"><a href="#Tracer-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Tracer-188"><a href="#Tracer-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Tracer-189"><a href="#Tracer-189"><span class="linenos">189</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Tracer-190"><a href="#Tracer-190"><span class="linenos">190</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Tracer-191"><a href="#Tracer-191"><span class="linenos">191</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="Tracer-192"><a href="#Tracer-192"><span class="linenos">192</span></a>
</span><span id="Tracer-193"><a href="#Tracer-193"><span class="linenos">193</span></a>    <span class="nd">@property</span>
</span><span id="Tracer-194"><a href="#Tracer-194"><span class="linenos">194</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="Tracer-195"><a href="#Tracer-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="Tracer-196"><a href="#Tracer-196"><span class="linenos">196</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span>
</span><span id="Tracer-197"><a href="#Tracer-197"><span class="linenos">197</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="Tracer-198"><a href="#Tracer-198"><span class="linenos">198</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span><span class="p">)</span> \
</span><span id="Tracer-199"><a href="#Tracer-199"><span class="linenos">199</span></a>                       <span class="o">/</span> <span class="n">divider</span>
</span><span id="Tracer-200"><a href="#Tracer-200"><span class="linenos">200</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="Tracer-201"><a href="#Tracer-201"><span class="linenos">201</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Tracer-202"><a href="#Tracer-202"><span class="linenos">202</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="Tracer-203"><a href="#Tracer-203"><span class="linenos">203</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="Tracer-204"><a href="#Tracer-204"><span class="linenos">204</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="Tracer-205"><a href="#Tracer-205"><span class="linenos">205</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="Tracer-206"><a href="#Tracer-206"><span class="linenos">206</span></a>
</span><span id="Tracer-207"><a href="#Tracer-207"><span class="linenos">207</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-208"><a href="#Tracer-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Tracer-209"><a href="#Tracer-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="Tracer-210"><a href="#Tracer-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="Tracer-211"><a href="#Tracer-211"><span class="linenos">211</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span><span class="p">)</span>
</span><span id="Tracer-212"><a href="#Tracer-212"><span class="linenos">212</span></a>
</span><span id="Tracer-213"><a href="#Tracer-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-214"><a href="#Tracer-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="Tracer-215"><a href="#Tracer-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span><span class="p">:</span>
</span><span id="Tracer-216"><a href="#Tracer-216"><span class="linenos">216</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span><span class="p">()</span>
</span><span id="Tracer-217"><a href="#Tracer-217"><span class="linenos">217</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="Tracer-218"><a href="#Tracer-218"><span class="linenos">218</span></a>
</span><span id="Tracer-219"><a href="#Tracer-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="nf">_test_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-220"><a href="#Tracer-220"><span class="linenos">220</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">())</span>
</span><span id="Tracer-221"><a href="#Tracer-221"><span class="linenos">221</span></a>
</span><span id="Tracer-222"><a href="#Tracer-222"><span class="linenos">222</span></a>    <span class="k">def</span> <span class="nf">_test_sub_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_time</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-223"><a href="#Tracer-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="Tracer-224"><a href="#Tracer-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="Tracer-225"><a href="#Tracer-225"><span class="linenos">225</span></a>        <span class="n">delta_time</span> <span class="o">=</span> <span class="n">current_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="Tracer-226"><a href="#Tracer-226"><span class="linenos">226</span></a>        <span class="k">if</span> <span class="n">delta_time</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span><span class="p">:</span>
</span><span id="Tracer-227"><a href="#Tracer-227"><span class="linenos">227</span></a>            <span class="n">time_left</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">-</span> <span class="n">delta_time</span>
</span><span id="Tracer-228"><a href="#Tracer-228"><span class="linenos">228</span></a>            <span class="c1"># No need to:</span>
</span><span id="Tracer-229"><a href="#Tracer-229"><span class="linenos">229</span></a>            <span class="c1"># if time_left &lt; 0:</span>
</span><span id="Tracer-230"><a href="#Tracer-230"><span class="linenos">230</span></a>            <span class="c1">#     time_left = 0</span>
</span><span id="Tracer-231"><a href="#Tracer-231"><span class="linenos">231</span></a>            <span class="n">iterations_per_second</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">/</span> <span class="n">delta_time</span>
</span><span id="Tracer-232"><a href="#Tracer-232"><span class="linenos">232</span></a>            <span class="n">iterations_left</span> <span class="o">=</span> <span class="n">iterations_per_second</span> <span class="o">*</span> <span class="n">time_left</span>
</span><span id="Tracer-233"><a href="#Tracer-233"><span class="linenos">233</span></a>            <span class="k">if</span> <span class="n">iterations_left</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="Tracer-234"><a href="#Tracer-234"><span class="linenos">234</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+</span> <span class="nb">round</span><span class="p">(</span><span class="n">iterations_left</span><span class="p">)</span>
</span><span id="Tracer-235"><a href="#Tracer-235"><span class="linenos">235</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run</span>
</span><span id="Tracer-236"><a href="#Tracer-236"><span class="linenos">236</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="Tracer-237"><a href="#Tracer-237"><span class="linenos">237</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="Tracer-238"><a href="#Tracer-238"><span class="linenos">238</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="Tracer-239"><a href="#Tracer-239"><span class="linenos">239</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="Tracer-240"><a href="#Tracer-240"><span class="linenos">240</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_sub_run</span><span class="p">(</span><span class="n">current_time</span><span class="p">)</span>
</span><span id="Tracer-241"><a href="#Tracer-241"><span class="linenos">241</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">*=</span> <span class="mi">2</span>
</span><span id="Tracer-242"><a href="#Tracer-242"><span class="linenos">242</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="Tracer-243"><a href="#Tracer-243"><span class="linenos">243</span></a>
</span><span id="Tracer-244"><a href="#Tracer-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">_last_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-245"><a href="#Tracer-245"><span class="linenos">245</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_sub_run</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">())</span>
</span><span id="Tracer-246"><a href="#Tracer-246"><span class="linenos">246</span></a>
</span><span id="Tracer-247"><a href="#Tracer-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="nf">_last_sub_run</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_time</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-248"><a href="#Tracer-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="n">current_time</span>
</span><span id="Tracer-249"><a href="#Tracer-249"><span class="linenos">249</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="Tracer-250"><a href="#Tracer-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span>
</span><span id="Tracer-251"><a href="#Tracer-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="Tracer-252"><a href="#Tracer-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="Tracer-253"><a href="#Tracer-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="Tracer-254"><a href="#Tracer-254"><span class="linenos">254</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="Tracer-255"><a href="#Tracer-255"><span class="linenos">255</span></a>
</span><span id="Tracer-256"><a href="#Tracer-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Tracer-257"><a href="#Tracer-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="Tracer-258"><a href="#Tracer-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


            <div class="docstring"><p>Main tracer.
Its task is to find out the speed of code execution, and to stop the counting at about the specified time.</p>

<p>Example of use:</p>

<pre><code>tr = Tracer(10.0)
while tr.iter():
    i = '456'
    k = int('1243' + i)

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))
</code></pre>
</div>


                            <div id="Tracer.__init__" class="classattr">
                                        <input id="Tracer.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Tracer</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">clock_type</span><span class="p">:</span> <span class="n"><a href="#ClockType">ClockType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#ClockType.perf_counter">ClockType.perf_counter</a></span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="Tracer.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Tracer.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Tracer.__init__-181"><a href="#Tracer.__init__-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">:</span> <span class="n">ClockType</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="Tracer.__init__-182"><a href="#Tracer.__init__-182"><span class="linenos">182</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="Tracer.__init__-183"><a href="#Tracer.__init__-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_testing_worker</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_test_runs</span>
</span><span id="Tracer.__init__-184"><a href="#Tracer.__init__-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span> <span class="o">/</span> <span class="mi">2</span>
</span><span id="Tracer.__init__-185"><a href="#Tracer.__init__-185"><span class="linenos">185</span></a>        <span class="k">if</span> <span class="mf">0.0</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_half_of_the_run_time</span><span class="p">:</span>
</span><span id="Tracer.__init__-186"><a href="#Tracer.__init__-186"><span class="linenos">186</span></a>            <span class="k">raise</span> <span class="n">TimeLimitIsTooSmall</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="Tracer.__init__-187"><a href="#Tracer.__init__-187"><span class="linenos">187</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Tracer.__init__-188"><a href="#Tracer.__init__-188"><span class="linenos">188</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Tracer.__init__-189"><a href="#Tracer.__init__-189"><span class="linenos">189</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Tracer.__init__-190"><a href="#Tracer.__init__-190"><span class="linenos">190</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_next_test_stop_on</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Tracer.__init__-191"><a href="#Tracer.__init__-191"><span class="linenos">191</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span></pre></div>


    

                            </div>
                            <div id="Tracer.iter" class="classattr">
                                <div class="attr variable">
            <span class="name">iter</span>

        
    </div>
    <a class="headerlink" href="#Tracer.iter"></a>
    
    

                            </div>
                            <div id="Tracer.iter_per_time_unit" class="classattr">
                                        <input id="Tracer.iter_per_time_unit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">iter_per_time_unit</span><span class="annotation">: float</span>

                <label class="view-source-button" for="Tracer.iter_per_time_unit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Tracer.iter_per_time_unit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Tracer.iter_per_time_unit-193"><a href="#Tracer.iter_per_time_unit-193"><span class="linenos">193</span></a>    <span class="nd">@property</span>
</span><span id="Tracer.iter_per_time_unit-194"><a href="#Tracer.iter_per_time_unit-194"><span class="linenos">194</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="Tracer.iter_per_time_unit-195"><a href="#Tracer.iter_per_time_unit-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="Tracer.iter_per_time_unit-196"><a href="#Tracer.iter_per_time_unit-196"><span class="linenos">196</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_start_time</span>
</span><span id="Tracer.iter_per_time_unit-197"><a href="#Tracer.iter_per_time_unit-197"><span class="linenos">197</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="Tracer.iter_per_time_unit-198"><a href="#Tracer.iter_per_time_unit-198"><span class="linenos">198</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_end</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_number_of_iterations_at_start</span><span class="p">)</span> \
</span><span id="Tracer.iter_per_time_unit-199"><a href="#Tracer.iter_per_time_unit-199"><span class="linenos">199</span></a>                       <span class="o">/</span> <span class="n">divider</span>
</span><span id="Tracer.iter_per_time_unit-200"><a href="#Tracer.iter_per_time_unit-200"><span class="linenos">200</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="Tracer.iter_per_time_unit-201"><a href="#Tracer.iter_per_time_unit-201"><span class="linenos">201</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Tracer.iter_per_time_unit-202"><a href="#Tracer.iter_per_time_unit-202"><span class="linenos">202</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="Tracer.iter_per_time_unit-203"><a href="#Tracer.iter_per_time_unit-203"><span class="linenos">203</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="Tracer.iter_per_time_unit-204"><a href="#Tracer.iter_per_time_unit-204"><span class="linenos">204</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="Tracer.iter_per_time_unit-205"><a href="#Tracer.iter_per_time_unit-205"><span class="linenos">205</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#BaseTracer">BaseTracer</a></dt>
                                <dd id="Tracer.iterations_made" class="variable"><a href="#BaseTracer.iterations_made">iterations_made</a></dd>
                <dd id="Tracer.total_number_of_iterations_made" class="variable"><a href="#BaseTracer.total_number_of_iterations_made">total_number_of_iterations_made</a></dd>
                <dd id="Tracer.time_spent" class="variable"><a href="#BaseTracer.time_spent">time_spent</a></dd>
                <dd id="Tracer.total_amount_of_time_spent" class="variable"><a href="#BaseTracer.total_amount_of_time_spent">total_amount_of_time_spent</a></dd>
                <dd id="Tracer.clock_type" class="variable"><a href="#BaseTracer.clock_type">clock_type</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="GreedyTracer">
                            <input id="GreedyTracer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">GreedyTracer</span><wbr>(<span class="base"><a href="#BaseTracer">BaseTracer</a></span>):

                <label class="view-source-button" for="GreedyTracer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GreedyTracer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GreedyTracer-261"><a href="#GreedyTracer-261"><span class="linenos">261</span></a><span class="k">class</span> <span class="nc">GreedyTracer</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="GreedyTracer-262"><a href="#GreedyTracer-262"><span class="linenos">262</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="GreedyTracer-263"><a href="#GreedyTracer-263"><span class="linenos">263</span></a><span class="sd">    Greedy Main tracer.</span>
</span><span id="GreedyTracer-264"><a href="#GreedyTracer-264"><span class="linenos">264</span></a><span class="sd">    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.</span>
</span><span id="GreedyTracer-265"><a href="#GreedyTracer-265"><span class="linenos">265</span></a><span class="sd">    The difference is that he checks time every single iteration.</span>
</span><span id="GreedyTracer-266"><a href="#GreedyTracer-266"><span class="linenos">266</span></a>
</span><span id="GreedyTracer-267"><a href="#GreedyTracer-267"><span class="linenos">267</span></a><span class="sd">    Example of use is the same as for the Tracer()</span>
</span><span id="GreedyTracer-268"><a href="#GreedyTracer-268"><span class="linenos">268</span></a>
</span><span id="GreedyTracer-269"><a href="#GreedyTracer-269"><span class="linenos">269</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="GreedyTracer-270"><a href="#GreedyTracer-270"><span class="linenos">270</span></a>
</span><span id="GreedyTracer-271"><a href="#GreedyTracer-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="GreedyTracer-272"><a href="#GreedyTracer-272"><span class="linenos">272</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="GreedyTracer-273"><a href="#GreedyTracer-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="GreedyTracer-274"><a href="#GreedyTracer-274"><span class="linenos">274</span></a>
</span><span id="GreedyTracer-275"><a href="#GreedyTracer-275"><span class="linenos">275</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="GreedyTracer-276"><a href="#GreedyTracer-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="GreedyTracer-277"><a href="#GreedyTracer-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="GreedyTracer-278"><a href="#GreedyTracer-278"><span class="linenos">278</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span><span class="p">()</span>
</span><span id="GreedyTracer-279"><a href="#GreedyTracer-279"><span class="linenos">279</span></a>
</span><span id="GreedyTracer-280"><a href="#GreedyTracer-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="GreedyTracer-281"><a href="#GreedyTracer-281"><span class="linenos">281</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="GreedyTracer-282"><a href="#GreedyTracer-282"><span class="linenos">282</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="GreedyTracer-283"><a href="#GreedyTracer-283"><span class="linenos">283</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="GreedyTracer-284"><a href="#GreedyTracer-284"><span class="linenos">284</span></a>        
</span><span id="GreedyTracer-285"><a href="#GreedyTracer-285"><span class="linenos">285</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span><span class="p">)</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">:</span>
</span><span id="GreedyTracer-286"><a href="#GreedyTracer-286"><span class="linenos">286</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="GreedyTracer-287"><a href="#GreedyTracer-287"><span class="linenos">287</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="GreedyTracer-288"><a href="#GreedyTracer-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="GreedyTracer-289"><a href="#GreedyTracer-289"><span class="linenos">289</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="GreedyTracer-290"><a href="#GreedyTracer-290"><span class="linenos">290</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="GreedyTracer-291"><a href="#GreedyTracer-291"><span class="linenos">291</span></a>
</span><span id="GreedyTracer-292"><a href="#GreedyTracer-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="GreedyTracer-293"><a href="#GreedyTracer-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="GreedyTracer-294"><a href="#GreedyTracer-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="GreedyTracer-295"><a href="#GreedyTracer-295"><span class="linenos">295</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="GreedyTracer-296"><a href="#GreedyTracer-296"><span class="linenos">296</span></a>
</span><span id="GreedyTracer-297"><a href="#GreedyTracer-297"><span class="linenos">297</span></a>    <span class="nd">@property</span>
</span><span id="GreedyTracer-298"><a href="#GreedyTracer-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="GreedyTracer-299"><a href="#GreedyTracer-299"><span class="linenos">299</span></a>        <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="GreedyTracer-300"><a href="#GreedyTracer-300"><span class="linenos">300</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="GreedyTracer-301"><a href="#GreedyTracer-301"><span class="linenos">301</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="GreedyTracer-302"><a href="#GreedyTracer-302"><span class="linenos">302</span></a>        <span class="k">return</span> <span class="mi">0</span>
</span></pre></div>


            <div class="docstring"><p>Greedy Main tracer.
Its task is to find out the speed of code execution, and to stop the counting at about the specified time.
The difference is that he checks time every single iteration.</p>

<p>Example of use is the same as for the Tracer()</p>
</div>


                            <div id="GreedyTracer.__init__" class="classattr">
                                        <input id="GreedyTracer.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">GreedyTracer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span>, </span><span class="param"><span class="n">clock_type</span><span class="o">=&lt;</span><span class="n"><a href="#ClockType.perf_counter">ClockType.perf_counter</a></span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="GreedyTracer.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GreedyTracer.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GreedyTracer.__init__-271"><a href="#GreedyTracer.__init__-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">):</span>
</span><span id="GreedyTracer.__init__-272"><a href="#GreedyTracer.__init__-272"><span class="linenos">272</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="GreedyTracer.__init__-273"><a href="#GreedyTracer.__init__-273"><span class="linenos">273</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span></pre></div>


    

                            </div>
                            <div id="GreedyTracer.iter" class="classattr">
                                <div class="attr variable">
            <span class="name">iter</span>

        
    </div>
    <a class="headerlink" href="#GreedyTracer.iter"></a>
    
    

                            </div>
                            <div id="GreedyTracer.iter_per_time_unit" class="classattr">
                                        <input id="GreedyTracer.iter_per_time_unit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">iter_per_time_unit</span><span class="annotation">: float</span>

                <label class="view-source-button" for="GreedyTracer.iter_per_time_unit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GreedyTracer.iter_per_time_unit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GreedyTracer.iter_per_time_unit-297"><a href="#GreedyTracer.iter_per_time_unit-297"><span class="linenos">297</span></a>    <span class="nd">@property</span>
</span><span id="GreedyTracer.iter_per_time_unit-298"><a href="#GreedyTracer.iter_per_time_unit-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="GreedyTracer.iter_per_time_unit-299"><a href="#GreedyTracer.iter_per_time_unit-299"><span class="linenos">299</span></a>        <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="GreedyTracer.iter_per_time_unit-300"><a href="#GreedyTracer.iter_per_time_unit-300"><span class="linenos">300</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="GreedyTracer.iter_per_time_unit-301"><a href="#GreedyTracer.iter_per_time_unit-301"><span class="linenos">301</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="GreedyTracer.iter_per_time_unit-302"><a href="#GreedyTracer.iter_per_time_unit-302"><span class="linenos">302</span></a>        <span class="k">return</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#BaseTracer">BaseTracer</a></dt>
                                <dd id="GreedyTracer.iterations_made" class="variable"><a href="#BaseTracer.iterations_made">iterations_made</a></dd>
                <dd id="GreedyTracer.total_number_of_iterations_made" class="variable"><a href="#BaseTracer.total_number_of_iterations_made">total_number_of_iterations_made</a></dd>
                <dd id="GreedyTracer.time_spent" class="variable"><a href="#BaseTracer.time_spent">time_spent</a></dd>
                <dd id="GreedyTracer.total_amount_of_time_spent" class="variable"><a href="#BaseTracer.total_amount_of_time_spent">total_amount_of_time_spent</a></dd>
                <dd id="GreedyTracer.clock_type" class="variable"><a href="#BaseTracer.clock_type">clock_type</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TracerCounter">
                            <input id="TracerCounter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TracerCounter</span><wbr>(<span class="base"><a href="#BaseTracer">BaseTracer</a></span>):

                <label class="view-source-button" for="TracerCounter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerCounter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerCounter-305"><a href="#TracerCounter-305"><span class="linenos">305</span></a><span class="k">class</span> <span class="nc">TracerCounter</span><span class="p">(</span><span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="TracerCounter-306"><a href="#TracerCounter-306"><span class="linenos">306</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TracerCounter-307"><a href="#TracerCounter-307"><span class="linenos">307</span></a><span class="sd">    Counting tracer. Pseudo-tracer.</span>
</span><span id="TracerCounter-308"><a href="#TracerCounter-308"><span class="linenos">308</span></a><span class="sd">    Its don&#39;t have an overhead of periodic calling time() function.</span>
</span><span id="TracerCounter-309"><a href="#TracerCounter-309"><span class="linenos">309</span></a><span class="sd">    Its task is to count down within a given time, using the speed information already counted by the real tracer</span>
</span><span id="TracerCounter-310"><a href="#TracerCounter-310"><span class="linenos">310</span></a><span class="sd">    (by the Tracer class).</span>
</span><span id="TracerCounter-311"><a href="#TracerCounter-311"><span class="linenos">311</span></a>
</span><span id="TracerCounter-312"><a href="#TracerCounter-312"><span class="linenos">312</span></a><span class="sd">    Example of use:</span>
</span><span id="TracerCounter-313"><a href="#TracerCounter-313"><span class="linenos">313</span></a>
</span><span id="TracerCounter-314"><a href="#TracerCounter-314"><span class="linenos">314</span></a><span class="sd">        trc = TracerCounter(10000, 10.0)</span>
</span><span id="TracerCounter-315"><a href="#TracerCounter-315"><span class="linenos">315</span></a><span class="sd">        while trc.iter():</span>
</span><span id="TracerCounter-316"><a href="#TracerCounter-316"><span class="linenos">316</span></a><span class="sd">            i = &#39;456&#39;</span>
</span><span id="TracerCounter-317"><a href="#TracerCounter-317"><span class="linenos">317</span></a><span class="sd">            k = int(&#39;1243&#39; + i)</span>
</span><span id="TracerCounter-318"><a href="#TracerCounter-318"><span class="linenos">318</span></a>
</span><span id="TracerCounter-319"><a href="#TracerCounter-319"><span class="linenos">319</span></a><span class="sd">        print(&#39;{} iter/s; {} seconds; {} iters&#39;.format(trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))</span>
</span><span id="TracerCounter-320"><a href="#TracerCounter-320"><span class="linenos">320</span></a>
</span><span id="TracerCounter-321"><a href="#TracerCounter-321"><span class="linenos">321</span></a><span class="sd">    or:</span>
</span><span id="TracerCounter-322"><a href="#TracerCounter-322"><span class="linenos">322</span></a><span class="sd">        def made_tests() -&gt; Tracer:</span>
</span><span id="TracerCounter-323"><a href="#TracerCounter-323"><span class="linenos">323</span></a><span class="sd">            tr = Tracer(0.1)  # Run for about 0.1 of second.</span>
</span><span id="TracerCounter-324"><a href="#TracerCounter-324"><span class="linenos">324</span></a><span class="sd">            while tr.iter():</span>
</span><span id="TracerCounter-325"><a href="#TracerCounter-325"><span class="linenos">325</span></a><span class="sd">                some_my_code()</span>
</span><span id="TracerCounter-326"><a href="#TracerCounter-326"><span class="linenos">326</span></a><span class="sd">            return tr</span>
</span><span id="TracerCounter-327"><a href="#TracerCounter-327"><span class="linenos">327</span></a>
</span><span id="TracerCounter-328"><a href="#TracerCounter-328"><span class="linenos">328</span></a><span class="sd">        def run(run_time: float, tests_result: Tracer):</span>
</span><span id="TracerCounter-329"><a href="#TracerCounter-329"><span class="linenos">329</span></a><span class="sd">            trc = TracerCounter(tests_result.iter_per_time_unit, run_time)</span>
</span><span id="TracerCounter-330"><a href="#TracerCounter-330"><span class="linenos">330</span></a><span class="sd">            while trc.iter():</span>
</span><span id="TracerCounter-331"><a href="#TracerCounter-331"><span class="linenos">331</span></a><span class="sd">                some_my_code()</span>
</span><span id="TracerCounter-332"><a href="#TracerCounter-332"><span class="linenos">332</span></a>
</span><span id="TracerCounter-333"><a href="#TracerCounter-333"><span class="linenos">333</span></a><span class="sd">            print(&#39;{} iter/s; {} seconds; {} iterations&#39;.format(trc.iter_per_time_unit, trc.time_spent,</span>
</span><span id="TracerCounter-334"><a href="#TracerCounter-334"><span class="linenos">334</span></a><span class="sd">                    trc.iterations_made))</span>
</span><span id="TracerCounter-335"><a href="#TracerCounter-335"><span class="linenos">335</span></a>
</span><span id="TracerCounter-336"><a href="#TracerCounter-336"><span class="linenos">336</span></a><span class="sd">        def main():</span>
</span><span id="TracerCounter-337"><a href="#TracerCounter-337"><span class="linenos">337</span></a><span class="sd">            tests_result = made_tests()</span>
</span><span id="TracerCounter-338"><a href="#TracerCounter-338"><span class="linenos">338</span></a><span class="sd">            ...</span>
</span><span id="TracerCounter-339"><a href="#TracerCounter-339"><span class="linenos">339</span></a><span class="sd">            while True:</span>
</span><span id="TracerCounter-340"><a href="#TracerCounter-340"><span class="linenos">340</span></a><span class="sd">                time_to_rur_str = input(&#39;Enter run time: &#39;)</span>
</span><span id="TracerCounter-341"><a href="#TracerCounter-341"><span class="linenos">341</span></a><span class="sd">                if not time_to_run_str:</span>
</span><span id="TracerCounter-342"><a href="#TracerCounter-342"><span class="linenos">342</span></a><span class="sd">                    break</span>
</span><span id="TracerCounter-343"><a href="#TracerCounter-343"><span class="linenos">343</span></a><span class="sd">                run(float(time_to_rur_str), tests_result)</span>
</span><span id="TracerCounter-344"><a href="#TracerCounter-344"><span class="linenos">344</span></a>
</span><span id="TracerCounter-345"><a href="#TracerCounter-345"><span class="linenos">345</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="TracerCounter-346"><a href="#TracerCounter-346"><span class="linenos">346</span></a>
</span><span id="TracerCounter-347"><a href="#TracerCounter-347"><span class="linenos">347</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iter_per_time_unit</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">fake</span><span class="p">):</span>
</span><span id="TracerCounter-348"><a href="#TracerCounter-348"><span class="linenos">348</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="TracerCounter-349"><a href="#TracerCounter-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">=</span> <span class="n">iter_per_time_unit</span>
</span><span id="TracerCounter-350"><a href="#TracerCounter-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations_needed</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">)</span>
</span><span id="TracerCounter-351"><a href="#TracerCounter-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span><span id="TracerCounter-352"><a href="#TracerCounter-352"><span class="linenos">352</span></a>
</span><span id="TracerCounter-353"><a href="#TracerCounter-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">_first_run</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TracerCounter-354"><a href="#TracerCounter-354"><span class="linenos">354</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="TracerCounter-355"><a href="#TracerCounter-355"><span class="linenos">355</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span>
</span><span id="TracerCounter-356"><a href="#TracerCounter-356"><span class="linenos">356</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_subsequent_runs</span><span class="p">()</span>
</span><span id="TracerCounter-357"><a href="#TracerCounter-357"><span class="linenos">357</span></a>
</span><span id="TracerCounter-358"><a href="#TracerCounter-358"><span class="linenos">358</span></a>    <span class="k">def</span> <span class="nf">_subsequent_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TracerCounter-359"><a href="#TracerCounter-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TracerCounter-360"><a href="#TracerCounter-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span>
</span><span id="TracerCounter-361"><a href="#TracerCounter-361"><span class="linenos">361</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations_needed</span><span class="p">:</span>
</span><span id="TracerCounter-362"><a href="#TracerCounter-362"><span class="linenos">362</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="TracerCounter-363"><a href="#TracerCounter-363"><span class="linenos">363</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TracerCounter-364"><a href="#TracerCounter-364"><span class="linenos">364</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="TracerCounter-365"><a href="#TracerCounter-365"><span class="linenos">365</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TracerCounter-366"><a href="#TracerCounter-366"><span class="linenos">366</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_after_last_runs</span>
</span><span id="TracerCounter-367"><a href="#TracerCounter-367"><span class="linenos">367</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TracerCounter-368"><a href="#TracerCounter-368"><span class="linenos">368</span></a>
</span><span id="TracerCounter-369"><a href="#TracerCounter-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">_after_last_runs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TracerCounter-370"><a href="#TracerCounter-370"><span class="linenos">370</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TracerCounter-371"><a href="#TracerCounter-371"><span class="linenos">371</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_time</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_clock</span><span class="p">()</span>
</span><span id="TracerCounter-372"><a href="#TracerCounter-372"><span class="linenos">372</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="TracerCounter-373"><a href="#TracerCounter-373"><span class="linenos">373</span></a>
</span><span id="TracerCounter-374"><a href="#TracerCounter-374"><span class="linenos">374</span></a>    <span class="nd">@property</span>
</span><span id="TracerCounter-375"><a href="#TracerCounter-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="TracerCounter-376"><a href="#TracerCounter-376"><span class="linenos">376</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="TracerCounter-377"><a href="#TracerCounter-377"><span class="linenos">377</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="TracerCounter-378"><a href="#TracerCounter-378"><span class="linenos">378</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="TracerCounter-379"><a href="#TracerCounter-379"><span class="linenos">379</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="TracerCounter-380"><a href="#TracerCounter-380"><span class="linenos">380</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="TracerCounter-381"><a href="#TracerCounter-381"><span class="linenos">381</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TracerCounter-382"><a href="#TracerCounter-382"><span class="linenos">382</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span>
</span></pre></div>


            <div class="docstring"><p>Counting tracer. Pseudo-tracer.
Its don't have an overhead of periodic calling time() function.
Its task is to count down within a given time, using the speed information already counted by the real tracer
(by the Tracer class).</p>

<p>Example of use:</p>

<pre><code>trc = TracerCounter(10000, 10.0)
while trc.iter():
    i = '456'
    k = int('1243' + i)

print('{} iter/s; {} seconds; {} iters'.format(trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))
</code></pre>

<p>or:
    def made_tests() -> Tracer:
        tr = Tracer(0.1)  # Run for about 0.1 of second.
        while tr.iter():
            some_my_code()
        return tr</p>

<pre><code>def run(run_time: float, tests_result: Tracer):
    trc = TracerCounter(tests_result.iter_per_time_unit, run_time)
    while trc.iter():
        some_my_code()

    print('{} iter/s; {} seconds; {} iterations'.format(trc.iter_per_time_unit, trc.time_spent,
            trc.iterations_made))

def main():
    tests_result = made_tests()
    ...
    while True:
        time_to_rur_str = input('Enter run time: ')
        if not time_to_run_str:
            break
        run(float(time_to_rur_str), tests_result)
</code></pre>
</div>


                            <div id="TracerCounter.__init__" class="classattr">
                                        <input id="TracerCounter.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TracerCounter</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">iter_per_time_unit</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">clock_type</span><span class="o">=&lt;</span><span class="n"><a href="#ClockType.fake">ClockType.fake</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="TracerCounter.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerCounter.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerCounter.__init__-347"><a href="#TracerCounter.__init__-347"><span class="linenos">347</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iter_per_time_unit</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">run_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">clock_type</span><span class="o">=</span><span class="n">ClockType</span><span class="o">.</span><span class="n">fake</span><span class="p">):</span>
</span><span id="TracerCounter.__init__-348"><a href="#TracerCounter.__init__-348"><span class="linenos">348</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">run_time</span><span class="p">,</span> <span class="n">clock_type</span><span class="p">)</span>
</span><span id="TracerCounter.__init__-349"><a href="#TracerCounter.__init__-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">=</span> <span class="n">iter_per_time_unit</span>
</span><span id="TracerCounter.__init__-350"><a href="#TracerCounter.__init__-350"><span class="linenos">350</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_number_of_iterations_needed</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_run_time</span><span class="p">)</span>
</span><span id="TracerCounter.__init__-351"><a href="#TracerCounter.__init__-351"><span class="linenos">351</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iter</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_first_run</span>
</span></pre></div>


    

                            </div>
                            <div id="TracerCounter.iter" class="classattr">
                                <div class="attr variable">
            <span class="name">iter</span>

        
    </div>
    <a class="headerlink" href="#TracerCounter.iter"></a>
    
    

                            </div>
                            <div id="TracerCounter.iter_per_time_unit" class="classattr">
                                        <input id="TracerCounter.iter_per_time_unit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">iter_per_time_unit</span><span class="annotation">: float</span>

                <label class="view-source-button" for="TracerCounter.iter_per_time_unit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerCounter.iter_per_time_unit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerCounter.iter_per_time_unit-374"><a href="#TracerCounter.iter_per_time_unit-374"><span class="linenos">374</span></a>    <span class="nd">@property</span>
</span><span id="TracerCounter.iter_per_time_unit-375"><a href="#TracerCounter.iter_per_time_unit-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">iter_per_time_unit</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
</span><span id="TracerCounter.iter_per_time_unit-376"><a href="#TracerCounter.iter_per_time_unit-376"><span class="linenos">376</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_run_was_made</span><span class="p">:</span>
</span><span id="TracerCounter.iter_per_time_unit-377"><a href="#TracerCounter.iter_per_time_unit-377"><span class="linenos">377</span></a>            <span class="n">divider</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_relevant_stop_time</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_start_time</span>
</span><span id="TracerCounter.iter_per_time_unit-378"><a href="#TracerCounter.iter_per_time_unit-378"><span class="linenos">378</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="o">!=</span> <span class="n">divider</span><span class="p">:</span>
</span><span id="TracerCounter.iter_per_time_unit-379"><a href="#TracerCounter.iter_per_time_unit-379"><span class="linenos">379</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_last_tracked_number_of_iterations</span> <span class="o">/</span> <span class="n">divider</span>
</span><span id="TracerCounter.iter_per_time_unit-380"><a href="#TracerCounter.iter_per_time_unit-380"><span class="linenos">380</span></a>            <span class="k">return</span> <span class="mi">0</span>
</span><span id="TracerCounter.iter_per_time_unit-381"><a href="#TracerCounter.iter_per_time_unit-381"><span class="linenos">381</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TracerCounter.iter_per_time_unit-382"><a href="#TracerCounter.iter_per_time_unit-382"><span class="linenos">382</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_iter_per_time_unit</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#BaseTracer">BaseTracer</a></dt>
                                <dd id="TracerCounter.iterations_made" class="variable"><a href="#BaseTracer.iterations_made">iterations_made</a></dd>
                <dd id="TracerCounter.total_number_of_iterations_made" class="variable"><a href="#BaseTracer.total_number_of_iterations_made">total_number_of_iterations_made</a></dd>
                <dd id="TracerCounter.time_spent" class="variable"><a href="#BaseTracer.time_spent">time_spent</a></dd>
                <dd id="TracerCounter.total_amount_of_time_spent" class="variable"><a href="#BaseTracer.total_amount_of_time_spent">total_amount_of_time_spent</a></dd>
                <dd id="TracerCounter.clock_type" class="variable"><a href="#BaseTracer.clock_type">clock_type</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TracerIterator">
                            <input id="TracerIterator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TracerIterator</span>:

                <label class="view-source-button" for="TracerIterator-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerIterator"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerIterator-385"><a href="#TracerIterator-385"><span class="linenos">385</span></a><span class="k">class</span> <span class="nc">TracerIterator</span><span class="p">:</span>
</span><span id="TracerIterator-386"><a href="#TracerIterator-386"><span class="linenos">386</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TracerIterator-387"><a href="#TracerIterator-387"><span class="linenos">387</span></a><span class="sd">    An iterator class. It converts any type of given tracer into an iterator.</span>
</span><span id="TracerIterator-388"><a href="#TracerIterator-388"><span class="linenos">388</span></a>
</span><span id="TracerIterator-389"><a href="#TracerIterator-389"><span class="linenos">389</span></a><span class="sd">    As result you have an option to use constructions like this:</span>
</span><span id="TracerIterator-390"><a href="#TracerIterator-390"><span class="linenos">390</span></a>
</span><span id="TracerIterator-391"><a href="#TracerIterator-391"><span class="linenos">391</span></a><span class="sd">        for i in TracerIterator(Tracer(20.0)):</span>
</span><span id="TracerIterator-392"><a href="#TracerIterator-392"><span class="linenos">392</span></a><span class="sd">            k = int(&#39;1243&#39;)</span>
</span><span id="TracerIterator-393"><a href="#TracerIterator-393"><span class="linenos">393</span></a>
</span><span id="TracerIterator-394"><a href="#TracerIterator-394"><span class="linenos">394</span></a><span class="sd">    But keep in mind that in this case there will be a bigger overhead. And there will be less CPU time for the payload.</span>
</span><span id="TracerIterator-395"><a href="#TracerIterator-395"><span class="linenos">395</span></a>
</span><span id="TracerIterator-396"><a href="#TracerIterator-396"><span class="linenos">396</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="TracerIterator-397"><a href="#TracerIterator-397"><span class="linenos">397</span></a>
</span><span id="TracerIterator-398"><a href="#TracerIterator-398"><span class="linenos">398</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tracer</span><span class="p">:</span> <span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="TracerIterator-399"><a href="#TracerIterator-399"><span class="linenos">399</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span> <span class="o">=</span> <span class="n">tracer</span>
</span><span id="TracerIterator-400"><a href="#TracerIterator-400"><span class="linenos">400</span></a>
</span><span id="TracerIterator-401"><a href="#TracerIterator-401"><span class="linenos">401</span></a>    <span class="k">def</span> <span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TracerIterator-402"><a href="#TracerIterator-402"><span class="linenos">402</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="TracerIterator-403"><a href="#TracerIterator-403"><span class="linenos">403</span></a>
</span><span id="TracerIterator-404"><a href="#TracerIterator-404"><span class="linenos">404</span></a>    <span class="k">def</span> <span class="fm">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TracerIterator-405"><a href="#TracerIterator-405"><span class="linenos">405</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="TracerIterator-406"><a href="#TracerIterator-406"><span class="linenos">406</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iterations_made</span>
</span><span id="TracerIterator-407"><a href="#TracerIterator-407"><span class="linenos">407</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TracerIterator-408"><a href="#TracerIterator-408"><span class="linenos">408</span></a>            <span class="k">raise</span> <span class="ne">StopIteration</span><span class="p">()</span>
</span><span id="TracerIterator-409"><a href="#TracerIterator-409"><span class="linenos">409</span></a>
</span><span id="TracerIterator-410"><a href="#TracerIterator-410"><span class="linenos">410</span></a>    <span class="nb">next</span> <span class="o">=</span> <span class="fm">__next__</span>
</span><span id="TracerIterator-411"><a href="#TracerIterator-411"><span class="linenos">411</span></a>
</span><span id="TracerIterator-412"><a href="#TracerIterator-412"><span class="linenos">412</span></a>    <span class="nd">@property</span>
</span><span id="TracerIterator-413"><a href="#TracerIterator-413"><span class="linenos">413</span></a>    <span class="k">def</span> <span class="nf">tracer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TracerIterator-414"><a href="#TracerIterator-414"><span class="linenos">414</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span>
</span></pre></div>


            <div class="docstring"><p>An iterator class. It converts any type of given tracer into an iterator.</p>

<p>As result you have an option to use constructions like this:</p>

<pre><code>for i in TracerIterator(Tracer(20.0)):
    k = int('1243')
</code></pre>

<p>But keep in mind that in this case there will be a bigger overhead. And there will be less CPU time for the payload.</p>
</div>


                            <div id="TracerIterator.__init__" class="classattr">
                                        <input id="TracerIterator.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TracerIterator</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">tracer</span><span class="p">:</span> <span class="n"><a href="#BaseTracer">BaseTracer</a></span></span>)</span>

                <label class="view-source-button" for="TracerIterator.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerIterator.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerIterator.__init__-398"><a href="#TracerIterator.__init__-398"><span class="linenos">398</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tracer</span><span class="p">:</span> <span class="n">BaseTracer</span><span class="p">):</span>
</span><span id="TracerIterator.__init__-399"><a href="#TracerIterator.__init__-399"><span class="linenos">399</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span> <span class="o">=</span> <span class="n">tracer</span>
</span></pre></div>


    

                            </div>
                            <div id="TracerIterator.next" class="classattr">
                                        <input id="TracerIterator.next-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">next</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TracerIterator.next-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerIterator.next"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerIterator.next-404"><a href="#TracerIterator.next-404"><span class="linenos">404</span></a>    <span class="k">def</span> <span class="fm">__next__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TracerIterator.next-405"><a href="#TracerIterator.next-405"><span class="linenos">405</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="TracerIterator.next-406"><a href="#TracerIterator.next-406"><span class="linenos">406</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span><span class="o">.</span><span class="n">iterations_made</span>
</span><span id="TracerIterator.next-407"><a href="#TracerIterator.next-407"><span class="linenos">407</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TracerIterator.next-408"><a href="#TracerIterator.next-408"><span class="linenos">408</span></a>            <span class="k">raise</span> <span class="ne">StopIteration</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TracerIterator.tracer" class="classattr">
                                        <input id="TracerIterator.tracer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">tracer</span>

                <label class="view-source-button" for="TracerIterator.tracer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TracerIterator.tracer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TracerIterator.tracer-412"><a href="#TracerIterator.tracer-412"><span class="linenos">412</span></a>    <span class="nd">@property</span>
</span><span id="TracerIterator.tracer-413"><a href="#TracerIterator.tracer-413"><span class="linenos">413</span></a>    <span class="k">def</span> <span class="nf">tracer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TracerIterator.tracer-414"><a href="#TracerIterator.tracer-414"><span class="linenos">414</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tracer</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>