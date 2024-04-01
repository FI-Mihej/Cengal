---
title: aggregator_view
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.user_interface<wbr>.gui<wbr>.tkinter<wbr>.components<wbr>.aggregator_view<wbr>.versions<wbr>.v_0<wbr>.aggregator_view    </h1>

                
                        <input id="mod-aggregator_view-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-aggregator_view-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;AggregatorAppendFormatter&#39;</span><span class="p">,</span> <span class="s1">&#39;AggregatorView&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="sd">Module Docstring</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">math</span> <span class="kn">import</span> <span class="n">ceil</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">import</span> <span class="nn">ttkbootstrap</span> <span class="k">as</span> <span class="nn">ttkb</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">ttkbootstrap.constants</span> <span class="kn">import</span> <span class="n">INSERT</span> <span class="k">as</span> <span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">CURRENT</span> <span class="k">as</span> <span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="n">SEL_FIRST</span> <span class="k">as</span> <span class="n">ttkb__SEL_FIRST</span><span class="p">,</span> <span class="n">SEL_LAST</span> <span class="k">as</span> <span class="n">ttkb__SEL_LAST</span><span class="p">,</span> <span class="n">SEL</span> <span class="k">as</span> <span class="n">ttkb__SEL</span><span class="p">,</span> <span class="n">END</span> <span class="k">as</span> <span class="n">ttkb__END</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">ttkbootstrap</span> <span class="kn">import</span> <span class="n">Style</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.tkinter</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.sleep</span> <span class="kn">import</span> <span class="n">Sleep</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">cengal.user_interface.gui.tkinter.components.read_only_text</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="k">class</span> <span class="nc">AggregatorAppendFormatter</span><span class="p">:</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">initial_text</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">current_interface</span><span class="p">()</span><span class="o">.</span><span class="n">coro_id</span><span class="si">}</span><span class="s1">. </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">initial_text</span><span class="si">}</span><span class="s1">:</span><span class="se">\n</span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="k">class</span> <span class="nc">AggregatorView</span><span class="p">(</span><span class="n">ttkb</span><span class="o">.</span><span class="n">Frame</span><span class="p">):</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">default_auto_scroll</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">append_data</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">updating_interval</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">aggregator_key</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_formatter_func</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_len</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="n">text_area_config</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>            <span class="s1">&#39;highlightcolor&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">primary</span><span class="p">,</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>            <span class="s1">&#39;highlightbackground&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">border</span><span class="p">,</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>            <span class="s1">&#39;highlightthickness&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>            <span class="s1">&#39;wrap&#39;</span><span class="p">:</span> <span class="s1">&#39;none&#39;</span><span class="p">,</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="p">}</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="k">if</span> <span class="n">width</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>                <span class="s1">&#39;width&#39;</span><span class="p">:</span> <span class="n">width</span><span class="p">,</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>            <span class="p">})</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="k">if</span> <span class="n">height</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>                <span class="s1">&#39;height&#39;</span><span class="p">:</span> <span class="n">height</span><span class="p">,</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>            <span class="p">})</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span> <span class="o">=</span> <span class="n">ReadOnlyText</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">text_area_config</span><span class="p">)</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s1">&#39;both&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="s1">&#39;yes&#39;</span><span class="p">)</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="p">[</span><span class="s1">&#39;yscrollcommand&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">yscroll</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">command</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">yview</span><span class="p">)</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">default_auto_scroll</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yscroll</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_lines_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yview</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-3&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b3_down</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">append_data</span><span class="p">:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;&lt;Selection&gt;&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_changed</span><span class="p">)</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Double-Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_double</span><span class="p">)</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_down</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;B1-Motion&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_motion</span><span class="p">)</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;ButtonRelease-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_up</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Control-a&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ctrl_a</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">ctrl_a</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="s1">&#39;end&#39;</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">clear_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="nf">normalize_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>            <span class="k">if</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>            <span class="k">elif</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>                <span class="k">pass</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>                <span class="n">sel_left</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>                <span class="n">sel_right</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>                <span class="k">if</span> <span class="n">sel_left</span> <span class="o">&gt;</span> <span class="n">sel_right</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">apply_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>                <span class="k">return</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>            
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">)</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_up</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">!=</span> <span class="n">selection_last</span><span class="p">:</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_motion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>    
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_double</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span><span class="p">:</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> linestart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> lineend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordstart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="nf">mouse_b3_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="n">selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="n">current_selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">current_selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_FIRST</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="n">current_selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_LAST</span><span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="k">if</span> <span class="n">current_selection_first</span> <span class="ow">and</span> <span class="n">current_selection_last</span><span class="p">:</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>                <span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_selection_first</span><span class="p">,</span> <span class="n">current_selection_last</span><span class="p">)</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="k">if</span> <span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_clear</span><span class="p">()</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>            <span class="n">text_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_append</span><span class="p">(</span><span class="n">text_content</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>    
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="k">def</span> <span class="nf">selection_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">return</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="n">lines_num_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="n">view_fractions_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>        <span class="n">line_before</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_before</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_before</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="n">tag_insert_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="n">tag_current_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">)</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_context</span><span class="p">()</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="n">ttkb__END</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="n">tag_current_before</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="n">lines_num_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="n">view_fractions_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_after</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_after</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>            
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            <span class="n">line_before</span> <span class="o">=</span> <span class="n">line_before</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="n">line_after</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="k">if</span> <span class="n">line_after</span> <span class="o">!=</span> <span class="n">line_before</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                <span class="n">movement</span> <span class="o">=</span> <span class="n">line_before</span> <span class="o">-</span> <span class="n">line_after</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview_scroll</span><span class="p">(</span><span class="n">movement</span><span class="p">,</span> <span class="s1">&#39;units&#39;</span><span class="p">)</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="nf">clear_context</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>    <span class="k">def</span> <span class="nf">yscroll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        <span class="n">first</span><span class="p">,</span> <span class="n">last</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="n">lines_num</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="n">last_line_index</span> <span class="o">=</span> <span class="n">lines_num</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="n">first_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">first</span><span class="p">)))</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="n">last_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">last</span><span class="p">)))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&lt;</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&gt;=</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">==</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">yview</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wr</span><span class="p">:</span> <span class="n">TkObjWrapper</span><span class="p">):</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="n">wr</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_updater</span><span class="p">)</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>    
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="nf">_updater</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span><span class="p">:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">max_len</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_len</span><span class="p">):</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">,</span> <span class="n">AggregatorAppendFormatter</span><span class="p">):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>                        <span class="n">auto_scroll_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">clear_context</span><span class="p">()</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="n">auto_scroll_buff</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                    
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">FastAggregator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">aggregator_key</span><span class="p">)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>                    <span class="n">text</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">data</span><span class="p">])</span> <span class="o">+</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>                    <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>                    
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                <span class="k">pass</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">updating_interval</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="AggregatorAppendFormatter">
                            <input id="AggregatorAppendFormatter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AggregatorAppendFormatter</span>:

                <label class="view-source-button" for="AggregatorAppendFormatter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorAppendFormatter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorAppendFormatter-52"><a href="#AggregatorAppendFormatter-52"><span class="linenos">52</span></a><span class="k">class</span> <span class="nc">AggregatorAppendFormatter</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter-53"><a href="#AggregatorAppendFormatter-53"><span class="linenos">53</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter-54"><a href="#AggregatorAppendFormatter-54"><span class="linenos">54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">initial_text</span>
</span><span id="AggregatorAppendFormatter-55"><a href="#AggregatorAppendFormatter-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorAppendFormatter-56"><a href="#AggregatorAppendFormatter-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorAppendFormatter-57"><a href="#AggregatorAppendFormatter-57"><span class="linenos">57</span></a>    
</span><span id="AggregatorAppendFormatter-58"><a href="#AggregatorAppendFormatter-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorAppendFormatter-59"><a href="#AggregatorAppendFormatter-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorAppendFormatter-60"><a href="#AggregatorAppendFormatter-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorAppendFormatter-61"><a href="#AggregatorAppendFormatter-61"><span class="linenos">61</span></a>    
</span><span id="AggregatorAppendFormatter-62"><a href="#AggregatorAppendFormatter-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter-63"><a href="#AggregatorAppendFormatter-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AggregatorAppendFormatter-64"><a href="#AggregatorAppendFormatter-64"><span class="linenos">64</span></a>        
</span><span id="AggregatorAppendFormatter-65"><a href="#AggregatorAppendFormatter-65"><span class="linenos">65</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter-66"><a href="#AggregatorAppendFormatter-66"><span class="linenos">66</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="AggregatorAppendFormatter-67"><a href="#AggregatorAppendFormatter-67"><span class="linenos">67</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter-68"><a href="#AggregatorAppendFormatter-68"><span class="linenos">68</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorAppendFormatter-69"><a href="#AggregatorAppendFormatter-69"><span class="linenos">69</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">current_interface</span><span class="p">()</span><span class="o">.</span><span class="n">coro_id</span><span class="si">}</span><span class="s1">. </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">initial_text</span><span class="si">}</span><span class="s1">:</span><span class="se">\n</span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


    

                            <div id="AggregatorAppendFormatter.__init__" class="classattr">
                                        <input id="AggregatorAppendFormatter.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">AggregatorAppendFormatter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span></span>)</span>

                <label class="view-source-button" for="AggregatorAppendFormatter.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorAppendFormatter.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorAppendFormatter.__init__-53"><a href="#AggregatorAppendFormatter.__init__-53"><span class="linenos">53</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorAppendFormatter.__init__-54"><a href="#AggregatorAppendFormatter.__init__-54"><span class="linenos">54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initial_text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">initial_text</span>
</span><span id="AggregatorAppendFormatter.__init__-55"><a href="#AggregatorAppendFormatter.__init__-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorAppendFormatter.__init__-56"><a href="#AggregatorAppendFormatter.__init__-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorAppendFormatter.initial_text" class="classattr">
                                <div class="attr variable">
            <span class="name">initial_text</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#AggregatorAppendFormatter.initial_text"></a>
    
    

                            </div>
                            <div id="AggregatorAppendFormatter.initiated" class="classattr">
                                <div class="attr variable">
            <span class="name">initiated</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AggregatorAppendFormatter.initiated"></a>
    
    

                            </div>
                            <div id="AggregatorAppendFormatter.reset" class="classattr">
                                        <input id="AggregatorAppendFormatter.reset-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">reset</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorAppendFormatter.reset-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorAppendFormatter.reset"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorAppendFormatter.reset-58"><a href="#AggregatorAppendFormatter.reset-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorAppendFormatter.reset-59"><a href="#AggregatorAppendFormatter.reset-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_items_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorAppendFormatter.reset-60"><a href="#AggregatorAppendFormatter.reset-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">initiated</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="AggregatorView">
                            <input id="AggregatorView-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AggregatorView</span><wbr>(<span class="base">tkinter.ttk.Frame</span>):

                <label class="view-source-button" for="AggregatorView-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView-72"><a href="#AggregatorView-72"><span class="linenos"> 72</span></a><span class="k">class</span> <span class="nc">AggregatorView</span><span class="p">(</span><span class="n">ttkb</span><span class="o">.</span><span class="n">Frame</span><span class="p">):</span>
</span><span id="AggregatorView-73"><a href="#AggregatorView-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">default_auto_scroll</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="AggregatorView-74"><a href="#AggregatorView-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">append_data</span>
</span><span id="AggregatorView-75"><a href="#AggregatorView-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">updating_interval</span>
</span><span id="AggregatorView-76"><a href="#AggregatorView-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">aggregator_key</span>
</span><span id="AggregatorView-77"><a href="#AggregatorView-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="AggregatorView-78"><a href="#AggregatorView-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_formatter_func</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span>
</span><span id="AggregatorView-79"><a href="#AggregatorView-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-80"><a href="#AggregatorView-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView-81"><a href="#AggregatorView-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_len</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-82"><a href="#AggregatorView-82"><span class="linenos"> 82</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="AggregatorView-83"><a href="#AggregatorView-83"><span class="linenos"> 83</span></a>
</span><span id="AggregatorView-84"><a href="#AggregatorView-84"><span class="linenos"> 84</span></a>        <span class="n">text_area_config</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="AggregatorView-85"><a href="#AggregatorView-85"><span class="linenos"> 85</span></a>            <span class="s1">&#39;highlightcolor&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">primary</span><span class="p">,</span>
</span><span id="AggregatorView-86"><a href="#AggregatorView-86"><span class="linenos"> 86</span></a>            <span class="s1">&#39;highlightbackground&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">border</span><span class="p">,</span>
</span><span id="AggregatorView-87"><a href="#AggregatorView-87"><span class="linenos"> 87</span></a>            <span class="s1">&#39;highlightthickness&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="AggregatorView-88"><a href="#AggregatorView-88"><span class="linenos"> 88</span></a>            <span class="s1">&#39;wrap&#39;</span><span class="p">:</span> <span class="s1">&#39;none&#39;</span><span class="p">,</span>
</span><span id="AggregatorView-89"><a href="#AggregatorView-89"><span class="linenos"> 89</span></a>        <span class="p">}</span>
</span><span id="AggregatorView-90"><a href="#AggregatorView-90"><span class="linenos"> 90</span></a>        <span class="k">if</span> <span class="n">width</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-91"><a href="#AggregatorView-91"><span class="linenos"> 91</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="AggregatorView-92"><a href="#AggregatorView-92"><span class="linenos"> 92</span></a>                <span class="s1">&#39;width&#39;</span><span class="p">:</span> <span class="n">width</span><span class="p">,</span>
</span><span id="AggregatorView-93"><a href="#AggregatorView-93"><span class="linenos"> 93</span></a>            <span class="p">})</span>
</span><span id="AggregatorView-94"><a href="#AggregatorView-94"><span class="linenos"> 94</span></a>        
</span><span id="AggregatorView-95"><a href="#AggregatorView-95"><span class="linenos"> 95</span></a>        <span class="k">if</span> <span class="n">height</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-96"><a href="#AggregatorView-96"><span class="linenos"> 96</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="AggregatorView-97"><a href="#AggregatorView-97"><span class="linenos"> 97</span></a>                <span class="s1">&#39;height&#39;</span><span class="p">:</span> <span class="n">height</span><span class="p">,</span>
</span><span id="AggregatorView-98"><a href="#AggregatorView-98"><span class="linenos"> 98</span></a>            <span class="p">})</span>
</span><span id="AggregatorView-99"><a href="#AggregatorView-99"><span class="linenos"> 99</span></a>        
</span><span id="AggregatorView-100"><a href="#AggregatorView-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span> <span class="o">=</span> <span class="n">ReadOnlyText</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">text_area_config</span><span class="p">)</span>
</span><span id="AggregatorView-101"><a href="#AggregatorView-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s1">&#39;both&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="s1">&#39;yes&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-102"><a href="#AggregatorView-102"><span class="linenos">102</span></a>
</span><span id="AggregatorView-103"><a href="#AggregatorView-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="p">[</span><span class="s1">&#39;yscrollcommand&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">yscroll</span>
</span><span id="AggregatorView-104"><a href="#AggregatorView-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">command</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">yview</span><span class="p">)</span>
</span><span id="AggregatorView-105"><a href="#AggregatorView-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">default_auto_scroll</span>
</span><span id="AggregatorView-106"><a href="#AggregatorView-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yscroll</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-107"><a href="#AggregatorView-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_lines_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-108"><a href="#AggregatorView-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yview</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-109"><a href="#AggregatorView-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView-110"><a href="#AggregatorView-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView-111"><a href="#AggregatorView-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-112"><a href="#AggregatorView-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-113"><a href="#AggregatorView-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-114"><a href="#AggregatorView-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-115"><a href="#AggregatorView-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-116"><a href="#AggregatorView-116"><span class="linenos">116</span></a>        
</span><span id="AggregatorView-117"><a href="#AggregatorView-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-3&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b3_down</span><span class="p">)</span>
</span><span id="AggregatorView-118"><a href="#AggregatorView-118"><span class="linenos">118</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView-119"><a href="#AggregatorView-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;&lt;Selection&gt;&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_changed</span><span class="p">)</span>
</span><span id="AggregatorView-120"><a href="#AggregatorView-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Double-Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_double</span><span class="p">)</span>
</span><span id="AggregatorView-121"><a href="#AggregatorView-121"><span class="linenos">121</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_down</span><span class="p">)</span>
</span><span id="AggregatorView-122"><a href="#AggregatorView-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;B1-Motion&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_motion</span><span class="p">)</span>
</span><span id="AggregatorView-123"><a href="#AggregatorView-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;ButtonRelease-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_up</span><span class="p">)</span>
</span><span id="AggregatorView-124"><a href="#AggregatorView-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Control-a&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ctrl_a</span><span class="p">)</span>
</span><span id="AggregatorView-125"><a href="#AggregatorView-125"><span class="linenos">125</span></a>
</span><span id="AggregatorView-126"><a href="#AggregatorView-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">ctrl_a</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-127"><a href="#AggregatorView-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="AggregatorView-128"><a href="#AggregatorView-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
</span><span id="AggregatorView-129"><a href="#AggregatorView-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="s1">&#39;end&#39;</span>
</span><span id="AggregatorView-130"><a href="#AggregatorView-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-131"><a href="#AggregatorView-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-132"><a href="#AggregatorView-132"><span class="linenos">132</span></a>        
</span><span id="AggregatorView-133"><a href="#AggregatorView-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-134"><a href="#AggregatorView-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-135"><a href="#AggregatorView-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView-136"><a href="#AggregatorView-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-137"><a href="#AggregatorView-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="AggregatorView-138"><a href="#AggregatorView-138"><span class="linenos">138</span></a>
</span><span id="AggregatorView-139"><a href="#AggregatorView-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">clear_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView-140"><a href="#AggregatorView-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-141"><a href="#AggregatorView-141"><span class="linenos">141</span></a>    
</span><span id="AggregatorView-142"><a href="#AggregatorView-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="nf">normalize_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView-143"><a href="#AggregatorView-143"><span class="linenos">143</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-144"><a href="#AggregatorView-144"><span class="linenos">144</span></a>            <span class="k">if</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="AggregatorView-145"><a href="#AggregatorView-145"><span class="linenos">145</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="AggregatorView-146"><a href="#AggregatorView-146"><span class="linenos">146</span></a>            <span class="k">elif</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="AggregatorView-147"><a href="#AggregatorView-147"><span class="linenos">147</span></a>                <span class="k">pass</span>
</span><span id="AggregatorView-148"><a href="#AggregatorView-148"><span class="linenos">148</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-149"><a href="#AggregatorView-149"><span class="linenos">149</span></a>                <span class="n">sel_left</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="AggregatorView-150"><a href="#AggregatorView-150"><span class="linenos">150</span></a>                <span class="n">sel_right</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="AggregatorView-151"><a href="#AggregatorView-151"><span class="linenos">151</span></a>                <span class="k">if</span> <span class="n">sel_left</span> <span class="o">&gt;</span> <span class="n">sel_right</span><span class="p">:</span>
</span><span id="AggregatorView-152"><a href="#AggregatorView-152"><span class="linenos">152</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="AggregatorView-153"><a href="#AggregatorView-153"><span class="linenos">153</span></a>    
</span><span id="AggregatorView-154"><a href="#AggregatorView-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">apply_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView-155"><a href="#AggregatorView-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-156"><a href="#AggregatorView-156"><span class="linenos">156</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="AggregatorView-157"><a href="#AggregatorView-157"><span class="linenos">157</span></a>                <span class="k">return</span>
</span><span id="AggregatorView-158"><a href="#AggregatorView-158"><span class="linenos">158</span></a>            
</span><span id="AggregatorView-159"><a href="#AggregatorView-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="AggregatorView-160"><a href="#AggregatorView-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-161"><a href="#AggregatorView-161"><span class="linenos">161</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">)</span>
</span><span id="AggregatorView-162"><a href="#AggregatorView-162"><span class="linenos">162</span></a>
</span><span id="AggregatorView-163"><a href="#AggregatorView-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-164"><a href="#AggregatorView-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-165"><a href="#AggregatorView-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-166"><a href="#AggregatorView-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-167"><a href="#AggregatorView-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="AggregatorView-168"><a href="#AggregatorView-168"><span class="linenos">168</span></a>
</span><span id="AggregatorView-169"><a href="#AggregatorView-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_up</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-170"><a href="#AggregatorView-170"><span class="linenos">170</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-171"><a href="#AggregatorView-171"><span class="linenos">171</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-172"><a href="#AggregatorView-172"><span class="linenos">172</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-173"><a href="#AggregatorView-173"><span class="linenos">173</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">!=</span> <span class="n">selection_last</span><span class="p">:</span>
</span><span id="AggregatorView-174"><a href="#AggregatorView-174"><span class="linenos">174</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-175"><a href="#AggregatorView-175"><span class="linenos">175</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-176"><a href="#AggregatorView-176"><span class="linenos">176</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-177"><a href="#AggregatorView-177"><span class="linenos">177</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-178"><a href="#AggregatorView-178"><span class="linenos">178</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-179"><a href="#AggregatorView-179"><span class="linenos">179</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-180"><a href="#AggregatorView-180"><span class="linenos">180</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-181"><a href="#AggregatorView-181"><span class="linenos">181</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-182"><a href="#AggregatorView-182"><span class="linenos">182</span></a>        
</span><span id="AggregatorView-183"><a href="#AggregatorView-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-184"><a href="#AggregatorView-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-185"><a href="#AggregatorView-185"><span class="linenos">185</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView-186"><a href="#AggregatorView-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-187"><a href="#AggregatorView-187"><span class="linenos">187</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="AggregatorView-188"><a href="#AggregatorView-188"><span class="linenos">188</span></a>
</span><span id="AggregatorView-189"><a href="#AggregatorView-189"><span class="linenos">189</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_motion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-190"><a href="#AggregatorView-190"><span class="linenos">190</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-191"><a href="#AggregatorView-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-192"><a href="#AggregatorView-192"><span class="linenos">192</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-193"><a href="#AggregatorView-193"><span class="linenos">193</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-194"><a href="#AggregatorView-194"><span class="linenos">194</span></a>        
</span><span id="AggregatorView-195"><a href="#AggregatorView-195"><span class="linenos">195</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="AggregatorView-196"><a href="#AggregatorView-196"><span class="linenos">196</span></a>    
</span><span id="AggregatorView-197"><a href="#AggregatorView-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_double</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-198"><a href="#AggregatorView-198"><span class="linenos">198</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span><span class="p">:</span>
</span><span id="AggregatorView-199"><a href="#AggregatorView-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> linestart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-200"><a href="#AggregatorView-200"><span class="linenos">200</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> lineend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-201"><a href="#AggregatorView-201"><span class="linenos">201</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-202"><a href="#AggregatorView-202"><span class="linenos">202</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-203"><a href="#AggregatorView-203"><span class="linenos">203</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-204"><a href="#AggregatorView-204"><span class="linenos">204</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-205"><a href="#AggregatorView-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordstart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-206"><a href="#AggregatorView-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView-207"><a href="#AggregatorView-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-208"><a href="#AggregatorView-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-209"><a href="#AggregatorView-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorView-210"><a href="#AggregatorView-210"><span class="linenos">210</span></a>        
</span><span id="AggregatorView-211"><a href="#AggregatorView-211"><span class="linenos">211</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span><span id="AggregatorView-212"><a href="#AggregatorView-212"><span class="linenos">212</span></a>
</span><span id="AggregatorView-213"><a href="#AggregatorView-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="nf">mouse_b3_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-214"><a href="#AggregatorView-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView-215"><a href="#AggregatorView-215"><span class="linenos">215</span></a>        <span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-216"><a href="#AggregatorView-216"><span class="linenos">216</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-217"><a href="#AggregatorView-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="AggregatorView-218"><a href="#AggregatorView-218"><span class="linenos">218</span></a>            <span class="n">selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span>
</span><span id="AggregatorView-219"><a href="#AggregatorView-219"><span class="linenos">219</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-220"><a href="#AggregatorView-220"><span class="linenos">220</span></a>            <span class="n">current_selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">)</span>
</span><span id="AggregatorView-221"><a href="#AggregatorView-221"><span class="linenos">221</span></a>            <span class="n">current_selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_FIRST</span><span class="p">)</span>
</span><span id="AggregatorView-222"><a href="#AggregatorView-222"><span class="linenos">222</span></a>            <span class="n">current_selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_LAST</span><span class="p">)</span>
</span><span id="AggregatorView-223"><a href="#AggregatorView-223"><span class="linenos">223</span></a>            <span class="k">if</span> <span class="n">current_selection_first</span> <span class="ow">and</span> <span class="n">current_selection_last</span><span class="p">:</span>
</span><span id="AggregatorView-224"><a href="#AggregatorView-224"><span class="linenos">224</span></a>                <span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_selection_first</span><span class="p">,</span> <span class="n">current_selection_last</span><span class="p">)</span>
</span><span id="AggregatorView-225"><a href="#AggregatorView-225"><span class="linenos">225</span></a>
</span><span id="AggregatorView-226"><a href="#AggregatorView-226"><span class="linenos">226</span></a>        <span class="k">if</span> <span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView-227"><a href="#AggregatorView-227"><span class="linenos">227</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_clear</span><span class="p">()</span>
</span><span id="AggregatorView-228"><a href="#AggregatorView-228"><span class="linenos">228</span></a>            <span class="n">text_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="AggregatorView-229"><a href="#AggregatorView-229"><span class="linenos">229</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_append</span><span class="p">(</span><span class="n">text_content</span><span class="p">)</span>
</span><span id="AggregatorView-230"><a href="#AggregatorView-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-231"><a href="#AggregatorView-231"><span class="linenos">231</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView-232"><a href="#AggregatorView-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-233"><a href="#AggregatorView-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="AggregatorView-234"><a href="#AggregatorView-234"><span class="linenos">234</span></a>    
</span><span id="AggregatorView-235"><a href="#AggregatorView-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="nf">selection_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView-236"><a href="#AggregatorView-236"><span class="linenos">236</span></a>        <span class="k">return</span>
</span><span id="AggregatorView-237"><a href="#AggregatorView-237"><span class="linenos">237</span></a>
</span><span id="AggregatorView-238"><a href="#AggregatorView-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="AggregatorView-239"><a href="#AggregatorView-239"><span class="linenos">239</span></a>        <span class="n">lines_num_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="AggregatorView-240"><a href="#AggregatorView-240"><span class="linenos">240</span></a>        <span class="n">view_fractions_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="AggregatorView-241"><a href="#AggregatorView-241"><span class="linenos">241</span></a>        <span class="n">line_before</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_before</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_before</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="AggregatorView-242"><a href="#AggregatorView-242"><span class="linenos">242</span></a>        <span class="n">tag_insert_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView-243"><a href="#AggregatorView-243"><span class="linenos">243</span></a>        <span class="n">tag_current_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">)</span>
</span><span id="AggregatorView-244"><a href="#AggregatorView-244"><span class="linenos">244</span></a>        
</span><span id="AggregatorView-245"><a href="#AggregatorView-245"><span class="linenos">245</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView-246"><a href="#AggregatorView-246"><span class="linenos">246</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_context</span><span class="p">()</span>
</span><span id="AggregatorView-247"><a href="#AggregatorView-247"><span class="linenos">247</span></a>        
</span><span id="AggregatorView-248"><a href="#AggregatorView-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
</span><span id="AggregatorView-249"><a href="#AggregatorView-249"><span class="linenos">249</span></a>        
</span><span id="AggregatorView-250"><a href="#AggregatorView-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="AggregatorView-251"><a href="#AggregatorView-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="n">ttkb__END</span><span class="p">)</span>
</span><span id="AggregatorView-252"><a href="#AggregatorView-252"><span class="linenos">252</span></a>
</span><span id="AggregatorView-253"><a href="#AggregatorView-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView-254"><a href="#AggregatorView-254"><span class="linenos">254</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-255"><a href="#AggregatorView-255"><span class="linenos">255</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="AggregatorView-256"><a href="#AggregatorView-256"><span class="linenos">256</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-257"><a href="#AggregatorView-257"><span class="linenos">257</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="n">tag_current_before</span><span class="p">)</span>
</span><span id="AggregatorView-258"><a href="#AggregatorView-258"><span class="linenos">258</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView-259"><a href="#AggregatorView-259"><span class="linenos">259</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="AggregatorView-260"><a href="#AggregatorView-260"><span class="linenos">260</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView-261"><a href="#AggregatorView-261"><span class="linenos">261</span></a>            
</span><span id="AggregatorView-262"><a href="#AggregatorView-262"><span class="linenos">262</span></a>            <span class="n">lines_num_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="AggregatorView-263"><a href="#AggregatorView-263"><span class="linenos">263</span></a>            <span class="n">view_fractions_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="AggregatorView-264"><a href="#AggregatorView-264"><span class="linenos">264</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_after</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_after</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="AggregatorView-265"><a href="#AggregatorView-265"><span class="linenos">265</span></a>            
</span><span id="AggregatorView-266"><a href="#AggregatorView-266"><span class="linenos">266</span></a>            <span class="n">line_before</span> <span class="o">=</span> <span class="n">line_before</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="AggregatorView-267"><a href="#AggregatorView-267"><span class="linenos">267</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="n">line_after</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="AggregatorView-268"><a href="#AggregatorView-268"><span class="linenos">268</span></a>            <span class="k">if</span> <span class="n">line_after</span> <span class="o">!=</span> <span class="n">line_before</span><span class="p">:</span>
</span><span id="AggregatorView-269"><a href="#AggregatorView-269"><span class="linenos">269</span></a>                <span class="n">movement</span> <span class="o">=</span> <span class="n">line_before</span> <span class="o">-</span> <span class="n">line_after</span>
</span><span id="AggregatorView-270"><a href="#AggregatorView-270"><span class="linenos">270</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview_scroll</span><span class="p">(</span><span class="n">movement</span><span class="p">,</span> <span class="s1">&#39;units&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-271"><a href="#AggregatorView-271"><span class="linenos">271</span></a>    
</span><span id="AggregatorView-272"><a href="#AggregatorView-272"><span class="linenos">272</span></a>    <span class="k">def</span> <span class="nf">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="AggregatorView-273"><a href="#AggregatorView-273"><span class="linenos">273</span></a>        <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="AggregatorView-274"><a href="#AggregatorView-274"><span class="linenos">274</span></a>
</span><span id="AggregatorView-275"><a href="#AggregatorView-275"><span class="linenos">275</span></a>    <span class="k">def</span> <span class="nf">clear_context</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView-276"><a href="#AggregatorView-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView-277"><a href="#AggregatorView-277"><span class="linenos">277</span></a>
</span><span id="AggregatorView-278"><a href="#AggregatorView-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="nf">yscroll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="AggregatorView-279"><a href="#AggregatorView-279"><span class="linenos">279</span></a>        <span class="n">first</span><span class="p">,</span> <span class="n">last</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="AggregatorView-280"><a href="#AggregatorView-280"><span class="linenos">280</span></a>        <span class="n">lines_num</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView-281"><a href="#AggregatorView-281"><span class="linenos">281</span></a>        <span class="n">last_line_index</span> <span class="o">=</span> <span class="n">lines_num</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView-282"><a href="#AggregatorView-282"><span class="linenos">282</span></a>        <span class="n">first_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">first</span><span class="p">)))</span>
</span><span id="AggregatorView-283"><a href="#AggregatorView-283"><span class="linenos">283</span></a>        <span class="n">last_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">last</span><span class="p">)))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView-284"><a href="#AggregatorView-284"><span class="linenos">284</span></a>
</span><span id="AggregatorView-285"><a href="#AggregatorView-285"><span class="linenos">285</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="AggregatorView-286"><a href="#AggregatorView-286"><span class="linenos">286</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&lt;</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="AggregatorView-287"><a href="#AggregatorView-287"><span class="linenos">287</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView-288"><a href="#AggregatorView-288"><span class="linenos">288</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-289"><a href="#AggregatorView-289"><span class="linenos">289</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&gt;=</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">==</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="AggregatorView-290"><a href="#AggregatorView-290"><span class="linenos">290</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorView-291"><a href="#AggregatorView-291"><span class="linenos">291</span></a>        
</span><span id="AggregatorView-292"><a href="#AggregatorView-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="AggregatorView-293"><a href="#AggregatorView-293"><span class="linenos">293</span></a>
</span><span id="AggregatorView-294"><a href="#AggregatorView-294"><span class="linenos">294</span></a>    <span class="k">def</span> <span class="nf">yview</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="AggregatorView-295"><a href="#AggregatorView-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span><span id="AggregatorView-296"><a href="#AggregatorView-296"><span class="linenos">296</span></a>    
</span><span id="AggregatorView-297"><a href="#AggregatorView-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wr</span><span class="p">:</span> <span class="n">TkObjWrapper</span><span class="p">):</span>
</span><span id="AggregatorView-298"><a href="#AggregatorView-298"><span class="linenos">298</span></a>        <span class="n">wr</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_updater</span><span class="p">)</span>
</span><span id="AggregatorView-299"><a href="#AggregatorView-299"><span class="linenos">299</span></a>    
</span><span id="AggregatorView-300"><a href="#AggregatorView-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView-301"><a href="#AggregatorView-301"><span class="linenos">301</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorView-302"><a href="#AggregatorView-302"><span class="linenos">302</span></a>    
</span><span id="AggregatorView-303"><a href="#AggregatorView-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">_updater</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="AggregatorView-304"><a href="#AggregatorView-304"><span class="linenos">304</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span><span class="p">:</span>
</span><span id="AggregatorView-305"><a href="#AggregatorView-305"><span class="linenos">305</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="AggregatorView-306"><a href="#AggregatorView-306"><span class="linenos">306</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="AggregatorView-307"><a href="#AggregatorView-307"><span class="linenos">307</span></a>                <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">max_len</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_len</span><span class="p">):</span>
</span><span id="AggregatorView-308"><a href="#AggregatorView-308"><span class="linenos">308</span></a>                    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">,</span> <span class="n">AggregatorAppendFormatter</span><span class="p">):</span>
</span><span id="AggregatorView-309"><a href="#AggregatorView-309"><span class="linenos">309</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="AggregatorView-310"><a href="#AggregatorView-310"><span class="linenos">310</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
</span><span id="AggregatorView-311"><a href="#AggregatorView-311"><span class="linenos">311</span></a>                        <span class="n">auto_scroll_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span>
</span><span id="AggregatorView-312"><a href="#AggregatorView-312"><span class="linenos">312</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">clear_context</span><span class="p">()</span>
</span><span id="AggregatorView-313"><a href="#AggregatorView-313"><span class="linenos">313</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="n">auto_scroll_buff</span>
</span><span id="AggregatorView-314"><a href="#AggregatorView-314"><span class="linenos">314</span></a>                    
</span><span id="AggregatorView-315"><a href="#AggregatorView-315"><span class="linenos">315</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">FastAggregator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">aggregator_key</span><span class="p">)</span>
</span><span id="AggregatorView-316"><a href="#AggregatorView-316"><span class="linenos">316</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView-317"><a href="#AggregatorView-317"><span class="linenos">317</span></a>                    <span class="n">text</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">data</span><span class="p">])</span> <span class="o">+</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="AggregatorView-318"><a href="#AggregatorView-318"><span class="linenos">318</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView-319"><a href="#AggregatorView-319"><span class="linenos">319</span></a>                    <span class="n">text</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</span><span id="AggregatorView-320"><a href="#AggregatorView-320"><span class="linenos">320</span></a>                    
</span><span id="AggregatorView-321"><a href="#AggregatorView-321"><span class="linenos">321</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</span><span id="AggregatorView-322"><a href="#AggregatorView-322"><span class="linenos">322</span></a>            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="AggregatorView-323"><a href="#AggregatorView-323"><span class="linenos">323</span></a>                <span class="k">pass</span>
</span><span id="AggregatorView-324"><a href="#AggregatorView-324"><span class="linenos">324</span></a>
</span><span id="AggregatorView-325"><a href="#AggregatorView-325"><span class="linenos">325</span></a>            <span class="n">i</span><span class="p">(</span><span class="n">Sleep</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">updating_interval</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Ttk Frame widget is a container, used to group other widgets
together.</p>
</div>


                            <div id="AggregatorView.__init__" class="classattr">
                                        <input id="AggregatorView.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">AggregatorView</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">default_auto_scroll</span><span class="p">:</span> <span class="nb">bool</span>,</span><span class="param">	<span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">width</span>,</span><span class="param">	<span class="n">height</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="AggregatorView.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.__init__-73"><a href="#AggregatorView.__init__-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">default_auto_scroll</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">],</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="AggregatorView.__init__-74"><a href="#AggregatorView.__init__-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">append_data</span>
</span><span id="AggregatorView.__init__-75"><a href="#AggregatorView.__init__-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updating_interval</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="n">updating_interval</span>
</span><span id="AggregatorView.__init__-76"><a href="#AggregatorView.__init__-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">aggregator_key</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">aggregator_key</span>
</span><span id="AggregatorView.__init__-77"><a href="#AggregatorView.__init__-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="AggregatorView.__init__-78"><a href="#AggregatorView.__init__-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data_formatter_func</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_formatter_func</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_data_formatter_func</span>
</span><span id="AggregatorView.__init__-79"><a href="#AggregatorView.__init__-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.__init__-80"><a href="#AggregatorView.__init__-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">updates_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView.__init__-81"><a href="#AggregatorView.__init__-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_len</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-82"><a href="#AggregatorView.__init__-82"><span class="linenos"> 82</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-83"><a href="#AggregatorView.__init__-83"><span class="linenos"> 83</span></a>
</span><span id="AggregatorView.__init__-84"><a href="#AggregatorView.__init__-84"><span class="linenos"> 84</span></a>        <span class="n">text_area_config</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="AggregatorView.__init__-85"><a href="#AggregatorView.__init__-85"><span class="linenos"> 85</span></a>            <span class="s1">&#39;highlightcolor&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">primary</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-86"><a href="#AggregatorView.__init__-86"><span class="linenos"> 86</span></a>            <span class="s1">&#39;highlightbackground&#39;</span><span class="p">:</span> <span class="n">Style</span><span class="o">.</span><span class="n">instance</span><span class="o">.</span><span class="n">colors</span><span class="o">.</span><span class="n">border</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-87"><a href="#AggregatorView.__init__-87"><span class="linenos"> 87</span></a>            <span class="s1">&#39;highlightthickness&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-88"><a href="#AggregatorView.__init__-88"><span class="linenos"> 88</span></a>            <span class="s1">&#39;wrap&#39;</span><span class="p">:</span> <span class="s1">&#39;none&#39;</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-89"><a href="#AggregatorView.__init__-89"><span class="linenos"> 89</span></a>        <span class="p">}</span>
</span><span id="AggregatorView.__init__-90"><a href="#AggregatorView.__init__-90"><span class="linenos"> 90</span></a>        <span class="k">if</span> <span class="n">width</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.__init__-91"><a href="#AggregatorView.__init__-91"><span class="linenos"> 91</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="AggregatorView.__init__-92"><a href="#AggregatorView.__init__-92"><span class="linenos"> 92</span></a>                <span class="s1">&#39;width&#39;</span><span class="p">:</span> <span class="n">width</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-93"><a href="#AggregatorView.__init__-93"><span class="linenos"> 93</span></a>            <span class="p">})</span>
</span><span id="AggregatorView.__init__-94"><a href="#AggregatorView.__init__-94"><span class="linenos"> 94</span></a>        
</span><span id="AggregatorView.__init__-95"><a href="#AggregatorView.__init__-95"><span class="linenos"> 95</span></a>        <span class="k">if</span> <span class="n">height</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.__init__-96"><a href="#AggregatorView.__init__-96"><span class="linenos"> 96</span></a>            <span class="n">text_area_config</span><span class="o">.</span><span class="n">update</span><span class="p">({</span>
</span><span id="AggregatorView.__init__-97"><a href="#AggregatorView.__init__-97"><span class="linenos"> 97</span></a>                <span class="s1">&#39;height&#39;</span><span class="p">:</span> <span class="n">height</span><span class="p">,</span>
</span><span id="AggregatorView.__init__-98"><a href="#AggregatorView.__init__-98"><span class="linenos"> 98</span></a>            <span class="p">})</span>
</span><span id="AggregatorView.__init__-99"><a href="#AggregatorView.__init__-99"><span class="linenos"> 99</span></a>        
</span><span id="AggregatorView.__init__-100"><a href="#AggregatorView.__init__-100"><span class="linenos">100</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span> <span class="o">=</span> <span class="n">ReadOnlyText</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">text_area_config</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-101"><a href="#AggregatorView.__init__-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s1">&#39;both&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="s1">&#39;yes&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-102"><a href="#AggregatorView.__init__-102"><span class="linenos">102</span></a>
</span><span id="AggregatorView.__init__-103"><a href="#AggregatorView.__init__-103"><span class="linenos">103</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="p">[</span><span class="s1">&#39;yscrollcommand&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">yscroll</span>
</span><span id="AggregatorView.__init__-104"><a href="#AggregatorView.__init__-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">config</span><span class="p">(</span><span class="n">command</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">yview</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-105"><a href="#AggregatorView.__init__-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">default_auto_scroll</span>
</span><span id="AggregatorView.__init__-106"><a href="#AggregatorView.__init__-106"><span class="linenos">106</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yscroll</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-107"><a href="#AggregatorView.__init__-107"><span class="linenos">107</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_lines_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-108"><a href="#AggregatorView.__init__-108"><span class="linenos">108</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_yview</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-109"><a href="#AggregatorView.__init__-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView.__init__-110"><a href="#AggregatorView.__init__-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">desired_line</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="AggregatorView.__init__-111"><a href="#AggregatorView.__init__-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_started</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.__init__-112"><a href="#AggregatorView.__init__-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-113"><a href="#AggregatorView.__init__-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-114"><a href="#AggregatorView.__init__-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.__init__-115"><a href="#AggregatorView.__init__-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.__init__-116"><a href="#AggregatorView.__init__-116"><span class="linenos">116</span></a>        
</span><span id="AggregatorView.__init__-117"><a href="#AggregatorView.__init__-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-3&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b3_down</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-118"><a href="#AggregatorView.__init__-118"><span class="linenos">118</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView.__init__-119"><a href="#AggregatorView.__init__-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;&lt;Selection&gt;&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_changed</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-120"><a href="#AggregatorView.__init__-120"><span class="linenos">120</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Double-Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_double</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-121"><a href="#AggregatorView.__init__-121"><span class="linenos">121</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Button-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_down</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-122"><a href="#AggregatorView.__init__-122"><span class="linenos">122</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;B1-Motion&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_motion</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-123"><a href="#AggregatorView.__init__-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;ButtonRelease-1&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mouse_b1_up</span><span class="p">)</span>
</span><span id="AggregatorView.__init__-124"><a href="#AggregatorView.__init__-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="s2">&quot;&lt;Control-a&gt;&quot;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">ctrl_a</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Constructs a Ttk Widget with the parent master.</p>

<p>STANDARD OPTIONS</p>

<pre><code>class, cursor, takefocus, style
</code></pre>

<p>SCROLLABLE WIDGET OPTIONS</p>

<pre><code>xscrollcommand, yscrollcommand
</code></pre>

<p>LABEL WIDGET OPTIONS</p>

<pre><code>text, textvariable, underline, image, compound, width
</code></pre>

<p>WIDGET STATES</p>

<pre><code>active, disabled, focus, pressed, selected, background,
readonly, alternate, invalid
</code></pre>
</div>


                            </div>
                            <div id="AggregatorView.append_data" class="classattr">
                                <div class="attr variable">
            <span class="name">append_data</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.append_data"></a>
    
    

                            </div>
                            <div id="AggregatorView.updating_interval" class="classattr">
                                <div class="attr variable">
            <span class="name">updating_interval</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.updating_interval"></a>
    
    

                            </div>
                            <div id="AggregatorView.aggregator_key" class="classattr">
                                <div class="attr variable">
            <span class="name">aggregator_key</span><span class="annotation">: Hashable</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.aggregator_key"></a>
    
    

                            </div>
                            <div id="AggregatorView.data_formatter_func" class="classattr">
                                <div class="attr variable">
            <span class="name">data_formatter_func</span><span class="annotation">: Union[Callable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.data_formatter_func"></a>
    
    

                            </div>
                            <div id="AggregatorView.updates_num" class="classattr">
                                <div class="attr variable">
            <span class="name">updates_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.updates_num"></a>
    
    

                            </div>
                            <div id="AggregatorView.max_len" class="classattr">
                                <div class="attr variable">
            <span class="name">max_len</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.max_len"></a>
    
    

                            </div>
                            <div id="AggregatorView.text_area" class="classattr">
                                <div class="attr variable">
            <span class="name">text_area</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.text_area"></a>
    
    

                            </div>
                            <div id="AggregatorView.auto_scroll" class="classattr">
                                <div class="attr variable">
            <span class="name">auto_scroll</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.auto_scroll"></a>
    
    

                            </div>
                            <div id="AggregatorView.last_yscroll" class="classattr">
                                <div class="attr variable">
            <span class="name">last_yscroll</span><span class="annotation">: Tuple[str, str]</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.last_yscroll"></a>
    
    

                            </div>
                            <div id="AggregatorView.last_lines_num" class="classattr">
                                <div class="attr variable">
            <span class="name">last_lines_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.last_lines_num"></a>
    
    

                            </div>
                            <div id="AggregatorView.last_yview" class="classattr">
                                <div class="attr variable">
            <span class="name">last_yview</span><span class="annotation">: Tuple[str]</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.last_yview"></a>
    
    

                            </div>
                            <div id="AggregatorView.last_line" class="classattr">
                                <div class="attr variable">
            <span class="name">last_line</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.last_line"></a>
    
    

                            </div>
                            <div id="AggregatorView.desired_line" class="classattr">
                                <div class="attr variable">
            <span class="name">desired_line</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.desired_line"></a>
    
    

                            </div>
                            <div id="AggregatorView.selection_started" class="classattr">
                                <div class="attr variable">
            <span class="name">selection_started</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.selection_started"></a>
    
    

                            </div>
                            <div id="AggregatorView.selection_first" class="classattr">
                                <div class="attr variable">
            <span class="name">selection_first</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.selection_first"></a>
    
    

                            </div>
                            <div id="AggregatorView.selection_last" class="classattr">
                                <div class="attr variable">
            <span class="name">selection_last</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.selection_last"></a>
    
    

                            </div>
                            <div id="AggregatorView.selection" class="classattr">
                                <div class="attr variable">
            <span class="name">selection</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.selection"></a>
    
    

                            </div>
                            <div id="AggregatorView.previously_was_mouse_b1_double" class="classattr">
                                <div class="attr variable">
            <span class="name">previously_was_mouse_b1_double</span>

        
    </div>
    <a class="headerlink" href="#AggregatorView.previously_was_mouse_b1_double"></a>
    
    

                            </div>
                            <div id="AggregatorView.ctrl_a" class="classattr">
                                        <input id="AggregatorView.ctrl_a-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ctrl_a</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.ctrl_a-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.ctrl_a"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.ctrl_a-126"><a href="#AggregatorView.ctrl_a-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">ctrl_a</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.ctrl_a-127"><a href="#AggregatorView.ctrl_a-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span><span id="AggregatorView.ctrl_a-128"><a href="#AggregatorView.ctrl_a-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
</span><span id="AggregatorView.ctrl_a-129"><a href="#AggregatorView.ctrl_a-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="s1">&#39;end&#39;</span>
</span><span id="AggregatorView.ctrl_a-130"><a href="#AggregatorView.ctrl_a-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.ctrl_a-131"><a href="#AggregatorView.ctrl_a-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.ctrl_a-132"><a href="#AggregatorView.ctrl_a-132"><span class="linenos">132</span></a>        
</span><span id="AggregatorView.ctrl_a-133"><a href="#AggregatorView.ctrl_a-133"><span class="linenos">133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.ctrl_a-134"><a href="#AggregatorView.ctrl_a-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.ctrl_a-135"><a href="#AggregatorView.ctrl_a-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView.ctrl_a-136"><a href="#AggregatorView.ctrl_a-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.ctrl_a-137"><a href="#AggregatorView.ctrl_a-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.clear_selection" class="classattr">
                                        <input id="AggregatorView.clear_selection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear_selection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.clear_selection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.clear_selection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.clear_selection-139"><a href="#AggregatorView.clear_selection-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">clear_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView.clear_selection-140"><a href="#AggregatorView.clear_selection-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.normalize_selection" class="classattr">
                                        <input id="AggregatorView.normalize_selection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">normalize_selection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.normalize_selection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.normalize_selection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.normalize_selection-142"><a href="#AggregatorView.normalize_selection-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="nf">normalize_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView.normalize_selection-143"><a href="#AggregatorView.normalize_selection-143"><span class="linenos">143</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.normalize_selection-144"><a href="#AggregatorView.normalize_selection-144"><span class="linenos">144</span></a>            <span class="k">if</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="AggregatorView.normalize_selection-145"><a href="#AggregatorView.normalize_selection-145"><span class="linenos">145</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="AggregatorView.normalize_selection-146"><a href="#AggregatorView.normalize_selection-146"><span class="linenos">146</span></a>            <span class="k">elif</span> <span class="s1">&#39;end&#39;</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="AggregatorView.normalize_selection-147"><a href="#AggregatorView.normalize_selection-147"><span class="linenos">147</span></a>                <span class="k">pass</span>
</span><span id="AggregatorView.normalize_selection-148"><a href="#AggregatorView.normalize_selection-148"><span class="linenos">148</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.normalize_selection-149"><a href="#AggregatorView.normalize_selection-149"><span class="linenos">149</span></a>                <span class="n">sel_left</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="AggregatorView.normalize_selection-150"><a href="#AggregatorView.normalize_selection-150"><span class="linenos">150</span></a>                <span class="n">sel_right</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)]</span>
</span><span id="AggregatorView.normalize_selection-151"><a href="#AggregatorView.normalize_selection-151"><span class="linenos">151</span></a>                <span class="k">if</span> <span class="n">sel_left</span> <span class="o">&gt;</span> <span class="n">sel_right</span><span class="p">:</span>
</span><span id="AggregatorView.normalize_selection-152"><a href="#AggregatorView.normalize_selection-152"><span class="linenos">152</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.apply_selection" class="classattr">
                                        <input id="AggregatorView.apply_selection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">apply_selection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.apply_selection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.apply_selection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.apply_selection-154"><a href="#AggregatorView.apply_selection-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">apply_selection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView.apply_selection-155"><a href="#AggregatorView.apply_selection-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.apply_selection-156"><a href="#AggregatorView.apply_selection-156"><span class="linenos">156</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
</span><span id="AggregatorView.apply_selection-157"><a href="#AggregatorView.apply_selection-157"><span class="linenos">157</span></a>                <span class="k">return</span>
</span><span id="AggregatorView.apply_selection-158"><a href="#AggregatorView.apply_selection-158"><span class="linenos">158</span></a>            
</span><span id="AggregatorView.apply_selection-159"><a href="#AggregatorView.apply_selection-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="AggregatorView.apply_selection-160"><a href="#AggregatorView.apply_selection-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.apply_selection-161"><a href="#AggregatorView.apply_selection-161"><span class="linenos">161</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">,</span> <span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">selection</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.mouse_b1_down" class="classattr">
                                        <input id="AggregatorView.mouse_b1_down-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mouse_b1_down</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.mouse_b1_down-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.mouse_b1_down"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.mouse_b1_down-163"><a href="#AggregatorView.mouse_b1_down-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.mouse_b1_down-164"><a href="#AggregatorView.mouse_b1_down-164"><span class="linenos">164</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.mouse_b1_down-165"><a href="#AggregatorView.mouse_b1_down-165"><span class="linenos">165</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_down-166"><a href="#AggregatorView.mouse_b1_down-166"><span class="linenos">166</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b1_down-167"><a href="#AggregatorView.mouse_b1_down-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.mouse_b1_up" class="classattr">
                                        <input id="AggregatorView.mouse_b1_up-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mouse_b1_up</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.mouse_b1_up-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.mouse_b1_up"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.mouse_b1_up-169"><a href="#AggregatorView.mouse_b1_up-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_up</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.mouse_b1_up-170"><a href="#AggregatorView.mouse_b1_up-170"><span class="linenos">170</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_up-171"><a href="#AggregatorView.mouse_b1_up-171"><span class="linenos">171</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_up-172"><a href="#AggregatorView.mouse_b1_up-172"><span class="linenos">172</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_up-173"><a href="#AggregatorView.mouse_b1_up-173"><span class="linenos">173</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">!=</span> <span class="n">selection_last</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_up-174"><a href="#AggregatorView.mouse_b1_up-174"><span class="linenos">174</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-175"><a href="#AggregatorView.mouse_b1_up-175"><span class="linenos">175</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b1_up-176"><a href="#AggregatorView.mouse_b1_up-176"><span class="linenos">176</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b1_up-177"><a href="#AggregatorView.mouse_b1_up-177"><span class="linenos">177</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_up-178"><a href="#AggregatorView.mouse_b1_up-178"><span class="linenos">178</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b1_up-179"><a href="#AggregatorView.mouse_b1_up-179"><span class="linenos">179</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_up-180"><a href="#AggregatorView.mouse_b1_up-180"><span class="linenos">180</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-181"><a href="#AggregatorView.mouse_b1_up-181"><span class="linenos">181</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b1_up-182"><a href="#AggregatorView.mouse_b1_up-182"><span class="linenos">182</span></a>        
</span><span id="AggregatorView.mouse_b1_up-183"><a href="#AggregatorView.mouse_b1_up-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-184"><a href="#AggregatorView.mouse_b1_up-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-185"><a href="#AggregatorView.mouse_b1_up-185"><span class="linenos">185</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-186"><a href="#AggregatorView.mouse_b1_up-186"><span class="linenos">186</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_up-187"><a href="#AggregatorView.mouse_b1_up-187"><span class="linenos">187</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.mouse_b1_motion" class="classattr">
                                        <input id="AggregatorView.mouse_b1_motion-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mouse_b1_motion</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.mouse_b1_motion-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.mouse_b1_motion"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.mouse_b1_motion-189"><a href="#AggregatorView.mouse_b1_motion-189"><span class="linenos">189</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_motion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.mouse_b1_motion-190"><a href="#AggregatorView.mouse_b1_motion-190"><span class="linenos">190</span></a>        <span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_motion-191"><a href="#AggregatorView.mouse_b1_motion-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_motion-192"><a href="#AggregatorView.mouse_b1_motion-192"><span class="linenos">192</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_motion-193"><a href="#AggregatorView.mouse_b1_motion-193"><span class="linenos">193</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b1_motion-194"><a href="#AggregatorView.mouse_b1_motion-194"><span class="linenos">194</span></a>        
</span><span id="AggregatorView.mouse_b1_motion-195"><a href="#AggregatorView.mouse_b1_motion-195"><span class="linenos">195</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.mouse_b1_double" class="classattr">
                                        <input id="AggregatorView.mouse_b1_double-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mouse_b1_double</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.mouse_b1_double-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.mouse_b1_double"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.mouse_b1_double-197"><a href="#AggregatorView.mouse_b1_double-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">mouse_b1_double</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.mouse_b1_double-198"><a href="#AggregatorView.mouse_b1_double-198"><span class="linenos">198</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_double-199"><a href="#AggregatorView.mouse_b1_double-199"><span class="linenos">199</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> linestart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_double-200"><a href="#AggregatorView.mouse_b1_double-200"><span class="linenos">200</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> lineend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_double-201"><a href="#AggregatorView.mouse_b1_double-201"><span class="linenos">201</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_double-202"><a href="#AggregatorView.mouse_b1_double-202"><span class="linenos">202</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b1_double-203"><a href="#AggregatorView.mouse_b1_double-203"><span class="linenos">203</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.mouse_b1_double-204"><a href="#AggregatorView.mouse_b1_double-204"><span class="linenos">204</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b1_double-205"><a href="#AggregatorView.mouse_b1_double-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordstart&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_double-206"><a href="#AggregatorView.mouse_b1_double-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;@</span><span class="si">%s</span><span class="s1">,</span><span class="si">%s</span><span class="s1"> wordend&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">))</span>
</span><span id="AggregatorView.mouse_b1_double-207"><a href="#AggregatorView.mouse_b1_double-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">selection_first</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b1_double-208"><a href="#AggregatorView.mouse_b1_double-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b1_double-209"><a href="#AggregatorView.mouse_b1_double-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorView.mouse_b1_double-210"><a href="#AggregatorView.mouse_b1_double-210"><span class="linenos">210</span></a>        
</span><span id="AggregatorView.mouse_b1_double-211"><a href="#AggregatorView.mouse_b1_double-211"><span class="linenos">211</span></a>        <span class="k">return</span> <span class="s1">&#39;break&#39;</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.mouse_b3_down" class="classattr">
                                        <input id="AggregatorView.mouse_b3_down-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mouse_b3_down</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.mouse_b3_down-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.mouse_b3_down"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.mouse_b3_down-213"><a href="#AggregatorView.mouse_b3_down-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="nf">mouse_b3_down</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.mouse_b3_down-214"><a href="#AggregatorView.mouse_b3_down-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-215"><a href="#AggregatorView.mouse_b3_down-215"><span class="linenos">215</span></a>        <span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b3_down-216"><a href="#AggregatorView.mouse_b3_down-216"><span class="linenos">216</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b3_down-217"><a href="#AggregatorView.mouse_b3_down-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">normalize_selection</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b3_down-218"><a href="#AggregatorView.mouse_b3_down-218"><span class="linenos">218</span></a>            <span class="n">selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">selection</span>
</span><span id="AggregatorView.mouse_b3_down-219"><a href="#AggregatorView.mouse_b3_down-219"><span class="linenos">219</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b3_down-220"><a href="#AggregatorView.mouse_b3_down-220"><span class="linenos">220</span></a>            <span class="n">current_selection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-221"><a href="#AggregatorView.mouse_b3_down-221"><span class="linenos">221</span></a>            <span class="n">current_selection_first</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_FIRST</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-222"><a href="#AggregatorView.mouse_b3_down-222"><span class="linenos">222</span></a>            <span class="n">current_selection_last</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__SEL_LAST</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-223"><a href="#AggregatorView.mouse_b3_down-223"><span class="linenos">223</span></a>            <span class="k">if</span> <span class="n">current_selection_first</span> <span class="ow">and</span> <span class="n">current_selection_last</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b3_down-224"><a href="#AggregatorView.mouse_b3_down-224"><span class="linenos">224</span></a>                <span class="n">selection</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_selection_first</span><span class="p">,</span> <span class="n">current_selection_last</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-225"><a href="#AggregatorView.mouse_b3_down-225"><span class="linenos">225</span></a>
</span><span id="AggregatorView.mouse_b3_down-226"><a href="#AggregatorView.mouse_b3_down-226"><span class="linenos">226</span></a>        <span class="k">if</span> <span class="n">selection</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="AggregatorView.mouse_b3_down-227"><a href="#AggregatorView.mouse_b3_down-227"><span class="linenos">227</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_clear</span><span class="p">()</span>
</span><span id="AggregatorView.mouse_b3_down-228"><a href="#AggregatorView.mouse_b3_down-228"><span class="linenos">228</span></a>            <span class="n">text_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">selection</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">selection</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="AggregatorView.mouse_b3_down-229"><a href="#AggregatorView.mouse_b3_down-229"><span class="linenos">229</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">clipboard_append</span><span class="p">(</span><span class="n">text_content</span><span class="p">)</span>
</span><span id="AggregatorView.mouse_b3_down-230"><a href="#AggregatorView.mouse_b3_down-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection_last</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b3_down-231"><a href="#AggregatorView.mouse_b3_down-231"><span class="linenos">231</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">selection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="AggregatorView.mouse_b3_down-232"><a href="#AggregatorView.mouse_b3_down-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">previously_was_mouse_b1_double</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.mouse_b3_down-233"><a href="#AggregatorView.mouse_b3_down-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_selection</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.selection_changed" class="classattr">
                                        <input id="AggregatorView.selection_changed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">selection_changed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.selection_changed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.selection_changed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.selection_changed-235"><a href="#AggregatorView.selection_changed-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="nf">selection_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
</span><span id="AggregatorView.selection_changed-236"><a href="#AggregatorView.selection_changed-236"><span class="linenos">236</span></a>        <span class="k">return</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.put" class="classattr">
                                        <input id="AggregatorView.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">text</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.put-238"><a href="#AggregatorView.put-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="AggregatorView.put-239"><a href="#AggregatorView.put-239"><span class="linenos">239</span></a>        <span class="n">lines_num_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="AggregatorView.put-240"><a href="#AggregatorView.put-240"><span class="linenos">240</span></a>        <span class="n">view_fractions_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="AggregatorView.put-241"><a href="#AggregatorView.put-241"><span class="linenos">241</span></a>        <span class="n">line_before</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_before</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_before</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="AggregatorView.put-242"><a href="#AggregatorView.put-242"><span class="linenos">242</span></a>        <span class="n">tag_insert_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView.put-243"><a href="#AggregatorView.put-243"><span class="linenos">243</span></a>        <span class="n">tag_current_before</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">)</span>
</span><span id="AggregatorView.put-244"><a href="#AggregatorView.put-244"><span class="linenos">244</span></a>        
</span><span id="AggregatorView.put-245"><a href="#AggregatorView.put-245"><span class="linenos">245</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView.put-246"><a href="#AggregatorView.put-246"><span class="linenos">246</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear_context</span><span class="p">()</span>
</span><span id="AggregatorView.put-247"><a href="#AggregatorView.put-247"><span class="linenos">247</span></a>        
</span><span id="AggregatorView.put-248"><a href="#AggregatorView.put-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">,</span> <span class="n">text</span><span class="p">)</span>
</span><span id="AggregatorView.put-249"><a href="#AggregatorView.put-249"><span class="linenos">249</span></a>        
</span><span id="AggregatorView.put-250"><a href="#AggregatorView.put-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="AggregatorView.put-251"><a href="#AggregatorView.put-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="n">ttkb__END</span><span class="p">)</span>
</span><span id="AggregatorView.put-252"><a href="#AggregatorView.put-252"><span class="linenos">252</span></a>
</span><span id="AggregatorView.put-253"><a href="#AggregatorView.put-253"><span class="linenos">253</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">append_data</span><span class="p">:</span>
</span><span id="AggregatorView.put-254"><a href="#AggregatorView.put-254"><span class="linenos">254</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.put-255"><a href="#AggregatorView.put-255"><span class="linenos">255</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="AggregatorView.put-256"><a href="#AggregatorView.put-256"><span class="linenos">256</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_remove</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span><span id="AggregatorView.put-257"><a href="#AggregatorView.put-257"><span class="linenos">257</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">tag_add</span><span class="p">(</span><span class="n">ttkb__CURRENT</span><span class="p">,</span> <span class="n">tag_current_before</span><span class="p">)</span>
</span><span id="AggregatorView.put-258"><a href="#AggregatorView.put-258"><span class="linenos">258</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_unset</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">)</span>
</span><span id="AggregatorView.put-259"><a href="#AggregatorView.put-259"><span class="linenos">259</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">mark_set</span><span class="p">(</span><span class="n">ttkb__INSERT</span><span class="p">,</span> <span class="n">tag_insert_before</span><span class="p">)</span>
</span><span id="AggregatorView.put-260"><a href="#AggregatorView.put-260"><span class="linenos">260</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">apply_selection</span><span class="p">()</span>
</span><span id="AggregatorView.put-261"><a href="#AggregatorView.put-261"><span class="linenos">261</span></a>            
</span><span id="AggregatorView.put-262"><a href="#AggregatorView.put-262"><span class="linenos">262</span></a>            <span class="n">lines_num_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span>
</span><span id="AggregatorView.put-263"><a href="#AggregatorView.put-263"><span class="linenos">263</span></a>            <span class="n">view_fractions_after</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">()</span>
</span><span id="AggregatorView.put-264"><a href="#AggregatorView.put-264"><span class="linenos">264</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num_after</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">view_fractions_after</span><span class="p">[</span><span class="mi">0</span><span class="p">])))</span>
</span><span id="AggregatorView.put-265"><a href="#AggregatorView.put-265"><span class="linenos">265</span></a>            
</span><span id="AggregatorView.put-266"><a href="#AggregatorView.put-266"><span class="linenos">266</span></a>            <span class="n">line_before</span> <span class="o">=</span> <span class="n">line_before</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="AggregatorView.put-267"><a href="#AggregatorView.put-267"><span class="linenos">267</span></a>            <span class="n">line_after</span> <span class="o">=</span> <span class="n">line_after</span> <span class="ow">or</span> <span class="mi">1</span>
</span><span id="AggregatorView.put-268"><a href="#AggregatorView.put-268"><span class="linenos">268</span></a>            <span class="k">if</span> <span class="n">line_after</span> <span class="o">!=</span> <span class="n">line_before</span><span class="p">:</span>
</span><span id="AggregatorView.put-269"><a href="#AggregatorView.put-269"><span class="linenos">269</span></a>                <span class="n">movement</span> <span class="o">=</span> <span class="n">line_before</span> <span class="o">-</span> <span class="n">line_after</span>
</span><span id="AggregatorView.put-270"><a href="#AggregatorView.put-270"><span class="linenos">270</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview_scroll</span><span class="p">(</span><span class="n">movement</span><span class="p">,</span> <span class="s1">&#39;units&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.index_to_line_number" class="classattr">
                                        <input id="AggregatorView.index_to_line_number-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">index_to_line_number</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">index</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.index_to_line_number-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.index_to_line_number"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.index_to_line_number-272"><a href="#AggregatorView.index_to_line_number-272"><span class="linenos">272</span></a>    <span class="k">def</span> <span class="nf">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="AggregatorView.index_to_line_number-273"><a href="#AggregatorView.index_to_line_number-273"><span class="linenos">273</span></a>        <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.clear_context" class="classattr">
                                        <input id="AggregatorView.clear_context-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear_context</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.clear_context-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.clear_context"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.clear_context-275"><a href="#AggregatorView.clear_context-275"><span class="linenos">275</span></a>    <span class="k">def</span> <span class="nf">clear_context</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView.clear_context-276"><a href="#AggregatorView.clear_context-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="s1">&#39;1.0&#39;</span><span class="p">,</span> <span class="s1">&#39;end&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.yscroll" class="classattr">
                                        <input id="AggregatorView.yscroll-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">yscroll</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.yscroll-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.yscroll"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.yscroll-278"><a href="#AggregatorView.yscroll-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="nf">yscroll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="AggregatorView.yscroll-279"><a href="#AggregatorView.yscroll-279"><span class="linenos">279</span></a>        <span class="n">first</span><span class="p">,</span> <span class="n">last</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="AggregatorView.yscroll-280"><a href="#AggregatorView.yscroll-280"><span class="linenos">280</span></a>        <span class="n">lines_num</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index_to_line_number</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="s1">&#39;end&#39;</span><span class="p">))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView.yscroll-281"><a href="#AggregatorView.yscroll-281"><span class="linenos">281</span></a>        <span class="n">last_line_index</span> <span class="o">=</span> <span class="n">lines_num</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView.yscroll-282"><a href="#AggregatorView.yscroll-282"><span class="linenos">282</span></a>        <span class="n">first_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">first</span><span class="p">)))</span>
</span><span id="AggregatorView.yscroll-283"><a href="#AggregatorView.yscroll-283"><span class="linenos">283</span></a>        <span class="n">last_visible_line_index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">ceil</span><span class="p">(</span><span class="n">lines_num</span> <span class="o">*</span> <span class="nb">float</span><span class="p">(</span><span class="n">last</span><span class="p">)))</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="AggregatorView.yscroll-284"><a href="#AggregatorView.yscroll-284"><span class="linenos">284</span></a>
</span><span id="AggregatorView.yscroll-285"><a href="#AggregatorView.yscroll-285"><span class="linenos">285</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span><span class="p">:</span>
</span><span id="AggregatorView.yscroll-286"><a href="#AggregatorView.yscroll-286"><span class="linenos">286</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&lt;</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="AggregatorView.yscroll-287"><a href="#AggregatorView.yscroll-287"><span class="linenos">287</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="AggregatorView.yscroll-288"><a href="#AggregatorView.yscroll-288"><span class="linenos">288</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="AggregatorView.yscroll-289"><a href="#AggregatorView.yscroll-289"><span class="linenos">289</span></a>            <span class="k">if</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">last_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="mi">0</span> <span class="o">&lt;</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">&gt;=</span> <span class="n">first_visible_line_index</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">last_visible_line_index</span> <span class="o">==</span> <span class="n">last_line_index</span><span class="p">):</span>
</span><span id="AggregatorView.yscroll-290"><a href="#AggregatorView.yscroll-290"><span class="linenos">290</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">auto_scroll</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="AggregatorView.yscroll-291"><a href="#AggregatorView.yscroll-291"><span class="linenos">291</span></a>        
</span><span id="AggregatorView.yscroll-292"><a href="#AggregatorView.yscroll-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_vbar</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.yview" class="classattr">
                                        <input id="AggregatorView.yview-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">yview</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.yview-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.yview"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.yview-294"><a href="#AggregatorView.yview-294"><span class="linenos">294</span></a>    <span class="k">def</span> <span class="nf">yview</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="AggregatorView.yview-295"><a href="#AggregatorView.yview-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_area</span><span class="o">.</span><span class="n">_text</span><span class="o">.</span><span class="n">yview</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.start" class="classattr">
                                        <input id="AggregatorView.start-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">wr</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">TkObjWrapper</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.start-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.start"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.start-297"><a href="#AggregatorView.start-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">wr</span><span class="p">:</span> <span class="n">TkObjWrapper</span><span class="p">):</span>
</span><span id="AggregatorView.start-298"><a href="#AggregatorView.start-298"><span class="linenos">298</span></a>        <span class="n">wr</span><span class="o">.</span><span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_updater</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="AggregatorView.stop" class="classattr">
                                        <input id="AggregatorView.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="AggregatorView.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AggregatorView.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AggregatorView.stop-300"><a href="#AggregatorView.stop-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AggregatorView.stop-301"><a href="#AggregatorView.stop-301"><span class="linenos">301</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stop</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>tkinter.ttk.Widget</dt>
                                <dd id="AggregatorView.identify" class="function">identify</dd>
                <dd id="AggregatorView.instate" class="function">instate</dd>
                <dd id="AggregatorView.state" class="function">state</dd>

            </div>
            <div><dt>tkinter.BaseWidget</dt>
                                <dd id="AggregatorView.widgetName" class="variable">widgetName</dd>
                <dd id="AggregatorView.destroy" class="function">destroy</dd>

            </div>
            <div><dt>tkinter.Misc</dt>
                                <dd id="AggregatorView.deletecommand" class="function">deletecommand</dd>
                <dd id="AggregatorView.tk_strictMotif" class="function">tk_strictMotif</dd>
                <dd id="AggregatorView.tk_bisque" class="function">tk_bisque</dd>
                <dd id="AggregatorView.tk_setPalette" class="function">tk_setPalette</dd>
                <dd id="AggregatorView.wait_variable" class="function">wait_variable</dd>
                <dd id="AggregatorView.waitvar" class="function">waitvar</dd>
                <dd id="AggregatorView.wait_window" class="function">wait_window</dd>
                <dd id="AggregatorView.wait_visibility" class="function">wait_visibility</dd>
                <dd id="AggregatorView.setvar" class="function">setvar</dd>
                <dd id="AggregatorView.getvar" class="function">getvar</dd>
                <dd id="AggregatorView.getint" class="function">getint</dd>
                <dd id="AggregatorView.getdouble" class="function">getdouble</dd>
                <dd id="AggregatorView.getboolean" class="function">getboolean</dd>
                <dd id="AggregatorView.focus_set" class="function">focus_set</dd>
                <dd id="AggregatorView.focus" class="function">focus</dd>
                <dd id="AggregatorView.focus_force" class="function">focus_force</dd>
                <dd id="AggregatorView.focus_get" class="function">focus_get</dd>
                <dd id="AggregatorView.focus_displayof" class="function">focus_displayof</dd>
                <dd id="AggregatorView.focus_lastfor" class="function">focus_lastfor</dd>
                <dd id="AggregatorView.tk_focusFollowsMouse" class="function">tk_focusFollowsMouse</dd>
                <dd id="AggregatorView.tk_focusNext" class="function">tk_focusNext</dd>
                <dd id="AggregatorView.tk_focusPrev" class="function">tk_focusPrev</dd>
                <dd id="AggregatorView.after" class="function">after</dd>
                <dd id="AggregatorView.after_idle" class="function">after_idle</dd>
                <dd id="AggregatorView.after_cancel" class="function">after_cancel</dd>
                <dd id="AggregatorView.bell" class="function">bell</dd>
                <dd id="AggregatorView.clipboard_get" class="function">clipboard_get</dd>
                <dd id="AggregatorView.clipboard_clear" class="function">clipboard_clear</dd>
                <dd id="AggregatorView.clipboard_append" class="function">clipboard_append</dd>
                <dd id="AggregatorView.grab_current" class="function">grab_current</dd>
                <dd id="AggregatorView.grab_release" class="function">grab_release</dd>
                <dd id="AggregatorView.grab_set" class="function">grab_set</dd>
                <dd id="AggregatorView.grab_set_global" class="function">grab_set_global</dd>
                <dd id="AggregatorView.grab_status" class="function">grab_status</dd>
                <dd id="AggregatorView.option_add" class="function">option_add</dd>
                <dd id="AggregatorView.option_clear" class="function">option_clear</dd>
                <dd id="AggregatorView.option_get" class="function">option_get</dd>
                <dd id="AggregatorView.option_readfile" class="function">option_readfile</dd>
                <dd id="AggregatorView.selection_clear" class="function">selection_clear</dd>
                <dd id="AggregatorView.selection_get" class="function">selection_get</dd>
                <dd id="AggregatorView.selection_handle" class="function">selection_handle</dd>
                <dd id="AggregatorView.selection_own" class="function">selection_own</dd>
                <dd id="AggregatorView.selection_own_get" class="function">selection_own_get</dd>
                <dd id="AggregatorView.send" class="function">send</dd>
                <dd id="AggregatorView.lower" class="function">lower</dd>
                <dd id="AggregatorView.tkraise" class="function">tkraise</dd>
                <dd id="AggregatorView.lift" class="function">lift</dd>
                <dd id="AggregatorView.winfo_atom" class="function">winfo_atom</dd>
                <dd id="AggregatorView.winfo_atomname" class="function">winfo_atomname</dd>
                <dd id="AggregatorView.winfo_cells" class="function">winfo_cells</dd>
                <dd id="AggregatorView.winfo_children" class="function">winfo_children</dd>
                <dd id="AggregatorView.winfo_class" class="function">winfo_class</dd>
                <dd id="AggregatorView.winfo_colormapfull" class="function">winfo_colormapfull</dd>
                <dd id="AggregatorView.winfo_containing" class="function">winfo_containing</dd>
                <dd id="AggregatorView.winfo_depth" class="function">winfo_depth</dd>
                <dd id="AggregatorView.winfo_exists" class="function">winfo_exists</dd>
                <dd id="AggregatorView.winfo_fpixels" class="function">winfo_fpixels</dd>
                <dd id="AggregatorView.winfo_geometry" class="function">winfo_geometry</dd>
                <dd id="AggregatorView.winfo_height" class="function">winfo_height</dd>
                <dd id="AggregatorView.winfo_id" class="function">winfo_id</dd>
                <dd id="AggregatorView.winfo_interps" class="function">winfo_interps</dd>
                <dd id="AggregatorView.winfo_ismapped" class="function">winfo_ismapped</dd>
                <dd id="AggregatorView.winfo_manager" class="function">winfo_manager</dd>
                <dd id="AggregatorView.winfo_name" class="function">winfo_name</dd>
                <dd id="AggregatorView.winfo_parent" class="function">winfo_parent</dd>
                <dd id="AggregatorView.winfo_pathname" class="function">winfo_pathname</dd>
                <dd id="AggregatorView.winfo_pixels" class="function">winfo_pixels</dd>
                <dd id="AggregatorView.winfo_pointerx" class="function">winfo_pointerx</dd>
                <dd id="AggregatorView.winfo_pointerxy" class="function">winfo_pointerxy</dd>
                <dd id="AggregatorView.winfo_pointery" class="function">winfo_pointery</dd>
                <dd id="AggregatorView.winfo_reqheight" class="function">winfo_reqheight</dd>
                <dd id="AggregatorView.winfo_reqwidth" class="function">winfo_reqwidth</dd>
                <dd id="AggregatorView.winfo_rgb" class="function">winfo_rgb</dd>
                <dd id="AggregatorView.winfo_rootx" class="function">winfo_rootx</dd>
                <dd id="AggregatorView.winfo_rooty" class="function">winfo_rooty</dd>
                <dd id="AggregatorView.winfo_screen" class="function">winfo_screen</dd>
                <dd id="AggregatorView.winfo_screencells" class="function">winfo_screencells</dd>
                <dd id="AggregatorView.winfo_screendepth" class="function">winfo_screendepth</dd>
                <dd id="AggregatorView.winfo_screenheight" class="function">winfo_screenheight</dd>
                <dd id="AggregatorView.winfo_screenmmheight" class="function">winfo_screenmmheight</dd>
                <dd id="AggregatorView.winfo_screenmmwidth" class="function">winfo_screenmmwidth</dd>
                <dd id="AggregatorView.winfo_screenvisual" class="function">winfo_screenvisual</dd>
                <dd id="AggregatorView.winfo_screenwidth" class="function">winfo_screenwidth</dd>
                <dd id="AggregatorView.winfo_server" class="function">winfo_server</dd>
                <dd id="AggregatorView.winfo_toplevel" class="function">winfo_toplevel</dd>
                <dd id="AggregatorView.winfo_viewable" class="function">winfo_viewable</dd>
                <dd id="AggregatorView.winfo_visual" class="function">winfo_visual</dd>
                <dd id="AggregatorView.winfo_visualid" class="function">winfo_visualid</dd>
                <dd id="AggregatorView.winfo_visualsavailable" class="function">winfo_visualsavailable</dd>
                <dd id="AggregatorView.winfo_vrootheight" class="function">winfo_vrootheight</dd>
                <dd id="AggregatorView.winfo_vrootwidth" class="function">winfo_vrootwidth</dd>
                <dd id="AggregatorView.winfo_vrootx" class="function">winfo_vrootx</dd>
                <dd id="AggregatorView.winfo_vrooty" class="function">winfo_vrooty</dd>
                <dd id="AggregatorView.winfo_width" class="function">winfo_width</dd>
                <dd id="AggregatorView.winfo_x" class="function">winfo_x</dd>
                <dd id="AggregatorView.winfo_y" class="function">winfo_y</dd>
                <dd id="AggregatorView.update" class="function">update</dd>
                <dd id="AggregatorView.update_idletasks" class="function">update_idletasks</dd>
                <dd id="AggregatorView.bindtags" class="function">bindtags</dd>
                <dd id="AggregatorView.bind" class="function">bind</dd>
                <dd id="AggregatorView.unbind" class="function">unbind</dd>
                <dd id="AggregatorView.bind_all" class="function">bind_all</dd>
                <dd id="AggregatorView.unbind_all" class="function">unbind_all</dd>
                <dd id="AggregatorView.bind_class" class="function">bind_class</dd>
                <dd id="AggregatorView.unbind_class" class="function">unbind_class</dd>
                <dd id="AggregatorView.mainloop" class="function">mainloop</dd>
                <dd id="AggregatorView.quit" class="function">quit</dd>
                <dd id="AggregatorView.nametowidget" class="function">nametowidget</dd>
                <dd id="AggregatorView.register" class="function">register</dd>
                <dd id="AggregatorView.cget" class="function">cget</dd>
                <dd id="AggregatorView.keys" class="function">keys</dd>
                <dd id="AggregatorView.pack_propagate" class="function">pack_propagate</dd>
                <dd id="AggregatorView.propagate" class="function">propagate</dd>
                <dd id="AggregatorView.pack_slaves" class="function">pack_slaves</dd>
                <dd id="AggregatorView.slaves" class="function">slaves</dd>
                <dd id="AggregatorView.place_slaves" class="function">place_slaves</dd>
                <dd id="AggregatorView.grid_anchor" class="function">grid_anchor</dd>
                <dd id="AggregatorView.anchor" class="function">anchor</dd>
                <dd id="AggregatorView.grid_bbox" class="function">grid_bbox</dd>
                <dd id="AggregatorView.bbox" class="function">bbox</dd>
                <dd id="AggregatorView.grid_columnconfigure" class="function">grid_columnconfigure</dd>
                <dd id="AggregatorView.columnconfigure" class="function">columnconfigure</dd>
                <dd id="AggregatorView.grid_location" class="function">grid_location</dd>
                <dd id="AggregatorView.grid_propagate" class="function">grid_propagate</dd>
                <dd id="AggregatorView.grid_rowconfigure" class="function">grid_rowconfigure</dd>
                <dd id="AggregatorView.rowconfigure" class="function">rowconfigure</dd>
                <dd id="AggregatorView.grid_size" class="function">grid_size</dd>
                <dd id="AggregatorView.size" class="function">size</dd>
                <dd id="AggregatorView.grid_slaves" class="function">grid_slaves</dd>
                <dd id="AggregatorView.event_add" class="function">event_add</dd>
                <dd id="AggregatorView.event_delete" class="function">event_delete</dd>
                <dd id="AggregatorView.event_generate" class="function">event_generate</dd>
                <dd id="AggregatorView.event_info" class="function">event_info</dd>
                <dd id="AggregatorView.image_names" class="function">image_names</dd>
                <dd id="AggregatorView.image_types" class="function">image_types</dd>

            </div>
            <div><dt>tkinter.ttk.Frame</dt>
                                <dd id="AggregatorView.configure" class="function">configure</dd>
                <dd id="AggregatorView.config" class="function">config</dd>

            </div>
            <div><dt>tkinter.Pack</dt>
                                <dd id="AggregatorView.pack_configure" class="function">pack_configure</dd>
                <dd id="AggregatorView.pack_forget" class="function">pack_forget</dd>
                <dd id="AggregatorView.forget" class="function">forget</dd>
                <dd id="AggregatorView.pack_info" class="function">pack_info</dd>
                <dd id="AggregatorView.info" class="function">info</dd>
                <dd id="AggregatorView.pack" class="function">pack</dd>

            </div>
            <div><dt>tkinter.Place</dt>
                                <dd id="AggregatorView.place_configure" class="function">place_configure</dd>
                <dd id="AggregatorView.place_forget" class="function">place_forget</dd>
                <dd id="AggregatorView.place_info" class="function">place_info</dd>
                <dd id="AggregatorView.place" class="function">place</dd>

            </div>
            <div><dt>tkinter.Grid</dt>
                                <dd id="AggregatorView.grid_configure" class="function">grid_configure</dd>
                <dd id="AggregatorView.grid_forget" class="function">grid_forget</dd>
                <dd id="AggregatorView.grid_remove" class="function">grid_remove</dd>
                <dd id="AggregatorView.grid_info" class="function">grid_info</dd>
                <dd id="AggregatorView.grid" class="function">grid</dd>
                <dd id="AggregatorView.location" class="function">location</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>