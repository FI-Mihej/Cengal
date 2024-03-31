---
title: json
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_tools<wbr>.low_latency<wbr>.json<wbr>.versions<wbr>.v_0<wbr>.json    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-json-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-json-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="sd">Module Docstring</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.2.0&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;LowLatencyJSONDecoder&#39;</span><span class="p">,</span> <span class="s1">&#39;LowLatencyJSONEncoder&#39;</span><span class="p">,</span> <span class="s1">&#39;LowLatencyObjectPairsHook&#39;</span><span class="p">,</span> <span class="s1">&#39;original_json_dump&#39;</span><span class="p">,</span> <span class="s1">&#39;original_json_dumps&#39;</span><span class="p">,</span> <span class="s1">&#39;original_json_load&#39;</span><span class="p">,</span> <span class="s1">&#39;original_json_loads&#39;</span><span class="p">]</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">import</span> <span class="nn">json</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">original_json_dump</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dump</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">original_json_dumps</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="n">original_json_load</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="n">original_json_loads</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="c1"># You may use</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="c1"># ly = None, priority: CoroPriority = CoroPriority.normal</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="c1"># as an additional parameters in order to configure LowLatencyJSONEncoder</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;cls&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyJSONEncoder</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="k">return</span> <span class="n">original_json_dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="k">def</span> <span class="nf">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="c1"># You may use</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="c1"># ly = None, priority: CoroPriority = CoroPriority.normal</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="c1"># as an additional parameters in order to configure LowLatencyJSONEncoder</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;cls&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyJSONEncoder</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">return</span> <span class="n">original_json_dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="c1"># You may use</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="c1"># ly = None, priority: CoroPriority = CoroPriority.normal</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="c1"># as an additional parameters in order to configure LowLatencyJSONEncoder</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;cls&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyJSONDecoder</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyObjectPairsHook</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">return</span> <span class="n">original_json_load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="k">def</span> <span class="nf">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="c1"># You may use</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="c1"># ly = None, priority: CoroPriority = CoroPriority.normal</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="c1"># as an additional parameters in order to configure LowLatencyJSONEncoder</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;cls&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyJSONDecoder</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">LowLatencyObjectPairsHook</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    <span class="k">return</span> <span class="n">original_json_loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="c1"># json.dump = dump</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="c1"># json.dumps = dumps</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="c1"># json.load = load</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="c1"># json.loads = loads</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="k">def</span> <span class="nf">low_latency_json_mock_all</span><span class="p">():</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="n">dump</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="n">dumps</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="n">load</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="n">loads</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="k">def</span> <span class="nf">low_latency_json_demock_all</span><span class="p">():</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="n">original_json_dump</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="n">original_json_dumps</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="n">original_json_load</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="n">json</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="n">original_json_loads</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">List</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="k">class</span> <span class="nc">LowLatencyJSONDecoder</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">JSONDecoder</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">object_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_float</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_int</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_constant</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">strict</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">object_hook</span><span class="o">=</span><span class="n">object_hook</span><span class="p">,</span> <span class="n">parse_float</span><span class="o">=</span><span class="n">parse_float</span><span class="p">,</span> <span class="n">parse_int</span><span class="o">=</span><span class="n">parse_int</span><span class="p">,</span> <span class="n">parse_constant</span><span class="o">=</span><span class="n">parse_constant</span><span class="p">,</span> <span class="n">strict</span><span class="o">=</span><span class="n">strict</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="n">object_pairs_hook</span><span class="p">)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="k">class</span> <span class="nc">LowLatencyJSONEncoder</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">JSONEncoder</span><span class="p">):</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">skipkeys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">check_circular</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">allow_nan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">sort_keys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">skipkeys</span><span class="o">=</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="n">ensure_ascii</span><span class="p">,</span> <span class="n">check_circular</span><span class="o">=</span><span class="n">check_circular</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="n">allow_nan</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="n">sort_keys</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span> <span class="n">separators</span><span class="o">=</span><span class="n">separators</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">)</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_low_latency_iterencode</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">_low_latency_iterencode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_original_iterencode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="k">class</span> <span class="nc">LowLatencyObjectPairsHook</span><span class="p">:</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pairs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">pairs</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="LowLatencyJSONDecoder">
                            <input id="LowLatencyJSONDecoder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LowLatencyJSONDecoder</span><wbr>(<span class="base">json.decoder.JSONDecoder</span>):

                <label class="view-source-button" for="LowLatencyJSONDecoder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyJSONDecoder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyJSONDecoder-109"><a href="#LowLatencyJSONDecoder-109"><span class="linenos">109</span></a><span class="k">class</span> <span class="nc">LowLatencyJSONDecoder</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">JSONDecoder</span><span class="p">):</span>
</span><span id="LowLatencyJSONDecoder-110"><a href="#LowLatencyJSONDecoder-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">object_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_float</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_int</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_constant</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">strict</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyJSONDecoder-111"><a href="#LowLatencyJSONDecoder-111"><span class="linenos">111</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">object_hook</span><span class="o">=</span><span class="n">object_hook</span><span class="p">,</span> <span class="n">parse_float</span><span class="o">=</span><span class="n">parse_float</span><span class="p">,</span> <span class="n">parse_int</span><span class="o">=</span><span class="n">parse_int</span><span class="p">,</span> <span class="n">parse_constant</span><span class="o">=</span><span class="n">parse_constant</span><span class="p">,</span> <span class="n">strict</span><span class="o">=</span><span class="n">strict</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="n">object_pairs_hook</span><span class="p">)</span>
</span><span id="LowLatencyJSONDecoder-112"><a href="#LowLatencyJSONDecoder-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="LowLatencyJSONDecoder-113"><a href="#LowLatencyJSONDecoder-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Simple JSON <a href="http://json.org">http://json.org</a> decoder</p>

<p>Performs the following translations in decoding by default:</p>

<p>+---------------+-------------------+
| JSON          | Python            |
+===============+===================+
| object        | dict              |
+---------------+-------------------+
| array         | list              |
+---------------+-------------------+
| string        | str               |
+---------------+-------------------+
| number (int)  | int               |
+---------------+-------------------+
| number (real) | float             |
+---------------+-------------------+
| true          | True              |
+---------------+-------------------+
| false         | False             |
+---------------+-------------------+
| null          | None              |
+---------------+-------------------+</p>

<p>It also understands <code>NaN</code>, <code>Infinity</code>, and <code>-Infinity</code> as
their corresponding <code>float</code> values, which is outside the JSON spec.</p>
</div>


                            <div id="LowLatencyJSONDecoder.__init__" class="classattr">
                                        <input id="LowLatencyJSONDecoder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LowLatencyJSONDecoder</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">object_hook</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">parse_float</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">parse_int</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">parse_constant</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">strict</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">object_pairs_hook</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]],</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">ly</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="LowLatencyJSONDecoder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyJSONDecoder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyJSONDecoder.__init__-110"><a href="#LowLatencyJSONDecoder.__init__-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">object_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_float</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_int</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">parse_constant</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">strict</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]],</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyJSONDecoder.__init__-111"><a href="#LowLatencyJSONDecoder.__init__-111"><span class="linenos">111</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">object_hook</span><span class="o">=</span><span class="n">object_hook</span><span class="p">,</span> <span class="n">parse_float</span><span class="o">=</span><span class="n">parse_float</span><span class="p">,</span> <span class="n">parse_int</span><span class="o">=</span><span class="n">parse_int</span><span class="p">,</span> <span class="n">parse_constant</span><span class="o">=</span><span class="n">parse_constant</span><span class="p">,</span> <span class="n">strict</span><span class="o">=</span><span class="n">strict</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="n">object_pairs_hook</span><span class="p">)</span>
</span><span id="LowLatencyJSONDecoder.__init__-112"><a href="#LowLatencyJSONDecoder.__init__-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="LowLatencyJSONDecoder.__init__-113"><a href="#LowLatencyJSONDecoder.__init__-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p><code><a href="#LowLatencyJSONDecoder.object_hook">object_hook</a></code>, if specified, will be called with the result
of every JSON object decoded and its return value will be used in
place of the given <code>dict</code>.  This can be used to provide custom
deserializations (e.g. to support JSON-RPC class hinting).</p>

<p><code><a href="#LowLatencyJSONDecoder.object_pairs_hook">object_pairs_hook</a></code>, if specified will be called with the result of
every JSON object decoded with an ordered list of pairs.  The return
value of <code><a href="#LowLatencyJSONDecoder.object_pairs_hook">object_pairs_hook</a></code> will be used instead of the <code>dict</code>.
This feature can be used to implement custom decoders.
If <code><a href="#LowLatencyJSONDecoder.object_hook">object_hook</a></code> is also defined, the <code><a href="#LowLatencyJSONDecoder.object_pairs_hook">object_pairs_hook</a></code> takes
priority.</p>

<p><code><a href="#LowLatencyJSONDecoder.parse_float">parse_float</a></code>, if specified, will be called with the string
of every JSON float to be decoded. By default this is equivalent to
float(num_str). This can be used to use another datatype or parser
for JSON floats (e.g. decimal.Decimal).</p>

<p><code><a href="#LowLatencyJSONDecoder.parse_int">parse_int</a></code>, if specified, will be called with the string
of every JSON int to be decoded. By default this is equivalent to
int(num_str). This can be used to use another datatype or parser
for JSON integers (e.g. float).</p>

<p><code><a href="#LowLatencyJSONDecoder.parse_constant">parse_constant</a></code>, if specified, will be called with one of the
following strings: -Infinity, Infinity, NaN.
This can be used to raise an exception if invalid JSON numbers
are encountered.</p>

<p>If <code><a href="#LowLatencyJSONDecoder.strict">strict</a></code> is false (true is the default), then control
characters will be allowed inside strings.  Control characters in
this context are those with character codes in the 0-31 range,
including <code>'\t'</code> (tab), <code>'\n'</code>, <code>'\r'</code> and <code>'\0'</code>.</p>
</div>


                            </div>
                            <div id="LowLatencyJSONDecoder.ly" class="classattr">
                                <div class="attr variable">
            <span class="name">ly</span>

        
    </div>
    <a class="headerlink" href="#LowLatencyJSONDecoder.ly"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>json.decoder.JSONDecoder</dt>
                                <dd id="LowLatencyJSONDecoder.object_hook" class="variable">object_hook</dd>
                <dd id="LowLatencyJSONDecoder.parse_float" class="variable">parse_float</dd>
                <dd id="LowLatencyJSONDecoder.parse_int" class="variable">parse_int</dd>
                <dd id="LowLatencyJSONDecoder.parse_constant" class="variable">parse_constant</dd>
                <dd id="LowLatencyJSONDecoder.strict" class="variable">strict</dd>
                <dd id="LowLatencyJSONDecoder.object_pairs_hook" class="variable">object_pairs_hook</dd>
                <dd id="LowLatencyJSONDecoder.parse_object" class="variable">parse_object</dd>
                <dd id="LowLatencyJSONDecoder.parse_array" class="variable">parse_array</dd>
                <dd id="LowLatencyJSONDecoder.parse_string" class="variable">parse_string</dd>
                <dd id="LowLatencyJSONDecoder.memo" class="variable">memo</dd>
                <dd id="LowLatencyJSONDecoder.scan_once" class="variable">scan_once</dd>
                <dd id="LowLatencyJSONDecoder.decode" class="function">decode</dd>
                <dd id="LowLatencyJSONDecoder.raw_decode" class="function">raw_decode</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LowLatencyJSONEncoder">
                            <input id="LowLatencyJSONEncoder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LowLatencyJSONEncoder</span><wbr>(<span class="base">json.encoder.JSONEncoder</span>):

                <label class="view-source-button" for="LowLatencyJSONEncoder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyJSONEncoder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyJSONEncoder-116"><a href="#LowLatencyJSONEncoder-116"><span class="linenos">116</span></a><span class="k">class</span> <span class="nc">LowLatencyJSONEncoder</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">JSONEncoder</span><span class="p">):</span>
</span><span id="LowLatencyJSONEncoder-117"><a href="#LowLatencyJSONEncoder-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">skipkeys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">check_circular</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">allow_nan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">sort_keys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder-118"><a href="#LowLatencyJSONEncoder-118"><span class="linenos">118</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">skipkeys</span><span class="o">=</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="n">ensure_ascii</span><span class="p">,</span> <span class="n">check_circular</span><span class="o">=</span><span class="n">check_circular</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="n">allow_nan</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="n">sort_keys</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span> <span class="n">separators</span><span class="o">=</span><span class="n">separators</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder-119"><a href="#LowLatencyJSONEncoder-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span>
</span><span id="LowLatencyJSONEncoder-120"><a href="#LowLatencyJSONEncoder-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_low_latency_iterencode</span>
</span><span id="LowLatencyJSONEncoder-121"><a href="#LowLatencyJSONEncoder-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder-122"><a href="#LowLatencyJSONEncoder-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="LowLatencyJSONEncoder-123"><a href="#LowLatencyJSONEncoder-123"><span class="linenos">123</span></a>    
</span><span id="LowLatencyJSONEncoder-124"><a href="#LowLatencyJSONEncoder-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">_low_latency_iterencode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="LowLatencyJSONEncoder-125"><a href="#LowLatencyJSONEncoder-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="LowLatencyJSONEncoder-126"><a href="#LowLatencyJSONEncoder-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_original_iterencode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Extensible JSON <a href="http://json.org">http://json.org</a> encoder for Python data structures.</p>

<p>Supports the following objects and types by default:</p>

<p>+-------------------+---------------+
| Python            | JSON          |
+===================+===============+
| dict              | object        |
+-------------------+---------------+
| list, tuple       | array         |
+-------------------+---------------+
| str               | string        |
+-------------------+---------------+
| int, float        | number        |
+-------------------+---------------+
| True              | true          |
+-------------------+---------------+
| False             | false         |
+-------------------+---------------+
| None              | null          |
+-------------------+---------------+</p>

<p>To extend this to recognize other objects, subclass and implement a
<code>.default()</code> method with another method that returns a serializable
object for <code>o</code> if possible, otherwise it should call the superclass
implementation (to raise <code>TypeError</code>).</p>
</div>


                            <div id="LowLatencyJSONEncoder.__init__" class="classattr">
                                        <input id="LowLatencyJSONEncoder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LowLatencyJSONEncoder</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">skipkeys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>,</span><span class="param">	<span class="n">ensure_ascii</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">check_circular</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">allow_nan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">sort_keys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>,</span><span class="param">	<span class="n">indent</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">separators</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">default</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">ly</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="LowLatencyJSONEncoder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyJSONEncoder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyJSONEncoder.__init__-117"><a href="#LowLatencyJSONEncoder.__init__-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">skipkeys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">check_circular</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">allow_nan</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">sort_keys</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">indent</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">separators</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">[</span><span class="o">...</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.__init__-118"><a href="#LowLatencyJSONEncoder.__init__-118"><span class="linenos">118</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">skipkeys</span><span class="o">=</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="n">ensure_ascii</span><span class="p">,</span> <span class="n">check_circular</span><span class="o">=</span><span class="n">check_circular</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="n">allow_nan</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="n">sort_keys</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span> <span class="n">separators</span><span class="o">=</span><span class="n">separators</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder.__init__-119"><a href="#LowLatencyJSONEncoder.__init__-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_original_iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span>
</span><span id="LowLatencyJSONEncoder.__init__-120"><a href="#LowLatencyJSONEncoder.__init__-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">iterencode</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_low_latency_iterencode</span>
</span><span id="LowLatencyJSONEncoder.__init__-121"><a href="#LowLatencyJSONEncoder.__init__-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder.__init__-122"><a href="#LowLatencyJSONEncoder.__init__-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Constructor for JSONEncoder, with sensible defaults.</p>

<p>If skipkeys is false, then it is a TypeError to attempt
encoding of keys that are not str, int, float or None.  If
skipkeys is True, such items are simply skipped.</p>

<p>If ensure_ascii is true, the output is guaranteed to be str
objects with all incoming non-ASCII characters escaped.  If
ensure_ascii is false, the output can contain non-ASCII characters.</p>

<p>If check_circular is true, then lists, dicts, and custom encoded
objects will be checked for circular references during encoding to
prevent an infinite recursion (which would cause an OverflowError).
Otherwise, no such check takes place.</p>

<p>If allow_nan is true, then NaN, Infinity, and -Infinity will be
encoded as such.  This behavior is not JSON specification compliant,
but is consistent with most JavaScript based encoders and decoders.
Otherwise, it will be a ValueError to encode such floats.</p>

<p>If sort_keys is true, then the output of dictionaries will be
sorted by key; this is useful for regression tests to ensure
that JSON serializations can be compared on a day-to-day basis.</p>

<p>If indent is a non-negative integer, then JSON array
elements and object members will be pretty-printed with that
indent level.  An indent level of 0 will only insert newlines.
None is the most compact representation.</p>

<p>If specified, separators should be an (item_separator, key_separator)
tuple.  The default is (', ', ': ') if <em>indent</em> is <code>None</code> and
(',', ': ') otherwise.  To get the most compact JSON representation,
you should specify (',', ':') to eliminate whitespace.</p>

<p>If specified, default is a function that gets called for objects
that can't otherwise be serialized.  It should return a JSON encodable
version of the object or raise a <code>TypeError</code>.</p>
</div>


                            </div>
                            <div id="LowLatencyJSONEncoder.iterencode" class="classattr">
                                        <input id="LowLatencyJSONEncoder.iterencode-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">iterencode</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">o</span>, </span><span class="param"><span class="n">_one_shot</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="LowLatencyJSONEncoder.iterencode-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyJSONEncoder.iterencode"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyJSONEncoder.iterencode-205"><a href="#LowLatencyJSONEncoder.iterencode-205"><span class="linenos">205</span></a>    <span class="k">def</span> <span class="nf">iterencode</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">o</span><span class="p">,</span> <span class="n">_one_shot</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="LowLatencyJSONEncoder.iterencode-206"><a href="#LowLatencyJSONEncoder.iterencode-206"><span class="linenos">206</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Encode the given object and yield each string</span>
</span><span id="LowLatencyJSONEncoder.iterencode-207"><a href="#LowLatencyJSONEncoder.iterencode-207"><span class="linenos">207</span></a><span class="sd">        representation as available.</span>
</span><span id="LowLatencyJSONEncoder.iterencode-208"><a href="#LowLatencyJSONEncoder.iterencode-208"><span class="linenos">208</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-209"><a href="#LowLatencyJSONEncoder.iterencode-209"><span class="linenos">209</span></a><span class="sd">        For example::</span>
</span><span id="LowLatencyJSONEncoder.iterencode-210"><a href="#LowLatencyJSONEncoder.iterencode-210"><span class="linenos">210</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-211"><a href="#LowLatencyJSONEncoder.iterencode-211"><span class="linenos">211</span></a><span class="sd">            for chunk in JSONEncoder().iterencode(bigobject):</span>
</span><span id="LowLatencyJSONEncoder.iterencode-212"><a href="#LowLatencyJSONEncoder.iterencode-212"><span class="linenos">212</span></a><span class="sd">                mysocket.write(chunk)</span>
</span><span id="LowLatencyJSONEncoder.iterencode-213"><a href="#LowLatencyJSONEncoder.iterencode-213"><span class="linenos">213</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-214"><a href="#LowLatencyJSONEncoder.iterencode-214"><span class="linenos">214</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="LowLatencyJSONEncoder.iterencode-215"><a href="#LowLatencyJSONEncoder.iterencode-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_circular</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-216"><a href="#LowLatencyJSONEncoder.iterencode-216"><span class="linenos">216</span></a>            <span class="n">markers</span> <span class="o">=</span> <span class="p">{}</span>
</span><span id="LowLatencyJSONEncoder.iterencode-217"><a href="#LowLatencyJSONEncoder.iterencode-217"><span class="linenos">217</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-218"><a href="#LowLatencyJSONEncoder.iterencode-218"><span class="linenos">218</span></a>            <span class="n">markers</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="LowLatencyJSONEncoder.iterencode-219"><a href="#LowLatencyJSONEncoder.iterencode-219"><span class="linenos">219</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">ensure_ascii</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-220"><a href="#LowLatencyJSONEncoder.iterencode-220"><span class="linenos">220</span></a>            <span class="n">_encoder</span> <span class="o">=</span> <span class="n">encode_basestring_ascii</span>
</span><span id="LowLatencyJSONEncoder.iterencode-221"><a href="#LowLatencyJSONEncoder.iterencode-221"><span class="linenos">221</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-222"><a href="#LowLatencyJSONEncoder.iterencode-222"><span class="linenos">222</span></a>            <span class="n">_encoder</span> <span class="o">=</span> <span class="n">encode_basestring</span>
</span><span id="LowLatencyJSONEncoder.iterencode-223"><a href="#LowLatencyJSONEncoder.iterencode-223"><span class="linenos">223</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-224"><a href="#LowLatencyJSONEncoder.iterencode-224"><span class="linenos">224</span></a>        <span class="k">def</span> <span class="nf">floatstr</span><span class="p">(</span><span class="n">o</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">allow_nan</span><span class="p">,</span>
</span><span id="LowLatencyJSONEncoder.iterencode-225"><a href="#LowLatencyJSONEncoder.iterencode-225"><span class="linenos">225</span></a>                <span class="n">_repr</span><span class="o">=</span><span class="nb">float</span><span class="o">.</span><span class="fm">__repr__</span><span class="p">,</span> <span class="n">_inf</span><span class="o">=</span><span class="n">INFINITY</span><span class="p">,</span> <span class="n">_neginf</span><span class="o">=-</span><span class="n">INFINITY</span><span class="p">):</span>
</span><span id="LowLatencyJSONEncoder.iterencode-226"><a href="#LowLatencyJSONEncoder.iterencode-226"><span class="linenos">226</span></a>            <span class="c1"># Check for specials.  Note that this type of test is processor</span>
</span><span id="LowLatencyJSONEncoder.iterencode-227"><a href="#LowLatencyJSONEncoder.iterencode-227"><span class="linenos">227</span></a>            <span class="c1"># and/or platform-specific, so do tests which don&#39;t depend on the</span>
</span><span id="LowLatencyJSONEncoder.iterencode-228"><a href="#LowLatencyJSONEncoder.iterencode-228"><span class="linenos">228</span></a>            <span class="c1"># internals.</span>
</span><span id="LowLatencyJSONEncoder.iterencode-229"><a href="#LowLatencyJSONEncoder.iterencode-229"><span class="linenos">229</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-230"><a href="#LowLatencyJSONEncoder.iterencode-230"><span class="linenos">230</span></a>            <span class="k">if</span> <span class="n">o</span> <span class="o">!=</span> <span class="n">o</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-231"><a href="#LowLatencyJSONEncoder.iterencode-231"><span class="linenos">231</span></a>                <span class="n">text</span> <span class="o">=</span> <span class="s1">&#39;NaN&#39;</span>
</span><span id="LowLatencyJSONEncoder.iterencode-232"><a href="#LowLatencyJSONEncoder.iterencode-232"><span class="linenos">232</span></a>            <span class="k">elif</span> <span class="n">o</span> <span class="o">==</span> <span class="n">_inf</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-233"><a href="#LowLatencyJSONEncoder.iterencode-233"><span class="linenos">233</span></a>                <span class="n">text</span> <span class="o">=</span> <span class="s1">&#39;Infinity&#39;</span>
</span><span id="LowLatencyJSONEncoder.iterencode-234"><a href="#LowLatencyJSONEncoder.iterencode-234"><span class="linenos">234</span></a>            <span class="k">elif</span> <span class="n">o</span> <span class="o">==</span> <span class="n">_neginf</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-235"><a href="#LowLatencyJSONEncoder.iterencode-235"><span class="linenos">235</span></a>                <span class="n">text</span> <span class="o">=</span> <span class="s1">&#39;-Infinity&#39;</span>
</span><span id="LowLatencyJSONEncoder.iterencode-236"><a href="#LowLatencyJSONEncoder.iterencode-236"><span class="linenos">236</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-237"><a href="#LowLatencyJSONEncoder.iterencode-237"><span class="linenos">237</span></a>                <span class="k">return</span> <span class="n">_repr</span><span class="p">(</span><span class="n">o</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder.iterencode-238"><a href="#LowLatencyJSONEncoder.iterencode-238"><span class="linenos">238</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-239"><a href="#LowLatencyJSONEncoder.iterencode-239"><span class="linenos">239</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">allow_nan</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-240"><a href="#LowLatencyJSONEncoder.iterencode-240"><span class="linenos">240</span></a>                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span>
</span><span id="LowLatencyJSONEncoder.iterencode-241"><a href="#LowLatencyJSONEncoder.iterencode-241"><span class="linenos">241</span></a>                    <span class="s2">&quot;Out of range float values are not JSON compliant: &quot;</span> <span class="o">+</span>
</span><span id="LowLatencyJSONEncoder.iterencode-242"><a href="#LowLatencyJSONEncoder.iterencode-242"><span class="linenos">242</span></a>                    <span class="nb">repr</span><span class="p">(</span><span class="n">o</span><span class="p">))</span>
</span><span id="LowLatencyJSONEncoder.iterencode-243"><a href="#LowLatencyJSONEncoder.iterencode-243"><span class="linenos">243</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-244"><a href="#LowLatencyJSONEncoder.iterencode-244"><span class="linenos">244</span></a>            <span class="k">return</span> <span class="n">text</span>
</span><span id="LowLatencyJSONEncoder.iterencode-245"><a href="#LowLatencyJSONEncoder.iterencode-245"><span class="linenos">245</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-246"><a href="#LowLatencyJSONEncoder.iterencode-246"><span class="linenos">246</span></a>
</span><span id="LowLatencyJSONEncoder.iterencode-247"><a href="#LowLatencyJSONEncoder.iterencode-247"><span class="linenos">247</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">_one_shot</span> <span class="ow">and</span> <span class="n">c_make_encoder</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="LowLatencyJSONEncoder.iterencode-248"><a href="#LowLatencyJSONEncoder.iterencode-248"><span class="linenos">248</span></a>                <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">indent</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="LowLatencyJSONEncoder.iterencode-249"><a href="#LowLatencyJSONEncoder.iterencode-249"><span class="linenos">249</span></a>            <span class="n">_iterencode</span> <span class="o">=</span> <span class="n">c_make_encoder</span><span class="p">(</span>
</span><span id="LowLatencyJSONEncoder.iterencode-250"><a href="#LowLatencyJSONEncoder.iterencode-250"><span class="linenos">250</span></a>                <span class="n">markers</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">default</span><span class="p">,</span> <span class="n">_encoder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">indent</span><span class="p">,</span>
</span><span id="LowLatencyJSONEncoder.iterencode-251"><a href="#LowLatencyJSONEncoder.iterencode-251"><span class="linenos">251</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">key_separator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_separator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_keys</span><span class="p">,</span>
</span><span id="LowLatencyJSONEncoder.iterencode-252"><a href="#LowLatencyJSONEncoder.iterencode-252"><span class="linenos">252</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">skipkeys</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">allow_nan</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder.iterencode-253"><a href="#LowLatencyJSONEncoder.iterencode-253"><span class="linenos">253</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="LowLatencyJSONEncoder.iterencode-254"><a href="#LowLatencyJSONEncoder.iterencode-254"><span class="linenos">254</span></a>            <span class="n">_iterencode</span> <span class="o">=</span> <span class="n">_make_iterencode</span><span class="p">(</span>
</span><span id="LowLatencyJSONEncoder.iterencode-255"><a href="#LowLatencyJSONEncoder.iterencode-255"><span class="linenos">255</span></a>                <span class="n">markers</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">default</span><span class="p">,</span> <span class="n">_encoder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">indent</span><span class="p">,</span> <span class="n">floatstr</span><span class="p">,</span>
</span><span id="LowLatencyJSONEncoder.iterencode-256"><a href="#LowLatencyJSONEncoder.iterencode-256"><span class="linenos">256</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">key_separator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_separator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_keys</span><span class="p">,</span>
</span><span id="LowLatencyJSONEncoder.iterencode-257"><a href="#LowLatencyJSONEncoder.iterencode-257"><span class="linenos">257</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">_one_shot</span><span class="p">)</span>
</span><span id="LowLatencyJSONEncoder.iterencode-258"><a href="#LowLatencyJSONEncoder.iterencode-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="n">_iterencode</span><span class="p">(</span><span class="n">o</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Encode the given object and yield each string
representation as available.</p>

<p>For example::</p>

<pre><code>for chunk in JSONEncoder().iterencode(bigobject):
    mysocket.write(chunk)
</code></pre>
</div>


                            </div>
                            <div id="LowLatencyJSONEncoder.ly" class="classattr">
                                <div class="attr variable">
            <span class="name">ly</span>

        
    </div>
    <a class="headerlink" href="#LowLatencyJSONEncoder.ly"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>json.encoder.JSONEncoder</dt>
                                <dd id="LowLatencyJSONEncoder.item_separator" class="variable">item_separator</dd>
                <dd id="LowLatencyJSONEncoder.key_separator" class="variable">key_separator</dd>
                <dd id="LowLatencyJSONEncoder.skipkeys" class="variable">skipkeys</dd>
                <dd id="LowLatencyJSONEncoder.ensure_ascii" class="variable">ensure_ascii</dd>
                <dd id="LowLatencyJSONEncoder.check_circular" class="variable">check_circular</dd>
                <dd id="LowLatencyJSONEncoder.allow_nan" class="variable">allow_nan</dd>
                <dd id="LowLatencyJSONEncoder.sort_keys" class="variable">sort_keys</dd>
                <dd id="LowLatencyJSONEncoder.indent" class="variable">indent</dd>
                <dd id="LowLatencyJSONEncoder.default" class="function">default</dd>
                <dd id="LowLatencyJSONEncoder.encode" class="function">encode</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="LowLatencyObjectPairsHook">
                            <input id="LowLatencyObjectPairsHook-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LowLatencyObjectPairsHook</span>:

                <label class="view-source-button" for="LowLatencyObjectPairsHook-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyObjectPairsHook"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyObjectPairsHook-129"><a href="#LowLatencyObjectPairsHook-129"><span class="linenos">129</span></a><span class="k">class</span> <span class="nc">LowLatencyObjectPairsHook</span><span class="p">:</span>
</span><span id="LowLatencyObjectPairsHook-130"><a href="#LowLatencyObjectPairsHook-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyObjectPairsHook-131"><a href="#LowLatencyObjectPairsHook-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="LowLatencyObjectPairsHook-132"><a href="#LowLatencyObjectPairsHook-132"><span class="linenos">132</span></a>    
</span><span id="LowLatencyObjectPairsHook-133"><a href="#LowLatencyObjectPairsHook-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pairs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="LowLatencyObjectPairsHook-134"><a href="#LowLatencyObjectPairsHook-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span><span class="p">()</span>
</span><span id="LowLatencyObjectPairsHook-135"><a href="#LowLatencyObjectPairsHook-135"><span class="linenos">135</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">pairs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="LowLatencyObjectPairsHook.__init__" class="classattr">
                                        <input id="LowLatencyObjectPairsHook.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">LowLatencyObjectPairsHook</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">ly</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="LowLatencyObjectPairsHook.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LowLatencyObjectPairsHook.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LowLatencyObjectPairsHook.__init__-130"><a href="#LowLatencyObjectPairsHook.__init__-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ly</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="LowLatencyObjectPairsHook.__init__-131"><a href="#LowLatencyObjectPairsHook.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ly</span> <span class="o">=</span> <span class="n">ly</span> <span class="ow">or</span> <span class="n">gly</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="LowLatencyObjectPairsHook.ly" class="classattr">
                                <div class="attr variable">
            <span class="name">ly</span>

        
    </div>
    <a class="headerlink" href="#LowLatencyObjectPairsHook.ly"></a>
    
    

                            </div>
                </section>
                <section id="original_json_dump">
                            <input id="original_json_dump-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">original_json_dump</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">obj</span>,</span><span class="param">	<span class="n">fp</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">skipkeys</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">ensure_ascii</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="n">check_circular</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="n">allow_nan</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="bp">cls</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">indent</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">separators</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">default</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="o">**</span><span class="n">kw</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="original_json_dump-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#original_json_dump"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="original_json_dump-121"><a href="#original_json_dump-121"><span class="linenos">121</span></a><span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">skipkeys</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">check_circular</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
</span><span id="original_json_dump-122"><a href="#original_json_dump-122"><span class="linenos">122</span></a>        <span class="n">allow_nan</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="bp">cls</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">separators</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="original_json_dump-123"><a href="#original_json_dump-123"><span class="linenos">123</span></a>        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_dump-124"><a href="#original_json_dump-124"><span class="linenos">124</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Serialize ``obj`` as a JSON formatted stream to ``fp`` (a</span>
</span><span id="original_json_dump-125"><a href="#original_json_dump-125"><span class="linenos">125</span></a><span class="sd">    ``.write()``-supporting file-like object).</span>
</span><span id="original_json_dump-126"><a href="#original_json_dump-126"><span class="linenos">126</span></a>
</span><span id="original_json_dump-127"><a href="#original_json_dump-127"><span class="linenos">127</span></a><span class="sd">    If ``skipkeys`` is true then ``dict`` keys that are not basic types</span>
</span><span id="original_json_dump-128"><a href="#original_json_dump-128"><span class="linenos">128</span></a><span class="sd">    (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped</span>
</span><span id="original_json_dump-129"><a href="#original_json_dump-129"><span class="linenos">129</span></a><span class="sd">    instead of raising a ``TypeError``.</span>
</span><span id="original_json_dump-130"><a href="#original_json_dump-130"><span class="linenos">130</span></a>
</span><span id="original_json_dump-131"><a href="#original_json_dump-131"><span class="linenos">131</span></a><span class="sd">    If ``ensure_ascii`` is false, then the strings written to ``fp`` can</span>
</span><span id="original_json_dump-132"><a href="#original_json_dump-132"><span class="linenos">132</span></a><span class="sd">    contain non-ASCII characters if they appear in strings contained in</span>
</span><span id="original_json_dump-133"><a href="#original_json_dump-133"><span class="linenos">133</span></a><span class="sd">    ``obj``. Otherwise, all such characters are escaped in JSON strings.</span>
</span><span id="original_json_dump-134"><a href="#original_json_dump-134"><span class="linenos">134</span></a>
</span><span id="original_json_dump-135"><a href="#original_json_dump-135"><span class="linenos">135</span></a><span class="sd">    If ``check_circular`` is false, then the circular reference check</span>
</span><span id="original_json_dump-136"><a href="#original_json_dump-136"><span class="linenos">136</span></a><span class="sd">    for container types will be skipped and a circular reference will</span>
</span><span id="original_json_dump-137"><a href="#original_json_dump-137"><span class="linenos">137</span></a><span class="sd">    result in an ``OverflowError`` (or worse).</span>
</span><span id="original_json_dump-138"><a href="#original_json_dump-138"><span class="linenos">138</span></a>
</span><span id="original_json_dump-139"><a href="#original_json_dump-139"><span class="linenos">139</span></a><span class="sd">    If ``allow_nan`` is false, then it will be a ``ValueError`` to</span>
</span><span id="original_json_dump-140"><a href="#original_json_dump-140"><span class="linenos">140</span></a><span class="sd">    serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)</span>
</span><span id="original_json_dump-141"><a href="#original_json_dump-141"><span class="linenos">141</span></a><span class="sd">    in strict compliance of the JSON specification, instead of using the</span>
</span><span id="original_json_dump-142"><a href="#original_json_dump-142"><span class="linenos">142</span></a><span class="sd">    JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).</span>
</span><span id="original_json_dump-143"><a href="#original_json_dump-143"><span class="linenos">143</span></a>
</span><span id="original_json_dump-144"><a href="#original_json_dump-144"><span class="linenos">144</span></a><span class="sd">    If ``indent`` is a non-negative integer, then JSON array elements and</span>
</span><span id="original_json_dump-145"><a href="#original_json_dump-145"><span class="linenos">145</span></a><span class="sd">    object members will be pretty-printed with that indent level. An indent</span>
</span><span id="original_json_dump-146"><a href="#original_json_dump-146"><span class="linenos">146</span></a><span class="sd">    level of 0 will only insert newlines. ``None`` is the most compact</span>
</span><span id="original_json_dump-147"><a href="#original_json_dump-147"><span class="linenos">147</span></a><span class="sd">    representation.</span>
</span><span id="original_json_dump-148"><a href="#original_json_dump-148"><span class="linenos">148</span></a>
</span><span id="original_json_dump-149"><a href="#original_json_dump-149"><span class="linenos">149</span></a><span class="sd">    If specified, ``separators`` should be an ``(item_separator, key_separator)``</span>
</span><span id="original_json_dump-150"><a href="#original_json_dump-150"><span class="linenos">150</span></a><span class="sd">    tuple.  The default is ``(&#39;, &#39;, &#39;: &#39;)`` if *indent* is ``None`` and</span>
</span><span id="original_json_dump-151"><a href="#original_json_dump-151"><span class="linenos">151</span></a><span class="sd">    ``(&#39;,&#39;, &#39;: &#39;)`` otherwise.  To get the most compact JSON representation,</span>
</span><span id="original_json_dump-152"><a href="#original_json_dump-152"><span class="linenos">152</span></a><span class="sd">    you should specify ``(&#39;,&#39;, &#39;:&#39;)`` to eliminate whitespace.</span>
</span><span id="original_json_dump-153"><a href="#original_json_dump-153"><span class="linenos">153</span></a>
</span><span id="original_json_dump-154"><a href="#original_json_dump-154"><span class="linenos">154</span></a><span class="sd">    ``default(obj)`` is a function that should return a serializable version</span>
</span><span id="original_json_dump-155"><a href="#original_json_dump-155"><span class="linenos">155</span></a><span class="sd">    of obj or raise TypeError. The default simply raises TypeError.</span>
</span><span id="original_json_dump-156"><a href="#original_json_dump-156"><span class="linenos">156</span></a>
</span><span id="original_json_dump-157"><a href="#original_json_dump-157"><span class="linenos">157</span></a><span class="sd">    If *sort_keys* is true (default: ``False``), then the output of</span>
</span><span id="original_json_dump-158"><a href="#original_json_dump-158"><span class="linenos">158</span></a><span class="sd">    dictionaries will be sorted by key.</span>
</span><span id="original_json_dump-159"><a href="#original_json_dump-159"><span class="linenos">159</span></a>
</span><span id="original_json_dump-160"><a href="#original_json_dump-160"><span class="linenos">160</span></a><span class="sd">    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the</span>
</span><span id="original_json_dump-161"><a href="#original_json_dump-161"><span class="linenos">161</span></a><span class="sd">    ``.default()`` method to serialize additional types), specify it with</span>
</span><span id="original_json_dump-162"><a href="#original_json_dump-162"><span class="linenos">162</span></a><span class="sd">    the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.</span>
</span><span id="original_json_dump-163"><a href="#original_json_dump-163"><span class="linenos">163</span></a>
</span><span id="original_json_dump-164"><a href="#original_json_dump-164"><span class="linenos">164</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="original_json_dump-165"><a href="#original_json_dump-165"><span class="linenos">165</span></a>    <span class="c1"># cached encoder</span>
</span><span id="original_json_dump-166"><a href="#original_json_dump-166"><span class="linenos">166</span></a>    <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">skipkeys</span> <span class="ow">and</span> <span class="n">ensure_ascii</span> <span class="ow">and</span>
</span><span id="original_json_dump-167"><a href="#original_json_dump-167"><span class="linenos">167</span></a>        <span class="n">check_circular</span> <span class="ow">and</span> <span class="n">allow_nan</span> <span class="ow">and</span>
</span><span id="original_json_dump-168"><a href="#original_json_dump-168"><span class="linenos">168</span></a>        <span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">indent</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">separators</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="original_json_dump-169"><a href="#original_json_dump-169"><span class="linenos">169</span></a>        <span class="n">default</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">sort_keys</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_dump-170"><a href="#original_json_dump-170"><span class="linenos">170</span></a>        <span class="n">iterable</span> <span class="o">=</span> <span class="n">_default_encoder</span><span class="o">.</span><span class="n">iterencode</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="original_json_dump-171"><a href="#original_json_dump-171"><span class="linenos">171</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="original_json_dump-172"><a href="#original_json_dump-172"><span class="linenos">172</span></a>        <span class="k">if</span> <span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_dump-173"><a href="#original_json_dump-173"><span class="linenos">173</span></a>            <span class="bp">cls</span> <span class="o">=</span> <span class="n">JSONEncoder</span>
</span><span id="original_json_dump-174"><a href="#original_json_dump-174"><span class="linenos">174</span></a>        <span class="n">iterable</span> <span class="o">=</span> <span class="bp">cls</span><span class="p">(</span><span class="n">skipkeys</span><span class="o">=</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="n">ensure_ascii</span><span class="p">,</span>
</span><span id="original_json_dump-175"><a href="#original_json_dump-175"><span class="linenos">175</span></a>            <span class="n">check_circular</span><span class="o">=</span><span class="n">check_circular</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="n">allow_nan</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span>
</span><span id="original_json_dump-176"><a href="#original_json_dump-176"><span class="linenos">176</span></a>            <span class="n">separators</span><span class="o">=</span><span class="n">separators</span><span class="p">,</span>
</span><span id="original_json_dump-177"><a href="#original_json_dump-177"><span class="linenos">177</span></a>            <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="n">sort_keys</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span><span class="o">.</span><span class="n">iterencode</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="original_json_dump-178"><a href="#original_json_dump-178"><span class="linenos">178</span></a>    <span class="c1"># could accelerate with writelines in some versions of Python, at</span>
</span><span id="original_json_dump-179"><a href="#original_json_dump-179"><span class="linenos">179</span></a>    <span class="c1"># a debuggability cost</span>
</span><span id="original_json_dump-180"><a href="#original_json_dump-180"><span class="linenos">180</span></a>    <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">iterable</span><span class="p">:</span>
</span><span id="original_json_dump-181"><a href="#original_json_dump-181"><span class="linenos">181</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Serialize <code>obj</code> as a JSON formatted stream to <code>fp</code> (a
<code>.write()</code>-supporting file-like object).</p>

<p>If <code>skipkeys</code> is true then <code>dict</code> keys that are not basic types
(<code>str</code>, <code>int</code>, <code>float</code>, <code>bool</code>, <code>None</code>) will be skipped
instead of raising a <code>TypeError</code>.</p>

<p>If <code>ensure_ascii</code> is false, then the strings written to <code>fp</code> can
contain non-ASCII characters if they appear in strings contained in
<code>obj</code>. Otherwise, all such characters are escaped in JSON strings.</p>

<p>If <code>check_circular</code> is false, then the circular reference check
for container types will be skipped and a circular reference will
result in an <code>OverflowError</code> (or worse).</p>

<p>If <code>allow_nan</code> is false, then it will be a <code>ValueError</code> to
serialize out of range <code>float</code> values (<code>nan</code>, <code>inf</code>, <code>-inf</code>)
in strict compliance of the JSON specification, instead of using the
JavaScript equivalents (<code>NaN</code>, <code>Infinity</code>, <code>-Infinity</code>).</p>

<p>If <code>indent</code> is a non-negative integer, then JSON array elements and
object members will be pretty-printed with that indent level. An indent
level of 0 will only insert newlines. <code>None</code> is the most compact
representation.</p>

<p>If specified, <code>separators</code> should be an <code>(item_separator, key_separator)</code>
tuple.  The default is <code>(', ', ': ')</code> if <em>indent</em> is <code>None</code> and
<code>(',', ': ')</code> otherwise.  To get the most compact JSON representation,
you should specify <code>(',', ':')</code> to eliminate whitespace.</p>

<p><code>default(obj)</code> is a function that should return a serializable version
of obj or raise TypeError. The default simply raises TypeError.</p>

<p>If <em>sort_keys</em> is true (default: <code>False</code>), then the output of
dictionaries will be sorted by key.</p>

<p>To use a custom <code>JSONEncoder</code> subclass (e.g. one that overrides the
<code>.default()</code> method to serialize additional types), specify it with
the <code>cls</code> kwarg; otherwise <code>JSONEncoder</code> is used.</p>
</div>


                </section>
                <section id="original_json_dumps">
                            <input id="original_json_dumps-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">original_json_dumps</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">obj</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">skipkeys</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">ensure_ascii</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="n">check_circular</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="n">allow_nan</span><span class="o">=</span><span class="kc">True</span>,</span><span class="param">	<span class="bp">cls</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">indent</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">separators</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">default</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="o">**</span><span class="n">kw</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="original_json_dumps-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#original_json_dumps"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="original_json_dumps-184"><a href="#original_json_dumps-184"><span class="linenos">184</span></a><span class="k">def</span> <span class="nf">dumps</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">skipkeys</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">check_circular</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
</span><span id="original_json_dumps-185"><a href="#original_json_dumps-185"><span class="linenos">185</span></a>        <span class="n">allow_nan</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="bp">cls</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">separators</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="original_json_dumps-186"><a href="#original_json_dumps-186"><span class="linenos">186</span></a>        <span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_dumps-187"><a href="#original_json_dumps-187"><span class="linenos">187</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Serialize ``obj`` to a JSON formatted ``str``.</span>
</span><span id="original_json_dumps-188"><a href="#original_json_dumps-188"><span class="linenos">188</span></a>
</span><span id="original_json_dumps-189"><a href="#original_json_dumps-189"><span class="linenos">189</span></a><span class="sd">    If ``skipkeys`` is true then ``dict`` keys that are not basic types</span>
</span><span id="original_json_dumps-190"><a href="#original_json_dumps-190"><span class="linenos">190</span></a><span class="sd">    (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped</span>
</span><span id="original_json_dumps-191"><a href="#original_json_dumps-191"><span class="linenos">191</span></a><span class="sd">    instead of raising a ``TypeError``.</span>
</span><span id="original_json_dumps-192"><a href="#original_json_dumps-192"><span class="linenos">192</span></a>
</span><span id="original_json_dumps-193"><a href="#original_json_dumps-193"><span class="linenos">193</span></a><span class="sd">    If ``ensure_ascii`` is false, then the return value can contain non-ASCII</span>
</span><span id="original_json_dumps-194"><a href="#original_json_dumps-194"><span class="linenos">194</span></a><span class="sd">    characters if they appear in strings contained in ``obj``. Otherwise, all</span>
</span><span id="original_json_dumps-195"><a href="#original_json_dumps-195"><span class="linenos">195</span></a><span class="sd">    such characters are escaped in JSON strings.</span>
</span><span id="original_json_dumps-196"><a href="#original_json_dumps-196"><span class="linenos">196</span></a>
</span><span id="original_json_dumps-197"><a href="#original_json_dumps-197"><span class="linenos">197</span></a><span class="sd">    If ``check_circular`` is false, then the circular reference check</span>
</span><span id="original_json_dumps-198"><a href="#original_json_dumps-198"><span class="linenos">198</span></a><span class="sd">    for container types will be skipped and a circular reference will</span>
</span><span id="original_json_dumps-199"><a href="#original_json_dumps-199"><span class="linenos">199</span></a><span class="sd">    result in an ``OverflowError`` (or worse).</span>
</span><span id="original_json_dumps-200"><a href="#original_json_dumps-200"><span class="linenos">200</span></a>
</span><span id="original_json_dumps-201"><a href="#original_json_dumps-201"><span class="linenos">201</span></a><span class="sd">    If ``allow_nan`` is false, then it will be a ``ValueError`` to</span>
</span><span id="original_json_dumps-202"><a href="#original_json_dumps-202"><span class="linenos">202</span></a><span class="sd">    serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in</span>
</span><span id="original_json_dumps-203"><a href="#original_json_dumps-203"><span class="linenos">203</span></a><span class="sd">    strict compliance of the JSON specification, instead of using the</span>
</span><span id="original_json_dumps-204"><a href="#original_json_dumps-204"><span class="linenos">204</span></a><span class="sd">    JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).</span>
</span><span id="original_json_dumps-205"><a href="#original_json_dumps-205"><span class="linenos">205</span></a>
</span><span id="original_json_dumps-206"><a href="#original_json_dumps-206"><span class="linenos">206</span></a><span class="sd">    If ``indent`` is a non-negative integer, then JSON array elements and</span>
</span><span id="original_json_dumps-207"><a href="#original_json_dumps-207"><span class="linenos">207</span></a><span class="sd">    object members will be pretty-printed with that indent level. An indent</span>
</span><span id="original_json_dumps-208"><a href="#original_json_dumps-208"><span class="linenos">208</span></a><span class="sd">    level of 0 will only insert newlines. ``None`` is the most compact</span>
</span><span id="original_json_dumps-209"><a href="#original_json_dumps-209"><span class="linenos">209</span></a><span class="sd">    representation.</span>
</span><span id="original_json_dumps-210"><a href="#original_json_dumps-210"><span class="linenos">210</span></a>
</span><span id="original_json_dumps-211"><a href="#original_json_dumps-211"><span class="linenos">211</span></a><span class="sd">    If specified, ``separators`` should be an ``(item_separator, key_separator)``</span>
</span><span id="original_json_dumps-212"><a href="#original_json_dumps-212"><span class="linenos">212</span></a><span class="sd">    tuple.  The default is ``(&#39;, &#39;, &#39;: &#39;)`` if *indent* is ``None`` and</span>
</span><span id="original_json_dumps-213"><a href="#original_json_dumps-213"><span class="linenos">213</span></a><span class="sd">    ``(&#39;,&#39;, &#39;: &#39;)`` otherwise.  To get the most compact JSON representation,</span>
</span><span id="original_json_dumps-214"><a href="#original_json_dumps-214"><span class="linenos">214</span></a><span class="sd">    you should specify ``(&#39;,&#39;, &#39;:&#39;)`` to eliminate whitespace.</span>
</span><span id="original_json_dumps-215"><a href="#original_json_dumps-215"><span class="linenos">215</span></a>
</span><span id="original_json_dumps-216"><a href="#original_json_dumps-216"><span class="linenos">216</span></a><span class="sd">    ``default(obj)`` is a function that should return a serializable version</span>
</span><span id="original_json_dumps-217"><a href="#original_json_dumps-217"><span class="linenos">217</span></a><span class="sd">    of obj or raise TypeError. The default simply raises TypeError.</span>
</span><span id="original_json_dumps-218"><a href="#original_json_dumps-218"><span class="linenos">218</span></a>
</span><span id="original_json_dumps-219"><a href="#original_json_dumps-219"><span class="linenos">219</span></a><span class="sd">    If *sort_keys* is true (default: ``False``), then the output of</span>
</span><span id="original_json_dumps-220"><a href="#original_json_dumps-220"><span class="linenos">220</span></a><span class="sd">    dictionaries will be sorted by key.</span>
</span><span id="original_json_dumps-221"><a href="#original_json_dumps-221"><span class="linenos">221</span></a>
</span><span id="original_json_dumps-222"><a href="#original_json_dumps-222"><span class="linenos">222</span></a><span class="sd">    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the</span>
</span><span id="original_json_dumps-223"><a href="#original_json_dumps-223"><span class="linenos">223</span></a><span class="sd">    ``.default()`` method to serialize additional types), specify it with</span>
</span><span id="original_json_dumps-224"><a href="#original_json_dumps-224"><span class="linenos">224</span></a><span class="sd">    the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.</span>
</span><span id="original_json_dumps-225"><a href="#original_json_dumps-225"><span class="linenos">225</span></a>
</span><span id="original_json_dumps-226"><a href="#original_json_dumps-226"><span class="linenos">226</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="original_json_dumps-227"><a href="#original_json_dumps-227"><span class="linenos">227</span></a>    <span class="c1"># cached encoder</span>
</span><span id="original_json_dumps-228"><a href="#original_json_dumps-228"><span class="linenos">228</span></a>    <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">skipkeys</span> <span class="ow">and</span> <span class="n">ensure_ascii</span> <span class="ow">and</span>
</span><span id="original_json_dumps-229"><a href="#original_json_dumps-229"><span class="linenos">229</span></a>        <span class="n">check_circular</span> <span class="ow">and</span> <span class="n">allow_nan</span> <span class="ow">and</span>
</span><span id="original_json_dumps-230"><a href="#original_json_dumps-230"><span class="linenos">230</span></a>        <span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">indent</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">separators</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="original_json_dumps-231"><a href="#original_json_dumps-231"><span class="linenos">231</span></a>        <span class="n">default</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">sort_keys</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_dumps-232"><a href="#original_json_dumps-232"><span class="linenos">232</span></a>        <span class="k">return</span> <span class="n">_default_encoder</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="original_json_dumps-233"><a href="#original_json_dumps-233"><span class="linenos">233</span></a>    <span class="k">if</span> <span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_dumps-234"><a href="#original_json_dumps-234"><span class="linenos">234</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="n">JSONEncoder</span>
</span><span id="original_json_dumps-235"><a href="#original_json_dumps-235"><span class="linenos">235</span></a>    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span>
</span><span id="original_json_dumps-236"><a href="#original_json_dumps-236"><span class="linenos">236</span></a>        <span class="n">skipkeys</span><span class="o">=</span><span class="n">skipkeys</span><span class="p">,</span> <span class="n">ensure_ascii</span><span class="o">=</span><span class="n">ensure_ascii</span><span class="p">,</span>
</span><span id="original_json_dumps-237"><a href="#original_json_dumps-237"><span class="linenos">237</span></a>        <span class="n">check_circular</span><span class="o">=</span><span class="n">check_circular</span><span class="p">,</span> <span class="n">allow_nan</span><span class="o">=</span><span class="n">allow_nan</span><span class="p">,</span> <span class="n">indent</span><span class="o">=</span><span class="n">indent</span><span class="p">,</span>
</span><span id="original_json_dumps-238"><a href="#original_json_dumps-238"><span class="linenos">238</span></a>        <span class="n">separators</span><span class="o">=</span><span class="n">separators</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="n">default</span><span class="p">,</span> <span class="n">sort_keys</span><span class="o">=</span><span class="n">sort_keys</span><span class="p">,</span>
</span><span id="original_json_dumps-239"><a href="#original_json_dumps-239"><span class="linenos">239</span></a>        <span class="o">**</span><span class="n">kw</span><span class="p">)</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Serialize <code>obj</code> to a JSON formatted <code>str</code>.</p>

<p>If <code>skipkeys</code> is true then <code>dict</code> keys that are not basic types
(<code>str</code>, <code>int</code>, <code>float</code>, <code>bool</code>, <code>None</code>) will be skipped
instead of raising a <code>TypeError</code>.</p>

<p>If <code>ensure_ascii</code> is false, then the return value can contain non-ASCII
characters if they appear in strings contained in <code>obj</code>. Otherwise, all
such characters are escaped in JSON strings.</p>

<p>If <code>check_circular</code> is false, then the circular reference check
for container types will be skipped and a circular reference will
result in an <code>OverflowError</code> (or worse).</p>

<p>If <code>allow_nan</code> is false, then it will be a <code>ValueError</code> to
serialize out of range <code>float</code> values (<code>nan</code>, <code>inf</code>, <code>-inf</code>) in
strict compliance of the JSON specification, instead of using the
JavaScript equivalents (<code>NaN</code>, <code>Infinity</code>, <code>-Infinity</code>).</p>

<p>If <code>indent</code> is a non-negative integer, then JSON array elements and
object members will be pretty-printed with that indent level. An indent
level of 0 will only insert newlines. <code>None</code> is the most compact
representation.</p>

<p>If specified, <code>separators</code> should be an <code>(item_separator, key_separator)</code>
tuple.  The default is <code>(', ', ': ')</code> if <em>indent</em> is <code>None</code> and
<code>(',', ': ')</code> otherwise.  To get the most compact JSON representation,
you should specify <code>(',', ':')</code> to eliminate whitespace.</p>

<p><code>default(obj)</code> is a function that should return a serializable version
of obj or raise TypeError. The default simply raises TypeError.</p>

<p>If <em>sort_keys</em> is true (default: <code>False</code>), then the output of
dictionaries will be sorted by key.</p>

<p>To use a custom <code>JSONEncoder</code> subclass (e.g. one that overrides the
<code>.default()</code> method to serialize additional types), specify it with
the <code>cls</code> kwarg; otherwise <code>JSONEncoder</code> is used.</p>
</div>


                </section>
                <section id="original_json_load">
                            <input id="original_json_load-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">original_json_load</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">fp</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="bp">cls</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">object_hook</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_float</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_int</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_constant</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">object_pairs_hook</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kw</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="original_json_load-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#original_json_load"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="original_json_load-275"><a href="#original_json_load-275"><span class="linenos">275</span></a><span class="k">def</span> <span class="nf">load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="bp">cls</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">object_hook</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">parse_float</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="original_json_load-276"><a href="#original_json_load-276"><span class="linenos">276</span></a>        <span class="n">parse_int</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">parse_constant</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_load-277"><a href="#original_json_load-277"><span class="linenos">277</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Deserialize ``fp`` (a ``.read()``-supporting file-like object containing</span>
</span><span id="original_json_load-278"><a href="#original_json_load-278"><span class="linenos">278</span></a><span class="sd">    a JSON document) to a Python object.</span>
</span><span id="original_json_load-279"><a href="#original_json_load-279"><span class="linenos">279</span></a>
</span><span id="original_json_load-280"><a href="#original_json_load-280"><span class="linenos">280</span></a><span class="sd">    ``object_hook`` is an optional function that will be called with the</span>
</span><span id="original_json_load-281"><a href="#original_json_load-281"><span class="linenos">281</span></a><span class="sd">    result of any object literal decode (a ``dict``). The return value of</span>
</span><span id="original_json_load-282"><a href="#original_json_load-282"><span class="linenos">282</span></a><span class="sd">    ``object_hook`` will be used instead of the ``dict``. This feature</span>
</span><span id="original_json_load-283"><a href="#original_json_load-283"><span class="linenos">283</span></a><span class="sd">    can be used to implement custom decoders (e.g. JSON-RPC class hinting).</span>
</span><span id="original_json_load-284"><a href="#original_json_load-284"><span class="linenos">284</span></a>
</span><span id="original_json_load-285"><a href="#original_json_load-285"><span class="linenos">285</span></a><span class="sd">    ``object_pairs_hook`` is an optional function that will be called with the</span>
</span><span id="original_json_load-286"><a href="#original_json_load-286"><span class="linenos">286</span></a><span class="sd">    result of any object literal decoded with an ordered list of pairs.  The</span>
</span><span id="original_json_load-287"><a href="#original_json_load-287"><span class="linenos">287</span></a><span class="sd">    return value of ``object_pairs_hook`` will be used instead of the ``dict``.</span>
</span><span id="original_json_load-288"><a href="#original_json_load-288"><span class="linenos">288</span></a><span class="sd">    This feature can be used to implement custom decoders.  If ``object_hook``</span>
</span><span id="original_json_load-289"><a href="#original_json_load-289"><span class="linenos">289</span></a><span class="sd">    is also defined, the ``object_pairs_hook`` takes priority.</span>
</span><span id="original_json_load-290"><a href="#original_json_load-290"><span class="linenos">290</span></a>
</span><span id="original_json_load-291"><a href="#original_json_load-291"><span class="linenos">291</span></a><span class="sd">    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``</span>
</span><span id="original_json_load-292"><a href="#original_json_load-292"><span class="linenos">292</span></a><span class="sd">    kwarg; otherwise ``JSONDecoder`` is used.</span>
</span><span id="original_json_load-293"><a href="#original_json_load-293"><span class="linenos">293</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="original_json_load-294"><a href="#original_json_load-294"><span class="linenos">294</span></a>    <span class="k">return</span> <span class="n">loads</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span>
</span><span id="original_json_load-295"><a href="#original_json_load-295"><span class="linenos">295</span></a>        <span class="bp">cls</span><span class="o">=</span><span class="bp">cls</span><span class="p">,</span> <span class="n">object_hook</span><span class="o">=</span><span class="n">object_hook</span><span class="p">,</span>
</span><span id="original_json_load-296"><a href="#original_json_load-296"><span class="linenos">296</span></a>        <span class="n">parse_float</span><span class="o">=</span><span class="n">parse_float</span><span class="p">,</span> <span class="n">parse_int</span><span class="o">=</span><span class="n">parse_int</span><span class="p">,</span>
</span><span id="original_json_load-297"><a href="#original_json_load-297"><span class="linenos">297</span></a>        <span class="n">parse_constant</span><span class="o">=</span><span class="n">parse_constant</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="n">object_pairs_hook</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Deserialize <code>fp</code> (a <code>.read()</code>-supporting file-like object containing
a JSON document) to a Python object.</p>

<p><code>object_hook</code> is an optional function that will be called with the
result of any object literal decode (a <code>dict</code>). The return value of
<code>object_hook</code> will be used instead of the <code>dict</code>. This feature
can be used to implement custom decoders (e.g. JSON-RPC class hinting).</p>

<p><code>object_pairs_hook</code> is an optional function that will be called with the
result of any object literal decoded with an ordered list of pairs.  The
return value of <code>object_pairs_hook</code> will be used instead of the <code>dict</code>.
This feature can be used to implement custom decoders.  If <code>object_hook</code>
is also defined, the <code>object_pairs_hook</code> takes priority.</p>

<p>To use a custom <code>JSONDecoder</code> subclass, specify it with the <code>cls</code>
kwarg; otherwise <code>JSONDecoder</code> is used.</p>
</div>


                </section>
                <section id="original_json_loads">
                            <input id="original_json_loads-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">original_json_loads</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">s</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="bp">cls</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">object_hook</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_float</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_int</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">parse_constant</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">object_pairs_hook</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kw</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="original_json_loads-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#original_json_loads"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="original_json_loads-300"><a href="#original_json_loads-300"><span class="linenos">300</span></a><span class="k">def</span> <span class="nf">loads</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="bp">cls</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">object_hook</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">parse_float</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="original_json_loads-301"><a href="#original_json_loads-301"><span class="linenos">301</span></a>        <span class="n">parse_int</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">parse_constant</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">object_pairs_hook</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_loads-302"><a href="#original_json_loads-302"><span class="linenos">302</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance</span>
</span><span id="original_json_loads-303"><a href="#original_json_loads-303"><span class="linenos">303</span></a><span class="sd">    containing a JSON document) to a Python object.</span>
</span><span id="original_json_loads-304"><a href="#original_json_loads-304"><span class="linenos">304</span></a>
</span><span id="original_json_loads-305"><a href="#original_json_loads-305"><span class="linenos">305</span></a><span class="sd">    ``object_hook`` is an optional function that will be called with the</span>
</span><span id="original_json_loads-306"><a href="#original_json_loads-306"><span class="linenos">306</span></a><span class="sd">    result of any object literal decode (a ``dict``). The return value of</span>
</span><span id="original_json_loads-307"><a href="#original_json_loads-307"><span class="linenos">307</span></a><span class="sd">    ``object_hook`` will be used instead of the ``dict``. This feature</span>
</span><span id="original_json_loads-308"><a href="#original_json_loads-308"><span class="linenos">308</span></a><span class="sd">    can be used to implement custom decoders (e.g. JSON-RPC class hinting).</span>
</span><span id="original_json_loads-309"><a href="#original_json_loads-309"><span class="linenos">309</span></a>
</span><span id="original_json_loads-310"><a href="#original_json_loads-310"><span class="linenos">310</span></a><span class="sd">    ``object_pairs_hook`` is an optional function that will be called with the</span>
</span><span id="original_json_loads-311"><a href="#original_json_loads-311"><span class="linenos">311</span></a><span class="sd">    result of any object literal decoded with an ordered list of pairs.  The</span>
</span><span id="original_json_loads-312"><a href="#original_json_loads-312"><span class="linenos">312</span></a><span class="sd">    return value of ``object_pairs_hook`` will be used instead of the ``dict``.</span>
</span><span id="original_json_loads-313"><a href="#original_json_loads-313"><span class="linenos">313</span></a><span class="sd">    This feature can be used to implement custom decoders.  If ``object_hook``</span>
</span><span id="original_json_loads-314"><a href="#original_json_loads-314"><span class="linenos">314</span></a><span class="sd">    is also defined, the ``object_pairs_hook`` takes priority.</span>
</span><span id="original_json_loads-315"><a href="#original_json_loads-315"><span class="linenos">315</span></a>
</span><span id="original_json_loads-316"><a href="#original_json_loads-316"><span class="linenos">316</span></a><span class="sd">    ``parse_float``, if specified, will be called with the string</span>
</span><span id="original_json_loads-317"><a href="#original_json_loads-317"><span class="linenos">317</span></a><span class="sd">    of every JSON float to be decoded. By default this is equivalent to</span>
</span><span id="original_json_loads-318"><a href="#original_json_loads-318"><span class="linenos">318</span></a><span class="sd">    float(num_str). This can be used to use another datatype or parser</span>
</span><span id="original_json_loads-319"><a href="#original_json_loads-319"><span class="linenos">319</span></a><span class="sd">    for JSON floats (e.g. decimal.Decimal).</span>
</span><span id="original_json_loads-320"><a href="#original_json_loads-320"><span class="linenos">320</span></a>
</span><span id="original_json_loads-321"><a href="#original_json_loads-321"><span class="linenos">321</span></a><span class="sd">    ``parse_int``, if specified, will be called with the string</span>
</span><span id="original_json_loads-322"><a href="#original_json_loads-322"><span class="linenos">322</span></a><span class="sd">    of every JSON int to be decoded. By default this is equivalent to</span>
</span><span id="original_json_loads-323"><a href="#original_json_loads-323"><span class="linenos">323</span></a><span class="sd">    int(num_str). This can be used to use another datatype or parser</span>
</span><span id="original_json_loads-324"><a href="#original_json_loads-324"><span class="linenos">324</span></a><span class="sd">    for JSON integers (e.g. float).</span>
</span><span id="original_json_loads-325"><a href="#original_json_loads-325"><span class="linenos">325</span></a>
</span><span id="original_json_loads-326"><a href="#original_json_loads-326"><span class="linenos">326</span></a><span class="sd">    ``parse_constant``, if specified, will be called with one of the</span>
</span><span id="original_json_loads-327"><a href="#original_json_loads-327"><span class="linenos">327</span></a><span class="sd">    following strings: -Infinity, Infinity, NaN.</span>
</span><span id="original_json_loads-328"><a href="#original_json_loads-328"><span class="linenos">328</span></a><span class="sd">    This can be used to raise an exception if invalid JSON numbers</span>
</span><span id="original_json_loads-329"><a href="#original_json_loads-329"><span class="linenos">329</span></a><span class="sd">    are encountered.</span>
</span><span id="original_json_loads-330"><a href="#original_json_loads-330"><span class="linenos">330</span></a>
</span><span id="original_json_loads-331"><a href="#original_json_loads-331"><span class="linenos">331</span></a><span class="sd">    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``</span>
</span><span id="original_json_loads-332"><a href="#original_json_loads-332"><span class="linenos">332</span></a><span class="sd">    kwarg; otherwise ``JSONDecoder`` is used.</span>
</span><span id="original_json_loads-333"><a href="#original_json_loads-333"><span class="linenos">333</span></a>
</span><span id="original_json_loads-334"><a href="#original_json_loads-334"><span class="linenos">334</span></a><span class="sd">    The ``encoding`` argument is ignored and deprecated since Python 3.1.</span>
</span><span id="original_json_loads-335"><a href="#original_json_loads-335"><span class="linenos">335</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="original_json_loads-336"><a href="#original_json_loads-336"><span class="linenos">336</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="original_json_loads-337"><a href="#original_json_loads-337"><span class="linenos">337</span></a>        <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\ufeff</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="original_json_loads-338"><a href="#original_json_loads-338"><span class="linenos">338</span></a>            <span class="k">raise</span> <span class="n">JSONDecodeError</span><span class="p">(</span><span class="s2">&quot;Unexpected UTF-8 BOM (decode using utf-8-sig)&quot;</span><span class="p">,</span>
</span><span id="original_json_loads-339"><a href="#original_json_loads-339"><span class="linenos">339</span></a>                                  <span class="n">s</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="original_json_loads-340"><a href="#original_json_loads-340"><span class="linenos">340</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="original_json_loads-341"><a href="#original_json_loads-341"><span class="linenos">341</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">)):</span>
</span><span id="original_json_loads-342"><a href="#original_json_loads-342"><span class="linenos">342</span></a>            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;the JSON object must be str, bytes or bytearray, &#39;</span>
</span><span id="original_json_loads-343"><a href="#original_json_loads-343"><span class="linenos">343</span></a>                            <span class="sa">f</span><span class="s1">&#39;not </span><span class="si">{</span><span class="n">s</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="original_json_loads-344"><a href="#original_json_loads-344"><span class="linenos">344</span></a>        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">detect_encoding</span><span class="p">(</span><span class="n">s</span><span class="p">),</span> <span class="s1">&#39;surrogatepass&#39;</span><span class="p">)</span>
</span><span id="original_json_loads-345"><a href="#original_json_loads-345"><span class="linenos">345</span></a>
</span><span id="original_json_loads-346"><a href="#original_json_loads-346"><span class="linenos">346</span></a>    <span class="k">if</span> <span class="s2">&quot;encoding&quot;</span> <span class="ow">in</span> <span class="n">kw</span><span class="p">:</span>
</span><span id="original_json_loads-347"><a href="#original_json_loads-347"><span class="linenos">347</span></a>        <span class="kn">import</span> <span class="nn">warnings</span>
</span><span id="original_json_loads-348"><a href="#original_json_loads-348"><span class="linenos">348</span></a>        <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span>
</span><span id="original_json_loads-349"><a href="#original_json_loads-349"><span class="linenos">349</span></a>            <span class="s2">&quot;&#39;encoding&#39; is ignored and deprecated. It will be removed in Python 3.9&quot;</span><span class="p">,</span>
</span><span id="original_json_loads-350"><a href="#original_json_loads-350"><span class="linenos">350</span></a>            <span class="ne">DeprecationWarning</span><span class="p">,</span>
</span><span id="original_json_loads-351"><a href="#original_json_loads-351"><span class="linenos">351</span></a>            <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span>
</span><span id="original_json_loads-352"><a href="#original_json_loads-352"><span class="linenos">352</span></a>        <span class="p">)</span>
</span><span id="original_json_loads-353"><a href="#original_json_loads-353"><span class="linenos">353</span></a>        <span class="k">del</span> <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;encoding&#39;</span><span class="p">]</span>
</span><span id="original_json_loads-354"><a href="#original_json_loads-354"><span class="linenos">354</span></a>
</span><span id="original_json_loads-355"><a href="#original_json_loads-355"><span class="linenos">355</span></a>    <span class="k">if</span> <span class="p">(</span><span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">object_hook</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="original_json_loads-356"><a href="#original_json_loads-356"><span class="linenos">356</span></a>            <span class="n">parse_int</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">parse_float</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="original_json_loads-357"><a href="#original_json_loads-357"><span class="linenos">357</span></a>            <span class="n">parse_constant</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">object_pairs_hook</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">kw</span><span class="p">):</span>
</span><span id="original_json_loads-358"><a href="#original_json_loads-358"><span class="linenos">358</span></a>        <span class="k">return</span> <span class="n">_default_decoder</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
</span><span id="original_json_loads-359"><a href="#original_json_loads-359"><span class="linenos">359</span></a>    <span class="k">if</span> <span class="bp">cls</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-360"><a href="#original_json_loads-360"><span class="linenos">360</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="n">JSONDecoder</span>
</span><span id="original_json_loads-361"><a href="#original_json_loads-361"><span class="linenos">361</span></a>    <span class="k">if</span> <span class="n">object_hook</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-362"><a href="#original_json_loads-362"><span class="linenos">362</span></a>        <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;object_hook&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">object_hook</span>
</span><span id="original_json_loads-363"><a href="#original_json_loads-363"><span class="linenos">363</span></a>    <span class="k">if</span> <span class="n">object_pairs_hook</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-364"><a href="#original_json_loads-364"><span class="linenos">364</span></a>        <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">object_pairs_hook</span>
</span><span id="original_json_loads-365"><a href="#original_json_loads-365"><span class="linenos">365</span></a>    <span class="k">if</span> <span class="n">parse_float</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-366"><a href="#original_json_loads-366"><span class="linenos">366</span></a>        <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;parse_float&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">parse_float</span>
</span><span id="original_json_loads-367"><a href="#original_json_loads-367"><span class="linenos">367</span></a>    <span class="k">if</span> <span class="n">parse_int</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-368"><a href="#original_json_loads-368"><span class="linenos">368</span></a>        <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;parse_int&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">parse_int</span>
</span><span id="original_json_loads-369"><a href="#original_json_loads-369"><span class="linenos">369</span></a>    <span class="k">if</span> <span class="n">parse_constant</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="original_json_loads-370"><a href="#original_json_loads-370"><span class="linenos">370</span></a>        <span class="n">kw</span><span class="p">[</span><span class="s1">&#39;parse_constant&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">parse_constant</span>
</span><span id="original_json_loads-371"><a href="#original_json_loads-371"><span class="linenos">371</span></a>    <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">**</span><span class="n">kw</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Deserialize <code>s</code> (a <code>str</code>, <code>bytes</code> or <code>bytearray</code> instance
containing a JSON document) to a Python object.</p>

<p><code>object_hook</code> is an optional function that will be called with the
result of any object literal decode (a <code>dict</code>). The return value of
<code>object_hook</code> will be used instead of the <code>dict</code>. This feature
can be used to implement custom decoders (e.g. JSON-RPC class hinting).</p>

<p><code>object_pairs_hook</code> is an optional function that will be called with the
result of any object literal decoded with an ordered list of pairs.  The
return value of <code>object_pairs_hook</code> will be used instead of the <code>dict</code>.
This feature can be used to implement custom decoders.  If <code>object_hook</code>
is also defined, the <code>object_pairs_hook</code> takes priority.</p>

<p><code>parse_float</code>, if specified, will be called with the string
of every JSON float to be decoded. By default this is equivalent to
float(num_str). This can be used to use another datatype or parser
for JSON floats (e.g. decimal.Decimal).</p>

<p><code>parse_int</code>, if specified, will be called with the string
of every JSON int to be decoded. By default this is equivalent to
int(num_str). This can be used to use another datatype or parser
for JSON integers (e.g. float).</p>

<p><code>parse_constant</code>, if specified, will be called with one of the
following strings: -Infinity, Infinity, NaN.
This can be used to raise an exception if invalid JSON numbers
are encountered.</p>

<p>To use a custom <code>JSONDecoder</code> subclass, specify it with the <code>cls</code>
kwarg; otherwise <code>JSONDecoder</code> is used.</p>

<p>The <code>encoding</code> argument is ignored and deprecated since Python 3.1.</p>
</div>


                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>