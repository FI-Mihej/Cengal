---
title: TagDB
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_containers<wbr>.dynamic_tag_tree<wbr>.versions<wbr>.v_1<wbr>.TagDB    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-TagDB-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-TagDB-view-source"><span>View Source</span></label>

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
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s1">&#39;Mikhail Butenko &lt;gtalk@mikhail-butenko.in.ua&gt;&#39;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.data_generation.id_generator</span> <span class="kn">import</span> <span class="n">IDGenerator</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">contextmanager</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Any</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.compound_dict_management.standard_library.key__hashable__to__value__set</span> <span class="kn">import</span> <span class="n">AddToCompoundDict__Set</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.compound_dict_management.standard_library.key_counter</span> <span class="kn">import</span> <span class="n">KeyCounter</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">gly</span><span class="p">,</span> <span class="n">CoroPriority</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">EntityStatsMixin</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">SMART_TREE_TYPE</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># smart tree. Умное дерево тегов: сеть отображенная на древо. Возвращает только список</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="c1"># непосредственных подтегов текущего пути, но не их подтеги; возвращает элементы текущего пути, но не элементы</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="c1"># из подпутей</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">SMART_TREE_TYPE_WITH_INTERNAL_MENU</span> <span class="o">=</span> <span class="mi">1</span>   <span class="c1"># smart tree with internal menu. В древо встроено меню, позволяющее прямо из</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="c1"># древа производить смену типа вывода: SMART_TREE_TYPE, FULL_TREE_TYPE и PLAIN_PSEUDO_TREE_TYPE. На каждый тип</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="c1"># вывода будет доступен подтег/подпапка, внутри когорого уже будет нормальное древо элементов, но уже выбранного</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="c1"># типа</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="n">FULL_TREE_TYPE</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># full tree with all tags - with repeats and without filtering. Список айтемов - как у</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="c1"># SMART_TREE_TYPE, но при этом список тегов - как у PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="n">PLAIN_PSEUDO_TREE_TYPE</span> <span class="o">=</span> <span class="mi">3</span>   <span class="c1"># plain tags and items set (will show all tags, subtags and items of</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="c1"># current hm... dir - current tag set). Показывает все теги и подтеги единым списком - как у примитивных теговых</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="c1"># файловых систем; показывает все элементы текущего пути + все элементы всех под-путей</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="n">USUAL_TREE_TYPE</span> <span class="o">=</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="n">_ROOT_TAG</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">&#39;k{1+vdcY#m8t-4m9`)G2\b]/O</span><span class="se">\&#39;</span><span class="s1">Rzqyr@FEO~%./nGPzl)[^q 0RS!.bCPh ?fag{8~{SGj;Ss3U85Q-:&#39;</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="k">class</span> <span class="nc">ToManyIdenticalItemsOnTheGivenTagPathError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="k">pass</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="k">class</span> <span class="nc">UnknownTreeTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">pass</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="k">class</span> <span class="nc">LockableMixin</span><span class="p">:</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="nd">@property</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="nd">@lock</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="nd">@contextmanager</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="k">def</span> <span class="nf">obj_locker</span><span class="p">(</span><span class="n">obj</span><span class="p">:</span> <span class="n">LockableMixin</span><span class="p">):</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="n">obj</span><span class="o">.</span><span class="n">lock</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="k">yield</span> <span class="n">obj</span><span class="o">.</span><span class="n">lock</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="n">obj</span><span class="o">.</span><span class="n">lock</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="k">class</span> <span class="nc">Example</span><span class="p">(</span><span class="n">LockableMixin</span><span class="p">):</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">write_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">with</span> <span class="n">obj_locker</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>            <span class="k">pass</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">read_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="k">pass</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="k">class</span> <span class="nc">TagDB</span><span class="p">(</span><span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - item hash; data - set of itemIDs</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - binItem</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="c1"># TODO: заменить список тегов на хеш единожды сохраненного списка тегов</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - sorted common TagsTuple&#39;s hash</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="c1"># TODO: убрать tagsNumPerItemID из кода. Заменить этот список itemID - на список hashOfTheTagHashTuple</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - number of tags in this ItemID group; data - set of itemIDs which are have</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>            <span class="c1"># needed number of tags</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - tag hash; data - binTag</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - Tag hash; data - set of itemIDs</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - Tag hash; data - quantity of the items with this tag</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - sorted TagsTuple</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span> <span class="o">=</span> <span class="p">{}</span>   <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - set of itemIDs</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - number of tags; data - set of TagsTuple hashes</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>   <span class="c1"># {tagQntInGroup1, tagQntInGroup2, ..., tagQntInGroupN} where</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="c1"># each Group is an key of the self.tagsQntPerCommonTagSet</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="c1"># TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="c1"># где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="c1"># TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}] и вычитывать это из него</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="c1"># и/или</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashTuple_1, hashOfTheTagHashTuple_2, ...</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="c1"># , hashOfTheTagHashTuple_N}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="c1"># где hashOfTheTagHashTuple - это tagHashTuple.__hash__()</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>            <span class="s1">&#39;items num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">),</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>            <span class="s1">&#39;tags num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">),</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="p">}</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="nf">get_root_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">_ROOT_TAG</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">add_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">binTag</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">remove_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="c1"># will try to delete given tag. If there is at least one item with this tag, than function will fail</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="c1"># and will return False; otherwise it will delete given tag and will return True.</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">if</span> <span class="n">functionResult</span><span class="p">:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="k">return</span> <span class="n">functionResult</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>        <span class="c1"># will add new item and return it&#39;s dynamic ID or None object If this Item already exist on the given tag path</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="c1"># the given binItem)  on this tag path</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="c1"># may raise an exception in this place. Nope - from now it will be not</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="p">()</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">binItem</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>            <span class="n">IDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="n">tagQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="k">if</span> <span class="n">tagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="c1"># self.tagsNumPerItemID[tagQnt] = itemIDsSet</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">add_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tagHash</span><span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="n">setOfItems</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="k">if</span> <span class="n">itemID</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">setOfItems</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                <span class="n">setOfItems</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">setOfItems</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>        <span class="n">sortedTagTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">binTagHashes</span><span class="p">))</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="n">hashOfTheSortedTagTuple</span> <span class="o">=</span> <span class="n">sortedTagTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">hashOfTheSortedTagTuple</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="n">sortedTagTuple</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="k">if</span> <span class="n">hashOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="c1"># self.itemsOnTheCommonTagSets[tagQnt] = itemIDsSet</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="n">lenOfTheSortedTagTuple</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sortedTagTuple</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>        <span class="k">if</span> <span class="n">lenOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="c1"># self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple] = itemIDsSet</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">}</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">remove_item_by_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="n">itemHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>                <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">tagTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="n">numberOfTags</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>            <span class="k">if</span> <span class="n">commonTagTupleHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>                <span class="c1"># self.itemsOnTheCommonTagSets[commonTagTupleHash] = IDsSet</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                    <span class="k">if</span> <span class="n">numberOfTags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                        <span class="n">setOfTagTuplesHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                        <span class="n">setOfTagTuplesHashes</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                        <span class="c1"># self.tagsQntPerCommonTagSet[numberOfTags] = setOfTagTuplesHashes</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagTuplesHashes</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="n">setOfTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagHashes</span><span class="p">)</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="k">if</span> <span class="n">tagsQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                <span class="c1"># self.tagsNumPerItemID[tagsQnt] = IDsSet</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">setOfTagHashes</span><span class="p">:</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>                    <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>                    <span class="n">tagsQuantity</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                        <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">tagsQuantity</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                    <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>                    <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>                    <span class="c1"># self.tagWithItems[tagHash] = IDsSet</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="o">.</span><span class="n">remove_id</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="c1"># will return ItemId for deleted item or None object if Item is not exist</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="c1"># the given binItem) on this tag path</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">remove_item_by_itemID</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>    <span class="k">def</span> <span class="nf">__OLD__get_itemID_from_item_and_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>        <span class="n">potentialIDs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">))</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">SMART_TREE_TYPE</span><span class="p">))</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        <span class="n">resultItemIDsList</span> <span class="o">=</span> <span class="n">potentialIDs</span> <span class="o">&amp;</span> <span class="n">itemIDsSet</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>            <span class="n">resultItemID</span> <span class="o">=</span> <span class="n">resultItemIDsList</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>  <span class="c1"># we have assume that we&#39;ll have only one item in intersection</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>                <span class="c1"># between potential IDs and Items that have (and have only) given tag list (without another tags in the</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                <span class="c1"># path to this items). We need to check it in the adding new item to the given tag path.</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>            <span class="k">return</span> <span class="n">resultItemID</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>            <span class="k">raise</span> <span class="n">ToManyIdenticalItemsOnTheGivenTagPathError</span><span class="p">()</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>    <span class="k">def</span> <span class="nf">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="n">potentialIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>        <span class="n">setOfBinTagsHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>            <span class="n">setOfBinTagsHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">potentialIDs</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="n">currentItemTagsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>            <span class="k">if</span> <span class="n">setOfBinTagsHashes</span> <span class="o">==</span> <span class="n">currentItemTagsSet</span><span class="p">:</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>                <span class="k">return</span> <span class="n">itemID</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashList</span><span class="p">):</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashList</span><span class="p">:</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">get_item_and_tags_from_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()}</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">))</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>    <span class="c1"># @profile</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="n">tagsQnt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>        <span class="k">if</span> <span class="n">local_tags_qnt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="n">tag_hash_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">tag_by_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="n">tag_by_qnt__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">tag_hash_set</span><span class="p">:</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>            <span class="n">qnt</span> <span class="o">=</span> <span class="n">tagsQnt</span><span class="p">[</span><span class="n">tag_hash</span><span class="p">]</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>            <span class="k">if</span> <span class="n">qnt</span> <span class="o">&gt;</span> <span class="n">biggest_qnt</span><span class="p">:</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>                <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="n">qnt</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>            <span class="c1"># if qnt not in tag_by_qnt:</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>            <span class="c1">#     tag_by_qnt[qnt] = set()</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>            <span class="c1"># tag_by_qnt[qnt].add(tag_hash)</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            <span class="n">tag_by_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">qnt</span><span class="p">,</span> <span class="n">tag_hash</span><span class="p">)</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>            <span class="c1"># biggest_qnt = max(tag_by_qnt)</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">[</span><span class="n">biggest_qnt</span><span class="p">])</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">sort_raw_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rawTagList</span><span class="p">):</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="c1"># will return sorted tag list</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">tagAndWeight</span><span class="p">:</span> <span class="n">tagAndWeight</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        <span class="k">for</span> <span class="n">rawTag</span> <span class="ow">in</span> <span class="n">rawTagList</span><span class="p">:</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">rawTag</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">get_itemIDs_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                              <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>        <span class="c1"># TODO: исправить ошибку: SMART_TREE_TYPE: возвращает не только список файлов в текущей директории, но и из</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>        <span class="c1"># непосредственных подпапок данной папки</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>        <span class="c1"># PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>            <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>            <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>            <span class="n">itemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">))</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>                <span class="n">itemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>            <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>                <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>                    <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>                    <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>            <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>                <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>                <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">commonTagHashSet</span><span class="p">):</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>                    <span class="n">itemIDSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">])</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>                <span class="c1"># # if len(tagHashSet &amp; commonTagHashSet) == len(tagHashSet):</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>                <span class="c1"># res_set = tagHashSet.intersection(commonTagHashSet)</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>                <span class="c1"># if len(res_set) == binTagsQnt:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>                <span class="c1">#     itemIDSet = itemIDSet | self.itemsOnTheCommonTagSets[commonTagGroupHash]</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>            <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="n">itemIDSet</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>            <span class="c1"># isFirstHash = True</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>            <span class="c1">#     tagHash = tag.__hash__()</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>            <span class="c1">#     if tagHash in self.tagWithItems:</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>            <span class="c1">#         if isFirstHash:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>            <span class="c1">#             interceptionOfItemsWithTags = self.tagWithItems[tagHash]</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>            <span class="c1">#             isFirstHash = False</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>            <span class="c1">#         else:</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="c1">#             itemsWithTag = self.tagWithItems[tagHash]</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>            <span class="c1">#             interceptionOfItemsWithTags = interceptionOfItemsWithTags &amp; itemsWithTag</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>            <span class="c1">#     else:</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>            <span class="c1">#         # TODO: произвести такую же провеку в get_items_from_tags() и build_smart_tree()</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>            <span class="c1">#         if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>            <span class="c1">#             result = (set(), set())</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>            <span class="c1">#             return result</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>            <span class="c1">#         else:</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>            <span class="c1">#             return set()</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="n">setOfAllInternalItemIDsForThisSetOfTags</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>        <span class="c1"># SMART_TREE_TYPE or FULL_TREE_TYPE</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>            <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">binTagHashTuple</span><span class="p">)</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>                <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>            <span class="c1"># filteredItemIDsSet = set()</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>            <span class="c1"># # for itemID in setOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>            <span class="c1"># #     if len(self.itemWithTags[itemID]) == tagQnt:</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>            <span class="c1"># #         # и вычитывать это из него</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>            <span class="c1"># #         # и/или</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashSet_1, hashOfTheTagHashSet_2, ...</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>            <span class="c1"># #         # , hashOfTheTagHashSet_3}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>            <span class="c1"># #         # где hashOfTheTagHashSet - это tagHashSet.__hash__()</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>            <span class="c1"># #         filteredItemIDsSet.add(itemID)</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>            <span class="c1"># if tagQnt in self.tagsNumPerItemID:</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>            <span class="c1">#     filteredItemIDsSet = setOfAllInternalItemIDsForThisSetOfTags &amp; self.tagsNumPerItemID[tagQnt]</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>            <span class="c1">#</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>            <span class="c1"># resultItemIDSet = set()</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>            <span class="c1"># for binTag in binTags:</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>            <span class="c1">#     tagHashSet.add(binTag.__hash__())</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>            <span class="c1"># for itemID in filteredItemIDsSet:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>            <span class="c1">#     commonTagTupleHash = self.itemWithTags[itemID]</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>            <span class="c1">#     tagSet = set(self.commonTagSets[commonTagTupleHash])</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>            <span class="c1">#     if tagSet == tagHashSet:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>            <span class="c1">#         # _TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>            <span class="c1">#         # где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>            <span class="c1">#         # _TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ...</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>            <span class="c1">#         # , itemID_3}]</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>            <span class="c1">#         resultItemIDSet.add(itemID)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">:</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>            <span class="c1"># already implemented (see bellow). Don&#39;t touch this code!</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>            <span class="k">pass</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">setOfAllInternalItemIDsForThisSetOfTags</span><span class="p">))</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">)</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>    <span class="k">def</span> <span class="nf">get_items_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>                            <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>        <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>  <span class="c1"># result == (usual items set, additional set of all</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                <span class="c1"># internal itemIDs)</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">:</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">)</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>    <span class="k">def</span> <span class="nf">get_tagHashes_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>                                <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>        <span class="c1"># where &quot;itemIDsSet&quot; is externally given &quot;get_itemIDs_from_tags(binTags, treeType=PLAIN_PSEUDO_TREE_TYPE)&quot;</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>        <span class="c1"># so &quot;itemIDsSet&quot; is a set of the all items inside the &quot;folder&quot; binTags (including items from &quot;subfolders&quot;)</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>        <span class="c1"># treeType - the same as in the &quot;get_items_from_tags()&quot; method</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>        <span class="c1"># prePreparedSetOfAllInternalItemIDsForThisSetOfTags can be generated by:</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE)</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>        <span class="c1">#   c) get_items_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>        <span class="c1">#   d) get_items_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE) || BUT: it&#39;ll return item set - not itemID</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>        <span class="c1">#       set</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>        <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>        <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>            <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>                <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>            <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>                <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>                    <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>                    <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>                    <span class="n">tagHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>            <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">tagHashSet</span> <span class="o">-</span> <span class="n">binTagHashes</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">:</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>            <span class="c1"># smartTree = self.build_smart_tree(binTags, prePreparedSetOfAllInternalItemIDs=setOfAllInternalItemIDs)</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>            <span class="n">smartTree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_smart_tree</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="n">setOfAllInternalItemIDs</span><span class="p">,</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>                                              <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="ow">in</span> <span class="n">smartTree</span><span class="p">:</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>                <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">smartTree</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>            <span class="c1"># filteredItemIDsList = list()</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>            <span class="c1"># for itemID in listOfAllInternalItemIDs:</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>            <span class="c1">#     if len(self.itemWithTags[itemID]) == (tagQnt + 1):</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>            <span class="c1">#         filteredItemIDsList.append(itemID)</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>            <span class="c1">#</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>            <span class="c1"># for itemID in filteredItemIDsList:</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>            <span class="c1">#     tagHashSet.update(set(self.itemWithTags[itemID]))</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>            <span class="c1"># givenTagHashes = set()</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>            <span class="c1">#     givenTagHashes.add(tag.__hash__())</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>            <span class="c1"># tagHashSet.difference_update(givenTagHashes)</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>            <span class="c1"># ##resultTagHashList = list(tagHashSet)</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>            <span class="c1"># # если остановиться тут - то мы увидим не все папки: мы не увидим папки непосредственно в которых есть</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>            <span class="c1"># # только другие подпапки, но ни одного файла.</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>            <span class="c1"># #</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>            <span class="c1"># # значит далее мы должны исключить все файлы, которые имеют только что найденные теги, и начать строить</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>            <span class="c1"># # древо тегов для оставшихся</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a>            <span class="c1"># #</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>            <span class="c1"># # а далее - повторить все это в цикле, увеличив при проверке кол-во тегов еще раз на единицу (и используя</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>            <span class="c1"># # уже оставшийся после отсеивания набор файлов). В итоге кол-во итераций зависит не от количества файлов,</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>            <span class="c1"># # а от максимальной фактически имеющейся вложенности файлов внутри тегов-каталогов</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">resultTagHashSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>    <span class="k">def</span> <span class="nf">get_tags_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagHashes_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a>
</span><span id="L-713"><a href="#L-713"><span class="linenos">713</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos">714</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos">715</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-716"><a href="#L-716"><span class="linenos">716</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos">717</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos">718</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-719"><a href="#L-719"><span class="linenos">719</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos">720</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos">721</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos">722</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos">723</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos">724</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-725"><a href="#L-725"><span class="linenos">725</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos">726</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos">727</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="L-728"><a href="#L-728"><span class="linenos">728</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos">729</span></a>
</span><span id="L-730"><a href="#L-730"><span class="linenos">730</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos">731</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos">732</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos">733</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos">734</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos">735</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos">736</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-737"><a href="#L-737"><span class="linenos">737</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos">738</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos">739</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-740"><a href="#L-740"><span class="linenos">740</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos">741</span></a>
</span><span id="L-742"><a href="#L-742"><span class="linenos">742</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos">743</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos">744</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-745"><a href="#L-745"><span class="linenos">745</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="L-746"><a href="#L-746"><span class="linenos">746</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-747"><a href="#L-747"><span class="linenos">747</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="L-748"><a href="#L-748"><span class="linenos">748</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos">749</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos">750</span></a>                    <span class="k">pass</span>
</span><span id="L-751"><a href="#L-751"><span class="linenos">751</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-752"><a href="#L-752"><span class="linenos">752</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos">753</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos">754</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-755"><a href="#L-755"><span class="linenos">755</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos">756</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos">757</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="L-758"><a href="#L-758"><span class="linenos">758</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="L-759"><a href="#L-759"><span class="linenos">759</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos">760</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="L-761"><a href="#L-761"><span class="linenos">761</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="L-762"><a href="#L-762"><span class="linenos">762</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos">763</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos">764</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="L-765"><a href="#L-765"><span class="linenos">765</span></a>
</span><span id="L-766"><a href="#L-766"><span class="linenos">766</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree_2</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos">767</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos">768</span></a>
</span><span id="L-769"><a href="#L-769"><span class="linenos">769</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos">770</span></a>
</span><span id="L-771"><a href="#L-771"><span class="linenos">771</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="L-772"><a href="#L-772"><span class="linenos">772</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos">773</span></a>
</span><span id="L-774"><a href="#L-774"><span class="linenos">774</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos">775</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="L-776"><a href="#L-776"><span class="linenos">776</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-777"><a href="#L-777"><span class="linenos">777</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos">778</span></a>
</span><span id="L-779"><a href="#L-779"><span class="linenos">779</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos">780</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="L-781"><a href="#L-781"><span class="linenos">781</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-782"><a href="#L-782"><span class="linenos">782</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos">783</span></a>
</span><span id="L-784"><a href="#L-784"><span class="linenos">784</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="L-785"><a href="#L-785"><span class="linenos">785</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="L-786"><a href="#L-786"><span class="linenos">786</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos">787</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="L-788"><a href="#L-788"><span class="linenos">788</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="L-789"><a href="#L-789"><span class="linenos">789</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-790"><a href="#L-790"><span class="linenos">790</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos">791</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos">792</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos">793</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos">794</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="L-795"><a href="#L-795"><span class="linenos">795</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos">796</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="L-797"><a href="#L-797"><span class="linenos">797</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="L-798"><a href="#L-798"><span class="linenos">798</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="L-799"><a href="#L-799"><span class="linenos">799</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos">800</span></a>
</span><span id="L-801"><a href="#L-801"><span class="linenos">801</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos">802</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos">803</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-804"><a href="#L-804"><span class="linenos">804</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-805"><a href="#L-805"><span class="linenos">805</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos">806</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos">807</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-808"><a href="#L-808"><span class="linenos">808</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos">809</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos">810</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-811"><a href="#L-811"><span class="linenos">811</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="L-812"><a href="#L-812"><span class="linenos">812</span></a>
</span><span id="L-813"><a href="#L-813"><span class="linenos">813</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos">814</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-815"><a href="#L-815"><span class="linenos">815</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-816"><a href="#L-816"><span class="linenos">816</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos">817</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos">818</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos">819</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="L-820"><a href="#L-820"><span class="linenos">820</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="L-821"><a href="#L-821"><span class="linenos">821</span></a>                    <span class="k">pass</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos">822</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-823"><a href="#L-823"><span class="linenos">823</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-824"><a href="#L-824"><span class="linenos">824</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-825"><a href="#L-825"><span class="linenos">825</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-826"><a href="#L-826"><span class="linenos">826</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos">827</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="L-828"><a href="#L-828"><span class="linenos">828</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="L-829"><a href="#L-829"><span class="linenos">829</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="L-830"><a href="#L-830"><span class="linenos">830</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="L-831"><a href="#L-831"><span class="linenos">831</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="L-832"><a href="#L-832"><span class="linenos">832</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos">833</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos">834</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="L-835"><a href="#L-835"><span class="linenos">835</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="L-836"><a href="#L-836"><span class="linenos">836</span></a>
</span><span id="L-837"><a href="#L-837"><span class="linenos">837</span></a>    <span class="k">def</span> <span class="nf">get_all_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos">838</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-839"><a href="#L-839"><span class="linenos">839</span></a>        <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="L-840"><a href="#L-840"><span class="linenos">840</span></a>                                         <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-841"><a href="#L-841"><span class="linenos">841</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-842"><a href="#L-842"><span class="linenos">842</span></a>            <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="L-843"><a href="#L-843"><span class="linenos">843</span></a>                                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-844"><a href="#L-844"><span class="linenos">844</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">tags</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="L-845"><a href="#L-845"><span class="linenos">845</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-846"><a href="#L-846"><span class="linenos">846</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-847"><a href="#L-847"><span class="linenos">847</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(),</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="L-848"><a href="#L-848"><span class="linenos">848</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-849"><a href="#L-849"><span class="linenos">849</span></a>
</span><span id="L-850"><a href="#L-850"><span class="linenos">850</span></a>    <span class="k">def</span> <span class="nf">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-851"><a href="#L-851"><span class="linenos">851</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="L-852"><a href="#L-852"><span class="linenos">852</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="L-853"><a href="#L-853"><span class="linenos">853</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="L-854"><a href="#L-854"><span class="linenos">854</span></a>            <span class="k">if</span> <span class="n">isWithoutRootHash</span><span class="p">:</span>
</span><span id="L-855"><a href="#L-855"><span class="linenos">855</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="L-856"><a href="#L-856"><span class="linenos">856</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-857"><a href="#L-857"><span class="linenos">857</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="L-858"><a href="#L-858"><span class="linenos">858</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-859"><a href="#L-859"><span class="linenos">859</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-860"><a href="#L-860"><span class="linenos">860</span></a>
</span><span id="L-861"><a href="#L-861"><span class="linenos">861</span></a>    <span class="k">def</span> <span class="nf">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="L-862"><a href="#L-862"><span class="linenos">862</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="L-863"><a href="#L-863"><span class="linenos">863</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="L-864"><a href="#L-864"><span class="linenos">864</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">])</span>
</span><span id="L-865"><a href="#L-865"><span class="linenos">865</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-866"><a href="#L-866"><span class="linenos">866</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-867"><a href="#L-867"><span class="linenos">867</span></a>
</span><span id="L-868"><a href="#L-868"><span class="linenos">868</span></a>    <span class="k">def</span> <span class="nf">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-869"><a href="#L-869"><span class="linenos">869</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-870"><a href="#L-870"><span class="linenos">870</span></a>
</span><span id="L-871"><a href="#L-871"><span class="linenos">871</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-872"><a href="#L-872"><span class="linenos">872</span></a>
</span><span id="L-873"><a href="#L-873"><span class="linenos">873</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-874"><a href="#L-874"><span class="linenos">874</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="L-875"><a href="#L-875"><span class="linenos">875</span></a>
</span><span id="L-876"><a href="#L-876"><span class="linenos">876</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-877"><a href="#L-877"><span class="linenos">877</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="L-878"><a href="#L-878"><span class="linenos">878</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-879"><a href="#L-879"><span class="linenos">879</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="L-880"><a href="#L-880"><span class="linenos">880</span></a>
</span><span id="L-881"><a href="#L-881"><span class="linenos">881</span></a>        <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="L-882"><a href="#L-882"><span class="linenos">882</span></a>        <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-883"><a href="#L-883"><span class="linenos">883</span></a>        <span class="c1"># setOfLenOfTheCommonTagHashSetForChecking = set()</span>
</span><span id="L-884"><a href="#L-884"><span class="linenos">884</span></a>        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-885"><a href="#L-885"><span class="linenos">885</span></a>        <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="L-886"><a href="#L-886"><span class="linenos">886</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-887"><a href="#L-887"><span class="linenos">887</span></a>            <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="L-888"><a href="#L-888"><span class="linenos">888</span></a>                <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="L-889"><a href="#L-889"><span class="linenos">889</span></a>                <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="L-890"><a href="#L-890"><span class="linenos">890</span></a>        <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="L-891"><a href="#L-891"><span class="linenos">891</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-892"><a href="#L-892"><span class="linenos">892</span></a>            <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="L-893"><a href="#L-893"><span class="linenos">893</span></a>            <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="L-894"><a href="#L-894"><span class="linenos">894</span></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="L-895"><a href="#L-895"><span class="linenos">895</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span> <span class="o">!=</span> <span class="n">commonTagHashSet</span><span class="p">:</span>
</span><span id="L-896"><a href="#L-896"><span class="linenos">896</span></a>                    <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-897"><a href="#L-897"><span class="linenos">897</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">commonTagHashSet</span>
</span><span id="L-898"><a href="#L-898"><span class="linenos">898</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-899"><a href="#L-899"><span class="linenos">899</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span>
</span><span id="L-900"><a href="#L-900"><span class="linenos">900</span></a>        <span class="c1">#         if tagHashSet != commonTagHashSet:</span>
</span><span id="L-901"><a href="#L-901"><span class="linenos">901</span></a>        <span class="c1">#             setOfLenOfTheCommonTagHashSetForChecking.add(len(commonTagHashSet))</span>
</span><span id="L-902"><a href="#L-902"><span class="linenos">902</span></a>        <span class="c1"># minimalTagPath = min(setOfLenOfTheCommonTagHashSetForChecking)</span>
</span><span id="L-903"><a href="#L-903"><span class="linenos">903</span></a>        <span class="c1"># pathDiff = minimalTagPath - len(tagHashSet)</span>
</span><span id="L-904"><a href="#L-904"><span class="linenos">904</span></a>        <span class="c1"># if pathDiff &gt; 0:</span>
</span><span id="L-905"><a href="#L-905"><span class="linenos">905</span></a>        <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-906"><a href="#L-906"><span class="linenos">906</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-907"><a href="#L-907"><span class="linenos">907</span></a>
</span><span id="L-908"><a href="#L-908"><span class="linenos">908</span></a>        <span class="n">setOfTheTagsForAReduction</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">-</span> <span class="n">tagHashSet</span>
</span><span id="L-909"><a href="#L-909"><span class="linenos">909</span></a>
</span><span id="L-910"><a href="#L-910"><span class="linenos">910</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTheTagsForAReduction</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="L-911"><a href="#L-911"><span class="linenos">911</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span><span id="L-912"><a href="#L-912"><span class="linenos">912</span></a>
</span><span id="L-913"><a href="#L-913"><span class="linenos">913</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="L-914"><a href="#L-914"><span class="linenos">914</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="L-915"><a href="#L-915"><span class="linenos">915</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span></pre></div>


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
                <section id="LockableMixin">
                            <input id="LockableMixin-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">LockableMixin</span>:

                <label class="view-source-button" for="LockableMixin-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LockableMixin"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LockableMixin-75"><a href="#LockableMixin-75"><span class="linenos">75</span></a><span class="k">class</span> <span class="nc">LockableMixin</span><span class="p">:</span>
</span><span id="LockableMixin-76"><a href="#LockableMixin-76"><span class="linenos">76</span></a>    <span class="nd">@property</span>
</span><span id="LockableMixin-77"><a href="#LockableMixin-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LockableMixin-78"><a href="#LockableMixin-78"><span class="linenos">78</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="LockableMixin-79"><a href="#LockableMixin-79"><span class="linenos">79</span></a>    
</span><span id="LockableMixin-80"><a href="#LockableMixin-80"><span class="linenos">80</span></a>    <span class="nd">@lock</span><span class="o">.</span><span class="n">setter</span>
</span><span id="LockableMixin-81"><a href="#LockableMixin-81"><span class="linenos">81</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LockableMixin-82"><a href="#LockableMixin-82"><span class="linenos">82</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="LockableMixin.lock" class="classattr">
                                        <input id="LockableMixin.lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">lock</span><span class="annotation">: bool</span>

                <label class="view-source-button" for="LockableMixin.lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#LockableMixin.lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="LockableMixin.lock-76"><a href="#LockableMixin.lock-76"><span class="linenos">76</span></a>    <span class="nd">@property</span>
</span><span id="LockableMixin.lock-77"><a href="#LockableMixin.lock-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="LockableMixin.lock-78"><a href="#LockableMixin.lock-78"><span class="linenos">78</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="obj_locker">
                            <input id="obj_locker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@contextmanager</div>

        <span class="def">def</span>
        <span class="name">obj_locker</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n"><a href="#LockableMixin">LockableMixin</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="obj_locker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#obj_locker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="obj_locker-85"><a href="#obj_locker-85"><span class="linenos">85</span></a><span class="nd">@contextmanager</span>
</span><span id="obj_locker-86"><a href="#obj_locker-86"><span class="linenos">86</span></a><span class="k">def</span> <span class="nf">obj_locker</span><span class="p">(</span><span class="n">obj</span><span class="p">:</span> <span class="n">LockableMixin</span><span class="p">):</span>
</span><span id="obj_locker-87"><a href="#obj_locker-87"><span class="linenos">87</span></a>    <span class="n">obj</span><span class="o">.</span><span class="n">lock</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="obj_locker-88"><a href="#obj_locker-88"><span class="linenos">88</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="obj_locker-89"><a href="#obj_locker-89"><span class="linenos">89</span></a>        <span class="k">yield</span> <span class="n">obj</span><span class="o">.</span><span class="n">lock</span>
</span><span id="obj_locker-90"><a href="#obj_locker-90"><span class="linenos">90</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="obj_locker-91"><a href="#obj_locker-91"><span class="linenos">91</span></a>        <span class="n">obj</span><span class="o">.</span><span class="n">lock</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="Example">
                            <input id="Example-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Example</span><wbr>(<span class="base"><a href="#LockableMixin">LockableMixin</a></span>):

                <label class="view-source-button" for="Example-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Example"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Example-94"><a href="#Example-94"><span class="linenos"> 94</span></a><span class="k">class</span> <span class="nc">Example</span><span class="p">(</span><span class="n">LockableMixin</span><span class="p">):</span>
</span><span id="Example-95"><a href="#Example-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Example-96"><a href="#Example-96"><span class="linenos"> 96</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="Example-97"><a href="#Example-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="Example-98"><a href="#Example-98"><span class="linenos"> 98</span></a>    
</span><span id="Example-99"><a href="#Example-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">write_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example-100"><a href="#Example-100"><span class="linenos">100</span></a>        <span class="k">with</span> <span class="n">obj_locker</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example-101"><a href="#Example-101"><span class="linenos">101</span></a>            <span class="k">pass</span>
</span><span id="Example-102"><a href="#Example-102"><span class="linenos">102</span></a>    
</span><span id="Example-103"><a href="#Example-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">read_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example-104"><a href="#Example-104"><span class="linenos">104</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
</span><span id="Example-105"><a href="#Example-105"><span class="linenos">105</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            <div id="Example.lock" class="classattr">
                                        <input id="Example.lock-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">lock</span><span class="annotation">: bool</span>

                <label class="view-source-button" for="Example.lock-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Example.lock"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Example.lock-76"><a href="#Example.lock-76"><span class="linenos">76</span></a>    <span class="nd">@property</span>
</span><span id="Example.lock-77"><a href="#Example.lock-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">lock</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="Example.lock-78"><a href="#Example.lock-78"><span class="linenos">78</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="Example.write_coroutine" class="classattr">
                                        <input id="Example.write_coroutine-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">write_coroutine</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Example.write_coroutine-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Example.write_coroutine"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Example.write_coroutine-99"><a href="#Example.write_coroutine-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">write_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example.write_coroutine-100"><a href="#Example.write_coroutine-100"><span class="linenos">100</span></a>        <span class="k">with</span> <span class="n">obj_locker</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example.write_coroutine-101"><a href="#Example.write_coroutine-101"><span class="linenos">101</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="Example.read_coroutine" class="classattr">
                                        <input id="Example.read_coroutine-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_coroutine</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Example.read_coroutine-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Example.read_coroutine"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Example.read_coroutine-103"><a href="#Example.read_coroutine-103"><span class="linenos">103</span></a>    <span class="k">def</span> <span class="nf">read_coroutine</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Example.read_coroutine-104"><a href="#Example.read_coroutine-104"><span class="linenos">104</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lock</span><span class="p">:</span>
</span><span id="Example.read_coroutine-105"><a href="#Example.read_coroutine-105"><span class="linenos">105</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TagDB">
                            <input id="TagDB-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TagDB</span><wbr>(<span class="base">cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</span>):

                <label class="view-source-button" for="TagDB-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB-108"><a href="#TagDB-108"><span class="linenos">108</span></a><span class="k">class</span> <span class="nc">TagDB</span><span class="p">(</span><span class="n">EntityStatsMixin</span><span class="p">):</span>
</span><span id="TagDB-109"><a href="#TagDB-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="TagDB-110"><a href="#TagDB-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="TagDB-111"><a href="#TagDB-111"><span class="linenos">111</span></a>
</span><span id="TagDB-112"><a href="#TagDB-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="TagDB-113"><a href="#TagDB-113"><span class="linenos">113</span></a>
</span><span id="TagDB-114"><a href="#TagDB-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - item hash; data - set of itemIDs</span>
</span><span id="TagDB-115"><a href="#TagDB-115"><span class="linenos">115</span></a>
</span><span id="TagDB-116"><a href="#TagDB-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - binItem</span>
</span><span id="TagDB-117"><a href="#TagDB-117"><span class="linenos">117</span></a>        <span class="c1"># TODO: заменить список тегов на хеш единожды сохраненного списка тегов</span>
</span><span id="TagDB-118"><a href="#TagDB-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - sorted common TagsTuple&#39;s hash</span>
</span><span id="TagDB-119"><a href="#TagDB-119"><span class="linenos">119</span></a>
</span><span id="TagDB-120"><a href="#TagDB-120"><span class="linenos">120</span></a>        <span class="c1"># TODO: убрать tagsNumPerItemID из кода. Заменить этот список itemID - на список hashOfTheTagHashTuple</span>
</span><span id="TagDB-121"><a href="#TagDB-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - number of tags in this ItemID group; data - set of itemIDs which are have</span>
</span><span id="TagDB-122"><a href="#TagDB-122"><span class="linenos">122</span></a>            <span class="c1"># needed number of tags</span>
</span><span id="TagDB-123"><a href="#TagDB-123"><span class="linenos">123</span></a>
</span><span id="TagDB-124"><a href="#TagDB-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - tag hash; data - binTag</span>
</span><span id="TagDB-125"><a href="#TagDB-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - Tag hash; data - set of itemIDs</span>
</span><span id="TagDB-126"><a href="#TagDB-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - Tag hash; data - quantity of the items with this tag</span>
</span><span id="TagDB-127"><a href="#TagDB-127"><span class="linenos">127</span></a>
</span><span id="TagDB-128"><a href="#TagDB-128"><span class="linenos">128</span></a>
</span><span id="TagDB-129"><a href="#TagDB-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - sorted TagsTuple</span>
</span><span id="TagDB-130"><a href="#TagDB-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span> <span class="o">=</span> <span class="p">{}</span>   <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - set of itemIDs</span>
</span><span id="TagDB-131"><a href="#TagDB-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - number of tags; data - set of TagsTuple hashes</span>
</span><span id="TagDB-132"><a href="#TagDB-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>   <span class="c1"># {tagQntInGroup1, tagQntInGroup2, ..., tagQntInGroupN} where</span>
</span><span id="TagDB-133"><a href="#TagDB-133"><span class="linenos">133</span></a>            <span class="c1"># each Group is an key of the self.tagsQntPerCommonTagSet</span>
</span><span id="TagDB-134"><a href="#TagDB-134"><span class="linenos">134</span></a>
</span><span id="TagDB-135"><a href="#TagDB-135"><span class="linenos">135</span></a>        <span class="c1"># TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="TagDB-136"><a href="#TagDB-136"><span class="linenos">136</span></a>        <span class="c1"># где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="TagDB-137"><a href="#TagDB-137"><span class="linenos">137</span></a>        <span class="c1"># TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="TagDB-138"><a href="#TagDB-138"><span class="linenos">138</span></a>
</span><span id="TagDB-139"><a href="#TagDB-139"><span class="linenos">139</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}] и вычитывать это из него</span>
</span><span id="TagDB-140"><a href="#TagDB-140"><span class="linenos">140</span></a>        <span class="c1"># и/или</span>
</span><span id="TagDB-141"><a href="#TagDB-141"><span class="linenos">141</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashTuple_1, hashOfTheTagHashTuple_2, ...</span>
</span><span id="TagDB-142"><a href="#TagDB-142"><span class="linenos">142</span></a>        <span class="c1"># , hashOfTheTagHashTuple_N}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="TagDB-143"><a href="#TagDB-143"><span class="linenos">143</span></a>        <span class="c1"># где hashOfTheTagHashTuple - это tagHashTuple.__hash__()</span>
</span><span id="TagDB-144"><a href="#TagDB-144"><span class="linenos">144</span></a>
</span><span id="TagDB-145"><a href="#TagDB-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="TagDB-146"><a href="#TagDB-146"><span class="linenos">146</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="TagDB-147"><a href="#TagDB-147"><span class="linenos">147</span></a>            <span class="s1">&#39;items num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">),</span>
</span><span id="TagDB-148"><a href="#TagDB-148"><span class="linenos">148</span></a>            <span class="s1">&#39;tags num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">),</span>
</span><span id="TagDB-149"><a href="#TagDB-149"><span class="linenos">149</span></a>        <span class="p">}</span>
</span><span id="TagDB-150"><a href="#TagDB-150"><span class="linenos">150</span></a>
</span><span id="TagDB-151"><a href="#TagDB-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">get_root_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TagDB-152"><a href="#TagDB-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">_ROOT_TAG</span><span class="p">)</span>
</span><span id="TagDB-153"><a href="#TagDB-153"><span class="linenos">153</span></a>
</span><span id="TagDB-154"><a href="#TagDB-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">add_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="TagDB-155"><a href="#TagDB-155"><span class="linenos">155</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-156"><a href="#TagDB-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">binTag</span>
</span><span id="TagDB-157"><a href="#TagDB-157"><span class="linenos">157</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="TagDB-158"><a href="#TagDB-158"><span class="linenos">158</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB-159"><a href="#TagDB-159"><span class="linenos">159</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB-160"><a href="#TagDB-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-161"><a href="#TagDB-161"><span class="linenos">161</span></a>
</span><span id="TagDB-162"><a href="#TagDB-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">remove_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="TagDB-163"><a href="#TagDB-163"><span class="linenos">163</span></a>        <span class="c1"># will try to delete given tag. If there is at least one item with this tag, than function will fail</span>
</span><span id="TagDB-164"><a href="#TagDB-164"><span class="linenos">164</span></a>        <span class="c1"># and will return False; otherwise it will delete given tag and will return True.</span>
</span><span id="TagDB-165"><a href="#TagDB-165"><span class="linenos">165</span></a>        <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TagDB-166"><a href="#TagDB-166"><span class="linenos">166</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-167"><a href="#TagDB-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="TagDB-168"><a href="#TagDB-168"><span class="linenos">168</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB-169"><a href="#TagDB-169"><span class="linenos">169</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB-170"><a href="#TagDB-170"><span class="linenos">170</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-171"><a href="#TagDB-171"><span class="linenos">171</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-172"><a href="#TagDB-172"><span class="linenos">172</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TagDB-173"><a href="#TagDB-173"><span class="linenos">173</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-174"><a href="#TagDB-174"><span class="linenos">174</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TagDB-175"><a href="#TagDB-175"><span class="linenos">175</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-176"><a href="#TagDB-176"><span class="linenos">176</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-177"><a href="#TagDB-177"><span class="linenos">177</span></a>                <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TagDB-178"><a href="#TagDB-178"><span class="linenos">178</span></a>
</span><span id="TagDB-179"><a href="#TagDB-179"><span class="linenos">179</span></a>        <span class="k">if</span> <span class="n">functionResult</span><span class="p">:</span>
</span><span id="TagDB-180"><a href="#TagDB-180"><span class="linenos">180</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB-181"><a href="#TagDB-181"><span class="linenos">181</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-182"><a href="#TagDB-182"><span class="linenos">182</span></a>
</span><span id="TagDB-183"><a href="#TagDB-183"><span class="linenos">183</span></a>        <span class="k">return</span> <span class="n">functionResult</span>
</span><span id="TagDB-184"><a href="#TagDB-184"><span class="linenos">184</span></a>
</span><span id="TagDB-185"><a href="#TagDB-185"><span class="linenos">185</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB-186"><a href="#TagDB-186"><span class="linenos">186</span></a>        <span class="c1"># will add new item and return it&#39;s dynamic ID or None object If this Item already exist on the given tag path</span>
</span><span id="TagDB-187"><a href="#TagDB-187"><span class="linenos">187</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="TagDB-188"><a href="#TagDB-188"><span class="linenos">188</span></a>        <span class="c1"># the given binItem)  on this tag path</span>
</span><span id="TagDB-189"><a href="#TagDB-189"><span class="linenos">189</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-190"><a href="#TagDB-190"><span class="linenos">190</span></a>
</span><span id="TagDB-191"><a href="#TagDB-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-192"><a href="#TagDB-192"><span class="linenos">192</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-193"><a href="#TagDB-193"><span class="linenos">193</span></a>
</span><span id="TagDB-194"><a href="#TagDB-194"><span class="linenos">194</span></a>        <span class="c1"># may raise an exception in this place. Nope - from now it will be not</span>
</span><span id="TagDB-195"><a href="#TagDB-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-196"><a href="#TagDB-196"><span class="linenos">196</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="TagDB-197"><a href="#TagDB-197"><span class="linenos">197</span></a>
</span><span id="TagDB-198"><a href="#TagDB-198"><span class="linenos">198</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="p">()</span>
</span><span id="TagDB-199"><a href="#TagDB-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">binItem</span>
</span><span id="TagDB-200"><a href="#TagDB-200"><span class="linenos">200</span></a>
</span><span id="TagDB-201"><a href="#TagDB-201"><span class="linenos">201</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-202"><a href="#TagDB-202"><span class="linenos">202</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB-203"><a href="#TagDB-203"><span class="linenos">203</span></a>            <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB-204"><a href="#TagDB-204"><span class="linenos">204</span></a>            <span class="n">IDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-205"><a href="#TagDB-205"><span class="linenos">205</span></a>            <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="TagDB-206"><a href="#TagDB-206"><span class="linenos">206</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-207"><a href="#TagDB-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB-208"><a href="#TagDB-208"><span class="linenos">208</span></a>
</span><span id="TagDB-209"><a href="#TagDB-209"><span class="linenos">209</span></a>        <span class="n">tagQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-210"><a href="#TagDB-210"><span class="linenos">210</span></a>        <span class="k">if</span> <span class="n">tagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="TagDB-211"><a href="#TagDB-211"><span class="linenos">211</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span>
</span><span id="TagDB-212"><a href="#TagDB-212"><span class="linenos">212</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-213"><a href="#TagDB-213"><span class="linenos">213</span></a>            <span class="c1"># self.tagsNumPerItemID[tagQnt] = itemIDsSet</span>
</span><span id="TagDB-214"><a href="#TagDB-214"><span class="linenos">214</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-215"><a href="#TagDB-215"><span class="linenos">215</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB-216"><a href="#TagDB-216"><span class="linenos">216</span></a>
</span><span id="TagDB-217"><a href="#TagDB-217"><span class="linenos">217</span></a>        <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-218"><a href="#TagDB-218"><span class="linenos">218</span></a>
</span><span id="TagDB-219"><a href="#TagDB-219"><span class="linenos">219</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-220"><a href="#TagDB-220"><span class="linenos">220</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">add_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="TagDB-221"><a href="#TagDB-221"><span class="linenos">221</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-222"><a href="#TagDB-222"><span class="linenos">222</span></a>            <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB-223"><a href="#TagDB-223"><span class="linenos">223</span></a>            <span class="n">setOfItems</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-224"><a href="#TagDB-224"><span class="linenos">224</span></a>            <span class="k">if</span> <span class="n">itemID</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">setOfItems</span><span class="p">:</span>
</span><span id="TagDB-225"><a href="#TagDB-225"><span class="linenos">225</span></a>                <span class="n">setOfItems</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-226"><a href="#TagDB-226"><span class="linenos">226</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB-227"><a href="#TagDB-227"><span class="linenos">227</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB-228"><a href="#TagDB-228"><span class="linenos">228</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-229"><a href="#TagDB-229"><span class="linenos">229</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="TagDB-230"><a href="#TagDB-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">setOfItems</span>
</span><span id="TagDB-231"><a href="#TagDB-231"><span class="linenos">231</span></a>
</span><span id="TagDB-232"><a href="#TagDB-232"><span class="linenos">232</span></a>        <span class="n">sortedTagTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">binTagHashes</span><span class="p">))</span>
</span><span id="TagDB-233"><a href="#TagDB-233"><span class="linenos">233</span></a>        <span class="n">hashOfTheSortedTagTuple</span> <span class="o">=</span> <span class="n">sortedTagTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-234"><a href="#TagDB-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">hashOfTheSortedTagTuple</span>
</span><span id="TagDB-235"><a href="#TagDB-235"><span class="linenos">235</span></a>
</span><span id="TagDB-236"><a href="#TagDB-236"><span class="linenos">236</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="n">sortedTagTuple</span>
</span><span id="TagDB-237"><a href="#TagDB-237"><span class="linenos">237</span></a>
</span><span id="TagDB-238"><a href="#TagDB-238"><span class="linenos">238</span></a>        <span class="k">if</span> <span class="n">hashOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB-239"><a href="#TagDB-239"><span class="linenos">239</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="TagDB-240"><a href="#TagDB-240"><span class="linenos">240</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-241"><a href="#TagDB-241"><span class="linenos">241</span></a>            <span class="c1"># self.itemsOnTheCommonTagSets[tagQnt] = itemIDsSet</span>
</span><span id="TagDB-242"><a href="#TagDB-242"><span class="linenos">242</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-243"><a href="#TagDB-243"><span class="linenos">243</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB-244"><a href="#TagDB-244"><span class="linenos">244</span></a>
</span><span id="TagDB-245"><a href="#TagDB-245"><span class="linenos">245</span></a>        <span class="n">lenOfTheSortedTagTuple</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB-246"><a href="#TagDB-246"><span class="linenos">246</span></a>        <span class="k">if</span> <span class="n">lenOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="TagDB-247"><a href="#TagDB-247"><span class="linenos">247</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="TagDB-248"><a href="#TagDB-248"><span class="linenos">248</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB-249"><a href="#TagDB-249"><span class="linenos">249</span></a>            <span class="c1"># self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple] = itemIDsSet</span>
</span><span id="TagDB-250"><a href="#TagDB-250"><span class="linenos">250</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-251"><a href="#TagDB-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">}</span>
</span><span id="TagDB-252"><a href="#TagDB-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB-253"><a href="#TagDB-253"><span class="linenos">253</span></a>
</span><span id="TagDB-254"><a href="#TagDB-254"><span class="linenos">254</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span><span id="TagDB-255"><a href="#TagDB-255"><span class="linenos">255</span></a>
</span><span id="TagDB-256"><a href="#TagDB-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="nf">remove_item_by_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="TagDB-257"><a href="#TagDB-257"><span class="linenos">257</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-258"><a href="#TagDB-258"><span class="linenos">258</span></a>
</span><span id="TagDB-259"><a href="#TagDB-259"><span class="linenos">259</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">:</span>
</span><span id="TagDB-260"><a href="#TagDB-260"><span class="linenos">260</span></a>            <span class="n">itemHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-261"><a href="#TagDB-261"><span class="linenos">261</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-262"><a href="#TagDB-262"><span class="linenos">262</span></a>
</span><span id="TagDB-263"><a href="#TagDB-263"><span class="linenos">263</span></a>            <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB-264"><a href="#TagDB-264"><span class="linenos">264</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB-265"><a href="#TagDB-265"><span class="linenos">265</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB-266"><a href="#TagDB-266"><span class="linenos">266</span></a>                <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="TagDB-267"><a href="#TagDB-267"><span class="linenos">267</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-268"><a href="#TagDB-268"><span class="linenos">268</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB-269"><a href="#TagDB-269"><span class="linenos">269</span></a>
</span><span id="TagDB-270"><a href="#TagDB-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB-271"><a href="#TagDB-271"><span class="linenos">271</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-272"><a href="#TagDB-272"><span class="linenos">272</span></a>            <span class="n">tagTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB-273"><a href="#TagDB-273"><span class="linenos">273</span></a>            <span class="n">numberOfTags</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="TagDB-274"><a href="#TagDB-274"><span class="linenos">274</span></a>
</span><span id="TagDB-275"><a href="#TagDB-275"><span class="linenos">275</span></a>            <span class="k">if</span> <span class="n">commonTagTupleHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB-276"><a href="#TagDB-276"><span class="linenos">276</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB-277"><a href="#TagDB-277"><span class="linenos">277</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB-278"><a href="#TagDB-278"><span class="linenos">278</span></a>                <span class="c1"># self.itemsOnTheCommonTagSets[commonTagTupleHash] = IDsSet</span>
</span><span id="TagDB-279"><a href="#TagDB-279"><span class="linenos">279</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-280"><a href="#TagDB-280"><span class="linenos">280</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB-281"><a href="#TagDB-281"><span class="linenos">281</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB-282"><a href="#TagDB-282"><span class="linenos">282</span></a>                    <span class="k">if</span> <span class="n">numberOfTags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="TagDB-283"><a href="#TagDB-283"><span class="linenos">283</span></a>                        <span class="n">setOfTagTuplesHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="TagDB-284"><a href="#TagDB-284"><span class="linenos">284</span></a>                        <span class="n">setOfTagTuplesHashes</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="TagDB-285"><a href="#TagDB-285"><span class="linenos">285</span></a>                        <span class="c1"># self.tagsQntPerCommonTagSet[numberOfTags] = setOfTagTuplesHashes</span>
</span><span id="TagDB-286"><a href="#TagDB-286"><span class="linenos">286</span></a>                        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagTuplesHashes</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-287"><a href="#TagDB-287"><span class="linenos">287</span></a>                            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="TagDB-288"><a href="#TagDB-288"><span class="linenos">288</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="TagDB-289"><a href="#TagDB-289"><span class="linenos">289</span></a>
</span><span id="TagDB-290"><a href="#TagDB-290"><span class="linenos">290</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-291"><a href="#TagDB-291"><span class="linenos">291</span></a>
</span><span id="TagDB-292"><a href="#TagDB-292"><span class="linenos">292</span></a>            <span class="n">setOfTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="TagDB-293"><a href="#TagDB-293"><span class="linenos">293</span></a>
</span><span id="TagDB-294"><a href="#TagDB-294"><span class="linenos">294</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagHashes</span><span class="p">)</span>
</span><span id="TagDB-295"><a href="#TagDB-295"><span class="linenos">295</span></a>            <span class="k">if</span> <span class="n">tagsQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="TagDB-296"><a href="#TagDB-296"><span class="linenos">296</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="TagDB-297"><a href="#TagDB-297"><span class="linenos">297</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB-298"><a href="#TagDB-298"><span class="linenos">298</span></a>                <span class="c1"># self.tagsNumPerItemID[tagsQnt] = IDsSet</span>
</span><span id="TagDB-299"><a href="#TagDB-299"><span class="linenos">299</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-300"><a href="#TagDB-300"><span class="linenos">300</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="TagDB-301"><a href="#TagDB-301"><span class="linenos">301</span></a>
</span><span id="TagDB-302"><a href="#TagDB-302"><span class="linenos">302</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">setOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB-303"><a href="#TagDB-303"><span class="linenos">303</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-304"><a href="#TagDB-304"><span class="linenos">304</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB-305"><a href="#TagDB-305"><span class="linenos">305</span></a>                    <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-306"><a href="#TagDB-306"><span class="linenos">306</span></a>                    <span class="n">tagsQuantity</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="TagDB-307"><a href="#TagDB-307"><span class="linenos">307</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-308"><a href="#TagDB-308"><span class="linenos">308</span></a>                        <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB-309"><a href="#TagDB-309"><span class="linenos">309</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">tagsQuantity</span>
</span><span id="TagDB-310"><a href="#TagDB-310"><span class="linenos">310</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-311"><a href="#TagDB-311"><span class="linenos">311</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-312"><a href="#TagDB-312"><span class="linenos">312</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-313"><a href="#TagDB-313"><span class="linenos">313</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB-314"><a href="#TagDB-314"><span class="linenos">314</span></a>                    <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-315"><a href="#TagDB-315"><span class="linenos">315</span></a>                    <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB-316"><a href="#TagDB-316"><span class="linenos">316</span></a>                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-317"><a href="#TagDB-317"><span class="linenos">317</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-318"><a href="#TagDB-318"><span class="linenos">318</span></a>                    <span class="c1"># self.tagWithItems[tagHash] = IDsSet</span>
</span><span id="TagDB-319"><a href="#TagDB-319"><span class="linenos">319</span></a>
</span><span id="TagDB-320"><a href="#TagDB-320"><span class="linenos">320</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="o">.</span><span class="n">remove_id</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-321"><a href="#TagDB-321"><span class="linenos">321</span></a>
</span><span id="TagDB-322"><a href="#TagDB-322"><span class="linenos">322</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB-323"><a href="#TagDB-323"><span class="linenos">323</span></a>        <span class="c1"># will return ItemId for deleted item or None object if Item is not exist</span>
</span><span id="TagDB-324"><a href="#TagDB-324"><span class="linenos">324</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="TagDB-325"><a href="#TagDB-325"><span class="linenos">325</span></a>        <span class="c1"># the given binItem) on this tag path</span>
</span><span id="TagDB-326"><a href="#TagDB-326"><span class="linenos">326</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-327"><a href="#TagDB-327"><span class="linenos">327</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-328"><a href="#TagDB-328"><span class="linenos">328</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-329"><a href="#TagDB-329"><span class="linenos">329</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="TagDB-330"><a href="#TagDB-330"><span class="linenos">330</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-331"><a href="#TagDB-331"><span class="linenos">331</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">remove_item_by_itemID</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB-332"><a href="#TagDB-332"><span class="linenos">332</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span><span id="TagDB-333"><a href="#TagDB-333"><span class="linenos">333</span></a>
</span><span id="TagDB-334"><a href="#TagDB-334"><span class="linenos">334</span></a>    <span class="k">def</span> <span class="nf">__OLD__get_itemID_from_item_and_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB-335"><a href="#TagDB-335"><span class="linenos">335</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-336"><a href="#TagDB-336"><span class="linenos">336</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-337"><a href="#TagDB-337"><span class="linenos">337</span></a>        <span class="n">potentialIDs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">))</span>
</span><span id="TagDB-338"><a href="#TagDB-338"><span class="linenos">338</span></a>        <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">SMART_TREE_TYPE</span><span class="p">))</span>
</span><span id="TagDB-339"><a href="#TagDB-339"><span class="linenos">339</span></a>        <span class="n">resultItemIDsList</span> <span class="o">=</span> <span class="n">potentialIDs</span> <span class="o">&amp;</span> <span class="n">itemIDsSet</span>
</span><span id="TagDB-340"><a href="#TagDB-340"><span class="linenos">340</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB-341"><a href="#TagDB-341"><span class="linenos">341</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="TagDB-342"><a href="#TagDB-342"><span class="linenos">342</span></a>        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-343"><a href="#TagDB-343"><span class="linenos">343</span></a>            <span class="n">resultItemID</span> <span class="o">=</span> <span class="n">resultItemIDsList</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>  <span class="c1"># we have assume that we&#39;ll have only one item in intersection</span>
</span><span id="TagDB-344"><a href="#TagDB-344"><span class="linenos">344</span></a>                <span class="c1"># between potential IDs and Items that have (and have only) given tag list (without another tags in the</span>
</span><span id="TagDB-345"><a href="#TagDB-345"><span class="linenos">345</span></a>                <span class="c1"># path to this items). We need to check it in the adding new item to the given tag path.</span>
</span><span id="TagDB-346"><a href="#TagDB-346"><span class="linenos">346</span></a>            <span class="k">return</span> <span class="n">resultItemID</span>
</span><span id="TagDB-347"><a href="#TagDB-347"><span class="linenos">347</span></a>        <span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">resultItemIDsList</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB-348"><a href="#TagDB-348"><span class="linenos">348</span></a>            <span class="k">raise</span> <span class="n">ToManyIdenticalItemsOnTheGivenTagPathError</span><span class="p">()</span>
</span><span id="TagDB-349"><a href="#TagDB-349"><span class="linenos">349</span></a>
</span><span id="TagDB-350"><a href="#TagDB-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB-351"><a href="#TagDB-351"><span class="linenos">351</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-352"><a href="#TagDB-352"><span class="linenos">352</span></a>
</span><span id="TagDB-353"><a href="#TagDB-353"><span class="linenos">353</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-354"><a href="#TagDB-354"><span class="linenos">354</span></a>
</span><span id="TagDB-355"><a href="#TagDB-355"><span class="linenos">355</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-356"><a href="#TagDB-356"><span class="linenos">356</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-357"><a href="#TagDB-357"><span class="linenos">357</span></a>
</span><span id="TagDB-358"><a href="#TagDB-358"><span class="linenos">358</span></a>        <span class="n">potentialIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="TagDB-359"><a href="#TagDB-359"><span class="linenos">359</span></a>        <span class="n">setOfBinTagsHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-360"><a href="#TagDB-360"><span class="linenos">360</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-361"><a href="#TagDB-361"><span class="linenos">361</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-362"><a href="#TagDB-362"><span class="linenos">362</span></a>            <span class="n">setOfBinTagsHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-363"><a href="#TagDB-363"><span class="linenos">363</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">potentialIDs</span><span class="p">:</span>
</span><span id="TagDB-364"><a href="#TagDB-364"><span class="linenos">364</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-365"><a href="#TagDB-365"><span class="linenos">365</span></a>            <span class="n">currentItemTagsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="TagDB-366"><a href="#TagDB-366"><span class="linenos">366</span></a>            <span class="k">if</span> <span class="n">setOfBinTagsHashes</span> <span class="o">==</span> <span class="n">currentItemTagsSet</span><span class="p">:</span>
</span><span id="TagDB-367"><a href="#TagDB-367"><span class="linenos">367</span></a>                <span class="k">return</span> <span class="n">itemID</span>
</span><span id="TagDB-368"><a href="#TagDB-368"><span class="linenos">368</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="TagDB-369"><a href="#TagDB-369"><span class="linenos">369</span></a>
</span><span id="TagDB-370"><a href="#TagDB-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="nf">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashList</span><span class="p">):</span>
</span><span id="TagDB-371"><a href="#TagDB-371"><span class="linenos">371</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-372"><a href="#TagDB-372"><span class="linenos">372</span></a>
</span><span id="TagDB-373"><a href="#TagDB-373"><span class="linenos">373</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-374"><a href="#TagDB-374"><span class="linenos">374</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashList</span><span class="p">:</span>
</span><span id="TagDB-375"><a href="#TagDB-375"><span class="linenos">375</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-376"><a href="#TagDB-376"><span class="linenos">376</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB-377"><a href="#TagDB-377"><span class="linenos">377</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span><span id="TagDB-378"><a href="#TagDB-378"><span class="linenos">378</span></a>
</span><span id="TagDB-379"><a href="#TagDB-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">get_item_and_tags_from_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="TagDB-380"><a href="#TagDB-380"><span class="linenos">380</span></a>        <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-381"><a href="#TagDB-381"><span class="linenos">381</span></a>        <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()}</span>
</span><span id="TagDB-382"><a href="#TagDB-382"><span class="linenos">382</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB-383"><a href="#TagDB-383"><span class="linenos">383</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">))</span>
</span><span id="TagDB-384"><a href="#TagDB-384"><span class="linenos">384</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-385"><a href="#TagDB-385"><span class="linenos">385</span></a>
</span><span id="TagDB-386"><a href="#TagDB-386"><span class="linenos">386</span></a>    <span class="c1"># @profile</span>
</span><span id="TagDB-387"><a href="#TagDB-387"><span class="linenos">387</span></a>    <span class="k">def</span> <span class="nf">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB-388"><a href="#TagDB-388"><span class="linenos">388</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-389"><a href="#TagDB-389"><span class="linenos">389</span></a>
</span><span id="TagDB-390"><a href="#TagDB-390"><span class="linenos">390</span></a>        <span class="n">tagsQnt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span>
</span><span id="TagDB-391"><a href="#TagDB-391"><span class="linenos">391</span></a>        <span class="k">if</span> <span class="n">local_tags_qnt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-392"><a href="#TagDB-392"><span class="linenos">392</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span>
</span><span id="TagDB-393"><a href="#TagDB-393"><span class="linenos">393</span></a>        <span class="n">tag_hash_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-394"><a href="#TagDB-394"><span class="linenos">394</span></a>        <span class="n">tag_by_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB-395"><a href="#TagDB-395"><span class="linenos">395</span></a>        <span class="n">tag_by_qnt__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span>
</span><span id="TagDB-396"><a href="#TagDB-396"><span class="linenos">396</span></a>        <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB-397"><a href="#TagDB-397"><span class="linenos">397</span></a>        <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">tag_hash_set</span><span class="p">:</span>
</span><span id="TagDB-398"><a href="#TagDB-398"><span class="linenos">398</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-399"><a href="#TagDB-399"><span class="linenos">399</span></a>            <span class="n">qnt</span> <span class="o">=</span> <span class="n">tagsQnt</span><span class="p">[</span><span class="n">tag_hash</span><span class="p">]</span>
</span><span id="TagDB-400"><a href="#TagDB-400"><span class="linenos">400</span></a>            <span class="k">if</span> <span class="n">qnt</span> <span class="o">&gt;</span> <span class="n">biggest_qnt</span><span class="p">:</span>
</span><span id="TagDB-401"><a href="#TagDB-401"><span class="linenos">401</span></a>                <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="n">qnt</span>
</span><span id="TagDB-402"><a href="#TagDB-402"><span class="linenos">402</span></a>            <span class="c1"># if qnt not in tag_by_qnt:</span>
</span><span id="TagDB-403"><a href="#TagDB-403"><span class="linenos">403</span></a>            <span class="c1">#     tag_by_qnt[qnt] = set()</span>
</span><span id="TagDB-404"><a href="#TagDB-404"><span class="linenos">404</span></a>            <span class="c1"># tag_by_qnt[qnt].add(tag_hash)</span>
</span><span id="TagDB-405"><a href="#TagDB-405"><span class="linenos">405</span></a>            <span class="n">tag_by_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">qnt</span><span class="p">,</span> <span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB-406"><a href="#TagDB-406"><span class="linenos">406</span></a>
</span><span id="TagDB-407"><a href="#TagDB-407"><span class="linenos">407</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-408"><a href="#TagDB-408"><span class="linenos">408</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB-409"><a href="#TagDB-409"><span class="linenos">409</span></a>            <span class="c1"># biggest_qnt = max(tag_by_qnt)</span>
</span><span id="TagDB-410"><a href="#TagDB-410"><span class="linenos">410</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">[</span><span class="n">biggest_qnt</span><span class="p">])</span>
</span><span id="TagDB-411"><a href="#TagDB-411"><span class="linenos">411</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-412"><a href="#TagDB-412"><span class="linenos">412</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TagDB-413"><a href="#TagDB-413"><span class="linenos">413</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-414"><a href="#TagDB-414"><span class="linenos">414</span></a>
</span><span id="TagDB-415"><a href="#TagDB-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB-416"><a href="#TagDB-416"><span class="linenos">416</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="TagDB-417"><a href="#TagDB-417"><span class="linenos">417</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-418"><a href="#TagDB-418"><span class="linenos">418</span></a>
</span><span id="TagDB-419"><a href="#TagDB-419"><span class="linenos">419</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-420"><a href="#TagDB-420"><span class="linenos">420</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-421"><a href="#TagDB-421"><span class="linenos">421</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="TagDB-422"><a href="#TagDB-422"><span class="linenos">422</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-423"><a href="#TagDB-423"><span class="linenos">423</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB-424"><a href="#TagDB-424"><span class="linenos">424</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB-425"><a href="#TagDB-425"><span class="linenos">425</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="TagDB-426"><a href="#TagDB-426"><span class="linenos">426</span></a>
</span><span id="TagDB-427"><a href="#TagDB-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB-428"><a href="#TagDB-428"><span class="linenos">428</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-429"><a href="#TagDB-429"><span class="linenos">429</span></a>
</span><span id="TagDB-430"><a href="#TagDB-430"><span class="linenos">430</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-431"><a href="#TagDB-431"><span class="linenos">431</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-432"><a href="#TagDB-432"><span class="linenos">432</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-433"><a href="#TagDB-433"><span class="linenos">433</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-434"><a href="#TagDB-434"><span class="linenos">434</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-435"><a href="#TagDB-435"><span class="linenos">435</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB-436"><a href="#TagDB-436"><span class="linenos">436</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB-437"><a href="#TagDB-437"><span class="linenos">437</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="TagDB-438"><a href="#TagDB-438"><span class="linenos">438</span></a>
</span><span id="TagDB-439"><a href="#TagDB-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB-440"><a href="#TagDB-440"><span class="linenos">440</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="TagDB-441"><a href="#TagDB-441"><span class="linenos">441</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-442"><a href="#TagDB-442"><span class="linenos">442</span></a>
</span><span id="TagDB-443"><a href="#TagDB-443"><span class="linenos">443</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-444"><a href="#TagDB-444"><span class="linenos">444</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-445"><a href="#TagDB-445"><span class="linenos">445</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="TagDB-446"><a href="#TagDB-446"><span class="linenos">446</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-447"><a href="#TagDB-447"><span class="linenos">447</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB-448"><a href="#TagDB-448"><span class="linenos">448</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB-449"><a href="#TagDB-449"><span class="linenos">449</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="TagDB-450"><a href="#TagDB-450"><span class="linenos">450</span></a>
</span><span id="TagDB-451"><a href="#TagDB-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB-452"><a href="#TagDB-452"><span class="linenos">452</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-453"><a href="#TagDB-453"><span class="linenos">453</span></a>
</span><span id="TagDB-454"><a href="#TagDB-454"><span class="linenos">454</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-455"><a href="#TagDB-455"><span class="linenos">455</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-456"><a href="#TagDB-456"><span class="linenos">456</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-457"><a href="#TagDB-457"><span class="linenos">457</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-458"><a href="#TagDB-458"><span class="linenos">458</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-459"><a href="#TagDB-459"><span class="linenos">459</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB-460"><a href="#TagDB-460"><span class="linenos">460</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB-461"><a href="#TagDB-461"><span class="linenos">461</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span><span id="TagDB-462"><a href="#TagDB-462"><span class="linenos">462</span></a>
</span><span id="TagDB-463"><a href="#TagDB-463"><span class="linenos">463</span></a>    <span class="k">def</span> <span class="nf">sort_raw_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rawTagList</span><span class="p">):</span>
</span><span id="TagDB-464"><a href="#TagDB-464"><span class="linenos">464</span></a>        <span class="c1"># will return sorted tag list</span>
</span><span id="TagDB-465"><a href="#TagDB-465"><span class="linenos">465</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-466"><a href="#TagDB-466"><span class="linenos">466</span></a>
</span><span id="TagDB-467"><a href="#TagDB-467"><span class="linenos">467</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">tagAndWeight</span><span class="p">:</span> <span class="n">tagAndWeight</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB-468"><a href="#TagDB-468"><span class="linenos">468</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-469"><a href="#TagDB-469"><span class="linenos">469</span></a>        <span class="k">for</span> <span class="n">rawTag</span> <span class="ow">in</span> <span class="n">rawTagList</span><span class="p">:</span>
</span><span id="TagDB-470"><a href="#TagDB-470"><span class="linenos">470</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-471"><a href="#TagDB-471"><span class="linenos">471</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">rawTag</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="TagDB-472"><a href="#TagDB-472"><span class="linenos">472</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span><span id="TagDB-473"><a href="#TagDB-473"><span class="linenos">473</span></a>
</span><span id="TagDB-474"><a href="#TagDB-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">get_itemIDs_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB-475"><a href="#TagDB-475"><span class="linenos">475</span></a>                              <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB-476"><a href="#TagDB-476"><span class="linenos">476</span></a>        <span class="c1"># TODO: исправить ошибку: SMART_TREE_TYPE: возвращает не только список файлов в текущей директории, но и из</span>
</span><span id="TagDB-477"><a href="#TagDB-477"><span class="linenos">477</span></a>        <span class="c1"># непосредственных подпапок данной папки</span>
</span><span id="TagDB-478"><a href="#TagDB-478"><span class="linenos">478</span></a>
</span><span id="TagDB-479"><a href="#TagDB-479"><span class="linenos">479</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="TagDB-480"><a href="#TagDB-480"><span class="linenos">480</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="TagDB-481"><a href="#TagDB-481"><span class="linenos">481</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB-482"><a href="#TagDB-482"><span class="linenos">482</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-483"><a href="#TagDB-483"><span class="linenos">483</span></a>
</span><span id="TagDB-484"><a href="#TagDB-484"><span class="linenos">484</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-485"><a href="#TagDB-485"><span class="linenos">485</span></a>
</span><span id="TagDB-486"><a href="#TagDB-486"><span class="linenos">486</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-487"><a href="#TagDB-487"><span class="linenos">487</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-488"><a href="#TagDB-488"><span class="linenos">488</span></a>
</span><span id="TagDB-489"><a href="#TagDB-489"><span class="linenos">489</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-490"><a href="#TagDB-490"><span class="linenos">490</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-491"><a href="#TagDB-491"><span class="linenos">491</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-492"><a href="#TagDB-492"><span class="linenos">492</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-493"><a href="#TagDB-493"><span class="linenos">493</span></a>
</span><span id="TagDB-494"><a href="#TagDB-494"><span class="linenos">494</span></a>        <span class="c1"># PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="TagDB-495"><a href="#TagDB-495"><span class="linenos">495</span></a>        <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-496"><a href="#TagDB-496"><span class="linenos">496</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB-497"><a href="#TagDB-497"><span class="linenos">497</span></a>            <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-498"><a href="#TagDB-498"><span class="linenos">498</span></a>            <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-499"><a href="#TagDB-499"><span class="linenos">499</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-500"><a href="#TagDB-500"><span class="linenos">500</span></a>            <span class="n">itemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-501"><a href="#TagDB-501"><span class="linenos">501</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">))</span>
</span><span id="TagDB-502"><a href="#TagDB-502"><span class="linenos">502</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-503"><a href="#TagDB-503"><span class="linenos">503</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB-504"><a href="#TagDB-504"><span class="linenos">504</span></a>                <span class="n">itemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="TagDB-505"><a href="#TagDB-505"><span class="linenos">505</span></a>            <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="TagDB-506"><a href="#TagDB-506"><span class="linenos">506</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-507"><a href="#TagDB-507"><span class="linenos">507</span></a>                <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="TagDB-508"><a href="#TagDB-508"><span class="linenos">508</span></a>                    <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="TagDB-509"><a href="#TagDB-509"><span class="linenos">509</span></a>                    <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="TagDB-510"><a href="#TagDB-510"><span class="linenos">510</span></a>            <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="TagDB-511"><a href="#TagDB-511"><span class="linenos">511</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-512"><a href="#TagDB-512"><span class="linenos">512</span></a>                <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="TagDB-513"><a href="#TagDB-513"><span class="linenos">513</span></a>                <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB-514"><a href="#TagDB-514"><span class="linenos">514</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">commonTagHashSet</span><span class="p">):</span>
</span><span id="TagDB-515"><a href="#TagDB-515"><span class="linenos">515</span></a>                    <span class="n">itemIDSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">])</span>
</span><span id="TagDB-516"><a href="#TagDB-516"><span class="linenos">516</span></a>                <span class="c1"># # if len(tagHashSet &amp; commonTagHashSet) == len(tagHashSet):</span>
</span><span id="TagDB-517"><a href="#TagDB-517"><span class="linenos">517</span></a>                <span class="c1"># res_set = tagHashSet.intersection(commonTagHashSet)</span>
</span><span id="TagDB-518"><a href="#TagDB-518"><span class="linenos">518</span></a>                <span class="c1"># if len(res_set) == binTagsQnt:</span>
</span><span id="TagDB-519"><a href="#TagDB-519"><span class="linenos">519</span></a>                <span class="c1">#     itemIDSet = itemIDSet | self.itemsOnTheCommonTagSets[commonTagGroupHash]</span>
</span><span id="TagDB-520"><a href="#TagDB-520"><span class="linenos">520</span></a>            <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="n">itemIDSet</span>
</span><span id="TagDB-521"><a href="#TagDB-521"><span class="linenos">521</span></a>
</span><span id="TagDB-522"><a href="#TagDB-522"><span class="linenos">522</span></a>            <span class="c1"># isFirstHash = True</span>
</span><span id="TagDB-523"><a href="#TagDB-523"><span class="linenos">523</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="TagDB-524"><a href="#TagDB-524"><span class="linenos">524</span></a>            <span class="c1">#     tagHash = tag.__hash__()</span>
</span><span id="TagDB-525"><a href="#TagDB-525"><span class="linenos">525</span></a>            <span class="c1">#     if tagHash in self.tagWithItems:</span>
</span><span id="TagDB-526"><a href="#TagDB-526"><span class="linenos">526</span></a>            <span class="c1">#         if isFirstHash:</span>
</span><span id="TagDB-527"><a href="#TagDB-527"><span class="linenos">527</span></a>            <span class="c1">#             interceptionOfItemsWithTags = self.tagWithItems[tagHash]</span>
</span><span id="TagDB-528"><a href="#TagDB-528"><span class="linenos">528</span></a>            <span class="c1">#             isFirstHash = False</span>
</span><span id="TagDB-529"><a href="#TagDB-529"><span class="linenos">529</span></a>            <span class="c1">#         else:</span>
</span><span id="TagDB-530"><a href="#TagDB-530"><span class="linenos">530</span></a>            <span class="c1">#             itemsWithTag = self.tagWithItems[tagHash]</span>
</span><span id="TagDB-531"><a href="#TagDB-531"><span class="linenos">531</span></a>            <span class="c1">#             interceptionOfItemsWithTags = interceptionOfItemsWithTags &amp; itemsWithTag</span>
</span><span id="TagDB-532"><a href="#TagDB-532"><span class="linenos">532</span></a>            <span class="c1">#     else:</span>
</span><span id="TagDB-533"><a href="#TagDB-533"><span class="linenos">533</span></a>            <span class="c1">#         # TODO: произвести такую же провеку в get_items_from_tags() и build_smart_tree()</span>
</span><span id="TagDB-534"><a href="#TagDB-534"><span class="linenos">534</span></a>            <span class="c1">#         if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="TagDB-535"><a href="#TagDB-535"><span class="linenos">535</span></a>            <span class="c1">#             result = (set(), set())</span>
</span><span id="TagDB-536"><a href="#TagDB-536"><span class="linenos">536</span></a>            <span class="c1">#             return result</span>
</span><span id="TagDB-537"><a href="#TagDB-537"><span class="linenos">537</span></a>            <span class="c1">#         else:</span>
</span><span id="TagDB-538"><a href="#TagDB-538"><span class="linenos">538</span></a>            <span class="c1">#             return set()</span>
</span><span id="TagDB-539"><a href="#TagDB-539"><span class="linenos">539</span></a>
</span><span id="TagDB-540"><a href="#TagDB-540"><span class="linenos">540</span></a>        <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="TagDB-541"><a href="#TagDB-541"><span class="linenos">541</span></a>        <span class="n">setOfAllInternalItemIDsForThisSetOfTags</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="TagDB-542"><a href="#TagDB-542"><span class="linenos">542</span></a>
</span><span id="TagDB-543"><a href="#TagDB-543"><span class="linenos">543</span></a>        <span class="c1"># SMART_TREE_TYPE or FULL_TREE_TYPE</span>
</span><span id="TagDB-544"><a href="#TagDB-544"><span class="linenos">544</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB-545"><a href="#TagDB-545"><span class="linenos">545</span></a>            <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-546"><a href="#TagDB-546"><span class="linenos">546</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-547"><a href="#TagDB-547"><span class="linenos">547</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">binTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB-548"><a href="#TagDB-548"><span class="linenos">548</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-549"><a href="#TagDB-549"><span class="linenos">549</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB-550"><a href="#TagDB-550"><span class="linenos">550</span></a>                <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="TagDB-551"><a href="#TagDB-551"><span class="linenos">551</span></a>
</span><span id="TagDB-552"><a href="#TagDB-552"><span class="linenos">552</span></a>            <span class="c1"># filteredItemIDsSet = set()</span>
</span><span id="TagDB-553"><a href="#TagDB-553"><span class="linenos">553</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="TagDB-554"><a href="#TagDB-554"><span class="linenos">554</span></a>            <span class="c1"># # for itemID in setOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="TagDB-555"><a href="#TagDB-555"><span class="linenos">555</span></a>            <span class="c1"># #     if len(self.itemWithTags[itemID]) == tagQnt:</span>
</span><span id="TagDB-556"><a href="#TagDB-556"><span class="linenos">556</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="TagDB-557"><a href="#TagDB-557"><span class="linenos">557</span></a>            <span class="c1"># #         # и вычитывать это из него</span>
</span><span id="TagDB-558"><a href="#TagDB-558"><span class="linenos">558</span></a>            <span class="c1"># #         # и/или</span>
</span><span id="TagDB-559"><a href="#TagDB-559"><span class="linenos">559</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashSet_1, hashOfTheTagHashSet_2, ...</span>
</span><span id="TagDB-560"><a href="#TagDB-560"><span class="linenos">560</span></a>            <span class="c1"># #         # , hashOfTheTagHashSet_3}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="TagDB-561"><a href="#TagDB-561"><span class="linenos">561</span></a>            <span class="c1"># #         # где hashOfTheTagHashSet - это tagHashSet.__hash__()</span>
</span><span id="TagDB-562"><a href="#TagDB-562"><span class="linenos">562</span></a>            <span class="c1"># #         filteredItemIDsSet.add(itemID)</span>
</span><span id="TagDB-563"><a href="#TagDB-563"><span class="linenos">563</span></a>            <span class="c1"># if tagQnt in self.tagsNumPerItemID:</span>
</span><span id="TagDB-564"><a href="#TagDB-564"><span class="linenos">564</span></a>            <span class="c1">#     filteredItemIDsSet = setOfAllInternalItemIDsForThisSetOfTags &amp; self.tagsNumPerItemID[tagQnt]</span>
</span><span id="TagDB-565"><a href="#TagDB-565"><span class="linenos">565</span></a>            <span class="c1">#</span>
</span><span id="TagDB-566"><a href="#TagDB-566"><span class="linenos">566</span></a>            <span class="c1"># resultItemIDSet = set()</span>
</span><span id="TagDB-567"><a href="#TagDB-567"><span class="linenos">567</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="TagDB-568"><a href="#TagDB-568"><span class="linenos">568</span></a>            <span class="c1"># for binTag in binTags:</span>
</span><span id="TagDB-569"><a href="#TagDB-569"><span class="linenos">569</span></a>            <span class="c1">#     tagHashSet.add(binTag.__hash__())</span>
</span><span id="TagDB-570"><a href="#TagDB-570"><span class="linenos">570</span></a>            <span class="c1"># for itemID in filteredItemIDsSet:</span>
</span><span id="TagDB-571"><a href="#TagDB-571"><span class="linenos">571</span></a>            <span class="c1">#     commonTagTupleHash = self.itemWithTags[itemID]</span>
</span><span id="TagDB-572"><a href="#TagDB-572"><span class="linenos">572</span></a>            <span class="c1">#     tagSet = set(self.commonTagSets[commonTagTupleHash])</span>
</span><span id="TagDB-573"><a href="#TagDB-573"><span class="linenos">573</span></a>            <span class="c1">#     if tagSet == tagHashSet:</span>
</span><span id="TagDB-574"><a href="#TagDB-574"><span class="linenos">574</span></a>            <span class="c1">#         # _TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="TagDB-575"><a href="#TagDB-575"><span class="linenos">575</span></a>            <span class="c1">#         # где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="TagDB-576"><a href="#TagDB-576"><span class="linenos">576</span></a>            <span class="c1">#         # _TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ...</span>
</span><span id="TagDB-577"><a href="#TagDB-577"><span class="linenos">577</span></a>            <span class="c1">#         # , itemID_3}]</span>
</span><span id="TagDB-578"><a href="#TagDB-578"><span class="linenos">578</span></a>            <span class="c1">#         resultItemIDSet.add(itemID)</span>
</span><span id="TagDB-579"><a href="#TagDB-579"><span class="linenos">579</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">:</span>
</span><span id="TagDB-580"><a href="#TagDB-580"><span class="linenos">580</span></a>            <span class="c1"># already implemented (see bellow). Don&#39;t touch this code!</span>
</span><span id="TagDB-581"><a href="#TagDB-581"><span class="linenos">581</span></a>            <span class="k">pass</span>
</span><span id="TagDB-582"><a href="#TagDB-582"><span class="linenos">582</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-583"><a href="#TagDB-583"><span class="linenos">583</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="TagDB-584"><a href="#TagDB-584"><span class="linenos">584</span></a>
</span><span id="TagDB-585"><a href="#TagDB-585"><span class="linenos">585</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB-586"><a href="#TagDB-586"><span class="linenos">586</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">setOfAllInternalItemIDsForThisSetOfTags</span><span class="p">))</span>
</span><span id="TagDB-587"><a href="#TagDB-587"><span class="linenos">587</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-588"><a href="#TagDB-588"><span class="linenos">588</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-589"><a href="#TagDB-589"><span class="linenos">589</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">)</span>
</span><span id="TagDB-590"><a href="#TagDB-590"><span class="linenos">590</span></a>
</span><span id="TagDB-591"><a href="#TagDB-591"><span class="linenos">591</span></a>    <span class="k">def</span> <span class="nf">get_items_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB-592"><a href="#TagDB-592"><span class="linenos">592</span></a>                            <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB-593"><a href="#TagDB-593"><span class="linenos">593</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="TagDB-594"><a href="#TagDB-594"><span class="linenos">594</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="TagDB-595"><a href="#TagDB-595"><span class="linenos">595</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB-596"><a href="#TagDB-596"><span class="linenos">596</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-597"><a href="#TagDB-597"><span class="linenos">597</span></a>
</span><span id="TagDB-598"><a href="#TagDB-598"><span class="linenos">598</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-599"><a href="#TagDB-599"><span class="linenos">599</span></a>        <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB-600"><a href="#TagDB-600"><span class="linenos">600</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="TagDB-601"><a href="#TagDB-601"><span class="linenos">601</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="TagDB-602"><a href="#TagDB-602"><span class="linenos">602</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB-603"><a href="#TagDB-603"><span class="linenos">603</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-604"><a href="#TagDB-604"><span class="linenos">604</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="TagDB-605"><a href="#TagDB-605"><span class="linenos">605</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-606"><a href="#TagDB-606"><span class="linenos">606</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="TagDB-607"><a href="#TagDB-607"><span class="linenos">607</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>  <span class="c1"># result == (usual items set, additional set of all</span>
</span><span id="TagDB-608"><a href="#TagDB-608"><span class="linenos">608</span></a>                <span class="c1"># internal itemIDs)</span>
</span><span id="TagDB-609"><a href="#TagDB-609"><span class="linenos">609</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-610"><a href="#TagDB-610"><span class="linenos">610</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-611"><a href="#TagDB-611"><span class="linenos">611</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-612"><a href="#TagDB-612"><span class="linenos">612</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">:</span>
</span><span id="TagDB-613"><a href="#TagDB-613"><span class="linenos">613</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-614"><a href="#TagDB-614"><span class="linenos">614</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="TagDB-615"><a href="#TagDB-615"><span class="linenos">615</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">)</span>
</span><span id="TagDB-616"><a href="#TagDB-616"><span class="linenos">616</span></a>
</span><span id="TagDB-617"><a href="#TagDB-617"><span class="linenos">617</span></a>    <span class="k">def</span> <span class="nf">get_tagHashes_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB-618"><a href="#TagDB-618"><span class="linenos">618</span></a>                                <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB-619"><a href="#TagDB-619"><span class="linenos">619</span></a>        <span class="c1"># where &quot;itemIDsSet&quot; is externally given &quot;get_itemIDs_from_tags(binTags, treeType=PLAIN_PSEUDO_TREE_TYPE)&quot;</span>
</span><span id="TagDB-620"><a href="#TagDB-620"><span class="linenos">620</span></a>        <span class="c1"># so &quot;itemIDsSet&quot; is a set of the all items inside the &quot;folder&quot; binTags (including items from &quot;subfolders&quot;)</span>
</span><span id="TagDB-621"><a href="#TagDB-621"><span class="linenos">621</span></a>        <span class="c1"># treeType - the same as in the &quot;get_items_from_tags()&quot; method</span>
</span><span id="TagDB-622"><a href="#TagDB-622"><span class="linenos">622</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB-623"><a href="#TagDB-623"><span class="linenos">623</span></a>        <span class="c1"># prePreparedSetOfAllInternalItemIDsForThisSetOfTags can be generated by:</span>
</span><span id="TagDB-624"><a href="#TagDB-624"><span class="linenos">624</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE)</span>
</span><span id="TagDB-625"><a href="#TagDB-625"><span class="linenos">625</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="TagDB-626"><a href="#TagDB-626"><span class="linenos">626</span></a>        <span class="c1">#   c) get_items_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="TagDB-627"><a href="#TagDB-627"><span class="linenos">627</span></a>        <span class="c1">#   d) get_items_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE) || BUT: it&#39;ll return item set - not itemID</span>
</span><span id="TagDB-628"><a href="#TagDB-628"><span class="linenos">628</span></a>        <span class="c1">#       set</span>
</span><span id="TagDB-629"><a href="#TagDB-629"><span class="linenos">629</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-630"><a href="#TagDB-630"><span class="linenos">630</span></a>
</span><span id="TagDB-631"><a href="#TagDB-631"><span class="linenos">631</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-632"><a href="#TagDB-632"><span class="linenos">632</span></a>
</span><span id="TagDB-633"><a href="#TagDB-633"><span class="linenos">633</span></a>        <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-634"><a href="#TagDB-634"><span class="linenos">634</span></a>
</span><span id="TagDB-635"><a href="#TagDB-635"><span class="linenos">635</span></a>        <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-636"><a href="#TagDB-636"><span class="linenos">636</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-637"><a href="#TagDB-637"><span class="linenos">637</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB-638"><a href="#TagDB-638"><span class="linenos">638</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-639"><a href="#TagDB-639"><span class="linenos">639</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span>
</span><span id="TagDB-640"><a href="#TagDB-640"><span class="linenos">640</span></a>
</span><span id="TagDB-641"><a href="#TagDB-641"><span class="linenos">641</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB-642"><a href="#TagDB-642"><span class="linenos">642</span></a>            <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-643"><a href="#TagDB-643"><span class="linenos">643</span></a>            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-644"><a href="#TagDB-644"><span class="linenos">644</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-645"><a href="#TagDB-645"><span class="linenos">645</span></a>                <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-646"><a href="#TagDB-646"><span class="linenos">646</span></a>            <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-647"><a href="#TagDB-647"><span class="linenos">647</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB-648"><a href="#TagDB-648"><span class="linenos">648</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-649"><a href="#TagDB-649"><span class="linenos">649</span></a>                <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB-650"><a href="#TagDB-650"><span class="linenos">650</span></a>                    <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-651"><a href="#TagDB-651"><span class="linenos">651</span></a>                    <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-652"><a href="#TagDB-652"><span class="linenos">652</span></a>                    <span class="n">tagHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB-653"><a href="#TagDB-653"><span class="linenos">653</span></a>            <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">tagHashSet</span> <span class="o">-</span> <span class="n">binTagHashes</span>
</span><span id="TagDB-654"><a href="#TagDB-654"><span class="linenos">654</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">:</span>
</span><span id="TagDB-655"><a href="#TagDB-655"><span class="linenos">655</span></a>            <span class="c1"># smartTree = self.build_smart_tree(binTags, prePreparedSetOfAllInternalItemIDs=setOfAllInternalItemIDs)</span>
</span><span id="TagDB-656"><a href="#TagDB-656"><span class="linenos">656</span></a>            <span class="n">smartTree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_smart_tree</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="n">setOfAllInternalItemIDs</span><span class="p">,</span>
</span><span id="TagDB-657"><a href="#TagDB-657"><span class="linenos">657</span></a>                                              <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB-658"><a href="#TagDB-658"><span class="linenos">658</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="ow">in</span> <span class="n">smartTree</span><span class="p">:</span>
</span><span id="TagDB-659"><a href="#TagDB-659"><span class="linenos">659</span></a>                <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">smartTree</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="TagDB-660"><a href="#TagDB-660"><span class="linenos">660</span></a>            <span class="c1"># filteredItemIDsList = list()</span>
</span><span id="TagDB-661"><a href="#TagDB-661"><span class="linenos">661</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="TagDB-662"><a href="#TagDB-662"><span class="linenos">662</span></a>            <span class="c1"># for itemID in listOfAllInternalItemIDs:</span>
</span><span id="TagDB-663"><a href="#TagDB-663"><span class="linenos">663</span></a>            <span class="c1">#     if len(self.itemWithTags[itemID]) == (tagQnt + 1):</span>
</span><span id="TagDB-664"><a href="#TagDB-664"><span class="linenos">664</span></a>            <span class="c1">#         filteredItemIDsList.append(itemID)</span>
</span><span id="TagDB-665"><a href="#TagDB-665"><span class="linenos">665</span></a>            <span class="c1">#</span>
</span><span id="TagDB-666"><a href="#TagDB-666"><span class="linenos">666</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="TagDB-667"><a href="#TagDB-667"><span class="linenos">667</span></a>            <span class="c1"># for itemID in filteredItemIDsList:</span>
</span><span id="TagDB-668"><a href="#TagDB-668"><span class="linenos">668</span></a>            <span class="c1">#     tagHashSet.update(set(self.itemWithTags[itemID]))</span>
</span><span id="TagDB-669"><a href="#TagDB-669"><span class="linenos">669</span></a>            <span class="c1"># givenTagHashes = set()</span>
</span><span id="TagDB-670"><a href="#TagDB-670"><span class="linenos">670</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="TagDB-671"><a href="#TagDB-671"><span class="linenos">671</span></a>            <span class="c1">#     givenTagHashes.add(tag.__hash__())</span>
</span><span id="TagDB-672"><a href="#TagDB-672"><span class="linenos">672</span></a>            <span class="c1"># tagHashSet.difference_update(givenTagHashes)</span>
</span><span id="TagDB-673"><a href="#TagDB-673"><span class="linenos">673</span></a>            <span class="c1"># ##resultTagHashList = list(tagHashSet)</span>
</span><span id="TagDB-674"><a href="#TagDB-674"><span class="linenos">674</span></a>            <span class="c1"># # если остановиться тут - то мы увидим не все папки: мы не увидим папки непосредственно в которых есть</span>
</span><span id="TagDB-675"><a href="#TagDB-675"><span class="linenos">675</span></a>            <span class="c1"># # только другие подпапки, но ни одного файла.</span>
</span><span id="TagDB-676"><a href="#TagDB-676"><span class="linenos">676</span></a>            <span class="c1"># #</span>
</span><span id="TagDB-677"><a href="#TagDB-677"><span class="linenos">677</span></a>            <span class="c1"># # значит далее мы должны исключить все файлы, которые имеют только что найденные теги, и начать строить</span>
</span><span id="TagDB-678"><a href="#TagDB-678"><span class="linenos">678</span></a>            <span class="c1"># # древо тегов для оставшихся</span>
</span><span id="TagDB-679"><a href="#TagDB-679"><span class="linenos">679</span></a>            <span class="c1"># #</span>
</span><span id="TagDB-680"><a href="#TagDB-680"><span class="linenos">680</span></a>            <span class="c1"># # а далее - повторить все это в цикле, увеличив при проверке кол-во тегов еще раз на единицу (и используя</span>
</span><span id="TagDB-681"><a href="#TagDB-681"><span class="linenos">681</span></a>            <span class="c1"># # уже оставшийся после отсеивания набор файлов). В итоге кол-во итераций зависит не от количества файлов,</span>
</span><span id="TagDB-682"><a href="#TagDB-682"><span class="linenos">682</span></a>            <span class="c1"># # а от максимальной фактически имеющейся вложенности файлов внутри тегов-каталогов</span>
</span><span id="TagDB-683"><a href="#TagDB-683"><span class="linenos">683</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-684"><a href="#TagDB-684"><span class="linenos">684</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="TagDB-685"><a href="#TagDB-685"><span class="linenos">685</span></a>
</span><span id="TagDB-686"><a href="#TagDB-686"><span class="linenos">686</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">resultTagHashSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB-687"><a href="#TagDB-687"><span class="linenos">687</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span><span id="TagDB-688"><a href="#TagDB-688"><span class="linenos">688</span></a>
</span><span id="TagDB-689"><a href="#TagDB-689"><span class="linenos">689</span></a>    <span class="k">def</span> <span class="nf">get_tags_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB-690"><a href="#TagDB-690"><span class="linenos">690</span></a>                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB-691"><a href="#TagDB-691"><span class="linenos">691</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagHashes_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB-692"><a href="#TagDB-692"><span class="linenos">692</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="TagDB-693"><a href="#TagDB-693"><span class="linenos">693</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="TagDB-694"><a href="#TagDB-694"><span class="linenos">694</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span><span id="TagDB-695"><a href="#TagDB-695"><span class="linenos">695</span></a>
</span><span id="TagDB-696"><a href="#TagDB-696"><span class="linenos">696</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB-697"><a href="#TagDB-697"><span class="linenos">697</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-698"><a href="#TagDB-698"><span class="linenos">698</span></a>
</span><span id="TagDB-699"><a href="#TagDB-699"><span class="linenos">699</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="TagDB-700"><a href="#TagDB-700"><span class="linenos">700</span></a>
</span><span id="TagDB-701"><a href="#TagDB-701"><span class="linenos">701</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB-702"><a href="#TagDB-702"><span class="linenos">702</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-703"><a href="#TagDB-703"><span class="linenos">703</span></a>
</span><span id="TagDB-704"><a href="#TagDB-704"><span class="linenos">704</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-705"><a href="#TagDB-705"><span class="linenos">705</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB-706"><a href="#TagDB-706"><span class="linenos">706</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-707"><a href="#TagDB-707"><span class="linenos">707</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-708"><a href="#TagDB-708"><span class="linenos">708</span></a>
</span><span id="TagDB-709"><a href="#TagDB-709"><span class="linenos">709</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-710"><a href="#TagDB-710"><span class="linenos">710</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB-711"><a href="#TagDB-711"><span class="linenos">711</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-712"><a href="#TagDB-712"><span class="linenos">712</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="TagDB-713"><a href="#TagDB-713"><span class="linenos">713</span></a>
</span><span id="TagDB-714"><a href="#TagDB-714"><span class="linenos">714</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="TagDB-715"><a href="#TagDB-715"><span class="linenos">715</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB-716"><a href="#TagDB-716"><span class="linenos">716</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB-717"><a href="#TagDB-717"><span class="linenos">717</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB-718"><a href="#TagDB-718"><span class="linenos">718</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB-719"><a href="#TagDB-719"><span class="linenos">719</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-720"><a href="#TagDB-720"><span class="linenos">720</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-721"><a href="#TagDB-721"><span class="linenos">721</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-722"><a href="#TagDB-722"><span class="linenos">722</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB-723"><a href="#TagDB-723"><span class="linenos">723</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB-724"><a href="#TagDB-724"><span class="linenos">724</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="TagDB-725"><a href="#TagDB-725"><span class="linenos">725</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-726"><a href="#TagDB-726"><span class="linenos">726</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="TagDB-727"><a href="#TagDB-727"><span class="linenos">727</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="TagDB-728"><a href="#TagDB-728"><span class="linenos">728</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="TagDB-729"><a href="#TagDB-729"><span class="linenos">729</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB-730"><a href="#TagDB-730"><span class="linenos">730</span></a>
</span><span id="TagDB-731"><a href="#TagDB-731"><span class="linenos">731</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB-732"><a href="#TagDB-732"><span class="linenos">732</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-733"><a href="#TagDB-733"><span class="linenos">733</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-734"><a href="#TagDB-734"><span class="linenos">734</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-735"><a href="#TagDB-735"><span class="linenos">735</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB-736"><a href="#TagDB-736"><span class="linenos">736</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB-737"><a href="#TagDB-737"><span class="linenos">737</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-738"><a href="#TagDB-738"><span class="linenos">738</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="TagDB-739"><a href="#TagDB-739"><span class="linenos">739</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB-740"><a href="#TagDB-740"><span class="linenos">740</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-741"><a href="#TagDB-741"><span class="linenos">741</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="TagDB-742"><a href="#TagDB-742"><span class="linenos">742</span></a>
</span><span id="TagDB-743"><a href="#TagDB-743"><span class="linenos">743</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-744"><a href="#TagDB-744"><span class="linenos">744</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-745"><a href="#TagDB-745"><span class="linenos">745</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB-746"><a href="#TagDB-746"><span class="linenos">746</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB-747"><a href="#TagDB-747"><span class="linenos">747</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-748"><a href="#TagDB-748"><span class="linenos">748</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="TagDB-749"><a href="#TagDB-749"><span class="linenos">749</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-750"><a href="#TagDB-750"><span class="linenos">750</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="TagDB-751"><a href="#TagDB-751"><span class="linenos">751</span></a>                    <span class="k">pass</span>
</span><span id="TagDB-752"><a href="#TagDB-752"><span class="linenos">752</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-753"><a href="#TagDB-753"><span class="linenos">753</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB-754"><a href="#TagDB-754"><span class="linenos">754</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-755"><a href="#TagDB-755"><span class="linenos">755</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-756"><a href="#TagDB-756"><span class="linenos">756</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="TagDB-757"><a href="#TagDB-757"><span class="linenos">757</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="TagDB-758"><a href="#TagDB-758"><span class="linenos">758</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="TagDB-759"><a href="#TagDB-759"><span class="linenos">759</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="TagDB-760"><a href="#TagDB-760"><span class="linenos">760</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="TagDB-761"><a href="#TagDB-761"><span class="linenos">761</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="TagDB-762"><a href="#TagDB-762"><span class="linenos">762</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB-763"><a href="#TagDB-763"><span class="linenos">763</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="TagDB-764"><a href="#TagDB-764"><span class="linenos">764</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="TagDB-765"><a href="#TagDB-765"><span class="linenos">765</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB-766"><a href="#TagDB-766"><span class="linenos">766</span></a>
</span><span id="TagDB-767"><a href="#TagDB-767"><span class="linenos">767</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree_2</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB-768"><a href="#TagDB-768"><span class="linenos">768</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-769"><a href="#TagDB-769"><span class="linenos">769</span></a>
</span><span id="TagDB-770"><a href="#TagDB-770"><span class="linenos">770</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="TagDB-771"><a href="#TagDB-771"><span class="linenos">771</span></a>
</span><span id="TagDB-772"><a href="#TagDB-772"><span class="linenos">772</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB-773"><a href="#TagDB-773"><span class="linenos">773</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-774"><a href="#TagDB-774"><span class="linenos">774</span></a>
</span><span id="TagDB-775"><a href="#TagDB-775"><span class="linenos">775</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-776"><a href="#TagDB-776"><span class="linenos">776</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB-777"><a href="#TagDB-777"><span class="linenos">777</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-778"><a href="#TagDB-778"><span class="linenos">778</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-779"><a href="#TagDB-779"><span class="linenos">779</span></a>
</span><span id="TagDB-780"><a href="#TagDB-780"><span class="linenos">780</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-781"><a href="#TagDB-781"><span class="linenos">781</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB-782"><a href="#TagDB-782"><span class="linenos">782</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-783"><a href="#TagDB-783"><span class="linenos">783</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="TagDB-784"><a href="#TagDB-784"><span class="linenos">784</span></a>
</span><span id="TagDB-785"><a href="#TagDB-785"><span class="linenos">785</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="TagDB-786"><a href="#TagDB-786"><span class="linenos">786</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB-787"><a href="#TagDB-787"><span class="linenos">787</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB-788"><a href="#TagDB-788"><span class="linenos">788</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB-789"><a href="#TagDB-789"><span class="linenos">789</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB-790"><a href="#TagDB-790"><span class="linenos">790</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-791"><a href="#TagDB-791"><span class="linenos">791</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-792"><a href="#TagDB-792"><span class="linenos">792</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-793"><a href="#TagDB-793"><span class="linenos">793</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB-794"><a href="#TagDB-794"><span class="linenos">794</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB-795"><a href="#TagDB-795"><span class="linenos">795</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="TagDB-796"><a href="#TagDB-796"><span class="linenos">796</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-797"><a href="#TagDB-797"><span class="linenos">797</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="TagDB-798"><a href="#TagDB-798"><span class="linenos">798</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="TagDB-799"><a href="#TagDB-799"><span class="linenos">799</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="TagDB-800"><a href="#TagDB-800"><span class="linenos">800</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB-801"><a href="#TagDB-801"><span class="linenos">801</span></a>
</span><span id="TagDB-802"><a href="#TagDB-802"><span class="linenos">802</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB-803"><a href="#TagDB-803"><span class="linenos">803</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-804"><a href="#TagDB-804"><span class="linenos">804</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-805"><a href="#TagDB-805"><span class="linenos">805</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-806"><a href="#TagDB-806"><span class="linenos">806</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB-807"><a href="#TagDB-807"><span class="linenos">807</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB-808"><a href="#TagDB-808"><span class="linenos">808</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-809"><a href="#TagDB-809"><span class="linenos">809</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="TagDB-810"><a href="#TagDB-810"><span class="linenos">810</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB-811"><a href="#TagDB-811"><span class="linenos">811</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-812"><a href="#TagDB-812"><span class="linenos">812</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="TagDB-813"><a href="#TagDB-813"><span class="linenos">813</span></a>
</span><span id="TagDB-814"><a href="#TagDB-814"><span class="linenos">814</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-815"><a href="#TagDB-815"><span class="linenos">815</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-816"><a href="#TagDB-816"><span class="linenos">816</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB-817"><a href="#TagDB-817"><span class="linenos">817</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB-818"><a href="#TagDB-818"><span class="linenos">818</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-819"><a href="#TagDB-819"><span class="linenos">819</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="TagDB-820"><a href="#TagDB-820"><span class="linenos">820</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB-821"><a href="#TagDB-821"><span class="linenos">821</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="TagDB-822"><a href="#TagDB-822"><span class="linenos">822</span></a>                    <span class="k">pass</span>
</span><span id="TagDB-823"><a href="#TagDB-823"><span class="linenos">823</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-824"><a href="#TagDB-824"><span class="linenos">824</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB-825"><a href="#TagDB-825"><span class="linenos">825</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-826"><a href="#TagDB-826"><span class="linenos">826</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-827"><a href="#TagDB-827"><span class="linenos">827</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="TagDB-828"><a href="#TagDB-828"><span class="linenos">828</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="TagDB-829"><a href="#TagDB-829"><span class="linenos">829</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="TagDB-830"><a href="#TagDB-830"><span class="linenos">830</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="TagDB-831"><a href="#TagDB-831"><span class="linenos">831</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="TagDB-832"><a href="#TagDB-832"><span class="linenos">832</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="TagDB-833"><a href="#TagDB-833"><span class="linenos">833</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB-834"><a href="#TagDB-834"><span class="linenos">834</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="TagDB-835"><a href="#TagDB-835"><span class="linenos">835</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="TagDB-836"><a href="#TagDB-836"><span class="linenos">836</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB-837"><a href="#TagDB-837"><span class="linenos">837</span></a>
</span><span id="TagDB-838"><a href="#TagDB-838"><span class="linenos">838</span></a>    <span class="k">def</span> <span class="nf">get_all_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB-839"><a href="#TagDB-839"><span class="linenos">839</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-840"><a href="#TagDB-840"><span class="linenos">840</span></a>        <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB-841"><a href="#TagDB-841"><span class="linenos">841</span></a>                                         <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB-842"><a href="#TagDB-842"><span class="linenos">842</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB-843"><a href="#TagDB-843"><span class="linenos">843</span></a>            <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB-844"><a href="#TagDB-844"><span class="linenos">844</span></a>                                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="TagDB-845"><a href="#TagDB-845"><span class="linenos">845</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">tags</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="TagDB-846"><a href="#TagDB-846"><span class="linenos">846</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-847"><a href="#TagDB-847"><span class="linenos">847</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-848"><a href="#TagDB-848"><span class="linenos">848</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(),</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="TagDB-849"><a href="#TagDB-849"><span class="linenos">849</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB-850"><a href="#TagDB-850"><span class="linenos">850</span></a>
</span><span id="TagDB-851"><a href="#TagDB-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="TagDB-852"><a href="#TagDB-852"><span class="linenos">852</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB-853"><a href="#TagDB-853"><span class="linenos">853</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB-854"><a href="#TagDB-854"><span class="linenos">854</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB-855"><a href="#TagDB-855"><span class="linenos">855</span></a>            <span class="k">if</span> <span class="n">isWithoutRootHash</span><span class="p">:</span>
</span><span id="TagDB-856"><a href="#TagDB-856"><span class="linenos">856</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB-857"><a href="#TagDB-857"><span class="linenos">857</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-858"><a href="#TagDB-858"><span class="linenos">858</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB-859"><a href="#TagDB-859"><span class="linenos">859</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-860"><a href="#TagDB-860"><span class="linenos">860</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-861"><a href="#TagDB-861"><span class="linenos">861</span></a>
</span><span id="TagDB-862"><a href="#TagDB-862"><span class="linenos">862</span></a>    <span class="k">def</span> <span class="nf">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB-863"><a href="#TagDB-863"><span class="linenos">863</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB-864"><a href="#TagDB-864"><span class="linenos">864</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB-865"><a href="#TagDB-865"><span class="linenos">865</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">])</span>
</span><span id="TagDB-866"><a href="#TagDB-866"><span class="linenos">866</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-867"><a href="#TagDB-867"><span class="linenos">867</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-868"><a href="#TagDB-868"><span class="linenos">868</span></a>
</span><span id="TagDB-869"><a href="#TagDB-869"><span class="linenos">869</span></a>    <span class="k">def</span> <span class="nf">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB-870"><a href="#TagDB-870"><span class="linenos">870</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB-871"><a href="#TagDB-871"><span class="linenos">871</span></a>
</span><span id="TagDB-872"><a href="#TagDB-872"><span class="linenos">872</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-873"><a href="#TagDB-873"><span class="linenos">873</span></a>
</span><span id="TagDB-874"><a href="#TagDB-874"><span class="linenos">874</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-875"><a href="#TagDB-875"><span class="linenos">875</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB-876"><a href="#TagDB-876"><span class="linenos">876</span></a>
</span><span id="TagDB-877"><a href="#TagDB-877"><span class="linenos">877</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-878"><a href="#TagDB-878"><span class="linenos">878</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB-879"><a href="#TagDB-879"><span class="linenos">879</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-880"><a href="#TagDB-880"><span class="linenos">880</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB-881"><a href="#TagDB-881"><span class="linenos">881</span></a>
</span><span id="TagDB-882"><a href="#TagDB-882"><span class="linenos">882</span></a>        <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB-883"><a href="#TagDB-883"><span class="linenos">883</span></a>        <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB-884"><a href="#TagDB-884"><span class="linenos">884</span></a>        <span class="c1"># setOfLenOfTheCommonTagHashSetForChecking = set()</span>
</span><span id="TagDB-885"><a href="#TagDB-885"><span class="linenos">885</span></a>        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB-886"><a href="#TagDB-886"><span class="linenos">886</span></a>        <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="TagDB-887"><a href="#TagDB-887"><span class="linenos">887</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-888"><a href="#TagDB-888"><span class="linenos">888</span></a>            <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="TagDB-889"><a href="#TagDB-889"><span class="linenos">889</span></a>                <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="TagDB-890"><a href="#TagDB-890"><span class="linenos">890</span></a>                <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="TagDB-891"><a href="#TagDB-891"><span class="linenos">891</span></a>        <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="TagDB-892"><a href="#TagDB-892"><span class="linenos">892</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB-893"><a href="#TagDB-893"><span class="linenos">893</span></a>            <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="TagDB-894"><a href="#TagDB-894"><span class="linenos">894</span></a>            <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB-895"><a href="#TagDB-895"><span class="linenos">895</span></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB-896"><a href="#TagDB-896"><span class="linenos">896</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span> <span class="o">!=</span> <span class="n">commonTagHashSet</span><span class="p">:</span>
</span><span id="TagDB-897"><a href="#TagDB-897"><span class="linenos">897</span></a>                    <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-898"><a href="#TagDB-898"><span class="linenos">898</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">commonTagHashSet</span>
</span><span id="TagDB-899"><a href="#TagDB-899"><span class="linenos">899</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB-900"><a href="#TagDB-900"><span class="linenos">900</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span>
</span><span id="TagDB-901"><a href="#TagDB-901"><span class="linenos">901</span></a>        <span class="c1">#         if tagHashSet != commonTagHashSet:</span>
</span><span id="TagDB-902"><a href="#TagDB-902"><span class="linenos">902</span></a>        <span class="c1">#             setOfLenOfTheCommonTagHashSetForChecking.add(len(commonTagHashSet))</span>
</span><span id="TagDB-903"><a href="#TagDB-903"><span class="linenos">903</span></a>        <span class="c1"># minimalTagPath = min(setOfLenOfTheCommonTagHashSetForChecking)</span>
</span><span id="TagDB-904"><a href="#TagDB-904"><span class="linenos">904</span></a>        <span class="c1"># pathDiff = minimalTagPath - len(tagHashSet)</span>
</span><span id="TagDB-905"><a href="#TagDB-905"><span class="linenos">905</span></a>        <span class="c1"># if pathDiff &gt; 0:</span>
</span><span id="TagDB-906"><a href="#TagDB-906"><span class="linenos">906</span></a>        <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB-907"><a href="#TagDB-907"><span class="linenos">907</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB-908"><a href="#TagDB-908"><span class="linenos">908</span></a>
</span><span id="TagDB-909"><a href="#TagDB-909"><span class="linenos">909</span></a>        <span class="n">setOfTheTagsForAReduction</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">-</span> <span class="n">tagHashSet</span>
</span><span id="TagDB-910"><a href="#TagDB-910"><span class="linenos">910</span></a>
</span><span id="TagDB-911"><a href="#TagDB-911"><span class="linenos">911</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTheTagsForAReduction</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB-912"><a href="#TagDB-912"><span class="linenos">912</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span><span id="TagDB-913"><a href="#TagDB-913"><span class="linenos">913</span></a>
</span><span id="TagDB-914"><a href="#TagDB-914"><span class="linenos">914</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB-915"><a href="#TagDB-915"><span class="linenos">915</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB-916"><a href="#TagDB-916"><span class="linenos">916</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span></pre></div>


    

                            <div id="TagDB.__init__" class="classattr">
                                        <input id="TagDB.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TagDB</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="TagDB.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.__init__-109"><a href="#TagDB.__init__-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">):</span>
</span><span id="TagDB.__init__-110"><a href="#TagDB.__init__-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">default_priority</span>
</span><span id="TagDB.__init__-111"><a href="#TagDB.__init__-111"><span class="linenos">111</span></a>
</span><span id="TagDB.__init__-112"><a href="#TagDB.__init__-112"><span class="linenos">112</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="TagDB.__init__-113"><a href="#TagDB.__init__-113"><span class="linenos">113</span></a>
</span><span id="TagDB.__init__-114"><a href="#TagDB.__init__-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - item hash; data - set of itemIDs</span>
</span><span id="TagDB.__init__-115"><a href="#TagDB.__init__-115"><span class="linenos">115</span></a>
</span><span id="TagDB.__init__-116"><a href="#TagDB.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - binItem</span>
</span><span id="TagDB.__init__-117"><a href="#TagDB.__init__-117"><span class="linenos">117</span></a>        <span class="c1"># TODO: заменить список тегов на хеш единожды сохраненного списка тегов</span>
</span><span id="TagDB.__init__-118"><a href="#TagDB.__init__-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - ItemID; data - sorted common TagsTuple&#39;s hash</span>
</span><span id="TagDB.__init__-119"><a href="#TagDB.__init__-119"><span class="linenos">119</span></a>
</span><span id="TagDB.__init__-120"><a href="#TagDB.__init__-120"><span class="linenos">120</span></a>        <span class="c1"># TODO: убрать tagsNumPerItemID из кода. Заменить этот список itemID - на список hashOfTheTagHashTuple</span>
</span><span id="TagDB.__init__-121"><a href="#TagDB.__init__-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - number of tags in this ItemID group; data - set of itemIDs which are have</span>
</span><span id="TagDB.__init__-122"><a href="#TagDB.__init__-122"><span class="linenos">122</span></a>            <span class="c1"># needed number of tags</span>
</span><span id="TagDB.__init__-123"><a href="#TagDB.__init__-123"><span class="linenos">123</span></a>
</span><span id="TagDB.__init__-124"><a href="#TagDB.__init__-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - tag hash; data - binTag</span>
</span><span id="TagDB.__init__-125"><a href="#TagDB.__init__-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - Tag hash; data - set of itemIDs</span>
</span><span id="TagDB.__init__-126"><a href="#TagDB.__init__-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - Tag hash; data - quantity of the items with this tag</span>
</span><span id="TagDB.__init__-127"><a href="#TagDB.__init__-127"><span class="linenos">127</span></a>
</span><span id="TagDB.__init__-128"><a href="#TagDB.__init__-128"><span class="linenos">128</span></a>
</span><span id="TagDB.__init__-129"><a href="#TagDB.__init__-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span> <span class="o">=</span> <span class="p">{}</span>  <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - sorted TagsTuple</span>
</span><span id="TagDB.__init__-130"><a href="#TagDB.__init__-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span> <span class="o">=</span> <span class="p">{}</span>   <span class="c1"># key - sorted common TagsTuple&#39;s hash; data - set of itemIDs</span>
</span><span id="TagDB.__init__-131"><a href="#TagDB.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span> <span class="o">=</span> <span class="p">{}</span>    <span class="c1"># key - number of tags; data - set of TagsTuple hashes</span>
</span><span id="TagDB.__init__-132"><a href="#TagDB.__init__-132"><span class="linenos">132</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>   <span class="c1"># {tagQntInGroup1, tagQntInGroup2, ..., tagQntInGroupN} where</span>
</span><span id="TagDB.__init__-133"><a href="#TagDB.__init__-133"><span class="linenos">133</span></a>            <span class="c1"># each Group is an key of the self.tagsQntPerCommonTagSet</span>
</span><span id="TagDB.__init__-134"><a href="#TagDB.__init__-134"><span class="linenos">134</span></a>
</span><span id="TagDB.__init__-135"><a href="#TagDB.__init__-135"><span class="linenos">135</span></a>        <span class="c1"># TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="TagDB.__init__-136"><a href="#TagDB.__init__-136"><span class="linenos">136</span></a>        <span class="c1"># где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="TagDB.__init__-137"><a href="#TagDB.__init__-137"><span class="linenos">137</span></a>        <span class="c1"># TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="TagDB.__init__-138"><a href="#TagDB.__init__-138"><span class="linenos">138</span></a>
</span><span id="TagDB.__init__-139"><a href="#TagDB.__init__-139"><span class="linenos">139</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}] и вычитывать это из него</span>
</span><span id="TagDB.__init__-140"><a href="#TagDB.__init__-140"><span class="linenos">140</span></a>        <span class="c1"># и/или</span>
</span><span id="TagDB.__init__-141"><a href="#TagDB.__init__-141"><span class="linenos">141</span></a>        <span class="c1"># TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashTuple_1, hashOfTheTagHashTuple_2, ...</span>
</span><span id="TagDB.__init__-142"><a href="#TagDB.__init__-142"><span class="linenos">142</span></a>        <span class="c1"># , hashOfTheTagHashTuple_N}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="TagDB.__init__-143"><a href="#TagDB.__init__-143"><span class="linenos">143</span></a>        <span class="c1"># где hashOfTheTagHashTuple - это tagHashTuple.__hash__()</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.default_priority" class="classattr">
                                <div class="attr variable">
            <span class="name">default_priority</span><span class="annotation">: cengal.parallel_execution.coroutines.coro_standard_services.loop_yield.versions.v_0.loop_yield.CoroPriority</span>

        
    </div>
    <a class="headerlink" href="#TagDB.default_priority"></a>
    
    

                            </div>
                            <div id="TagDB.itemsID" class="classattr">
                                <div class="attr variable">
            <span class="name">itemsID</span>

        
    </div>
    <a class="headerlink" href="#TagDB.itemsID"></a>
    
    

                            </div>
                            <div id="TagDB.itemIDsForItem" class="classattr">
                                <div class="attr variable">
            <span class="name">itemIDsForItem</span>

        
    </div>
    <a class="headerlink" href="#TagDB.itemIDsForItem"></a>
    
    

                            </div>
                            <div id="TagDB.itemsSet" class="classattr">
                                <div class="attr variable">
            <span class="name">itemsSet</span>

        
    </div>
    <a class="headerlink" href="#TagDB.itemsSet"></a>
    
    

                            </div>
                            <div id="TagDB.itemWithTags" class="classattr">
                                <div class="attr variable">
            <span class="name">itemWithTags</span>

        
    </div>
    <a class="headerlink" href="#TagDB.itemWithTags"></a>
    
    

                            </div>
                            <div id="TagDB.tagsNumPerItemID" class="classattr">
                                <div class="attr variable">
            <span class="name">tagsNumPerItemID</span>

        
    </div>
    <a class="headerlink" href="#TagDB.tagsNumPerItemID"></a>
    
    

                            </div>
                            <div id="TagDB.tagsSet" class="classattr">
                                <div class="attr variable">
            <span class="name">tagsSet</span>

        
    </div>
    <a class="headerlink" href="#TagDB.tagsSet"></a>
    
    

                            </div>
                            <div id="TagDB.tagWithItems" class="classattr">
                                <div class="attr variable">
            <span class="name">tagWithItems</span>

        
    </div>
    <a class="headerlink" href="#TagDB.tagWithItems"></a>
    
    

                            </div>
                            <div id="TagDB.tagsQnt" class="classattr">
                                <div class="attr variable">
            <span class="name">tagsQnt</span>

        
    </div>
    <a class="headerlink" href="#TagDB.tagsQnt"></a>
    
    

                            </div>
                            <div id="TagDB.commonTagSets" class="classattr">
                                <div class="attr variable">
            <span class="name">commonTagSets</span>

        
    </div>
    <a class="headerlink" href="#TagDB.commonTagSets"></a>
    
    

                            </div>
                            <div id="TagDB.itemsOnTheCommonTagSets" class="classattr">
                                <div class="attr variable">
            <span class="name">itemsOnTheCommonTagSets</span>

        
    </div>
    <a class="headerlink" href="#TagDB.itemsOnTheCommonTagSets"></a>
    
    

                            </div>
                            <div id="TagDB.tagsQntPerCommonTagSet" class="classattr">
                                <div class="attr variable">
            <span class="name">tagsQntPerCommonTagSet</span>

        
    </div>
    <a class="headerlink" href="#TagDB.tagsQntPerCommonTagSet"></a>
    
    

                            </div>
                            <div id="TagDB.setOfTagGroupQnt" class="classattr">
                                <div class="attr variable">
            <span class="name">setOfTagGroupQnt</span>

        
    </div>
    <a class="headerlink" href="#TagDB.setOfTagGroupQnt"></a>
    
    

                            </div>
                            <div id="TagDB.get_entity_stats" class="classattr">
                                        <input id="TagDB.get_entity_stats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_entity_stats</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">stats_level</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="TagDB.get_entity_stats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_entity_stats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_entity_stats-145"><a href="#TagDB.get_entity_stats-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="nf">get_entity_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stats_level</span><span class="p">:</span> <span class="s1">&#39;EntityStatsMixin.StatsLevel&#39;</span> <span class="o">=</span> <span class="n">EntityStatsMixin</span><span class="o">.</span><span class="n">StatsLevel</span><span class="o">.</span><span class="n">debug</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="TagDB.get_entity_stats-146"><a href="#TagDB.get_entity_stats-146"><span class="linenos">146</span></a>        <span class="k">return</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="p">,</span> <span class="p">{</span>
</span><span id="TagDB.get_entity_stats-147"><a href="#TagDB.get_entity_stats-147"><span class="linenos">147</span></a>            <span class="s1">&#39;items num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">),</span>
</span><span id="TagDB.get_entity_stats-148"><a href="#TagDB.get_entity_stats-148"><span class="linenos">148</span></a>            <span class="s1">&#39;tags num&#39;</span><span class="p">:</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">),</span>
</span><span id="TagDB.get_entity_stats-149"><a href="#TagDB.get_entity_stats-149"><span class="linenos">149</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_root_tag" class="classattr">
                                        <input id="TagDB.get_root_tag-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_root_tag</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_root_tag-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_root_tag"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_root_tag-151"><a href="#TagDB.get_root_tag-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">get_root_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TagDB.get_root_tag-152"><a href="#TagDB.get_root_tag-152"><span class="linenos">152</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">_ROOT_TAG</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.add_tag" class="classattr">
                                        <input id="TagDB.add_tag-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_tag</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTag</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.add_tag-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.add_tag"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.add_tag-154"><a href="#TagDB.add_tag-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="nf">add_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="TagDB.add_tag-155"><a href="#TagDB.add_tag-155"><span class="linenos">155</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.add_tag-156"><a href="#TagDB.add_tag-156"><span class="linenos">156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">binTag</span>
</span><span id="TagDB.add_tag-157"><a href="#TagDB.add_tag-157"><span class="linenos">157</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="TagDB.add_tag-158"><a href="#TagDB.add_tag-158"><span class="linenos">158</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB.add_tag-159"><a href="#TagDB.add_tag-159"><span class="linenos">159</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB.add_tag-160"><a href="#TagDB.add_tag-160"><span class="linenos">160</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.remove_tag" class="classattr">
                                        <input id="TagDB.remove_tag-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_tag</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTag</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.remove_tag-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.remove_tag"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.remove_tag-162"><a href="#TagDB.remove_tag-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">remove_tag</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTag</span><span class="p">):</span>
</span><span id="TagDB.remove_tag-163"><a href="#TagDB.remove_tag-163"><span class="linenos">163</span></a>        <span class="c1"># will try to delete given tag. If there is at least one item with this tag, than function will fail</span>
</span><span id="TagDB.remove_tag-164"><a href="#TagDB.remove_tag-164"><span class="linenos">164</span></a>        <span class="c1"># and will return False; otherwise it will delete given tag and will return True.</span>
</span><span id="TagDB.remove_tag-165"><a href="#TagDB.remove_tag-165"><span class="linenos">165</span></a>        <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TagDB.remove_tag-166"><a href="#TagDB.remove_tag-166"><span class="linenos">166</span></a>        <span class="n">tagHash</span> <span class="o">=</span> <span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.remove_tag-167"><a href="#TagDB.remove_tag-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-168"><a href="#TagDB.remove_tag-168"><span class="linenos">168</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-169"><a href="#TagDB.remove_tag-169"><span class="linenos">169</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-170"><a href="#TagDB.remove_tag-170"><span class="linenos">170</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_tag-171"><a href="#TagDB.remove_tag-171"><span class="linenos">171</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_tag-172"><a href="#TagDB.remove_tag-172"><span class="linenos">172</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TagDB.remove_tag-173"><a href="#TagDB.remove_tag-173"><span class="linenos">173</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-174"><a href="#TagDB.remove_tag-174"><span class="linenos">174</span></a>                    <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TagDB.remove_tag-175"><a href="#TagDB.remove_tag-175"><span class="linenos">175</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-176"><a href="#TagDB.remove_tag-176"><span class="linenos">176</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_tag-177"><a href="#TagDB.remove_tag-177"><span class="linenos">177</span></a>                <span class="n">functionResult</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TagDB.remove_tag-178"><a href="#TagDB.remove_tag-178"><span class="linenos">178</span></a>
</span><span id="TagDB.remove_tag-179"><a href="#TagDB.remove_tag-179"><span class="linenos">179</span></a>        <span class="k">if</span> <span class="n">functionResult</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-180"><a href="#TagDB.remove_tag-180"><span class="linenos">180</span></a>            <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB.remove_tag-181"><a href="#TagDB.remove_tag-181"><span class="linenos">181</span></a>                <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_tag-182"><a href="#TagDB.remove_tag-182"><span class="linenos">182</span></a>
</span><span id="TagDB.remove_tag-183"><a href="#TagDB.remove_tag-183"><span class="linenos">183</span></a>        <span class="k">return</span> <span class="n">functionResult</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.add_item" class="classattr">
                                        <input id="TagDB.add_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binItem</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.add_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.add_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.add_item-185"><a href="#TagDB.add_item-185"><span class="linenos">185</span></a>    <span class="k">def</span> <span class="nf">add_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB.add_item-186"><a href="#TagDB.add_item-186"><span class="linenos">186</span></a>        <span class="c1"># will add new item and return it&#39;s dynamic ID or None object If this Item already exist on the given tag path</span>
</span><span id="TagDB.add_item-187"><a href="#TagDB.add_item-187"><span class="linenos">187</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="TagDB.add_item-188"><a href="#TagDB.add_item-188"><span class="linenos">188</span></a>        <span class="c1"># the given binItem)  on this tag path</span>
</span><span id="TagDB.add_item-189"><a href="#TagDB.add_item-189"><span class="linenos">189</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.add_item-190"><a href="#TagDB.add_item-190"><span class="linenos">190</span></a>
</span><span id="TagDB.add_item-191"><a href="#TagDB.add_item-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.add_item-192"><a href="#TagDB.add_item-192"><span class="linenos">192</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.add_item-193"><a href="#TagDB.add_item-193"><span class="linenos">193</span></a>
</span><span id="TagDB.add_item-194"><a href="#TagDB.add_item-194"><span class="linenos">194</span></a>        <span class="c1"># may raise an exception in this place. Nope - from now it will be not</span>
</span><span id="TagDB.add_item-195"><a href="#TagDB.add_item-195"><span class="linenos">195</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.add_item-196"><a href="#TagDB.add_item-196"><span class="linenos">196</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="TagDB.add_item-197"><a href="#TagDB.add_item-197"><span class="linenos">197</span></a>
</span><span id="TagDB.add_item-198"><a href="#TagDB.add_item-198"><span class="linenos">198</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="p">()</span>
</span><span id="TagDB.add_item-199"><a href="#TagDB.add_item-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">binItem</span>
</span><span id="TagDB.add_item-200"><a href="#TagDB.add_item-200"><span class="linenos">200</span></a>
</span><span id="TagDB.add_item-201"><a href="#TagDB.add_item-201"><span class="linenos">201</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.add_item-202"><a href="#TagDB.add_item-202"><span class="linenos">202</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB.add_item-203"><a href="#TagDB.add_item-203"><span class="linenos">203</span></a>            <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB.add_item-204"><a href="#TagDB.add_item-204"><span class="linenos">204</span></a>            <span class="n">IDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB.add_item-205"><a href="#TagDB.add_item-205"><span class="linenos">205</span></a>            <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="TagDB.add_item-206"><a href="#TagDB.add_item-206"><span class="linenos">206</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.add_item-207"><a href="#TagDB.add_item-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB.add_item-208"><a href="#TagDB.add_item-208"><span class="linenos">208</span></a>
</span><span id="TagDB.add_item-209"><a href="#TagDB.add_item-209"><span class="linenos">209</span></a>        <span class="n">tagQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.add_item-210"><a href="#TagDB.add_item-210"><span class="linenos">210</span></a>        <span class="k">if</span> <span class="n">tagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="TagDB.add_item-211"><a href="#TagDB.add_item-211"><span class="linenos">211</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span>
</span><span id="TagDB.add_item-212"><a href="#TagDB.add_item-212"><span class="linenos">212</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB.add_item-213"><a href="#TagDB.add_item-213"><span class="linenos">213</span></a>            <span class="c1"># self.tagsNumPerItemID[tagQnt] = itemIDsSet</span>
</span><span id="TagDB.add_item-214"><a href="#TagDB.add_item-214"><span class="linenos">214</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.add_item-215"><a href="#TagDB.add_item-215"><span class="linenos">215</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagQnt</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB.add_item-216"><a href="#TagDB.add_item-216"><span class="linenos">216</span></a>
</span><span id="TagDB.add_item-217"><a href="#TagDB.add_item-217"><span class="linenos">217</span></a>        <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.add_item-218"><a href="#TagDB.add_item-218"><span class="linenos">218</span></a>
</span><span id="TagDB.add_item-219"><a href="#TagDB.add_item-219"><span class="linenos">219</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.add_item-220"><a href="#TagDB.add_item-220"><span class="linenos">220</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">add_tag</span><span class="p">(</span><span class="n">tag</span><span class="p">)</span>
</span><span id="TagDB.add_item-221"><a href="#TagDB.add_item-221"><span class="linenos">221</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.add_item-222"><a href="#TagDB.add_item-222"><span class="linenos">222</span></a>            <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB.add_item-223"><a href="#TagDB.add_item-223"><span class="linenos">223</span></a>            <span class="n">setOfItems</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.add_item-224"><a href="#TagDB.add_item-224"><span class="linenos">224</span></a>            <span class="k">if</span> <span class="n">itemID</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">setOfItems</span><span class="p">:</span>
</span><span id="TagDB.add_item-225"><a href="#TagDB.add_item-225"><span class="linenos">225</span></a>                <span class="n">setOfItems</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB.add_item-226"><a href="#TagDB.add_item-226"><span class="linenos">226</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB.add_item-227"><a href="#TagDB.add_item-227"><span class="linenos">227</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB.add_item-228"><a href="#TagDB.add_item-228"><span class="linenos">228</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.add_item-229"><a href="#TagDB.add_item-229"><span class="linenos">229</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="TagDB.add_item-230"><a href="#TagDB.add_item-230"><span class="linenos">230</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">setOfItems</span>
</span><span id="TagDB.add_item-231"><a href="#TagDB.add_item-231"><span class="linenos">231</span></a>
</span><span id="TagDB.add_item-232"><a href="#TagDB.add_item-232"><span class="linenos">232</span></a>        <span class="n">sortedTagTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">binTagHashes</span><span class="p">))</span>
</span><span id="TagDB.add_item-233"><a href="#TagDB.add_item-233"><span class="linenos">233</span></a>        <span class="n">hashOfTheSortedTagTuple</span> <span class="o">=</span> <span class="n">sortedTagTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.add_item-234"><a href="#TagDB.add_item-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span> <span class="o">=</span> <span class="n">hashOfTheSortedTagTuple</span>
</span><span id="TagDB.add_item-235"><a href="#TagDB.add_item-235"><span class="linenos">235</span></a>
</span><span id="TagDB.add_item-236"><a href="#TagDB.add_item-236"><span class="linenos">236</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="n">sortedTagTuple</span>
</span><span id="TagDB.add_item-237"><a href="#TagDB.add_item-237"><span class="linenos">237</span></a>
</span><span id="TagDB.add_item-238"><a href="#TagDB.add_item-238"><span class="linenos">238</span></a>        <span class="k">if</span> <span class="n">hashOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB.add_item-239"><a href="#TagDB.add_item-239"><span class="linenos">239</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="TagDB.add_item-240"><a href="#TagDB.add_item-240"><span class="linenos">240</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB.add_item-241"><a href="#TagDB.add_item-241"><span class="linenos">241</span></a>            <span class="c1"># self.itemsOnTheCommonTagSets[tagQnt] = itemIDsSet</span>
</span><span id="TagDB.add_item-242"><a href="#TagDB.add_item-242"><span class="linenos">242</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.add_item-243"><a href="#TagDB.add_item-243"><span class="linenos">243</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">itemID</span><span class="p">}</span>
</span><span id="TagDB.add_item-244"><a href="#TagDB.add_item-244"><span class="linenos">244</span></a>
</span><span id="TagDB.add_item-245"><a href="#TagDB.add_item-245"><span class="linenos">245</span></a>        <span class="n">lenOfTheSortedTagTuple</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB.add_item-246"><a href="#TagDB.add_item-246"><span class="linenos">246</span></a>        <span class="k">if</span> <span class="n">lenOfTheSortedTagTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="TagDB.add_item-247"><a href="#TagDB.add_item-247"><span class="linenos">247</span></a>            <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span>
</span><span id="TagDB.add_item-248"><a href="#TagDB.add_item-248"><span class="linenos">248</span></a>            <span class="n">itemIDsSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB.add_item-249"><a href="#TagDB.add_item-249"><span class="linenos">249</span></a>            <span class="c1"># self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple] = itemIDsSet</span>
</span><span id="TagDB.add_item-250"><a href="#TagDB.add_item-250"><span class="linenos">250</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.add_item-251"><a href="#TagDB.add_item-251"><span class="linenos">251</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="n">hashOfTheSortedTagTuple</span><span class="p">}</span>
</span><span id="TagDB.add_item-252"><a href="#TagDB.add_item-252"><span class="linenos">252</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">lenOfTheSortedTagTuple</span><span class="p">)</span>
</span><span id="TagDB.add_item-253"><a href="#TagDB.add_item-253"><span class="linenos">253</span></a>
</span><span id="TagDB.add_item-254"><a href="#TagDB.add_item-254"><span class="linenos">254</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.remove_item_by_itemID" class="classattr">
                                        <input id="TagDB.remove_item_by_itemID-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_item_by_itemID</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">itemID</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.remove_item_by_itemID-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.remove_item_by_itemID"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.remove_item_by_itemID-256"><a href="#TagDB.remove_item_by_itemID-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="nf">remove_item_by_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="TagDB.remove_item_by_itemID-257"><a href="#TagDB.remove_item_by_itemID-257"><span class="linenos">257</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.remove_item_by_itemID-258"><a href="#TagDB.remove_item_by_itemID-258"><span class="linenos">258</span></a>
</span><span id="TagDB.remove_item_by_itemID-259"><a href="#TagDB.remove_item_by_itemID-259"><span class="linenos">259</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-260"><a href="#TagDB.remove_item_by_itemID-260"><span class="linenos">260</span></a>            <span class="n">itemHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.remove_item_by_itemID-261"><a href="#TagDB.remove_item_by_itemID-261"><span class="linenos">261</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-262"><a href="#TagDB.remove_item_by_itemID-262"><span class="linenos">262</span></a>
</span><span id="TagDB.remove_item_by_itemID-263"><a href="#TagDB.remove_item_by_itemID-263"><span class="linenos">263</span></a>            <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-264"><a href="#TagDB.remove_item_by_itemID-264"><span class="linenos">264</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-265"><a href="#TagDB.remove_item_by_itemID-265"><span class="linenos">265</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-266"><a href="#TagDB.remove_item_by_itemID-266"><span class="linenos">266</span></a>                <span class="c1"># self.itemIDsForItem[itemHash] = IDsSet</span>
</span><span id="TagDB.remove_item_by_itemID-267"><a href="#TagDB.remove_item_by_itemID-267"><span class="linenos">267</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-268"><a href="#TagDB.remove_item_by_itemID-268"><span class="linenos">268</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-269"><a href="#TagDB.remove_item_by_itemID-269"><span class="linenos">269</span></a>
</span><span id="TagDB.remove_item_by_itemID-270"><a href="#TagDB.remove_item_by_itemID-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-271"><a href="#TagDB.remove_item_by_itemID-271"><span class="linenos">271</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-272"><a href="#TagDB.remove_item_by_itemID-272"><span class="linenos">272</span></a>            <span class="n">tagTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-273"><a href="#TagDB.remove_item_by_itemID-273"><span class="linenos">273</span></a>            <span class="n">numberOfTags</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="TagDB.remove_item_by_itemID-274"><a href="#TagDB.remove_item_by_itemID-274"><span class="linenos">274</span></a>
</span><span id="TagDB.remove_item_by_itemID-275"><a href="#TagDB.remove_item_by_itemID-275"><span class="linenos">275</span></a>            <span class="k">if</span> <span class="n">commonTagTupleHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-276"><a href="#TagDB.remove_item_by_itemID-276"><span class="linenos">276</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-277"><a href="#TagDB.remove_item_by_itemID-277"><span class="linenos">277</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-278"><a href="#TagDB.remove_item_by_itemID-278"><span class="linenos">278</span></a>                <span class="c1"># self.itemsOnTheCommonTagSets[commonTagTupleHash] = IDsSet</span>
</span><span id="TagDB.remove_item_by_itemID-279"><a href="#TagDB.remove_item_by_itemID-279"><span class="linenos">279</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-280"><a href="#TagDB.remove_item_by_itemID-280"><span class="linenos">280</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-281"><a href="#TagDB.remove_item_by_itemID-281"><span class="linenos">281</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-282"><a href="#TagDB.remove_item_by_itemID-282"><span class="linenos">282</span></a>                    <span class="k">if</span> <span class="n">numberOfTags</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-283"><a href="#TagDB.remove_item_by_itemID-283"><span class="linenos">283</span></a>                        <span class="n">setOfTagTuplesHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-284"><a href="#TagDB.remove_item_by_itemID-284"><span class="linenos">284</span></a>                        <span class="n">setOfTagTuplesHashes</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-285"><a href="#TagDB.remove_item_by_itemID-285"><span class="linenos">285</span></a>                        <span class="c1"># self.tagsQntPerCommonTagSet[numberOfTags] = setOfTagTuplesHashes</span>
</span><span id="TagDB.remove_item_by_itemID-286"><a href="#TagDB.remove_item_by_itemID-286"><span class="linenos">286</span></a>                        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagTuplesHashes</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-287"><a href="#TagDB.remove_item_by_itemID-287"><span class="linenos">287</span></a>                            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">numberOfTags</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-288"><a href="#TagDB.remove_item_by_itemID-288"><span class="linenos">288</span></a>                            <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">numberOfTags</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-289"><a href="#TagDB.remove_item_by_itemID-289"><span class="linenos">289</span></a>
</span><span id="TagDB.remove_item_by_itemID-290"><a href="#TagDB.remove_item_by_itemID-290"><span class="linenos">290</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-291"><a href="#TagDB.remove_item_by_itemID-291"><span class="linenos">291</span></a>
</span><span id="TagDB.remove_item_by_itemID-292"><a href="#TagDB.remove_item_by_itemID-292"><span class="linenos">292</span></a>            <span class="n">setOfTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagTuple</span><span class="p">)</span>
</span><span id="TagDB.remove_item_by_itemID-293"><a href="#TagDB.remove_item_by_itemID-293"><span class="linenos">293</span></a>
</span><span id="TagDB.remove_item_by_itemID-294"><a href="#TagDB.remove_item_by_itemID-294"><span class="linenos">294</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">setOfTagHashes</span><span class="p">)</span>
</span><span id="TagDB.remove_item_by_itemID-295"><a href="#TagDB.remove_item_by_itemID-295"><span class="linenos">295</span></a>            <span class="k">if</span> <span class="n">tagsQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-296"><a href="#TagDB.remove_item_by_itemID-296"><span class="linenos">296</span></a>                <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-297"><a href="#TagDB.remove_item_by_itemID-297"><span class="linenos">297</span></a>                <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-298"><a href="#TagDB.remove_item_by_itemID-298"><span class="linenos">298</span></a>                <span class="c1"># self.tagsNumPerItemID[tagsQnt] = IDsSet</span>
</span><span id="TagDB.remove_item_by_itemID-299"><a href="#TagDB.remove_item_by_itemID-299"><span class="linenos">299</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-300"><a href="#TagDB.remove_item_by_itemID-300"><span class="linenos">300</span></a>                    <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsNumPerItemID</span><span class="p">[</span><span class="n">tagsQnt</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-301"><a href="#TagDB.remove_item_by_itemID-301"><span class="linenos">301</span></a>
</span><span id="TagDB.remove_item_by_itemID-302"><a href="#TagDB.remove_item_by_itemID-302"><span class="linenos">302</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">setOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-303"><a href="#TagDB.remove_item_by_itemID-303"><span class="linenos">303</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.remove_item_by_itemID-304"><a href="#TagDB.remove_item_by_itemID-304"><span class="linenos">304</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-305"><a href="#TagDB.remove_item_by_itemID-305"><span class="linenos">305</span></a>                    <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-306"><a href="#TagDB.remove_item_by_itemID-306"><span class="linenos">306</span></a>                    <span class="n">tagsQuantity</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="TagDB.remove_item_by_itemID-307"><a href="#TagDB.remove_item_by_itemID-307"><span class="linenos">307</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-308"><a href="#TagDB.remove_item_by_itemID-308"><span class="linenos">308</span></a>                        <span class="n">tagsQuantity</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB.remove_item_by_itemID-309"><a href="#TagDB.remove_item_by_itemID-309"><span class="linenos">309</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span> <span class="o">=</span> <span class="n">tagsQuantity</span>
</span><span id="TagDB.remove_item_by_itemID-310"><a href="#TagDB.remove_item_by_itemID-310"><span class="linenos">310</span></a>                    <span class="k">if</span> <span class="n">tagsQuantity</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-311"><a href="#TagDB.remove_item_by_itemID-311"><span class="linenos">311</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-312"><a href="#TagDB.remove_item_by_itemID-312"><span class="linenos">312</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-313"><a href="#TagDB.remove_item_by_itemID-313"><span class="linenos">313</span></a>                <span class="k">if</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-314"><a href="#TagDB.remove_item_by_itemID-314"><span class="linenos">314</span></a>                    <span class="n">IDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-315"><a href="#TagDB.remove_item_by_itemID-315"><span class="linenos">315</span></a>                    <span class="n">IDsSet</span><span class="o">.</span><span class="n">difference_update</span><span class="p">({</span><span class="n">itemID</span><span class="p">})</span>
</span><span id="TagDB.remove_item_by_itemID-316"><a href="#TagDB.remove_item_by_itemID-316"><span class="linenos">316</span></a>                    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">IDsSet</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="TagDB.remove_item_by_itemID-317"><a href="#TagDB.remove_item_by_itemID-317"><span class="linenos">317</span></a>                        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagWithItems</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.remove_item_by_itemID-318"><a href="#TagDB.remove_item_by_itemID-318"><span class="linenos">318</span></a>                    <span class="c1"># self.tagWithItems[tagHash] = IDsSet</span>
</span><span id="TagDB.remove_item_by_itemID-319"><a href="#TagDB.remove_item_by_itemID-319"><span class="linenos">319</span></a>
</span><span id="TagDB.remove_item_by_itemID-320"><a href="#TagDB.remove_item_by_itemID-320"><span class="linenos">320</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">itemsID</span><span class="o">.</span><span class="n">remove_id</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.remove_item" class="classattr">
                                        <input id="TagDB.remove_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">binItem</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.remove_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.remove_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.remove_item-322"><a href="#TagDB.remove_item-322"><span class="linenos">322</span></a>    <span class="k">def</span> <span class="nf">remove_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB.remove_item-323"><a href="#TagDB.remove_item-323"><span class="linenos">323</span></a>        <span class="c1"># will return ItemId for deleted item or None object if Item is not exist</span>
</span><span id="TagDB.remove_item-324"><a href="#TagDB.remove_item-324"><span class="linenos">324</span></a>        <span class="c1"># Or will raise an exception if we already have more than one binItem (another item that is identical to</span>
</span><span id="TagDB.remove_item-325"><a href="#TagDB.remove_item-325"><span class="linenos">325</span></a>        <span class="c1"># the given binItem) on this tag path</span>
</span><span id="TagDB.remove_item-326"><a href="#TagDB.remove_item-326"><span class="linenos">326</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.remove_item-327"><a href="#TagDB.remove_item-327"><span class="linenos">327</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.remove_item-328"><a href="#TagDB.remove_item-328"><span class="linenos">328</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.remove_item-329"><a href="#TagDB.remove_item-329"><span class="linenos">329</span></a>        <span class="n">itemID</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">)</span>
</span><span id="TagDB.remove_item-330"><a href="#TagDB.remove_item-330"><span class="linenos">330</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.remove_item-331"><a href="#TagDB.remove_item-331"><span class="linenos">331</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">remove_item_by_itemID</span><span class="p">(</span><span class="n">itemID</span><span class="p">)</span>
</span><span id="TagDB.remove_item-332"><a href="#TagDB.remove_item-332"><span class="linenos">332</span></a>        <span class="k">return</span> <span class="n">itemID</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_itemID_from_item_and_tags" class="classattr">
                                        <input id="TagDB.get_itemID_from_item_and_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_itemID_from_item_and_tags</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">binItem</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_itemID_from_item_and_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_itemID_from_item_and_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_itemID_from_item_and_tags-350"><a href="#TagDB.get_itemID_from_item_and_tags-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="nf">get_itemID_from_item_and_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-351"><a href="#TagDB.get_itemID_from_item_and_tags-351"><span class="linenos">351</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-352"><a href="#TagDB.get_itemID_from_item_and_tags-352"><span class="linenos">352</span></a>
</span><span id="TagDB.get_itemID_from_item_and_tags-353"><a href="#TagDB.get_itemID_from_item_and_tags-353"><span class="linenos">353</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-354"><a href="#TagDB.get_itemID_from_item_and_tags-354"><span class="linenos">354</span></a>
</span><span id="TagDB.get_itemID_from_item_and_tags-355"><a href="#TagDB.get_itemID_from_item_and_tags-355"><span class="linenos">355</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-356"><a href="#TagDB.get_itemID_from_item_and_tags-356"><span class="linenos">356</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-357"><a href="#TagDB.get_itemID_from_item_and_tags-357"><span class="linenos">357</span></a>
</span><span id="TagDB.get_itemID_from_item_and_tags-358"><a href="#TagDB.get_itemID_from_item_and_tags-358"><span class="linenos">358</span></a>        <span class="n">potentialIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="n">binItem</span><span class="p">)</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-359"><a href="#TagDB.get_itemID_from_item_and_tags-359"><span class="linenos">359</span></a>        <span class="n">setOfBinTagsHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-360"><a href="#TagDB.get_itemID_from_item_and_tags-360"><span class="linenos">360</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-361"><a href="#TagDB.get_itemID_from_item_and_tags-361"><span class="linenos">361</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-362"><a href="#TagDB.get_itemID_from_item_and_tags-362"><span class="linenos">362</span></a>            <span class="n">setOfBinTagsHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-363"><a href="#TagDB.get_itemID_from_item_and_tags-363"><span class="linenos">363</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">potentialIDs</span><span class="p">:</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-364"><a href="#TagDB.get_itemID_from_item_and_tags-364"><span class="linenos">364</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-365"><a href="#TagDB.get_itemID_from_item_and_tags-365"><span class="linenos">365</span></a>            <span class="n">currentItemTagsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-366"><a href="#TagDB.get_itemID_from_item_and_tags-366"><span class="linenos">366</span></a>            <span class="k">if</span> <span class="n">setOfBinTagsHashes</span> <span class="o">==</span> <span class="n">currentItemTagsSet</span><span class="p">:</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-367"><a href="#TagDB.get_itemID_from_item_and_tags-367"><span class="linenos">367</span></a>                <span class="k">return</span> <span class="n">itemID</span>
</span><span id="TagDB.get_itemID_from_item_and_tags-368"><a href="#TagDB.get_itemID_from_item_and_tags-368"><span class="linenos">368</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.tag_hash_list_2_tag_list" class="classattr">
                                        <input id="TagDB.tag_hash_list_2_tag_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">tag_hash_list_2_tag_list</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tagHashList</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.tag_hash_list_2_tag_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.tag_hash_list_2_tag_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.tag_hash_list_2_tag_list-370"><a href="#TagDB.tag_hash_list_2_tag_list-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="nf">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashList</span><span class="p">):</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-371"><a href="#TagDB.tag_hash_list_2_tag_list-371"><span class="linenos">371</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-372"><a href="#TagDB.tag_hash_list_2_tag_list-372"><span class="linenos">372</span></a>
</span><span id="TagDB.tag_hash_list_2_tag_list-373"><a href="#TagDB.tag_hash_list_2_tag_list-373"><span class="linenos">373</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-374"><a href="#TagDB.tag_hash_list_2_tag_list-374"><span class="linenos">374</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashList</span><span class="p">:</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-375"><a href="#TagDB.tag_hash_list_2_tag_list-375"><span class="linenos">375</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-376"><a href="#TagDB.tag_hash_list_2_tag_list-376"><span class="linenos">376</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tagsSet</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB.tag_hash_list_2_tag_list-377"><a href="#TagDB.tag_hash_list_2_tag_list-377"><span class="linenos">377</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_item_and_tags_from_itemID" class="classattr">
                                        <input id="TagDB.get_item_and_tags_from_itemID-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_item_and_tags_from_itemID</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">itemID</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_item_and_tags_from_itemID-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_item_and_tags_from_itemID"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_item_and_tags_from_itemID-379"><a href="#TagDB.get_item_and_tags_from_itemID-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">get_item_and_tags_from_itemID</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">):</span>
</span><span id="TagDB.get_item_and_tags_from_itemID-380"><a href="#TagDB.get_item_and_tags_from_itemID-380"><span class="linenos">380</span></a>        <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.get_item_and_tags_from_itemID-381"><a href="#TagDB.get_item_and_tags_from_itemID-381"><span class="linenos">381</span></a>        <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()}</span>
</span><span id="TagDB.get_item_and_tags_from_itemID-382"><a href="#TagDB.get_item_and_tags_from_itemID-382"><span class="linenos">382</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB.get_item_and_tags_from_itemID-383"><a href="#TagDB.get_item_and_tags_from_itemID-383"><span class="linenos">383</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">],</span> <span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">))</span>
</span><span id="TagDB.get_item_and_tags_from_itemID-384"><a href="#TagDB.get_item_and_tags_from_itemID-384"><span class="linenos">384</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_top_tag_hash_list_by_qnt" class="classattr">
                                        <input id="TagDB.get_top_tag_hash_list_by_qnt-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_top_tag_hash_list_by_qnt</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tagHashSet</span>, </span><span class="param"><span class="n">local_tags_qnt</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_top_tag_hash_list_by_qnt-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_top_tag_hash_list_by_qnt"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_top_tag_hash_list_by_qnt-387"><a href="#TagDB.get_top_tag_hash_list_by_qnt-387"><span class="linenos">387</span></a>    <span class="k">def</span> <span class="nf">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-388"><a href="#TagDB.get_top_tag_hash_list_by_qnt-388"><span class="linenos">388</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-389"><a href="#TagDB.get_top_tag_hash_list_by_qnt-389"><span class="linenos">389</span></a>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-390"><a href="#TagDB.get_top_tag_hash_list_by_qnt-390"><span class="linenos">390</span></a>        <span class="n">tagsQnt</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-391"><a href="#TagDB.get_top_tag_hash_list_by_qnt-391"><span class="linenos">391</span></a>        <span class="k">if</span> <span class="n">local_tags_qnt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-392"><a href="#TagDB.get_top_tag_hash_list_by_qnt-392"><span class="linenos">392</span></a>            <span class="n">tagsQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-393"><a href="#TagDB.get_top_tag_hash_list_by_qnt-393"><span class="linenos">393</span></a>        <span class="n">tag_hash_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-394"><a href="#TagDB.get_top_tag_hash_list_by_qnt-394"><span class="linenos">394</span></a>        <span class="n">tag_by_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-395"><a href="#TagDB.get_top_tag_hash_list_by_qnt-395"><span class="linenos">395</span></a>        <span class="n">tag_by_qnt__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-396"><a href="#TagDB.get_top_tag_hash_list_by_qnt-396"><span class="linenos">396</span></a>        <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-397"><a href="#TagDB.get_top_tag_hash_list_by_qnt-397"><span class="linenos">397</span></a>        <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">tag_hash_set</span><span class="p">:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-398"><a href="#TagDB.get_top_tag_hash_list_by_qnt-398"><span class="linenos">398</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-399"><a href="#TagDB.get_top_tag_hash_list_by_qnt-399"><span class="linenos">399</span></a>            <span class="n">qnt</span> <span class="o">=</span> <span class="n">tagsQnt</span><span class="p">[</span><span class="n">tag_hash</span><span class="p">]</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-400"><a href="#TagDB.get_top_tag_hash_list_by_qnt-400"><span class="linenos">400</span></a>            <span class="k">if</span> <span class="n">qnt</span> <span class="o">&gt;</span> <span class="n">biggest_qnt</span><span class="p">:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-401"><a href="#TagDB.get_top_tag_hash_list_by_qnt-401"><span class="linenos">401</span></a>                <span class="n">biggest_qnt</span> <span class="o">=</span> <span class="n">qnt</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-402"><a href="#TagDB.get_top_tag_hash_list_by_qnt-402"><span class="linenos">402</span></a>            <span class="c1"># if qnt not in tag_by_qnt:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-403"><a href="#TagDB.get_top_tag_hash_list_by_qnt-403"><span class="linenos">403</span></a>            <span class="c1">#     tag_by_qnt[qnt] = set()</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-404"><a href="#TagDB.get_top_tag_hash_list_by_qnt-404"><span class="linenos">404</span></a>            <span class="c1"># tag_by_qnt[qnt].add(tag_hash)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-405"><a href="#TagDB.get_top_tag_hash_list_by_qnt-405"><span class="linenos">405</span></a>            <span class="n">tag_by_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">qnt</span><span class="p">,</span> <span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-406"><a href="#TagDB.get_top_tag_hash_list_by_qnt-406"><span class="linenos">406</span></a>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-407"><a href="#TagDB.get_top_tag_hash_list_by_qnt-407"><span class="linenos">407</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-408"><a href="#TagDB.get_top_tag_hash_list_by_qnt-408"><span class="linenos">408</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-409"><a href="#TagDB.get_top_tag_hash_list_by_qnt-409"><span class="linenos">409</span></a>            <span class="c1"># biggest_qnt = max(tag_by_qnt)</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-410"><a href="#TagDB.get_top_tag_hash_list_by_qnt-410"><span class="linenos">410</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">tag_by_qnt</span><span class="p">[</span><span class="n">biggest_qnt</span><span class="p">])</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-411"><a href="#TagDB.get_top_tag_hash_list_by_qnt-411"><span class="linenos">411</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-412"><a href="#TagDB.get_top_tag_hash_list_by_qnt-412"><span class="linenos">412</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TagDB.get_top_tag_hash_list_by_qnt-413"><a href="#TagDB.get_top_tag_hash_list_by_qnt-413"><span class="linenos">413</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.sort_tag_hash_list_by_qnt" class="classattr">
                                        <input id="TagDB.sort_tag_hash_list_by_qnt-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sort_tag_hash_list_by_qnt</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tagHashSet</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.sort_tag_hash_list_by_qnt-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.sort_tag_hash_list_by_qnt"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.sort_tag_hash_list_by_qnt-415"><a href="#TagDB.sort_tag_hash_list_by_qnt-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-416"><a href="#TagDB.sort_tag_hash_list_by_qnt-416"><span class="linenos">416</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-417"><a href="#TagDB.sort_tag_hash_list_by_qnt-417"><span class="linenos">417</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-418"><a href="#TagDB.sort_tag_hash_list_by_qnt-418"><span class="linenos">418</span></a>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-419"><a href="#TagDB.sort_tag_hash_list_by_qnt-419"><span class="linenos">419</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-420"><a href="#TagDB.sort_tag_hash_list_by_qnt-420"><span class="linenos">420</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-421"><a href="#TagDB.sort_tag_hash_list_by_qnt-421"><span class="linenos">421</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-422"><a href="#TagDB.sort_tag_hash_list_by_qnt-422"><span class="linenos">422</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-423"><a href="#TagDB.sort_tag_hash_list_by_qnt-423"><span class="linenos">423</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-424"><a href="#TagDB.sort_tag_hash_list_by_qnt-424"><span class="linenos">424</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_qnt-425"><a href="#TagDB.sort_tag_hash_list_by_qnt-425"><span class="linenos">425</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.sort_tag_list_by_qnt" class="classattr">
                                        <input id="TagDB.sort_tag_list_by_qnt-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sort_tag_list_by_qnt</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.sort_tag_list_by_qnt-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.sort_tag_list_by_qnt"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.sort_tag_list_by_qnt-427"><a href="#TagDB.sort_tag_list_by_qnt-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_qnt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB.sort_tag_list_by_qnt-428"><a href="#TagDB.sort_tag_list_by_qnt-428"><span class="linenos">428</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_qnt-429"><a href="#TagDB.sort_tag_list_by_qnt-429"><span class="linenos">429</span></a>
</span><span id="TagDB.sort_tag_list_by_qnt-430"><a href="#TagDB.sort_tag_list_by_qnt-430"><span class="linenos">430</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_qnt-431"><a href="#TagDB.sort_tag_list_by_qnt-431"><span class="linenos">431</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_qnt-432"><a href="#TagDB.sort_tag_list_by_qnt-432"><span class="linenos">432</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.sort_tag_list_by_qnt-433"><a href="#TagDB.sort_tag_list_by_qnt-433"><span class="linenos">433</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_qnt-434"><a href="#TagDB.sort_tag_list_by_qnt-434"><span class="linenos">434</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_qnt-435"><a href="#TagDB.sort_tag_list_by_qnt-435"><span class="linenos">435</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">])</span>
</span><span id="TagDB.sort_tag_list_by_qnt-436"><a href="#TagDB.sort_tag_list_by_qnt-436"><span class="linenos">436</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_qnt-437"><a href="#TagDB.sort_tag_list_by_qnt-437"><span class="linenos">437</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.sort_tag_hash_list_by_hash" class="classattr">
                                        <input id="TagDB.sort_tag_hash_list_by_hash-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sort_tag_hash_list_by_hash</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">tagHashSet</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.sort_tag_hash_list_by_hash-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.sort_tag_hash_list_by_hash"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.sort_tag_hash_list_by_hash-439"><a href="#TagDB.sort_tag_hash_list_by_hash-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-440"><a href="#TagDB.sort_tag_hash_list_by_hash-440"><span class="linenos">440</span></a>        <span class="c1"># will return sorted tag list - not sorted tag hash list</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-441"><a href="#TagDB.sort_tag_hash_list_by_hash-441"><span class="linenos">441</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-442"><a href="#TagDB.sort_tag_hash_list_by_hash-442"><span class="linenos">442</span></a>
</span><span id="TagDB.sort_tag_hash_list_by_hash-443"><a href="#TagDB.sort_tag_hash_list_by_hash-443"><span class="linenos">443</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-444"><a href="#TagDB.sort_tag_hash_list_by_hash-444"><span class="linenos">444</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-445"><a href="#TagDB.sort_tag_hash_list_by_hash-445"><span class="linenos">445</span></a>        <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">tagHashSet</span><span class="p">:</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-446"><a href="#TagDB.sort_tag_hash_list_by_hash-446"><span class="linenos">446</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-447"><a href="#TagDB.sort_tag_hash_list_by_hash-447"><span class="linenos">447</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tagHash</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-448"><a href="#TagDB.sort_tag_hash_list_by_hash-448"><span class="linenos">448</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_hash_list_by_hash-449"><a href="#TagDB.sort_tag_hash_list_by_hash-449"><span class="linenos">449</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.sort_tag_list_by_hash" class="classattr">
                                        <input id="TagDB.sort_tag_list_by_hash-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sort_tag_list_by_hash</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.sort_tag_list_by_hash-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.sort_tag_list_by_hash"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.sort_tag_list_by_hash-451"><a href="#TagDB.sort_tag_list_by_hash-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">sort_tag_list_by_hash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB.sort_tag_list_by_hash-452"><a href="#TagDB.sort_tag_list_by_hash-452"><span class="linenos">452</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_hash-453"><a href="#TagDB.sort_tag_list_by_hash-453"><span class="linenos">453</span></a>
</span><span id="TagDB.sort_tag_list_by_hash-454"><a href="#TagDB.sort_tag_list_by_hash-454"><span class="linenos">454</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_hash-455"><a href="#TagDB.sort_tag_list_by_hash-455"><span class="linenos">455</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_hash-456"><a href="#TagDB.sort_tag_list_by_hash-456"><span class="linenos">456</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.sort_tag_list_by_hash-457"><a href="#TagDB.sort_tag_list_by_hash-457"><span class="linenos">457</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_hash-458"><a href="#TagDB.sort_tag_list_by_hash-458"><span class="linenos">458</span></a>            <span class="n">tagHash</span> <span class="o">=</span> <span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.sort_tag_list_by_hash-459"><a href="#TagDB.sort_tag_list_by_hash-459"><span class="linenos">459</span></a>            <span class="n">tagWithWeight</span> <span class="o">=</span> <span class="p">(</span><span class="n">tag</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_hash-460"><a href="#TagDB.sort_tag_list_by_hash-460"><span class="linenos">460</span></a>            <span class="n">rawTagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">tagWithWeight</span><span class="p">)</span>
</span><span id="TagDB.sort_tag_list_by_hash-461"><a href="#TagDB.sort_tag_list_by_hash-461"><span class="linenos">461</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_raw_tag_list</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.sort_raw_tag_list" class="classattr">
                                        <input id="TagDB.sort_raw_tag_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">sort_raw_tag_list</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">rawTagList</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.sort_raw_tag_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.sort_raw_tag_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.sort_raw_tag_list-463"><a href="#TagDB.sort_raw_tag_list-463"><span class="linenos">463</span></a>    <span class="k">def</span> <span class="nf">sort_raw_tag_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rawTagList</span><span class="p">):</span>
</span><span id="TagDB.sort_raw_tag_list-464"><a href="#TagDB.sort_raw_tag_list-464"><span class="linenos">464</span></a>        <span class="c1"># will return sorted tag list</span>
</span><span id="TagDB.sort_raw_tag_list-465"><a href="#TagDB.sort_raw_tag_list-465"><span class="linenos">465</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.sort_raw_tag_list-466"><a href="#TagDB.sort_raw_tag_list-466"><span class="linenos">466</span></a>
</span><span id="TagDB.sort_raw_tag_list-467"><a href="#TagDB.sort_raw_tag_list-467"><span class="linenos">467</span></a>        <span class="n">rawTagList</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">rawTagList</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">tagAndWeight</span><span class="p">:</span> <span class="n">tagAndWeight</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB.sort_raw_tag_list-468"><a href="#TagDB.sort_raw_tag_list-468"><span class="linenos">468</span></a>        <span class="n">tagList</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.sort_raw_tag_list-469"><a href="#TagDB.sort_raw_tag_list-469"><span class="linenos">469</span></a>        <span class="k">for</span> <span class="n">rawTag</span> <span class="ow">in</span> <span class="n">rawTagList</span><span class="p">:</span>
</span><span id="TagDB.sort_raw_tag_list-470"><a href="#TagDB.sort_raw_tag_list-470"><span class="linenos">470</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.sort_raw_tag_list-471"><a href="#TagDB.sort_raw_tag_list-471"><span class="linenos">471</span></a>            <span class="n">tagList</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">rawTag</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="TagDB.sort_raw_tag_list-472"><a href="#TagDB.sort_raw_tag_list-472"><span class="linenos">472</span></a>        <span class="k">return</span> <span class="n">tagList</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_itemIDs_from_tags" class="classattr">
                                        <input id="TagDB.get_itemIDs_from_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_itemIDs_from_tags</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">binTags</span>,</span><span class="param">	<span class="n">treeType</span><span class="o">=</span><span class="mi">3</span>,</span><span class="param">	<span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_itemIDs_from_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_itemIDs_from_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_itemIDs_from_tags-474"><a href="#TagDB.get_itemIDs_from_tags-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">get_itemIDs_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB.get_itemIDs_from_tags-475"><a href="#TagDB.get_itemIDs_from_tags-475"><span class="linenos">475</span></a>                              <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB.get_itemIDs_from_tags-476"><a href="#TagDB.get_itemIDs_from_tags-476"><span class="linenos">476</span></a>        <span class="c1"># TODO: исправить ошибку: SMART_TREE_TYPE: возвращает не только список файлов в текущей директории, но и из</span>
</span><span id="TagDB.get_itemIDs_from_tags-477"><a href="#TagDB.get_itemIDs_from_tags-477"><span class="linenos">477</span></a>        <span class="c1"># непосредственных подпапок данной папки</span>
</span><span id="TagDB.get_itemIDs_from_tags-478"><a href="#TagDB.get_itemIDs_from_tags-478"><span class="linenos">478</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-479"><a href="#TagDB.get_itemIDs_from_tags-479"><span class="linenos">479</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="TagDB.get_itemIDs_from_tags-480"><a href="#TagDB.get_itemIDs_from_tags-480"><span class="linenos">480</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="TagDB.get_itemIDs_from_tags-481"><a href="#TagDB.get_itemIDs_from_tags-481"><span class="linenos">481</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB.get_itemIDs_from_tags-482"><a href="#TagDB.get_itemIDs_from_tags-482"><span class="linenos">482</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-483"><a href="#TagDB.get_itemIDs_from_tags-483"><span class="linenos">483</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-484"><a href="#TagDB.get_itemIDs_from_tags-484"><span class="linenos">484</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-485"><a href="#TagDB.get_itemIDs_from_tags-485"><span class="linenos">485</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-486"><a href="#TagDB.get_itemIDs_from_tags-486"><span class="linenos">486</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-487"><a href="#TagDB.get_itemIDs_from_tags-487"><span class="linenos">487</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.get_itemIDs_from_tags-488"><a href="#TagDB.get_itemIDs_from_tags-488"><span class="linenos">488</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-489"><a href="#TagDB.get_itemIDs_from_tags-489"><span class="linenos">489</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-490"><a href="#TagDB.get_itemIDs_from_tags-490"><span class="linenos">490</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-491"><a href="#TagDB.get_itemIDs_from_tags-491"><span class="linenos">491</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-492"><a href="#TagDB.get_itemIDs_from_tags-492"><span class="linenos">492</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.get_itemIDs_from_tags-493"><a href="#TagDB.get_itemIDs_from_tags-493"><span class="linenos">493</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-494"><a href="#TagDB.get_itemIDs_from_tags-494"><span class="linenos">494</span></a>        <span class="c1"># PLAIN_PSEUDO_TREE_TYPE</span>
</span><span id="TagDB.get_itemIDs_from_tags-495"><a href="#TagDB.get_itemIDs_from_tags-495"><span class="linenos">495</span></a>        <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-496"><a href="#TagDB.get_itemIDs_from_tags-496"><span class="linenos">496</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-497"><a href="#TagDB.get_itemIDs_from_tags-497"><span class="linenos">497</span></a>            <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-498"><a href="#TagDB.get_itemIDs_from_tags-498"><span class="linenos">498</span></a>            <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-499"><a href="#TagDB.get_itemIDs_from_tags-499"><span class="linenos">499</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-500"><a href="#TagDB.get_itemIDs_from_tags-500"><span class="linenos">500</span></a>            <span class="n">itemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-501"><a href="#TagDB.get_itemIDs_from_tags-501"><span class="linenos">501</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">))</span>
</span><span id="TagDB.get_itemIDs_from_tags-502"><a href="#TagDB.get_itemIDs_from_tags-502"><span class="linenos">502</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-503"><a href="#TagDB.get_itemIDs_from_tags-503"><span class="linenos">503</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-504"><a href="#TagDB.get_itemIDs_from_tags-504"><span class="linenos">504</span></a>                <span class="n">itemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="TagDB.get_itemIDs_from_tags-505"><a href="#TagDB.get_itemIDs_from_tags-505"><span class="linenos">505</span></a>            <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-506"><a href="#TagDB.get_itemIDs_from_tags-506"><span class="linenos">506</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-507"><a href="#TagDB.get_itemIDs_from_tags-507"><span class="linenos">507</span></a>                <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-508"><a href="#TagDB.get_itemIDs_from_tags-508"><span class="linenos">508</span></a>                    <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="TagDB.get_itemIDs_from_tags-509"><a href="#TagDB.get_itemIDs_from_tags-509"><span class="linenos">509</span></a>                    <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-510"><a href="#TagDB.get_itemIDs_from_tags-510"><span class="linenos">510</span></a>            <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-511"><a href="#TagDB.get_itemIDs_from_tags-511"><span class="linenos">511</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-512"><a href="#TagDB.get_itemIDs_from_tags-512"><span class="linenos">512</span></a>                <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="TagDB.get_itemIDs_from_tags-513"><a href="#TagDB.get_itemIDs_from_tags-513"><span class="linenos">513</span></a>                <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-514"><a href="#TagDB.get_itemIDs_from_tags-514"><span class="linenos">514</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">commonTagHashSet</span><span class="p">):</span>
</span><span id="TagDB.get_itemIDs_from_tags-515"><a href="#TagDB.get_itemIDs_from_tags-515"><span class="linenos">515</span></a>                    <span class="n">itemIDSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">])</span>
</span><span id="TagDB.get_itemIDs_from_tags-516"><a href="#TagDB.get_itemIDs_from_tags-516"><span class="linenos">516</span></a>                <span class="c1"># # if len(tagHashSet &amp; commonTagHashSet) == len(tagHashSet):</span>
</span><span id="TagDB.get_itemIDs_from_tags-517"><a href="#TagDB.get_itemIDs_from_tags-517"><span class="linenos">517</span></a>                <span class="c1"># res_set = tagHashSet.intersection(commonTagHashSet)</span>
</span><span id="TagDB.get_itemIDs_from_tags-518"><a href="#TagDB.get_itemIDs_from_tags-518"><span class="linenos">518</span></a>                <span class="c1"># if len(res_set) == binTagsQnt:</span>
</span><span id="TagDB.get_itemIDs_from_tags-519"><a href="#TagDB.get_itemIDs_from_tags-519"><span class="linenos">519</span></a>                <span class="c1">#     itemIDSet = itemIDSet | self.itemsOnTheCommonTagSets[commonTagGroupHash]</span>
</span><span id="TagDB.get_itemIDs_from_tags-520"><a href="#TagDB.get_itemIDs_from_tags-520"><span class="linenos">520</span></a>            <span class="n">interceptionOfItemsWithTags</span> <span class="o">=</span> <span class="n">itemIDSet</span>
</span><span id="TagDB.get_itemIDs_from_tags-521"><a href="#TagDB.get_itemIDs_from_tags-521"><span class="linenos">521</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-522"><a href="#TagDB.get_itemIDs_from_tags-522"><span class="linenos">522</span></a>            <span class="c1"># isFirstHash = True</span>
</span><span id="TagDB.get_itemIDs_from_tags-523"><a href="#TagDB.get_itemIDs_from_tags-523"><span class="linenos">523</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="TagDB.get_itemIDs_from_tags-524"><a href="#TagDB.get_itemIDs_from_tags-524"><span class="linenos">524</span></a>            <span class="c1">#     tagHash = tag.__hash__()</span>
</span><span id="TagDB.get_itemIDs_from_tags-525"><a href="#TagDB.get_itemIDs_from_tags-525"><span class="linenos">525</span></a>            <span class="c1">#     if tagHash in self.tagWithItems:</span>
</span><span id="TagDB.get_itemIDs_from_tags-526"><a href="#TagDB.get_itemIDs_from_tags-526"><span class="linenos">526</span></a>            <span class="c1">#         if isFirstHash:</span>
</span><span id="TagDB.get_itemIDs_from_tags-527"><a href="#TagDB.get_itemIDs_from_tags-527"><span class="linenos">527</span></a>            <span class="c1">#             interceptionOfItemsWithTags = self.tagWithItems[tagHash]</span>
</span><span id="TagDB.get_itemIDs_from_tags-528"><a href="#TagDB.get_itemIDs_from_tags-528"><span class="linenos">528</span></a>            <span class="c1">#             isFirstHash = False</span>
</span><span id="TagDB.get_itemIDs_from_tags-529"><a href="#TagDB.get_itemIDs_from_tags-529"><span class="linenos">529</span></a>            <span class="c1">#         else:</span>
</span><span id="TagDB.get_itemIDs_from_tags-530"><a href="#TagDB.get_itemIDs_from_tags-530"><span class="linenos">530</span></a>            <span class="c1">#             itemsWithTag = self.tagWithItems[tagHash]</span>
</span><span id="TagDB.get_itemIDs_from_tags-531"><a href="#TagDB.get_itemIDs_from_tags-531"><span class="linenos">531</span></a>            <span class="c1">#             interceptionOfItemsWithTags = interceptionOfItemsWithTags &amp; itemsWithTag</span>
</span><span id="TagDB.get_itemIDs_from_tags-532"><a href="#TagDB.get_itemIDs_from_tags-532"><span class="linenos">532</span></a>            <span class="c1">#     else:</span>
</span><span id="TagDB.get_itemIDs_from_tags-533"><a href="#TagDB.get_itemIDs_from_tags-533"><span class="linenos">533</span></a>            <span class="c1">#         # TODO: произвести такую же провеку в get_items_from_tags() и build_smart_tree()</span>
</span><span id="TagDB.get_itemIDs_from_tags-534"><a href="#TagDB.get_itemIDs_from_tags-534"><span class="linenos">534</span></a>            <span class="c1">#         if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="TagDB.get_itemIDs_from_tags-535"><a href="#TagDB.get_itemIDs_from_tags-535"><span class="linenos">535</span></a>            <span class="c1">#             result = (set(), set())</span>
</span><span id="TagDB.get_itemIDs_from_tags-536"><a href="#TagDB.get_itemIDs_from_tags-536"><span class="linenos">536</span></a>            <span class="c1">#             return result</span>
</span><span id="TagDB.get_itemIDs_from_tags-537"><a href="#TagDB.get_itemIDs_from_tags-537"><span class="linenos">537</span></a>            <span class="c1">#         else:</span>
</span><span id="TagDB.get_itemIDs_from_tags-538"><a href="#TagDB.get_itemIDs_from_tags-538"><span class="linenos">538</span></a>            <span class="c1">#             return set()</span>
</span><span id="TagDB.get_itemIDs_from_tags-539"><a href="#TagDB.get_itemIDs_from_tags-539"><span class="linenos">539</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-540"><a href="#TagDB.get_itemIDs_from_tags-540"><span class="linenos">540</span></a>        <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="TagDB.get_itemIDs_from_tags-541"><a href="#TagDB.get_itemIDs_from_tags-541"><span class="linenos">541</span></a>        <span class="n">setOfAllInternalItemIDsForThisSetOfTags</span> <span class="o">=</span> <span class="n">interceptionOfItemsWithTags</span>
</span><span id="TagDB.get_itemIDs_from_tags-542"><a href="#TagDB.get_itemIDs_from_tags-542"><span class="linenos">542</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-543"><a href="#TagDB.get_itemIDs_from_tags-543"><span class="linenos">543</span></a>        <span class="c1"># SMART_TREE_TYPE or FULL_TREE_TYPE</span>
</span><span id="TagDB.get_itemIDs_from_tags-544"><a href="#TagDB.get_itemIDs_from_tags-544"><span class="linenos">544</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB.get_itemIDs_from_tags-545"><a href="#TagDB.get_itemIDs_from_tags-545"><span class="linenos">545</span></a>            <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-546"><a href="#TagDB.get_itemIDs_from_tags-546"><span class="linenos">546</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_hash</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-547"><a href="#TagDB.get_itemIDs_from_tags-547"><span class="linenos">547</span></a>            <span class="n">binTagHashTuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">binTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB.get_itemIDs_from_tags-548"><a href="#TagDB.get_itemIDs_from_tags-548"><span class="linenos">548</span></a>            <span class="n">hashOfTheBinTagHashTuple</span> <span class="o">=</span> <span class="n">binTagHashTuple</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-549"><a href="#TagDB.get_itemIDs_from_tags-549"><span class="linenos">549</span></a>            <span class="k">if</span> <span class="n">hashOfTheBinTagHashTuple</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-550"><a href="#TagDB.get_itemIDs_from_tags-550"><span class="linenos">550</span></a>                <span class="n">resultItemIDSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemsOnTheCommonTagSets</span><span class="p">[</span><span class="n">hashOfTheBinTagHashTuple</span><span class="p">]</span>
</span><span id="TagDB.get_itemIDs_from_tags-551"><a href="#TagDB.get_itemIDs_from_tags-551"><span class="linenos">551</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-552"><a href="#TagDB.get_itemIDs_from_tags-552"><span class="linenos">552</span></a>            <span class="c1"># filteredItemIDsSet = set()</span>
</span><span id="TagDB.get_itemIDs_from_tags-553"><a href="#TagDB.get_itemIDs_from_tags-553"><span class="linenos">553</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="TagDB.get_itemIDs_from_tags-554"><a href="#TagDB.get_itemIDs_from_tags-554"><span class="linenos">554</span></a>            <span class="c1"># # for itemID in setOfAllInternalItemIDsForThisSetOfTags:</span>
</span><span id="TagDB.get_itemIDs_from_tags-555"><a href="#TagDB.get_itemIDs_from_tags-555"><span class="linenos">555</span></a>            <span class="c1"># #     if len(self.itemWithTags[itemID]) == tagQnt:</span>
</span><span id="TagDB.get_itemIDs_from_tags-556"><a href="#TagDB.get_itemIDs_from_tags-556"><span class="linenos">556</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}]</span>
</span><span id="TagDB.get_itemIDs_from_tags-557"><a href="#TagDB.get_itemIDs_from_tags-557"><span class="linenos">557</span></a>            <span class="c1"># #         # и вычитывать это из него</span>
</span><span id="TagDB.get_itemIDs_from_tags-558"><a href="#TagDB.get_itemIDs_from_tags-558"><span class="linenos">558</span></a>            <span class="c1"># #         # и/или</span>
</span><span id="TagDB.get_itemIDs_from_tags-559"><a href="#TagDB.get_itemIDs_from_tags-559"><span class="linenos">559</span></a>            <span class="c1"># #         # _TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashSet_1, hashOfTheTagHashSet_2, ...</span>
</span><span id="TagDB.get_itemIDs_from_tags-560"><a href="#TagDB.get_itemIDs_from_tags-560"><span class="linenos">560</span></a>            <span class="c1"># #         # , hashOfTheTagHashSet_3}] и вычитывать это из него, а потом уже и из каждого tagHashSet</span>
</span><span id="TagDB.get_itemIDs_from_tags-561"><a href="#TagDB.get_itemIDs_from_tags-561"><span class="linenos">561</span></a>            <span class="c1"># #         # где hashOfTheTagHashSet - это tagHashSet.__hash__()</span>
</span><span id="TagDB.get_itemIDs_from_tags-562"><a href="#TagDB.get_itemIDs_from_tags-562"><span class="linenos">562</span></a>            <span class="c1"># #         filteredItemIDsSet.add(itemID)</span>
</span><span id="TagDB.get_itemIDs_from_tags-563"><a href="#TagDB.get_itemIDs_from_tags-563"><span class="linenos">563</span></a>            <span class="c1"># if tagQnt in self.tagsNumPerItemID:</span>
</span><span id="TagDB.get_itemIDs_from_tags-564"><a href="#TagDB.get_itemIDs_from_tags-564"><span class="linenos">564</span></a>            <span class="c1">#     filteredItemIDsSet = setOfAllInternalItemIDsForThisSetOfTags &amp; self.tagsNumPerItemID[tagQnt]</span>
</span><span id="TagDB.get_itemIDs_from_tags-565"><a href="#TagDB.get_itemIDs_from_tags-565"><span class="linenos">565</span></a>            <span class="c1">#</span>
</span><span id="TagDB.get_itemIDs_from_tags-566"><a href="#TagDB.get_itemIDs_from_tags-566"><span class="linenos">566</span></a>            <span class="c1"># resultItemIDSet = set()</span>
</span><span id="TagDB.get_itemIDs_from_tags-567"><a href="#TagDB.get_itemIDs_from_tags-567"><span class="linenos">567</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="TagDB.get_itemIDs_from_tags-568"><a href="#TagDB.get_itemIDs_from_tags-568"><span class="linenos">568</span></a>            <span class="c1"># for binTag in binTags:</span>
</span><span id="TagDB.get_itemIDs_from_tags-569"><a href="#TagDB.get_itemIDs_from_tags-569"><span class="linenos">569</span></a>            <span class="c1">#     tagHashSet.add(binTag.__hash__())</span>
</span><span id="TagDB.get_itemIDs_from_tags-570"><a href="#TagDB.get_itemIDs_from_tags-570"><span class="linenos">570</span></a>            <span class="c1"># for itemID in filteredItemIDsSet:</span>
</span><span id="TagDB.get_itemIDs_from_tags-571"><a href="#TagDB.get_itemIDs_from_tags-571"><span class="linenos">571</span></a>            <span class="c1">#     commonTagTupleHash = self.itemWithTags[itemID]</span>
</span><span id="TagDB.get_itemIDs_from_tags-572"><a href="#TagDB.get_itemIDs_from_tags-572"><span class="linenos">572</span></a>            <span class="c1">#     tagSet = set(self.commonTagSets[commonTagTupleHash])</span>
</span><span id="TagDB.get_itemIDs_from_tags-573"><a href="#TagDB.get_itemIDs_from_tags-573"><span class="linenos">573</span></a>            <span class="c1">#     if tagSet == tagHashSet:</span>
</span><span id="TagDB.get_itemIDs_from_tags-574"><a href="#TagDB.get_itemIDs_from_tags-574"><span class="linenos">574</span></a>            <span class="c1">#         # _TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]</span>
</span><span id="TagDB.get_itemIDs_from_tags-575"><a href="#TagDB.get_itemIDs_from_tags-575"><span class="linenos">575</span></a>            <span class="c1">#         # где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}</span>
</span><span id="TagDB.get_itemIDs_from_tags-576"><a href="#TagDB.get_itemIDs_from_tags-576"><span class="linenos">576</span></a>            <span class="c1">#         # _TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ...</span>
</span><span id="TagDB.get_itemIDs_from_tags-577"><a href="#TagDB.get_itemIDs_from_tags-577"><span class="linenos">577</span></a>            <span class="c1">#         # , itemID_3}]</span>
</span><span id="TagDB.get_itemIDs_from_tags-578"><a href="#TagDB.get_itemIDs_from_tags-578"><span class="linenos">578</span></a>            <span class="c1">#         resultItemIDSet.add(itemID)</span>
</span><span id="TagDB.get_itemIDs_from_tags-579"><a href="#TagDB.get_itemIDs_from_tags-579"><span class="linenos">579</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-580"><a href="#TagDB.get_itemIDs_from_tags-580"><span class="linenos">580</span></a>            <span class="c1"># already implemented (see bellow). Don&#39;t touch this code!</span>
</span><span id="TagDB.get_itemIDs_from_tags-581"><a href="#TagDB.get_itemIDs_from_tags-581"><span class="linenos">581</span></a>            <span class="k">pass</span>
</span><span id="TagDB.get_itemIDs_from_tags-582"><a href="#TagDB.get_itemIDs_from_tags-582"><span class="linenos">582</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-583"><a href="#TagDB.get_itemIDs_from_tags-583"><span class="linenos">583</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="TagDB.get_itemIDs_from_tags-584"><a href="#TagDB.get_itemIDs_from_tags-584"><span class="linenos">584</span></a>
</span><span id="TagDB.get_itemIDs_from_tags-585"><a href="#TagDB.get_itemIDs_from_tags-585"><span class="linenos">585</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-586"><a href="#TagDB.get_itemIDs_from_tags-586"><span class="linenos">586</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">setOfAllInternalItemIDsForThisSetOfTags</span><span class="p">))</span>
</span><span id="TagDB.get_itemIDs_from_tags-587"><a href="#TagDB.get_itemIDs_from_tags-587"><span class="linenos">587</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB.get_itemIDs_from_tags-588"><a href="#TagDB.get_itemIDs_from_tags-588"><span class="linenos">588</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_itemIDs_from_tags-589"><a href="#TagDB.get_itemIDs_from_tags-589"><span class="linenos">589</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">resultItemIDSet</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_items_from_tags" class="classattr">
                                        <input id="TagDB.get_items_from_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_items_from_tags</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">binTags</span>,</span><span class="param">	<span class="n">treeType</span><span class="o">=</span><span class="mi">3</span>,</span><span class="param">	<span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_items_from_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_items_from_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_items_from_tags-591"><a href="#TagDB.get_items_from_tags-591"><span class="linenos">591</span></a>    <span class="k">def</span> <span class="nf">get_items_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB.get_items_from_tags-592"><a href="#TagDB.get_items_from_tags-592"><span class="linenos">592</span></a>                            <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB.get_items_from_tags-593"><a href="#TagDB.get_items_from_tags-593"><span class="linenos">593</span></a>        <span class="c1"># treeType - type of the graph tree representation: show all tags with replies (pure representation);</span>
</span><span id="TagDB.get_items_from_tags-594"><a href="#TagDB.get_items_from_tags-594"><span class="linenos">594</span></a>        <span class="c1"># show only relevant tags; etc.</span>
</span><span id="TagDB.get_items_from_tags-595"><a href="#TagDB.get_items_from_tags-595"><span class="linenos">595</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB.get_items_from_tags-596"><a href="#TagDB.get_items_from_tags-596"><span class="linenos">596</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.get_items_from_tags-597"><a href="#TagDB.get_items_from_tags-597"><span class="linenos">597</span></a>
</span><span id="TagDB.get_items_from_tags-598"><a href="#TagDB.get_items_from_tags-598"><span class="linenos">598</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_items_from_tags-599"><a href="#TagDB.get_items_from_tags-599"><span class="linenos">599</span></a>        <span class="n">itemIDsSet</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB.get_items_from_tags-600"><a href="#TagDB.get_items_from_tags-600"><span class="linenos">600</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="TagDB.get_items_from_tags-601"><a href="#TagDB.get_items_from_tags-601"><span class="linenos">601</span></a>                                                <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="TagDB.get_items_from_tags-602"><a href="#TagDB.get_items_from_tags-602"><span class="linenos">602</span></a>        <span class="k">if</span> <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">:</span>
</span><span id="TagDB.get_items_from_tags-603"><a href="#TagDB.get_items_from_tags-603"><span class="linenos">603</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_items_from_tags-604"><a href="#TagDB.get_items_from_tags-604"><span class="linenos">604</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="TagDB.get_items_from_tags-605"><a href="#TagDB.get_items_from_tags-605"><span class="linenos">605</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_items_from_tags-606"><a href="#TagDB.get_items_from_tags-606"><span class="linenos">606</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="TagDB.get_items_from_tags-607"><a href="#TagDB.get_items_from_tags-607"><span class="linenos">607</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemIDsSet</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>  <span class="c1"># result == (usual items set, additional set of all</span>
</span><span id="TagDB.get_items_from_tags-608"><a href="#TagDB.get_items_from_tags-608"><span class="linenos">608</span></a>                <span class="c1"># internal itemIDs)</span>
</span><span id="TagDB.get_items_from_tags-609"><a href="#TagDB.get_items_from_tags-609"><span class="linenos">609</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB.get_items_from_tags-610"><a href="#TagDB.get_items_from_tags-610"><span class="linenos">610</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_items_from_tags-611"><a href="#TagDB.get_items_from_tags-611"><span class="linenos">611</span></a>            <span class="n">itemSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_items_from_tags-612"><a href="#TagDB.get_items_from_tags-612"><span class="linenos">612</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">itemIDsSet</span><span class="p">:</span>
</span><span id="TagDB.get_items_from_tags-613"><a href="#TagDB.get_items_from_tags-613"><span class="linenos">613</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_items_from_tags-614"><a href="#TagDB.get_items_from_tags-614"><span class="linenos">614</span></a>                <span class="n">itemSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemsSet</span><span class="p">[</span><span class="n">itemID</span><span class="p">])</span>
</span><span id="TagDB.get_items_from_tags-615"><a href="#TagDB.get_items_from_tags-615"><span class="linenos">615</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">itemSet</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_tagHashes_from_tags" class="classattr">
                                        <input id="TagDB.get_tagHashes_from_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tagHashes_from_tags</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">binTags</span>,</span><span class="param">	<span class="n">treeType</span><span class="o">=</span><span class="mi">3</span>,</span><span class="param">	<span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_tagHashes_from_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_tagHashes_from_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_tagHashes_from_tags-617"><a href="#TagDB.get_tagHashes_from_tags-617"><span class="linenos">617</span></a>    <span class="k">def</span> <span class="nf">get_tagHashes_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB.get_tagHashes_from_tags-618"><a href="#TagDB.get_tagHashes_from_tags-618"><span class="linenos">618</span></a>                                <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB.get_tagHashes_from_tags-619"><a href="#TagDB.get_tagHashes_from_tags-619"><span class="linenos">619</span></a>        <span class="c1"># where &quot;itemIDsSet&quot; is externally given &quot;get_itemIDs_from_tags(binTags, treeType=PLAIN_PSEUDO_TREE_TYPE)&quot;</span>
</span><span id="TagDB.get_tagHashes_from_tags-620"><a href="#TagDB.get_tagHashes_from_tags-620"><span class="linenos">620</span></a>        <span class="c1"># so &quot;itemIDsSet&quot; is a set of the all items inside the &quot;folder&quot; binTags (including items from &quot;subfolders&quot;)</span>
</span><span id="TagDB.get_tagHashes_from_tags-621"><a href="#TagDB.get_tagHashes_from_tags-621"><span class="linenos">621</span></a>        <span class="c1"># treeType - the same as in the &quot;get_items_from_tags()&quot; method</span>
</span><span id="TagDB.get_tagHashes_from_tags-622"><a href="#TagDB.get_tagHashes_from_tags-622"><span class="linenos">622</span></a>        <span class="c1"># return set of itemIDs</span>
</span><span id="TagDB.get_tagHashes_from_tags-623"><a href="#TagDB.get_tagHashes_from_tags-623"><span class="linenos">623</span></a>        <span class="c1"># prePreparedSetOfAllInternalItemIDsForThisSetOfTags can be generated by:</span>
</span><span id="TagDB.get_tagHashes_from_tags-624"><a href="#TagDB.get_tagHashes_from_tags-624"><span class="linenos">624</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE)</span>
</span><span id="TagDB.get_tagHashes_from_tags-625"><a href="#TagDB.get_tagHashes_from_tags-625"><span class="linenos">625</span></a>        <span class="c1">#   a) get_itemIDs_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="TagDB.get_tagHashes_from_tags-626"><a href="#TagDB.get_tagHashes_from_tags-626"><span class="linenos">626</span></a>        <span class="c1">#   c) get_items_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)</span>
</span><span id="TagDB.get_tagHashes_from_tags-627"><a href="#TagDB.get_tagHashes_from_tags-627"><span class="linenos">627</span></a>        <span class="c1">#   d) get_items_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE) || BUT: it&#39;ll return item set - not itemID</span>
</span><span id="TagDB.get_tagHashes_from_tags-628"><a href="#TagDB.get_tagHashes_from_tags-628"><span class="linenos">628</span></a>        <span class="c1">#       set</span>
</span><span id="TagDB.get_tagHashes_from_tags-629"><a href="#TagDB.get_tagHashes_from_tags-629"><span class="linenos">629</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.get_tagHashes_from_tags-630"><a href="#TagDB.get_tagHashes_from_tags-630"><span class="linenos">630</span></a>
</span><span id="TagDB.get_tagHashes_from_tags-631"><a href="#TagDB.get_tagHashes_from_tags-631"><span class="linenos">631</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_tagHashes_from_tags-632"><a href="#TagDB.get_tagHashes_from_tags-632"><span class="linenos">632</span></a>
</span><span id="TagDB.get_tagHashes_from_tags-633"><a href="#TagDB.get_tagHashes_from_tags-633"><span class="linenos">633</span></a>        <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-634"><a href="#TagDB.get_tagHashes_from_tags-634"><span class="linenos">634</span></a>
</span><span id="TagDB.get_tagHashes_from_tags-635"><a href="#TagDB.get_tagHashes_from_tags-635"><span class="linenos">635</span></a>        <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-636"><a href="#TagDB.get_tagHashes_from_tags-636"><span class="linenos">636</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-637"><a href="#TagDB.get_tagHashes_from_tags-637"><span class="linenos">637</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB.get_tagHashes_from_tags-638"><a href="#TagDB.get_tagHashes_from_tags-638"><span class="linenos">638</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-639"><a href="#TagDB.get_tagHashes_from_tags-639"><span class="linenos">639</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span>
</span><span id="TagDB.get_tagHashes_from_tags-640"><a href="#TagDB.get_tagHashes_from_tags-640"><span class="linenos">640</span></a>
</span><span id="TagDB.get_tagHashes_from_tags-641"><a href="#TagDB.get_tagHashes_from_tags-641"><span class="linenos">641</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">treeType</span> <span class="o">==</span> <span class="n">FULL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB.get_tagHashes_from_tags-642"><a href="#TagDB.get_tagHashes_from_tags-642"><span class="linenos">642</span></a>            <span class="n">binTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-643"><a href="#TagDB.get_tagHashes_from_tags-643"><span class="linenos">643</span></a>            <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-644"><a href="#TagDB.get_tagHashes_from_tags-644"><span class="linenos">644</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-645"><a href="#TagDB.get_tagHashes_from_tags-645"><span class="linenos">645</span></a>                <span class="n">binTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.get_tagHashes_from_tags-646"><a href="#TagDB.get_tagHashes_from_tags-646"><span class="linenos">646</span></a>            <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-647"><a href="#TagDB.get_tagHashes_from_tags-647"><span class="linenos">647</span></a>            <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-648"><a href="#TagDB.get_tagHashes_from_tags-648"><span class="linenos">648</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-649"><a href="#TagDB.get_tagHashes_from_tags-649"><span class="linenos">649</span></a>                <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-650"><a href="#TagDB.get_tagHashes_from_tags-650"><span class="linenos">650</span></a>                    <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.get_tagHashes_from_tags-651"><a href="#TagDB.get_tagHashes_from_tags-651"><span class="linenos">651</span></a>                    <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.get_tagHashes_from_tags-652"><a href="#TagDB.get_tagHashes_from_tags-652"><span class="linenos">652</span></a>                    <span class="n">tagHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB.get_tagHashes_from_tags-653"><a href="#TagDB.get_tagHashes_from_tags-653"><span class="linenos">653</span></a>            <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">tagHashSet</span> <span class="o">-</span> <span class="n">binTagHashes</span>
</span><span id="TagDB.get_tagHashes_from_tags-654"><a href="#TagDB.get_tagHashes_from_tags-654"><span class="linenos">654</span></a>        <span class="k">elif</span> <span class="n">treeType</span> <span class="o">==</span> <span class="n">SMART_TREE_TYPE</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-655"><a href="#TagDB.get_tagHashes_from_tags-655"><span class="linenos">655</span></a>            <span class="c1"># smartTree = self.build_smart_tree(binTags, prePreparedSetOfAllInternalItemIDs=setOfAllInternalItemIDs)</span>
</span><span id="TagDB.get_tagHashes_from_tags-656"><a href="#TagDB.get_tagHashes_from_tags-656"><span class="linenos">656</span></a>            <span class="n">smartTree</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">build_smart_tree</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="n">setOfAllInternalItemIDs</span><span class="p">,</span>
</span><span id="TagDB.get_tagHashes_from_tags-657"><a href="#TagDB.get_tagHashes_from_tags-657"><span class="linenos">657</span></a>                                              <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB.get_tagHashes_from_tags-658"><a href="#TagDB.get_tagHashes_from_tags-658"><span class="linenos">658</span></a>            <span class="k">if</span> <span class="mi">0</span> <span class="ow">in</span> <span class="n">smartTree</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-659"><a href="#TagDB.get_tagHashes_from_tags-659"><span class="linenos">659</span></a>                <span class="n">resultTagHashSet</span> <span class="o">=</span> <span class="n">smartTree</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="TagDB.get_tagHashes_from_tags-660"><a href="#TagDB.get_tagHashes_from_tags-660"><span class="linenos">660</span></a>            <span class="c1"># filteredItemIDsList = list()</span>
</span><span id="TagDB.get_tagHashes_from_tags-661"><a href="#TagDB.get_tagHashes_from_tags-661"><span class="linenos">661</span></a>            <span class="c1"># tagQnt = len(binTags)</span>
</span><span id="TagDB.get_tagHashes_from_tags-662"><a href="#TagDB.get_tagHashes_from_tags-662"><span class="linenos">662</span></a>            <span class="c1"># for itemID in listOfAllInternalItemIDs:</span>
</span><span id="TagDB.get_tagHashes_from_tags-663"><a href="#TagDB.get_tagHashes_from_tags-663"><span class="linenos">663</span></a>            <span class="c1">#     if len(self.itemWithTags[itemID]) == (tagQnt + 1):</span>
</span><span id="TagDB.get_tagHashes_from_tags-664"><a href="#TagDB.get_tagHashes_from_tags-664"><span class="linenos">664</span></a>            <span class="c1">#         filteredItemIDsList.append(itemID)</span>
</span><span id="TagDB.get_tagHashes_from_tags-665"><a href="#TagDB.get_tagHashes_from_tags-665"><span class="linenos">665</span></a>            <span class="c1">#</span>
</span><span id="TagDB.get_tagHashes_from_tags-666"><a href="#TagDB.get_tagHashes_from_tags-666"><span class="linenos">666</span></a>            <span class="c1"># tagHashSet = set()</span>
</span><span id="TagDB.get_tagHashes_from_tags-667"><a href="#TagDB.get_tagHashes_from_tags-667"><span class="linenos">667</span></a>            <span class="c1"># for itemID in filteredItemIDsList:</span>
</span><span id="TagDB.get_tagHashes_from_tags-668"><a href="#TagDB.get_tagHashes_from_tags-668"><span class="linenos">668</span></a>            <span class="c1">#     tagHashSet.update(set(self.itemWithTags[itemID]))</span>
</span><span id="TagDB.get_tagHashes_from_tags-669"><a href="#TagDB.get_tagHashes_from_tags-669"><span class="linenos">669</span></a>            <span class="c1"># givenTagHashes = set()</span>
</span><span id="TagDB.get_tagHashes_from_tags-670"><a href="#TagDB.get_tagHashes_from_tags-670"><span class="linenos">670</span></a>            <span class="c1"># for tag in binTags:</span>
</span><span id="TagDB.get_tagHashes_from_tags-671"><a href="#TagDB.get_tagHashes_from_tags-671"><span class="linenos">671</span></a>            <span class="c1">#     givenTagHashes.add(tag.__hash__())</span>
</span><span id="TagDB.get_tagHashes_from_tags-672"><a href="#TagDB.get_tagHashes_from_tags-672"><span class="linenos">672</span></a>            <span class="c1"># tagHashSet.difference_update(givenTagHashes)</span>
</span><span id="TagDB.get_tagHashes_from_tags-673"><a href="#TagDB.get_tagHashes_from_tags-673"><span class="linenos">673</span></a>            <span class="c1"># ##resultTagHashList = list(tagHashSet)</span>
</span><span id="TagDB.get_tagHashes_from_tags-674"><a href="#TagDB.get_tagHashes_from_tags-674"><span class="linenos">674</span></a>            <span class="c1"># # если остановиться тут - то мы увидим не все папки: мы не увидим папки непосредственно в которых есть</span>
</span><span id="TagDB.get_tagHashes_from_tags-675"><a href="#TagDB.get_tagHashes_from_tags-675"><span class="linenos">675</span></a>            <span class="c1"># # только другие подпапки, но ни одного файла.</span>
</span><span id="TagDB.get_tagHashes_from_tags-676"><a href="#TagDB.get_tagHashes_from_tags-676"><span class="linenos">676</span></a>            <span class="c1"># #</span>
</span><span id="TagDB.get_tagHashes_from_tags-677"><a href="#TagDB.get_tagHashes_from_tags-677"><span class="linenos">677</span></a>            <span class="c1"># # значит далее мы должны исключить все файлы, которые имеют только что найденные теги, и начать строить</span>
</span><span id="TagDB.get_tagHashes_from_tags-678"><a href="#TagDB.get_tagHashes_from_tags-678"><span class="linenos">678</span></a>            <span class="c1"># # древо тегов для оставшихся</span>
</span><span id="TagDB.get_tagHashes_from_tags-679"><a href="#TagDB.get_tagHashes_from_tags-679"><span class="linenos">679</span></a>            <span class="c1"># #</span>
</span><span id="TagDB.get_tagHashes_from_tags-680"><a href="#TagDB.get_tagHashes_from_tags-680"><span class="linenos">680</span></a>            <span class="c1"># # а далее - повторить все это в цикле, увеличив при проверке кол-во тегов еще раз на единицу (и используя</span>
</span><span id="TagDB.get_tagHashes_from_tags-681"><a href="#TagDB.get_tagHashes_from_tags-681"><span class="linenos">681</span></a>            <span class="c1"># # уже оставшийся после отсеивания набор файлов). В итоге кол-во итераций зависит не от количества файлов,</span>
</span><span id="TagDB.get_tagHashes_from_tags-682"><a href="#TagDB.get_tagHashes_from_tags-682"><span class="linenos">682</span></a>            <span class="c1"># # а от максимальной фактически имеющейся вложенности файлов внутри тегов-каталогов</span>
</span><span id="TagDB.get_tagHashes_from_tags-683"><a href="#TagDB.get_tagHashes_from_tags-683"><span class="linenos">683</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_tagHashes_from_tags-684"><a href="#TagDB.get_tagHashes_from_tags-684"><span class="linenos">684</span></a>            <span class="k">raise</span> <span class="n">UnknownTreeTypeError</span><span class="p">()</span>
</span><span id="TagDB.get_tagHashes_from_tags-685"><a href="#TagDB.get_tagHashes_from_tags-685"><span class="linenos">685</span></a>
</span><span id="TagDB.get_tagHashes_from_tags-686"><a href="#TagDB.get_tagHashes_from_tags-686"><span class="linenos">686</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">resultTagHashSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB.get_tagHashes_from_tags-687"><a href="#TagDB.get_tagHashes_from_tags-687"><span class="linenos">687</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_tags_from_tags" class="classattr">
                                        <input id="TagDB.get_tags_from_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tags_from_tags</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">binTags</span>,</span><span class="param">	<span class="n">treeType</span><span class="o">=</span><span class="mi">3</span>,</span><span class="param">	<span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_tags_from_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_tags_from_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_tags_from_tags-689"><a href="#TagDB.get_tags_from_tags-689"><span class="linenos">689</span></a>    <span class="k">def</span> <span class="nf">get_tags_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">,</span>
</span><span id="TagDB.get_tags_from_tags-690"><a href="#TagDB.get_tags_from_tags-690"><span class="linenos">690</span></a>                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TagDB.get_tags_from_tags-691"><a href="#TagDB.get_tags_from_tags-691"><span class="linenos">691</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tagHashes_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB.get_tags_from_tags-692"><a href="#TagDB.get_tags_from_tags-692"><span class="linenos">692</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span>
</span><span id="TagDB.get_tags_from_tags-693"><a href="#TagDB.get_tags_from_tags-693"><span class="linenos">693</span></a>                                              <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="p">)</span>
</span><span id="TagDB.get_tags_from_tags-694"><a href="#TagDB.get_tags_from_tags-694"><span class="linenos">694</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.build_smart_tree" class="classattr">
                                        <input id="TagDB.build_smart_tree-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">build_smart_tree</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">startingBinTags</span>,</span><span class="param">	<span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.build_smart_tree-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.build_smart_tree"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.build_smart_tree-696"><a href="#TagDB.build_smart_tree-696"><span class="linenos">696</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB.build_smart_tree-697"><a href="#TagDB.build_smart_tree-697"><span class="linenos">697</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-698"><a href="#TagDB.build_smart_tree-698"><span class="linenos">698</span></a>
</span><span id="TagDB.build_smart_tree-699"><a href="#TagDB.build_smart_tree-699"><span class="linenos">699</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-700"><a href="#TagDB.build_smart_tree-700"><span class="linenos">700</span></a>
</span><span id="TagDB.build_smart_tree-701"><a href="#TagDB.build_smart_tree-701"><span class="linenos">701</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-702"><a href="#TagDB.build_smart_tree-702"><span class="linenos">702</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.build_smart_tree-703"><a href="#TagDB.build_smart_tree-703"><span class="linenos">703</span></a>
</span><span id="TagDB.build_smart_tree-704"><a href="#TagDB.build_smart_tree-704"><span class="linenos">704</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-705"><a href="#TagDB.build_smart_tree-705"><span class="linenos">705</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-706"><a href="#TagDB.build_smart_tree-706"><span class="linenos">706</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-707"><a href="#TagDB.build_smart_tree-707"><span class="linenos">707</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.build_smart_tree-708"><a href="#TagDB.build_smart_tree-708"><span class="linenos">708</span></a>
</span><span id="TagDB.build_smart_tree-709"><a href="#TagDB.build_smart_tree-709"><span class="linenos">709</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-710"><a href="#TagDB.build_smart_tree-710"><span class="linenos">710</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-711"><a href="#TagDB.build_smart_tree-711"><span class="linenos">711</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-712"><a href="#TagDB.build_smart_tree-712"><span class="linenos">712</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="TagDB.build_smart_tree-713"><a href="#TagDB.build_smart_tree-713"><span class="linenos">713</span></a>
</span><span id="TagDB.build_smart_tree-714"><a href="#TagDB.build_smart_tree-714"><span class="linenos">714</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="TagDB.build_smart_tree-715"><a href="#TagDB.build_smart_tree-715"><span class="linenos">715</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-716"><a href="#TagDB.build_smart_tree-716"><span class="linenos">716</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-717"><a href="#TagDB.build_smart_tree-717"><span class="linenos">717</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-718"><a href="#TagDB.build_smart_tree-718"><span class="linenos">718</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-719"><a href="#TagDB.build_smart_tree-719"><span class="linenos">719</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-720"><a href="#TagDB.build_smart_tree-720"><span class="linenos">720</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree-721"><a href="#TagDB.build_smart_tree-721"><span class="linenos">721</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.build_smart_tree-722"><a href="#TagDB.build_smart_tree-722"><span class="linenos">722</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB.build_smart_tree-723"><a href="#TagDB.build_smart_tree-723"><span class="linenos">723</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB.build_smart_tree-724"><a href="#TagDB.build_smart_tree-724"><span class="linenos">724</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-725"><a href="#TagDB.build_smart_tree-725"><span class="linenos">725</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-726"><a href="#TagDB.build_smart_tree-726"><span class="linenos">726</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="TagDB.build_smart_tree-727"><a href="#TagDB.build_smart_tree-727"><span class="linenos">727</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="TagDB.build_smart_tree-728"><a href="#TagDB.build_smart_tree-728"><span class="linenos">728</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="TagDB.build_smart_tree-729"><a href="#TagDB.build_smart_tree-729"><span class="linenos">729</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-730"><a href="#TagDB.build_smart_tree-730"><span class="linenos">730</span></a>
</span><span id="TagDB.build_smart_tree-731"><a href="#TagDB.build_smart_tree-731"><span class="linenos">731</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-732"><a href="#TagDB.build_smart_tree-732"><span class="linenos">732</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-733"><a href="#TagDB.build_smart_tree-733"><span class="linenos">733</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree-734"><a href="#TagDB.build_smart_tree-734"><span class="linenos">734</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.build_smart_tree-735"><a href="#TagDB.build_smart_tree-735"><span class="linenos">735</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB.build_smart_tree-736"><a href="#TagDB.build_smart_tree-736"><span class="linenos">736</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB.build_smart_tree-737"><a href="#TagDB.build_smart_tree-737"><span class="linenos">737</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree-738"><a href="#TagDB.build_smart_tree-738"><span class="linenos">738</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-739"><a href="#TagDB.build_smart_tree-739"><span class="linenos">739</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-740"><a href="#TagDB.build_smart_tree-740"><span class="linenos">740</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-741"><a href="#TagDB.build_smart_tree-741"><span class="linenos">741</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-742"><a href="#TagDB.build_smart_tree-742"><span class="linenos">742</span></a>
</span><span id="TagDB.build_smart_tree-743"><a href="#TagDB.build_smart_tree-743"><span class="linenos">743</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree-744"><a href="#TagDB.build_smart_tree-744"><span class="linenos">744</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree-745"><a href="#TagDB.build_smart_tree-745"><span class="linenos">745</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB.build_smart_tree-746"><a href="#TagDB.build_smart_tree-746"><span class="linenos">746</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-747"><a href="#TagDB.build_smart_tree-747"><span class="linenos">747</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree-748"><a href="#TagDB.build_smart_tree-748"><span class="linenos">748</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="TagDB.build_smart_tree-749"><a href="#TagDB.build_smart_tree-749"><span class="linenos">749</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree-750"><a href="#TagDB.build_smart_tree-750"><span class="linenos">750</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="TagDB.build_smart_tree-751"><a href="#TagDB.build_smart_tree-751"><span class="linenos">751</span></a>                    <span class="k">pass</span>
</span><span id="TagDB.build_smart_tree-752"><a href="#TagDB.build_smart_tree-752"><span class="linenos">752</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree-753"><a href="#TagDB.build_smart_tree-753"><span class="linenos">753</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB.build_smart_tree-754"><a href="#TagDB.build_smart_tree-754"><span class="linenos">754</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree-755"><a href="#TagDB.build_smart_tree-755"><span class="linenos">755</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree-756"><a href="#TagDB.build_smart_tree-756"><span class="linenos">756</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="TagDB.build_smart_tree-757"><a href="#TagDB.build_smart_tree-757"><span class="linenos">757</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="TagDB.build_smart_tree-758"><a href="#TagDB.build_smart_tree-758"><span class="linenos">758</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="TagDB.build_smart_tree-759"><a href="#TagDB.build_smart_tree-759"><span class="linenos">759</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="TagDB.build_smart_tree-760"><a href="#TagDB.build_smart_tree-760"><span class="linenos">760</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="TagDB.build_smart_tree-761"><a href="#TagDB.build_smart_tree-761"><span class="linenos">761</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="TagDB.build_smart_tree-762"><a href="#TagDB.build_smart_tree-762"><span class="linenos">762</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree-763"><a href="#TagDB.build_smart_tree-763"><span class="linenos">763</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="TagDB.build_smart_tree-764"><a href="#TagDB.build_smart_tree-764"><span class="linenos">764</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="TagDB.build_smart_tree-765"><a href="#TagDB.build_smart_tree-765"><span class="linenos">765</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.build_smart_tree_2" class="classattr">
                                        <input id="TagDB.build_smart_tree_2-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">build_smart_tree_2</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">startingBinTags</span>,</span><span class="param">	<span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.build_smart_tree_2-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.build_smart_tree_2"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.build_smart_tree_2-767"><a href="#TagDB.build_smart_tree_2-767"><span class="linenos">767</span></a>    <span class="k">def</span> <span class="nf">build_smart_tree_2</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingBinTags</span><span class="p">,</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">zeroSliceOnly</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="TagDB.build_smart_tree_2-768"><a href="#TagDB.build_smart_tree_2-768"><span class="linenos">768</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-769"><a href="#TagDB.build_smart_tree_2-769"><span class="linenos">769</span></a>
</span><span id="TagDB.build_smart_tree_2-770"><a href="#TagDB.build_smart_tree_2-770"><span class="linenos">770</span></a>        <span class="n">startingBinTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-771"><a href="#TagDB.build_smart_tree_2-771"><span class="linenos">771</span></a>
</span><span id="TagDB.build_smart_tree_2-772"><a href="#TagDB.build_smart_tree_2-772"><span class="linenos">772</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-773"><a href="#TagDB.build_smart_tree_2-773"><span class="linenos">773</span></a>            <span class="n">startingBinTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.build_smart_tree_2-774"><a href="#TagDB.build_smart_tree_2-774"><span class="linenos">774</span></a>
</span><span id="TagDB.build_smart_tree_2-775"><a href="#TagDB.build_smart_tree_2-775"><span class="linenos">775</span></a>        <span class="n">startingTagHashes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-776"><a href="#TagDB.build_smart_tree_2-776"><span class="linenos">776</span></a>        <span class="k">for</span> <span class="n">tag</span> <span class="ow">in</span> <span class="n">startingBinTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-777"><a href="#TagDB.build_smart_tree_2-777"><span class="linenos">777</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-778"><a href="#TagDB.build_smart_tree_2-778"><span class="linenos">778</span></a>            <span class="n">startingTagHashes</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.build_smart_tree_2-779"><a href="#TagDB.build_smart_tree_2-779"><span class="linenos">779</span></a>
</span><span id="TagDB.build_smart_tree_2-780"><a href="#TagDB.build_smart_tree_2-780"><span class="linenos">780</span></a>        <span class="k">if</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-781"><a href="#TagDB.build_smart_tree_2-781"><span class="linenos">781</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_itemIDs_from_tags</span><span class="p">(</span><span class="n">startingBinTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">PLAIN_PSEUDO_TREE_TYPE</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-782"><a href="#TagDB.build_smart_tree_2-782"><span class="linenos">782</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-783"><a href="#TagDB.build_smart_tree_2-783"><span class="linenos">783</span></a>            <span class="n">setOfAllInternalItemIDs</span> <span class="o">=</span> <span class="n">prePreparedSetOfAllInternalItemIDs</span>
</span><span id="TagDB.build_smart_tree_2-784"><a href="#TagDB.build_smart_tree_2-784"><span class="linenos">784</span></a>
</span><span id="TagDB.build_smart_tree_2-785"><a href="#TagDB.build_smart_tree_2-785"><span class="linenos">785</span></a>        <span class="n">smartTree</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="nb">set</span><span class="p">()}</span>
</span><span id="TagDB.build_smart_tree_2-786"><a href="#TagDB.build_smart_tree_2-786"><span class="linenos">786</span></a>        <span class="n">smartTree__filler</span> <span class="o">=</span> <span class="n">AddToCompoundDict__Set</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-787"><a href="#TagDB.build_smart_tree_2-787"><span class="linenos">787</span></a>        <span class="n">local_tags_qnt</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-788"><a href="#TagDB.build_smart_tree_2-788"><span class="linenos">788</span></a>        <span class="n">local_tags_qnt__filler</span> <span class="o">=</span> <span class="n">KeyCounter</span><span class="p">(</span><span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-789"><a href="#TagDB.build_smart_tree_2-789"><span class="linenos">789</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-790"><a href="#TagDB.build_smart_tree_2-790"><span class="linenos">790</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-791"><a href="#TagDB.build_smart_tree_2-791"><span class="linenos">791</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree_2-792"><a href="#TagDB.build_smart_tree_2-792"><span class="linenos">792</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.build_smart_tree_2-793"><a href="#TagDB.build_smart_tree_2-793"><span class="linenos">793</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB.build_smart_tree_2-794"><a href="#TagDB.build_smart_tree_2-794"><span class="linenos">794</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB.build_smart_tree_2-795"><a href="#TagDB.build_smart_tree_2-795"><span class="linenos">795</span></a>            <span class="k">for</span> <span class="n">tag_hash</span> <span class="ow">in</span> <span class="n">setOfTags</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-796"><a href="#TagDB.build_smart_tree_2-796"><span class="linenos">796</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-797"><a href="#TagDB.build_smart_tree_2-797"><span class="linenos">797</span></a>                <span class="c1"># if tag_hash not in local_tags_qnt:</span>
</span><span id="TagDB.build_smart_tree_2-798"><a href="#TagDB.build_smart_tree_2-798"><span class="linenos">798</span></a>                <span class="c1">#     local_tags_qnt[tag_hash] = 0</span>
</span><span id="TagDB.build_smart_tree_2-799"><a href="#TagDB.build_smart_tree_2-799"><span class="linenos">799</span></a>                <span class="c1"># local_tags_qnt[tag_hash] += 1</span>
</span><span id="TagDB.build_smart_tree_2-800"><a href="#TagDB.build_smart_tree_2-800"><span class="linenos">800</span></a>                <span class="n">local_tags_qnt__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">tag_hash</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-801"><a href="#TagDB.build_smart_tree_2-801"><span class="linenos">801</span></a>
</span><span id="TagDB.build_smart_tree_2-802"><a href="#TagDB.build_smart_tree_2-802"><span class="linenos">802</span></a>        <span class="k">for</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="n">setOfAllInternalItemIDs</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-803"><a href="#TagDB.build_smart_tree_2-803"><span class="linenos">803</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-804"><a href="#TagDB.build_smart_tree_2-804"><span class="linenos">804</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree_2-805"><a href="#TagDB.build_smart_tree_2-805"><span class="linenos">805</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.build_smart_tree_2-806"><a href="#TagDB.build_smart_tree_2-806"><span class="linenos">806</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">tagSet</span>
</span><span id="TagDB.build_smart_tree_2-807"><a href="#TagDB.build_smart_tree_2-807"><span class="linenos">807</span></a>            <span class="n">setOfTags</span> <span class="o">=</span> <span class="n">setOfTags</span> <span class="o">-</span> <span class="n">startingTagHashes</span>
</span><span id="TagDB.build_smart_tree_2-808"><a href="#TagDB.build_smart_tree_2-808"><span class="linenos">808</span></a>            <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree_2-809"><a href="#TagDB.build_smart_tree_2-809"><span class="linenos">809</span></a>            <span class="k">if</span> <span class="n">zeroSliceOnly</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-810"><a href="#TagDB.build_smart_tree_2-810"><span class="linenos">810</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_top_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">,</span> <span class="n">local_tags_qnt</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-811"><a href="#TagDB.build_smart_tree_2-811"><span class="linenos">811</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-812"><a href="#TagDB.build_smart_tree_2-812"><span class="linenos">812</span></a>                <span class="n">listOfTagHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTags</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-813"><a href="#TagDB.build_smart_tree_2-813"><span class="linenos">813</span></a>
</span><span id="TagDB.build_smart_tree_2-814"><a href="#TagDB.build_smart_tree_2-814"><span class="linenos">814</span></a>            <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree_2-815"><a href="#TagDB.build_smart_tree_2-815"><span class="linenos">815</span></a>            <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree_2-816"><a href="#TagDB.build_smart_tree_2-816"><span class="linenos">816</span></a>            <span class="n">treeLevel</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TagDB.build_smart_tree_2-817"><a href="#TagDB.build_smart_tree_2-817"><span class="linenos">817</span></a>            <span class="k">for</span> <span class="n">tagHash</span> <span class="ow">in</span> <span class="n">listOfTagHashes</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-818"><a href="#TagDB.build_smart_tree_2-818"><span class="linenos">818</span></a>                <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.build_smart_tree_2-819"><a href="#TagDB.build_smart_tree_2-819"><span class="linenos">819</span></a>                <span class="c1"># currentTagHashQnt = self.tagsQnt[tagHash]</span>
</span><span id="TagDB.build_smart_tree_2-820"><a href="#TagDB.build_smart_tree_2-820"><span class="linenos">820</span></a>                <span class="n">currentTagHashQnt</span> <span class="o">=</span> <span class="n">local_tags_qnt</span><span class="p">[</span><span class="n">tagHash</span><span class="p">]</span>
</span><span id="TagDB.build_smart_tree_2-821"><a href="#TagDB.build_smart_tree_2-821"><span class="linenos">821</span></a>                <span class="k">if</span> <span class="p">(</span><span class="n">lastTagHash</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">currentTagHashQnt</span> <span class="o">==</span> <span class="n">lastTagHashQnt</span><span class="p">):</span>
</span><span id="TagDB.build_smart_tree_2-822"><a href="#TagDB.build_smart_tree_2-822"><span class="linenos">822</span></a>                    <span class="k">pass</span>
</span><span id="TagDB.build_smart_tree_2-823"><a href="#TagDB.build_smart_tree_2-823"><span class="linenos">823</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.build_smart_tree_2-824"><a href="#TagDB.build_smart_tree_2-824"><span class="linenos">824</span></a>                    <span class="n">treeLevel</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TagDB.build_smart_tree_2-825"><a href="#TagDB.build_smart_tree_2-825"><span class="linenos">825</span></a>                    <span class="n">lastTagHash</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree_2-826"><a href="#TagDB.build_smart_tree_2-826"><span class="linenos">826</span></a>                    <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.build_smart_tree_2-827"><a href="#TagDB.build_smart_tree_2-827"><span class="linenos">827</span></a>                <span class="c1"># if treeLevel not in smartTree:</span>
</span><span id="TagDB.build_smart_tree_2-828"><a href="#TagDB.build_smart_tree_2-828"><span class="linenos">828</span></a>                <span class="c1">#     smartTree[treeLevel] = set()</span>
</span><span id="TagDB.build_smart_tree_2-829"><a href="#TagDB.build_smart_tree_2-829"><span class="linenos">829</span></a>                <span class="c1"># # tagsSetOnTheLevel = smartTree[treeLevel]</span>
</span><span id="TagDB.build_smart_tree_2-830"><a href="#TagDB.build_smart_tree_2-830"><span class="linenos">830</span></a>                <span class="c1"># # tagsSetOnTheLevel.add(tagHash)</span>
</span><span id="TagDB.build_smart_tree_2-831"><a href="#TagDB.build_smart_tree_2-831"><span class="linenos">831</span></a>                <span class="c1"># # smartTree[treeLevel] = tagsSetOnTheLevel</span>
</span><span id="TagDB.build_smart_tree_2-832"><a href="#TagDB.build_smart_tree_2-832"><span class="linenos">832</span></a>                <span class="c1"># smartTree[treeLevel].add(tagHash)</span>
</span><span id="TagDB.build_smart_tree_2-833"><a href="#TagDB.build_smart_tree_2-833"><span class="linenos">833</span></a>                <span class="n">smartTree__filler</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">treeLevel</span><span class="p">,</span> <span class="n">tagHash</span><span class="p">)</span>
</span><span id="TagDB.build_smart_tree_2-834"><a href="#TagDB.build_smart_tree_2-834"><span class="linenos">834</span></a>                <span class="n">lastTagHash</span> <span class="o">=</span> <span class="n">tagHash</span>
</span><span id="TagDB.build_smart_tree_2-835"><a href="#TagDB.build_smart_tree_2-835"><span class="linenos">835</span></a>                <span class="n">lastTagHashQnt</span> <span class="o">=</span> <span class="n">currentTagHashQnt</span>
</span><span id="TagDB.build_smart_tree_2-836"><a href="#TagDB.build_smart_tree_2-836"><span class="linenos">836</span></a>        <span class="k">return</span> <span class="nb">dict</span><span class="p">(</span><span class="n">smartTree</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_all_from_tags" class="classattr">
                                        <input id="TagDB.get_all_from_tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_all_from_tags</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span>, </span><span class="param"><span class="n">treeType</span><span class="o">=</span><span class="mi">3</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_all_from_tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_all_from_tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_all_from_tags-838"><a href="#TagDB.get_all_from_tags-838"><span class="linenos">838</span></a>    <span class="k">def</span> <span class="nf">get_all_from_tags</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">USUAL_TREE_TYPE</span><span class="p">):</span>
</span><span id="TagDB.get_all_from_tags-839"><a href="#TagDB.get_all_from_tags-839"><span class="linenos">839</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_all_from_tags-840"><a href="#TagDB.get_all_from_tags-840"><span class="linenos">840</span></a>        <span class="n">items</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_items_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB.get_all_from_tags-841"><a href="#TagDB.get_all_from_tags-841"><span class="linenos">841</span></a>                                         <span class="n">isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="TagDB.get_all_from_tags-842"><a href="#TagDB.get_all_from_tags-842"><span class="linenos">842</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TagDB.get_all_from_tags-843"><a href="#TagDB.get_all_from_tags-843"><span class="linenos">843</span></a>            <span class="n">tags</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_tags_from_tags</span><span class="p">(</span><span class="n">binTags</span><span class="p">,</span> <span class="n">treeType</span><span class="o">=</span><span class="n">treeType</span><span class="p">,</span>
</span><span id="TagDB.get_all_from_tags-844"><a href="#TagDB.get_all_from_tags-844"><span class="linenos">844</span></a>                                           <span class="n">prePreparedSetOfAllInternalItemIDsForThisSetOfTags</span><span class="o">=</span><span class="n">items</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="TagDB.get_all_from_tags-845"><a href="#TagDB.get_all_from_tags-845"><span class="linenos">845</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">tags</span><span class="p">),</span> <span class="nb">set</span><span class="p">(</span><span class="n">items</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="TagDB.get_all_from_tags-846"><a href="#TagDB.get_all_from_tags-846"><span class="linenos">846</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="TagDB.get_all_from_tags-847"><a href="#TagDB.get_all_from_tags-847"><span class="linenos">847</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_all_from_tags-848"><a href="#TagDB.get_all_from_tags-848"><span class="linenos">848</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">(),</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="TagDB.get_all_from_tags-849"><a href="#TagDB.get_all_from_tags-849"><span class="linenos">849</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_tagsHashes_from_single_item" class="classattr">
                                        <input id="TagDB.get_tagsHashes_from_single_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tagsHashes_from_single_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">itemID</span>, </span><span class="param"><span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_tagsHashes_from_single_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_tagsHashes_from_single_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_tagsHashes_from_single_item-851"><a href="#TagDB.get_tagsHashes_from_single_item-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">get_tagsHashes_from_single_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">itemID</span><span class="p">,</span> <span class="n">isWithoutRootHash</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-852"><a href="#TagDB.get_tagsHashes_from_single_item-852"><span class="linenos">852</span></a>        <span class="k">if</span> <span class="n">itemID</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">:</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-853"><a href="#TagDB.get_tagsHashes_from_single_item-853"><span class="linenos">853</span></a>            <span class="n">commonTagTupleHash</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemWithTags</span><span class="p">[</span><span class="n">itemID</span><span class="p">]</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-854"><a href="#TagDB.get_tagsHashes_from_single_item-854"><span class="linenos">854</span></a>            <span class="n">tagSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagTupleHash</span><span class="p">])</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-855"><a href="#TagDB.get_tagsHashes_from_single_item-855"><span class="linenos">855</span></a>            <span class="k">if</span> <span class="n">isWithoutRootHash</span><span class="p">:</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-856"><a href="#TagDB.get_tagsHashes_from_single_item-856"><span class="linenos">856</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-857"><a href="#TagDB.get_tagsHashes_from_single_item-857"><span class="linenos">857</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-858"><a href="#TagDB.get_tagsHashes_from_single_item-858"><span class="linenos">858</span></a>                <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="n">tagSet</span><span class="p">)</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-859"><a href="#TagDB.get_tagsHashes_from_single_item-859"><span class="linenos">859</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_tagsHashes_from_single_item-860"><a href="#TagDB.get_tagsHashes_from_single_item-860"><span class="linenos">860</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_potential_itemIDs_from_item" class="classattr">
                                        <input id="TagDB.get_potential_itemIDs_from_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_potential_itemIDs_from_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binItem</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_potential_itemIDs_from_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_potential_itemIDs_from_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_potential_itemIDs_from_item-862"><a href="#TagDB.get_potential_itemIDs_from_item-862"><span class="linenos">862</span></a>    <span class="k">def</span> <span class="nf">get_potential_itemIDs_from_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binItem</span><span class="p">):</span>
</span><span id="TagDB.get_potential_itemIDs_from_item-863"><a href="#TagDB.get_potential_itemIDs_from_item-863"><span class="linenos">863</span></a>        <span class="n">itemHash</span> <span class="o">=</span> <span class="n">binItem</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()</span>
</span><span id="TagDB.get_potential_itemIDs_from_item-864"><a href="#TagDB.get_potential_itemIDs_from_item-864"><span class="linenos">864</span></a>        <span class="k">if</span> <span class="n">itemHash</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">:</span>
</span><span id="TagDB.get_potential_itemIDs_from_item-865"><a href="#TagDB.get_potential_itemIDs_from_item-865"><span class="linenos">865</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">itemIDsForItem</span><span class="p">[</span><span class="n">itemHash</span><span class="p">])</span>
</span><span id="TagDB.get_potential_itemIDs_from_item-866"><a href="#TagDB.get_potential_itemIDs_from_item-866"><span class="linenos">866</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.get_potential_itemIDs_from_item-867"><a href="#TagDB.get_potential_itemIDs_from_item-867"><span class="linenos">867</span></a>            <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed" class="classattr">
                                        <input id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-869"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-869"><span class="linenos">869</span></a>    <span class="k">def</span> <span class="nf">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-870"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-870"><span class="linenos">870</span></a>        <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-871"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-871"><span class="linenos">871</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-872"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-872"><span class="linenos">872</span></a>        <span class="n">binTags</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-873"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-873"><span class="linenos">873</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-874"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-874"><span class="linenos">874</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-875"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-875"><span class="linenos">875</span></a>            <span class="n">binTags</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">())</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-876"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-876"><span class="linenos">876</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-877"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-877"><span class="linenos">877</span></a>        <span class="n">tagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-878"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-878"><span class="linenos">878</span></a>        <span class="k">for</span> <span class="n">binTag</span> <span class="ow">in</span> <span class="n">binTags</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-879"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-879"><span class="linenos">879</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-880"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-880"><span class="linenos">880</span></a>            <span class="n">tagHashSet</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">binTag</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">())</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-881"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-881"><span class="linenos">881</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-882"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-882"><span class="linenos">882</span></a>        <span class="n">binTagsQnt</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-883"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-883"><span class="linenos">883</span></a>        <span class="n">commonTagGroupHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-884"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-884"><span class="linenos">884</span></a>        <span class="c1"># setOfLenOfTheCommonTagHashSetForChecking = set()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-885"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-885"><span class="linenos">885</span></a>        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-886"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-886"><span class="linenos">886</span></a>        <span class="k">for</span> <span class="n">commonTagQnt</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">setOfTagGroupQnt</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-887"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-887"><span class="linenos">887</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-888"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-888"><span class="linenos">888</span></a>            <span class="k">if</span> <span class="n">commonTagQnt</span> <span class="o">&gt;</span> <span class="n">binTagsQnt</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-889"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-889"><span class="linenos">889</span></a>                <span class="n">setOfTheCommonTagGroupHashes</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tagsQntPerCommonTagSet</span><span class="p">[</span><span class="n">commonTagQnt</span><span class="p">]</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-890"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-890"><span class="linenos">890</span></a>                <span class="n">commonTagGroupHashSet</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">setOfTheCommonTagGroupHashes</span><span class="p">)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-891"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-891"><span class="linenos">891</span></a>        <span class="k">for</span> <span class="n">commonTagGroupHash</span> <span class="ow">in</span> <span class="n">commonTagGroupHashSet</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-892"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-892"><span class="linenos">892</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-893"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-893"><span class="linenos">893</span></a>            <span class="n">commonTagHashTuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">commonTagSets</span><span class="p">[</span><span class="n">commonTagGroupHash</span><span class="p">]</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-894"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-894"><span class="linenos">894</span></a>            <span class="n">commonTagHashSet</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">commonTagHashTuple</span><span class="p">)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-895"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-895"><span class="linenos">895</span></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">tagHashSet</span><span class="p">):</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-896"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-896"><span class="linenos">896</span></a>                <span class="k">if</span> <span class="n">tagHashSet</span> <span class="o">!=</span> <span class="n">commonTagHashSet</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-897"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-897"><span class="linenos">897</span></a>                    <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-898"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-898"><span class="linenos">898</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">commonTagHashSet</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-899"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-899"><span class="linenos">899</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-900"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-900"><span class="linenos">900</span></a>                        <span class="n">setOfTheTagsIntersection</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">&amp;</span> <span class="n">commonTagHashSet</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-901"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-901"><span class="linenos">901</span></a>        <span class="c1">#         if tagHashSet != commonTagHashSet:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-902"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-902"><span class="linenos">902</span></a>        <span class="c1">#             setOfLenOfTheCommonTagHashSetForChecking.add(len(commonTagHashSet))</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-903"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-903"><span class="linenos">903</span></a>        <span class="c1"># minimalTagPath = min(setOfLenOfTheCommonTagHashSetForChecking)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-904"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-904"><span class="linenos">904</span></a>        <span class="c1"># pathDiff = minimalTagPath - len(tagHashSet)</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-905"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-905"><span class="linenos">905</span></a>        <span class="c1"># if pathDiff &gt; 0:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-906"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-906"><span class="linenos">906</span></a>        <span class="k">if</span> <span class="n">setOfTheTagsIntersection</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-907"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-907"><span class="linenos">907</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-908"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-908"><span class="linenos">908</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-909"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-909"><span class="linenos">909</span></a>        <span class="n">setOfTheTagsForAReduction</span> <span class="o">=</span> <span class="n">setOfTheTagsIntersection</span> <span class="o">-</span> <span class="n">tagHashSet</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-910"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-910"><span class="linenos">910</span></a>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-911"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-911"><span class="linenos">911</span></a>        <span class="n">sortedTagHashList</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_tag_hash_list_by_qnt</span><span class="p">(</span><span class="n">setOfTheTagsForAReduction</span> <span class="o">-</span> <span class="p">{</span><span class="bp">self</span><span class="o">.</span><span class="n">get_root_tag</span><span class="p">()</span><span class="o">.</span><span class="fm">__hash__</span><span class="p">()})</span>
</span><span id="TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-912"><a href="#TagDB.is_smart_redirection_for_a_tag_path_reduction_needed-912"><span class="linenos">912</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">sortedTagHashList</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TagDB.get_tags_for_a_smart_redirection" class="classattr">
                                        <input id="TagDB.get_tags_for_a_smart_redirection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_tags_for_a_smart_redirection</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">binTags</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TagDB.get_tags_for_a_smart_redirection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TagDB.get_tags_for_a_smart_redirection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TagDB.get_tags_for_a_smart_redirection-914"><a href="#TagDB.get_tags_for_a_smart_redirection-914"><span class="linenos">914</span></a>    <span class="k">def</span> <span class="nf">get_tags_for_a_smart_redirection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binTags</span><span class="p">):</span>
</span><span id="TagDB.get_tags_for_a_smart_redirection-915"><a href="#TagDB.get_tags_for_a_smart_redirection-915"><span class="linenos">915</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_smart_redirection_for_a_tag_path_reduction_needed</span><span class="p">(</span><span class="n">binTags</span><span class="p">)</span>
</span><span id="TagDB.get_tags_for_a_smart_redirection-916"><a href="#TagDB.get_tags_for_a_smart_redirection-916"><span class="linenos">916</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tag_hash_list_2_tag_list</span><span class="p">(</span><span class="n">result</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.EntityStatsMixin</dt>
                                <dd id="TagDB.StatsLevel" class="class">StatsLevel</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>