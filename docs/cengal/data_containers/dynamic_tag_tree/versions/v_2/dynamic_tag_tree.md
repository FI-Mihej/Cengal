---
title: dynamic_tag_tree
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_containers<wbr>.dynamic_tag_tree<wbr>.versions<wbr>.v_2<wbr>.dynamic_tag_tree    </h1>

                
                        <input id="mod-dynamic_tag_tree-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-dynamic_tag_tree-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">,</span> <span class="n">Callable</span>
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
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="n">ItemID</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">TagID</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">UniqueItemID</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">UniqueIdGen</span><span class="p">:</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="k">def</span> <span class="nf">tags_set_2_tuple</span><span class="p">(</span><span class="n">tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="n">tags_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="n">tags_list</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">tags_list</span><span class="p">)</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="k">def</span> <span class="nf">default_growth_during_the_search_checker</span><span class="p">():</span> <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="k">def</span> <span class="nf">default_scheduler</span><span class="p">():</span> <span class="k">pass</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="k">class</span> <span class="nc">TagNotFound</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">pass</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">DynamicTagTree</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>                 <span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>                 <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> \
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>            <span class="n">growth_during_the_search_is_allowed</span> <span class="ow">or</span> <span class="n">default_growth_during_the_search_checker</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span> <span class="o">=</span> <span class="n">UniqueIdGen</span><span class="p">()</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]],</span> <span class="n">UniqueItemID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">ItemID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="c1"># self.tags_by_number_of_tags_by_tag: Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]] = dict()</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tag; value: keyb  from self.tags_by_number_of_tags</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]]]</span> <span class="o">=</span> \
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, Dict[len of tags set, Set[tag sets]]]]</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> \
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, len of tags set]]</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: interested tags set;</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="c1"># value: bigger tags sets which includes interested tags set</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tag_weight_by_tag_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_tag_weight_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: any</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="c1"># interested tags set (input from user); value: set of known tags sets which has an item(-s) and includes given</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="c1"># interested tags set</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tags; value: same tags object</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">set_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">def</span> <span class="nf">get_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">UniqueItemID</span><span class="p">:</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span><span class="p">()</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="n">item</span> <span class="o">=</span> <span class="p">(</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="n">tags_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">[</span><span class="n">unique_item_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span> <span class="o">=</span> <span class="n">unique_item_id</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="c1"># self.item_tags_by_tag</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>            
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>            <span class="c1"># self.neighbor_tags_of_a_tag</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tags</span> <span class="o">-</span> <span class="n">tag</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>            
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>            <span class="c1"># self.set_of_tags</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="c1"># self.direct_items_by_tags</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">item_id</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="c1"># self.tags_by_number_of_tags</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">if</span> <span class="n">tags_len</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="c1"># self.tags_len_by_tag</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="n">tags_len</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">]:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="o">.</span><span class="n">get</span><span class="p">((</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]:</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">unique_item_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">):</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="k">pass</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="k">def</span> <span class="nf">list_direct_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="k">pass</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">list_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">pass</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="nf">list_direct_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">pass</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">def</span> <span class="nf">list_all_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="k">pass</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="nf">get_nearest_non_empty_tags_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_gen_nearest_non_empty_tags_by_some_tags</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_normalise_tags</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_check_tags</span><span class="p">(</span><span class="n">tags</span><span class="p">)))</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">_gen_nearest_non_empty_tags_by_some_tags</span><span class="p">(</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">is_search_request</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]:</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">[</span><span class="n">tags</span><span class="p">])</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="n">nearest_non_empty_tags_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="n">inclusion_tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="n">min_tags_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">inclusion_tags</span><span class="p">))</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="k">for</span> <span class="n">tags2</span> <span class="ow">in</span> <span class="n">inclusion_tags</span><span class="p">:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags2</span><span class="p">)</span> <span class="o">==</span> <span class="n">min_tags_len</span><span class="p">:</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>                    <span class="n">nearest_non_empty_tags_set</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags2</span><span class="p">)</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="n">minimal_nearest_non_empty_tags_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="n">tags_by_number_of_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>                <span class="n">lookup1</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]]</span> <span class="o">=</span> \
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">near_tags_by_number_of_tags_by_tag_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                <span class="k">for</span> <span class="n">tag2</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                    <span class="k">if</span> <span class="n">tag</span> <span class="o">==</span> <span class="n">tag2</span><span class="p">:</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>                        <span class="k">continue</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>                    <span class="k">if</span> <span class="n">tag2</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">lookup1</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>                        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>                    <span class="n">lookup2</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">lookup1</span><span class="p">[</span><span class="n">tag2</span><span class="p">]</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>                    <span class="n">sorted_tags_sizes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">lookup2</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>                    <span class="k">for</span> <span class="n">tags_size</span> <span class="ow">in</span> <span class="n">sorted_tags_sizes</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>                        <span class="k">if</span> <span class="n">tags_size</span> <span class="o">&lt;</span> <span class="n">minimal_nearest_non_empty_tags_size</span><span class="p">:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>                            <span class="k">continue</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>                        <span class="n">lookup3</span> <span class="o">=</span> <span class="n">lookup2</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>                        <span class="k">for</span> <span class="n">another_tags</span> <span class="ow">in</span> <span class="n">lookup3</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>                            <span class="k">if</span> <span class="n">tags</span> <span class="o">!=</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="n">another_tags</span><span class="p">):</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>                                <span class="k">continue</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>                            <span class="k">if</span> <span class="n">tags_size</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">tags_by_number_of_tags</span><span class="p">:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>                                <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                            <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">another_tags</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            <span class="n">min_tags_len</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">tags_by_number_of_tags</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="n">nearest_non_empty_tags_set</span> <span class="o">=</span> <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">min_tags_len</span><span class="p">]</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_growth_allowed</span><span class="p">(</span><span class="n">is_search_request</span><span class="p">):</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>                <span class="k">for</span> <span class="n">inclusion_tags_set</span> <span class="ow">in</span> <span class="n">tags_by_number_of_tags</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">inclusion_tags_set</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_growth_allowed</span><span class="p">(</span><span class="n">is_search_request</span><span class="p">):</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="n">nearest_non_empty_tags_set</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="k">return</span> <span class="n">nearest_non_empty_tags_set</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">def</span> <span class="nf">_normalise_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="k">return</span> <span class="n">tags</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="nf">_check_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">tags</span> <span class="o">==</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">)):</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">raise</span> <span class="n">TagNotFound</span><span class="p">(</span><span class="n">tags</span> <span class="o">-</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">))</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">return</span> <span class="n">tags</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="nf">_is_growth_allowed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_search_request</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        <span class="k">return</span> <span class="p">(</span><span class="ow">not</span> <span class="n">is_search_request</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">is_search_request</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">growth_during_the_search_is_allowed</span><span class="p">())</span>
</span></pre></div>


            </section>
                <section id="ItemID">
                    <div class="attr variable">
            <span class="name">ItemID</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#ItemID"></a>
    
    

                </section>
                <section id="TagID">
                    <div class="attr variable">
            <span class="name">TagID</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#TagID"></a>
    
    

                </section>
                <section id="UniqueItemID">
                    <div class="attr variable">
            <span class="name">UniqueItemID</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#UniqueItemID"></a>
    
    

                </section>
                <section id="UniqueIdGen">
                            <input id="UniqueIdGen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UniqueIdGen</span>:

                <label class="view-source-button" for="UniqueIdGen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UniqueIdGen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UniqueIdGen-45"><a href="#UniqueIdGen-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">UniqueIdGen</span><span class="p">:</span>
</span><span id="UniqueIdGen-46"><a href="#UniqueIdGen-46"><span class="linenos">46</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UniqueIdGen-47"><a href="#UniqueIdGen-47"><span class="linenos">47</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="UniqueIdGen-48"><a href="#UniqueIdGen-48"><span class="linenos">48</span></a>
</span><span id="UniqueIdGen-49"><a href="#UniqueIdGen-49"><span class="linenos">49</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="UniqueIdGen-50"><a href="#UniqueIdGen-50"><span class="linenos">50</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">index</span>
</span><span id="UniqueIdGen-51"><a href="#UniqueIdGen-51"><span class="linenos">51</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="UniqueIdGen-52"><a href="#UniqueIdGen-52"><span class="linenos">52</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="UniqueIdGen.index" class="classattr">
                                <div class="attr variable">
            <span class="name">index</span>

        
    </div>
    <a class="headerlink" href="#UniqueIdGen.index"></a>
    
    

                            </div>
                </section>
                <section id="tags_set_2_tuple">
                            <input id="tags_set_2_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">tags_set_2_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="tags_set_2_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#tags_set_2_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="tags_set_2_tuple-55"><a href="#tags_set_2_tuple-55"><span class="linenos">55</span></a><span class="k">def</span> <span class="nf">tags_set_2_tuple</span><span class="p">(</span><span class="n">tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="tags_set_2_tuple-56"><a href="#tags_set_2_tuple-56"><span class="linenos">56</span></a>    <span class="n">tags_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="tags_set_2_tuple-57"><a href="#tags_set_2_tuple-57"><span class="linenos">57</span></a>    <span class="n">tags_list</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="tags_set_2_tuple-58"><a href="#tags_set_2_tuple-58"><span class="linenos">58</span></a>    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">tags_list</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="default_growth_during_the_search_checker">
                            <input id="default_growth_during_the_search_checker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">default_growth_during_the_search_checker</span><span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>

                <label class="view-source-button" for="default_growth_during_the_search_checker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#default_growth_during_the_search_checker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="default_growth_during_the_search_checker-61"><a href="#default_growth_during_the_search_checker-61"><span class="linenos">61</span></a><span class="k">def</span> <span class="nf">default_growth_during_the_search_checker</span><span class="p">():</span> <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                </section>
                <section id="default_scheduler">
                            <input id="default_scheduler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">default_scheduler</span><span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>

                <label class="view-source-button" for="default_scheduler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#default_scheduler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="default_scheduler-64"><a href="#default_scheduler-64"><span class="linenos">64</span></a><span class="k">def</span> <span class="nf">default_scheduler</span><span class="p">():</span> <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="TagNotFound">
                            <input id="TagNotFound-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TagNotFound</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TagNotFound-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagNotFound"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagNotFound-67"><a href="#TagNotFound-67"><span class="linenos">67</span></a><span class="k">class</span> <span class="nc">TagNotFound</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TagNotFound-68"><a href="#TagNotFound-68"><span class="linenos">68</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="TagNotFound.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="TagNotFound.with_traceback" class="function">with_traceback</dd>
                <dd id="TagNotFound.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="DynamicTagTree">
                            <input id="DynamicTagTree-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">DynamicTagTree</span>:

                <label class="view-source-button" for="DynamicTagTree-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree-71"><a href="#DynamicTagTree-71"><span class="linenos"> 71</span></a><span class="k">class</span> <span class="nc">DynamicTagTree</span><span class="p">:</span>
</span><span id="DynamicTagTree-72"><a href="#DynamicTagTree-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="DynamicTagTree-73"><a href="#DynamicTagTree-73"><span class="linenos"> 73</span></a>                 <span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="DynamicTagTree-74"><a href="#DynamicTagTree-74"><span class="linenos"> 74</span></a>                 <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="DynamicTagTree-75"><a href="#DynamicTagTree-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> \
</span><span id="DynamicTagTree-76"><a href="#DynamicTagTree-76"><span class="linenos"> 76</span></a>            <span class="n">growth_during_the_search_is_allowed</span> <span class="ow">or</span> <span class="n">default_growth_during_the_search_checker</span>
</span><span id="DynamicTagTree-77"><a href="#DynamicTagTree-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span><span id="DynamicTagTree-78"><a href="#DynamicTagTree-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span> <span class="o">=</span> <span class="n">UniqueIdGen</span><span class="p">()</span>
</span><span id="DynamicTagTree-79"><a href="#DynamicTagTree-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-80"><a href="#DynamicTagTree-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]],</span> <span class="n">UniqueItemID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-81"><a href="#DynamicTagTree-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-82"><a href="#DynamicTagTree-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-83"><a href="#DynamicTagTree-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-84"><a href="#DynamicTagTree-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">ItemID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-85"><a href="#DynamicTagTree-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-86"><a href="#DynamicTagTree-86"><span class="linenos"> 86</span></a>        
</span><span id="DynamicTagTree-87"><a href="#DynamicTagTree-87"><span class="linenos"> 87</span></a>        <span class="c1"># self.tags_by_number_of_tags_by_tag: Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]] = dict()</span>
</span><span id="DynamicTagTree-88"><a href="#DynamicTagTree-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tag; value: keyb  from self.tags_by_number_of_tags</span>
</span><span id="DynamicTagTree-89"><a href="#DynamicTagTree-89"><span class="linenos"> 89</span></a>        
</span><span id="DynamicTagTree-90"><a href="#DynamicTagTree-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]]]</span> <span class="o">=</span> \
</span><span id="DynamicTagTree-91"><a href="#DynamicTagTree-91"><span class="linenos"> 91</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, Dict[len of tags set, Set[tag sets]]]]</span>
</span><span id="DynamicTagTree-92"><a href="#DynamicTagTree-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> \
</span><span id="DynamicTagTree-93"><a href="#DynamicTagTree-93"><span class="linenos"> 93</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, len of tags set]]</span>
</span><span id="DynamicTagTree-94"><a href="#DynamicTagTree-94"><span class="linenos"> 94</span></a>        
</span><span id="DynamicTagTree-95"><a href="#DynamicTagTree-95"><span class="linenos"> 95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: interested tags set;</span>
</span><span id="DynamicTagTree-96"><a href="#DynamicTagTree-96"><span class="linenos"> 96</span></a>        <span class="c1"># value: bigger tags sets which includes interested tags set</span>
</span><span id="DynamicTagTree-97"><a href="#DynamicTagTree-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tag_weight_by_tag_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-98"><a href="#DynamicTagTree-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_tag_weight_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-99"><a href="#DynamicTagTree-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: any</span>
</span><span id="DynamicTagTree-100"><a href="#DynamicTagTree-100"><span class="linenos">100</span></a>        <span class="c1"># interested tags set (input from user); value: set of known tags sets which has an item(-s) and includes given</span>
</span><span id="DynamicTagTree-101"><a href="#DynamicTagTree-101"><span class="linenos">101</span></a>        <span class="c1"># interested tags set</span>
</span><span id="DynamicTagTree-102"><a href="#DynamicTagTree-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tags; value: same tags object</span>
</span><span id="DynamicTagTree-103"><a href="#DynamicTagTree-103"><span class="linenos">103</span></a>
</span><span id="DynamicTagTree-104"><a href="#DynamicTagTree-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">set_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="DynamicTagTree-105"><a href="#DynamicTagTree-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span><span id="DynamicTagTree-106"><a href="#DynamicTagTree-106"><span class="linenos">106</span></a>
</span><span id="DynamicTagTree-107"><a href="#DynamicTagTree-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">get_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="DynamicTagTree-108"><a href="#DynamicTagTree-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span>
</span><span id="DynamicTagTree-109"><a href="#DynamicTagTree-109"><span class="linenos">109</span></a>
</span><span id="DynamicTagTree-110"><a href="#DynamicTagTree-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">UniqueItemID</span><span class="p">:</span>
</span><span id="DynamicTagTree-111"><a href="#DynamicTagTree-111"><span class="linenos">111</span></a>        <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span><span class="p">()</span>
</span><span id="DynamicTagTree-112"><a href="#DynamicTagTree-112"><span class="linenos">112</span></a>        <span class="n">item</span> <span class="o">=</span> <span class="p">(</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree-113"><a href="#DynamicTagTree-113"><span class="linenos">113</span></a>        <span class="n">tags_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree-114"><a href="#DynamicTagTree-114"><span class="linenos">114</span></a>        
</span><span id="DynamicTagTree-115"><a href="#DynamicTagTree-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">[</span><span class="n">unique_item_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="DynamicTagTree-116"><a href="#DynamicTagTree-116"><span class="linenos">116</span></a>        
</span><span id="DynamicTagTree-117"><a href="#DynamicTagTree-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span> <span class="o">=</span> <span class="n">unique_item_id</span>
</span><span id="DynamicTagTree-118"><a href="#DynamicTagTree-118"><span class="linenos">118</span></a>        
</span><span id="DynamicTagTree-119"><a href="#DynamicTagTree-119"><span class="linenos">119</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-120"><a href="#DynamicTagTree-120"><span class="linenos">120</span></a>            <span class="c1"># self.item_tags_by_tag</span>
</span><span id="DynamicTagTree-121"><a href="#DynamicTagTree-121"><span class="linenos">121</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span>
</span><span id="DynamicTagTree-122"><a href="#DynamicTagTree-122"><span class="linenos">122</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-123"><a href="#DynamicTagTree-123"><span class="linenos">123</span></a>            
</span><span id="DynamicTagTree-124"><a href="#DynamicTagTree-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree-125"><a href="#DynamicTagTree-125"><span class="linenos">125</span></a>        
</span><span id="DynamicTagTree-126"><a href="#DynamicTagTree-126"><span class="linenos">126</span></a>            <span class="c1"># self.neighbor_tags_of_a_tag</span>
</span><span id="DynamicTagTree-127"><a href="#DynamicTagTree-127"><span class="linenos">127</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span>
</span><span id="DynamicTagTree-128"><a href="#DynamicTagTree-128"><span class="linenos">128</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-129"><a href="#DynamicTagTree-129"><span class="linenos">129</span></a>            
</span><span id="DynamicTagTree-130"><a href="#DynamicTagTree-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tags</span> <span class="o">-</span> <span class="n">tag</span><span class="p">)</span>
</span><span id="DynamicTagTree-131"><a href="#DynamicTagTree-131"><span class="linenos">131</span></a>            
</span><span id="DynamicTagTree-132"><a href="#DynamicTagTree-132"><span class="linenos">132</span></a>            <span class="c1"># self.set_of_tags</span>
</span><span id="DynamicTagTree-133"><a href="#DynamicTagTree-133"><span class="linenos">133</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="DynamicTagTree-134"><a href="#DynamicTagTree-134"><span class="linenos">134</span></a>        
</span><span id="DynamicTagTree-135"><a href="#DynamicTagTree-135"><span class="linenos">135</span></a>        <span class="c1"># self.direct_items_by_tags</span>
</span><span id="DynamicTagTree-136"><a href="#DynamicTagTree-136"><span class="linenos">136</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-137"><a href="#DynamicTagTree-137"><span class="linenos">137</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-138"><a href="#DynamicTagTree-138"><span class="linenos">138</span></a>        
</span><span id="DynamicTagTree-139"><a href="#DynamicTagTree-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">item_id</span><span class="p">)</span>
</span><span id="DynamicTagTree-140"><a href="#DynamicTagTree-140"><span class="linenos">140</span></a>        
</span><span id="DynamicTagTree-141"><a href="#DynamicTagTree-141"><span class="linenos">141</span></a>        <span class="c1"># self.tags_by_number_of_tags</span>
</span><span id="DynamicTagTree-142"><a href="#DynamicTagTree-142"><span class="linenos">142</span></a>        <span class="k">if</span> <span class="n">tags_len</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-143"><a href="#DynamicTagTree-143"><span class="linenos">143</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-144"><a href="#DynamicTagTree-144"><span class="linenos">144</span></a>        
</span><span id="DynamicTagTree-145"><a href="#DynamicTagTree-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree-146"><a href="#DynamicTagTree-146"><span class="linenos">146</span></a>        
</span><span id="DynamicTagTree-147"><a href="#DynamicTagTree-147"><span class="linenos">147</span></a>        <span class="c1"># self.tags_len_by_tag</span>
</span><span id="DynamicTagTree-148"><a href="#DynamicTagTree-148"><span class="linenos">148</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-149"><a href="#DynamicTagTree-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="n">tags_len</span>
</span><span id="DynamicTagTree-150"><a href="#DynamicTagTree-150"><span class="linenos">150</span></a>
</span><span id="DynamicTagTree-151"><a href="#DynamicTagTree-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">]:</span>
</span><span id="DynamicTagTree-152"><a href="#DynamicTagTree-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="o">.</span><span class="n">get</span><span class="p">((</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="DynamicTagTree-153"><a href="#DynamicTagTree-153"><span class="linenos">153</span></a>
</span><span id="DynamicTagTree-154"><a href="#DynamicTagTree-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]:</span>
</span><span id="DynamicTagTree-155"><a href="#DynamicTagTree-155"><span class="linenos">155</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">unique_item_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="DynamicTagTree-156"><a href="#DynamicTagTree-156"><span class="linenos">156</span></a>
</span><span id="DynamicTagTree-157"><a href="#DynamicTagTree-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">):</span>
</span><span id="DynamicTagTree-158"><a href="#DynamicTagTree-158"><span class="linenos">158</span></a>        <span class="k">pass</span>
</span><span id="DynamicTagTree-159"><a href="#DynamicTagTree-159"><span class="linenos">159</span></a>
</span><span id="DynamicTagTree-160"><a href="#DynamicTagTree-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">list_direct_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree-161"><a href="#DynamicTagTree-161"><span class="linenos">161</span></a>        <span class="k">pass</span>
</span><span id="DynamicTagTree-162"><a href="#DynamicTagTree-162"><span class="linenos">162</span></a>
</span><span id="DynamicTagTree-163"><a href="#DynamicTagTree-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">list_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree-164"><a href="#DynamicTagTree-164"><span class="linenos">164</span></a>        <span class="k">pass</span>
</span><span id="DynamicTagTree-165"><a href="#DynamicTagTree-165"><span class="linenos">165</span></a>
</span><span id="DynamicTagTree-166"><a href="#DynamicTagTree-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">list_direct_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree-167"><a href="#DynamicTagTree-167"><span class="linenos">167</span></a>        <span class="k">pass</span>
</span><span id="DynamicTagTree-168"><a href="#DynamicTagTree-168"><span class="linenos">168</span></a>
</span><span id="DynamicTagTree-169"><a href="#DynamicTagTree-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">list_all_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree-170"><a href="#DynamicTagTree-170"><span class="linenos">170</span></a>        <span class="k">pass</span>
</span><span id="DynamicTagTree-171"><a href="#DynamicTagTree-171"><span class="linenos">171</span></a>
</span><span id="DynamicTagTree-172"><a href="#DynamicTagTree-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">get_nearest_non_empty_tags_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]:</span>
</span><span id="DynamicTagTree-173"><a href="#DynamicTagTree-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_gen_nearest_non_empty_tags_by_some_tags</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_normalise_tags</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_check_tags</span><span class="p">(</span><span class="n">tags</span><span class="p">)))</span>
</span><span id="DynamicTagTree-174"><a href="#DynamicTagTree-174"><span class="linenos">174</span></a>
</span><span id="DynamicTagTree-175"><a href="#DynamicTagTree-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">_gen_nearest_non_empty_tags_by_some_tags</span><span class="p">(</span>
</span><span id="DynamicTagTree-176"><a href="#DynamicTagTree-176"><span class="linenos">176</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">is_search_request</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]:</span>
</span><span id="DynamicTagTree-177"><a href="#DynamicTagTree-177"><span class="linenos">177</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span>
</span><span id="DynamicTagTree-178"><a href="#DynamicTagTree-178"><span class="linenos">178</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">[</span><span class="n">tags</span><span class="p">])</span>
</span><span id="DynamicTagTree-179"><a href="#DynamicTagTree-179"><span class="linenos">179</span></a>
</span><span id="DynamicTagTree-180"><a href="#DynamicTagTree-180"><span class="linenos">180</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-181"><a href="#DynamicTagTree-181"><span class="linenos">181</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="DynamicTagTree-182"><a href="#DynamicTagTree-182"><span class="linenos">182</span></a>
</span><span id="DynamicTagTree-183"><a href="#DynamicTagTree-183"><span class="linenos">183</span></a>        <span class="n">nearest_non_empty_tags_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-184"><a href="#DynamicTagTree-184"><span class="linenos">184</span></a>
</span><span id="DynamicTagTree-185"><a href="#DynamicTagTree-185"><span class="linenos">185</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-186"><a href="#DynamicTagTree-186"><span class="linenos">186</span></a>            <span class="n">inclusion_tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="DynamicTagTree-187"><a href="#DynamicTagTree-187"><span class="linenos">187</span></a>            <span class="n">min_tags_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">inclusion_tags</span><span class="p">))</span>
</span><span id="DynamicTagTree-188"><a href="#DynamicTagTree-188"><span class="linenos">188</span></a>            <span class="k">for</span> <span class="n">tags2</span> <span class="ow">in</span> <span class="n">inclusion_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-189"><a href="#DynamicTagTree-189"><span class="linenos">189</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags2</span><span class="p">)</span> <span class="o">==</span> <span class="n">min_tags_len</span><span class="p">:</span>
</span><span id="DynamicTagTree-190"><a href="#DynamicTagTree-190"><span class="linenos">190</span></a>                    <span class="n">nearest_non_empty_tags_set</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags2</span><span class="p">)</span>
</span><span id="DynamicTagTree-191"><a href="#DynamicTagTree-191"><span class="linenos">191</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="DynamicTagTree-192"><a href="#DynamicTagTree-192"><span class="linenos">192</span></a>            <span class="n">minimal_nearest_non_empty_tags_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="DynamicTagTree-193"><a href="#DynamicTagTree-193"><span class="linenos">193</span></a>            <span class="n">tags_by_number_of_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree-194"><a href="#DynamicTagTree-194"><span class="linenos">194</span></a>            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-195"><a href="#DynamicTagTree-195"><span class="linenos">195</span></a>                <span class="n">lookup1</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]]</span> <span class="o">=</span> \
</span><span id="DynamicTagTree-196"><a href="#DynamicTagTree-196"><span class="linenos">196</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">near_tags_by_number_of_tags_by_tag_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span>
</span><span id="DynamicTagTree-197"><a href="#DynamicTagTree-197"><span class="linenos">197</span></a>                <span class="k">for</span> <span class="n">tag2</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-198"><a href="#DynamicTagTree-198"><span class="linenos">198</span></a>                    <span class="k">if</span> <span class="n">tag</span> <span class="o">==</span> <span class="n">tag2</span><span class="p">:</span>
</span><span id="DynamicTagTree-199"><a href="#DynamicTagTree-199"><span class="linenos">199</span></a>                        <span class="k">continue</span>
</span><span id="DynamicTagTree-200"><a href="#DynamicTagTree-200"><span class="linenos">200</span></a>                    <span class="k">if</span> <span class="n">tag2</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">lookup1</span><span class="p">:</span>
</span><span id="DynamicTagTree-201"><a href="#DynamicTagTree-201"><span class="linenos">201</span></a>                        <span class="k">return</span> <span class="kc">None</span>
</span><span id="DynamicTagTree-202"><a href="#DynamicTagTree-202"><span class="linenos">202</span></a>                    <span class="n">lookup2</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="n">lookup1</span><span class="p">[</span><span class="n">tag2</span><span class="p">]</span>
</span><span id="DynamicTagTree-203"><a href="#DynamicTagTree-203"><span class="linenos">203</span></a>                    <span class="n">sorted_tags_sizes</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">lookup2</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="DynamicTagTree-204"><a href="#DynamicTagTree-204"><span class="linenos">204</span></a>                    <span class="k">for</span> <span class="n">tags_size</span> <span class="ow">in</span> <span class="n">sorted_tags_sizes</span><span class="p">:</span>
</span><span id="DynamicTagTree-205"><a href="#DynamicTagTree-205"><span class="linenos">205</span></a>                        <span class="k">if</span> <span class="n">tags_size</span> <span class="o">&lt;</span> <span class="n">minimal_nearest_non_empty_tags_size</span><span class="p">:</span>
</span><span id="DynamicTagTree-206"><a href="#DynamicTagTree-206"><span class="linenos">206</span></a>                            <span class="k">continue</span>
</span><span id="DynamicTagTree-207"><a href="#DynamicTagTree-207"><span class="linenos">207</span></a>                        <span class="n">lookup3</span> <span class="o">=</span> <span class="n">lookup2</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span>
</span><span id="DynamicTagTree-208"><a href="#DynamicTagTree-208"><span class="linenos">208</span></a>                        <span class="k">for</span> <span class="n">another_tags</span> <span class="ow">in</span> <span class="n">lookup3</span><span class="p">:</span>
</span><span id="DynamicTagTree-209"><a href="#DynamicTagTree-209"><span class="linenos">209</span></a>                            <span class="k">if</span> <span class="n">tags</span> <span class="o">!=</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="n">another_tags</span><span class="p">):</span>
</span><span id="DynamicTagTree-210"><a href="#DynamicTagTree-210"><span class="linenos">210</span></a>                                <span class="k">continue</span>
</span><span id="DynamicTagTree-211"><a href="#DynamicTagTree-211"><span class="linenos">211</span></a>                            <span class="k">if</span> <span class="n">tags_size</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">tags_by_number_of_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree-212"><a href="#DynamicTagTree-212"><span class="linenos">212</span></a>                                <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-213"><a href="#DynamicTagTree-213"><span class="linenos">213</span></a>                            <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_size</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">another_tags</span><span class="p">)</span>
</span><span id="DynamicTagTree-214"><a href="#DynamicTagTree-214"><span class="linenos">214</span></a>            <span class="n">min_tags_len</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">tags_by_number_of_tags</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="DynamicTagTree-215"><a href="#DynamicTagTree-215"><span class="linenos">215</span></a>            <span class="n">nearest_non_empty_tags_set</span> <span class="o">=</span> <span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">min_tags_len</span><span class="p">]</span>
</span><span id="DynamicTagTree-216"><a href="#DynamicTagTree-216"><span class="linenos">216</span></a>
</span><span id="DynamicTagTree-217"><a href="#DynamicTagTree-217"><span class="linenos">217</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_growth_allowed</span><span class="p">(</span><span class="n">is_search_request</span><span class="p">):</span>
</span><span id="DynamicTagTree-218"><a href="#DynamicTagTree-218"><span class="linenos">218</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree-219"><a href="#DynamicTagTree-219"><span class="linenos">219</span></a>                <span class="k">for</span> <span class="n">inclusion_tags_set</span> <span class="ow">in</span> <span class="n">tags_by_number_of_tags</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
</span><span id="DynamicTagTree-220"><a href="#DynamicTagTree-220"><span class="linenos">220</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">inclusion_tags_set</span><span class="p">)</span>
</span><span id="DynamicTagTree-221"><a href="#DynamicTagTree-221"><span class="linenos">221</span></a>
</span><span id="DynamicTagTree-222"><a href="#DynamicTagTree-222"><span class="linenos">222</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_growth_allowed</span><span class="p">(</span><span class="n">is_search_request</span><span class="p">):</span>
</span><span id="DynamicTagTree-223"><a href="#DynamicTagTree-223"><span class="linenos">223</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="n">nearest_non_empty_tags_set</span>
</span><span id="DynamicTagTree-224"><a href="#DynamicTagTree-224"><span class="linenos">224</span></a>
</span><span id="DynamicTagTree-225"><a href="#DynamicTagTree-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="n">nearest_non_empty_tags_set</span>
</span><span id="DynamicTagTree-226"><a href="#DynamicTagTree-226"><span class="linenos">226</span></a>
</span><span id="DynamicTagTree-227"><a href="#DynamicTagTree-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">_normalise_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="DynamicTagTree-228"><a href="#DynamicTagTree-228"><span class="linenos">228</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span>
</span><span id="DynamicTagTree-229"><a href="#DynamicTagTree-229"><span class="linenos">229</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span>
</span><span id="DynamicTagTree-230"><a href="#DynamicTagTree-230"><span class="linenos">230</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="DynamicTagTree-231"><a href="#DynamicTagTree-231"><span class="linenos">231</span></a>            <span class="k">return</span> <span class="n">tags</span>
</span><span id="DynamicTagTree-232"><a href="#DynamicTagTree-232"><span class="linenos">232</span></a>
</span><span id="DynamicTagTree-233"><a href="#DynamicTagTree-233"><span class="linenos">233</span></a>    <span class="k">def</span> <span class="nf">_check_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]:</span>
</span><span id="DynamicTagTree-234"><a href="#DynamicTagTree-234"><span class="linenos">234</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">tags</span> <span class="o">==</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">)):</span>
</span><span id="DynamicTagTree-235"><a href="#DynamicTagTree-235"><span class="linenos">235</span></a>            <span class="k">raise</span> <span class="n">TagNotFound</span><span class="p">(</span><span class="n">tags</span> <span class="o">-</span> <span class="p">(</span><span class="n">tags</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">))</span>
</span><span id="DynamicTagTree-236"><a href="#DynamicTagTree-236"><span class="linenos">236</span></a>        <span class="k">return</span> <span class="n">tags</span>
</span><span id="DynamicTagTree-237"><a href="#DynamicTagTree-237"><span class="linenos">237</span></a>
</span><span id="DynamicTagTree-238"><a href="#DynamicTagTree-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">_is_growth_allowed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">is_search_request</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="DynamicTagTree-239"><a href="#DynamicTagTree-239"><span class="linenos">239</span></a>        <span class="k">return</span> <span class="p">(</span><span class="ow">not</span> <span class="n">is_search_request</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">is_search_request</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">growth_during_the_search_is_allowed</span><span class="p">())</span>
</span></pre></div>


    

                            <div id="DynamicTagTree.__init__" class="classattr">
                                        <input id="DynamicTagTree.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">DynamicTagTree</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="DynamicTagTree.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.__init__-72"><a href="#DynamicTagTree.__init__-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span>
</span><span id="DynamicTagTree.__init__-73"><a href="#DynamicTagTree.__init__-73"><span class="linenos"> 73</span></a>                 <span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="DynamicTagTree.__init__-74"><a href="#DynamicTagTree.__init__-74"><span class="linenos"> 74</span></a>                 <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="DynamicTagTree.__init__-75"><a href="#DynamicTagTree.__init__-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">growth_during_the_search_is_allowed</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> \
</span><span id="DynamicTagTree.__init__-76"><a href="#DynamicTagTree.__init__-76"><span class="linenos"> 76</span></a>            <span class="n">growth_during_the_search_is_allowed</span> <span class="ow">or</span> <span class="n">default_growth_during_the_search_checker</span>
</span><span id="DynamicTagTree.__init__-77"><a href="#DynamicTagTree.__init__-77"><span class="linenos"> 77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span><span id="DynamicTagTree.__init__-78"><a href="#DynamicTagTree.__init__-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span> <span class="o">=</span> <span class="n">UniqueIdGen</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-79"><a href="#DynamicTagTree.__init__-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-80"><a href="#DynamicTagTree.__init__-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]],</span> <span class="n">UniqueItemID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-81"><a href="#DynamicTagTree.__init__-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-82"><a href="#DynamicTagTree.__init__-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-83"><a href="#DynamicTagTree.__init__-83"><span class="linenos"> 83</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-84"><a href="#DynamicTagTree.__init__-84"><span class="linenos"> 84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">ItemID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-85"><a href="#DynamicTagTree.__init__-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-86"><a href="#DynamicTagTree.__init__-86"><span class="linenos"> 86</span></a>        
</span><span id="DynamicTagTree.__init__-87"><a href="#DynamicTagTree.__init__-87"><span class="linenos"> 87</span></a>        <span class="c1"># self.tags_by_number_of_tags_by_tag: Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]] = dict()</span>
</span><span id="DynamicTagTree.__init__-88"><a href="#DynamicTagTree.__init__-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tag; value: keyb  from self.tags_by_number_of_tags</span>
</span><span id="DynamicTagTree.__init__-89"><a href="#DynamicTagTree.__init__-89"><span class="linenos"> 89</span></a>        
</span><span id="DynamicTagTree.__init__-90"><a href="#DynamicTagTree.__init__-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]]]</span> <span class="o">=</span> \
</span><span id="DynamicTagTree.__init__-91"><a href="#DynamicTagTree.__init__-91"><span class="linenos"> 91</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, Dict[len of tags set, Set[tag sets]]]]</span>
</span><span id="DynamicTagTree.__init__-92"><a href="#DynamicTagTree.__init__-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag_by_near_tag</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> \
</span><span id="DynamicTagTree.__init__-93"><a href="#DynamicTagTree.__init__-93"><span class="linenos"> 93</span></a>            <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># Dict[interested tag, Dict[near tag, len of tags set]]</span>
</span><span id="DynamicTagTree.__init__-94"><a href="#DynamicTagTree.__init__-94"><span class="linenos"> 94</span></a>        
</span><span id="DynamicTagTree.__init__-95"><a href="#DynamicTagTree.__init__-95"><span class="linenos"> 95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_inclusion_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: interested tags set;</span>
</span><span id="DynamicTagTree.__init__-96"><a href="#DynamicTagTree.__init__-96"><span class="linenos"> 96</span></a>        <span class="c1"># value: bigger tags sets which includes interested tags set</span>
</span><span id="DynamicTagTree.__init__-97"><a href="#DynamicTagTree.__init__-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tag_weight_by_tag_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TagID</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-98"><a href="#DynamicTagTree.__init__-98"><span class="linenos"> 98</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_tag_weight_by_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">Set</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="DynamicTagTree.__init__-99"><a href="#DynamicTagTree.__init__-99"><span class="linenos"> 99</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">nearest_non_empty_tags_by_some_tags</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: any</span>
</span><span id="DynamicTagTree.__init__-100"><a href="#DynamicTagTree.__init__-100"><span class="linenos">100</span></a>        <span class="c1"># interested tags set (input from user); value: set of known tags sets which has an item(-s) and includes given</span>
</span><span id="DynamicTagTree.__init__-101"><a href="#DynamicTagTree.__init__-101"><span class="linenos">101</span></a>        <span class="c1"># interested tags set</span>
</span><span id="DynamicTagTree.__init__-102"><a href="#DynamicTagTree.__init__-102"><span class="linenos">102</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_itself</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">],</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># key: tags; value: same tags object</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.growth_during_the_search_is_allowed" class="classattr">
                                <div class="attr variable">
            <span class="name">growth_during_the_search_is_allowed</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.growth_during_the_search_is_allowed"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.scheduler" class="classattr">
                                <div class="attr variable">
            <span class="name">scheduler</span><span class="annotation">: Callable</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.scheduler"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.uiidg" class="classattr">
                                <div class="attr variable">
            <span class="name">uiidg</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.uiidg"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.item_by_uiid" class="classattr">
                                <div class="attr variable">
            <span class="name">item_by_uiid</span><span class="annotation">: Dict[Hashable, Tuple[Hashable, FrozenSet[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.item_by_uiid"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.uiid_by_item" class="classattr">
                                <div class="attr variable">
            <span class="name">uiid_by_item</span><span class="annotation">: Dict[Tuple[Hashable, FrozenSet[Hashable]], Hashable]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.uiid_by_item"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.item_tags_by_tag" class="classattr">
                                <div class="attr variable">
            <span class="name">item_tags_by_tag</span><span class="annotation">: Dict[Hashable, Set[FrozenSet[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.item_tags_by_tag"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.neighbor_tags_of_a_tag" class="classattr">
                                <div class="attr variable">
            <span class="name">neighbor_tags_of_a_tag</span><span class="annotation">: Dict[Hashable, Set[Hashable]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.neighbor_tags_of_a_tag"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.set_of_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">set_of_tags</span><span class="annotation">: Set[Hashable]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.set_of_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.direct_items_by_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">direct_items_by_tags</span><span class="annotation">: Dict[FrozenSet[Hashable], Set[Hashable]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.direct_items_by_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_by_number_of_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_by_number_of_tags</span><span class="annotation">: Dict[int, Set[FrozenSet[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_by_number_of_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_len_by_tag" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_len_by_tag</span><span class="annotation">: Dict[Hashable, int]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_len_by_tag"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_by_number_of_tags_by_tag_by_near_tag" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_by_number_of_tags_by_tag_by_near_tag</span><span class="annotation">: Dict[Hashable, Dict[Hashable, Dict[int, Set[FrozenSet[Hashable]]]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_by_number_of_tags_by_tag_by_near_tag"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_len_by_tag_by_near_tag" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_len_by_tag_by_near_tag</span><span class="annotation">: Dict[Hashable, Dict[Hashable, int]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_len_by_tag_by_near_tag"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_inclusion_by_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_inclusion_by_tags</span><span class="annotation">: Dict[FrozenSet[Hashable], Set[FrozenSet[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_inclusion_by_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tag_weight_by_tag_by_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">tag_weight_by_tag_by_tags</span><span class="annotation">: Dict[FrozenSet[Hashable], Dict[Hashable, int]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tag_weight_by_tag_by_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_by_tag_weight_by_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_by_tag_weight_by_tags</span><span class="annotation">: Dict[FrozenSet[Hashable], Dict[int, Set[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_by_tag_weight_by_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.nearest_non_empty_tags_by_some_tags" class="classattr">
                                <div class="attr variable">
            <span class="name">nearest_non_empty_tags_by_some_tags</span><span class="annotation">: Dict[FrozenSet[Hashable], Set[FrozenSet[Hashable]]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.nearest_non_empty_tags_by_some_tags"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.tags_by_itself" class="classattr">
                                <div class="attr variable">
            <span class="name">tags_by_itself</span><span class="annotation">: Dict[FrozenSet[Hashable], FrozenSet[Hashable]]</span>

        
    </div>
    <a class="headerlink" href="#DynamicTagTree.tags_by_itself"></a>
    
    

                            </div>
                            <div id="DynamicTagTree.set_scheduler" class="classattr">
                                        <input id="DynamicTagTree.set_scheduler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_scheduler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">scheduler</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.set_scheduler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.set_scheduler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.set_scheduler-104"><a href="#DynamicTagTree.set_scheduler-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">set_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]):</span>
</span><span id="DynamicTagTree.set_scheduler-105"><a href="#DynamicTagTree.set_scheduler-105"><span class="linenos">105</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span> <span class="o">=</span> <span class="n">scheduler</span> <span class="ow">or</span> <span class="n">default_scheduler</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.get_scheduler" class="classattr">
                                        <input id="DynamicTagTree.get_scheduler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_scheduler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.get_scheduler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.get_scheduler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.get_scheduler-107"><a href="#DynamicTagTree.get_scheduler-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">get_scheduler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="DynamicTagTree.get_scheduler-108"><a href="#DynamicTagTree.get_scheduler-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">scheduler</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.put" class="classattr">
                                        <input id="DynamicTagTree.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">item_id</span><span class="p">:</span> <span class="n">Hashable</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Hashable</span>:</span></span>

                <label class="view-source-button" for="DynamicTagTree.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.put-110"><a href="#DynamicTagTree.put-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">UniqueItemID</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-111"><a href="#DynamicTagTree.put-111"><span class="linenos">111</span></a>        <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiidg</span><span class="p">()</span>
</span><span id="DynamicTagTree.put-112"><a href="#DynamicTagTree.put-112"><span class="linenos">112</span></a>        <span class="n">item</span> <span class="o">=</span> <span class="p">(</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-113"><a href="#DynamicTagTree.put-113"><span class="linenos">113</span></a>        <span class="n">tags_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-114"><a href="#DynamicTagTree.put-114"><span class="linenos">114</span></a>        
</span><span id="DynamicTagTree.put-115"><a href="#DynamicTagTree.put-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="p">[</span><span class="n">unique_item_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="DynamicTagTree.put-116"><a href="#DynamicTagTree.put-116"><span class="linenos">116</span></a>        
</span><span id="DynamicTagTree.put-117"><a href="#DynamicTagTree.put-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span> <span class="o">=</span> <span class="n">unique_item_id</span>
</span><span id="DynamicTagTree.put-118"><a href="#DynamicTagTree.put-118"><span class="linenos">118</span></a>        
</span><span id="DynamicTagTree.put-119"><a href="#DynamicTagTree.put-119"><span class="linenos">119</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-120"><a href="#DynamicTagTree.put-120"><span class="linenos">120</span></a>            <span class="c1"># self.item_tags_by_tag</span>
</span><span id="DynamicTagTree.put-121"><a href="#DynamicTagTree.put-121"><span class="linenos">121</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-122"><a href="#DynamicTagTree.put-122"><span class="linenos">122</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree.put-123"><a href="#DynamicTagTree.put-123"><span class="linenos">123</span></a>            
</span><span id="DynamicTagTree.put-124"><a href="#DynamicTagTree.put-124"><span class="linenos">124</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">item_tags_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-125"><a href="#DynamicTagTree.put-125"><span class="linenos">125</span></a>        
</span><span id="DynamicTagTree.put-126"><a href="#DynamicTagTree.put-126"><span class="linenos">126</span></a>            <span class="c1"># self.neighbor_tags_of_a_tag</span>
</span><span id="DynamicTagTree.put-127"><a href="#DynamicTagTree.put-127"><span class="linenos">127</span></a>            <span class="k">if</span> <span class="n">tag</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-128"><a href="#DynamicTagTree.put-128"><span class="linenos">128</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree.put-129"><a href="#DynamicTagTree.put-129"><span class="linenos">129</span></a>            
</span><span id="DynamicTagTree.put-130"><a href="#DynamicTagTree.put-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">neighbor_tags_of_a_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tags</span> <span class="o">-</span> <span class="n">tag</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-131"><a href="#DynamicTagTree.put-131"><span class="linenos">131</span></a>            
</span><span id="DynamicTagTree.put-132"><a href="#DynamicTagTree.put-132"><span class="linenos">132</span></a>            <span class="c1"># self.set_of_tags</span>
</span><span id="DynamicTagTree.put-133"><a href="#DynamicTagTree.put-133"><span class="linenos">133</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">set_of_tags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-134"><a href="#DynamicTagTree.put-134"><span class="linenos">134</span></a>        
</span><span id="DynamicTagTree.put-135"><a href="#DynamicTagTree.put-135"><span class="linenos">135</span></a>        <span class="c1"># self.direct_items_by_tags</span>
</span><span id="DynamicTagTree.put-136"><a href="#DynamicTagTree.put-136"><span class="linenos">136</span></a>        <span class="k">if</span> <span class="n">tags</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-137"><a href="#DynamicTagTree.put-137"><span class="linenos">137</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree.put-138"><a href="#DynamicTagTree.put-138"><span class="linenos">138</span></a>        
</span><span id="DynamicTagTree.put-139"><a href="#DynamicTagTree.put-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">direct_items_by_tags</span><span class="p">[</span><span class="n">tags</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">item_id</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-140"><a href="#DynamicTagTree.put-140"><span class="linenos">140</span></a>        
</span><span id="DynamicTagTree.put-141"><a href="#DynamicTagTree.put-141"><span class="linenos">141</span></a>        <span class="c1"># self.tags_by_number_of_tags</span>
</span><span id="DynamicTagTree.put-142"><a href="#DynamicTagTree.put-142"><span class="linenos">142</span></a>        <span class="k">if</span> <span class="n">tags_len</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-143"><a href="#DynamicTagTree.put-143"><span class="linenos">143</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="DynamicTagTree.put-144"><a href="#DynamicTagTree.put-144"><span class="linenos">144</span></a>        
</span><span id="DynamicTagTree.put-145"><a href="#DynamicTagTree.put-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tags_by_number_of_tags</span><span class="p">[</span><span class="n">tags_len</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tags</span><span class="p">)</span>
</span><span id="DynamicTagTree.put-146"><a href="#DynamicTagTree.put-146"><span class="linenos">146</span></a>        
</span><span id="DynamicTagTree.put-147"><a href="#DynamicTagTree.put-147"><span class="linenos">147</span></a>        <span class="c1"># self.tags_len_by_tag</span>
</span><span id="DynamicTagTree.put-148"><a href="#DynamicTagTree.put-148"><span class="linenos">148</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">tags</span><span class="p">:</span>
</span><span id="DynamicTagTree.put-149"><a href="#DynamicTagTree.put-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tags_len_by_tag</span><span class="p">[</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="n">tags_len</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.get" class="classattr">
                                        <input id="DynamicTagTree.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">item_id</span><span class="p">:</span> <span class="n">Hashable</span>,</span><span class="param">	<span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="DynamicTagTree.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.get-151"><a href="#DynamicTagTree.get-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_id</span><span class="p">:</span> <span class="n">ItemID</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">UniqueItemID</span><span class="p">]:</span>
</span><span id="DynamicTagTree.get-152"><a href="#DynamicTagTree.get-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">uiid_by_item</span><span class="o">.</span><span class="n">get</span><span class="p">((</span><span class="n">item_id</span><span class="p">,</span> <span class="n">tags</span><span class="p">),</span> <span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.item" class="classattr">
                                        <input id="DynamicTagTree.item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">item</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">unique_item_id</span><span class="p">:</span> <span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="DynamicTagTree.item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.item-154"><a href="#DynamicTagTree.item-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">ItemID</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]]:</span>
</span><span id="DynamicTagTree.item-155"><a href="#DynamicTagTree.item-155"><span class="linenos">155</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">item_by_uiid</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">unique_item_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.delete" class="classattr">
                                        <input id="DynamicTagTree.delete-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">delete</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">unique_item_id</span><span class="p">:</span> <span class="n">Hashable</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.delete-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.delete"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.delete-157"><a href="#DynamicTagTree.delete-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">unique_item_id</span><span class="p">:</span> <span class="n">UniqueItemID</span><span class="p">):</span>
</span><span id="DynamicTagTree.delete-158"><a href="#DynamicTagTree.delete-158"><span class="linenos">158</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.list_direct_items" class="classattr">
                                        <input id="DynamicTagTree.list_direct_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">list_direct_items</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.list_direct_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.list_direct_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.list_direct_items-160"><a href="#DynamicTagTree.list_direct_items-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">list_direct_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree.list_direct_items-161"><a href="#DynamicTagTree.list_direct_items-161"><span class="linenos">161</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.list_all_items" class="classattr">
                                        <input id="DynamicTagTree.list_all_items-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">list_all_items</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.list_all_items-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.list_all_items"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.list_all_items-163"><a href="#DynamicTagTree.list_all_items-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">list_all_items</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree.list_all_items-164"><a href="#DynamicTagTree.list_all_items-164"><span class="linenos">164</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.list_direct_tags" class="classattr">
                                        <input id="DynamicTagTree.list_direct_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">list_direct_tags</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.list_direct_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.list_direct_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.list_direct_tags-166"><a href="#DynamicTagTree.list_direct_tags-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">list_direct_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree.list_direct_tags-167"><a href="#DynamicTagTree.list_direct_tags-167"><span class="linenos">167</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.list_all_tags" class="classattr">
                                        <input id="DynamicTagTree.list_all_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">list_all_tags</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="DynamicTagTree.list_all_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.list_all_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.list_all_tags-169"><a href="#DynamicTagTree.list_all_tags-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">list_all_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]):</span>
</span><span id="DynamicTagTree.list_all_tags-170"><a href="#DynamicTagTree.list_all_tags-170"><span class="linenos">170</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="DynamicTagTree.get_nearest_non_empty_tags_set" class="classattr">
                                        <input id="DynamicTagTree.get_nearest_non_empty_tags_set-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_nearest_non_empty_tags_set</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">Hashable</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="DynamicTagTree.get_nearest_non_empty_tags_set-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DynamicTagTree.get_nearest_non_empty_tags_set"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DynamicTagTree.get_nearest_non_empty_tags_set-172"><a href="#DynamicTagTree.get_nearest_non_empty_tags_set-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">get_nearest_non_empty_tags_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tags</span><span class="p">:</span> <span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">FrozenSet</span><span class="p">[</span><span class="n">TagID</span><span class="p">]]:</span>
</span><span id="DynamicTagTree.get_nearest_non_empty_tags_set-173"><a href="#DynamicTagTree.get_nearest_non_empty_tags_set-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_gen_nearest_non_empty_tags_by_some_tags</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_normalise_tags</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_check_tags</span><span class="p">(</span><span class="n">tags</span><span class="p">)))</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>