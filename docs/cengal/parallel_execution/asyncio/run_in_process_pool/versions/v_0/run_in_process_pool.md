---
title: run_in_process_pool
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.asyncio<wbr>.run_in_process_pool<wbr>.versions<wbr>.v_0<wbr>.run_in_process_pool    </h1>

                
                        <input id="mod-run_in_process_pool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-run_in_process_pool-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;run_coroutine_in_new_thread&#39;</span><span class="p">,</span> <span class="s1">&#39;ProcessPoolRuntimeError&#39;</span><span class="p">,</span> <span class="s1">&#39;ExecutorSetupBase&#39;</span><span class="p">,</span> <span class="s1">&#39;ExecutorTypeSetup&#39;</span><span class="p">,</span> <span class="s1">&#39;ExecutorInstanceSetup&#39;</span><span class="p">,</span> <span class="s1">&#39;InitializerSetup&#39;</span><span class="p">,</span> <span class="s1">&#39;ProcessPoolSetup&#39;</span><span class="p">,</span> <span class="s1">&#39;ProcessPool&#39;</span><span class="p">]</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="sd">Module Docstring</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">is_async</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ResultHolder</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">concurrent.futures</span> <span class="kn">import</span> <span class="n">Executor</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">threading</span> <span class="kn">import</span> <span class="n">Thread</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">partial</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Tuple</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">class</span> <span class="nc">ProcessPoolRuntimeError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">):</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="k">pass</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="k">class</span> <span class="nc">ExecutorSetupBase</span><span class="p">:</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">pass</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="k">class</span> <span class="nc">ExecutorTypeSetup</span><span class="p">(</span><span class="n">ExecutorSetupBase</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">]</span> <span class="o">=</span> <span class="n">executor_type</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="k">class</span> <span class="nc">ExecutorInstanceSetup</span><span class="p">(</span><span class="n">ExecutorSetupBase</span><span class="p">):</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="n">executor</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">InitializerSetup</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">initializer</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="k">class</span> <span class="nc">ProcessPoolSetup</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="k">def</span> <span class="nf">run_coroutine_in_new_thread</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="nf">thread_worker</span><span class="p">(</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>            <span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">coro</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span> <span class="o">=</span> <span class="n">ResultHolder</span><span class="p">()</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="n">thread_args</span> <span class="o">=</span> <span class="p">[</span><span class="n">result_holder</span><span class="p">,</span> <span class="n">coro</span><span class="p">,]</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="n">thread</span><span class="p">:</span> <span class="n">Thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">thread_worker</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">thread_args</span><span class="p">,</span> <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;ProcessPool internal error&#39;</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a><span class="k">class</span> <span class="nc">ProcessPool</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span><span class="p">,</span> <span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span> <span class="o">=</span> <span class="n">executor_setup</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">process_pool_setup</span> <span class="ow">or</span> <span class="n">ProcessPoolSetup</span><span class="p">()</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">initializer_setup</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_create_pool</span><span class="p">()</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">set_is_multiprocessing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">_create_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_initializer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">initializer</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">,</span> <span class="n">ExecutorInstanceSetup</span><span class="p">):</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">,</span> <span class="n">ExecutorTypeSetup</span><span class="p">):</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;initializer&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>                
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor_type</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>                <span class="k">raise</span> <span class="n">ProcessPoolRuntimeError</span><span class="p">(</span><span class="s1">&#39;Unknown &quot;executor_setup&quot; parameter type&#39;</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor_type</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">shutdown</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="n">wait</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="n">cancel_futures</span><span class="p">)</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">_initializer</span><span class="p">(</span><span class="n">initializer</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="kn">import</span> <span class="nn">multiprocessing</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">initializer</span><span class="p">(</span><span class="n">multiprocessing</span><span class="o">.</span><span class="n">current_process</span><span class="p">()</span><span class="o">.</span><span class="n">_identity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">_pool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="k">return</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">_apool_worker</span><span class="p">(</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">_apool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="k">return</span> <span class="n">run_coroutine_in_new_thread</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="nf">_apool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">return</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_a_single_process_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_a_single_process_pool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_a_single_process_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pool_execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="k">if</span> <span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">,</span> <span class="n">partial_pool_worker</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                <span class="n">a_single_process_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_a_single_process_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">a_single_process_pool_worker</span><span class="p">()</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>                <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">partial_pool_worker</span><span class="p">()</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="k">raise</span> <span class="n">exception</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pool_execute</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a><span class="c1"># def pool_initializer(text):</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a><span class="c1">#     import multiprocessing</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>    
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="c1">#     print(text, multiprocessing.current_process()._identity[0])</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a><span class="c1"># def create_pool():</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="c1">#     global executor_init_params</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a><span class="c1">#     executor_init_params = ((&#39;hello pool&#39;,), dict())</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a><span class="c1">#     global executor</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a><span class="c1">#     if (3, 7) &lt;= sys.version_info:</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a><span class="c1">#         pool_args, pool_kwargs = executor_init_params</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a><span class="c1">#         partial_pool_initializer = partial(pool_initializer, *pool_args, **pool_kwargs)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a><span class="c1">#         executor = ProcessPoolExecutor(max_workers=2, initializer=partial_pool_initializer)</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="c1">#     else:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="c1">#         executor = ProcessPoolExecutor(max_workers=2)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="c1"># def pool_worker_impl(item: int):</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a><span class="c1">#     return 1000 / item</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a><span class="c1"># def pool_worker(*args, **kwargs):</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a><span class="c1">#     result = None</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a><span class="c1">#     exception = None</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a><span class="c1">#     try:</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a><span class="c1">#         result = pool_worker_impl(*args, **kwargs)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a><span class="c1">#     except:</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="c1">#         exception = get_exception()</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a><span class="c1">#     return result, exception</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a><span class="c1"># def pool_worker_wrapper(pool_init_params, *args, **kwargs):</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a><span class="c1">#     global process_initialized</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a><span class="c1">#     if &#39;process_initialized&#39; not in globals():</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a><span class="c1">#         process_initialized = False</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a><span class="c1">#     if not process_initialized:</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a><span class="c1">#         pool_args, pool_kwargs = pool_init_params</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="c1">#         pool_initializer(*pool_args, **pool_kwargs)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="c1">#         process_initialized = True</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>    
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="c1">#     return pool_worker(*args, **kwargs)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a><span class="c1"># async def pool_execute(*args, **kwargs):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a><span class="c1">#     if (3, 7) &lt;= sys.version_info:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a><span class="c1">#         partial_pool_worker = partial(pool_worker, *args, **kwargs)</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a><span class="c1">#     else:</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a><span class="c1">#         partial_pool_worker = partial(pool_worker_wrapper, executor_init_params, *args, **kwargs)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="c1">#     if is_multiprocessing:</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a><span class="c1">#         result = await loop.run_in_executor(executor, partial_pool_worker)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="c1">#     else:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="c1">#         result = pool_worker(*args, **kwargs)</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a><span class="c1">#     result, exception = result</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="c1">#     if exception is not None:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="c1">#         raise exception</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>    
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a><span class="c1">#     return result</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a><span class="c1"># async def pool_single_processing_example(item: int = 2):</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a><span class="c1">#     return await pool_execute(item)</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a><span class="c1"># async def pool_gather_example(num: int = 3):</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a><span class="c1">#     return await asyncio.gather(*[pool_execute(i) for i in range(num)])</span>
</span></pre></div>


            </section>
                <section id="run_coroutine_in_new_thread">
                            <input id="run_coroutine_in_new_thread-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run_coroutine_in_new_thread</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">coro</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="run_coroutine_in_new_thread-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#run_coroutine_in_new_thread"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="run_coroutine_in_new_thread-84"><a href="#run_coroutine_in_new_thread-84"><span class="linenos"> 84</span></a><span class="k">def</span> <span class="nf">run_coroutine_in_new_thread</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="run_coroutine_in_new_thread-85"><a href="#run_coroutine_in_new_thread-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="nf">thread_worker</span><span class="p">(</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="run_coroutine_in_new_thread-86"><a href="#run_coroutine_in_new_thread-86"><span class="linenos"> 86</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="run_coroutine_in_new_thread-87"><a href="#run_coroutine_in_new_thread-87"><span class="linenos"> 87</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="run_coroutine_in_new_thread-88"><a href="#run_coroutine_in_new_thread-88"><span class="linenos"> 88</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="run_coroutine_in_new_thread-89"><a href="#run_coroutine_in_new_thread-89"><span class="linenos"> 89</span></a>            <span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="run_coroutine_in_new_thread-90"><a href="#run_coroutine_in_new_thread-90"><span class="linenos"> 90</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">coro</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="run_coroutine_in_new_thread-91"><a href="#run_coroutine_in_new_thread-91"><span class="linenos"> 91</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="run_coroutine_in_new_thread-92"><a href="#run_coroutine_in_new_thread-92"><span class="linenos"> 92</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="run_coroutine_in_new_thread-93"><a href="#run_coroutine_in_new_thread-93"><span class="linenos"> 93</span></a>        
</span><span id="run_coroutine_in_new_thread-94"><a href="#run_coroutine_in_new_thread-94"><span class="linenos"> 94</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="run_coroutine_in_new_thread-95"><a href="#run_coroutine_in_new_thread-95"><span class="linenos"> 95</span></a>    
</span><span id="run_coroutine_in_new_thread-96"><a href="#run_coroutine_in_new_thread-96"><span class="linenos"> 96</span></a>    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span> <span class="o">=</span> <span class="n">ResultHolder</span><span class="p">()</span>
</span><span id="run_coroutine_in_new_thread-97"><a href="#run_coroutine_in_new_thread-97"><span class="linenos"> 97</span></a>    <span class="n">thread_args</span> <span class="o">=</span> <span class="p">[</span><span class="n">result_holder</span><span class="p">,</span> <span class="n">coro</span><span class="p">,]</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span>
</span><span id="run_coroutine_in_new_thread-98"><a href="#run_coroutine_in_new_thread-98"><span class="linenos"> 98</span></a>    <span class="n">thread</span><span class="p">:</span> <span class="n">Thread</span> <span class="o">=</span> <span class="n">Thread</span><span class="p">(</span><span class="n">target</span><span class="o">=</span><span class="n">thread_worker</span><span class="p">,</span> <span class="n">args</span><span class="o">=</span><span class="n">thread_args</span><span class="p">,</span> <span class="n">kwargs</span><span class="o">=</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="run_coroutine_in_new_thread-99"><a href="#run_coroutine_in_new_thread-99"><span class="linenos"> 99</span></a>    <span class="n">thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="run_coroutine_in_new_thread-100"><a href="#run_coroutine_in_new_thread-100"><span class="linenos">100</span></a>    <span class="n">thread</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</span><span id="run_coroutine_in_new_thread-101"><a href="#run_coroutine_in_new_thread-101"><span class="linenos">101</span></a>    <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="run_coroutine_in_new_thread-102"><a href="#run_coroutine_in_new_thread-102"><span class="linenos">102</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span>
</span><span id="run_coroutine_in_new_thread-103"><a href="#run_coroutine_in_new_thread-103"><span class="linenos">103</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="run_coroutine_in_new_thread-104"><a href="#run_coroutine_in_new_thread-104"><span class="linenos">104</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="run_coroutine_in_new_thread-105"><a href="#run_coroutine_in_new_thread-105"><span class="linenos">105</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;ProcessPool internal error&#39;</span><span class="p">)</span>
</span><span id="run_coroutine_in_new_thread-106"><a href="#run_coroutine_in_new_thread-106"><span class="linenos">106</span></a>    
</span><span id="run_coroutine_in_new_thread-107"><a href="#run_coroutine_in_new_thread-107"><span class="linenos">107</span></a>    <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span></pre></div>


    

                </section>
                <section id="ProcessPoolRuntimeError">
                            <input id="ProcessPoolRuntimeError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ProcessPoolRuntimeError</span><wbr>(<span class="base">builtins.RuntimeError</span>):

                <label class="view-source-button" for="ProcessPoolRuntimeError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPoolRuntimeError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPoolRuntimeError-49"><a href="#ProcessPoolRuntimeError-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">ProcessPoolRuntimeError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">):</span>
</span><span id="ProcessPoolRuntimeError-50"><a href="#ProcessPoolRuntimeError-50"><span class="linenos">50</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="ProcessPoolRuntimeError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ProcessPoolRuntimeError.with_traceback" class="function">with_traceback</dd>
                <dd id="ProcessPoolRuntimeError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ExecutorSetupBase">
                            <input id="ExecutorSetupBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExecutorSetupBase</span>:

                <label class="view-source-button" for="ExecutorSetupBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExecutorSetupBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExecutorSetupBase-53"><a href="#ExecutorSetupBase-53"><span class="linenos">53</span></a><span class="k">class</span> <span class="nc">ExecutorSetupBase</span><span class="p">:</span>
</span><span id="ExecutorSetupBase-54"><a href="#ExecutorSetupBase-54"><span class="linenos">54</span></a>    <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="ExecutorTypeSetup">
                            <input id="ExecutorTypeSetup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExecutorTypeSetup</span><wbr>(<span class="base"><a href="#ExecutorSetupBase">ExecutorSetupBase</a></span>):

                <label class="view-source-button" for="ExecutorTypeSetup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExecutorTypeSetup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExecutorTypeSetup-57"><a href="#ExecutorTypeSetup-57"><span class="linenos">57</span></a><span class="k">class</span> <span class="nc">ExecutorTypeSetup</span><span class="p">(</span><span class="n">ExecutorSetupBase</span><span class="p">):</span>
</span><span id="ExecutorTypeSetup-58"><a href="#ExecutorTypeSetup-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ExecutorTypeSetup-59"><a href="#ExecutorTypeSetup-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">]</span> <span class="o">=</span> <span class="n">executor_type</span>
</span><span id="ExecutorTypeSetup-60"><a href="#ExecutorTypeSetup-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ExecutorTypeSetup-61"><a href="#ExecutorTypeSetup-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="ExecutorTypeSetup-62"><a href="#ExecutorTypeSetup-62"><span class="linenos">62</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="ExecutorTypeSetup.__init__" class="classattr">
                                        <input id="ExecutorTypeSetup.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ExecutorTypeSetup</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">concurrent</span><span class="o">.</span><span class="n">futures</span><span class="o">.</span><span class="n">_base</span><span class="o">.</span><span class="n">Executor</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="ExecutorTypeSetup.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExecutorTypeSetup.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExecutorTypeSetup.__init__-58"><a href="#ExecutorTypeSetup.__init__-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ExecutorTypeSetup.__init__-59"><a href="#ExecutorTypeSetup.__init__-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Executor</span><span class="p">]</span> <span class="o">=</span> <span class="n">executor_type</span>
</span><span id="ExecutorTypeSetup.__init__-60"><a href="#ExecutorTypeSetup.__init__-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ExecutorTypeSetup.__init__-61"><a href="#ExecutorTypeSetup.__init__-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="ExecutorTypeSetup.__init__-62"><a href="#ExecutorTypeSetup.__init__-62"><span class="linenos">62</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ExecutorTypeSetup.executor_type" class="classattr">
                                <div class="attr variable">
            <span class="name">executor_type</span><span class="annotation">: Type[concurrent.futures._base.Executor]</span>

        
    </div>
    <a class="headerlink" href="#ExecutorTypeSetup.executor_type"></a>
    
    

                            </div>
                            <div id="ExecutorTypeSetup.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span>

        
    </div>
    <a class="headerlink" href="#ExecutorTypeSetup.args"></a>
    
    

                            </div>
                            <div id="ExecutorTypeSetup.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#ExecutorTypeSetup.kwargs"></a>
    
    

                            </div>
                </section>
                <section id="ExecutorInstanceSetup">
                            <input id="ExecutorInstanceSetup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExecutorInstanceSetup</span><wbr>(<span class="base"><a href="#ExecutorSetupBase">ExecutorSetupBase</a></span>):

                <label class="view-source-button" for="ExecutorInstanceSetup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExecutorInstanceSetup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExecutorInstanceSetup-65"><a href="#ExecutorInstanceSetup-65"><span class="linenos">65</span></a><span class="k">class</span> <span class="nc">ExecutorInstanceSetup</span><span class="p">(</span><span class="n">ExecutorSetupBase</span><span class="p">):</span>
</span><span id="ExecutorInstanceSetup-66"><a href="#ExecutorInstanceSetup-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ExecutorInstanceSetup-67"><a href="#ExecutorInstanceSetup-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="n">executor</span>
</span><span id="ExecutorInstanceSetup-68"><a href="#ExecutorInstanceSetup-68"><span class="linenos">68</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="ExecutorInstanceSetup.__init__" class="classattr">
                                        <input id="ExecutorInstanceSetup.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ExecutorInstanceSetup</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">executor</span><span class="p">:</span> <span class="n">concurrent</span><span class="o">.</span><span class="n">futures</span><span class="o">.</span><span class="n">_base</span><span class="o">.</span><span class="n">Executor</span></span>)</span>

                <label class="view-source-button" for="ExecutorInstanceSetup.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExecutorInstanceSetup.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExecutorInstanceSetup.__init__-66"><a href="#ExecutorInstanceSetup.__init__-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ExecutorInstanceSetup.__init__-67"><a href="#ExecutorInstanceSetup.__init__-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="n">executor</span>
</span><span id="ExecutorInstanceSetup.__init__-68"><a href="#ExecutorInstanceSetup.__init__-68"><span class="linenos">68</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ExecutorInstanceSetup.executor" class="classattr">
                                <div class="attr variable">
            <span class="name">executor</span><span class="annotation">: concurrent.futures._base.Executor</span>

        
    </div>
    <a class="headerlink" href="#ExecutorInstanceSetup.executor"></a>
    
    

                            </div>
                </section>
                <section id="InitializerSetup">
                            <input id="InitializerSetup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">InitializerSetup</span>:

                <label class="view-source-button" for="InitializerSetup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InitializerSetup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InitializerSetup-71"><a href="#InitializerSetup-71"><span class="linenos">71</span></a><span class="k">class</span> <span class="nc">InitializerSetup</span><span class="p">:</span>
</span><span id="InitializerSetup-72"><a href="#InitializerSetup-72"><span class="linenos">72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="InitializerSetup-73"><a href="#InitializerSetup-73"><span class="linenos">73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">initializer</span>
</span><span id="InitializerSetup-74"><a href="#InitializerSetup-74"><span class="linenos">74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="InitializerSetup-75"><a href="#InitializerSetup-75"><span class="linenos">75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="InitializerSetup.__init__" class="classattr">
                                        <input id="InitializerSetup.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">InitializerSetup</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="InitializerSetup.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#InitializerSetup.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="InitializerSetup.__init__-72"><a href="#InitializerSetup.__init__-72"><span class="linenos">72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="InitializerSetup.__init__-73"><a href="#InitializerSetup.__init__-73"><span class="linenos">73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">initializer</span>
</span><span id="InitializerSetup.__init__-74"><a href="#InitializerSetup.__init__-74"><span class="linenos">74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="InitializerSetup.__init__-75"><a href="#InitializerSetup.__init__-75"><span class="linenos">75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="InitializerSetup.initializer" class="classattr">
                                <div class="attr variable">
            <span class="name">initializer</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#InitializerSetup.initializer"></a>
    
    

                            </div>
                            <div id="InitializerSetup.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span>

        
    </div>
    <a class="headerlink" href="#InitializerSetup.args"></a>
    
    

                            </div>
                            <div id="InitializerSetup.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#InitializerSetup.kwargs"></a>
    
    

                            </div>
                </section>
                <section id="ProcessPoolSetup">
                            <input id="ProcessPoolSetup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ProcessPoolSetup</span>:

                <label class="view-source-button" for="ProcessPoolSetup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPoolSetup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPoolSetup-78"><a href="#ProcessPoolSetup-78"><span class="linenos">78</span></a><span class="k">class</span> <span class="nc">ProcessPoolSetup</span><span class="p">:</span>
</span><span id="ProcessPoolSetup-79"><a href="#ProcessPoolSetup-79"><span class="linenos">79</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPoolSetup-80"><a href="#ProcessPoolSetup-80"><span class="linenos">80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="ProcessPoolSetup-81"><a href="#ProcessPoolSetup-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span></pre></div>


    

                            <div id="ProcessPoolSetup.__init__" class="classattr">
                                        <input id="ProcessPoolSetup.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ProcessPoolSetup</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">loop</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ProcessPoolSetup.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPoolSetup.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPoolSetup.__init__-79"><a href="#ProcessPoolSetup.__init__-79"><span class="linenos">79</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPoolSetup.__init__-80"><a href="#ProcessPoolSetup.__init__-80"><span class="linenos">80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loop</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">asyncio</span><span class="o">.</span><span class="n">AbstractEventLoop</span><span class="p">]</span> <span class="o">=</span> <span class="n">loop</span> <span class="ow">or</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="ProcessPoolSetup.__init__-81"><a href="#ProcessPoolSetup.__init__-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span></pre></div>


    

                            </div>
                            <div id="ProcessPoolSetup.loop" class="classattr">
                                <div class="attr variable">
            <span class="name">loop</span><span class="annotation">: Union[asyncio.events.AbstractEventLoop, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#ProcessPoolSetup.loop"></a>
    
    

                            </div>
                            <div id="ProcessPoolSetup.is_multiprocessing" class="classattr">
                                <div class="attr variable">
            <span class="name">is_multiprocessing</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#ProcessPoolSetup.is_multiprocessing"></a>
    
    

                            </div>
                </section>
                <section id="ProcessPool">
                            <input id="ProcessPool-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ProcessPool</span>:

                <label class="view-source-button" for="ProcessPool-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPool"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPool-110"><a href="#ProcessPool-110"><span class="linenos">110</span></a><span class="k">class</span> <span class="nc">ProcessPool</span><span class="p">:</span>
</span><span id="ProcessPool-111"><a href="#ProcessPool-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span><span class="p">,</span> <span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-112"><a href="#ProcessPool-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span> <span class="o">=</span> <span class="n">executor_setup</span>
</span><span id="ProcessPool-113"><a href="#ProcessPool-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">process_pool_setup</span> <span class="ow">or</span> <span class="n">ProcessPoolSetup</span><span class="p">()</span>
</span><span id="ProcessPool-114"><a href="#ProcessPool-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">initializer_setup</span>
</span><span id="ProcessPool-115"><a href="#ProcessPool-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-116"><a href="#ProcessPool-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-117"><a href="#ProcessPool-117"><span class="linenos">117</span></a>        
</span><span id="ProcessPool-118"><a href="#ProcessPool-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_create_pool</span><span class="p">()</span>
</span><span id="ProcessPool-119"><a href="#ProcessPool-119"><span class="linenos">119</span></a>    
</span><span id="ProcessPool-120"><a href="#ProcessPool-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">set_is_multiprocessing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="ProcessPool-121"><a href="#ProcessPool-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span><span id="ProcessPool-122"><a href="#ProcessPool-122"><span class="linenos">122</span></a>    
</span><span id="ProcessPool-123"><a href="#ProcessPool-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">_create_pool</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ProcessPool-124"><a href="#ProcessPool-124"><span class="linenos">124</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-125"><a href="#ProcessPool-125"><span class="linenos">125</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_initializer</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">initializer</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-126"><a href="#ProcessPool-126"><span class="linenos">126</span></a>        
</span><span id="ProcessPool-127"><a href="#ProcessPool-127"><span class="linenos">127</span></a>        <span class="k">if</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">:</span>
</span><span id="ProcessPool-128"><a href="#ProcessPool-128"><span class="linenos">128</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">,</span> <span class="n">ExecutorInstanceSetup</span><span class="p">):</span>
</span><span id="ProcessPool-129"><a href="#ProcessPool-129"><span class="linenos">129</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor</span>
</span><span id="ProcessPool-130"><a href="#ProcessPool-130"><span class="linenos">130</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">,</span> <span class="n">ExecutorTypeSetup</span><span class="p">):</span>
</span><span id="ProcessPool-131"><a href="#ProcessPool-131"><span class="linenos">131</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-132"><a href="#ProcessPool-132"><span class="linenos">132</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;initializer&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span>
</span><span id="ProcessPool-133"><a href="#ProcessPool-133"><span class="linenos">133</span></a>                
</span><span id="ProcessPool-134"><a href="#ProcessPool-134"><span class="linenos">134</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor_type</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-135"><a href="#ProcessPool-135"><span class="linenos">135</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-136"><a href="#ProcessPool-136"><span class="linenos">136</span></a>                <span class="k">raise</span> <span class="n">ProcessPoolRuntimeError</span><span class="p">(</span><span class="s1">&#39;Unknown &quot;executor_setup&quot; parameter type&#39;</span><span class="p">)</span>
</span><span id="ProcessPool-137"><a href="#ProcessPool-137"><span class="linenos">137</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-138"><a href="#ProcessPool-138"><span class="linenos">138</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">executor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">executor_type</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-139"><a href="#ProcessPool-139"><span class="linenos">139</span></a>    
</span><span id="ProcessPool-140"><a href="#ProcessPool-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">shutdown</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="ProcessPool-141"><a href="#ProcessPool-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="n">wait</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="n">cancel_futures</span><span class="p">)</span>
</span><span id="ProcessPool-142"><a href="#ProcessPool-142"><span class="linenos">142</span></a>    
</span><span id="ProcessPool-143"><a href="#ProcessPool-143"><span class="linenos">143</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-144"><a href="#ProcessPool-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">_initializer</span><span class="p">(</span><span class="n">initializer</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ProcessPool-145"><a href="#ProcessPool-145"><span class="linenos">145</span></a>        <span class="kn">import</span> <span class="nn">multiprocessing</span>
</span><span id="ProcessPool-146"><a href="#ProcessPool-146"><span class="linenos">146</span></a>        
</span><span id="ProcessPool-147"><a href="#ProcessPool-147"><span class="linenos">147</span></a>        <span class="n">initializer</span><span class="p">(</span><span class="n">multiprocessing</span><span class="o">.</span><span class="n">current_process</span><span class="p">()</span><span class="o">.</span><span class="n">_identity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-148"><a href="#ProcessPool-148"><span class="linenos">148</span></a>
</span><span id="ProcessPool-149"><a href="#ProcessPool-149"><span class="linenos">149</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-150"><a href="#ProcessPool-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="nf">_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-151"><a href="#ProcessPool-151"><span class="linenos">151</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-152"><a href="#ProcessPool-152"><span class="linenos">152</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-153"><a href="#ProcessPool-153"><span class="linenos">153</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ProcessPool-154"><a href="#ProcessPool-154"><span class="linenos">154</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-155"><a href="#ProcessPool-155"><span class="linenos">155</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="ProcessPool-156"><a href="#ProcessPool-156"><span class="linenos">156</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="ProcessPool-157"><a href="#ProcessPool-157"><span class="linenos">157</span></a>        
</span><span id="ProcessPool-158"><a href="#ProcessPool-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="ProcessPool-159"><a href="#ProcessPool-159"><span class="linenos">159</span></a>
</span><span id="ProcessPool-160"><a href="#ProcessPool-160"><span class="linenos">160</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-161"><a href="#ProcessPool-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">_pool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-162"><a href="#ProcessPool-162"><span class="linenos">162</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="ProcessPool-163"><a href="#ProcessPool-163"><span class="linenos">163</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="ProcessPool-164"><a href="#ProcessPool-164"><span class="linenos">164</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ProcessPool-165"><a href="#ProcessPool-165"><span class="linenos">165</span></a>        
</span><span id="ProcessPool-166"><a href="#ProcessPool-166"><span class="linenos">166</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="ProcessPool-167"><a href="#ProcessPool-167"><span class="linenos">167</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-168"><a href="#ProcessPool-168"><span class="linenos">168</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="ProcessPool-169"><a href="#ProcessPool-169"><span class="linenos">169</span></a>            
</span><span id="ProcessPool-170"><a href="#ProcessPool-170"><span class="linenos">170</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ProcessPool-171"><a href="#ProcessPool-171"><span class="linenos">171</span></a>        
</span><span id="ProcessPool-172"><a href="#ProcessPool-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-173"><a href="#ProcessPool-173"><span class="linenos">173</span></a>
</span><span id="ProcessPool-174"><a href="#ProcessPool-174"><span class="linenos">174</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-175"><a href="#ProcessPool-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">_apool_worker</span><span class="p">(</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ResultHolder</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-176"><a href="#ProcessPool-176"><span class="linenos">176</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-177"><a href="#ProcessPool-177"><span class="linenos">177</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-178"><a href="#ProcessPool-178"><span class="linenos">178</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ProcessPool-179"><a href="#ProcessPool-179"><span class="linenos">179</span></a>            <span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="ProcessPool-180"><a href="#ProcessPool-180"><span class="linenos">180</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="ProcessPool-181"><a href="#ProcessPool-181"><span class="linenos">181</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="ProcessPool-182"><a href="#ProcessPool-182"><span class="linenos">182</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="ProcessPool-183"><a href="#ProcessPool-183"><span class="linenos">183</span></a>        
</span><span id="ProcessPool-184"><a href="#ProcessPool-184"><span class="linenos">184</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="n">exception</span><span class="p">)</span>
</span><span id="ProcessPool-185"><a href="#ProcessPool-185"><span class="linenos">185</span></a>    
</span><span id="ProcessPool-186"><a href="#ProcessPool-186"><span class="linenos">186</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-187"><a href="#ProcessPool-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">_apool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-188"><a href="#ProcessPool-188"><span class="linenos">188</span></a>        <span class="k">return</span> <span class="n">run_coroutine_in_new_thread</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-189"><a href="#ProcessPool-189"><span class="linenos">189</span></a>
</span><span id="ProcessPool-190"><a href="#ProcessPool-190"><span class="linenos">190</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-191"><a href="#ProcessPool-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="nf">_apool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-192"><a href="#ProcessPool-192"><span class="linenos">192</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="ProcessPool-193"><a href="#ProcessPool-193"><span class="linenos">193</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="ProcessPool-194"><a href="#ProcessPool-194"><span class="linenos">194</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ProcessPool-195"><a href="#ProcessPool-195"><span class="linenos">195</span></a>        
</span><span id="ProcessPool-196"><a href="#ProcessPool-196"><span class="linenos">196</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="ProcessPool-197"><a href="#ProcessPool-197"><span class="linenos">197</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-198"><a href="#ProcessPool-198"><span class="linenos">198</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="ProcessPool-199"><a href="#ProcessPool-199"><span class="linenos">199</span></a>
</span><span id="ProcessPool-200"><a href="#ProcessPool-200"><span class="linenos">200</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ProcessPool-201"><a href="#ProcessPool-201"><span class="linenos">201</span></a>        
</span><span id="ProcessPool-202"><a href="#ProcessPool-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-203"><a href="#ProcessPool-203"><span class="linenos">203</span></a>
</span><span id="ProcessPool-204"><a href="#ProcessPool-204"><span class="linenos">204</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-205"><a href="#ProcessPool-205"><span class="linenos">205</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_a_single_process_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-206"><a href="#ProcessPool-206"><span class="linenos">206</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-207"><a href="#ProcessPool-207"><span class="linenos">207</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool-208"><a href="#ProcessPool-208"><span class="linenos">208</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ProcessPool-209"><a href="#ProcessPool-209"><span class="linenos">209</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">worker</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-210"><a href="#ProcessPool-210"><span class="linenos">210</span></a>        <span class="k">except</span><span class="p">:</span>
</span><span id="ProcessPool-211"><a href="#ProcessPool-211"><span class="linenos">211</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="ProcessPool-212"><a href="#ProcessPool-212"><span class="linenos">212</span></a>        
</span><span id="ProcessPool-213"><a href="#ProcessPool-213"><span class="linenos">213</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">exception</span>
</span><span id="ProcessPool-214"><a href="#ProcessPool-214"><span class="linenos">214</span></a>
</span><span id="ProcessPool-215"><a href="#ProcessPool-215"><span class="linenos">215</span></a>    <span class="nd">@staticmethod</span>
</span><span id="ProcessPool-216"><a href="#ProcessPool-216"><span class="linenos">216</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_a_single_process_pool_worker_wrapper</span><span class="p">(</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]:</span>
</span><span id="ProcessPool-217"><a href="#ProcessPool-217"><span class="linenos">217</span></a>        <span class="k">global</span> <span class="n">process_initialized</span>
</span><span id="ProcessPool-218"><a href="#ProcessPool-218"><span class="linenos">218</span></a>        <span class="k">if</span> <span class="s1">&#39;process_initialized&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">():</span>
</span><span id="ProcessPool-219"><a href="#ProcessPool-219"><span class="linenos">219</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ProcessPool-220"><a href="#ProcessPool-220"><span class="linenos">220</span></a>        
</span><span id="ProcessPool-221"><a href="#ProcessPool-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">process_initialized</span><span class="p">:</span>
</span><span id="ProcessPool-222"><a href="#ProcessPool-222"><span class="linenos">222</span></a>            <span class="k">if</span> <span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-223"><a href="#ProcessPool-223"><span class="linenos">223</span></a>                <span class="n">partial_pool_initializer</span><span class="p">()</span>
</span><span id="ProcessPool-224"><a href="#ProcessPool-224"><span class="linenos">224</span></a>
</span><span id="ProcessPool-225"><a href="#ProcessPool-225"><span class="linenos">225</span></a>            <span class="n">process_initialized</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ProcessPool-226"><a href="#ProcessPool-226"><span class="linenos">226</span></a>        
</span><span id="ProcessPool-227"><a href="#ProcessPool-227"><span class="linenos">227</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">ProcessPool</span><span class="o">.</span><span class="n">_a_single_process_pool_worker</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-228"><a href="#ProcessPool-228"><span class="linenos">228</span></a>
</span><span id="ProcessPool-229"><a href="#ProcessPool-229"><span class="linenos">229</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pool_execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ProcessPool-230"><a href="#ProcessPool-230"><span class="linenos">230</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span>
</span><span id="ProcessPool-231"><a href="#ProcessPool-231"><span class="linenos">231</span></a>            <span class="k">if</span> <span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ProcessPool-232"><a href="#ProcessPool-232"><span class="linenos">232</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool-233"><a href="#ProcessPool-233"><span class="linenos">233</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-234"><a href="#ProcessPool-234"><span class="linenos">234</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-235"><a href="#ProcessPool-235"><span class="linenos">235</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-236"><a href="#ProcessPool-236"><span class="linenos">236</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-237"><a href="#ProcessPool-237"><span class="linenos">237</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool-238"><a href="#ProcessPool-238"><span class="linenos">238</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-239"><a href="#ProcessPool-239"><span class="linenos">239</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-240"><a href="#ProcessPool-240"><span class="linenos">240</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-241"><a href="#ProcessPool-241"><span class="linenos">241</span></a>            
</span><span id="ProcessPool-242"><a href="#ProcessPool-242"><span class="linenos">242</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">,</span> <span class="n">partial_pool_worker</span><span class="p">)</span>
</span><span id="ProcessPool-243"><a href="#ProcessPool-243"><span class="linenos">243</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-244"><a href="#ProcessPool-244"><span class="linenos">244</span></a>            <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool-245"><a href="#ProcessPool-245"><span class="linenos">245</span></a>                <span class="n">a_single_process_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_a_single_process_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-246"><a href="#ProcessPool-246"><span class="linenos">246</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">a_single_process_pool_worker</span><span class="p">()</span>
</span><span id="ProcessPool-247"><a href="#ProcessPool-247"><span class="linenos">247</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool-248"><a href="#ProcessPool-248"><span class="linenos">248</span></a>                <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool-249"><a href="#ProcessPool-249"><span class="linenos">249</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">partial_pool_worker</span><span class="p">()</span>
</span><span id="ProcessPool-250"><a href="#ProcessPool-250"><span class="linenos">250</span></a>        
</span><span id="ProcessPool-251"><a href="#ProcessPool-251"><span class="linenos">251</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="ProcessPool-252"><a href="#ProcessPool-252"><span class="linenos">252</span></a>        
</span><span id="ProcessPool-253"><a href="#ProcessPool-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool-254"><a href="#ProcessPool-254"><span class="linenos">254</span></a>            <span class="k">raise</span> <span class="n">exception</span>
</span><span id="ProcessPool-255"><a href="#ProcessPool-255"><span class="linenos">255</span></a>        
</span><span id="ProcessPool-256"><a href="#ProcessPool-256"><span class="linenos">256</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="ProcessPool-257"><a href="#ProcessPool-257"><span class="linenos">257</span></a>    
</span><span id="ProcessPool-258"><a href="#ProcessPool-258"><span class="linenos">258</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ProcessPool-259"><a href="#ProcessPool-259"><span class="linenos">259</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pool_execute</span><span class="p">(</span><span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="ProcessPool.__init__" class="classattr">
                                        <input id="ProcessPool.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ProcessPool</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">executor_setup</span><span class="p">:</span> <span class="n"><a href="#ExecutorSetupBase">ExecutorSetupBase</a></span>,</span><span class="param">	<span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#InitializerSetup">InitializerSetup</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#ProcessPoolSetup">ProcessPoolSetup</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ProcessPool.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPool.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPool.__init__-111"><a href="#ProcessPool.__init__-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span><span class="p">,</span> <span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool.__init__-112"><a href="#ProcessPool.__init__-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor_setup</span><span class="p">:</span> <span class="n">ExecutorSetupBase</span> <span class="o">=</span> <span class="n">executor_setup</span>
</span><span id="ProcessPool.__init__-113"><a href="#ProcessPool.__init__-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">ProcessPoolSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">process_pool_setup</span> <span class="ow">or</span> <span class="n">ProcessPoolSetup</span><span class="p">()</span>
</span><span id="ProcessPool.__init__-114"><a href="#ProcessPool.__init__-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initializer_setup</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">InitializerSetup</span><span class="p">]</span> <span class="o">=</span> <span class="n">initializer_setup</span>
</span><span id="ProcessPool.__init__-115"><a href="#ProcessPool.__init__-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">:</span> <span class="n">Executor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool.__init__-116"><a href="#ProcessPool.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="ProcessPool.__init__-117"><a href="#ProcessPool.__init__-117"><span class="linenos">117</span></a>        
</span><span id="ProcessPool.__init__-118"><a href="#ProcessPool.__init__-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_create_pool</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ProcessPool.executor_setup" class="classattr">
                                <div class="attr variable">
            <span class="name">executor_setup</span><span class="annotation">: <a href="#ExecutorSetupBase">ExecutorSetupBase</a></span>

        
    </div>
    <a class="headerlink" href="#ProcessPool.executor_setup"></a>
    
    

                            </div>
                            <div id="ProcessPool.process_pool_setup" class="classattr">
                                <div class="attr variable">
            <span class="name">process_pool_setup</span><span class="annotation">: Union[<a href="#ProcessPoolSetup">ProcessPoolSetup</a>, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#ProcessPool.process_pool_setup"></a>
    
    

                            </div>
                            <div id="ProcessPool.initializer_setup" class="classattr">
                                <div class="attr variable">
            <span class="name">initializer_setup</span><span class="annotation">: Union[<a href="#InitializerSetup">InitializerSetup</a>, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#ProcessPool.initializer_setup"></a>
    
    

                            </div>
                            <div id="ProcessPool.executor" class="classattr">
                                <div class="attr variable">
            <span class="name">executor</span><span class="annotation">: concurrent.futures._base.Executor</span>

        
    </div>
    <a class="headerlink" href="#ProcessPool.executor"></a>
    
    

                            </div>
                            <div id="ProcessPool.partial_pool_initializer" class="classattr">
                                <div class="attr variable">
            <span class="name">partial_pool_initializer</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#ProcessPool.partial_pool_initializer"></a>
    
    

                            </div>
                            <div id="ProcessPool.set_is_multiprocessing" class="classattr">
                                        <input id="ProcessPool.set_is_multiprocessing-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_is_multiprocessing</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ProcessPool.set_is_multiprocessing-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPool.set_is_multiprocessing"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPool.set_is_multiprocessing-120"><a href="#ProcessPool.set_is_multiprocessing-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">set_is_multiprocessing</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_multiprocessing</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="ProcessPool.set_is_multiprocessing-121"><a href="#ProcessPool.set_is_multiprocessing-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span> <span class="o">=</span> <span class="n">is_multiprocessing</span>
</span></pre></div>


    

                            </div>
                            <div id="ProcessPool.shutdown" class="classattr">
                                        <input id="ProcessPool.shutdown-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shutdown</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">wait</span><span class="o">=</span><span class="kc">True</span>, </span><span class="param"><span class="n">cancel_futures</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ProcessPool.shutdown-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPool.shutdown"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPool.shutdown-140"><a href="#ProcessPool.shutdown-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">shutdown</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wait</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="ProcessPool.shutdown-141"><a href="#ProcessPool.shutdown-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="n">wait</span><span class="p">,</span> <span class="n">cancel_futures</span><span class="o">=</span><span class="n">cancel_futures</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ProcessPool.pool_execute" class="classattr">
                                        <input id="ProcessPool.pool_execute-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">pool_execute</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="ProcessPool.pool_execute-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ProcessPool.pool_execute"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ProcessPool.pool_execute-229"><a href="#ProcessPool.pool_execute-229"><span class="linenos">229</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pool_execute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-230"><a href="#ProcessPool.pool_execute-230"><span class="linenos">230</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">is_multiprocessing</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-231"><a href="#ProcessPool.pool_execute-231"><span class="linenos">231</span></a>            <span class="k">if</span> <span class="p">((</span><span class="mi">3</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ProcessPool.pool_execute-232"><a href="#ProcessPool.pool_execute-232"><span class="linenos">232</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool.pool_execute-233"><a href="#ProcessPool.pool_execute-233"><span class="linenos">233</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-234"><a href="#ProcessPool.pool_execute-234"><span class="linenos">234</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-235"><a href="#ProcessPool.pool_execute-235"><span class="linenos">235</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-236"><a href="#ProcessPool.pool_execute-236"><span class="linenos">236</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-237"><a href="#ProcessPool.pool_execute-237"><span class="linenos">237</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool.pool_execute-238"><a href="#ProcessPool.pool_execute-238"><span class="linenos">238</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_apool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-239"><a href="#ProcessPool.pool_execute-239"><span class="linenos">239</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-240"><a href="#ProcessPool.pool_execute-240"><span class="linenos">240</span></a>                    <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-241"><a href="#ProcessPool.pool_execute-241"><span class="linenos">241</span></a>            
</span><span id="ProcessPool.pool_execute-242"><a href="#ProcessPool.pool_execute-242"><span class="linenos">242</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="ne">BaseException</span><span class="p">]]</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_pool_setup</span><span class="o">.</span><span class="n">loop</span><span class="o">.</span><span class="n">run_in_executor</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">executor</span><span class="p">,</span> <span class="n">partial_pool_worker</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-243"><a href="#ProcessPool.pool_execute-243"><span class="linenos">243</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-244"><a href="#ProcessPool.pool_execute-244"><span class="linenos">244</span></a>            <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">worker</span><span class="p">):</span>
</span><span id="ProcessPool.pool_execute-245"><a href="#ProcessPool.pool_execute-245"><span class="linenos">245</span></a>                <span class="n">a_single_process_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_a_single_process_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-246"><a href="#ProcessPool.pool_execute-246"><span class="linenos">246</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">a_single_process_pool_worker</span><span class="p">()</span>
</span><span id="ProcessPool.pool_execute-247"><a href="#ProcessPool.pool_execute-247"><span class="linenos">247</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-248"><a href="#ProcessPool.pool_execute-248"><span class="linenos">248</span></a>                <span class="n">partial_pool_worker</span> <span class="o">=</span> <span class="n">partial</span><span class="p">(</span><span class="n">ProcessPool</span><span class="o">.</span><span class="n">_pool_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_pool_initializer</span><span class="p">,</span> <span class="n">worker</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ProcessPool.pool_execute-249"><a href="#ProcessPool.pool_execute-249"><span class="linenos">249</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="n">partial_pool_worker</span><span class="p">()</span>
</span><span id="ProcessPool.pool_execute-250"><a href="#ProcessPool.pool_execute-250"><span class="linenos">250</span></a>        
</span><span id="ProcessPool.pool_execute-251"><a href="#ProcessPool.pool_execute-251"><span class="linenos">251</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">exception</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="ProcessPool.pool_execute-252"><a href="#ProcessPool.pool_execute-252"><span class="linenos">252</span></a>        
</span><span id="ProcessPool.pool_execute-253"><a href="#ProcessPool.pool_execute-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="n">exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ProcessPool.pool_execute-254"><a href="#ProcessPool.pool_execute-254"><span class="linenos">254</span></a>            <span class="k">raise</span> <span class="n">exception</span>
</span><span id="ProcessPool.pool_execute-255"><a href="#ProcessPool.pool_execute-255"><span class="linenos">255</span></a>        
</span><span id="ProcessPool.pool_execute-256"><a href="#ProcessPool.pool_execute-256"><span class="linenos">256</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>