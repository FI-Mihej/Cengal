---
title: binary
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_manipulation<wbr>.conversion<wbr>.binary<wbr>.versions<wbr>.v_0<wbr>.binary    </h1>

                
                        <input id="mod-binary-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-binary-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>    <span class="s1">&#39;bigint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>    <span class="s1">&#39;bint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>    <span class="s1">&#39;bytes_to_bigint&#39;</span><span class="p">,</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>    <span class="s1">&#39;bytes_to_bint&#39;</span><span class="p">,</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>    <span class="s1">&#39;ubigint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>    <span class="s1">&#39;ubint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>    <span class="s1">&#39;bytes_to_ubigint&#39;</span><span class="p">,</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>    <span class="s1">&#39;bytes_to_ubint&#39;</span><span class="p">,</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>    <span class="s1">&#39;int64_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a>    <span class="s1">&#39;longlongint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>    <span class="s1">&#39;llint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>    <span class="s1">&#39;bytes_to_int64&#39;</span><span class="p">,</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a>    <span class="s1">&#39;bytes_to_longlongint&#39;</span><span class="p">,</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>    <span class="s1">&#39;bytes_to_llint&#39;</span><span class="p">,</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a>    <span class="s1">&#39;int32_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>    <span class="s1">&#39;int_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>    <span class="s1">&#39;bytes_to_int32&#39;</span><span class="p">,</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>    <span class="s1">&#39;bytes_to_int&#39;</span><span class="p">,</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="s1">&#39;int16_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>    <span class="s1">&#39;short_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>    <span class="s1">&#39;bytes_to_int16&#39;</span><span class="p">,</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>    <span class="s1">&#39;bytes_to_short&#39;</span><span class="p">,</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>    <span class="s1">&#39;int8_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>    <span class="s1">&#39;byte_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>    <span class="s1">&#39;bytes_to_int8&#39;</span><span class="p">,</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="s1">&#39;bytes_to_byte&#39;</span><span class="p">,</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="s1">&#39;uint64_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="s1">&#39;ulonglongint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="s1">&#39;ullint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="s1">&#39;bytes_to_uint64&#39;</span><span class="p">,</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="s1">&#39;bytes_to_ulonglongint&#39;</span><span class="p">,</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="s1">&#39;bytes_to_ullint&#39;</span><span class="p">,</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="s1">&#39;uint32_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="s1">&#39;uint_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="s1">&#39;bytes_to_uint32&#39;</span><span class="p">,</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="s1">&#39;bytes_to_uint&#39;</span><span class="p">,</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="s1">&#39;uint16_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="s1">&#39;ushort_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="s1">&#39;bytes_to_uint16&#39;</span><span class="p">,</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="s1">&#39;bytes_to_ushort&#39;</span><span class="p">,</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="s1">&#39;uint8_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="s1">&#39;ubyte_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="s1">&#39;bytes_to_uint8&#39;</span><span class="p">,</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="s1">&#39;bytes_to_ubyte&#39;</span><span class="p">,</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="s1">&#39;float64_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="s1">&#39;double_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="s1">&#39;bytes_to_float64&#39;</span><span class="p">,</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="s1">&#39;bytes_to_double&#39;</span><span class="p">,</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    <span class="s1">&#39;float32_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>    <span class="s1">&#39;float_to_bytes&#39;</span><span class="p">,</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="s1">&#39;bytes_to_float32&#39;</span><span class="p">,</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="s1">&#39;bytes_to_float&#39;</span><span class="p">,</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="p">]</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="sd">Module Docstring</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="kn">import</span> <span class="nn">struct</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="c1"># Arbitrary length integers </span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="k">def</span> <span class="nf">bigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">):</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8. Add 1 to ensure that the number is always has a sign bit</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="n">bint_to_bytes</span> <span class="o">=</span> <span class="n">bigint_to_bytes</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="k">def</span> <span class="nf">bytes_to_bigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a><span class="n">bytes_to_bint</span> <span class="o">=</span> <span class="n">bytes_to_bigint</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="k">def</span> <span class="nf">ubigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">7</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="n">ubint_to_bytes</span> <span class="o">=</span> <span class="n">ubigint_to_bytes</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="k">def</span> <span class="nf">bytes_to_ubigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="n">bytes_to_ubint</span> <span class="o">=</span> <span class="n">bytes_to_ubigint</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="c1"># Fixed length integers</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="k">def</span> <span class="nf">int64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="sd">    :param int_data:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="n">longlongint_to_bytes</span> <span class="o">=</span> <span class="n">int64_to_bytes</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="n">llint_to_bytes</span> <span class="o">=</span> <span class="n">int64_to_bytes</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a><span class="k">def</span> <span class="nf">bytes_to_int64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="sd">    :return:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a><span class="n">bytes_to_longlongint</span> <span class="o">=</span> <span class="n">bytes_to_int64</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="n">bytes_to_llint</span> <span class="o">=</span> <span class="n">bytes_to_int64</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a><span class="k">def</span> <span class="nf">int32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="sd">    :param int_data:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="n">int_to_bytes</span> <span class="o">=</span> <span class="n">int32_to_bytes</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="k">def</span> <span class="nf">bytes_to_int32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">    :return:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="n">bytes_to_int</span> <span class="o">=</span> <span class="n">bytes_to_int32</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="k">def</span> <span class="nf">int16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">    :param short_data:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="n">short_to_bytes</span> <span class="o">=</span> <span class="n">int16_to_bytes</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="k">def</span> <span class="nf">bytes_to_int16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">    :return:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a><span class="n">bytes_to_short</span> <span class="o">=</span> <span class="n">bytes_to_int16</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="k">def</span> <span class="nf">int8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a><span class="sd">    :param byte_data:</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a><span class="n">byte_to_bytes</span> <span class="o">=</span> <span class="n">int8_to_bytes</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a><span class="k">def</span> <span class="nf">bytes_to_int8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">    :return:</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a><span class="n">bytes_to_byte</span> <span class="o">=</span> <span class="n">bytes_to_int8</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a><span class="k">def</span> <span class="nf">uint64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a><span class="sd">    :param int_data:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a><span class="n">ulonglongint_to_bytes</span> <span class="o">=</span> <span class="n">uint64_to_bytes</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a><span class="n">ullint_to_bytes</span> <span class="o">=</span> <span class="n">uint64_to_bytes</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a><span class="k">def</span> <span class="nf">bytes_to_uint64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a><span class="sd">    :return:</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a><span class="n">bytes_to_ulonglongint</span> <span class="o">=</span> <span class="n">bytes_to_uint64</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a><span class="n">bytes_to_ullint</span> <span class="o">=</span> <span class="n">bytes_to_uint64</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a><span class="k">def</span> <span class="nf">uint32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="sd">    :param int_data:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a><span class="n">uint_to_bytes</span> <span class="o">=</span> <span class="n">uint32_to_bytes</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="k">def</span> <span class="nf">bytes_to_uint32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a><span class="sd">    :return:</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a><span class="n">bytes_to_uint</span> <span class="o">=</span> <span class="n">bytes_to_uint32</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="k">def</span> <span class="nf">uint16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a><span class="sd">    :param short_data:</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a><span class="n">ushort_to_bytes</span> <span class="o">=</span> <span class="n">uint16_to_bytes</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="k">def</span> <span class="nf">bytes_to_uint16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a><span class="sd">    :return:</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a><span class="n">bytes_to_ushort</span> <span class="o">=</span> <span class="n">bytes_to_uint16</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="k">def</span> <span class="nf">uint8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a><span class="sd">    :param byte_data:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a><span class="n">ubyte_to_bytes</span> <span class="o">=</span> <span class="n">uint8_to_bytes</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a><span class="k">def</span> <span class="nf">bytes_to_uint8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a><span class="sd">    :return:</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a><span class="n">bytes_to_ubyte</span> <span class="o">=</span> <span class="n">bytes_to_uint8</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a><span class="c1"># Fixed length floats</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a><span class="k">def</span> <span class="nf">float64_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a><span class="sd">    :param float_data:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a><span class="sd">    :return: bytes() with len == 8</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a><span class="n">double_to_bytes</span> <span class="o">=</span> <span class="n">float64_to_bytes</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a><span class="k">def</span> <span class="nf">bytes_to_float64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a><span class="sd">    :param bytes_data: bytes() with len == 8</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a><span class="sd">    :return:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="n">bytes_to_double</span> <span class="o">=</span> <span class="n">bytes_to_float64</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a><span class="k">def</span> <span class="nf">float32_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a><span class="sd">    :param float_data:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a><span class="sd">    :return: bytes() with len == 4</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a><span class="n">float_to_bytes</span> <span class="o">=</span> <span class="n">float32_to_bytes</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="k">def</span> <span class="nf">bytes_to_float32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">    :param bytes_data: bytes() with len == 4</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">    :return:</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a><span class="n">bytes_to_float</span> <span class="o">=</span> <span class="n">bytes_to_float32</span>
</span></pre></div>


            </section>
                <section id="bigint_to_bytes">
                            <input id="bigint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bigint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bigint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bigint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bigint_to_bytes-99"><a href="#bigint_to_bytes-99"><span class="linenos"> 99</span></a><span class="k">def</span> <span class="nf">bigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">):</span>
</span><span id="bigint_to_bytes-100"><a href="#bigint_to_bytes-100"><span class="linenos">100</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8. Add 1 to ensure that the number is always has a sign bit</span>
</span></pre></div>


    

                </section>
                <section id="bint_to_bytes">
                            <input id="bint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bint_to_bytes-99"><a href="#bint_to_bytes-99"><span class="linenos"> 99</span></a><span class="k">def</span> <span class="nf">bigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">):</span>
</span><span id="bint_to_bytes-100"><a href="#bint_to_bytes-100"><span class="linenos">100</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8. Add 1 to ensure that the number is always has a sign bit</span>
</span></pre></div>


    

                </section>
                <section id="bytes_to_bigint">
                            <input id="bytes_to_bigint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_bigint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_bigint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_bigint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_bigint-106"><a href="#bytes_to_bigint-106"><span class="linenos">106</span></a><span class="k">def</span> <span class="nf">bytes_to_bigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_bigint-107"><a href="#bytes_to_bigint-107"><span class="linenos">107</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="bytes_to_bint">
                            <input id="bytes_to_bint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_bint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_bint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_bint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_bint-106"><a href="#bytes_to_bint-106"><span class="linenos">106</span></a><span class="k">def</span> <span class="nf">bytes_to_bigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_bint-107"><a href="#bytes_to_bint-107"><span class="linenos">107</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="n">byteorder</span><span class="p">,</span> <span class="n">signed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="ubigint_to_bytes">
                            <input id="ubigint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ubigint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ubigint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ubigint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ubigint_to_bytes-113"><a href="#ubigint_to_bytes-113"><span class="linenos">113</span></a><span class="k">def</span> <span class="nf">ubigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="ubigint_to_bytes-114"><a href="#ubigint_to_bytes-114"><span class="linenos">114</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">7</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8</span>
</span></pre></div>


    

                </section>
                <section id="ubint_to_bytes">
                            <input id="ubint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ubint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ubint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ubint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ubint_to_bytes-113"><a href="#ubint_to_bytes-113"><span class="linenos">113</span></a><span class="k">def</span> <span class="nf">ubigint_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="ubint_to_bytes-114"><a href="#ubint_to_bytes-114"><span class="linenos">114</span></a>    <span class="k">return</span> <span class="n">int_data</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">((</span><span class="n">int_data</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span> <span class="o">+</span> <span class="mi">7</span><span class="p">)</span> <span class="o">//</span> <span class="mi">8</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>  <span class="c1"># Add 7 to handle cases where bit_length is not a multiple of 8</span>
</span></pre></div>


    

                </section>
                <section id="bytes_to_ubigint">
                            <input id="bytes_to_ubigint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ubigint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ubigint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ubigint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ubigint-120"><a href="#bytes_to_ubigint-120"><span class="linenos">120</span></a><span class="k">def</span> <span class="nf">bytes_to_ubigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ubigint-121"><a href="#bytes_to_ubigint-121"><span class="linenos">121</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="bytes_to_ubint">
                            <input id="bytes_to_ubint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ubint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span>, </span><span class="param"><span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ubint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ubint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ubint-120"><a href="#bytes_to_ubint-120"><span class="linenos">120</span></a><span class="k">def</span> <span class="nf">bytes_to_ubigint</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ubint-121"><a href="#bytes_to_ubint-121"><span class="linenos">121</span></a>    <span class="k">return</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">,</span> <span class="n">byteorder</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="int64_to_bytes">
                            <input id="int64_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">int64_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="int64_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#int64_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="int64_to_bytes-130"><a href="#int64_to_bytes-130"><span class="linenos">130</span></a><span class="k">def</span> <span class="nf">int64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="int64_to_bytes-131"><a href="#int64_to_bytes-131"><span class="linenos">131</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="int64_to_bytes-132"><a href="#int64_to_bytes-132"><span class="linenos">132</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="int64_to_bytes-133"><a href="#int64_to_bytes-133"><span class="linenos">133</span></a><span class="sd">    :param int_data:</span>
</span><span id="int64_to_bytes-134"><a href="#int64_to_bytes-134"><span class="linenos">134</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="int64_to_bytes-135"><a href="#int64_to_bytes-135"><span class="linenos">135</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="int64_to_bytes-136"><a href="#int64_to_bytes-136"><span class="linenos">136</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="int64_to_bytes-137"><a href="#int64_to_bytes-137"><span class="linenos">137</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="longlongint_to_bytes">
                            <input id="longlongint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">longlongint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="longlongint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#longlongint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="longlongint_to_bytes-130"><a href="#longlongint_to_bytes-130"><span class="linenos">130</span></a><span class="k">def</span> <span class="nf">int64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="longlongint_to_bytes-131"><a href="#longlongint_to_bytes-131"><span class="linenos">131</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="longlongint_to_bytes-132"><a href="#longlongint_to_bytes-132"><span class="linenos">132</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="longlongint_to_bytes-133"><a href="#longlongint_to_bytes-133"><span class="linenos">133</span></a><span class="sd">    :param int_data:</span>
</span><span id="longlongint_to_bytes-134"><a href="#longlongint_to_bytes-134"><span class="linenos">134</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="longlongint_to_bytes-135"><a href="#longlongint_to_bytes-135"><span class="linenos">135</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="longlongint_to_bytes-136"><a href="#longlongint_to_bytes-136"><span class="linenos">136</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="longlongint_to_bytes-137"><a href="#longlongint_to_bytes-137"><span class="linenos">137</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="llint_to_bytes">
                            <input id="llint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">llint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="llint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#llint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="llint_to_bytes-130"><a href="#llint_to_bytes-130"><span class="linenos">130</span></a><span class="k">def</span> <span class="nf">int64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="llint_to_bytes-131"><a href="#llint_to_bytes-131"><span class="linenos">131</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="llint_to_bytes-132"><a href="#llint_to_bytes-132"><span class="linenos">132</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="llint_to_bytes-133"><a href="#llint_to_bytes-133"><span class="linenos">133</span></a><span class="sd">    :param int_data:</span>
</span><span id="llint_to_bytes-134"><a href="#llint_to_bytes-134"><span class="linenos">134</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="llint_to_bytes-135"><a href="#llint_to_bytes-135"><span class="linenos">135</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="llint_to_bytes-136"><a href="#llint_to_bytes-136"><span class="linenos">136</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="llint_to_bytes-137"><a href="#llint_to_bytes-137"><span class="linenos">137</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="bytes_to_int64">
                            <input id="bytes_to_int64-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_int64</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_int64-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_int64"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_int64-144"><a href="#bytes_to_int64-144"><span class="linenos">144</span></a><span class="k">def</span> <span class="nf">bytes_to_int64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_int64-145"><a href="#bytes_to_int64-145"><span class="linenos">145</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_int64-146"><a href="#bytes_to_int64-146"><span class="linenos">146</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="bytes_to_int64-147"><a href="#bytes_to_int64-147"><span class="linenos">147</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_int64-148"><a href="#bytes_to_int64-148"><span class="linenos">148</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_int64-149"><a href="#bytes_to_int64-149"><span class="linenos">149</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_int64-150"><a href="#bytes_to_int64-150"><span class="linenos">150</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_int64-151"><a href="#bytes_to_int64-151"><span class="linenos">151</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_longlongint">
                            <input id="bytes_to_longlongint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_longlongint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_longlongint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_longlongint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_longlongint-144"><a href="#bytes_to_longlongint-144"><span class="linenos">144</span></a><span class="k">def</span> <span class="nf">bytes_to_int64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_longlongint-145"><a href="#bytes_to_longlongint-145"><span class="linenos">145</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_longlongint-146"><a href="#bytes_to_longlongint-146"><span class="linenos">146</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="bytes_to_longlongint-147"><a href="#bytes_to_longlongint-147"><span class="linenos">147</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_longlongint-148"><a href="#bytes_to_longlongint-148"><span class="linenos">148</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_longlongint-149"><a href="#bytes_to_longlongint-149"><span class="linenos">149</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_longlongint-150"><a href="#bytes_to_longlongint-150"><span class="linenos">150</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_longlongint-151"><a href="#bytes_to_longlongint-151"><span class="linenos">151</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_llint">
                            <input id="bytes_to_llint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_llint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_llint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_llint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_llint-144"><a href="#bytes_to_llint-144"><span class="linenos">144</span></a><span class="k">def</span> <span class="nf">bytes_to_int64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_llint-145"><a href="#bytes_to_llint-145"><span class="linenos">145</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_llint-146"><a href="#bytes_to_llint-146"><span class="linenos">146</span></a><span class="sd">    For a 64 bit signed int in little endian</span>
</span><span id="bytes_to_llint-147"><a href="#bytes_to_llint-147"><span class="linenos">147</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_llint-148"><a href="#bytes_to_llint-148"><span class="linenos">148</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_llint-149"><a href="#bytes_to_llint-149"><span class="linenos">149</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_llint-150"><a href="#bytes_to_llint-150"><span class="linenos">150</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_llint-151"><a href="#bytes_to_llint-151"><span class="linenos">151</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="int32_to_bytes">
                            <input id="int32_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">int32_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="int32_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#int32_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="int32_to_bytes-158"><a href="#int32_to_bytes-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">int32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="int32_to_bytes-159"><a href="#int32_to_bytes-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="int32_to_bytes-160"><a href="#int32_to_bytes-160"><span class="linenos">160</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="int32_to_bytes-161"><a href="#int32_to_bytes-161"><span class="linenos">161</span></a><span class="sd">    :param int_data:</span>
</span><span id="int32_to_bytes-162"><a href="#int32_to_bytes-162"><span class="linenos">162</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="int32_to_bytes-163"><a href="#int32_to_bytes-163"><span class="linenos">163</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="int32_to_bytes-164"><a href="#int32_to_bytes-164"><span class="linenos">164</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="int32_to_bytes-165"><a href="#int32_to_bytes-165"><span class="linenos">165</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed int in little endian
:param int_data:
:return: bytes(); len == 4</p>
</div>


                </section>
                <section id="int_to_bytes">
                            <input id="int_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">int_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="int_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#int_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="int_to_bytes-158"><a href="#int_to_bytes-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">int32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="int_to_bytes-159"><a href="#int_to_bytes-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="int_to_bytes-160"><a href="#int_to_bytes-160"><span class="linenos">160</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="int_to_bytes-161"><a href="#int_to_bytes-161"><span class="linenos">161</span></a><span class="sd">    :param int_data:</span>
</span><span id="int_to_bytes-162"><a href="#int_to_bytes-162"><span class="linenos">162</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="int_to_bytes-163"><a href="#int_to_bytes-163"><span class="linenos">163</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="int_to_bytes-164"><a href="#int_to_bytes-164"><span class="linenos">164</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="int_to_bytes-165"><a href="#int_to_bytes-165"><span class="linenos">165</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed int in little endian
:param int_data:
:return: bytes(); len == 4</p>
</div>


                </section>
                <section id="bytes_to_int32">
                            <input id="bytes_to_int32-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_int32</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_int32-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_int32"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_int32-171"><a href="#bytes_to_int32-171"><span class="linenos">171</span></a><span class="k">def</span> <span class="nf">bytes_to_int32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_int32-172"><a href="#bytes_to_int32-172"><span class="linenos">172</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_int32-173"><a href="#bytes_to_int32-173"><span class="linenos">173</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="bytes_to_int32-174"><a href="#bytes_to_int32-174"><span class="linenos">174</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_int32-175"><a href="#bytes_to_int32-175"><span class="linenos">175</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_int32-176"><a href="#bytes_to_int32-176"><span class="linenos">176</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_int32-177"><a href="#bytes_to_int32-177"><span class="linenos">177</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_int32-178"><a href="#bytes_to_int32-178"><span class="linenos">178</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_int">
                            <input id="bytes_to_int-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_int</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_int-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_int"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_int-171"><a href="#bytes_to_int-171"><span class="linenos">171</span></a><span class="k">def</span> <span class="nf">bytes_to_int32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_int-172"><a href="#bytes_to_int-172"><span class="linenos">172</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_int-173"><a href="#bytes_to_int-173"><span class="linenos">173</span></a><span class="sd">    For a 32 bit signed int in little endian</span>
</span><span id="bytes_to_int-174"><a href="#bytes_to_int-174"><span class="linenos">174</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_int-175"><a href="#bytes_to_int-175"><span class="linenos">175</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_int-176"><a href="#bytes_to_int-176"><span class="linenos">176</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_int-177"><a href="#bytes_to_int-177"><span class="linenos">177</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;i&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_int-178"><a href="#bytes_to_int-178"><span class="linenos">178</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="int16_to_bytes">
                            <input id="int16_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">int16_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="int16_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#int16_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="int16_to_bytes-184"><a href="#int16_to_bytes-184"><span class="linenos">184</span></a><span class="k">def</span> <span class="nf">int16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="int16_to_bytes-185"><a href="#int16_to_bytes-185"><span class="linenos">185</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="int16_to_bytes-186"><a href="#int16_to_bytes-186"><span class="linenos">186</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="int16_to_bytes-187"><a href="#int16_to_bytes-187"><span class="linenos">187</span></a><span class="sd">    :param short_data:</span>
</span><span id="int16_to_bytes-188"><a href="#int16_to_bytes-188"><span class="linenos">188</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="int16_to_bytes-189"><a href="#int16_to_bytes-189"><span class="linenos">189</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="int16_to_bytes-190"><a href="#int16_to_bytes-190"><span class="linenos">190</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="int16_to_bytes-191"><a href="#int16_to_bytes-191"><span class="linenos">191</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit signed short in little endian
:param short_data:
:return: bytes(); len == 2</p>
</div>


                </section>
                <section id="short_to_bytes">
                            <input id="short_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">short_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="short_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#short_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="short_to_bytes-184"><a href="#short_to_bytes-184"><span class="linenos">184</span></a><span class="k">def</span> <span class="nf">int16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="short_to_bytes-185"><a href="#short_to_bytes-185"><span class="linenos">185</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="short_to_bytes-186"><a href="#short_to_bytes-186"><span class="linenos">186</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="short_to_bytes-187"><a href="#short_to_bytes-187"><span class="linenos">187</span></a><span class="sd">    :param short_data:</span>
</span><span id="short_to_bytes-188"><a href="#short_to_bytes-188"><span class="linenos">188</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="short_to_bytes-189"><a href="#short_to_bytes-189"><span class="linenos">189</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="short_to_bytes-190"><a href="#short_to_bytes-190"><span class="linenos">190</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="short_to_bytes-191"><a href="#short_to_bytes-191"><span class="linenos">191</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit signed short in little endian
:param short_data:
:return: bytes(); len == 2</p>
</div>


                </section>
                <section id="bytes_to_int16">
                            <input id="bytes_to_int16-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_int16</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_int16-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_int16"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_int16-197"><a href="#bytes_to_int16-197"><span class="linenos">197</span></a><span class="k">def</span> <span class="nf">bytes_to_int16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_int16-198"><a href="#bytes_to_int16-198"><span class="linenos">198</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_int16-199"><a href="#bytes_to_int16-199"><span class="linenos">199</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="bytes_to_int16-200"><a href="#bytes_to_int16-200"><span class="linenos">200</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_int16-201"><a href="#bytes_to_int16-201"><span class="linenos">201</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_int16-202"><a href="#bytes_to_int16-202"><span class="linenos">202</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_int16-203"><a href="#bytes_to_int16-203"><span class="linenos">203</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_int16-204"><a href="#bytes_to_int16-204"><span class="linenos">204</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit signed short in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_short">
                            <input id="bytes_to_short-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_short</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_short-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_short"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_short-197"><a href="#bytes_to_short-197"><span class="linenos">197</span></a><span class="k">def</span> <span class="nf">bytes_to_int16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_short-198"><a href="#bytes_to_short-198"><span class="linenos">198</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_short-199"><a href="#bytes_to_short-199"><span class="linenos">199</span></a><span class="sd">    For a 16 bit signed short in little endian</span>
</span><span id="bytes_to_short-200"><a href="#bytes_to_short-200"><span class="linenos">200</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_short-201"><a href="#bytes_to_short-201"><span class="linenos">201</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_short-202"><a href="#bytes_to_short-202"><span class="linenos">202</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_short-203"><a href="#bytes_to_short-203"><span class="linenos">203</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;h&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_short-204"><a href="#bytes_to_short-204"><span class="linenos">204</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit signed short in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="int8_to_bytes">
                            <input id="int8_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">int8_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="int8_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#int8_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="int8_to_bytes-210"><a href="#int8_to_bytes-210"><span class="linenos">210</span></a><span class="k">def</span> <span class="nf">int8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="int8_to_bytes-211"><a href="#int8_to_bytes-211"><span class="linenos">211</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="int8_to_bytes-212"><a href="#int8_to_bytes-212"><span class="linenos">212</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="int8_to_bytes-213"><a href="#int8_to_bytes-213"><span class="linenos">213</span></a><span class="sd">    :param byte_data:</span>
</span><span id="int8_to_bytes-214"><a href="#int8_to_bytes-214"><span class="linenos">214</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="int8_to_bytes-215"><a href="#int8_to_bytes-215"><span class="linenos">215</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="int8_to_bytes-216"><a href="#int8_to_bytes-216"><span class="linenos">216</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="int8_to_bytes-217"><a href="#int8_to_bytes-217"><span class="linenos">217</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit signed byte
:param byte_data:
:return: bytes(); len == 1</p>
</div>


                </section>
                <section id="byte_to_bytes">
                            <input id="byte_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">byte_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="byte_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#byte_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="byte_to_bytes-210"><a href="#byte_to_bytes-210"><span class="linenos">210</span></a><span class="k">def</span> <span class="nf">int8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="byte_to_bytes-211"><a href="#byte_to_bytes-211"><span class="linenos">211</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="byte_to_bytes-212"><a href="#byte_to_bytes-212"><span class="linenos">212</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="byte_to_bytes-213"><a href="#byte_to_bytes-213"><span class="linenos">213</span></a><span class="sd">    :param byte_data:</span>
</span><span id="byte_to_bytes-214"><a href="#byte_to_bytes-214"><span class="linenos">214</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="byte_to_bytes-215"><a href="#byte_to_bytes-215"><span class="linenos">215</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="byte_to_bytes-216"><a href="#byte_to_bytes-216"><span class="linenos">216</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="byte_to_bytes-217"><a href="#byte_to_bytes-217"><span class="linenos">217</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit signed byte
:param byte_data:
:return: bytes(); len == 1</p>
</div>


                </section>
                <section id="bytes_to_int8">
                            <input id="bytes_to_int8-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_int8</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_int8-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_int8"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_int8-223"><a href="#bytes_to_int8-223"><span class="linenos">223</span></a><span class="k">def</span> <span class="nf">bytes_to_int8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_int8-224"><a href="#bytes_to_int8-224"><span class="linenos">224</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_int8-225"><a href="#bytes_to_int8-225"><span class="linenos">225</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="bytes_to_int8-226"><a href="#bytes_to_int8-226"><span class="linenos">226</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_int8-227"><a href="#bytes_to_int8-227"><span class="linenos">227</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_int8-228"><a href="#bytes_to_int8-228"><span class="linenos">228</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_int8-229"><a href="#bytes_to_int8-229"><span class="linenos">229</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_int8-230"><a href="#bytes_to_int8-230"><span class="linenos">230</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit signed byte
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_byte">
                            <input id="bytes_to_byte-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_byte</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_byte-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_byte"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_byte-223"><a href="#bytes_to_byte-223"><span class="linenos">223</span></a><span class="k">def</span> <span class="nf">bytes_to_int8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_byte-224"><a href="#bytes_to_byte-224"><span class="linenos">224</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_byte-225"><a href="#bytes_to_byte-225"><span class="linenos">225</span></a><span class="sd">    For a 8 bit signed byte</span>
</span><span id="bytes_to_byte-226"><a href="#bytes_to_byte-226"><span class="linenos">226</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_byte-227"><a href="#bytes_to_byte-227"><span class="linenos">227</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_byte-228"><a href="#bytes_to_byte-228"><span class="linenos">228</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_byte-229"><a href="#bytes_to_byte-229"><span class="linenos">229</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;b&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_byte-230"><a href="#bytes_to_byte-230"><span class="linenos">230</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit signed byte
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="uint64_to_bytes">
                            <input id="uint64_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">uint64_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="uint64_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#uint64_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="uint64_to_bytes-236"><a href="#uint64_to_bytes-236"><span class="linenos">236</span></a><span class="k">def</span> <span class="nf">uint64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="uint64_to_bytes-237"><a href="#uint64_to_bytes-237"><span class="linenos">237</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="uint64_to_bytes-238"><a href="#uint64_to_bytes-238"><span class="linenos">238</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="uint64_to_bytes-239"><a href="#uint64_to_bytes-239"><span class="linenos">239</span></a><span class="sd">    :param int_data:</span>
</span><span id="uint64_to_bytes-240"><a href="#uint64_to_bytes-240"><span class="linenos">240</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="uint64_to_bytes-241"><a href="#uint64_to_bytes-241"><span class="linenos">241</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="uint64_to_bytes-242"><a href="#uint64_to_bytes-242"><span class="linenos">242</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="uint64_to_bytes-243"><a href="#uint64_to_bytes-243"><span class="linenos">243</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="ulonglongint_to_bytes">
                            <input id="ulonglongint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ulonglongint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ulonglongint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ulonglongint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ulonglongint_to_bytes-236"><a href="#ulonglongint_to_bytes-236"><span class="linenos">236</span></a><span class="k">def</span> <span class="nf">uint64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="ulonglongint_to_bytes-237"><a href="#ulonglongint_to_bytes-237"><span class="linenos">237</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ulonglongint_to_bytes-238"><a href="#ulonglongint_to_bytes-238"><span class="linenos">238</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="ulonglongint_to_bytes-239"><a href="#ulonglongint_to_bytes-239"><span class="linenos">239</span></a><span class="sd">    :param int_data:</span>
</span><span id="ulonglongint_to_bytes-240"><a href="#ulonglongint_to_bytes-240"><span class="linenos">240</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="ulonglongint_to_bytes-241"><a href="#ulonglongint_to_bytes-241"><span class="linenos">241</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ulonglongint_to_bytes-242"><a href="#ulonglongint_to_bytes-242"><span class="linenos">242</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="ulonglongint_to_bytes-243"><a href="#ulonglongint_to_bytes-243"><span class="linenos">243</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="ullint_to_bytes">
                            <input id="ullint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ullint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ullint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ullint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ullint_to_bytes-236"><a href="#ullint_to_bytes-236"><span class="linenos">236</span></a><span class="k">def</span> <span class="nf">uint64_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="ullint_to_bytes-237"><a href="#ullint_to_bytes-237"><span class="linenos">237</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ullint_to_bytes-238"><a href="#ullint_to_bytes-238"><span class="linenos">238</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="ullint_to_bytes-239"><a href="#ullint_to_bytes-239"><span class="linenos">239</span></a><span class="sd">    :param int_data:</span>
</span><span id="ullint_to_bytes-240"><a href="#ullint_to_bytes-240"><span class="linenos">240</span></a><span class="sd">    :return: bytes(); len == 8</span>
</span><span id="ullint_to_bytes-241"><a href="#ullint_to_bytes-241"><span class="linenos">241</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ullint_to_bytes-242"><a href="#ullint_to_bytes-242"><span class="linenos">242</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="ullint_to_bytes-243"><a href="#ullint_to_bytes-243"><span class="linenos">243</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param int_data:
:return: bytes(); len == 8</p>
</div>


                </section>
                <section id="bytes_to_uint64">
                            <input id="bytes_to_uint64-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_uint64</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_uint64-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_uint64"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_uint64-250"><a href="#bytes_to_uint64-250"><span class="linenos">250</span></a><span class="k">def</span> <span class="nf">bytes_to_uint64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_uint64-251"><a href="#bytes_to_uint64-251"><span class="linenos">251</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_uint64-252"><a href="#bytes_to_uint64-252"><span class="linenos">252</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="bytes_to_uint64-253"><a href="#bytes_to_uint64-253"><span class="linenos">253</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_uint64-254"><a href="#bytes_to_uint64-254"><span class="linenos">254</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_uint64-255"><a href="#bytes_to_uint64-255"><span class="linenos">255</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_uint64-256"><a href="#bytes_to_uint64-256"><span class="linenos">256</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_uint64-257"><a href="#bytes_to_uint64-257"><span class="linenos">257</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_ulonglongint">
                            <input id="bytes_to_ulonglongint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ulonglongint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ulonglongint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ulonglongint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ulonglongint-250"><a href="#bytes_to_ulonglongint-250"><span class="linenos">250</span></a><span class="k">def</span> <span class="nf">bytes_to_uint64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ulonglongint-251"><a href="#bytes_to_ulonglongint-251"><span class="linenos">251</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_ulonglongint-252"><a href="#bytes_to_ulonglongint-252"><span class="linenos">252</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="bytes_to_ulonglongint-253"><a href="#bytes_to_ulonglongint-253"><span class="linenos">253</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_ulonglongint-254"><a href="#bytes_to_ulonglongint-254"><span class="linenos">254</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_ulonglongint-255"><a href="#bytes_to_ulonglongint-255"><span class="linenos">255</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_ulonglongint-256"><a href="#bytes_to_ulonglongint-256"><span class="linenos">256</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_ulonglongint-257"><a href="#bytes_to_ulonglongint-257"><span class="linenos">257</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_ullint">
                            <input id="bytes_to_ullint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ullint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ullint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ullint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ullint-250"><a href="#bytes_to_ullint-250"><span class="linenos">250</span></a><span class="k">def</span> <span class="nf">bytes_to_uint64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ullint-251"><a href="#bytes_to_ullint-251"><span class="linenos">251</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_ullint-252"><a href="#bytes_to_ullint-252"><span class="linenos">252</span></a><span class="sd">    For a 64 bit unsigned int in little endian</span>
</span><span id="bytes_to_ullint-253"><a href="#bytes_to_ullint-253"><span class="linenos">253</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_ullint-254"><a href="#bytes_to_ullint-254"><span class="linenos">254</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_ullint-255"><a href="#bytes_to_ullint-255"><span class="linenos">255</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_ullint-256"><a href="#bytes_to_ullint-256"><span class="linenos">256</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;Q&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_ullint-257"><a href="#bytes_to_ullint-257"><span class="linenos">257</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit unsigned int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="uint32_to_bytes">
                            <input id="uint32_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">uint32_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="uint32_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#uint32_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="uint32_to_bytes-264"><a href="#uint32_to_bytes-264"><span class="linenos">264</span></a><span class="k">def</span> <span class="nf">uint32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="uint32_to_bytes-265"><a href="#uint32_to_bytes-265"><span class="linenos">265</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="uint32_to_bytes-266"><a href="#uint32_to_bytes-266"><span class="linenos">266</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="uint32_to_bytes-267"><a href="#uint32_to_bytes-267"><span class="linenos">267</span></a><span class="sd">    :param int_data:</span>
</span><span id="uint32_to_bytes-268"><a href="#uint32_to_bytes-268"><span class="linenos">268</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="uint32_to_bytes-269"><a href="#uint32_to_bytes-269"><span class="linenos">269</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="uint32_to_bytes-270"><a href="#uint32_to_bytes-270"><span class="linenos">270</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="uint32_to_bytes-271"><a href="#uint32_to_bytes-271"><span class="linenos">271</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit unsigned int in little endian
:param int_data:
:return: bytes(); len == 4</p>
</div>


                </section>
                <section id="uint_to_bytes">
                            <input id="uint_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">uint_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="uint_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#uint_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="uint_to_bytes-264"><a href="#uint_to_bytes-264"><span class="linenos">264</span></a><span class="k">def</span> <span class="nf">uint32_to_bytes</span><span class="p">(</span><span class="n">int_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="uint_to_bytes-265"><a href="#uint_to_bytes-265"><span class="linenos">265</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="uint_to_bytes-266"><a href="#uint_to_bytes-266"><span class="linenos">266</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="uint_to_bytes-267"><a href="#uint_to_bytes-267"><span class="linenos">267</span></a><span class="sd">    :param int_data:</span>
</span><span id="uint_to_bytes-268"><a href="#uint_to_bytes-268"><span class="linenos">268</span></a><span class="sd">    :return: bytes(); len == 4</span>
</span><span id="uint_to_bytes-269"><a href="#uint_to_bytes-269"><span class="linenos">269</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="uint_to_bytes-270"><a href="#uint_to_bytes-270"><span class="linenos">270</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">int_data</span><span class="p">)</span>
</span><span id="uint_to_bytes-271"><a href="#uint_to_bytes-271"><span class="linenos">271</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit unsigned int in little endian
:param int_data:
:return: bytes(); len == 4</p>
</div>


                </section>
                <section id="bytes_to_uint32">
                            <input id="bytes_to_uint32-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_uint32</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_uint32-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_uint32"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_uint32-277"><a href="#bytes_to_uint32-277"><span class="linenos">277</span></a><span class="k">def</span> <span class="nf">bytes_to_uint32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_uint32-278"><a href="#bytes_to_uint32-278"><span class="linenos">278</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_uint32-279"><a href="#bytes_to_uint32-279"><span class="linenos">279</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="bytes_to_uint32-280"><a href="#bytes_to_uint32-280"><span class="linenos">280</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_uint32-281"><a href="#bytes_to_uint32-281"><span class="linenos">281</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_uint32-282"><a href="#bytes_to_uint32-282"><span class="linenos">282</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_uint32-283"><a href="#bytes_to_uint32-283"><span class="linenos">283</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_uint32-284"><a href="#bytes_to_uint32-284"><span class="linenos">284</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit unsigned int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_uint">
                            <input id="bytes_to_uint-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_uint</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_uint-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_uint"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_uint-277"><a href="#bytes_to_uint-277"><span class="linenos">277</span></a><span class="k">def</span> <span class="nf">bytes_to_uint32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_uint-278"><a href="#bytes_to_uint-278"><span class="linenos">278</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_uint-279"><a href="#bytes_to_uint-279"><span class="linenos">279</span></a><span class="sd">    For a 32 bit unsigned int in little endian</span>
</span><span id="bytes_to_uint-280"><a href="#bytes_to_uint-280"><span class="linenos">280</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_uint-281"><a href="#bytes_to_uint-281"><span class="linenos">281</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_uint-282"><a href="#bytes_to_uint-282"><span class="linenos">282</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_uint-283"><a href="#bytes_to_uint-283"><span class="linenos">283</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;I&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_uint-284"><a href="#bytes_to_uint-284"><span class="linenos">284</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit unsigned int in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="uint16_to_bytes">
                            <input id="uint16_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">uint16_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="uint16_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#uint16_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="uint16_to_bytes-290"><a href="#uint16_to_bytes-290"><span class="linenos">290</span></a><span class="k">def</span> <span class="nf">uint16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="uint16_to_bytes-291"><a href="#uint16_to_bytes-291"><span class="linenos">291</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="uint16_to_bytes-292"><a href="#uint16_to_bytes-292"><span class="linenos">292</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="uint16_to_bytes-293"><a href="#uint16_to_bytes-293"><span class="linenos">293</span></a><span class="sd">    :param short_data:</span>
</span><span id="uint16_to_bytes-294"><a href="#uint16_to_bytes-294"><span class="linenos">294</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="uint16_to_bytes-295"><a href="#uint16_to_bytes-295"><span class="linenos">295</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="uint16_to_bytes-296"><a href="#uint16_to_bytes-296"><span class="linenos">296</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="uint16_to_bytes-297"><a href="#uint16_to_bytes-297"><span class="linenos">297</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit unsigned short in little endian
:param short_data:
:return: bytes(); len == 2</p>
</div>


                </section>
                <section id="ushort_to_bytes">
                            <input id="ushort_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ushort_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ushort_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ushort_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ushort_to_bytes-290"><a href="#ushort_to_bytes-290"><span class="linenos">290</span></a><span class="k">def</span> <span class="nf">uint16_to_bytes</span><span class="p">(</span><span class="n">short_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="ushort_to_bytes-291"><a href="#ushort_to_bytes-291"><span class="linenos">291</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ushort_to_bytes-292"><a href="#ushort_to_bytes-292"><span class="linenos">292</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="ushort_to_bytes-293"><a href="#ushort_to_bytes-293"><span class="linenos">293</span></a><span class="sd">    :param short_data:</span>
</span><span id="ushort_to_bytes-294"><a href="#ushort_to_bytes-294"><span class="linenos">294</span></a><span class="sd">    :return: bytes(); len == 2</span>
</span><span id="ushort_to_bytes-295"><a href="#ushort_to_bytes-295"><span class="linenos">295</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ushort_to_bytes-296"><a href="#ushort_to_bytes-296"><span class="linenos">296</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">short_data</span><span class="p">)</span>
</span><span id="ushort_to_bytes-297"><a href="#ushort_to_bytes-297"><span class="linenos">297</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit unsigned short in little endian
:param short_data:
:return: bytes(); len == 2</p>
</div>


                </section>
                <section id="bytes_to_uint16">
                            <input id="bytes_to_uint16-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_uint16</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_uint16-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_uint16"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_uint16-303"><a href="#bytes_to_uint16-303"><span class="linenos">303</span></a><span class="k">def</span> <span class="nf">bytes_to_uint16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_uint16-304"><a href="#bytes_to_uint16-304"><span class="linenos">304</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_uint16-305"><a href="#bytes_to_uint16-305"><span class="linenos">305</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="bytes_to_uint16-306"><a href="#bytes_to_uint16-306"><span class="linenos">306</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_uint16-307"><a href="#bytes_to_uint16-307"><span class="linenos">307</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_uint16-308"><a href="#bytes_to_uint16-308"><span class="linenos">308</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_uint16-309"><a href="#bytes_to_uint16-309"><span class="linenos">309</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_uint16-310"><a href="#bytes_to_uint16-310"><span class="linenos">310</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit unsigned short in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_ushort">
                            <input id="bytes_to_ushort-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ushort</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ushort-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ushort"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ushort-303"><a href="#bytes_to_ushort-303"><span class="linenos">303</span></a><span class="k">def</span> <span class="nf">bytes_to_uint16</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ushort-304"><a href="#bytes_to_ushort-304"><span class="linenos">304</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_ushort-305"><a href="#bytes_to_ushort-305"><span class="linenos">305</span></a><span class="sd">    For a 16 bit unsigned short in little endian</span>
</span><span id="bytes_to_ushort-306"><a href="#bytes_to_ushort-306"><span class="linenos">306</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_ushort-307"><a href="#bytes_to_ushort-307"><span class="linenos">307</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_ushort-308"><a href="#bytes_to_ushort-308"><span class="linenos">308</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_ushort-309"><a href="#bytes_to_ushort-309"><span class="linenos">309</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;H&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_ushort-310"><a href="#bytes_to_ushort-310"><span class="linenos">310</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 16 bit unsigned short in little endian
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="uint8_to_bytes">
                            <input id="uint8_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">uint8_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="uint8_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#uint8_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="uint8_to_bytes-316"><a href="#uint8_to_bytes-316"><span class="linenos">316</span></a><span class="k">def</span> <span class="nf">uint8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="uint8_to_bytes-317"><a href="#uint8_to_bytes-317"><span class="linenos">317</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="uint8_to_bytes-318"><a href="#uint8_to_bytes-318"><span class="linenos">318</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="uint8_to_bytes-319"><a href="#uint8_to_bytes-319"><span class="linenos">319</span></a><span class="sd">    :param byte_data:</span>
</span><span id="uint8_to_bytes-320"><a href="#uint8_to_bytes-320"><span class="linenos">320</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="uint8_to_bytes-321"><a href="#uint8_to_bytes-321"><span class="linenos">321</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="uint8_to_bytes-322"><a href="#uint8_to_bytes-322"><span class="linenos">322</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="uint8_to_bytes-323"><a href="#uint8_to_bytes-323"><span class="linenos">323</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit unsigned byte
:param byte_data:
:return: bytes(); len == 1</p>
</div>


                </section>
                <section id="ubyte_to_bytes">
                            <input id="ubyte_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ubyte_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="ubyte_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ubyte_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ubyte_to_bytes-316"><a href="#ubyte_to_bytes-316"><span class="linenos">316</span></a><span class="k">def</span> <span class="nf">uint8_to_bytes</span><span class="p">(</span><span class="n">byte_data</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">bytes</span><span class="p">:</span>
</span><span id="ubyte_to_bytes-317"><a href="#ubyte_to_bytes-317"><span class="linenos">317</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ubyte_to_bytes-318"><a href="#ubyte_to_bytes-318"><span class="linenos">318</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="ubyte_to_bytes-319"><a href="#ubyte_to_bytes-319"><span class="linenos">319</span></a><span class="sd">    :param byte_data:</span>
</span><span id="ubyte_to_bytes-320"><a href="#ubyte_to_bytes-320"><span class="linenos">320</span></a><span class="sd">    :return: bytes(); len == 1</span>
</span><span id="ubyte_to_bytes-321"><a href="#ubyte_to_bytes-321"><span class="linenos">321</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ubyte_to_bytes-322"><a href="#ubyte_to_bytes-322"><span class="linenos">322</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">byte_data</span><span class="p">)</span>
</span><span id="ubyte_to_bytes-323"><a href="#ubyte_to_bytes-323"><span class="linenos">323</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit unsigned byte
:param byte_data:
:return: bytes(); len == 1</p>
</div>


                </section>
                <section id="bytes_to_uint8">
                            <input id="bytes_to_uint8-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_uint8</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_uint8-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_uint8"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_uint8-329"><a href="#bytes_to_uint8-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">bytes_to_uint8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_uint8-330"><a href="#bytes_to_uint8-330"><span class="linenos">330</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_uint8-331"><a href="#bytes_to_uint8-331"><span class="linenos">331</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="bytes_to_uint8-332"><a href="#bytes_to_uint8-332"><span class="linenos">332</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_uint8-333"><a href="#bytes_to_uint8-333"><span class="linenos">333</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_uint8-334"><a href="#bytes_to_uint8-334"><span class="linenos">334</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_uint8-335"><a href="#bytes_to_uint8-335"><span class="linenos">335</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_uint8-336"><a href="#bytes_to_uint8-336"><span class="linenos">336</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit unsigned byte
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="bytes_to_ubyte">
                            <input id="bytes_to_ubyte-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_ubyte</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="bytes_to_ubyte-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_ubyte"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_ubyte-329"><a href="#bytes_to_ubyte-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">bytes_to_uint8</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span><span class="o">-&gt;</span><span class="nb">int</span><span class="p">:</span>
</span><span id="bytes_to_ubyte-330"><a href="#bytes_to_ubyte-330"><span class="linenos">330</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_ubyte-331"><a href="#bytes_to_ubyte-331"><span class="linenos">331</span></a><span class="sd">    For a 8 bit unsigned byte</span>
</span><span id="bytes_to_ubyte-332"><a href="#bytes_to_ubyte-332"><span class="linenos">332</span></a><span class="sd">    :param bytes_data:</span>
</span><span id="bytes_to_ubyte-333"><a href="#bytes_to_ubyte-333"><span class="linenos">333</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_ubyte-334"><a href="#bytes_to_ubyte-334"><span class="linenos">334</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_ubyte-335"><a href="#bytes_to_ubyte-335"><span class="linenos">335</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;&lt;B&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_ubyte-336"><a href="#bytes_to_ubyte-336"><span class="linenos">336</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 8 bit unsigned byte
:param bytes_data:
:return:</p>
</div>


                </section>
                <section id="float64_to_bytes">
                            <input id="float64_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">float64_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">float_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="float64_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#float64_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="float64_to_bytes-345"><a href="#float64_to_bytes-345"><span class="linenos">345</span></a><span class="k">def</span> <span class="nf">float64_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="float64_to_bytes-346"><a href="#float64_to_bytes-346"><span class="linenos">346</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="float64_to_bytes-347"><a href="#float64_to_bytes-347"><span class="linenos">347</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="float64_to_bytes-348"><a href="#float64_to_bytes-348"><span class="linenos">348</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="float64_to_bytes-349"><a href="#float64_to_bytes-349"><span class="linenos">349</span></a><span class="sd">    :param float_data:</span>
</span><span id="float64_to_bytes-350"><a href="#float64_to_bytes-350"><span class="linenos">350</span></a><span class="sd">    :return: bytes() with len == 8</span>
</span><span id="float64_to_bytes-351"><a href="#float64_to_bytes-351"><span class="linenos">351</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="float64_to_bytes-352"><a href="#float64_to_bytes-352"><span class="linenos">352</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="float64_to_bytes-353"><a href="#float64_to_bytes-353"><span class="linenos">353</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param float_data:
:return: bytes() with len == 8</p>
</div>


                </section>
                <section id="double_to_bytes">
                            <input id="double_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">double_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">float_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="double_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#double_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="double_to_bytes-345"><a href="#double_to_bytes-345"><span class="linenos">345</span></a><span class="k">def</span> <span class="nf">float64_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="double_to_bytes-346"><a href="#double_to_bytes-346"><span class="linenos">346</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="double_to_bytes-347"><a href="#double_to_bytes-347"><span class="linenos">347</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="double_to_bytes-348"><a href="#double_to_bytes-348"><span class="linenos">348</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="double_to_bytes-349"><a href="#double_to_bytes-349"><span class="linenos">349</span></a><span class="sd">    :param float_data:</span>
</span><span id="double_to_bytes-350"><a href="#double_to_bytes-350"><span class="linenos">350</span></a><span class="sd">    :return: bytes() with len == 8</span>
</span><span id="double_to_bytes-351"><a href="#double_to_bytes-351"><span class="linenos">351</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="double_to_bytes-352"><a href="#double_to_bytes-352"><span class="linenos">352</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="double_to_bytes-353"><a href="#double_to_bytes-353"><span class="linenos">353</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param float_data:
:return: bytes() with len == 8</p>
</div>


                </section>
                <section id="bytes_to_float64">
                            <input id="bytes_to_float64-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_float64</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bytes_to_float64-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_float64"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_float64-359"><a href="#bytes_to_float64-359"><span class="linenos">359</span></a><span class="k">def</span> <span class="nf">bytes_to_float64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="bytes_to_float64-360"><a href="#bytes_to_float64-360"><span class="linenos">360</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_float64-361"><a href="#bytes_to_float64-361"><span class="linenos">361</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="bytes_to_float64-362"><a href="#bytes_to_float64-362"><span class="linenos">362</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="bytes_to_float64-363"><a href="#bytes_to_float64-363"><span class="linenos">363</span></a><span class="sd">    :param bytes_data: bytes() with len == 8</span>
</span><span id="bytes_to_float64-364"><a href="#bytes_to_float64-364"><span class="linenos">364</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_float64-365"><a href="#bytes_to_float64-365"><span class="linenos">365</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_float64-366"><a href="#bytes_to_float64-366"><span class="linenos">366</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_float64-367"><a href="#bytes_to_float64-367"><span class="linenos">367</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param bytes_data: bytes() with len == 8
:return:</p>
</div>


                </section>
                <section id="bytes_to_double">
                            <input id="bytes_to_double-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_double</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bytes_to_double-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_double"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_double-359"><a href="#bytes_to_double-359"><span class="linenos">359</span></a><span class="k">def</span> <span class="nf">bytes_to_float64</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="bytes_to_double-360"><a href="#bytes_to_double-360"><span class="linenos">360</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_double-361"><a href="#bytes_to_double-361"><span class="linenos">361</span></a><span class="sd">    For a 64 bit signed ieee 754 floating points</span>
</span><span id="bytes_to_double-362"><a href="#bytes_to_double-362"><span class="linenos">362</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="bytes_to_double-363"><a href="#bytes_to_double-363"><span class="linenos">363</span></a><span class="sd">    :param bytes_data: bytes() with len == 8</span>
</span><span id="bytes_to_double-364"><a href="#bytes_to_double-364"><span class="linenos">364</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_double-365"><a href="#bytes_to_double-365"><span class="linenos">365</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_double-366"><a href="#bytes_to_double-366"><span class="linenos">366</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;d&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_double-367"><a href="#bytes_to_double-367"><span class="linenos">367</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 64 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param bytes_data: bytes() with len == 8
:return:</p>
</div>


                </section>
                <section id="float32_to_bytes">
                            <input id="float32_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">float32_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">float_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="float32_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#float32_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="float32_to_bytes-373"><a href="#float32_to_bytes-373"><span class="linenos">373</span></a><span class="k">def</span> <span class="nf">float32_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="float32_to_bytes-374"><a href="#float32_to_bytes-374"><span class="linenos">374</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="float32_to_bytes-375"><a href="#float32_to_bytes-375"><span class="linenos">375</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="float32_to_bytes-376"><a href="#float32_to_bytes-376"><span class="linenos">376</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="float32_to_bytes-377"><a href="#float32_to_bytes-377"><span class="linenos">377</span></a><span class="sd">    :param float_data:</span>
</span><span id="float32_to_bytes-378"><a href="#float32_to_bytes-378"><span class="linenos">378</span></a><span class="sd">    :return: bytes() with len == 4</span>
</span><span id="float32_to_bytes-379"><a href="#float32_to_bytes-379"><span class="linenos">379</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="float32_to_bytes-380"><a href="#float32_to_bytes-380"><span class="linenos">380</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="float32_to_bytes-381"><a href="#float32_to_bytes-381"><span class="linenos">381</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param float_data:
:return: bytes() with len == 4</p>
</div>


                </section>
                <section id="float_to_bytes">
                            <input id="float_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">float_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">float_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="float_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#float_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="float_to_bytes-373"><a href="#float_to_bytes-373"><span class="linenos">373</span></a><span class="k">def</span> <span class="nf">float32_to_bytes</span><span class="p">(</span><span class="n">float_data</span><span class="p">):</span>
</span><span id="float_to_bytes-374"><a href="#float_to_bytes-374"><span class="linenos">374</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="float_to_bytes-375"><a href="#float_to_bytes-375"><span class="linenos">375</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="float_to_bytes-376"><a href="#float_to_bytes-376"><span class="linenos">376</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="float_to_bytes-377"><a href="#float_to_bytes-377"><span class="linenos">377</span></a><span class="sd">    :param float_data:</span>
</span><span id="float_to_bytes-378"><a href="#float_to_bytes-378"><span class="linenos">378</span></a><span class="sd">    :return: bytes() with len == 4</span>
</span><span id="float_to_bytes-379"><a href="#float_to_bytes-379"><span class="linenos">379</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="float_to_bytes-380"><a href="#float_to_bytes-380"><span class="linenos">380</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">float_data</span><span class="p">)</span>
</span><span id="float_to_bytes-381"><a href="#float_to_bytes-381"><span class="linenos">381</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param float_data:
:return: bytes() with len == 4</p>
</div>


                </section>
                <section id="bytes_to_float32">
                            <input id="bytes_to_float32-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_float32</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bytes_to_float32-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_float32"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_float32-387"><a href="#bytes_to_float32-387"><span class="linenos">387</span></a><span class="k">def</span> <span class="nf">bytes_to_float32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="bytes_to_float32-388"><a href="#bytes_to_float32-388"><span class="linenos">388</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_float32-389"><a href="#bytes_to_float32-389"><span class="linenos">389</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="bytes_to_float32-390"><a href="#bytes_to_float32-390"><span class="linenos">390</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="bytes_to_float32-391"><a href="#bytes_to_float32-391"><span class="linenos">391</span></a><span class="sd">    :param bytes_data: bytes() with len == 4</span>
</span><span id="bytes_to_float32-392"><a href="#bytes_to_float32-392"><span class="linenos">392</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_float32-393"><a href="#bytes_to_float32-393"><span class="linenos">393</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_float32-394"><a href="#bytes_to_float32-394"><span class="linenos">394</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_float32-395"><a href="#bytes_to_float32-395"><span class="linenos">395</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param bytes_data: bytes() with len == 4
:return:</p>
</div>


                </section>
                <section id="bytes_to_float">
                            <input id="bytes_to_float-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bytes_to_float</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">bytes_data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="bytes_to_float-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#bytes_to_float"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="bytes_to_float-387"><a href="#bytes_to_float-387"><span class="linenos">387</span></a><span class="k">def</span> <span class="nf">bytes_to_float32</span><span class="p">(</span><span class="n">bytes_data</span><span class="p">):</span>
</span><span id="bytes_to_float-388"><a href="#bytes_to_float-388"><span class="linenos">388</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="bytes_to_float-389"><a href="#bytes_to_float-389"><span class="linenos">389</span></a><span class="sd">    For a 32 bit signed ieee 754 floating points</span>
</span><span id="bytes_to_float-390"><a href="#bytes_to_float-390"><span class="linenos">390</span></a><span class="sd">    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</span>
</span><span id="bytes_to_float-391"><a href="#bytes_to_float-391"><span class="linenos">391</span></a><span class="sd">    :param bytes_data: bytes() with len == 4</span>
</span><span id="bytes_to_float-392"><a href="#bytes_to_float-392"><span class="linenos">392</span></a><span class="sd">    :return:</span>
</span><span id="bytes_to_float-393"><a href="#bytes_to_float-393"><span class="linenos">393</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="bytes_to_float-394"><a href="#bytes_to_float-394"><span class="linenos">394</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s1">&#39;f&#39;</span><span class="p">,</span> <span class="n">bytes_data</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="bytes_to_float-395"><a href="#bytes_to_float-395"><span class="linenos">395</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>For a 32 bit signed ieee 754 floating points
<a href="http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python">http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python</a>
:param bytes_data: bytes() with len == 4
:return:</p>
</div>


                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>