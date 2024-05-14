---
title: fast_fifo
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_containers<wbr>.fast_fifo<wbr>.versions<wbr>.v_0<wbr>.fast_fifo    </h1>

                
                        <input id="mod-fast_fifo-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-fast_fifo-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_0</span> <span class="kn">import</span> <span class="n">ResultCache</span><span class="p">,</span> <span class="n">ResultExistence</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">from</span> <span class="nn">cengal.code_inspection.line_profiling</span> <span class="kn">import</span> <span class="n">set_profiler</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="sd">Быстрый модуль FIFO. Скорость достигается за счет уменьшенного количества аллокаций и деаллокаций памяти и</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="sd">соответственно, за счет бОльшего размера используемой памяти в пИке. Расход памяти неравномерный: сначала происходит</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="sd">постоянное увеличение размера используемой памяти, а при превышении лимита - вся ненужная память деалоцируется</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="sd">одномоментно, что приводит лишь к одному пересозданию контейнерного списка блоков.</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="c1"># set_profiler(True)</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="n">set_profiler</span><span class="p">(</span><span class="kc">False</span><span class="p">)</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="k">class</span> <span class="nc">FIFOIsEmpty</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="k">pass</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="k">class</span> <span class="nc">FIFO</span><span class="p">:</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span> <span class="ow">or</span> <span class="mi">1000</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">:</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">_free</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">):</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="n">num</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="k">pass</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="n">FIFO</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span><span class="p">)</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="k">class</span> <span class="nc">FIFOWithLengthControl</span><span class="p">(</span><span class="n">FIFO</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_hold_data_size_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>                 <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>                 <span class="n">external_deletable_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">on_hold_limit</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span> <span class="ow">or</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span> <span class="o">*</span> <span class="mi">10</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data_size</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="k">while</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="n">piece_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">piece_size</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">piece_size</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="c1"># self._l_deletable_length.append(result_len)</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span><span class="p">):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>            <span class="c1"># diff_full_data_size = sum(self._l_length[:self._offset])</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>            <span class="c1"># diff_full_data_size = self._deletable_data_full_size</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            <span class="c1"># self.get_data_full_size()</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="c1"># @profile</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">_free</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">):</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+</span> <span class="n">num</span><span class="p">]</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="c1"># self._l_deletable_length.extend(result)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="n">num</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span><span class="p">):</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="nf">_calculate_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="n">data_full_size</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="n">last_data_full_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="n">diff_data_full_size</span> <span class="o">=</span> <span class="n">data_full_size</span> <span class="o">-</span> <span class="n">last_data_full_size</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">data_full_size</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">diff_data_full_size</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="k">def</span> <span class="nf">get_deletable_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="k">return</span> <span class="n">FIFOWithLengthControl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span><span class="p">,</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_data_size_limit</span><span class="p">,</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span><span class="p">,</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_deletable_data_full_size</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a><span class="k">class</span> <span class="nc">FIFODequeWithLengthControl</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="c1"># self._l_length = deque()</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="c1"># self._l_length.append(data_size)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">iterable_data</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="n">elem_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>            <span class="c1"># self._l_length.append(elem_size)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">elem_size</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="nf">get_at_least_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="n">result_data</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="n">result_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="n">result_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="ow">and</span> <span class="p">(</span><span class="n">result_size</span> <span class="o">&lt;</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            <span class="n">another_piece</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="n">result_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>            <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="n">result_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="n">result_qnt</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result_data</span><span class="p">,</span> <span class="n">result_size</span><span class="p">,</span> <span class="n">result_qnt</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span><span class="p">)</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span></pre></div>


            </section>
                <section id="FIFOIsEmpty">
                            <input id="FIFOIsEmpty-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FIFOIsEmpty</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="FIFOIsEmpty-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOIsEmpty"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOIsEmpty-47"><a href="#FIFOIsEmpty-47"><span class="linenos">47</span></a><span class="k">class</span> <span class="nc">FIFOIsEmpty</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="FIFOIsEmpty-48"><a href="#FIFOIsEmpty-48"><span class="linenos">48</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="FIFOIsEmpty.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="FIFOIsEmpty.with_traceback" class="function">with_traceback</dd>
                <dd id="FIFOIsEmpty.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="FIFO">
                            <input id="FIFO-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FIFO</span>:

                <label class="view-source-button" for="FIFO-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO-51"><a href="#FIFO-51"><span class="linenos"> 51</span></a><span class="k">class</span> <span class="nc">FIFO</span><span class="p">:</span>
</span><span id="FIFO-52"><a href="#FIFO-52"><span class="linenos"> 52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFO-53"><a href="#FIFO-53"><span class="linenos"> 53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span>
</span><span id="FIFO-54"><a href="#FIFO-54"><span class="linenos"> 54</span></a>
</span><span id="FIFO-55"><a href="#FIFO-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="FIFO-56"><a href="#FIFO-56"><span class="linenos"> 56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO-57"><a href="#FIFO-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span> <span class="ow">or</span> <span class="mi">1000</span>
</span><span id="FIFO-58"><a href="#FIFO-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO-59"><a href="#FIFO-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO-60"><a href="#FIFO-60"><span class="linenos"> 60</span></a>
</span><span id="FIFO-61"><a href="#FIFO-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFO-62"><a href="#FIFO-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFO-63"><a href="#FIFO-63"><span class="linenos"> 63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFO-64"><a href="#FIFO-64"><span class="linenos"> 64</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFO-65"><a href="#FIFO-65"><span class="linenos"> 65</span></a>
</span><span id="FIFO-66"><a href="#FIFO-66"><span class="linenos"> 66</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFO-67"><a href="#FIFO-67"><span class="linenos"> 67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="FIFO-68"><a href="#FIFO-68"><span class="linenos"> 68</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="FIFO-69"><a href="#FIFO-69"><span class="linenos"> 69</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFO-70"><a href="#FIFO-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFO-71"><a href="#FIFO-71"><span class="linenos"> 71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFO-72"><a href="#FIFO-72"><span class="linenos"> 72</span></a>
</span><span id="FIFO-73"><a href="#FIFO-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO-74"><a href="#FIFO-74"><span class="linenos"> 74</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="FIFO-75"><a href="#FIFO-75"><span class="linenos"> 75</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="FIFO-76"><a href="#FIFO-76"><span class="linenos"> 76</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFO-77"><a href="#FIFO-77"><span class="linenos"> 77</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFO-78"><a href="#FIFO-78"><span class="linenos"> 78</span></a>
</span><span id="FIFO-79"><a href="#FIFO-79"><span class="linenos"> 79</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFO-80"><a href="#FIFO-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFO-81"><a href="#FIFO-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFO-82"><a href="#FIFO-82"><span class="linenos"> 82</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">:</span>
</span><span id="FIFO-83"><a href="#FIFO-83"><span class="linenos"> 83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFO-84"><a href="#FIFO-84"><span class="linenos"> 84</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFO-85"><a href="#FIFO-85"><span class="linenos"> 85</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO-86"><a href="#FIFO-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="FIFO-87"><a href="#FIFO-87"><span class="linenos"> 87</span></a>
</span><span id="FIFO-88"><a href="#FIFO-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">_free</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">):</span>
</span><span id="FIFO-89"><a href="#FIFO-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="n">num</span>
</span><span id="FIFO-90"><a href="#FIFO-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="FIFO-91"><a href="#FIFO-91"><span class="linenos"> 91</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">:</span>
</span><span id="FIFO-92"><a href="#FIFO-92"><span class="linenos"> 92</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFO-93"><a href="#FIFO-93"><span class="linenos"> 93</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFO-94"><a href="#FIFO-94"><span class="linenos"> 94</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO-95"><a href="#FIFO-95"><span class="linenos"> 95</span></a>
</span><span id="FIFO-96"><a href="#FIFO-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO-97"><a href="#FIFO-97"><span class="linenos"> 97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span>
</span><span id="FIFO-98"><a href="#FIFO-98"><span class="linenos"> 98</span></a>
</span><span id="FIFO-99"><a href="#FIFO-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO-100"><a href="#FIFO-100"><span class="linenos">100</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFO-101"><a href="#FIFO-101"><span class="linenos">101</span></a>
</span><span id="FIFO-102"><a href="#FIFO-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO-103"><a href="#FIFO-103"><span class="linenos">103</span></a>        <span class="k">pass</span>
</span><span id="FIFO-104"><a href="#FIFO-104"><span class="linenos">104</span></a>
</span><span id="FIFO-105"><a href="#FIFO-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO-106"><a href="#FIFO-106"><span class="linenos">106</span></a>        <span class="k">return</span> <span class="n">FIFO</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="FIFO.__init__" class="classattr">
                                        <input id="FIFO.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">FIFO</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="FIFO.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.__init__-52"><a href="#FIFO.__init__-52"><span class="linenos">52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFO.__init__-53"><a href="#FIFO.__init__-53"><span class="linenos">53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span>
</span><span id="FIFO.__init__-54"><a href="#FIFO.__init__-54"><span class="linenos">54</span></a>
</span><span id="FIFO.__init__-55"><a href="#FIFO.__init__-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="FIFO.__init__-56"><a href="#FIFO.__init__-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO.__init__-57"><a href="#FIFO.__init__-57"><span class="linenos">57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span> <span class="o">=</span> <span class="n">on_hold_limit</span> <span class="ow">or</span> <span class="mi">1000</span>
</span><span id="FIFO.__init__-58"><a href="#FIFO.__init__-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO.__init__-59"><a href="#FIFO.__init__-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.put" class="classattr">
                                        <input id="FIFO.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.put-61"><a href="#FIFO.put-61"><span class="linenos">61</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFO.put-62"><a href="#FIFO.put-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFO.put-63"><a href="#FIFO.put-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFO.put-64"><a href="#FIFO.put-64"><span class="linenos">64</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.extend" class="classattr">
                                        <input id="FIFO.extend-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">extend</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">iterable_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.extend-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.extend"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.extend-66"><a href="#FIFO.extend-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFO.extend-67"><a href="#FIFO.extend-67"><span class="linenos">67</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="FIFO.extend-68"><a href="#FIFO.extend-68"><span class="linenos">68</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="FIFO.extend-69"><a href="#FIFO.extend-69"><span class="linenos">69</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFO.extend-70"><a href="#FIFO.extend-70"><span class="linenos">70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFO.extend-71"><a href="#FIFO.extend-71"><span class="linenos">71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.get" class="classattr">
                                        <input id="FIFO.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.get-73"><a href="#FIFO.get-73"><span class="linenos">73</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO.get-74"><a href="#FIFO.get-74"><span class="linenos">74</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="FIFO.get-75"><a href="#FIFO.get-75"><span class="linenos">75</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="FIFO.get-76"><a href="#FIFO.get-76"><span class="linenos">76</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFO.get-77"><a href="#FIFO.get-77"><span class="linenos">77</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFO.get-78"><a href="#FIFO.get-78"><span class="linenos">78</span></a>
</span><span id="FIFO.get-79"><a href="#FIFO.get-79"><span class="linenos">79</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFO.get-80"><a href="#FIFO.get-80"><span class="linenos">80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFO.get-81"><a href="#FIFO.get-81"><span class="linenos">81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFO.get-82"><a href="#FIFO.get-82"><span class="linenos">82</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">:</span>
</span><span id="FIFO.get-83"><a href="#FIFO.get-83"><span class="linenos">83</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFO.get-84"><a href="#FIFO.get-84"><span class="linenos">84</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFO.get-85"><a href="#FIFO.get-85"><span class="linenos">85</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFO.get-86"><a href="#FIFO.get-86"><span class="linenos">86</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.size" class="classattr">
                                        <input id="FIFO.size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.size-96"><a href="#FIFO.size-96"><span class="linenos">96</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO.size-97"><a href="#FIFO.size-97"><span class="linenos">97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.full_size" class="classattr">
                                        <input id="FIFO.full_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.full_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.full_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.full_size-99"><a href="#FIFO.full_size-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO.full_size-100"><a href="#FIFO.full_size-100"><span class="linenos">100</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFO.remove" class="classattr">
                                        <input id="FIFO.remove-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFO.remove-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFO.remove"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFO.remove-102"><a href="#FIFO.remove-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFO.remove-103"><a href="#FIFO.remove-103"><span class="linenos">103</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="FIFOWithLengthControl">
                            <input id="FIFOWithLengthControl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FIFOWithLengthControl</span><wbr>(<span class="base"><a href="#FIFO">FIFO</a></span>):

                <label class="view-source-button" for="FIFOWithLengthControl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl-109"><a href="#FIFOWithLengthControl-109"><span class="linenos">109</span></a><span class="k">class</span> <span class="nc">FIFOWithLengthControl</span><span class="p">(</span><span class="n">FIFO</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-110"><a href="#FIFOWithLengthControl-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_hold_data_size_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl-111"><a href="#FIFOWithLengthControl-111"><span class="linenos">111</span></a>                 <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl-112"><a href="#FIFOWithLengthControl-112"><span class="linenos">112</span></a>                 <span class="n">external_deletable_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-113"><a href="#FIFOWithLengthControl-113"><span class="linenos">113</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">on_hold_limit</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-114"><a href="#FIFOWithLengthControl-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="FIFOWithLengthControl-115"><a href="#FIFOWithLengthControl-115"><span class="linenos">115</span></a>
</span><span id="FIFOWithLengthControl-116"><a href="#FIFOWithLengthControl-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span>
</span><span id="FIFOWithLengthControl-117"><a href="#FIFOWithLengthControl-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="FIFOWithLengthControl-118"><a href="#FIFOWithLengthControl-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-119"><a href="#FIFOWithLengthControl-119"><span class="linenos">119</span></a>
</span><span id="FIFOWithLengthControl-120"><a href="#FIFOWithLengthControl-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-121"><a href="#FIFOWithLengthControl-121"><span class="linenos">121</span></a>        <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="FIFOWithLengthControl-122"><a href="#FIFOWithLengthControl-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-123"><a href="#FIFOWithLengthControl-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-124"><a href="#FIFOWithLengthControl-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-125"><a href="#FIFOWithLengthControl-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span> <span class="ow">or</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span> <span class="o">*</span> <span class="mi">10</span>
</span><span id="FIFOWithLengthControl-126"><a href="#FIFOWithLengthControl-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-127"><a href="#FIFOWithLengthControl-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-128"><a href="#FIFOWithLengthControl-128"><span class="linenos">128</span></a>
</span><span id="FIFOWithLengthControl-129"><a href="#FIFOWithLengthControl-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-130"><a href="#FIFOWithLengthControl-130"><span class="linenos">130</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-131"><a href="#FIFOWithLengthControl-131"><span class="linenos">131</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-132"><a href="#FIFOWithLengthControl-132"><span class="linenos">132</span></a>
</span><span id="FIFOWithLengthControl-133"><a href="#FIFOWithLengthControl-133"><span class="linenos">133</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-134"><a href="#FIFOWithLengthControl-134"><span class="linenos">134</span></a>        
</span><span id="FIFOWithLengthControl-135"><a href="#FIFOWithLengthControl-135"><span class="linenos">135</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-136"><a href="#FIFOWithLengthControl-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-137"><a href="#FIFOWithLengthControl-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFOWithLengthControl-138"><a href="#FIFOWithLengthControl-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFOWithLengthControl-139"><a href="#FIFOWithLengthControl-139"><span class="linenos">139</span></a>
</span><span id="FIFOWithLengthControl-140"><a href="#FIFOWithLengthControl-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-141"><a href="#FIFOWithLengthControl-141"><span class="linenos">141</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-142"><a href="#FIFOWithLengthControl-142"><span class="linenos">142</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-143"><a href="#FIFOWithLengthControl-143"><span class="linenos">143</span></a>
</span><span id="FIFOWithLengthControl-144"><a href="#FIFOWithLengthControl-144"><span class="linenos">144</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFOWithLengthControl-145"><a href="#FIFOWithLengthControl-145"><span class="linenos">145</span></a>
</span><span id="FIFOWithLengthControl-146"><a href="#FIFOWithLengthControl-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-147"><a href="#FIFOWithLengthControl-147"><span class="linenos">147</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-148"><a href="#FIFOWithLengthControl-148"><span class="linenos">148</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFOWithLengthControl-149"><a href="#FIFOWithLengthControl-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFOWithLengthControl-150"><a href="#FIFOWithLengthControl-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFOWithLengthControl-151"><a href="#FIFOWithLengthControl-151"><span class="linenos">151</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-152"><a href="#FIFOWithLengthControl-152"><span class="linenos">152</span></a>
</span><span id="FIFOWithLengthControl-153"><a href="#FIFOWithLengthControl-153"><span class="linenos">153</span></a>        <span class="k">while</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-154"><a href="#FIFOWithLengthControl-154"><span class="linenos">154</span></a>            <span class="n">piece_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="FIFOWithLengthControl-155"><a href="#FIFOWithLengthControl-155"><span class="linenos">155</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">piece_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-156"><a href="#FIFOWithLengthControl-156"><span class="linenos">156</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">piece_size</span>
</span><span id="FIFOWithLengthControl-157"><a href="#FIFOWithLengthControl-157"><span class="linenos">157</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl-158"><a href="#FIFOWithLengthControl-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFOWithLengthControl-159"><a href="#FIFOWithLengthControl-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFOWithLengthControl-160"><a href="#FIFOWithLengthControl-160"><span class="linenos">160</span></a>
</span><span id="FIFOWithLengthControl-161"><a href="#FIFOWithLengthControl-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-162"><a href="#FIFOWithLengthControl-162"><span class="linenos">162</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="FIFOWithLengthControl-163"><a href="#FIFOWithLengthControl-163"><span class="linenos">163</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="FIFOWithLengthControl-164"><a href="#FIFOWithLengthControl-164"><span class="linenos">164</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-165"><a href="#FIFOWithLengthControl-165"><span class="linenos">165</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-166"><a href="#FIFOWithLengthControl-166"><span class="linenos">166</span></a>
</span><span id="FIFOWithLengthControl-167"><a href="#FIFOWithLengthControl-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-168"><a href="#FIFOWithLengthControl-168"><span class="linenos">168</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-169"><a href="#FIFOWithLengthControl-169"><span class="linenos">169</span></a>
</span><span id="FIFOWithLengthControl-170"><a href="#FIFOWithLengthControl-170"><span class="linenos">170</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFOWithLengthControl-171"><a href="#FIFOWithLengthControl-171"><span class="linenos">171</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFOWithLengthControl-172"><a href="#FIFOWithLengthControl-172"><span class="linenos">172</span></a>        <span class="c1"># self._l_deletable_length.append(result_len)</span>
</span><span id="FIFOWithLengthControl-173"><a href="#FIFOWithLengthControl-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl-174"><a href="#FIFOWithLengthControl-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl-175"><a href="#FIFOWithLengthControl-175"><span class="linenos">175</span></a>
</span><span id="FIFOWithLengthControl-176"><a href="#FIFOWithLengthControl-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl-177"><a href="#FIFOWithLengthControl-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl-178"><a href="#FIFOWithLengthControl-178"><span class="linenos">178</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-179"><a href="#FIFOWithLengthControl-179"><span class="linenos">179</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFOWithLengthControl-180"><a href="#FIFOWithLengthControl-180"><span class="linenos">180</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl-181"><a href="#FIFOWithLengthControl-181"><span class="linenos">181</span></a>            <span class="c1"># diff_full_data_size = sum(self._l_length[:self._offset])</span>
</span><span id="FIFOWithLengthControl-182"><a href="#FIFOWithLengthControl-182"><span class="linenos">182</span></a>            <span class="c1"># diff_full_data_size = self._deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-183"><a href="#FIFOWithLengthControl-183"><span class="linenos">183</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-184"><a href="#FIFOWithLengthControl-184"><span class="linenos">184</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-185"><a href="#FIFOWithLengthControl-185"><span class="linenos">185</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl-186"><a href="#FIFOWithLengthControl-186"><span class="linenos">186</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-187"><a href="#FIFOWithLengthControl-187"><span class="linenos">187</span></a>            <span class="c1"># self.get_data_full_size()</span>
</span><span id="FIFOWithLengthControl-188"><a href="#FIFOWithLengthControl-188"><span class="linenos">188</span></a>            <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="FIFOWithLengthControl-189"><a href="#FIFOWithLengthControl-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-190"><a href="#FIFOWithLengthControl-190"><span class="linenos">190</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-191"><a href="#FIFOWithLengthControl-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="FIFOWithLengthControl-192"><a href="#FIFOWithLengthControl-192"><span class="linenos">192</span></a>
</span><span id="FIFOWithLengthControl-193"><a href="#FIFOWithLengthControl-193"><span class="linenos">193</span></a>    <span class="c1"># @profile</span>
</span><span id="FIFOWithLengthControl-194"><a href="#FIFOWithLengthControl-194"><span class="linenos">194</span></a>    <span class="k">def</span> <span class="nf">_free</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-195"><a href="#FIFOWithLengthControl-195"><span class="linenos">195</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+</span> <span class="n">num</span><span class="p">]</span>
</span><span id="FIFOWithLengthControl-196"><a href="#FIFOWithLengthControl-196"><span class="linenos">196</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-197"><a href="#FIFOWithLengthControl-197"><span class="linenos">197</span></a>        <span class="c1"># self._l_deletable_length.extend(result)</span>
</span><span id="FIFOWithLengthControl-198"><a href="#FIFOWithLengthControl-198"><span class="linenos">198</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl-199"><a href="#FIFOWithLengthControl-199"><span class="linenos">199</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl-200"><a href="#FIFOWithLengthControl-200"><span class="linenos">200</span></a>
</span><span id="FIFOWithLengthControl-201"><a href="#FIFOWithLengthControl-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="n">num</span>
</span><span id="FIFOWithLengthControl-202"><a href="#FIFOWithLengthControl-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="n">num</span>
</span><span id="FIFOWithLengthControl-203"><a href="#FIFOWithLengthControl-203"><span class="linenos">203</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-204"><a href="#FIFOWithLengthControl-204"><span class="linenos">204</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFOWithLengthControl-205"><a href="#FIFOWithLengthControl-205"><span class="linenos">205</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl-206"><a href="#FIFOWithLengthControl-206"><span class="linenos">206</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-207"><a href="#FIFOWithLengthControl-207"><span class="linenos">207</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-208"><a href="#FIFOWithLengthControl-208"><span class="linenos">208</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl-209"><a href="#FIFOWithLengthControl-209"><span class="linenos">209</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-210"><a href="#FIFOWithLengthControl-210"><span class="linenos">210</span></a>            <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="FIFOWithLengthControl-211"><a href="#FIFOWithLengthControl-211"><span class="linenos">211</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-212"><a href="#FIFOWithLengthControl-212"><span class="linenos">212</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl-213"><a href="#FIFOWithLengthControl-213"><span class="linenos">213</span></a>            
</span><span id="FIFOWithLengthControl-214"><a href="#FIFOWithLengthControl-214"><span class="linenos">214</span></a>    <span class="k">def</span> <span class="nf">_calculate_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-215"><a href="#FIFOWithLengthControl-215"><span class="linenos">215</span></a>        <span class="n">data_full_size</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-216"><a href="#FIFOWithLengthControl-216"><span class="linenos">216</span></a>        <span class="n">last_data_full_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="FIFOWithLengthControl-217"><a href="#FIFOWithLengthControl-217"><span class="linenos">217</span></a>        <span class="n">diff_data_full_size</span> <span class="o">=</span> <span class="n">data_full_size</span> <span class="o">-</span> <span class="n">last_data_full_size</span>
</span><span id="FIFOWithLengthControl-218"><a href="#FIFOWithLengthControl-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">data_full_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-219"><a href="#FIFOWithLengthControl-219"><span class="linenos">219</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">diff_data_full_size</span>
</span><span id="FIFOWithLengthControl-220"><a href="#FIFOWithLengthControl-220"><span class="linenos">220</span></a>        
</span><span id="FIFOWithLengthControl-221"><a href="#FIFOWithLengthControl-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-222"><a href="#FIFOWithLengthControl-222"><span class="linenos">222</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-223"><a href="#FIFOWithLengthControl-223"><span class="linenos">223</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl-224"><a href="#FIFOWithLengthControl-224"><span class="linenos">224</span></a>
</span><span id="FIFOWithLengthControl-225"><a href="#FIFOWithLengthControl-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="FIFOWithLengthControl-226"><a href="#FIFOWithLengthControl-226"><span class="linenos">226</span></a>
</span><span id="FIFOWithLengthControl-227"><a href="#FIFOWithLengthControl-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">get_deletable_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-228"><a href="#FIFOWithLengthControl-228"><span class="linenos">228</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-229"><a href="#FIFOWithLengthControl-229"><span class="linenos">229</span></a>
</span><span id="FIFOWithLengthControl-230"><a href="#FIFOWithLengthControl-230"><span class="linenos">230</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-231"><a href="#FIFOWithLengthControl-231"><span class="linenos">231</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl-232"><a href="#FIFOWithLengthControl-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="FIFOWithLengthControl-233"><a href="#FIFOWithLengthControl-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl-234"><a href="#FIFOWithLengthControl-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="FIFOWithLengthControl-235"><a href="#FIFOWithLengthControl-235"><span class="linenos">235</span></a>
</span><span id="FIFOWithLengthControl-236"><a href="#FIFOWithLengthControl-236"><span class="linenos">236</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-237"><a href="#FIFOWithLengthControl-237"><span class="linenos">237</span></a>        <span class="k">return</span> <span class="n">FIFOWithLengthControl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_limit</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl-238"><a href="#FIFOWithLengthControl-238"><span class="linenos">238</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_data_size_limit</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl-239"><a href="#FIFOWithLengthControl-239"><span class="linenos">239</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl-240"><a href="#FIFOWithLengthControl-240"><span class="linenos">240</span></a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_deletable_data_full_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl-241"><a href="#FIFOWithLengthControl-241"><span class="linenos">241</span></a>
</span><span id="FIFOWithLengthControl-242"><a href="#FIFOWithLengthControl-242"><span class="linenos">242</span></a>    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl-243"><a href="#FIFOWithLengthControl-243"><span class="linenos">243</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="FIFOWithLengthControl.__init__" class="classattr">
                                        <input id="FIFOWithLengthControl.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">FIFOWithLengthControl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">on_hold_data_size_limit</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">result_types</span><span class="o">.</span><span class="n">ResultExistence</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">external_deletable_data_full_size</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">result_types</span><span class="o">.</span><span class="n">ResultExistence</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="FIFOWithLengthControl.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.__init__-110"><a href="#FIFOWithLengthControl.__init__-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">on_hold_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">on_hold_data_size_limit</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl.__init__-111"><a href="#FIFOWithLengthControl.__init__-111"><span class="linenos">111</span></a>                 <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="FIFOWithLengthControl.__init__-112"><a href="#FIFOWithLengthControl.__init__-112"><span class="linenos">112</span></a>                 <span class="n">external_deletable_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.__init__-113"><a href="#FIFOWithLengthControl.__init__-113"><span class="linenos">113</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">on_hold_limit</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.__init__-114"><a href="#FIFOWithLengthControl.__init__-114"><span class="linenos">114</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="FIFOWithLengthControl.__init__-115"><a href="#FIFOWithLengthControl.__init__-115"><span class="linenos">115</span></a>
</span><span id="FIFOWithLengthControl.__init__-116"><a href="#FIFOWithLengthControl.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span>
</span><span id="FIFOWithLengthControl.__init__-117"><a href="#FIFOWithLengthControl.__init__-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="FIFOWithLengthControl.__init__-118"><a href="#FIFOWithLengthControl.__init__-118"><span class="linenos">118</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.__init__-119"><a href="#FIFOWithLengthControl.__init__-119"><span class="linenos">119</span></a>
</span><span id="FIFOWithLengthControl.__init__-120"><a href="#FIFOWithLengthControl.__init__-120"><span class="linenos">120</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.__init__-121"><a href="#FIFOWithLengthControl.__init__-121"><span class="linenos">121</span></a>        <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="FIFOWithLengthControl.__init__-122"><a href="#FIFOWithLengthControl.__init__-122"><span class="linenos">122</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.__init__-123"><a href="#FIFOWithLengthControl.__init__-123"><span class="linenos">123</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.__init__-124"><a href="#FIFOWithLengthControl.__init__-124"><span class="linenos">124</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl.__init__-125"><a href="#FIFOWithLengthControl.__init__-125"><span class="linenos">125</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span> <span class="o">=</span> <span class="n">on_hold_data_size_limit</span> <span class="ow">or</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span> <span class="o">*</span> <span class="mi">10</span>
</span><span id="FIFOWithLengthControl.__init__-126"><a href="#FIFOWithLengthControl.__init__-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.__init__-127"><a href="#FIFOWithLengthControl.__init__-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span> <span class="o">=</span> <span class="n">external_deletable_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.put" class="classattr">
                                        <input id="FIFOWithLengthControl.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.put-129"><a href="#FIFOWithLengthControl.put-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.put-130"><a href="#FIFOWithLengthControl.put-130"><span class="linenos">130</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.put-131"><a href="#FIFOWithLengthControl.put-131"><span class="linenos">131</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.put-132"><a href="#FIFOWithLengthControl.put-132"><span class="linenos">132</span></a>
</span><span id="FIFOWithLengthControl.put-133"><a href="#FIFOWithLengthControl.put-133"><span class="linenos">133</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">FIFOWithLengthControl</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">put</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.put-134"><a href="#FIFOWithLengthControl.put-134"><span class="linenos">134</span></a>        
</span><span id="FIFOWithLengthControl.put-135"><a href="#FIFOWithLengthControl.put-135"><span class="linenos">135</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.put-136"><a href="#FIFOWithLengthControl.put-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.put-137"><a href="#FIFOWithLengthControl.put-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFOWithLengthControl.put-138"><a href="#FIFOWithLengthControl.put-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.extend" class="classattr">
                                        <input id="FIFOWithLengthControl.extend-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">extend</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">iterable_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.extend-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.extend"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.extend-140"><a href="#FIFOWithLengthControl.extend-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.extend-141"><a href="#FIFOWithLengthControl.extend-141"><span class="linenos">141</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.extend-142"><a href="#FIFOWithLengthControl.extend-142"><span class="linenos">142</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.extend-143"><a href="#FIFOWithLengthControl.extend-143"><span class="linenos">143</span></a>
</span><span id="FIFOWithLengthControl.extend-144"><a href="#FIFOWithLengthControl.extend-144"><span class="linenos">144</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFOWithLengthControl.extend-145"><a href="#FIFOWithLengthControl.extend-145"><span class="linenos">145</span></a>
</span><span id="FIFOWithLengthControl.extend-146"><a href="#FIFOWithLengthControl.extend-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">iterable_data</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.extend-147"><a href="#FIFOWithLengthControl.extend-147"><span class="linenos">147</span></a>        <span class="n">new_full_length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.extend-148"><a href="#FIFOWithLengthControl.extend-148"><span class="linenos">148</span></a>        <span class="n">diff</span> <span class="o">=</span> <span class="n">new_full_length</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFOWithLengthControl.extend-149"><a href="#FIFOWithLengthControl.extend-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFOWithLengthControl.extend-150"><a href="#FIFOWithLengthControl.extend-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="n">diff</span>
</span><span id="FIFOWithLengthControl.extend-151"><a href="#FIFOWithLengthControl.extend-151"><span class="linenos">151</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl.extend-152"><a href="#FIFOWithLengthControl.extend-152"><span class="linenos">152</span></a>
</span><span id="FIFOWithLengthControl.extend-153"><a href="#FIFOWithLengthControl.extend-153"><span class="linenos">153</span></a>        <span class="k">while</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.extend-154"><a href="#FIFOWithLengthControl.extend-154"><span class="linenos">154</span></a>            <span class="n">piece_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="FIFOWithLengthControl.extend-155"><a href="#FIFOWithLengthControl.extend-155"><span class="linenos">155</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">piece_size</span><span class="p">)</span>
</span><span id="FIFOWithLengthControl.extend-156"><a href="#FIFOWithLengthControl.extend-156"><span class="linenos">156</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">piece_size</span>
</span><span id="FIFOWithLengthControl.extend-157"><a href="#FIFOWithLengthControl.extend-157"><span class="linenos">157</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl.extend-158"><a href="#FIFOWithLengthControl.extend-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFOWithLengthControl.extend-159"><a href="#FIFOWithLengthControl.extend-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.get" class="classattr">
                                        <input id="FIFOWithLengthControl.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.get-161"><a href="#FIFOWithLengthControl.get-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.get-162"><a href="#FIFOWithLengthControl.get-162"><span class="linenos">162</span></a>        <span class="c1"># l_offset_limit = 1000: 574305.7210067833 iterations per second</span>
</span><span id="FIFOWithLengthControl.get-163"><a href="#FIFOWithLengthControl.get-163"><span class="linenos">163</span></a>        <span class="c1"># PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second</span>
</span><span id="FIFOWithLengthControl.get-164"><a href="#FIFOWithLengthControl.get-164"><span class="linenos">164</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.get-165"><a href="#FIFOWithLengthControl.get-165"><span class="linenos">165</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.get-166"><a href="#FIFOWithLengthControl.get-166"><span class="linenos">166</span></a>
</span><span id="FIFOWithLengthControl.get-167"><a href="#FIFOWithLengthControl.get-167"><span class="linenos">167</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.get-168"><a href="#FIFOWithLengthControl.get-168"><span class="linenos">168</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.get-169"><a href="#FIFOWithLengthControl.get-169"><span class="linenos">169</span></a>
</span><span id="FIFOWithLengthControl.get-170"><a href="#FIFOWithLengthControl.get-170"><span class="linenos">170</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFOWithLengthControl.get-171"><a href="#FIFOWithLengthControl.get-171"><span class="linenos">171</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">]</span>
</span><span id="FIFOWithLengthControl.get-172"><a href="#FIFOWithLengthControl.get-172"><span class="linenos">172</span></a>        <span class="c1"># self._l_deletable_length.append(result_len)</span>
</span><span id="FIFOWithLengthControl.get-173"><a href="#FIFOWithLengthControl.get-173"><span class="linenos">173</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl.get-174"><a href="#FIFOWithLengthControl.get-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFOWithLengthControl.get-175"><a href="#FIFOWithLengthControl.get-175"><span class="linenos">175</span></a>
</span><span id="FIFOWithLengthControl.get-176"><a href="#FIFOWithLengthControl.get-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_useful_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl.get-177"><a href="#FIFOWithLengthControl.get-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFOWithLengthControl.get-178"><a href="#FIFOWithLengthControl.get-178"><span class="linenos">178</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset_limit</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_hold_data_size_limit</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.get-179"><a href="#FIFOWithLengthControl.get-179"><span class="linenos">179</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span>
</span><span id="FIFOWithLengthControl.get-180"><a href="#FIFOWithLengthControl.get-180"><span class="linenos">180</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl.get-181"><a href="#FIFOWithLengthControl.get-181"><span class="linenos">181</span></a>            <span class="c1"># diff_full_data_size = sum(self._l_length[:self._offset])</span>
</span><span id="FIFOWithLengthControl.get-182"><a href="#FIFOWithLengthControl.get-182"><span class="linenos">182</span></a>            <span class="c1"># diff_full_data_size = self._deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.get-183"><a href="#FIFOWithLengthControl.get-183"><span class="linenos">183</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.get-184"><a href="#FIFOWithLengthControl.get-184"><span class="linenos">184</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.get-185"><a href="#FIFOWithLengthControl.get-185"><span class="linenos">185</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l_length</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">:]</span>
</span><span id="FIFOWithLengthControl.get-186"><a href="#FIFOWithLengthControl.get-186"><span class="linenos">186</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl.get-187"><a href="#FIFOWithLengthControl.get-187"><span class="linenos">187</span></a>            <span class="c1"># self.get_data_full_size()</span>
</span><span id="FIFOWithLengthControl.get-188"><a href="#FIFOWithLengthControl.get-188"><span class="linenos">188</span></a>            <span class="c1"># self._l_deletable_length = list()</span>
</span><span id="FIFOWithLengthControl.get-189"><a href="#FIFOWithLengthControl.get-189"><span class="linenos">189</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.get-190"><a href="#FIFOWithLengthControl.get-190"><span class="linenos">190</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFOWithLengthControl.get-191"><a href="#FIFOWithLengthControl.get-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.get_data_full_size" class="classattr">
                                        <input id="FIFOWithLengthControl.get_data_full_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_data_full_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.get_data_full_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.get_data_full_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.get_data_full_size-221"><a href="#FIFOWithLengthControl.get_data_full_size-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.get_data_full_size-222"><a href="#FIFOWithLengthControl.get_data_full_size-222"><span class="linenos">222</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.get_data_full_size-223"><a href="#FIFOWithLengthControl.get_data_full_size-223"><span class="linenos">223</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_calculate_data_full_size</span><span class="p">()</span>
</span><span id="FIFOWithLengthControl.get_data_full_size-224"><a href="#FIFOWithLengthControl.get_data_full_size-224"><span class="linenos">224</span></a>
</span><span id="FIFOWithLengthControl.get_data_full_size-225"><a href="#FIFOWithLengthControl.get_data_full_size-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.get_deletable_data_full_size" class="classattr">
                                        <input id="FIFOWithLengthControl.get_deletable_data_full_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_deletable_data_full_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.get_deletable_data_full_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.get_deletable_data_full_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.get_deletable_data_full_size-227"><a href="#FIFOWithLengthControl.get_deletable_data_full_size-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">get_deletable_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.get_deletable_data_full_size-228"><a href="#FIFOWithLengthControl.get_deletable_data_full_size-228"><span class="linenos">228</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFOWithLengthControl.remove" class="classattr">
                                        <input id="FIFOWithLengthControl.remove-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFOWithLengthControl.remove-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFOWithLengthControl.remove"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFOWithLengthControl.remove-230"><a href="#FIFOWithLengthControl.remove-230"><span class="linenos">230</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFOWithLengthControl.remove-231"><a href="#FIFOWithLengthControl.remove-231"><span class="linenos">231</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="FIFOWithLengthControl.remove-232"><a href="#FIFOWithLengthControl.remove-232"><span class="linenos">232</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span><span class="o">.</span><span class="n">result</span>
</span><span id="FIFOWithLengthControl.remove-233"><a href="#FIFOWithLengthControl.remove-233"><span class="linenos">233</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_deletable_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_deletable_data_full_size</span>
</span><span id="FIFOWithLengthControl.remove-234"><a href="#FIFOWithLengthControl.remove-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#FIFO">FIFO</a></dt>
                                <dd id="FIFOWithLengthControl.size" class="function"><a href="#FIFO.size">size</a></dd>
                <dd id="FIFOWithLengthControl.full_size" class="function"><a href="#FIFO.full_size">full_size</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="FIFODequeWithLengthControl">
                            <input id="FIFODequeWithLengthControl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">FIFODequeWithLengthControl</span>:

                <label class="view-source-button" for="FIFODequeWithLengthControl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl-246"><a href="#FIFODequeWithLengthControl-246"><span class="linenos">246</span></a><span class="k">class</span> <span class="nc">FIFODequeWithLengthControl</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl-247"><a href="#FIFODequeWithLengthControl-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-248"><a href="#FIFODequeWithLengthControl-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="FIFODequeWithLengthControl-249"><a href="#FIFODequeWithLengthControl-249"><span class="linenos">249</span></a>
</span><span id="FIFODequeWithLengthControl-250"><a href="#FIFODequeWithLengthControl-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-251"><a href="#FIFODequeWithLengthControl-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl-252"><a href="#FIFODequeWithLengthControl-252"><span class="linenos">252</span></a>
</span><span id="FIFODequeWithLengthControl-253"><a href="#FIFODequeWithLengthControl-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="FIFODequeWithLengthControl-254"><a href="#FIFODequeWithLengthControl-254"><span class="linenos">254</span></a>
</span><span id="FIFODequeWithLengthControl-255"><a href="#FIFODequeWithLengthControl-255"><span class="linenos">255</span></a>        <span class="c1"># self._l_length = deque()</span>
</span><span id="FIFODequeWithLengthControl-256"><a href="#FIFODequeWithLengthControl-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl-257"><a href="#FIFODequeWithLengthControl-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-258"><a href="#FIFODequeWithLengthControl-258"><span class="linenos">258</span></a>
</span><span id="FIFODequeWithLengthControl-259"><a href="#FIFODequeWithLengthControl-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-260"><a href="#FIFODequeWithLengthControl-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-261"><a href="#FIFODequeWithLengthControl-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl-262"><a href="#FIFODequeWithLengthControl-262"><span class="linenos">262</span></a>
</span><span id="FIFODequeWithLengthControl-263"><a href="#FIFODequeWithLengthControl-263"><span class="linenos">263</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-264"><a href="#FIFODequeWithLengthControl-264"><span class="linenos">264</span></a>        <span class="c1"># self._l_length.append(data_size)</span>
</span><span id="FIFODequeWithLengthControl-265"><a href="#FIFODequeWithLengthControl-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFODequeWithLengthControl-266"><a href="#FIFODequeWithLengthControl-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFODequeWithLengthControl-267"><a href="#FIFODequeWithLengthControl-267"><span class="linenos">267</span></a>
</span><span id="FIFODequeWithLengthControl-268"><a href="#FIFODequeWithLengthControl-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-269"><a href="#FIFODequeWithLengthControl-269"><span class="linenos">269</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl-270"><a href="#FIFODequeWithLengthControl-270"><span class="linenos">270</span></a>        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">iterable_data</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl-271"><a href="#FIFODequeWithLengthControl-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-272"><a href="#FIFODequeWithLengthControl-272"><span class="linenos">272</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl-273"><a href="#FIFODequeWithLengthControl-273"><span class="linenos">273</span></a>            <span class="n">elem_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-274"><a href="#FIFODequeWithLengthControl-274"><span class="linenos">274</span></a>            <span class="c1"># self._l_length.append(elem_size)</span>
</span><span id="FIFODequeWithLengthControl-275"><a href="#FIFODequeWithLengthControl-275"><span class="linenos">275</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">elem_size</span>
</span><span id="FIFODequeWithLengthControl-276"><a href="#FIFODequeWithLengthControl-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFODequeWithLengthControl-277"><a href="#FIFODequeWithLengthControl-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFODequeWithLengthControl-278"><a href="#FIFODequeWithLengthControl-278"><span class="linenos">278</span></a>
</span><span id="FIFODequeWithLengthControl-279"><a href="#FIFODequeWithLengthControl-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-280"><a href="#FIFODequeWithLengthControl-280"><span class="linenos">280</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl-281"><a href="#FIFODequeWithLengthControl-281"><span class="linenos">281</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-282"><a href="#FIFODequeWithLengthControl-282"><span class="linenos">282</span></a>
</span><span id="FIFODequeWithLengthControl-283"><a href="#FIFODequeWithLengthControl-283"><span class="linenos">283</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-284"><a href="#FIFODequeWithLengthControl-284"><span class="linenos">284</span></a>        <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="FIFODequeWithLengthControl-285"><a href="#FIFODequeWithLengthControl-285"><span class="linenos">285</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-286"><a href="#FIFODequeWithLengthControl-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl-287"><a href="#FIFODequeWithLengthControl-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl-288"><a href="#FIFODequeWithLengthControl-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl-289"><a href="#FIFODequeWithLengthControl-289"><span class="linenos">289</span></a>
</span><span id="FIFODequeWithLengthControl-290"><a href="#FIFODequeWithLengthControl-290"><span class="linenos">290</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="FIFODequeWithLengthControl-291"><a href="#FIFODequeWithLengthControl-291"><span class="linenos">291</span></a>
</span><span id="FIFODequeWithLengthControl-292"><a href="#FIFODequeWithLengthControl-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">get_at_least_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-293"><a href="#FIFODequeWithLengthControl-293"><span class="linenos">293</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl-294"><a href="#FIFODequeWithLengthControl-294"><span class="linenos">294</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-295"><a href="#FIFODequeWithLengthControl-295"><span class="linenos">295</span></a>
</span><span id="FIFODequeWithLengthControl-296"><a href="#FIFODequeWithLengthControl-296"><span class="linenos">296</span></a>        <span class="n">result_data</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-297"><a href="#FIFODequeWithLengthControl-297"><span class="linenos">297</span></a>        <span class="n">result_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl-298"><a href="#FIFODequeWithLengthControl-298"><span class="linenos">298</span></a>        <span class="n">result_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl-299"><a href="#FIFODequeWithLengthControl-299"><span class="linenos">299</span></a>
</span><span id="FIFODequeWithLengthControl-300"><a href="#FIFODequeWithLengthControl-300"><span class="linenos">300</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="ow">and</span> <span class="p">(</span><span class="n">result_size</span> <span class="o">&lt;</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-301"><a href="#FIFODequeWithLengthControl-301"><span class="linenos">301</span></a>            <span class="n">another_piece</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-302"><a href="#FIFODequeWithLengthControl-302"><span class="linenos">302</span></a>            <span class="n">result_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-303"><a href="#FIFODequeWithLengthControl-303"><span class="linenos">303</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl-304"><a href="#FIFODequeWithLengthControl-304"><span class="linenos">304</span></a>            <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="FIFODequeWithLengthControl-305"><a href="#FIFODequeWithLengthControl-305"><span class="linenos">305</span></a>            <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-306"><a href="#FIFODequeWithLengthControl-306"><span class="linenos">306</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl-307"><a href="#FIFODequeWithLengthControl-307"><span class="linenos">307</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl-308"><a href="#FIFODequeWithLengthControl-308"><span class="linenos">308</span></a>            <span class="n">result_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl-309"><a href="#FIFODequeWithLengthControl-309"><span class="linenos">309</span></a>            <span class="n">result_qnt</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl-310"><a href="#FIFODequeWithLengthControl-310"><span class="linenos">310</span></a>
</span><span id="FIFODequeWithLengthControl-311"><a href="#FIFODequeWithLengthControl-311"><span class="linenos">311</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result_data</span><span class="p">,</span> <span class="n">result_size</span><span class="p">,</span> <span class="n">result_qnt</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-312"><a href="#FIFODequeWithLengthControl-312"><span class="linenos">312</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="FIFODequeWithLengthControl-313"><a href="#FIFODequeWithLengthControl-313"><span class="linenos">313</span></a>
</span><span id="FIFODequeWithLengthControl-314"><a href="#FIFODequeWithLengthControl-314"><span class="linenos">314</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-315"><a href="#FIFODequeWithLengthControl-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span><span id="FIFODequeWithLengthControl-316"><a href="#FIFODequeWithLengthControl-316"><span class="linenos">316</span></a>
</span><span id="FIFODequeWithLengthControl-317"><a href="#FIFODequeWithLengthControl-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-318"><a href="#FIFODequeWithLengthControl-318"><span class="linenos">318</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl-319"><a href="#FIFODequeWithLengthControl-319"><span class="linenos">319</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span><span id="FIFODequeWithLengthControl-320"><a href="#FIFODequeWithLengthControl-320"><span class="linenos">320</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="FIFODequeWithLengthControl-321"><a href="#FIFODequeWithLengthControl-321"><span class="linenos">321</span></a>
</span><span id="FIFODequeWithLengthControl-322"><a href="#FIFODequeWithLengthControl-322"><span class="linenos">322</span></a>    <span class="k">def</span> <span class="nf">__copy__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-323"><a href="#FIFODequeWithLengthControl-323"><span class="linenos">323</span></a>        <span class="k">return</span> <span class="n">FIFODequeWithLengthControl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl-324"><a href="#FIFODequeWithLengthControl-324"><span class="linenos">324</span></a>
</span><span id="FIFODequeWithLengthControl-325"><a href="#FIFODequeWithLengthControl-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-326"><a href="#FIFODequeWithLengthControl-326"><span class="linenos">326</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">remove</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl-327"><a href="#FIFODequeWithLengthControl-327"><span class="linenos">327</span></a>
</span><span id="FIFODequeWithLengthControl-328"><a href="#FIFODequeWithLengthControl-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-329"><a href="#FIFODequeWithLengthControl-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span><span id="FIFODequeWithLengthControl-330"><a href="#FIFODequeWithLengthControl-330"><span class="linenos">330</span></a>
</span><span id="FIFODequeWithLengthControl-331"><a href="#FIFODequeWithLengthControl-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl-332"><a href="#FIFODequeWithLengthControl-332"><span class="linenos">332</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span></pre></div>


    

                            <div id="FIFODequeWithLengthControl.__init__" class="classattr">
                                        <input id="FIFODequeWithLengthControl.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">FIFODequeWithLengthControl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">result_types</span><span class="o">.</span><span class="n">ResultExistence</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.__init__-247"><a href="#FIFODequeWithLengthControl.__init__-247"><span class="linenos">247</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">external_data_full_size</span><span class="p">:</span> <span class="n">ResultExistence</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.__init__-248"><a href="#FIFODequeWithLengthControl.__init__-248"><span class="linenos">248</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="FIFODequeWithLengthControl.__init__-249"><a href="#FIFODequeWithLengthControl.__init__-249"><span class="linenos">249</span></a>
</span><span id="FIFODequeWithLengthControl.__init__-250"><a href="#FIFODequeWithLengthControl.__init__-250"><span class="linenos">250</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.__init__-251"><a href="#FIFODequeWithLengthControl.__init__-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl.__init__-252"><a href="#FIFODequeWithLengthControl.__init__-252"><span class="linenos">252</span></a>
</span><span id="FIFODequeWithLengthControl.__init__-253"><a href="#FIFODequeWithLengthControl.__init__-253"><span class="linenos">253</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_init_param__external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span>
</span><span id="FIFODequeWithLengthControl.__init__-254"><a href="#FIFODequeWithLengthControl.__init__-254"><span class="linenos">254</span></a>
</span><span id="FIFODequeWithLengthControl.__init__-255"><a href="#FIFODequeWithLengthControl.__init__-255"><span class="linenos">255</span></a>        <span class="c1"># self._l_length = deque()</span>
</span><span id="FIFODequeWithLengthControl.__init__-256"><a href="#FIFODequeWithLengthControl.__init__-256"><span class="linenos">256</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl.__init__-257"><a href="#FIFODequeWithLengthControl.__init__-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span> <span class="o">=</span> <span class="n">external_data_full_size</span> <span class="ow">or</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.put" class="classattr">
                                        <input id="FIFODequeWithLengthControl.put-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">put</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.put-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.put"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.put-259"><a href="#FIFODequeWithLengthControl.put-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">put</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.put-260"><a href="#FIFODequeWithLengthControl.put-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.put-261"><a href="#FIFODequeWithLengthControl.put-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl.put-262"><a href="#FIFODequeWithLengthControl.put-262"><span class="linenos">262</span></a>
</span><span id="FIFODequeWithLengthControl.put-263"><a href="#FIFODequeWithLengthControl.put-263"><span class="linenos">263</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.put-264"><a href="#FIFODequeWithLengthControl.put-264"><span class="linenos">264</span></a>        <span class="c1"># self._l_length.append(data_size)</span>
</span><span id="FIFODequeWithLengthControl.put-265"><a href="#FIFODequeWithLengthControl.put-265"><span class="linenos">265</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">data_size</span>
</span><span id="FIFODequeWithLengthControl.put-266"><a href="#FIFODequeWithLengthControl.put-266"><span class="linenos">266</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">data_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.extend" class="classattr">
                                        <input id="FIFODequeWithLengthControl.extend-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">extend</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">iterable_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.extend-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.extend"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.extend-268"><a href="#FIFODequeWithLengthControl.extend-268"><span class="linenos">268</span></a>    <span class="k">def</span> <span class="nf">extend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterable_data</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.extend-269"><a href="#FIFODequeWithLengthControl.extend-269"><span class="linenos">269</span></a>        <span class="n">full_size_diff</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl.extend-270"><a href="#FIFODequeWithLengthControl.extend-270"><span class="linenos">270</span></a>        <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">iterable_data</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl.extend-271"><a href="#FIFODequeWithLengthControl.extend-271"><span class="linenos">271</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.extend-272"><a href="#FIFODequeWithLengthControl.extend-272"><span class="linenos">272</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl.extend-273"><a href="#FIFODequeWithLengthControl.extend-273"><span class="linenos">273</span></a>            <span class="n">elem_size</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">elem</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.extend-274"><a href="#FIFODequeWithLengthControl.extend-274"><span class="linenos">274</span></a>            <span class="c1"># self._l_length.append(elem_size)</span>
</span><span id="FIFODequeWithLengthControl.extend-275"><a href="#FIFODequeWithLengthControl.extend-275"><span class="linenos">275</span></a>            <span class="n">full_size_diff</span> <span class="o">+=</span> <span class="n">elem_size</span>
</span><span id="FIFODequeWithLengthControl.extend-276"><a href="#FIFODequeWithLengthControl.extend-276"><span class="linenos">276</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span><span id="FIFODequeWithLengthControl.extend-277"><a href="#FIFODequeWithLengthControl.extend-277"><span class="linenos">277</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">+=</span> <span class="n">full_size_diff</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.get" class="classattr">
                                        <input id="FIFODequeWithLengthControl.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.get-279"><a href="#FIFODequeWithLengthControl.get-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.get-280"><a href="#FIFODequeWithLengthControl.get-280"><span class="linenos">280</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl.get-281"><a href="#FIFODequeWithLengthControl.get-281"><span class="linenos">281</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.get-282"><a href="#FIFODequeWithLengthControl.get-282"><span class="linenos">282</span></a>
</span><span id="FIFODequeWithLengthControl.get-283"><a href="#FIFODequeWithLengthControl.get-283"><span class="linenos">283</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.get-284"><a href="#FIFODequeWithLengthControl.get-284"><span class="linenos">284</span></a>        <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="FIFODequeWithLengthControl.get-285"><a href="#FIFODequeWithLengthControl.get-285"><span class="linenos">285</span></a>        <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.get-286"><a href="#FIFODequeWithLengthControl.get-286"><span class="linenos">286</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl.get-287"><a href="#FIFODequeWithLengthControl.get-287"><span class="linenos">287</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl.get-288"><a href="#FIFODequeWithLengthControl.get-288"><span class="linenos">288</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl.get-289"><a href="#FIFODequeWithLengthControl.get-289"><span class="linenos">289</span></a>
</span><span id="FIFODequeWithLengthControl.get-290"><a href="#FIFODequeWithLengthControl.get-290"><span class="linenos">290</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.get_at_least_size" class="classattr">
                                        <input id="FIFODequeWithLengthControl.get_at_least_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_at_least_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">minimum_data_size</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.get_at_least_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.get_at_least_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.get_at_least_size-292"><a href="#FIFODequeWithLengthControl.get_at_least_size-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">get_at_least_size</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-293"><a href="#FIFODequeWithLengthControl.get_at_least_size-293"><span class="linenos">293</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-294"><a href="#FIFODequeWithLengthControl.get_at_least_size-294"><span class="linenos">294</span></a>            <span class="k">raise</span> <span class="n">FIFOIsEmpty</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-295"><a href="#FIFODequeWithLengthControl.get_at_least_size-295"><span class="linenos">295</span></a>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-296"><a href="#FIFODequeWithLengthControl.get_at_least_size-296"><span class="linenos">296</span></a>        <span class="n">result_data</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-297"><a href="#FIFODequeWithLengthControl.get_at_least_size-297"><span class="linenos">297</span></a>        <span class="n">result_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-298"><a href="#FIFODequeWithLengthControl.get_at_least_size-298"><span class="linenos">298</span></a>        <span class="n">result_qnt</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-299"><a href="#FIFODequeWithLengthControl.get_at_least_size-299"><span class="linenos">299</span></a>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-300"><a href="#FIFODequeWithLengthControl.get_at_least_size-300"><span class="linenos">300</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="ow">and</span> <span class="p">(</span><span class="n">result_size</span> <span class="o">&lt;</span> <span class="n">minimum_data_size</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-301"><a href="#FIFODequeWithLengthControl.get_at_least_size-301"><span class="linenos">301</span></a>            <span class="n">another_piece</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_l</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-302"><a href="#FIFODequeWithLengthControl.get_at_least_size-302"><span class="linenos">302</span></a>            <span class="n">result_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-303"><a href="#FIFODequeWithLengthControl.get_at_least_size-303"><span class="linenos">303</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-304"><a href="#FIFODequeWithLengthControl.get_at_least_size-304"><span class="linenos">304</span></a>            <span class="c1"># result_len = self._l_length.popleft()</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-305"><a href="#FIFODequeWithLengthControl.get_at_least_size-305"><span class="linenos">305</span></a>            <span class="n">result_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">another_piece</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-306"><a href="#FIFODequeWithLengthControl.get_at_least_size-306"><span class="linenos">306</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-307"><a href="#FIFODequeWithLengthControl.get_at_least_size-307"><span class="linenos">307</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-308"><a href="#FIFODequeWithLengthControl.get_at_least_size-308"><span class="linenos">308</span></a>            <span class="n">result_size</span> <span class="o">+=</span> <span class="n">result_len</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-309"><a href="#FIFODequeWithLengthControl.get_at_least_size-309"><span class="linenos">309</span></a>            <span class="n">result_qnt</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-310"><a href="#FIFODequeWithLengthControl.get_at_least_size-310"><span class="linenos">310</span></a>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-311"><a href="#FIFODequeWithLengthControl.get_at_least_size-311"><span class="linenos">311</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result_data</span><span class="p">,</span> <span class="n">result_size</span><span class="p">,</span> <span class="n">result_qnt</span><span class="p">)</span>
</span><span id="FIFODequeWithLengthControl.get_at_least_size-312"><a href="#FIFODequeWithLengthControl.get_at_least_size-312"><span class="linenos">312</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.get_data_full_size" class="classattr">
                                        <input id="FIFODequeWithLengthControl.get_data_full_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_data_full_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.get_data_full_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.get_data_full_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.get_data_full_size-314"><a href="#FIFODequeWithLengthControl.get_data_full_size-314"><span class="linenos">314</span></a>    <span class="k">def</span> <span class="nf">get_data_full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.get_data_full_size-315"><a href="#FIFODequeWithLengthControl.get_data_full_size-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.remove" class="classattr">
                                        <input id="FIFODequeWithLengthControl.remove-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.remove-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.remove"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.remove-317"><a href="#FIFODequeWithLengthControl.remove-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">remove</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.remove-318"><a href="#FIFODequeWithLengthControl.remove-318"><span class="linenos">318</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span><span class="p">:</span>
</span><span id="FIFODequeWithLengthControl.remove-319"><a href="#FIFODequeWithLengthControl.remove-319"><span class="linenos">319</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_external_data_full_size</span><span class="o">.</span><span class="n">result</span> <span class="o">-=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_data_full_size</span>
</span><span id="FIFODequeWithLengthControl.remove-320"><a href="#FIFODequeWithLengthControl.remove-320"><span class="linenos">320</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_removed</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.size" class="classattr">
                                        <input id="FIFODequeWithLengthControl.size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.size-328"><a href="#FIFODequeWithLengthControl.size-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.size-329"><a href="#FIFODequeWithLengthControl.size-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span></pre></div>


    

                            </div>
                            <div id="FIFODequeWithLengthControl.full_size" class="classattr">
                                        <input id="FIFODequeWithLengthControl.full_size-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">full_size</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="FIFODequeWithLengthControl.full_size-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#FIFODequeWithLengthControl.full_size"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="FIFODequeWithLengthControl.full_size-331"><a href="#FIFODequeWithLengthControl.full_size-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="nf">full_size</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="FIFODequeWithLengthControl.full_size-332"><a href="#FIFODequeWithLengthControl.full_size-332"><span class="linenos">332</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_real_size</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>