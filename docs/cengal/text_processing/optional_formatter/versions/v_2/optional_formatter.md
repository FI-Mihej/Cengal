---
title: optional_formatter
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.text_processing<wbr>.optional_formatter<wbr>.versions<wbr>.v_2<wbr>.optional_formatter    </h1>

                
                        <input id="mod-optional_formatter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-optional_formatter-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.args_manager</span> <span class="kn">import</span> <span class="n">ArgsKwargs</span><span class="p">,</span> <span class="n">AK</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">AnyStr</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Sequence</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="sd">Module Docstring</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.1.1&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">ItemTemplate</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s2">&quot;ItemTemplate&quot;</span><span class="p">,</span> <span class="s2">&quot;l_delimiter, prefix, template, postfix, r_delimiter&quot;</span><span class="p">,</span> <span class="n">defaults</span><span class="o">=</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s1">&#39;</span><span class="si">{}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">))</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">IT</span> <span class="o">=</span> <span class="n">ItemTemplate</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">OptionalFormatter</span><span class="p">:</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_positions</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>                 <span class="n">template_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_item_positions</span> <span class="o">=</span> <span class="n">item_positions</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_template_per_item</span> <span class="o">=</span> <span class="n">template_per_item</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arguments_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">AK</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>        <span class="n">is_first</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>        <span class="n">last_postfix</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="n">last_r_delimiter</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_item_positions</span><span class="p">:</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>            <span class="k">if</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">arguments_per_item</span><span class="p">:</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>                <span class="n">item_l_delimiter</span><span class="p">,</span> <span class="n">item_prefix</span><span class="p">,</span> <span class="n">item_template</span><span class="p">,</span> <span class="n">item_postfix</span><span class="p">,</span> <span class="n">item_r_delimiter</span> <span class="o">=</span> \
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_template_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>                <span class="n">item_args_kwargs</span> <span class="o">=</span> <span class="n">arguments_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item_args_kwargs</span><span class="p">,</span> <span class="n">AK</span><span class="p">):</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>                    <span class="n">item_args</span><span class="p">,</span> <span class="n">item_kwargs</span> <span class="o">=</span> <span class="n">arguments_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]()</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>                    <span class="n">item_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">item_args_kwargs</span><span class="p">,)</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>                    <span class="n">item_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>                
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>                <span class="n">rendered_item</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>                <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_prefix</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">last_r_delimiter</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_l_delimiter</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>                
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>                <span class="n">last_r_delimiter</span> <span class="o">=</span> <span class="n">item_r_delimiter</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>                <span class="n">last_postfix</span> <span class="o">=</span> <span class="n">item_postfix</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>                <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">item_args</span><span class="p">,</span> <span class="o">**</span><span class="n">item_kwargs</span><span class="p">)</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>                <span class="n">result</span> <span class="o">+=</span> <span class="n">rendered_item</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>                <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>                    <span class="n">is_first</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>                
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="n">result</span> <span class="o">+=</span> <span class="n">last_postfix</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="k">class</span> <span class="nc">OptionalFormatterHandy</span><span class="p">(</span><span class="n">OptionalFormatter</span><span class="p">):</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="sd">    template_per_item second tuple format:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="sd">    [left_delimiter(shown if not first), prefix(shown if first), template, postfix(shown if last), right_delimiter(shown if not last)]</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="sd">    Example 1:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="sd">        f = OptionalFormatterHandy(&#39;hour&#39;, &#39;part_of_day&#39;, &#39;minute&#39;, &#39;second&#39;, &#39;millisecond&#39;,</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">                                   hour=IT(&#39;&#39;, &#39;|(hours)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="sd">                                   part_of_day=IT(&#39;-&#39;, &#39;|(part_of_day)&#39;, &#39;&lt;{}.{second}&gt;&#39;, &#39;|&#39;),</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">                                   minutes=IT(&#39;:&#39;, &#39;|(minutes)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">                                   seconds=IT(&#39;:&#39;, &#39;|(seconds)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">                                   millisecond=IT(&#39;.&#39;, &#39;|(millisecond)&#39;, &#39;{}&#39;, &#39;|&#39;))</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="sd">        f(hour=4, minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="sd">        &gt;&gt; |(hours)4:15:54.341|</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="sd">        f(seconds=54, minutes=15, hour=0, millisecond=0)</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="sd">        &gt;&gt; |(hours)0:15:54.0|</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">        f(minutes=15, seconds=54)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="sd">        &gt;&gt; |(minutes)15:54|</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="sd">        f(hour=4, part_of_day=AK(&#39;a&#39;, second=&#39;m&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="sd">        &gt;&gt; |(hours)4-&lt;a.m&gt;:15:54.341|</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="sd">        f(part_of_day=AK(&#39;a&#39;, second=&#39;m&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="sd">        &gt;&gt; |(part_of_day)&lt;a.m&gt;:15:54.341|</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">        </span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">    Example 2:</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="sd">        f = OptionalFormatterHandy(&#39;hour&#39;, &#39;word&#39;, &#39;minute&#39;, &#39;second&#39;, &#39;millisecond&#39;,</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="sd">                                   hour=(&#39;&#39;, &#39;|(hours)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="sd">                                   word=(&#39;&#39;, &#39;|(word)&#39;, &#39;-&lt;&quot;{}&quot;-&quot;{second}&quot;&gt;-&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="sd">                                   minutes=(&#39;:&#39;, &#39;|(minutes)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">                                   seconds=(&#39;:&#39;, &#39;|(seconds)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">                                   millisecond=(&#39;.&#39;, &#39;|(millisecond)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;))</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">        f(hour=4, minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">        &gt;&gt; |(hours)4:15:54.341|</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">        f(seconds=54, minutes=15, hour=0, millisecond=0)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">        &gt;&gt; |(hours)0:15:54.0|</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="sd">        f(minutes=15, seconds=54)</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="sd">        &gt;&gt; |(minutes)15:54|</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="sd">        f(hour=4, word=AK(&#39;HELLO!&#39;, second=&#39;WORLD!&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="sd">        &gt;&gt; |(hours)4-&lt;&quot;HELLO!&quot;-&quot;WORLD!&quot;&gt;-:15:54.341|</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">        f(word=AK(&#39;HELLO!&#39;, second=&#39;WORLD!&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="sd">        &gt;&gt; |(word)-&lt;&quot;HELLO!&quot;-&quot;WORLD!&quot;&gt;-:15:54.341|</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">item_positions</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span> <span class="o">**</span><span class="n">template_per_item</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">item_positions</span><span class="p">,</span> <span class="n">template_per_item</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">arguments_per_item</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">AK</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">(</span><span class="n">OptionalFormatterHandy</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">arguments_per_item</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="ItemTemplate">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ItemTemplate</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#ItemTemplate"></a>
    
            <div class="docstring"><p>ItemTemplate(l_delimiter, prefix, template, postfix, r_delimiter)</p>
</div>


                            <div id="ItemTemplate.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">ItemTemplate</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">l_delimiter</span><span class="o">=</span><span class="s1">&#39;&#39;</span>, </span><span class="param"><span class="n">prefix</span><span class="o">=</span><span class="s1">&#39;&#39;</span>, </span><span class="param"><span class="n">template</span><span class="o">=</span><span class="s1">&#39;</span><span class="si">{}</span><span class="s1">&#39;</span>, </span><span class="param"><span class="n">postfix</span><span class="o">=</span><span class="s1">&#39;&#39;</span>, </span><span class="param"><span class="n">r_delimiter</span><span class="o">=</span><span class="s1">&#39;&#39;</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.__init__"></a>
    
            <div class="docstring"><p>Create new instance of ItemTemplate(l_delimiter, prefix, template, postfix, r_delimiter)</p>
</div>


                            </div>
                            <div id="ItemTemplate.l_delimiter" class="classattr">
                                <div class="attr variable">
            <span class="name">l_delimiter</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.l_delimiter"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="ItemTemplate.prefix" class="classattr">
                                <div class="attr variable">
            <span class="name">prefix</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.prefix"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div id="ItemTemplate.template" class="classattr">
                                <div class="attr variable">
            <span class="name">template</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.template"></a>
    
            <div class="docstring"><p>Alias for field number 2</p>
</div>


                            </div>
                            <div id="ItemTemplate.postfix" class="classattr">
                                <div class="attr variable">
            <span class="name">postfix</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.postfix"></a>
    
            <div class="docstring"><p>Alias for field number 3</p>
</div>


                            </div>
                            <div id="ItemTemplate.r_delimiter" class="classattr">
                                <div class="attr variable">
            <span class="name">r_delimiter</span>

        
    </div>
    <a class="headerlink" href="#ItemTemplate.r_delimiter"></a>
    
            <div class="docstring"><p>Alias for field number 4</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="ItemTemplate.index" class="function">index</dd>
                <dd id="ItemTemplate.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IT">
                    <div class="attr variable">
            <span class="name">IT</span>        =
<span class="default_value">&lt;class &#39;<a href="#ItemTemplate">ItemTemplate</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#IT"></a>
    
    

                </section>
                <section id="OptionalFormatter">
                            <input id="OptionalFormatter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">OptionalFormatter</span>:

                <label class="view-source-button" for="OptionalFormatter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OptionalFormatter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OptionalFormatter-45"><a href="#OptionalFormatter-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">OptionalFormatter</span><span class="p">:</span>
</span><span id="OptionalFormatter-46"><a href="#OptionalFormatter-46"><span class="linenos">46</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_positions</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span>
</span><span id="OptionalFormatter-47"><a href="#OptionalFormatter-47"><span class="linenos">47</span></a>                 <span class="n">template_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="OptionalFormatter-48"><a href="#OptionalFormatter-48"><span class="linenos">48</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_item_positions</span> <span class="o">=</span> <span class="n">item_positions</span>
</span><span id="OptionalFormatter-49"><a href="#OptionalFormatter-49"><span class="linenos">49</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_template_per_item</span> <span class="o">=</span> <span class="n">template_per_item</span>
</span><span id="OptionalFormatter-50"><a href="#OptionalFormatter-50"><span class="linenos">50</span></a>
</span><span id="OptionalFormatter-51"><a href="#OptionalFormatter-51"><span class="linenos">51</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arguments_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">AK</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="OptionalFormatter-52"><a href="#OptionalFormatter-52"><span class="linenos">52</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="OptionalFormatter-53"><a href="#OptionalFormatter-53"><span class="linenos">53</span></a>        <span class="n">is_first</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="OptionalFormatter-54"><a href="#OptionalFormatter-54"><span class="linenos">54</span></a>        <span class="n">last_postfix</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="OptionalFormatter-55"><a href="#OptionalFormatter-55"><span class="linenos">55</span></a>        <span class="n">last_r_delimiter</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="OptionalFormatter-56"><a href="#OptionalFormatter-56"><span class="linenos">56</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_item_positions</span><span class="p">:</span>
</span><span id="OptionalFormatter-57"><a href="#OptionalFormatter-57"><span class="linenos">57</span></a>            <span class="k">if</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">arguments_per_item</span><span class="p">:</span>
</span><span id="OptionalFormatter-58"><a href="#OptionalFormatter-58"><span class="linenos">58</span></a>                <span class="n">item_l_delimiter</span><span class="p">,</span> <span class="n">item_prefix</span><span class="p">,</span> <span class="n">item_template</span><span class="p">,</span> <span class="n">item_postfix</span><span class="p">,</span> <span class="n">item_r_delimiter</span> <span class="o">=</span> \
</span><span id="OptionalFormatter-59"><a href="#OptionalFormatter-59"><span class="linenos">59</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_template_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span>
</span><span id="OptionalFormatter-60"><a href="#OptionalFormatter-60"><span class="linenos">60</span></a>                <span class="n">item_args_kwargs</span> <span class="o">=</span> <span class="n">arguments_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]</span>
</span><span id="OptionalFormatter-61"><a href="#OptionalFormatter-61"><span class="linenos">61</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item_args_kwargs</span><span class="p">,</span> <span class="n">AK</span><span class="p">):</span>
</span><span id="OptionalFormatter-62"><a href="#OptionalFormatter-62"><span class="linenos">62</span></a>                    <span class="n">item_args</span><span class="p">,</span> <span class="n">item_kwargs</span> <span class="o">=</span> <span class="n">arguments_per_item</span><span class="p">[</span><span class="n">item</span><span class="p">]()</span>
</span><span id="OptionalFormatter-63"><a href="#OptionalFormatter-63"><span class="linenos">63</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="OptionalFormatter-64"><a href="#OptionalFormatter-64"><span class="linenos">64</span></a>                    <span class="n">item_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">item_args_kwargs</span><span class="p">,)</span>
</span><span id="OptionalFormatter-65"><a href="#OptionalFormatter-65"><span class="linenos">65</span></a>                    <span class="n">item_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="OptionalFormatter-66"><a href="#OptionalFormatter-66"><span class="linenos">66</span></a>                
</span><span id="OptionalFormatter-67"><a href="#OptionalFormatter-67"><span class="linenos">67</span></a>                <span class="n">rendered_item</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="OptionalFormatter-68"><a href="#OptionalFormatter-68"><span class="linenos">68</span></a>                <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
</span><span id="OptionalFormatter-69"><a href="#OptionalFormatter-69"><span class="linenos">69</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_prefix</span>
</span><span id="OptionalFormatter-70"><a href="#OptionalFormatter-70"><span class="linenos">70</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="OptionalFormatter-71"><a href="#OptionalFormatter-71"><span class="linenos">71</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">last_r_delimiter</span>
</span><span id="OptionalFormatter-72"><a href="#OptionalFormatter-72"><span class="linenos">72</span></a>                    <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_l_delimiter</span>
</span><span id="OptionalFormatter-73"><a href="#OptionalFormatter-73"><span class="linenos">73</span></a>                
</span><span id="OptionalFormatter-74"><a href="#OptionalFormatter-74"><span class="linenos">74</span></a>                <span class="n">last_r_delimiter</span> <span class="o">=</span> <span class="n">item_r_delimiter</span>
</span><span id="OptionalFormatter-75"><a href="#OptionalFormatter-75"><span class="linenos">75</span></a>                <span class="n">last_postfix</span> <span class="o">=</span> <span class="n">item_postfix</span>
</span><span id="OptionalFormatter-76"><a href="#OptionalFormatter-76"><span class="linenos">76</span></a>                <span class="n">rendered_item</span> <span class="o">+=</span> <span class="n">item_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">item_args</span><span class="p">,</span> <span class="o">**</span><span class="n">item_kwargs</span><span class="p">)</span>
</span><span id="OptionalFormatter-77"><a href="#OptionalFormatter-77"><span class="linenos">77</span></a>                <span class="n">result</span> <span class="o">+=</span> <span class="n">rendered_item</span>
</span><span id="OptionalFormatter-78"><a href="#OptionalFormatter-78"><span class="linenos">78</span></a>                <span class="k">if</span> <span class="n">is_first</span><span class="p">:</span>
</span><span id="OptionalFormatter-79"><a href="#OptionalFormatter-79"><span class="linenos">79</span></a>                    <span class="n">is_first</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="OptionalFormatter-80"><a href="#OptionalFormatter-80"><span class="linenos">80</span></a>                
</span><span id="OptionalFormatter-81"><a href="#OptionalFormatter-81"><span class="linenos">81</span></a>        <span class="n">result</span> <span class="o">+=</span> <span class="n">last_postfix</span>
</span><span id="OptionalFormatter-82"><a href="#OptionalFormatter-82"><span class="linenos">82</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="OptionalFormatter.__init__" class="classattr">
                                        <input id="OptionalFormatter.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">OptionalFormatter</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">item_positions</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="o">...</span><span class="p">]</span>,</span><span class="param">	<span class="n">template_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#ItemTemplate">ItemTemplate</a></span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]</span></span>)</span>

                <label class="view-source-button" for="OptionalFormatter.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OptionalFormatter.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OptionalFormatter.__init__-46"><a href="#OptionalFormatter.__init__-46"><span class="linenos">46</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_positions</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span>
</span><span id="OptionalFormatter.__init__-47"><a href="#OptionalFormatter.__init__-47"><span class="linenos">47</span></a>                 <span class="n">template_per_item</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="OptionalFormatter.__init__-48"><a href="#OptionalFormatter.__init__-48"><span class="linenos">48</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_item_positions</span> <span class="o">=</span> <span class="n">item_positions</span>
</span><span id="OptionalFormatter.__init__-49"><a href="#OptionalFormatter.__init__-49"><span class="linenos">49</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_template_per_item</span> <span class="o">=</span> <span class="n">template_per_item</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="OptionalFormatterHandy">
                            <input id="OptionalFormatterHandy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">OptionalFormatterHandy</span><wbr>(<span class="base"><a href="#OptionalFormatter">OptionalFormatter</a></span>):

                <label class="view-source-button" for="OptionalFormatterHandy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OptionalFormatterHandy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OptionalFormatterHandy-85"><a href="#OptionalFormatterHandy-85"><span class="linenos"> 85</span></a><span class="k">class</span> <span class="nc">OptionalFormatterHandy</span><span class="p">(</span><span class="n">OptionalFormatter</span><span class="p">):</span>
</span><span id="OptionalFormatterHandy-86"><a href="#OptionalFormatterHandy-86"><span class="linenos"> 86</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="OptionalFormatterHandy-87"><a href="#OptionalFormatterHandy-87"><span class="linenos"> 87</span></a><span class="sd">    template_per_item second tuple format:</span>
</span><span id="OptionalFormatterHandy-88"><a href="#OptionalFormatterHandy-88"><span class="linenos"> 88</span></a><span class="sd">    [left_delimiter(shown if not first), prefix(shown if first), template, postfix(shown if last), right_delimiter(shown if not last)]</span>
</span><span id="OptionalFormatterHandy-89"><a href="#OptionalFormatterHandy-89"><span class="linenos"> 89</span></a>
</span><span id="OptionalFormatterHandy-90"><a href="#OptionalFormatterHandy-90"><span class="linenos"> 90</span></a>
</span><span id="OptionalFormatterHandy-91"><a href="#OptionalFormatterHandy-91"><span class="linenos"> 91</span></a><span class="sd">    Example 1:</span>
</span><span id="OptionalFormatterHandy-92"><a href="#OptionalFormatterHandy-92"><span class="linenos"> 92</span></a><span class="sd">        f = OptionalFormatterHandy(&#39;hour&#39;, &#39;part_of_day&#39;, &#39;minute&#39;, &#39;second&#39;, &#39;millisecond&#39;,</span>
</span><span id="OptionalFormatterHandy-93"><a href="#OptionalFormatterHandy-93"><span class="linenos"> 93</span></a><span class="sd">                                   hour=IT(&#39;&#39;, &#39;|(hours)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="OptionalFormatterHandy-94"><a href="#OptionalFormatterHandy-94"><span class="linenos"> 94</span></a><span class="sd">                                   part_of_day=IT(&#39;-&#39;, &#39;|(part_of_day)&#39;, &#39;&lt;{}.{second}&gt;&#39;, &#39;|&#39;),</span>
</span><span id="OptionalFormatterHandy-95"><a href="#OptionalFormatterHandy-95"><span class="linenos"> 95</span></a><span class="sd">                                   minutes=IT(&#39;:&#39;, &#39;|(minutes)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="OptionalFormatterHandy-96"><a href="#OptionalFormatterHandy-96"><span class="linenos"> 96</span></a><span class="sd">                                   seconds=IT(&#39;:&#39;, &#39;|(seconds)&#39;, &#39;{}&#39;, &#39;|&#39;),</span>
</span><span id="OptionalFormatterHandy-97"><a href="#OptionalFormatterHandy-97"><span class="linenos"> 97</span></a><span class="sd">                                   millisecond=IT(&#39;.&#39;, &#39;|(millisecond)&#39;, &#39;{}&#39;, &#39;|&#39;))</span>
</span><span id="OptionalFormatterHandy-98"><a href="#OptionalFormatterHandy-98"><span class="linenos"> 98</span></a>
</span><span id="OptionalFormatterHandy-99"><a href="#OptionalFormatterHandy-99"><span class="linenos"> 99</span></a><span class="sd">        f(hour=4, minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-100"><a href="#OptionalFormatterHandy-100"><span class="linenos">100</span></a><span class="sd">        &gt;&gt; |(hours)4:15:54.341|</span>
</span><span id="OptionalFormatterHandy-101"><a href="#OptionalFormatterHandy-101"><span class="linenos">101</span></a>
</span><span id="OptionalFormatterHandy-102"><a href="#OptionalFormatterHandy-102"><span class="linenos">102</span></a><span class="sd">        f(seconds=54, minutes=15, hour=0, millisecond=0)</span>
</span><span id="OptionalFormatterHandy-103"><a href="#OptionalFormatterHandy-103"><span class="linenos">103</span></a><span class="sd">        &gt;&gt; |(hours)0:15:54.0|</span>
</span><span id="OptionalFormatterHandy-104"><a href="#OptionalFormatterHandy-104"><span class="linenos">104</span></a>
</span><span id="OptionalFormatterHandy-105"><a href="#OptionalFormatterHandy-105"><span class="linenos">105</span></a><span class="sd">        f(minutes=15, seconds=54)</span>
</span><span id="OptionalFormatterHandy-106"><a href="#OptionalFormatterHandy-106"><span class="linenos">106</span></a><span class="sd">        &gt;&gt; |(minutes)15:54|</span>
</span><span id="OptionalFormatterHandy-107"><a href="#OptionalFormatterHandy-107"><span class="linenos">107</span></a>
</span><span id="OptionalFormatterHandy-108"><a href="#OptionalFormatterHandy-108"><span class="linenos">108</span></a><span class="sd">        f(hour=4, part_of_day=AK(&#39;a&#39;, second=&#39;m&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-109"><a href="#OptionalFormatterHandy-109"><span class="linenos">109</span></a><span class="sd">        &gt;&gt; |(hours)4-&lt;a.m&gt;:15:54.341|</span>
</span><span id="OptionalFormatterHandy-110"><a href="#OptionalFormatterHandy-110"><span class="linenos">110</span></a>
</span><span id="OptionalFormatterHandy-111"><a href="#OptionalFormatterHandy-111"><span class="linenos">111</span></a><span class="sd">        f(part_of_day=AK(&#39;a&#39;, second=&#39;m&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-112"><a href="#OptionalFormatterHandy-112"><span class="linenos">112</span></a><span class="sd">        &gt;&gt; |(part_of_day)&lt;a.m&gt;:15:54.341|</span>
</span><span id="OptionalFormatterHandy-113"><a href="#OptionalFormatterHandy-113"><span class="linenos">113</span></a>
</span><span id="OptionalFormatterHandy-114"><a href="#OptionalFormatterHandy-114"><span class="linenos">114</span></a><span class="sd">        </span>
</span><span id="OptionalFormatterHandy-115"><a href="#OptionalFormatterHandy-115"><span class="linenos">115</span></a><span class="sd">    Example 2:</span>
</span><span id="OptionalFormatterHandy-116"><a href="#OptionalFormatterHandy-116"><span class="linenos">116</span></a><span class="sd">        f = OptionalFormatterHandy(&#39;hour&#39;, &#39;word&#39;, &#39;minute&#39;, &#39;second&#39;, &#39;millisecond&#39;,</span>
</span><span id="OptionalFormatterHandy-117"><a href="#OptionalFormatterHandy-117"><span class="linenos">117</span></a><span class="sd">                                   hour=(&#39;&#39;, &#39;|(hours)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="OptionalFormatterHandy-118"><a href="#OptionalFormatterHandy-118"><span class="linenos">118</span></a><span class="sd">                                   word=(&#39;&#39;, &#39;|(word)&#39;, &#39;-&lt;&quot;{}&quot;-&quot;{second}&quot;&gt;-&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="OptionalFormatterHandy-119"><a href="#OptionalFormatterHandy-119"><span class="linenos">119</span></a><span class="sd">                                   minutes=(&#39;:&#39;, &#39;|(minutes)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="OptionalFormatterHandy-120"><a href="#OptionalFormatterHandy-120"><span class="linenos">120</span></a><span class="sd">                                   seconds=(&#39;:&#39;, &#39;|(seconds)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;),</span>
</span><span id="OptionalFormatterHandy-121"><a href="#OptionalFormatterHandy-121"><span class="linenos">121</span></a><span class="sd">                                   millisecond=(&#39;.&#39;, &#39;|(millisecond)&#39;, &#39;{}&#39;, &#39;|&#39;, &#39;&#39;))</span>
</span><span id="OptionalFormatterHandy-122"><a href="#OptionalFormatterHandy-122"><span class="linenos">122</span></a>
</span><span id="OptionalFormatterHandy-123"><a href="#OptionalFormatterHandy-123"><span class="linenos">123</span></a><span class="sd">        f(hour=4, minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-124"><a href="#OptionalFormatterHandy-124"><span class="linenos">124</span></a><span class="sd">        &gt;&gt; |(hours)4:15:54.341|</span>
</span><span id="OptionalFormatterHandy-125"><a href="#OptionalFormatterHandy-125"><span class="linenos">125</span></a>
</span><span id="OptionalFormatterHandy-126"><a href="#OptionalFormatterHandy-126"><span class="linenos">126</span></a><span class="sd">        f(seconds=54, minutes=15, hour=0, millisecond=0)</span>
</span><span id="OptionalFormatterHandy-127"><a href="#OptionalFormatterHandy-127"><span class="linenos">127</span></a><span class="sd">        &gt;&gt; |(hours)0:15:54.0|</span>
</span><span id="OptionalFormatterHandy-128"><a href="#OptionalFormatterHandy-128"><span class="linenos">128</span></a>
</span><span id="OptionalFormatterHandy-129"><a href="#OptionalFormatterHandy-129"><span class="linenos">129</span></a><span class="sd">        f(minutes=15, seconds=54)</span>
</span><span id="OptionalFormatterHandy-130"><a href="#OptionalFormatterHandy-130"><span class="linenos">130</span></a><span class="sd">        &gt;&gt; |(minutes)15:54|</span>
</span><span id="OptionalFormatterHandy-131"><a href="#OptionalFormatterHandy-131"><span class="linenos">131</span></a>
</span><span id="OptionalFormatterHandy-132"><a href="#OptionalFormatterHandy-132"><span class="linenos">132</span></a><span class="sd">        f(hour=4, word=AK(&#39;HELLO!&#39;, second=&#39;WORLD!&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-133"><a href="#OptionalFormatterHandy-133"><span class="linenos">133</span></a><span class="sd">        &gt;&gt; |(hours)4-&lt;&quot;HELLO!&quot;-&quot;WORLD!&quot;&gt;-:15:54.341|</span>
</span><span id="OptionalFormatterHandy-134"><a href="#OptionalFormatterHandy-134"><span class="linenos">134</span></a>
</span><span id="OptionalFormatterHandy-135"><a href="#OptionalFormatterHandy-135"><span class="linenos">135</span></a><span class="sd">        f(word=AK(&#39;HELLO!&#39;, second=&#39;WORLD!&#39;), minutes=15, seconds=54, millisecond=341)</span>
</span><span id="OptionalFormatterHandy-136"><a href="#OptionalFormatterHandy-136"><span class="linenos">136</span></a><span class="sd">        &gt;&gt; |(word)-&lt;&quot;HELLO!&quot;-&quot;WORLD!&quot;&gt;-:15:54.341|</span>
</span><span id="OptionalFormatterHandy-137"><a href="#OptionalFormatterHandy-137"><span class="linenos">137</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="OptionalFormatterHandy-138"><a href="#OptionalFormatterHandy-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">item_positions</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span> <span class="o">**</span><span class="n">template_per_item</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="OptionalFormatterHandy-139"><a href="#OptionalFormatterHandy-139"><span class="linenos">139</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">item_positions</span><span class="p">,</span> <span class="n">template_per_item</span><span class="p">)</span>
</span><span id="OptionalFormatterHandy-140"><a href="#OptionalFormatterHandy-140"><span class="linenos">140</span></a>
</span><span id="OptionalFormatterHandy-141"><a href="#OptionalFormatterHandy-141"><span class="linenos">141</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">**</span><span class="n">arguments_per_item</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">AK</span><span class="p">,</span> <span class="n">Any</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="OptionalFormatterHandy-142"><a href="#OptionalFormatterHandy-142"><span class="linenos">142</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">(</span><span class="n">OptionalFormatterHandy</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">arguments_per_item</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>template_per_item second tuple format:
[left_delimiter(shown if not first), prefix(shown if first), template, postfix(shown if last), right_delimiter(shown if not last)]</p>

<p>Example 1:
    f = OptionalFormatterHandy('hour', 'part_of_day', 'minute', 'second', 'millisecond',
                               hour=IT('', '|(hours)', '{}', '|'),
                               part_of_day=IT('-', '|(part_of_day)', '&lt;{}.{second}&gt;', '|'),
                               minutes=IT(':', '|(minutes)', '{}', '|'),
                               seconds=IT(':', '|(seconds)', '{}', '|'),
                               millisecond=IT('.', '|(millisecond)', '{}', '|'))</p>

<pre><code>f(hour=4, minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(hours)4:15:54.341|

f(seconds=54, minutes=15, hour=0, millisecond=0)
&gt;&gt; |(hours)0:15:54.0|

f(minutes=15, seconds=54)
&gt;&gt; |(minutes)15:54|

f(hour=4, part_of_day=AK('a', second='m'), minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(hours)4-&lt;a.m&gt;:15:54.341|

f(part_of_day=AK('a', second='m'), minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(part_of_day)&lt;a.m&gt;:15:54.341|
</code></pre>

<p>Example 2:
    f = OptionalFormatterHandy('hour', 'word', 'minute', 'second', 'millisecond',
                               hour=('', '|(hours)', '{}', '|', ''),
                               word=('', '|(word)', '-&lt;"{}"-"{second}">-', '|', ''),
                               minutes=(':', '|(minutes)', '{}', '|', ''),
                               seconds=(':', '|(seconds)', '{}', '|', ''),
                               millisecond=('.', '|(millisecond)', '{}', '|', ''))</p>

<pre><code>f(hour=4, minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(hours)4:15:54.341|

f(seconds=54, minutes=15, hour=0, millisecond=0)
&gt;&gt; |(hours)0:15:54.0|

f(minutes=15, seconds=54)
&gt;&gt; |(minutes)15:54|

f(hour=4, word=AK('HELLO!', second='WORLD!'), minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(hours)4-&lt;"HELLO!"-"WORLD!"&gt;-:15:54.341|

f(word=AK('HELLO!', second='WORLD!'), minutes=15, seconds=54, millisecond=341)
&gt;&gt; |(word)-&lt;"HELLO!"-"WORLD!"&gt;-:15:54.341|
</code></pre>
</div>


                            <div id="OptionalFormatterHandy.__init__" class="classattr">
                                        <input id="OptionalFormatterHandy.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">OptionalFormatterHandy</span><span class="signature pdoc-code multiline">(<span class="param">	*item_positions: [&lt;class &#x27;str&#x27;&gt;, Ellipsis],</span><span class="param">	**template_per_item: [&lt;class &#x27;str&#x27;&gt;, typing.Union[<a href="#ItemTemplate">ItemTemplate</a>, typing.Tuple[str, str, str, str, str]]]</span>)</span>

                <label class="view-source-button" for="OptionalFormatterHandy.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OptionalFormatterHandy.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OptionalFormatterHandy.__init__-138"><a href="#OptionalFormatterHandy.__init__-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">item_positions</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="o">...</span><span class="p">],</span> <span class="o">**</span><span class="n">template_per_item</span><span class="p">:</span> <span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="n">IT</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]]):</span>
</span><span id="OptionalFormatterHandy.__init__-139"><a href="#OptionalFormatterHandy.__init__-139"><span class="linenos">139</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">item_positions</span><span class="p">,</span> <span class="n">template_per_item</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>