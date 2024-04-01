---
title: smart_values
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.smart_values<wbr>.versions<wbr>.v_1<wbr>.smart_values    </h1>

                
                        <input id="mod-smart_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-smart_values-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span>
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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="k">class</span> <span class="nc">ValueExistence</span><span class="p">:</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;existence&#39;</span><span class="p">,</span> <span class="s1">&#39;result&#39;</span><span class="p">)</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>        <span class="k">return</span> <span class="s1">&#39;ValueExistence(</span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="k">class</span> <span class="nc">ValueCache</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ValueCache</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_result</span><span class="p">):</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">new_result</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="k">class</span> <span class="nc">ValueType</span><span class="p">:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;result&#39;</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the result&quot;</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueType</span><span class="p">):</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">state</span>
</span></pre></div>


            </section>
                <section id="ValueExistence">
                            <input id="ValueExistence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueExistence</span>:

                <label class="view-source-button" for="ValueExistence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence-38"><a href="#ValueExistence-38"><span class="linenos">38</span></a><span class="k">class</span> <span class="nc">ValueExistence</span><span class="p">:</span>
</span><span id="ValueExistence-39"><a href="#ValueExistence-39"><span class="linenos">39</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;existence&#39;</span><span class="p">,</span> <span class="s1">&#39;result&#39;</span><span class="p">)</span>
</span><span id="ValueExistence-40"><a href="#ValueExistence-40"><span class="linenos">40</span></a>
</span><span id="ValueExistence-41"><a href="#ValueExistence-41"><span class="linenos">41</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="ValueExistence-42"><a href="#ValueExistence-42"><span class="linenos">42</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence-43"><a href="#ValueExistence-43"><span class="linenos">43</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="ValueExistence-44"><a href="#ValueExistence-44"><span class="linenos">44</span></a>
</span><span id="ValueExistence-45"><a href="#ValueExistence-45"><span class="linenos">45</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-46"><a href="#ValueExistence-46"><span class="linenos">46</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="ValueExistence-47"><a href="#ValueExistence-47"><span class="linenos">47</span></a>
</span><span id="ValueExistence-48"><a href="#ValueExistence-48"><span class="linenos">48</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-49"><a href="#ValueExistence-49"><span class="linenos">49</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="ValueExistence-50"><a href="#ValueExistence-50"><span class="linenos">50</span></a>
</span><span id="ValueExistence-51"><a href="#ValueExistence-51"><span class="linenos">51</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-52"><a href="#ValueExistence-52"><span class="linenos">52</span></a>        <span class="k">return</span> <span class="s1">&#39;ValueExistence(</span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="ValueExistence-53"><a href="#ValueExistence-53"><span class="linenos">53</span></a>
</span><span id="ValueExistence-54"><a href="#ValueExistence-54"><span class="linenos">54</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-55"><a href="#ValueExistence-55"><span class="linenos">55</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="ValueExistence-56"><a href="#ValueExistence-56"><span class="linenos">56</span></a>
</span><span id="ValueExistence-57"><a href="#ValueExistence-57"><span class="linenos">57</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueExistence-58"><a href="#ValueExistence-58"><span class="linenos">58</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueExistence-59"><a href="#ValueExistence-59"><span class="linenos">59</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueExistence-60"><a href="#ValueExistence-60"><span class="linenos">60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence-61"><a href="#ValueExistence-61"><span class="linenos">61</span></a>    
</span><span id="ValueExistence-62"><a href="#ValueExistence-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueExistence-63"><a href="#ValueExistence-63"><span class="linenos">63</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueExistence-64"><a href="#ValueExistence-64"><span class="linenos">64</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-65"><a href="#ValueExistence-65"><span class="linenos">65</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-66"><a href="#ValueExistence-66"><span class="linenos">66</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="ValueExistence-67"><a href="#ValueExistence-67"><span class="linenos">67</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="ValueExistence-68"><a href="#ValueExistence-68"><span class="linenos">68</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-69"><a href="#ValueExistence-69"><span class="linenos">69</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="ValueExistence-70"><a href="#ValueExistence-70"><span class="linenos">70</span></a>    
</span><span id="ValueExistence-71"><a href="#ValueExistence-71"><span class="linenos">71</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueExistence-72"><a href="#ValueExistence-72"><span class="linenos">72</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="ValueExistence.__init__" class="classattr">
                                        <input id="ValueExistence.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueExistence</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span>, </span><span class="param"><span class="n">result</span><span class="p">:</span> <span class="n">Any</span></span>)</span>

                <label class="view-source-button" for="ValueExistence.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.__init__-41"><a href="#ValueExistence.__init__-41"><span class="linenos">41</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="ValueExistence.__init__-42"><a href="#ValueExistence.__init__-42"><span class="linenos">42</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence.__init__-43"><a href="#ValueExistence.__init__-43"><span class="linenos">43</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.existence" class="classattr">
                                <div class="attr variable">
            <span class="name">existence</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#ValueExistence.existence"></a>
    
    

                            </div>
                            <div id="ValueExistence.result" class="classattr">
                                <div class="attr variable">
            <span class="name">result</span>

        
    </div>
    <a class="headerlink" href="#ValueExistence.result"></a>
    
    

                            </div>
                </section>
                <section id="ValueCache">
                            <input id="ValueCache-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueCache</span><wbr>(<span class="base"><a href="#ValueExistence">ValueExistence</a></span>):

                <label class="view-source-button" for="ValueCache-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache-75"><a href="#ValueCache-75"><span class="linenos"> 75</span></a><span class="k">class</span> <span class="nc">ValueCache</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueCache-76"><a href="#ValueCache-76"><span class="linenos"> 76</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="ValueCache-77"><a href="#ValueCache-77"><span class="linenos"> 77</span></a>
</span><span id="ValueCache-78"><a href="#ValueCache-78"><span class="linenos"> 78</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache-79"><a href="#ValueCache-79"><span class="linenos"> 79</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ValueCache</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="ValueCache-80"><a href="#ValueCache-80"><span class="linenos"> 80</span></a>
</span><span id="ValueCache-81"><a href="#ValueCache-81"><span class="linenos"> 81</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ValueCache-82"><a href="#ValueCache-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ValueCache-83"><a href="#ValueCache-83"><span class="linenos"> 83</span></a>
</span><span id="ValueCache-84"><a href="#ValueCache-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache-85"><a href="#ValueCache-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="ValueCache-86"><a href="#ValueCache-86"><span class="linenos"> 86</span></a>
</span><span id="ValueCache-87"><a href="#ValueCache-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_result</span><span class="p">):</span>
</span><span id="ValueCache-88"><a href="#ValueCache-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ValueCache-89"><a href="#ValueCache-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">new_result</span>
</span><span id="ValueCache-90"><a href="#ValueCache-90"><span class="linenos"> 90</span></a>
</span><span id="ValueCache-91"><a href="#ValueCache-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache-92"><a href="#ValueCache-92"><span class="linenos"> 92</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="ValueCache-93"><a href="#ValueCache-93"><span class="linenos"> 93</span></a>
</span><span id="ValueCache-94"><a href="#ValueCache-94"><span class="linenos"> 94</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueCache-95"><a href="#ValueCache-95"><span class="linenos"> 95</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueCache-96"><a href="#ValueCache-96"><span class="linenos"> 96</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueCache-97"><a href="#ValueCache-97"><span class="linenos"> 97</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueCache-98"><a href="#ValueCache-98"><span class="linenos"> 98</span></a>    
</span><span id="ValueCache-99"><a href="#ValueCache-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueCache-100"><a href="#ValueCache-100"><span class="linenos">100</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueCache-101"><a href="#ValueCache-101"><span class="linenos">101</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueCache-102"><a href="#ValueCache-102"><span class="linenos">102</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueCache-103"><a href="#ValueCache-103"><span class="linenos">103</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="ValueCache-104"><a href="#ValueCache-104"><span class="linenos">104</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="ValueCache-105"><a href="#ValueCache-105"><span class="linenos">105</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ValueCache-106"><a href="#ValueCache-106"><span class="linenos">106</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="ValueCache-107"><a href="#ValueCache-107"><span class="linenos">107</span></a>    
</span><span id="ValueCache-108"><a href="#ValueCache-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueCache-109"><a href="#ValueCache-109"><span class="linenos">109</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="ValueCache.get" class="classattr">
                                        <input id="ValueCache.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ValueCache.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.get-84"><a href="#ValueCache.get-84"><span class="linenos">84</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache.get-85"><a href="#ValueCache.get-85"><span class="linenos">85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueCache.set" class="classattr">
                                        <input id="ValueCache.set-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">new_result</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ValueCache.set-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.set"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.set-87"><a href="#ValueCache.set-87"><span class="linenos">87</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_result</span><span class="p">):</span>
</span><span id="ValueCache.set-88"><a href="#ValueCache.set-88"><span class="linenos">88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ValueCache.set-89"><a href="#ValueCache.set-89"><span class="linenos">89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">new_result</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ValueCache.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ValueCache.result" class="variable"><a href="#ValueExistence.result">result</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueType">
                            <input id="ValueType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueType</span>:

                <label class="view-source-button" for="ValueType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType-112"><a href="#ValueType-112"><span class="linenos">112</span></a><span class="k">class</span> <span class="nc">ValueType</span><span class="p">:</span>
</span><span id="ValueType-113"><a href="#ValueType-113"><span class="linenos">113</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;result&#39;</span><span class="p">)</span>
</span><span id="ValueType-114"><a href="#ValueType-114"><span class="linenos">114</span></a>
</span><span id="ValueType-115"><a href="#ValueType-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="ValueType-116"><a href="#ValueType-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueType-117"><a href="#ValueType-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="ValueType-118"><a href="#ValueType-118"><span class="linenos">118</span></a>
</span><span id="ValueType-119"><a href="#ValueType-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="ValueType-120"><a href="#ValueType-120"><span class="linenos">120</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the result&quot;</span>
</span><span id="ValueType-121"><a href="#ValueType-121"><span class="linenos">121</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueType</span><span class="p">):</span>
</span><span id="ValueType-122"><a href="#ValueType-122"><span class="linenos">122</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="ValueType-123"><a href="#ValueType-123"><span class="linenos">123</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType-124"><a href="#ValueType-124"><span class="linenos">124</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="ValueType-125"><a href="#ValueType-125"><span class="linenos">125</span></a>
</span><span id="ValueType-126"><a href="#ValueType-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueType-127"><a href="#ValueType-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span>
</span><span id="ValueType-128"><a href="#ValueType-128"><span class="linenos">128</span></a>
</span><span id="ValueType-129"><a href="#ValueType-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueType-130"><a href="#ValueType-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">state</span>
</span></pre></div>


    

                            <div id="ValueType.__init__" class="classattr">
                                        <input id="ValueType.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueType</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span>, </span><span class="param"><span class="n">result</span></span>)</span>

                <label class="view-source-button" for="ValueType.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.__init__-115"><a href="#ValueType.__init__-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="ValueType.__init__-116"><a href="#ValueType.__init__-116"><span class="linenos">116</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueType.__init__-117"><a href="#ValueType.__init__-117"><span class="linenos">117</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">result</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span>

        
    </div>
    <a class="headerlink" href="#ValueType.type_id"></a>
    
    

                            </div>
                            <div id="ValueType.result" class="classattr">
                                <div class="attr variable">
            <span class="name">result</span>

        
    </div>
    <a class="headerlink" href="#ValueType.result"></a>
    
    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>