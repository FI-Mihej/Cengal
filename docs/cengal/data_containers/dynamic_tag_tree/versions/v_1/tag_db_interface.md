---
title: tag_db_interface
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_containers<wbr>.dynamic_tag_tree<wbr>.versions<wbr>.v_1<wbr>.tag_db_interface    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-tag_db_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-tag_db_interface-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;tag_db_interface&#39;</span><span class="p">,</span> <span class="s1">&#39;SMART_TREE_TYPE&#39;</span><span class="p">,</span> <span class="s1">&#39;SMART_TREE_TYPE_WITH_INTERNAL_MENU&#39;</span><span class="p">,</span> <span class="s1">&#39;FULL_TREE_TYPE&#39;</span><span class="p">,</span> <span class="s1">&#39;PLAIN_PSEUDO_TREE_TYPE&#39;</span><span class="p">,</span> <span class="s1">&#39;USUAL_TREE_TYPE&#39;</span><span class="p">,</span> <span class="s1">&#39;ToManyIdenticalItemsOnTheGivenTagPathError&#39;</span><span class="p">,</span> <span class="s1">&#39;UnknownTreeTypeError&#39;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s1">&#39;Mikhail Butenko &lt;gtalk@mikhail-butenko.in.ua&gt;&#39;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="c1"># import TagDB</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="c1"># from TagDB import USUAL_TREE_TYPE as USUAL_TREE_TYPE</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="c1"># from TagDB import SMART_TREE_TYPE as SMART_TREE_TYPE</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="c1"># from TagDB import FULL_TREE_TYPE as FULL_TREE_TYPE</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="c1"># from TagDB import PLAIN_PSEUDO_TREE_TYPE as PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">.TagDB</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="kn">import</span> <span class="nn">copy</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="kn">from</span> <span class="nn">cengal.web_tools.request_cache</span> <span class="kn">import</span> <span class="n">RequestCache</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="kn">import</span> <span class="nn">time</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">gly</span><span class="p">,</span> <span class="n">CoroPriority</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.read_write_locker</span> <span class="kn">import</span> <span class="n">grwl</span><span class="p">,</span> <span class="n">RWOperation</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">EntityStatsMixin</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.tree_traversal</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="k">class</span> <span class="nc">tag_db_interface</span><span class="p">(</span><span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__db</span> <span class="o">=</span> <span class="n">TagDB</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">RequestCache</span><span class="p">(</span><span class="mi">300000</span><span class="p">,</span> <span class="n">default_priority</span><span class="o">=</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">lock_entity_id</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="n">tag_db_name</span><span class="p">,</span> <span class="n">tag_db_stats</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_entity_stats</span><span class="p">(</span><span class="n">stats_level</span><span class="p">)</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>            <span class="s1">&#39;interface&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>                <span class="s1">&#39;cache size&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">_requestsAndData</span><span class="p">),</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>                <span class="s1">&#39;last fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">,</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>                <span class="s1">&#39;last fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span><span class="p">,</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>                <span class="s1">&#39;last tested fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">,</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>                <span class="s1">&#39;last tested fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span><span class="p">,</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>                <span class="s1">&#39;fill cache iterations&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">,</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>                <span class="s1">&#39;fill cache iterations per second&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">,</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>            <span class="p">},</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>            <span class="s1">&#39;db&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>                <span class="n">tag_db_name</span><span class="p">:</span> <span class="n">tag_db_stats</span><span class="p">,</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>            <span class="p">}</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="p">}</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="nf">_glock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="k">return</span> <span class="n">grwl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="nf">_wlock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_glock</span><span class="p">()(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span><span class="p">)</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="nf">_rlock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_glock</span><span class="p">()(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span><span class="p">)</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">get_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">new_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;tag_db_interface&#39;</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">return</span> <span class="n">tag_db_interface</span><span class="p">(</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">,</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">,</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">,</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>            <span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">)</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">remove_item</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>            <span class="c1"># request = (&#39;get_items&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_items&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>                
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">get_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>            <span class="c1"># request = (&#39;get_tags&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_tags&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>            <span class="c1"># request = (&#39;get_all&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_all&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_all_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="c1"># request = (&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="c1">#            , tuple(self.__db.sort_tag_list_by_hash(binTags)))</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">fill_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="nb">list</span><span class="p">()):</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="n">tags_and_items_inside_curent_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="n">internal_tags</span> <span class="o">=</span> <span class="n">tags_and_items_inside_curent_path</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_items</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="k">if</span> <span class="n">resultTime</span> <span class="o">&gt;=</span> <span class="n">max_answer_time_in_seconds</span><span class="p">:</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">internal_tags</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache</span><span class="p">(</span><span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>    <span class="k">def</span> <span class="nf">fill_web_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="n">ly</span><span class="p">()</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="n">path</span> <span class="o">=</span> <span class="n">path</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">is_cached</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">web_browse_to</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="n">depth</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="n">dtime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="k">if</span> <span class="n">dtime</span> <span class="o">&gt;=</span> <span class="mf">1.0</span><span class="p">:</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="n">iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span> <span class="o">=</span> <span class="n">iterations</span> <span class="o">/</span> <span class="n">dtime</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="c1"># if (depth &gt; 0) and (is_cached or (resultTime &gt;= max_answer_time_in_seconds)):</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="c1"># if (depth &gt; 0) and (resultTime &gt;= max_answer_time_in_seconds):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="n">depth</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_web_cache</span><span class="p">(</span><span class="n">depth</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="nf">clear_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">web_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">return_is_cached_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">use_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>            <span class="n">additional_tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            <span class="k">if</span> <span class="n">additional_tags</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">additional_tags</span><span class="p">)</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="n">binTags</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">))</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="n">items</span><span class="p">,</span> <span class="n">items_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">,</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items_ids</span><span class="p">)</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="k">if</span> <span class="n">return_is_cached_result</span><span class="p">:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">is_cached_result</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="nf">fs_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            </section>
                <section id="tag_db_interface">
                            <input id="tag_db_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">tag_db_interface</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="tag_db_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface-57"><a href="#tag_db_interface-57"><span class="linenos"> 57</span></a><span class="k">class</span> <span class="nc">tag_db_interface</span><span class="p">(</span><span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="tag_db_interface-58"><a href="#tag_db_interface-58"><span class="linenos"> 58</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="tag_db_interface-59"><a href="#tag_db_interface-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="tag_db_interface-60"><a href="#tag_db_interface-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__db</span> <span class="o">=</span> <span class="n">TagDB</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface-61"><a href="#tag_db_interface-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">RequestCache</span><span class="p">(</span><span class="mi">300000</span><span class="p">,</span> <span class="n">default_priority</span><span class="o">=</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface-62"><a href="#tag_db_interface-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">lock_entity_id</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="tag_db_interface-63"><a href="#tag_db_interface-63"><span class="linenos"> 63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>
</span><span id="tag_db_interface-64"><a href="#tag_db_interface-64"><span class="linenos"> 64</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>
</span><span id="tag_db_interface-65"><a href="#tag_db_interface-65"><span class="linenos"> 65</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-66"><a href="#tag_db_interface-66"><span class="linenos"> 66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-67"><a href="#tag_db_interface-67"><span class="linenos"> 67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-68"><a href="#tag_db_interface-68"><span class="linenos"> 68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-69"><a href="#tag_db_interface-69"><span class="linenos"> 69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="tag_db_interface-70"><a href="#tag_db_interface-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-71"><a href="#tag_db_interface-71"><span class="linenos"> 71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-72"><a href="#tag_db_interface-72"><span class="linenos"> 72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="tag_db_interface-73"><a href="#tag_db_interface-73"><span class="linenos"> 73</span></a>
</span><span id="tag_db_interface-74"><a href="#tag_db_interface-74"><span class="linenos"> 74</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="tag_db_interface-75"><a href="#tag_db_interface-75"><span class="linenos"> 75</span></a>        <span class="n">tag_db_name</span><span class="p">,</span> <span class="n">tag_db_stats</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_entity_stats</span><span class="p">(</span><span class="n">stats_level</span><span class="p">)</span>
</span><span id="tag_db_interface-76"><a href="#tag_db_interface-76"><span class="linenos"> 76</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="tag_db_interface-77"><a href="#tag_db_interface-77"><span class="linenos"> 77</span></a>            <span class="s1">&#39;interface&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="tag_db_interface-78"><a href="#tag_db_interface-78"><span class="linenos"> 78</span></a>                <span class="s1">&#39;cache size&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">_requestsAndData</span><span class="p">),</span>
</span><span id="tag_db_interface-79"><a href="#tag_db_interface-79"><span class="linenos"> 79</span></a>                <span class="s1">&#39;last fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">,</span>
</span><span id="tag_db_interface-80"><a href="#tag_db_interface-80"><span class="linenos"> 80</span></a>                <span class="s1">&#39;last fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span><span class="p">,</span>
</span><span id="tag_db_interface-81"><a href="#tag_db_interface-81"><span class="linenos"> 81</span></a>                <span class="s1">&#39;last tested fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">,</span>
</span><span id="tag_db_interface-82"><a href="#tag_db_interface-82"><span class="linenos"> 82</span></a>                <span class="s1">&#39;last tested fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span><span class="p">,</span>
</span><span id="tag_db_interface-83"><a href="#tag_db_interface-83"><span class="linenos"> 83</span></a>                <span class="s1">&#39;fill cache iterations&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">,</span>
</span><span id="tag_db_interface-84"><a href="#tag_db_interface-84"><span class="linenos"> 84</span></a>                <span class="s1">&#39;fill cache iterations per second&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">,</span>
</span><span id="tag_db_interface-85"><a href="#tag_db_interface-85"><span class="linenos"> 85</span></a>            <span class="p">},</span>
</span><span id="tag_db_interface-86"><a href="#tag_db_interface-86"><span class="linenos"> 86</span></a>            <span class="s1">&#39;db&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="tag_db_interface-87"><a href="#tag_db_interface-87"><span class="linenos"> 87</span></a>                <span class="n">tag_db_name</span><span class="p">:</span> <span class="n">tag_db_stats</span><span class="p">,</span>
</span><span id="tag_db_interface-88"><a href="#tag_db_interface-88"><span class="linenos"> 88</span></a>            <span class="p">}</span>
</span><span id="tag_db_interface-89"><a href="#tag_db_interface-89"><span class="linenos"> 89</span></a>        <span class="p">}</span>
</span><span id="tag_db_interface-90"><a href="#tag_db_interface-90"><span class="linenos"> 90</span></a>    
</span><span id="tag_db_interface-91"><a href="#tag_db_interface-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">_glock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface-92"><a href="#tag_db_interface-92"><span class="linenos"> 92</span></a>        <span class="k">return</span> <span class="n">grwl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">,</span> <span class="kc">False</span><span class="p">)</span>
</span><span id="tag_db_interface-93"><a href="#tag_db_interface-93"><span class="linenos"> 93</span></a>    
</span><span id="tag_db_interface-94"><a href="#tag_db_interface-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="nf">_wlock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface-95"><a href="#tag_db_interface-95"><span class="linenos"> 95</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_glock</span><span class="p">()(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">write</span><span class="p">)</span>
</span><span id="tag_db_interface-96"><a href="#tag_db_interface-96"><span class="linenos"> 96</span></a>    
</span><span id="tag_db_interface-97"><a href="#tag_db_interface-97"><span class="linenos"> 97</span></a>    <span class="k">def</span> <span class="nf">_rlock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface-98"><a href="#tag_db_interface-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_glock</span><span class="p">()(</span><span class="n">RWOperation</span><span class="o">.</span><span class="n">read</span><span class="p">)</span>
</span><span id="tag_db_interface-99"><a href="#tag_db_interface-99"><span class="linenos"> 99</span></a>
</span><span id="tag_db_interface-100"><a href="#tag_db_interface-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">get_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface-101"><a href="#tag_db_interface-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span>
</span><span id="tag_db_interface-102"><a href="#tag_db_interface-102"><span class="linenos">102</span></a>    
</span><span id="tag_db_interface-103"><a href="#tag_db_interface-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">new_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;tag_db_interface&#39;</span><span class="p">:</span>
</span><span id="tag_db_interface-104"><a href="#tag_db_interface-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="n">tag_db_interface</span><span class="p">(</span>
</span><span id="tag_db_interface-105"><a href="#tag_db_interface-105"><span class="linenos">105</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">,</span>
</span><span id="tag_db_interface-106"><a href="#tag_db_interface-106"><span class="linenos">106</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">,</span>
</span><span id="tag_db_interface-107"><a href="#tag_db_interface-107"><span class="linenos">107</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">,</span>
</span><span id="tag_db_interface-108"><a href="#tag_db_interface-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="tag_db_interface-109"><a href="#tag_db_interface-109"><span class="linenos">109</span></a>            <span class="p">)</span>
</span><span id="tag_db_interface-110"><a href="#tag_db_interface-110"><span class="linenos">110</span></a>
</span><span id="tag_db_interface-111"><a href="#tag_db_interface-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface-112"><a href="#tag_db_interface-112"><span class="linenos">112</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="tag_db_interface-113"><a href="#tag_db_interface-113"><span class="linenos">113</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface-114"><a href="#tag_db_interface-114"><span class="linenos">114</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-115"><a href="#tag_db_interface-115"><span class="linenos">115</span></a>
</span><span id="tag_db_interface-116"><a href="#tag_db_interface-116"><span class="linenos">116</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-117"><a href="#tag_db_interface-117"><span class="linenos">117</span></a>
</span><span id="tag_db_interface-118"><a href="#tag_db_interface-118"><span class="linenos">118</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-119"><a href="#tag_db_interface-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface-120"><a href="#tag_db_interface-120"><span class="linenos">120</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-121"><a href="#tag_db_interface-121"><span class="linenos">121</span></a>
</span><span id="tag_db_interface-122"><a href="#tag_db_interface-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="tag_db_interface-123"><a href="#tag_db_interface-123"><span class="linenos">123</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="tag_db_interface-124"><a href="#tag_db_interface-124"><span class="linenos">124</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-125"><a href="#tag_db_interface-125"><span class="linenos">125</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface-126"><a href="#tag_db_interface-126"><span class="linenos">126</span></a>
</span><span id="tag_db_interface-127"><a href="#tag_db_interface-127"><span class="linenos">127</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">remove_item</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface-128"><a href="#tag_db_interface-128"><span class="linenos">128</span></a>
</span><span id="tag_db_interface-129"><a href="#tag_db_interface-129"><span class="linenos">129</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-130"><a href="#tag_db_interface-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface-131"><a href="#tag_db_interface-131"><span class="linenos">131</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-132"><a href="#tag_db_interface-132"><span class="linenos">132</span></a>
</span><span id="tag_db_interface-133"><a href="#tag_db_interface-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface-134"><a href="#tag_db_interface-134"><span class="linenos">134</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-135"><a href="#tag_db_interface-135"><span class="linenos">135</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-136"><a href="#tag_db_interface-136"><span class="linenos">136</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-137"><a href="#tag_db_interface-137"><span class="linenos">137</span></a>
</span><span id="tag_db_interface-138"><a href="#tag_db_interface-138"><span class="linenos">138</span></a>            <span class="c1"># request = (&#39;get_items&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface-139"><a href="#tag_db_interface-139"><span class="linenos">139</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_items&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-140"><a href="#tag_db_interface-140"><span class="linenos">140</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-141"><a href="#tag_db_interface-141"><span class="linenos">141</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-142"><a href="#tag_db_interface-142"><span class="linenos">142</span></a>                
</span><span id="tag_db_interface-143"><a href="#tag_db_interface-143"><span class="linenos">143</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-144"><a href="#tag_db_interface-144"><span class="linenos">144</span></a>
</span><span id="tag_db_interface-145"><a href="#tag_db_interface-145"><span class="linenos">145</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-146"><a href="#tag_db_interface-146"><span class="linenos">146</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-147"><a href="#tag_db_interface-147"><span class="linenos">147</span></a>
</span><span id="tag_db_interface-148"><a href="#tag_db_interface-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">get_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface-149"><a href="#tag_db_interface-149"><span class="linenos">149</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-150"><a href="#tag_db_interface-150"><span class="linenos">150</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-151"><a href="#tag_db_interface-151"><span class="linenos">151</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-152"><a href="#tag_db_interface-152"><span class="linenos">152</span></a>
</span><span id="tag_db_interface-153"><a href="#tag_db_interface-153"><span class="linenos">153</span></a>            <span class="c1"># request = (&#39;get_tags&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface-154"><a href="#tag_db_interface-154"><span class="linenos">154</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_tags&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-155"><a href="#tag_db_interface-155"><span class="linenos">155</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-156"><a href="#tag_db_interface-156"><span class="linenos">156</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-157"><a href="#tag_db_interface-157"><span class="linenos">157</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-158"><a href="#tag_db_interface-158"><span class="linenos">158</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-159"><a href="#tag_db_interface-159"><span class="linenos">159</span></a>
</span><span id="tag_db_interface-160"><a href="#tag_db_interface-160"><span class="linenos">160</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-161"><a href="#tag_db_interface-161"><span class="linenos">161</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-162"><a href="#tag_db_interface-162"><span class="linenos">162</span></a>
</span><span id="tag_db_interface-163"><a href="#tag_db_interface-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface-164"><a href="#tag_db_interface-164"><span class="linenos">164</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-165"><a href="#tag_db_interface-165"><span class="linenos">165</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-166"><a href="#tag_db_interface-166"><span class="linenos">166</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-167"><a href="#tag_db_interface-167"><span class="linenos">167</span></a>
</span><span id="tag_db_interface-168"><a href="#tag_db_interface-168"><span class="linenos">168</span></a>            <span class="c1"># request = (&#39;get_all&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface-169"><a href="#tag_db_interface-169"><span class="linenos">169</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_all&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-170"><a href="#tag_db_interface-170"><span class="linenos">170</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-171"><a href="#tag_db_interface-171"><span class="linenos">171</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-172"><a href="#tag_db_interface-172"><span class="linenos">172</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_all_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface-173"><a href="#tag_db_interface-173"><span class="linenos">173</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-174"><a href="#tag_db_interface-174"><span class="linenos">174</span></a>
</span><span id="tag_db_interface-175"><a href="#tag_db_interface-175"><span class="linenos">175</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-176"><a href="#tag_db_interface-176"><span class="linenos">176</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-177"><a href="#tag_db_interface-177"><span class="linenos">177</span></a>
</span><span id="tag_db_interface-178"><a href="#tag_db_interface-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface-179"><a href="#tag_db_interface-179"><span class="linenos">179</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-180"><a href="#tag_db_interface-180"><span class="linenos">180</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-181"><a href="#tag_db_interface-181"><span class="linenos">181</span></a>
</span><span id="tag_db_interface-182"><a href="#tag_db_interface-182"><span class="linenos">182</span></a>            <span class="c1"># request = (&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span>
</span><span id="tag_db_interface-183"><a href="#tag_db_interface-183"><span class="linenos">183</span></a>            <span class="c1">#            , tuple(self.__db.sort_tag_list_by_hash(binTags)))</span>
</span><span id="tag_db_interface-184"><a href="#tag_db_interface-184"><span class="linenos">184</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface-185"><a href="#tag_db_interface-185"><span class="linenos">185</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-186"><a href="#tag_db_interface-186"><span class="linenos">186</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-187"><a href="#tag_db_interface-187"><span class="linenos">187</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-188"><a href="#tag_db_interface-188"><span class="linenos">188</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-189"><a href="#tag_db_interface-189"><span class="linenos">189</span></a>
</span><span id="tag_db_interface-190"><a href="#tag_db_interface-190"><span class="linenos">190</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-191"><a href="#tag_db_interface-191"><span class="linenos">191</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-192"><a href="#tag_db_interface-192"><span class="linenos">192</span></a>
</span><span id="tag_db_interface-193"><a href="#tag_db_interface-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">fill_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="nb">list</span><span class="p">()):</span>
</span><span id="tag_db_interface-194"><a href="#tag_db_interface-194"><span class="linenos">194</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface-195"><a href="#tag_db_interface-195"><span class="linenos">195</span></a>        
</span><span id="tag_db_interface-196"><a href="#tag_db_interface-196"><span class="linenos">196</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="tag_db_interface-197"><a href="#tag_db_interface-197"><span class="linenos">197</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-198"><a href="#tag_db_interface-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface-199"><a href="#tag_db_interface-199"><span class="linenos">199</span></a>
</span><span id="tag_db_interface-200"><a href="#tag_db_interface-200"><span class="linenos">200</span></a>        <span class="n">tags_and_items_inside_curent_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface-201"><a href="#tag_db_interface-201"><span class="linenos">201</span></a>        <span class="n">internal_tags</span> <span class="o">=</span> <span class="n">tags_and_items_inside_curent_path</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="tag_db_interface-202"><a href="#tag_db_interface-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_items</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface-203"><a href="#tag_db_interface-203"><span class="linenos">203</span></a>        
</span><span id="tag_db_interface-204"><a href="#tag_db_interface-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="tag_db_interface-205"><a href="#tag_db_interface-205"><span class="linenos">205</span></a>
</span><span id="tag_db_interface-206"><a href="#tag_db_interface-206"><span class="linenos">206</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-207"><a href="#tag_db_interface-207"><span class="linenos">207</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="tag_db_interface-208"><a href="#tag_db_interface-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface-209"><a href="#tag_db_interface-209"><span class="linenos">209</span></a>        <span class="k">if</span> <span class="n">resultTime</span> <span class="o">&gt;=</span> <span class="n">max_answer_time_in_seconds</span><span class="p">:</span>
</span><span id="tag_db_interface-210"><a href="#tag_db_interface-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface-211"><a href="#tag_db_interface-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface-212"><a href="#tag_db_interface-212"><span class="linenos">212</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">internal_tags</span><span class="p">:</span>
</span><span id="tag_db_interface-213"><a href="#tag_db_interface-213"><span class="linenos">213</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="tag_db_interface-214"><a href="#tag_db_interface-214"><span class="linenos">214</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="tag_db_interface-215"><a href="#tag_db_interface-215"><span class="linenos">215</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache</span><span class="p">(</span><span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span><span id="tag_db_interface-216"><a href="#tag_db_interface-216"><span class="linenos">216</span></a>
</span><span id="tag_db_interface-217"><a href="#tag_db_interface-217"><span class="linenos">217</span></a>    <span class="k">def</span> <span class="nf">fill_web_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="tag_db_interface-218"><a href="#tag_db_interface-218"><span class="linenos">218</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface-219"><a href="#tag_db_interface-219"><span class="linenos">219</span></a>        <span class="n">ly</span><span class="p">()</span>
</span><span id="tag_db_interface-220"><a href="#tag_db_interface-220"><span class="linenos">220</span></a>
</span><span id="tag_db_interface-221"><a href="#tag_db_interface-221"><span class="linenos">221</span></a>        <span class="n">path</span> <span class="o">=</span> <span class="n">path</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="tag_db_interface-222"><a href="#tag_db_interface-222"><span class="linenos">222</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="tag_db_interface-223"><a href="#tag_db_interface-223"><span class="linenos">223</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-224"><a href="#tag_db_interface-224"><span class="linenos">224</span></a>
</span><span id="tag_db_interface-225"><a href="#tag_db_interface-225"><span class="linenos">225</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">is_cached</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">web_browse_to</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="tag_db_interface-226"><a href="#tag_db_interface-226"><span class="linenos">226</span></a>        <span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="tag_db_interface-227"><a href="#tag_db_interface-227"><span class="linenos">227</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">)</span>
</span><span id="tag_db_interface-228"><a href="#tag_db_interface-228"><span class="linenos">228</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface-229"><a href="#tag_db_interface-229"><span class="linenos">229</span></a>        
</span><span id="tag_db_interface-230"><a href="#tag_db_interface-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="tag_db_interface-231"><a href="#tag_db_interface-231"><span class="linenos">231</span></a>        <span class="n">depth</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="tag_db_interface-232"><a href="#tag_db_interface-232"><span class="linenos">232</span></a>        
</span><span id="tag_db_interface-233"><a href="#tag_db_interface-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="tag_db_interface-234"><a href="#tag_db_interface-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="tag_db_interface-235"><a href="#tag_db_interface-235"><span class="linenos">235</span></a>        
</span><span id="tag_db_interface-236"><a href="#tag_db_interface-236"><span class="linenos">236</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-237"><a href="#tag_db_interface-237"><span class="linenos">237</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-238"><a href="#tag_db_interface-238"><span class="linenos">238</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface-239"><a href="#tag_db_interface-239"><span class="linenos">239</span></a>            <span class="n">dtime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span>
</span><span id="tag_db_interface-240"><a href="#tag_db_interface-240"><span class="linenos">240</span></a>            <span class="k">if</span> <span class="n">dtime</span> <span class="o">&gt;=</span> <span class="mf">1.0</span><span class="p">:</span>
</span><span id="tag_db_interface-241"><a href="#tag_db_interface-241"><span class="linenos">241</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-242"><a href="#tag_db_interface-242"><span class="linenos">242</span></a>                <span class="n">iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span>
</span><span id="tag_db_interface-243"><a href="#tag_db_interface-243"><span class="linenos">243</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span> <span class="o">=</span> <span class="n">iterations</span> <span class="o">/</span> <span class="n">dtime</span>
</span><span id="tag_db_interface-244"><a href="#tag_db_interface-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="tag_db_interface-245"><a href="#tag_db_interface-245"><span class="linenos">245</span></a>
</span><span id="tag_db_interface-246"><a href="#tag_db_interface-246"><span class="linenos">246</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface-247"><a href="#tag_db_interface-247"><span class="linenos">247</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="tag_db_interface-248"><a href="#tag_db_interface-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface-249"><a href="#tag_db_interface-249"><span class="linenos">249</span></a>        <span class="c1"># if (depth &gt; 0) and (is_cached or (resultTime &gt;= max_answer_time_in_seconds)):</span>
</span><span id="tag_db_interface-250"><a href="#tag_db_interface-250"><span class="linenos">250</span></a>        <span class="c1"># if (depth &gt; 0) and (resultTime &gt;= max_answer_time_in_seconds):</span>
</span><span id="tag_db_interface-251"><a href="#tag_db_interface-251"><span class="linenos">251</span></a>        <span class="k">if</span> <span class="n">depth</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="tag_db_interface-252"><a href="#tag_db_interface-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface-253"><a href="#tag_db_interface-253"><span class="linenos">253</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface-254"><a href="#tag_db_interface-254"><span class="linenos">254</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="tag_db_interface-255"><a href="#tag_db_interface-255"><span class="linenos">255</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="tag_db_interface-256"><a href="#tag_db_interface-256"><span class="linenos">256</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_web_cache</span><span class="p">(</span><span class="n">depth</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span><span id="tag_db_interface-257"><a href="#tag_db_interface-257"><span class="linenos">257</span></a>    
</span><span id="tag_db_interface-258"><a href="#tag_db_interface-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">clear_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface-259"><a href="#tag_db_interface-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface-260"><a href="#tag_db_interface-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="tag_db_interface-261"><a href="#tag_db_interface-261"><span class="linenos">261</span></a>    
</span><span id="tag_db_interface-262"><a href="#tag_db_interface-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="nf">web_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">return_is_cached_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">use_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="tag_db_interface-263"><a href="#tag_db_interface-263"><span class="linenos">263</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-264"><a href="#tag_db_interface-264"><span class="linenos">264</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-265"><a href="#tag_db_interface-265"><span class="linenos">265</span></a>            <span class="n">additional_tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-266"><a href="#tag_db_interface-266"><span class="linenos">266</span></a>            <span class="k">if</span> <span class="n">additional_tags</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-267"><a href="#tag_db_interface-267"><span class="linenos">267</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">additional_tags</span><span class="p">)</span>
</span><span id="tag_db_interface-268"><a href="#tag_db_interface-268"><span class="linenos">268</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface-269"><a href="#tag_db_interface-269"><span class="linenos">269</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="n">binTags</span>
</span><span id="tag_db_interface-270"><a href="#tag_db_interface-270"><span class="linenos">270</span></a>
</span><span id="tag_db_interface-271"><a href="#tag_db_interface-271"><span class="linenos">271</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">))</span>
</span><span id="tag_db_interface-272"><a href="#tag_db_interface-272"><span class="linenos">272</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface-273"><a href="#tag_db_interface-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="tag_db_interface-274"><a href="#tag_db_interface-274"><span class="linenos">274</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-275"><a href="#tag_db_interface-275"><span class="linenos">275</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="tag_db_interface-276"><a href="#tag_db_interface-276"><span class="linenos">276</span></a>            
</span><span id="tag_db_interface-277"><a href="#tag_db_interface-277"><span class="linenos">277</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-278"><a href="#tag_db_interface-278"><span class="linenos">278</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="tag_db_interface-279"><a href="#tag_db_interface-279"><span class="linenos">279</span></a>                <span class="n">items</span><span class="p">,</span> <span class="n">items_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">,</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="tag_db_interface-280"><a href="#tag_db_interface-280"><span class="linenos">280</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items_ids</span><span class="p">)</span>
</span><span id="tag_db_interface-281"><a href="#tag_db_interface-281"><span class="linenos">281</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="tag_db_interface-282"><a href="#tag_db_interface-282"><span class="linenos">282</span></a>                <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="tag_db_interface-283"><a href="#tag_db_interface-283"><span class="linenos">283</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-284"><a href="#tag_db_interface-284"><span class="linenos">284</span></a>
</span><span id="tag_db_interface-285"><a href="#tag_db_interface-285"><span class="linenos">285</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-286"><a href="#tag_db_interface-286"><span class="linenos">286</span></a>            <span class="k">if</span> <span class="n">return_is_cached_result</span><span class="p">:</span>
</span><span id="tag_db_interface-287"><a href="#tag_db_interface-287"><span class="linenos">287</span></a>                <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">is_cached_result</span>
</span><span id="tag_db_interface-288"><a href="#tag_db_interface-288"><span class="linenos">288</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface-289"><a href="#tag_db_interface-289"><span class="linenos">289</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="tag_db_interface-290"><a href="#tag_db_interface-290"><span class="linenos">290</span></a>    
</span><span id="tag_db_interface-291"><a href="#tag_db_interface-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">fs_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface-292"><a href="#tag_db_interface-292"><span class="linenos">292</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface-293"><a href="#tag_db_interface-293"><span class="linenos">293</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface-294"><a href="#tag_db_interface-294"><span class="linenos">294</span></a>
</span><span id="tag_db_interface-295"><a href="#tag_db_interface-295"><span class="linenos">295</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface-296"><a href="#tag_db_interface-296"><span class="linenos">296</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface-297"><a href="#tag_db_interface-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface-298"><a href="#tag_db_interface-298"><span class="linenos">298</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface-299"><a href="#tag_db_interface-299"><span class="linenos">299</span></a>                <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface-300"><a href="#tag_db_interface-300"><span class="linenos">300</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface-301"><a href="#tag_db_interface-301"><span class="linenos">301</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="tag_db_interface-302"><a href="#tag_db_interface-302"><span class="linenos">302</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-303"><a href="#tag_db_interface-303"><span class="linenos">303</span></a>
</span><span id="tag_db_interface-304"><a href="#tag_db_interface-304"><span class="linenos">304</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface-305"><a href="#tag_db_interface-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="tag_db_interface.__init__" class="classattr">
                                        <input id="tag_db_interface.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">tag_db_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="tag_db_interface.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.__init__-58"><a href="#tag_db_interface.__init__-58"><span class="linenos">58</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="tag_db_interface.__init__-59"><a href="#tag_db_interface.__init__-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="tag_db_interface.__init__-60"><a href="#tag_db_interface.__init__-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__db</span> <span class="o">=</span> <span class="n">TagDB</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface.__init__-61"><a href="#tag_db_interface.__init__-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">RequestCache</span><span class="p">(</span><span class="mi">300000</span><span class="p">,</span> <span class="n">default_priority</span><span class="o">=</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface.__init__-62"><a href="#tag_db_interface.__init__-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">lock_entity_id</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="tag_db_interface.__init__-63"><a href="#tag_db_interface.__init__-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_writers_in_progress</span>
</span><span id="tag_db_interface.__init__-64"><a href="#tag_db_interface.__init__-64"><span class="linenos">64</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">max_readers_in_progress</span>
</span><span id="tag_db_interface.__init__-65"><a href="#tag_db_interface.__init__-65"><span class="linenos">65</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-66"><a href="#tag_db_interface.__init__-66"><span class="linenos">66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-67"><a href="#tag_db_interface.__init__-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-68"><a href="#tag_db_interface.__init__-68"><span class="linenos">68</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-69"><a href="#tag_db_interface.__init__-69"><span class="linenos">69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="tag_db_interface.__init__-70"><a href="#tag_db_interface.__init__-70"><span class="linenos">70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-71"><a href="#tag_db_interface.__init__-71"><span class="linenos">71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.__init__-72"><a href="#tag_db_interface.__init__-72"><span class="linenos">72</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.default_priority" class="classattr">
                                <div class="attr variable">
            <span class="name">default_priority</span><span class="annotation">: cengal.parallel_execution.coroutines.coro_standard_services.loop_yield.versions.v_0.loop_yield.CoroPriority</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.default_priority"></a>
    
    

                            </div>
                            <div id="tag_db_interface.cache" class="classattr">
                                <div class="attr variable">
            <span class="name">cache</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.cache"></a>
    
    

                            </div>
                            <div id="tag_db_interface.lock_entity_id" class="classattr">
                                <div class="attr variable">
            <span class="name">lock_entity_id</span><span class="annotation">: Hashable</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.lock_entity_id"></a>
    
    

                            </div>
                            <div id="tag_db_interface.max_writers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">max_writers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.max_writers_in_progress"></a>
    
    

                            </div>
                            <div id="tag_db_interface.max_readers_in_progress" class="classattr">
                                <div class="attr variable">
            <span class="name">max_readers_in_progress</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.max_readers_in_progress"></a>
    
    

                            </div>
                            <div id="tag_db_interface.last_fill_cache_result_time" class="classattr">
                                <div class="attr variable">
            <span class="name">last_fill_cache_result_time</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.last_fill_cache_result_time"></a>
    
    

                            </div>
                            <div id="tag_db_interface.last_fill_cache_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">last_fill_cache_tags</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.last_fill_cache_tags"></a>
    
    

                            </div>
                            <div id="tag_db_interface.last_tested_fill_cache_result_time" class="classattr">
                                <div class="attr variable">
            <span class="name">last_tested_fill_cache_result_time</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.last_tested_fill_cache_result_time"></a>
    
    

                            </div>
                            <div id="tag_db_interface.last_tested_fill_cache_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">last_tested_fill_cache_tags</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.last_tested_fill_cache_tags"></a>
    
    

                            </div>
                            <div id="tag_db_interface.fill_cache_iterations" class="classattr">
                                <div class="attr variable">
            <span class="name">fill_cache_iterations</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.fill_cache_iterations"></a>
    
    

                            </div>
                            <div id="tag_db_interface.fill_cache_iterations_per_second" class="classattr">
                                <div class="attr variable">
            <span class="name">fill_cache_iterations_per_second</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.fill_cache_iterations_per_second"></a>
    
    

                            </div>
                            <div id="tag_db_interface.fill_cache_last_time_measurement" class="classattr">
                                <div class="attr variable">
            <span class="name">fill_cache_last_time_measurement</span><span class="annotation">: float</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.fill_cache_last_time_measurement"></a>
    
    

                            </div>
                            <div id="tag_db_interface.fill_cache_last_time_measurement_iterations" class="classattr">
                                <div class="attr variable">
            <span class="name">fill_cache_last_time_measurement_iterations</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#tag_db_interface.fill_cache_last_time_measurement_iterations"></a>
    
    

                            </div>
                            <div id="tag_db_interface.get_entity_stats" class="classattr">
                                        <input id="tag_db_interface.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="tag_db_interface.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_entity_stats-74"><a href="#tag_db_interface.get_entity_stats-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="tag_db_interface.get_entity_stats-75"><a href="#tag_db_interface.get_entity_stats-75"><span class="linenos">75</span></a>        <span class="n">tag_db_name</span><span class="p">,</span> <span class="n">tag_db_stats</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_entity_stats</span><span class="p">(</span><span class="n">stats_level</span><span class="p">)</span>
</span><span id="tag_db_interface.get_entity_stats-76"><a href="#tag_db_interface.get_entity_stats-76"><span class="linenos">76</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="tag_db_interface.get_entity_stats-77"><a href="#tag_db_interface.get_entity_stats-77"><span class="linenos">77</span></a>            <span class="s1">&#39;interface&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="tag_db_interface.get_entity_stats-78"><a href="#tag_db_interface.get_entity_stats-78"><span class="linenos">78</span></a>                <span class="s1">&#39;cache size&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">_requestsAndData</span><span class="p">),</span>
</span><span id="tag_db_interface.get_entity_stats-79"><a href="#tag_db_interface.get_entity_stats-79"><span class="linenos">79</span></a>                <span class="s1">&#39;last fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-80"><a href="#tag_db_interface.get_entity_stats-80"><span class="linenos">80</span></a>                <span class="s1">&#39;last fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-81"><a href="#tag_db_interface.get_entity_stats-81"><span class="linenos">81</span></a>                <span class="s1">&#39;last tested fill cache result time&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-82"><a href="#tag_db_interface.get_entity_stats-82"><span class="linenos">82</span></a>                <span class="s1">&#39;last tested fill cache tags&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-83"><a href="#tag_db_interface.get_entity_stats-83"><span class="linenos">83</span></a>                <span class="s1">&#39;fill cache iterations&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-84"><a href="#tag_db_interface.get_entity_stats-84"><span class="linenos">84</span></a>                <span class="s1">&#39;fill cache iterations per second&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-85"><a href="#tag_db_interface.get_entity_stats-85"><span class="linenos">85</span></a>            <span class="p">},</span>
</span><span id="tag_db_interface.get_entity_stats-86"><a href="#tag_db_interface.get_entity_stats-86"><span class="linenos">86</span></a>            <span class="s1">&#39;db&#39;</span><span class="p">:</span> <span class="p">{</span>
</span><span id="tag_db_interface.get_entity_stats-87"><a href="#tag_db_interface.get_entity_stats-87"><span class="linenos">87</span></a>                <span class="n">tag_db_name</span><span class="p">:</span> <span class="n">tag_db_stats</span><span class="p">,</span>
</span><span id="tag_db_interface.get_entity_stats-88"><a href="#tag_db_interface.get_entity_stats-88"><span class="linenos">88</span></a>            <span class="p">}</span>
</span><span id="tag_db_interface.get_entity_stats-89"><a href="#tag_db_interface.get_entity_stats-89"><span class="linenos">89</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.get_db" class="classattr">
                                        <input id="tag_db_interface.get_db-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_db</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.get_db-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_db"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_db-100"><a href="#tag_db_interface.get_db-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">get_db</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface.get_db-101"><a href="#tag_db_interface.get_db-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.new_empty" class="classattr">
                                        <input id="tag_db_interface.new_empty-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">new_empty</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#tag_db_interface">tag_db_interface</a></span>:</span></span>

                <label class="view-source-button" for="tag_db_interface.new_empty-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.new_empty"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.new_empty-103"><a href="#tag_db_interface.new_empty-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">new_empty</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;tag_db_interface&#39;</span><span class="p">:</span>
</span><span id="tag_db_interface.new_empty-104"><a href="#tag_db_interface.new_empty-104"><span class="linenos">104</span></a>        <span class="k">return</span> <span class="n">tag_db_interface</span><span class="p">(</span>
</span><span id="tag_db_interface.new_empty-105"><a href="#tag_db_interface.new_empty-105"><span class="linenos">105</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_writers_in_progress</span><span class="p">,</span>
</span><span id="tag_db_interface.new_empty-106"><a href="#tag_db_interface.new_empty-106"><span class="linenos">106</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">max_readers_in_progress</span><span class="p">,</span>
</span><span id="tag_db_interface.new_empty-107"><a href="#tag_db_interface.new_empty-107"><span class="linenos">107</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">lock_entity_id</span><span class="p">,</span>
</span><span id="tag_db_interface.new_empty-108"><a href="#tag_db_interface.new_empty-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span>
</span><span id="tag_db_interface.new_empty-109"><a href="#tag_db_interface.new_empty-109"><span class="linenos">109</span></a>            <span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.add_item" class="classattr">
                                        <input id="tag_db_interface.add_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binItem</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.add_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.add_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.add_item-111"><a href="#tag_db_interface.add_item-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface.add_item-112"><a href="#tag_db_interface.add_item-112"><span class="linenos">112</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="tag_db_interface.add_item-113"><a href="#tag_db_interface.add_item-113"><span class="linenos">113</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface.add_item-114"><a href="#tag_db_interface.add_item-114"><span class="linenos">114</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.add_item-115"><a href="#tag_db_interface.add_item-115"><span class="linenos">115</span></a>
</span><span id="tag_db_interface.add_item-116"><a href="#tag_db_interface.add_item-116"><span class="linenos">116</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">add_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.add_item-117"><a href="#tag_db_interface.add_item-117"><span class="linenos">117</span></a>
</span><span id="tag_db_interface.add_item-118"><a href="#tag_db_interface.add_item-118"><span class="linenos">118</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.add_item-119"><a href="#tag_db_interface.add_item-119"><span class="linenos">119</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface.add_item-120"><a href="#tag_db_interface.add_item-120"><span class="linenos">120</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.remove_item" class="classattr">
                                        <input id="tag_db_interface.remove_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">binItem</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.remove_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.remove_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.remove_item-122"><a href="#tag_db_interface.remove_item-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="tag_db_interface.remove_item-123"><a href="#tag_db_interface.remove_item-123"><span class="linenos">123</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wlock</span><span class="p">():</span>
</span><span id="tag_db_interface.remove_item-124"><a href="#tag_db_interface.remove_item-124"><span class="linenos">124</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.remove_item-125"><a href="#tag_db_interface.remove_item-125"><span class="linenos">125</span></a>            <span class="n">binItem</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface.remove_item-126"><a href="#tag_db_interface.remove_item-126"><span class="linenos">126</span></a>
</span><span id="tag_db_interface.remove_item-127"><a href="#tag_db_interface.remove_item-127"><span class="linenos">127</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">remove_item</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="tag_db_interface.remove_item-128"><a href="#tag_db_interface.remove_item-128"><span class="linenos">128</span></a>
</span><span id="tag_db_interface.remove_item-129"><a href="#tag_db_interface.remove_item-129"><span class="linenos">129</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.remove_item-130"><a href="#tag_db_interface.remove_item-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface.remove_item-131"><a href="#tag_db_interface.remove_item-131"><span class="linenos">131</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.get_items" class="classattr">
                                        <input id="tag_db_interface.get_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_items</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">treeType</span><span class="o">=</span><span class="mi">3</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.get_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_items-133"><a href="#tag_db_interface.get_items-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">get_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface.get_items-134"><a href="#tag_db_interface.get_items-134"><span class="linenos">134</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.get_items-135"><a href="#tag_db_interface.get_items-135"><span class="linenos">135</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-136"><a href="#tag_db_interface.get_items-136"><span class="linenos">136</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-137"><a href="#tag_db_interface.get_items-137"><span class="linenos">137</span></a>
</span><span id="tag_db_interface.get_items-138"><a href="#tag_db_interface.get_items-138"><span class="linenos">138</span></a>            <span class="c1"># request = (&#39;get_items&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface.get_items-139"><a href="#tag_db_interface.get_items-139"><span class="linenos">139</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_items&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-140"><a href="#tag_db_interface.get_items-140"><span class="linenos">140</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-141"><a href="#tag_db_interface.get_items-141"><span class="linenos">141</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.get_items-142"><a href="#tag_db_interface.get_items-142"><span class="linenos">142</span></a>                
</span><span id="tag_db_interface.get_items-143"><a href="#tag_db_interface.get_items-143"><span class="linenos">143</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-144"><a href="#tag_db_interface.get_items-144"><span class="linenos">144</span></a>
</span><span id="tag_db_interface.get_items-145"><a href="#tag_db_interface.get_items-145"><span class="linenos">145</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_items-146"><a href="#tag_db_interface.get_items-146"><span class="linenos">146</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.get_tags" class="classattr">
                                        <input id="tag_db_interface.get_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tags</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">treeType</span><span class="o">=</span><span class="mi">3</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.get_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_tags-148"><a href="#tag_db_interface.get_tags-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">get_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface.get_tags-149"><a href="#tag_db_interface.get_tags-149"><span class="linenos">149</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.get_tags-150"><a href="#tag_db_interface.get_tags-150"><span class="linenos">150</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-151"><a href="#tag_db_interface.get_tags-151"><span class="linenos">151</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-152"><a href="#tag_db_interface.get_tags-152"><span class="linenos">152</span></a>
</span><span id="tag_db_interface.get_tags-153"><a href="#tag_db_interface.get_tags-153"><span class="linenos">153</span></a>            <span class="c1"># request = (&#39;get_tags&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface.get_tags-154"><a href="#tag_db_interface.get_tags-154"><span class="linenos">154</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_tags&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-155"><a href="#tag_db_interface.get_tags-155"><span class="linenos">155</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-156"><a href="#tag_db_interface.get_tags-156"><span class="linenos">156</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.get_tags-157"><a href="#tag_db_interface.get_tags-157"><span class="linenos">157</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-158"><a href="#tag_db_interface.get_tags-158"><span class="linenos">158</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-159"><a href="#tag_db_interface.get_tags-159"><span class="linenos">159</span></a>
</span><span id="tag_db_interface.get_tags-160"><a href="#tag_db_interface.get_tags-160"><span class="linenos">160</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags-161"><a href="#tag_db_interface.get_tags-161"><span class="linenos">161</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.get_all" class="classattr">
                                        <input id="tag_db_interface.get_all-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_all</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">treeType</span><span class="o">=</span><span class="mi">3</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.get_all-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_all"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_all-163"><a href="#tag_db_interface.get_all-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">get_all</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="tag_db_interface.get_all-164"><a href="#tag_db_interface.get_all-164"><span class="linenos">164</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.get_all-165"><a href="#tag_db_interface.get_all-165"><span class="linenos">165</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-166"><a href="#tag_db_interface.get_all-166"><span class="linenos">166</span></a>            <span class="n">treeType</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-167"><a href="#tag_db_interface.get_all-167"><span class="linenos">167</span></a>
</span><span id="tag_db_interface.get_all-168"><a href="#tag_db_interface.get_all-168"><span class="linenos">168</span></a>            <span class="c1"># request = (&#39;get_all&#39;, tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)</span>
</span><span id="tag_db_interface.get_all-169"><a href="#tag_db_interface.get_all-169"><span class="linenos">169</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;get_all&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">),</span> <span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-170"><a href="#tag_db_interface.get_all-170"><span class="linenos">170</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-171"><a href="#tag_db_interface.get_all-171"><span class="linenos">171</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.get_all-172"><a href="#tag_db_interface.get_all-172"><span class="linenos">172</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_all_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-173"><a href="#tag_db_interface.get_all-173"><span class="linenos">173</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-174"><a href="#tag_db_interface.get_all-174"><span class="linenos">174</span></a>
</span><span id="tag_db_interface.get_all-175"><a href="#tag_db_interface.get_all-175"><span class="linenos">175</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_all-176"><a href="#tag_db_interface.get_all-176"><span class="linenos">176</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.get_tags_for_a_smart_redirection" class="classattr">
                                        <input id="tag_db_interface.get_tags_for_a_smart_redirection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tags_for_a_smart_redirection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.get_tags_for_a_smart_redirection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.get_tags_for_a_smart_redirection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.get_tags_for_a_smart_redirection-178"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-179"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-179"><span class="linenos">179</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-180"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-180"><span class="linenos">180</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-181"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-181"><span class="linenos">181</span></a>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-182"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-182"><span class="linenos">182</span></a>            <span class="c1"># request = (&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-183"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-183"><span class="linenos">183</span></a>            <span class="c1">#            , tuple(self.__db.sort_tag_list_by_hash(binTags)))</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-184"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-184"><span class="linenos">184</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;is_smart_redirection_for_a_tag_path_reduction_needed&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-185"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-185"><span class="linenos">185</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-186"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-186"><span class="linenos">186</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-187"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-187"><span class="linenos">187</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-188"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-188"><span class="linenos">188</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-189"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-189"><span class="linenos">189</span></a>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-190"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-190"><span class="linenos">190</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.get_tags_for_a_smart_redirection-191"><a href="#tag_db_interface.get_tags_for_a_smart_redirection-191"><span class="linenos">191</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.fill_cache" class="classattr">
                                        <input id="tag_db_interface.fill_cache-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fill_cache</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span>, </span><span class="param"><span class="n">path</span><span class="o">=</span><span class="p">[]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.fill_cache-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.fill_cache"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.fill_cache-193"><a href="#tag_db_interface.fill_cache-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">fill_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="nb">list</span><span class="p">()):</span>
</span><span id="tag_db_interface.fill_cache-194"><a href="#tag_db_interface.fill_cache-194"><span class="linenos">194</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_cache-195"><a href="#tag_db_interface.fill_cache-195"><span class="linenos">195</span></a>        
</span><span id="tag_db_interface.fill_cache-196"><a href="#tag_db_interface.fill_cache-196"><span class="linenos">196</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_cache-197"><a href="#tag_db_interface.fill_cache-197"><span class="linenos">197</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_cache-198"><a href="#tag_db_interface.fill_cache-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface.fill_cache-199"><a href="#tag_db_interface.fill_cache-199"><span class="linenos">199</span></a>
</span><span id="tag_db_interface.fill_cache-200"><a href="#tag_db_interface.fill_cache-200"><span class="linenos">200</span></a>        <span class="n">tags_and_items_inside_curent_path</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_all</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_cache-201"><a href="#tag_db_interface.fill_cache-201"><span class="linenos">201</span></a>        <span class="n">internal_tags</span> <span class="o">=</span> <span class="n">tags_and_items_inside_curent_path</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="tag_db_interface.fill_cache-202"><a href="#tag_db_interface.fill_cache-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">get_items</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_cache-203"><a href="#tag_db_interface.fill_cache-203"><span class="linenos">203</span></a>        
</span><span id="tag_db_interface.fill_cache-204"><a href="#tag_db_interface.fill_cache-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="tag_db_interface.fill_cache-205"><a href="#tag_db_interface.fill_cache-205"><span class="linenos">205</span></a>
</span><span id="tag_db_interface.fill_cache-206"><a href="#tag_db_interface.fill_cache-206"><span class="linenos">206</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_cache-207"><a href="#tag_db_interface.fill_cache-207"><span class="linenos">207</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="tag_db_interface.fill_cache-208"><a href="#tag_db_interface.fill_cache-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface.fill_cache-209"><a href="#tag_db_interface.fill_cache-209"><span class="linenos">209</span></a>        <span class="k">if</span> <span class="n">resultTime</span> <span class="o">&gt;=</span> <span class="n">max_answer_time_in_seconds</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_cache-210"><a href="#tag_db_interface.fill_cache-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface.fill_cache-211"><a href="#tag_db_interface.fill_cache-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface.fill_cache-212"><a href="#tag_db_interface.fill_cache-212"><span class="linenos">212</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">internal_tags</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_cache-213"><a href="#tag_db_interface.fill_cache-213"><span class="linenos">213</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_cache-214"><a href="#tag_db_interface.fill_cache-214"><span class="linenos">214</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="tag_db_interface.fill_cache-215"><a href="#tag_db_interface.fill_cache-215"><span class="linenos">215</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache</span><span class="p">(</span><span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.fill_web_cache" class="classattr">
                                        <input id="tag_db_interface.fill_web_cache-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fill_web_cache</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span>, </span><span class="param"><span class="n">path</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.fill_web_cache-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.fill_web_cache"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.fill_web_cache-217"><a href="#tag_db_interface.fill_web_cache-217"><span class="linenos">217</span></a>    <span class="k">def</span> <span class="nf">fill_web_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="tag_db_interface.fill_web_cache-218"><a href="#tag_db_interface.fill_web_cache-218"><span class="linenos">218</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_web_cache-219"><a href="#tag_db_interface.fill_web_cache-219"><span class="linenos">219</span></a>        <span class="n">ly</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-220"><a href="#tag_db_interface.fill_web_cache-220"><span class="linenos">220</span></a>
</span><span id="tag_db_interface.fill_web_cache-221"><a href="#tag_db_interface.fill_web_cache-221"><span class="linenos">221</span></a>        <span class="n">path</span> <span class="o">=</span> <span class="n">path</span> <span class="ow">or</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-222"><a href="#tag_db_interface.fill_web_cache-222"><span class="linenos">222</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_web_cache-223"><a href="#tag_db_interface.fill_web_cache-223"><span class="linenos">223</span></a>        <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-224"><a href="#tag_db_interface.fill_web_cache-224"><span class="linenos">224</span></a>
</span><span id="tag_db_interface.fill_web_cache-225"><a href="#tag_db_interface.fill_web_cache-225"><span class="linenos">225</span></a>        <span class="n">result</span><span class="p">,</span> <span class="n">is_cached</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">web_browse_to</span><span class="p">(</span><span class="n">current_path</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_web_cache-226"><a href="#tag_db_interface.fill_web_cache-226"><span class="linenos">226</span></a>        <span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="tag_db_interface.fill_web_cache-227"><a href="#tag_db_interface.fill_web_cache-227"><span class="linenos">227</span></a>        <span class="n">current_path</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">)</span>
</span><span id="tag_db_interface.fill_web_cache-228"><a href="#tag_db_interface.fill_web_cache-228"><span class="linenos">228</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface.fill_web_cache-229"><a href="#tag_db_interface.fill_web_cache-229"><span class="linenos">229</span></a>        
</span><span id="tag_db_interface.fill_web_cache-230"><a href="#tag_db_interface.fill_web_cache-230"><span class="linenos">230</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="tag_db_interface.fill_web_cache-231"><a href="#tag_db_interface.fill_web_cache-231"><span class="linenos">231</span></a>        <span class="n">depth</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="tag_db_interface.fill_web_cache-232"><a href="#tag_db_interface.fill_web_cache-232"><span class="linenos">232</span></a>        
</span><span id="tag_db_interface.fill_web_cache-233"><a href="#tag_db_interface.fill_web_cache-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-234"><a href="#tag_db_interface.fill_web_cache-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="tag_db_interface.fill_web_cache-235"><a href="#tag_db_interface.fill_web_cache-235"><span class="linenos">235</span></a>        
</span><span id="tag_db_interface.fill_web_cache-236"><a href="#tag_db_interface.fill_web_cache-236"><span class="linenos">236</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-237"><a href="#tag_db_interface.fill_web_cache-237"><span class="linenos">237</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-238"><a href="#tag_db_interface.fill_web_cache-238"><span class="linenos">238</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-239"><a href="#tag_db_interface.fill_web_cache-239"><span class="linenos">239</span></a>            <span class="n">dtime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span>
</span><span id="tag_db_interface.fill_web_cache-240"><a href="#tag_db_interface.fill_web_cache-240"><span class="linenos">240</span></a>            <span class="k">if</span> <span class="n">dtime</span> <span class="o">&gt;=</span> <span class="mf">1.0</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-241"><a href="#tag_db_interface.fill_web_cache-241"><span class="linenos">241</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-242"><a href="#tag_db_interface.fill_web_cache-242"><span class="linenos">242</span></a>                <span class="n">iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span>
</span><span id="tag_db_interface.fill_web_cache-243"><a href="#tag_db_interface.fill_web_cache-243"><span class="linenos">243</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations_per_second</span> <span class="o">=</span> <span class="n">iterations</span> <span class="o">/</span> <span class="n">dtime</span>
</span><span id="tag_db_interface.fill_web_cache-244"><a href="#tag_db_interface.fill_web_cache-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_last_time_measurement_iterations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span>
</span><span id="tag_db_interface.fill_web_cache-245"><a href="#tag_db_interface.fill_web_cache-245"><span class="linenos">245</span></a>
</span><span id="tag_db_interface.fill_web_cache-246"><a href="#tag_db_interface.fill_web_cache-246"><span class="linenos">246</span></a>        <span class="n">endTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">perf_counter</span><span class="p">()</span>
</span><span id="tag_db_interface.fill_web_cache-247"><a href="#tag_db_interface.fill_web_cache-247"><span class="linenos">247</span></a>        <span class="n">resultTime</span> <span class="o">=</span> <span class="n">endTime</span> <span class="o">-</span> <span class="n">startTime</span>
</span><span id="tag_db_interface.fill_web_cache-248"><a href="#tag_db_interface.fill_web_cache-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">last_tested_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface.fill_web_cache-249"><a href="#tag_db_interface.fill_web_cache-249"><span class="linenos">249</span></a>        <span class="c1"># if (depth &gt; 0) and (is_cached or (resultTime &gt;= max_answer_time_in_seconds)):</span>
</span><span id="tag_db_interface.fill_web_cache-250"><a href="#tag_db_interface.fill_web_cache-250"><span class="linenos">250</span></a>        <span class="c1"># if (depth &gt; 0) and (resultTime &gt;= max_answer_time_in_seconds):</span>
</span><span id="tag_db_interface.fill_web_cache-251"><a href="#tag_db_interface.fill_web_cache-251"><span class="linenos">251</span></a>        <span class="k">if</span> <span class="n">depth</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-252"><a href="#tag_db_interface.fill_web_cache-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_tags</span> <span class="o">=</span> <span class="n">current_path</span>
</span><span id="tag_db_interface.fill_web_cache-253"><a href="#tag_db_interface.fill_web_cache-253"><span class="linenos">253</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">last_fill_cache_result_time</span> <span class="o">=</span> <span class="n">resultTime</span>
</span><span id="tag_db_interface.fill_web_cache-254"><a href="#tag_db_interface.fill_web_cache-254"><span class="linenos">254</span></a>            <span class="k">for</span> <span class="n">additional_tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="tag_db_interface.fill_web_cache-255"><a href="#tag_db_interface.fill_web_cache-255"><span class="linenos">255</span></a>                <span class="n">new_path</span> <span class="o">=</span> <span class="n">current_path</span> <span class="o">+</span> <span class="p">[</span><span class="n">additional_tag</span><span class="p">]</span>
</span><span id="tag_db_interface.fill_web_cache-256"><a href="#tag_db_interface.fill_web_cache-256"><span class="linenos">256</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">fill_web_cache</span><span class="p">(</span><span class="n">depth</span><span class="p">,</span> <span class="n">max_answer_time_in_seconds</span><span class="p">,</span> <span class="n">new_path</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.clear_cache" class="classattr">
                                        <input id="tag_db_interface.clear_cache-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear_cache</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.clear_cache-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.clear_cache"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.clear_cache-258"><a href="#tag_db_interface.clear_cache-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">clear_cache</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="tag_db_interface.clear_cache-259"><a href="#tag_db_interface.clear_cache-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="tag_db_interface.clear_cache-260"><a href="#tag_db_interface.clear_cache-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">fill_cache_iterations</span> <span class="o">=</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.web_browse_to" class="classattr">
                                        <input id="tag_db_interface.web_browse_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">web_browse_to</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">binTags</span>,</span><span class="param">	<span class="n">return_is_cached_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>,</span><span class="param">	<span class="n">use_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.web_browse_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.web_browse_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.web_browse_to-262"><a href="#tag_db_interface.web_browse_to-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="nf">web_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">return_is_cached_result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">use_cache</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="tag_db_interface.web_browse_to-263"><a href="#tag_db_interface.web_browse_to-263"><span class="linenos">263</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.web_browse_to-264"><a href="#tag_db_interface.web_browse_to-264"><span class="linenos">264</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-265"><a href="#tag_db_interface.web_browse_to-265"><span class="linenos">265</span></a>            <span class="n">additional_tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-266"><a href="#tag_db_interface.web_browse_to-266"><span class="linenos">266</span></a>            <span class="k">if</span> <span class="n">additional_tags</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-267"><a href="#tag_db_interface.web_browse_to-267"><span class="linenos">267</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">additional_tags</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-268"><a href="#tag_db_interface.web_browse_to-268"><span class="linenos">268</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-269"><a href="#tag_db_interface.web_browse_to-269"><span class="linenos">269</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="n">binTags</span>
</span><span id="tag_db_interface.web_browse_to-270"><a href="#tag_db_interface.web_browse_to-270"><span class="linenos">270</span></a>
</span><span id="tag_db_interface.web_browse_to-271"><a href="#tag_db_interface.web_browse_to-271"><span class="linenos">271</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">))</span>
</span><span id="tag_db_interface.web_browse_to-272"><a href="#tag_db_interface.web_browse_to-272"><span class="linenos">272</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="tag_db_interface.web_browse_to-273"><a href="#tag_db_interface.web_browse_to-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-274"><a href="#tag_db_interface.web_browse_to-274"><span class="linenos">274</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-275"><a href="#tag_db_interface.web_browse_to-275"><span class="linenos">275</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="tag_db_interface.web_browse_to-276"><a href="#tag_db_interface.web_browse_to-276"><span class="linenos">276</span></a>            
</span><span id="tag_db_interface.web_browse_to-277"><a href="#tag_db_interface.web_browse_to-277"><span class="linenos">277</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-278"><a href="#tag_db_interface.web_browse_to-278"><span class="linenos">278</span></a>                <span class="n">is_cached_result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="tag_db_interface.web_browse_to-279"><a href="#tag_db_interface.web_browse_to-279"><span class="linenos">279</span></a>                <span class="n">items</span><span class="p">,</span> <span class="n">items_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">,</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-280"><a href="#tag_db_interface.web_browse_to-280"><span class="linenos">280</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items_ids</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-281"><a href="#tag_db_interface.web_browse_to-281"><span class="linenos">281</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-282"><a href="#tag_db_interface.web_browse_to-282"><span class="linenos">282</span></a>                <span class="k">if</span> <span class="n">use_cache</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-283"><a href="#tag_db_interface.web_browse_to-283"><span class="linenos">283</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-284"><a href="#tag_db_interface.web_browse_to-284"><span class="linenos">284</span></a>
</span><span id="tag_db_interface.web_browse_to-285"><a href="#tag_db_interface.web_browse_to-285"><span class="linenos">285</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.web_browse_to-286"><a href="#tag_db_interface.web_browse_to-286"><span class="linenos">286</span></a>            <span class="k">if</span> <span class="n">return_is_cached_result</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-287"><a href="#tag_db_interface.web_browse_to-287"><span class="linenos">287</span></a>                <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">is_cached_result</span>
</span><span id="tag_db_interface.web_browse_to-288"><a href="#tag_db_interface.web_browse_to-288"><span class="linenos">288</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="tag_db_interface.web_browse_to-289"><a href="#tag_db_interface.web_browse_to-289"><span class="linenos">289</span></a>                <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="tag_db_interface.fs_browse_to" class="classattr">
                                        <input id="tag_db_interface.fs_browse_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fs_browse_to</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="tag_db_interface.fs_browse_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tag_db_interface.fs_browse_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tag_db_interface.fs_browse_to-291"><a href="#tag_db_interface.fs_browse_to-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">fs_browse_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="tag_db_interface.fs_browse_to-292"><a href="#tag_db_interface.fs_browse_to-292"><span class="linenos">292</span></a>        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_rlock</span><span class="p">():</span>
</span><span id="tag_db_interface.fs_browse_to-293"><a href="#tag_db_interface.fs_browse_to-293"><span class="linenos">293</span></a>            <span class="n">binTags</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-294"><a href="#tag_db_interface.fs_browse_to-294"><span class="linenos">294</span></a>
</span><span id="tag_db_interface.fs_browse_to-295"><a href="#tag_db_interface.fs_browse_to-295"><span class="linenos">295</span></a>            <span class="n">request</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;web_browse_to&#39;</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface.fs_browse_to-296"><a href="#tag_db_interface.fs_browse_to-296"><span class="linenos">296</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">try_to_get_data_for_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-297"><a href="#tag_db_interface.fs_browse_to-297"><span class="linenos">297</span></a>            <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="tag_db_interface.fs_browse_to-298"><a href="#tag_db_interface.fs_browse_to-298"><span class="linenos">298</span></a>                <span class="n">optimized_path</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="n">binTags</span><span class="p">))</span>
</span><span id="tag_db_interface.fs_browse_to-299"><a href="#tag_db_interface.fs_browse_to-299"><span class="linenos">299</span></a>                <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-300"><a href="#tag_db_interface.fs_browse_to-300"><span class="linenos">300</span></a>                <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__db</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">SMART_TREE_TYPE</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-301"><a href="#tag_db_interface.fs_browse_to-301"><span class="linenos">301</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">optimized_path</span><span class="p">,</span> <span class="n">tags</span><span class="p">,</span> <span class="n">items</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-302"><a href="#tag_db_interface.fs_browse_to-302"><span class="linenos">302</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="o">.</span><span class="n">put_new_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-303"><a href="#tag_db_interface.fs_browse_to-303"><span class="linenos">303</span></a>
</span><span id="tag_db_interface.fs_browse_to-304"><a href="#tag_db_interface.fs_browse_to-304"><span class="linenos">304</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="tag_db_interface.fs_browse_to-305"><a href="#tag_db_interface.fs_browse_to-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="tag_db_interface.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SMART_TREE_TYPE">
                    <div class="attr variable">
            <span class="name">SMART_TREE_TYPE</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#SMART_TREE_TYPE"></a>
    
    

                </section>
                <section id="SMART_TREE_TYPE_WITH_INTERNAL_MENU">
                    <div class="attr variable">
            <span class="name">SMART_TREE_TYPE_WITH_INTERNAL_MENU</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#SMART_TREE_TYPE_WITH_INTERNAL_MENU"></a>
    
    

                </section>
                <section id="FULL_TREE_TYPE">
                    <div class="attr variable">
            <span class="name">FULL_TREE_TYPE</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#FULL_TREE_TYPE"></a>
    
    

                </section>
                <section id="PLAIN_PSEUDO_TREE_TYPE">
                    <div class="attr variable">
            <span class="name">PLAIN_PSEUDO_TREE_TYPE</span>        =
<span class="default_value">3</span>

        
    </div>
    <a class="headerlink" href="#PLAIN_PSEUDO_TREE_TYPE"></a>
    
    

                </section>
                <section id="USUAL_TREE_TYPE">
                    <div class="attr variable">
            <span class="name">USUAL_TREE_TYPE</span>        =
<span class="default_value">3</span>

        
    </div>
    <a class="headerlink" href="#USUAL_TREE_TYPE"></a>
    
    

                </section>
                <section id="ToManyIdenticalItemsOnTheGivenTagPathError">
                            <input id="ToManyIdenticalItemsOnTheGivenTagPathError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ToManyIdenticalItemsOnTheGivenTagPathError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="ToManyIdenticalItemsOnTheGivenTagPathError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ToManyIdenticalItemsOnTheGivenTagPathError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ToManyIdenticalItemsOnTheGivenTagPathError-67"><a href="#ToManyIdenticalItemsOnTheGivenTagPathError-67"><span class="linenos">67</span></a><span class="k">class</span> <span class="nc">ToManyIdenticalItemsOnTheGivenTagPathError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="ToManyIdenticalItemsOnTheGivenTagPathError-68"><a href="#ToManyIdenticalItemsOnTheGivenTagPathError-68"><span class="linenos">68</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="ToManyIdenticalItemsOnTheGivenTagPathError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ToManyIdenticalItemsOnTheGivenTagPathError.with_traceback" class="function">with_traceback</dd>
                <dd id="ToManyIdenticalItemsOnTheGivenTagPathError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UnknownTreeTypeError">
                            <input id="UnknownTreeTypeError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnknownTreeTypeError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="UnknownTreeTypeError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnknownTreeTypeError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnknownTreeTypeError-71"><a href="#UnknownTreeTypeError-71"><span class="linenos">71</span></a><span class="k">class</span> <span class="nc">UnknownTreeTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="UnknownTreeTypeError-72"><a href="#UnknownTreeTypeError-72"><span class="linenos">72</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="UnknownTreeTypeError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnknownTreeTypeError.with_traceback" class="function">with_traceback</dd>
                <dd id="UnknownTreeTypeError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>