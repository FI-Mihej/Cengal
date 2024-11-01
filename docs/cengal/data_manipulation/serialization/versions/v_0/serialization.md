---
title: serialization
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_manipulation<wbr>.serialization<wbr>.versions<wbr>.v_0<wbr>.serialization    </h1>

                
                        <input id="mod-serialization-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-serialization-view-source"><span>View Source</span></label>

                        <div class="pdoc-code codehilite"><pre><span></span><span id="L-1"><a href="#L-1"><span class="linenos">   1</span></a><span class="ch">#!/usr/bin/env python</span>
</span><span id="L-2"><a href="#L-2"><span class="linenos">   2</span></a><span class="c1"># coding=utf-8</span>
</span><span id="L-3"><a href="#L-3"><span class="linenos">   3</span></a>
</span><span id="L-4"><a href="#L-4"><span class="linenos">   4</span></a><span class="c1"># Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;</span>
</span><span id="L-5"><a href="#L-5"><span class="linenos">   5</span></a><span class="c1"># </span>
</span><span id="L-6"><a href="#L-6"><span class="linenos">   6</span></a><span class="c1"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span>
</span><span id="L-7"><a href="#L-7"><span class="linenos">   7</span></a><span class="c1"># you may not use this file except in compliance with the License.</span>
</span><span id="L-8"><a href="#L-8"><span class="linenos">   8</span></a><span class="c1"># You may obtain a copy of the License at</span>
</span><span id="L-9"><a href="#L-9"><span class="linenos">   9</span></a><span class="c1"># </span>
</span><span id="L-10"><a href="#L-10"><span class="linenos">  10</span></a><span class="c1">#     http://www.apache.org/licenses/LICENSE-2.0</span>
</span><span id="L-11"><a href="#L-11"><span class="linenos">  11</span></a><span class="c1"># </span>
</span><span id="L-12"><a href="#L-12"><span class="linenos">  12</span></a><span class="c1"># Unless required by applicable law or agreed to in writing, software</span>
</span><span id="L-13"><a href="#L-13"><span class="linenos">  13</span></a><span class="c1"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span>
</span><span id="L-14"><a href="#L-14"><span class="linenos">  14</span></a><span class="c1"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span>
</span><span id="L-15"><a href="#L-15"><span class="linenos">  15</span></a><span class="c1"># See the License for the specific language governing permissions and</span>
</span><span id="L-16"><a href="#L-16"><span class="linenos">  16</span></a><span class="c1"># limitations under the License.</span>
</span><span id="L-17"><a href="#L-17"><span class="linenos">  17</span></a>
</span><span id="L-18"><a href="#L-18"><span class="linenos">  18</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.gc</span> <span class="kn">import</span> <span class="n">DisableGC</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos">  19</span></a><span class="kn">from</span> <span class="nn">cengal.modules_management.alternative_import</span> <span class="kn">import</span> <span class="n">alt_import</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos">  20</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.repeat_for_a_time</span> <span class="kn">import</span> <span class="n">Tracer</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos">  21</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.cpu_clock_cycles</span> <span class="kn">import</span> <span class="n">perf_counter</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos">  22</span></a><span class="kn">import</span> <span class="nn">enum</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos">  23</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">lru_cache</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos">  24</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos">  25</span></a>
</span><span id="L-26"><a href="#L-26"><span class="linenos">  26</span></a>
</span><span id="L-27"><a href="#L-27"><span class="linenos">  27</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos">  28</span></a><span class="sd">Module Docstring</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos">  29</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos">  30</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos">  31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos">  32</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos">  33</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos">  34</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos">  35</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos">  36</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos">  37</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos">  38</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos">  39</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos">  40</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos">  41</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos">  42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos">  43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos">  44</span></a><span class="k">class</span> <span class="nc">Tags</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos">  45</span></a>    <span class="n">tested</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos">  46</span></a>    <span class="n">deep</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># can work with nested data structures</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos">  47</span></a>    <span class="n">superficial</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># can work with only single-layer of data</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos">  48</span></a>    <span class="n">multi_platform</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># serialized data can be deserialized by other languages/interpreters</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos">  49</span></a>    <span class="n">current_platform</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># serialized data can be deserialized by current type of python interpreter (only by CPython or only by PyPy for example)</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos">  50</span></a>    <span class="n">multicast</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># ?</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos">  51</span></a>    <span class="n">unique</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># ?</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos">  52</span></a>    <span class="n">can_use_set</span> <span class="o">=</span> <span class="mi">7</span>  <span class="c1"># can serialize set type</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos">  53</span></a>    <span class="n">can_use_bytes</span> <span class="o">=</span> <span class="mi">8</span>  <span class="c1"># can serialize bytes type</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos">  54</span></a>    <span class="n">can_use_custom_types</span> <span class="o">=</span> <span class="mi">9</span>  <span class="c1"># can serialize custom types</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos">  55</span></a>    <span class="n">can_use_lambda_functions</span> <span class="o">=</span> <span class="mi">10</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos">  56</span></a>    <span class="n">decode_str_as_str</span> <span class="o">=</span> <span class="mi">11</span>  <span class="c1"># does not convert strings to bytes</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos">  57</span></a>    <span class="n">decode_bytes_as_bytes</span> <span class="o">=</span> <span class="mi">12</span>  <span class="c1"># does not convert bytes to strings</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos">  58</span></a>    <span class="n">decode_str_and_bytes_as_requested</span> <span class="o">=</span> <span class="mi">13</span>  <span class="c1"># can chose: convert all str/bytes to str or to convert all str/bytes to bytes.</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos">  59</span></a>    <span class="n">decode_list_and_tuple_as_requested</span> <span class="o">=</span> <span class="mi">14</span>  <span class="c1"># can chose: convert all list/tuple to list or to convert all list/tuple to tuple.</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos">  60</span></a>    <span class="n">decode_tuple_as_tuple</span> <span class="o">=</span> <span class="mi">15</span>  <span class="c1"># does not conver tuples to list/set</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos">  61</span></a>    <span class="n">decode_list_as_list</span> <span class="o">=</span> <span class="mi">16</span>  <span class="c1"># does not convert lists to tuple/set</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos">  62</span></a>    <span class="n">explicit_format_version</span> <span class="o">=</span> <span class="mi">17</span>  <span class="c1"># Example: pickle can be of a different versions since python-version depent so it is Not tagged as an explicit_format_version.</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos">  63</span></a>    <span class="n">fast</span> <span class="o">=</span> <span class="mi">17</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos">  64</span></a>    <span class="n">compat</span> <span class="o">=</span> <span class="mi">18</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos">  65</span></a>    <span class="n">compat_with_python_below_3_8</span> <span class="o">=</span> <span class="mi">19</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos">  66</span></a>    <span class="n">compat_with_python_abowe_3_8</span> <span class="o">=</span> <span class="mi">20</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos">  67</span></a>    <span class="n">decode_set_as_set</span> <span class="o">=</span> <span class="mi">21</span>  <span class="c1"># does not convert sets to tuple/list</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos">  68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos">  69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos">  70</span></a><span class="k">class</span> <span class="nc">DataFormats</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos">  71</span></a>    <span class="nb">any</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># we don&#39;t care about the serialized data format</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos">  72</span></a>    <span class="n">json</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># serialized data is json</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos">  73</span></a>    <span class="n">binary</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># serialized data is binary (not really human-readable)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos">  74</span></a>    <span class="n">text</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># serialized data is human-readable</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos">  75</span></a>    <span class="n">yaml</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos">  76</span></a>    <span class="n">toml</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos">  77</span></a>    <span class="n">messagepack</span> <span class="o">=</span> <span class="mi">6</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos">  78</span></a>
</span><span id="L-79"><a href="#L-79"><span class="linenos">  79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos">  80</span></a><span class="n">SerializerFeatures</span> <span class="o">=</span> <span class="n">Set</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tags</span><span class="p">,</span> <span class="n">DataFormats</span><span class="p">]]</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos">  81</span></a><span class="n">SerializerFeaturesTuple</span> <span class="o">=</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Tags</span><span class="p">,</span> <span class="n">DataFormats</span><span class="p">]]</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos">  82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos">  83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos">  84</span></a><span class="c1"># !!! Keep an order! Add new serializers to the end of the list only !!!</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos">  85</span></a><span class="k">class</span> <span class="nc">Serializers</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos">  86</span></a>    <span class="n">json</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos">  87</span></a>    <span class="n">simplejson</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos">  88</span></a>    <span class="n">ujson</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos">  89</span></a>    <span class="n">orjson</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos">  90</span></a>    <span class="n">tnetstring</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos">  91</span></a>    <span class="n">pynetstring</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos">  92</span></a>    <span class="n">msgpack_fast</span> <span class="o">=</span> <span class="mi">6</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos">  93</span></a>    <span class="n">msgpack</span> <span class="o">=</span> <span class="mi">7</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos">  94</span></a>    <span class="n">cbor</span> <span class="o">=</span> <span class="mi">8</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos">  95</span></a>    <span class="n">cbor2</span> <span class="o">=</span> <span class="mi">9</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos">  96</span></a>    <span class="n">marshal</span> <span class="o">=</span> <span class="mi">10</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos">  97</span></a>    <span class="n">marshal_compat_4</span> <span class="o">=</span> <span class="mi">11</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos">  98</span></a>    <span class="n">marshal_compat_3</span> <span class="o">=</span> <span class="mi">12</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos">  99</span></a>    <span class="n">marshal_compat_2</span> <span class="o">=</span> <span class="mi">13</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos"> 100</span></a>    <span class="n">marshal_compat_1</span> <span class="o">=</span> <span class="mi">14</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos"> 101</span></a>    <span class="n">marshal_compat_0</span> <span class="o">=</span> <span class="mi">15</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos"> 102</span></a>    <span class="n">pickle</span> <span class="o">=</span> <span class="mi">16</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos"> 103</span></a>    <span class="n">pickle_default</span> <span class="o">=</span> <span class="mi">17</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos"> 104</span></a>    <span class="n">pickle_compat_5</span> <span class="o">=</span> <span class="mi">18</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos"> 105</span></a>    <span class="n">pickle_compat_4</span> <span class="o">=</span> <span class="mi">19</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos"> 106</span></a>    <span class="n">pickle_compat_3</span> <span class="o">=</span> <span class="mi">20</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos"> 107</span></a>    <span class="n">pickle_compat_2</span> <span class="o">=</span> <span class="mi">21</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos"> 108</span></a>    <span class="n">pickle_compat_1</span> <span class="o">=</span> <span class="mi">22</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos"> 109</span></a>    <span class="n">cpickle</span> <span class="o">=</span> <span class="mi">23</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos"> 110</span></a>    <span class="n">cpickle_default</span> <span class="o">=</span> <span class="mi">24</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos"> 111</span></a>    <span class="n">cpickle_compat_5</span> <span class="o">=</span> <span class="mi">25</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos"> 112</span></a>    <span class="n">cpickle_compat_4</span> <span class="o">=</span> <span class="mi">26</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos"> 113</span></a>    <span class="n">cpickle_compat_3</span> <span class="o">=</span> <span class="mi">27</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos"> 114</span></a>    <span class="n">cpickle_compat_2</span> <span class="o">=</span> <span class="mi">28</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos"> 115</span></a>    <span class="n">cpickle_compat_1</span> <span class="o">=</span> <span class="mi">29</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos"> 116</span></a>    <span class="n">cloudpickle</span> <span class="o">=</span> <span class="mi">30</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos"> 117</span></a>    <span class="n">cloudpickle_compat_5</span> <span class="o">=</span> <span class="mi">31</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos"> 118</span></a>    <span class="n">cloudpickle_compat_4</span> <span class="o">=</span> <span class="mi">32</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos"> 119</span></a>    <span class="n">cloudpickle_compat_3</span> <span class="o">=</span> <span class="mi">33</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos"> 120</span></a>    <span class="n">cloudpickle_compat_2</span> <span class="o">=</span> <span class="mi">34</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos"> 121</span></a>    <span class="n">cloudpickle_compat_1</span> <span class="o">=</span> <span class="mi">35</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos"> 122</span></a>    <span class="n">msgspec_json</span> <span class="o">=</span> <span class="mi">36</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos"> 123</span></a>    <span class="n">msgspec_messagepack</span> <span class="o">=</span> <span class="mi">37</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos"> 124</span></a>    <span class="n">msgspec_yaml</span> <span class="o">=</span> <span class="mi">38</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos"> 125</span></a>    <span class="n">msgspec_toml</span> <span class="o">=</span> <span class="mi">39</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos"> 126</span></a>
</span><span id="L-127"><a href="#L-127"><span class="linenos"> 127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos"> 128</span></a><span class="kn">import</span> <span class="nn">datetime</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos"> 129</span></a><span class="kn">import</span> <span class="nn">decimal</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos"> 130</span></a><span class="kn">import</span> <span class="nn">fractions</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos"> 131</span></a><span class="kn">import</span> <span class="nn">re</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos"> 132</span></a><span class="kn">from</span> <span class="nn">email.message</span> <span class="kn">import</span> <span class="n">Message</span> <span class="k">as</span> <span class="n">emailMessage</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos"> 133</span></a><span class="kn">import</span> <span class="nn">uuid</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos"> 134</span></a><span class="kn">import</span> <span class="nn">ipaddress</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos"> 135</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">CodeType</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos"> 136</span></a><span class="n">none_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos"> 137</span></a><span class="n">SUPPORTED_TYPES</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos"> 138</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">json</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos"> 139</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">simplejson</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos"> 140</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">ujson</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos"> 141</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">orjson</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos"> 142</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">tnetstring</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos"> 143</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">pynetstring</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos"> 144</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos"> 145</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack_fast</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos"> 146</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cbor</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos"> 147</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cbor2</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos"> 148</span></a>        <span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">,</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos"> 149</span></a>        <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">,</span> <span class="n">decimal</span><span class="o">.</span><span class="n">Decimal</span><span class="p">,</span> <span class="n">fractions</span><span class="o">.</span><span class="n">Fraction</span><span class="p">,</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos"> 150</span></a>        <span class="n">re</span><span class="o">.</span><span class="n">Pattern</span><span class="p">,</span> <span class="n">emailMessage</span><span class="p">,</span> <span class="n">uuid</span><span class="o">.</span><span class="n">UUID</span><span class="p">,</span> <span class="nb">set</span><span class="p">,</span> 
</span><span id="L-151"><a href="#L-151"><span class="linenos"> 151</span></a>        <span class="n">ipaddress</span><span class="o">.</span><span class="n">IPv4Address</span><span class="p">,</span> <span class="n">ipaddress</span><span class="o">.</span><span class="n">IPv6Address</span><span class="p">,</span> <span class="n">ipaddress</span><span class="o">.</span><span class="n">IPv4Network</span><span class="p">,</span> <span class="n">ipaddress</span><span class="o">.</span><span class="n">IPv6Network</span><span class="p">,</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos"> 152</span></a>    <span class="p">},</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos"> 153</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">marshal</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos"> 154</span></a>        <span class="nb">bool</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">complex</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">set</span><span class="p">,</span> <span class="nb">frozenset</span><span class="p">,</span> <span class="nb">dict</span><span class="p">,</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos"> 155</span></a>        <span class="n">CodeType</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="bp">Ellipsis</span><span class="p">,</span> <span class="ne">StopIteration</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos"> 156</span></a>    <span class="p">},</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos"> 157</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">pickle</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos"> 158</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cpickle</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos"> 159</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cloudpickle</span><span class="p">:</span> <span class="p">{},</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos"> 160</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos"> 161</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_json</span><span class="p">:</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">},</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos"> 162</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_yaml</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos"> 163</span></a>        <span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">none_type</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">list</span><span class="p">,</span> <span class="nb">dict</span><span class="p">,</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos"> 164</span></a>        <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">,</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos"> 165</span></a>    <span class="p">},</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos"> 166</span></a>    <span class="c1"># Serializers.msgspec_toml: {</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos"> 167</span></a>    <span class="c1">#     int, float, bool, none_type, str, list, dict,</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos"> 168</span></a>    <span class="c1">#     datetime.datetime, datetime.date, datetime.time,</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos"> 169</span></a>    <span class="c1"># },</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos"> 170</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_toml</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos"> 171</span></a>        <span class="nb">str</span><span class="p">,</span> <span class="nb">dict</span><span class="p">,</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos"> 172</span></a>        <span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">date</span><span class="p">,</span> <span class="n">datetime</span><span class="o">.</span><span class="n">time</span><span class="p">,</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos"> 173</span></a>    <span class="p">},</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos"> 174</span></a><span class="p">}</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos"> 175</span></a>
</span><span id="L-176"><a href="#L-176"><span class="linenos"> 176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos"> 177</span></a><span class="n">SERIALIZERS_DESCRIPTION</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos"> 178</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">json</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;json&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos"> 179</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos"> 180</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos"> 181</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos"> 182</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos"> 183</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos"> 184</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos"> 185</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos"> 186</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos"> 187</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos"> 188</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos"> 189</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos"> 190</span></a>    <span class="p">}),</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos"> 191</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">simplejson</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;simplejson&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos"> 192</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos"> 193</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos"> 194</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos"> 195</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos"> 196</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos"> 197</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos"> 198</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos"> 199</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos"> 200</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos"> 201</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos"> 202</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos"> 203</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos"> 204</span></a>    <span class="p">}),</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos"> 205</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">ujson</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;ujson&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos"> 206</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos"> 207</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos"> 208</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos"> 209</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos"> 210</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos"> 211</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos"> 212</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos"> 213</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos"> 214</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos"> 215</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos"> 216</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos"> 217</span></a>    <span class="p">}),</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos"> 218</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">orjson</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;orjson&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos"> 219</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos"> 220</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos"> 221</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos"> 222</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos"> 223</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos"> 224</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos"> 225</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos"> 226</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos"> 227</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos"> 228</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos"> 229</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos"> 230</span></a>    <span class="p">}),</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos"> 231</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">tnetstring</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;tnetstring&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos"> 232</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos"> 233</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos"> 234</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos"> 235</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos"> 236</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos"> 237</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos"> 238</span></a>    <span class="p">}),</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos"> 239</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">pynetstring</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;pynetstring&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos"> 240</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos"> 241</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos"> 242</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos"> 243</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos"> 244</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos"> 245</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos"> 246</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos"> 247</span></a>    <span class="p">}),</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos"> 248</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgpack&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos"> 249</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos"> 250</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos"> 251</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos"> 252</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos"> 253</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos"> 254</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos"> 255</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos"> 256</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos"> 257</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_and_bytes_as_requested</span><span class="p">,</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos"> 258</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_and_tuple_as_requested</span><span class="p">,</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos"> 259</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos"> 260</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos"> 261</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos"> 262</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos"> 263</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">messagepack</span><span class="p">,</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos"> 264</span></a>    <span class="p">}),</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos"> 265</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack_fast</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgpack_fast&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos"> 266</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos"> 267</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos"> 268</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos"> 269</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos"> 270</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos"> 271</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos"> 272</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos"> 273</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos"> 274</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_and_bytes_as_requested</span><span class="p">,</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos"> 275</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_and_tuple_as_requested</span><span class="p">,</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos"> 276</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_tuple_as_tuple</span><span class="p">,</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos"> 277</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos"> 278</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos"> 279</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos"> 280</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">messagepack</span><span class="p">,</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos"> 281</span></a>    <span class="p">}),</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos"> 282</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cbor</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;cbor&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos"> 283</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos"> 284</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos"> 285</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos"> 286</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos"> 287</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos"> 288</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos"> 289</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos"> 290</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos"> 291</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos"> 292</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos"> 293</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos"> 294</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos"> 295</span></a>    <span class="p">}),</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos"> 296</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cbor2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;cbor2&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos"> 297</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos"> 298</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos"> 299</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos"> 300</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos"> 301</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos"> 302</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos"> 303</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos"> 304</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos"> 305</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos"> 306</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos"> 307</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos"> 308</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos"> 309</span></a>    <span class="p">}),</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos"> 310</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">marshal</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;marshal&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos"> 311</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos"> 312</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos"> 313</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos"> 314</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos"> 315</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos"> 316</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos"> 317</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos"> 318</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos"> 319</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_tuple_as_tuple</span><span class="p">,</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos"> 320</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos"> 321</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos"> 322</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos"> 323</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos"> 324</span></a>    <span class="p">}),</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos"> 325</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">pickle</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;pickle&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos"> 326</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos"> 327</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos"> 328</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos"> 329</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos"> 330</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos"> 331</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos"> 332</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_custom_types</span><span class="p">,</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos"> 333</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos"> 334</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos"> 335</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_tuple_as_tuple</span><span class="p">,</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos"> 336</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos"> 337</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos"> 338</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos"> 339</span></a>    <span class="p">}),</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos"> 340</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cpickle</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;cPickle&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos"> 341</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos"> 342</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos"> 343</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos"> 344</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos"> 345</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos"> 346</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_custom_types</span><span class="p">,</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos"> 347</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos"> 348</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos"> 349</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_tuple_as_tuple</span><span class="p">,</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos"> 350</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos"> 351</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos"> 352</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos"> 353</span></a>    <span class="p">}),</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos"> 354</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">cloudpickle</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;cloudpickle&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos"> 355</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos"> 356</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos"> 357</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos"> 358</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos"> 359</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos"> 360</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_custom_types</span><span class="p">,</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos"> 361</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_lambda_functions</span><span class="p">,</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos"> 362</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos"> 363</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos"> 364</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_tuple_as_tuple</span><span class="p">,</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos"> 365</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos"> 366</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos"> 367</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos"> 368</span></a>    <span class="p">}),</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos"> 369</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgspec_messagepack&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos"> 370</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos"> 371</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos"> 372</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos"> 373</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos"> 374</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos"> 375</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos"> 376</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_bytes</span><span class="p">,</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos"> 377</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos"> 378</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_bytes_as_bytes</span><span class="p">,</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos"> 379</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos"> 380</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos"> 381</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos"> 382</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">binary</span><span class="p">,</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos"> 383</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">messagepack</span><span class="p">,</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos"> 384</span></a>    <span class="p">}),</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos"> 385</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_json</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgspec_json&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos"> 386</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos"> 387</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos"> 388</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos"> 389</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos"> 390</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos"> 391</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos"> 392</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos"> 393</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos"> 394</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos"> 395</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos"> 396</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos"> 397</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos"> 398</span></a>    <span class="p">}),</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos"> 399</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_yaml</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgspec_yaml&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos"> 400</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos"> 401</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos"> 402</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos"> 403</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos"> 404</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos"> 405</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos"> 406</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos"> 407</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos"> 408</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos"> 409</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos"> 410</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">yaml</span><span class="p">,</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos"> 411</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos"> 412</span></a>    <span class="p">}),</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos"> 413</span></a>    <span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_toml</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;msgspec_toml&#39;</span><span class="p">,</span> <span class="p">{</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos"> 414</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">tested</span><span class="p">,</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos"> 415</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">deep</span><span class="p">,</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos"> 416</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos"> 417</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">multi_platform</span><span class="p">,</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos"> 418</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">,</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos"> 419</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">can_use_set</span><span class="p">,</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos"> 420</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos"> 421</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos"> 422</span></a>        <span class="n">Tags</span><span class="o">.</span><span class="n">explicit_format_version</span><span class="p">,</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos"> 423</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">any</span><span class="p">,</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos"> 424</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">toml</span><span class="p">,</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos"> 425</span></a>        <span class="n">DataFormats</span><span class="o">.</span><span class="n">text</span><span class="p">,</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos"> 426</span></a>    <span class="p">}),</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos"> 427</span></a><span class="p">}</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos"> 428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos"> 429</span></a>
</span><span id="L-430"><a href="#L-430"><span class="linenos"> 430</span></a><span class="n">ujson_dump_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;skipkeys&#39;</span><span class="p">,</span> <span class="s1">&#39;check_circular&#39;</span><span class="p">,</span> <span class="s1">&#39;allow_nan&#39;</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;separators&#39;</span><span class="p">,</span> <span class="s1">&#39;default&#39;</span><span class="p">}</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos"> 431</span></a><span class="n">ujson_dumps_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;skipkeys&#39;</span><span class="p">,</span> <span class="s1">&#39;check_circular&#39;</span><span class="p">,</span> <span class="s1">&#39;allow_nan&#39;</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;separators&#39;</span><span class="p">,</span> <span class="s1">&#39;default&#39;</span><span class="p">}</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos"> 432</span></a><span class="n">ujson_load_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;object_hook&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_float&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_int&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_constant&#39;</span><span class="p">,</span> <span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">}</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos"> 433</span></a><span class="n">ujson_loads_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;object_hook&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_float&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_int&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_constant&#39;</span><span class="p">,</span> <span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">}</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos"> 434</span></a>
</span><span id="L-435"><a href="#L-435"><span class="linenos"> 435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos"> 436</span></a><span class="n">orjson_dump_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;skipkeys&#39;</span><span class="p">,</span> <span class="s1">&#39;check_circular&#39;</span><span class="p">,</span> <span class="s1">&#39;allow_nan&#39;</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;separators&#39;</span><span class="p">,</span> <span class="s1">&#39;default&#39;</span><span class="p">}</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos"> 437</span></a><span class="n">orjson_dumps_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;skipkeys&#39;</span><span class="p">,</span> <span class="s1">&#39;check_circular&#39;</span><span class="p">,</span> <span class="s1">&#39;allow_nan&#39;</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;separators&#39;</span><span class="p">,</span> <span class="s1">&#39;default&#39;</span><span class="p">}</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos"> 438</span></a><span class="n">orjson_load_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;object_hook&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_float&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_int&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_constant&#39;</span><span class="p">,</span> <span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">}</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos"> 439</span></a><span class="n">orjson_loads_skip_parameters</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;cls&#39;</span><span class="p">,</span> <span class="s1">&#39;object_hook&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_float&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_int&#39;</span><span class="p">,</span> <span class="s1">&#39;parse_constant&#39;</span><span class="p">,</span> <span class="s1">&#39;object_pairs_hook&#39;</span><span class="p">}</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos"> 440</span></a>
</span><span id="L-441"><a href="#L-441"><span class="linenos"> 441</span></a>
</span><span id="L-442"><a href="#L-442"><span class="linenos"> 442</span></a><span class="n">EXISTING_SERIALIZERS</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>  <span class="c1"># type: Set[Serializers]</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos"> 443</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;json&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">json</span><span class="p">:</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos"> 444</span></a>    <span class="k">if</span> <span class="n">json</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos"> 445</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">json</span><span class="p">)</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos"> 446</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;simplejson&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">simplejson</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos"> 447</span></a>    <span class="k">if</span> <span class="n">simplejson</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos"> 448</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">simplejson</span><span class="p">)</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos"> 449</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;ujson&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">ujson</span><span class="p">:</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos"> 450</span></a>    <span class="k">if</span> <span class="n">ujson</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos"> 451</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">ujson</span><span class="p">)</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos"> 452</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;orjson&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">orjson</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos"> 453</span></a>    <span class="k">if</span> <span class="n">orjson</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos"> 454</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">orjson</span><span class="p">)</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos"> 455</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;tnetstring&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">tnetstring</span><span class="p">:</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos"> 456</span></a>    <span class="k">if</span> <span class="n">tnetstring</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos"> 457</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">tnetstring</span><span class="p">)</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos"> 458</span></a><span class="c1"># with alt_import(&#39;pynetstring&#39;) as pynetstring:</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos"> 459</span></a><span class="c1">#     if pynetstring is not None:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos"> 460</span></a><span class="c1">#         EXISTING_SERIALIZERS.add(Serializers.pynetstring)</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos"> 461</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;msgpack&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">msgpack</span><span class="p">:</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos"> 462</span></a>    <span class="k">if</span> <span class="n">msgpack</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos"> 463</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack_fast</span><span class="p">)</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos"> 464</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgpack</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos"> 465</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;msgspec&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">msgspec</span><span class="p">:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos"> 466</span></a>    <span class="k">if</span> <span class="n">msgspec</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos"> 467</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_messagepack</span><span class="p">)</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos"> 468</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_json</span><span class="p">)</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos"> 469</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_yaml</span><span class="p">)</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos"> 470</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">msgspec_toml</span><span class="p">)</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos"> 471</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;cbor&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">cbor</span><span class="p">:</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos"> 472</span></a>    <span class="k">if</span> <span class="n">cbor</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos"> 473</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">cbor</span><span class="p">)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos"> 474</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;cbor2&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">cbor2</span><span class="p">:</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos"> 475</span></a>    <span class="k">if</span> <span class="n">cbor2</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos"> 476</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">cbor2</span><span class="p">)</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos"> 477</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;marshal&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">marshal</span><span class="p">:</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos"> 478</span></a>    <span class="k">if</span> <span class="n">marshal</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos"> 479</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">marshal</span><span class="p">)</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos"> 480</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;pickle&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">pickle</span><span class="p">:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos"> 481</span></a>    <span class="k">if</span> <span class="n">pickle</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos"> 482</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">pickle</span><span class="p">)</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos"> 483</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;cPickle&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">cPickle</span><span class="p">:</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos"> 484</span></a>    <span class="k">if</span> <span class="n">cPickle</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos"> 485</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">cpickle</span><span class="p">)</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos"> 486</span></a><span class="k">with</span> <span class="n">alt_import</span><span class="p">(</span><span class="s1">&#39;cloudpickle&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">cloudpickle</span><span class="p">:</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos"> 487</span></a>    <span class="k">if</span> <span class="n">cloudpickle</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos"> 488</span></a>        <span class="n">EXISTING_SERIALIZERS</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Serializers</span><span class="o">.</span><span class="n">cloudpickle</span><span class="p">)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos"> 489</span></a>
</span><span id="L-490"><a href="#L-490"><span class="linenos"> 490</span></a>
</span><span id="L-491"><a href="#L-491"><span class="linenos"> 491</span></a><span class="k">class</span> <span class="nc">Serializer</span><span class="p">:</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos"> 492</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serializer</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="n">Serializers</span><span class="p">]):</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos"> 493</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos"> 494</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos"> 495</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos"> 496</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos"> 497</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos"> 498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">serializer</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos"> 499</span></a>
</span><span id="L-500"><a href="#L-500"><span class="linenos"> 500</span></a>    <span class="nd">@property</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos"> 501</span></a>    <span class="k">def</span> <span class="nf">serializer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos"> 502</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos"> 503</span></a>
</span><span id="L-504"><a href="#L-504"><span class="linenos"> 504</span></a>    <span class="nd">@serializer</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos"> 505</span></a>    <span class="k">def</span> <span class="nf">serializer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serializer</span><span class="p">:</span> <span class="n">Serializers</span><span class="p">):</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos"> 506</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="o">=</span> <span class="n">serializer</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos"> 507</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos"> 508</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos"> 509</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos"> 510</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos"> 511</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos"> 512</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos"> 513</span></a>            <span class="n">serializer_name</span><span class="p">,</span> <span class="n">serializer_tags</span> <span class="o">=</span> <span class="n">SERIALIZERS_DESCRIPTION</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span><span class="p">]</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos"> 514</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__dump&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos"> 515</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__dumps&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos"> 516</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__load&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos"> 517</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__loads&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos"> 518</span></a>
</span><span id="L-519"><a href="#L-519"><span class="linenos"> 519</span></a>    <span class="c1"># json</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos"> 520</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos"> 521</span></a>    <span class="k">def</span> <span class="nf">_json__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos"> 522</span></a>        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos"> 523</span></a>
</span><span id="L-524"><a href="#L-524"><span class="linenos"> 524</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos"> 525</span></a>    <span class="k">def</span> <span class="nf">_json__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos"> 526</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos"> 527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos"> 528</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos"> 529</span></a>    <span class="k">def</span> <span class="nf">_json__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos"> 530</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos"> 531</span></a>
</span><span id="L-532"><a href="#L-532"><span class="linenos"> 532</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos"> 533</span></a>    <span class="k">def</span> <span class="nf">_json__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos"> 534</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos"> 535</span></a>
</span><span id="L-536"><a href="#L-536"><span class="linenos"> 536</span></a>    <span class="c1"># simplejson</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos"> 537</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos"> 538</span></a>    <span class="k">def</span> <span class="nf">_simplejson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos"> 539</span></a>        <span class="n">simplejson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos"> 540</span></a>
</span><span id="L-541"><a href="#L-541"><span class="linenos"> 541</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos"> 542</span></a>    <span class="k">def</span> <span class="nf">_simplejson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos"> 543</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos"> 544</span></a>
</span><span id="L-545"><a href="#L-545"><span class="linenos"> 545</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos"> 546</span></a>    <span class="k">def</span> <span class="nf">_simplejson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos"> 547</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos"> 548</span></a>
</span><span id="L-549"><a href="#L-549"><span class="linenos"> 549</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos"> 550</span></a>    <span class="k">def</span> <span class="nf">_simplejson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos"> 551</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos"> 552</span></a>
</span><span id="L-553"><a href="#L-553"><span class="linenos"> 553</span></a>    <span class="c1"># ujson</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos"> 554</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos"> 555</span></a>    <span class="k">def</span> <span class="nf">_ujson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos"> 556</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_dump_skip_parameters</span><span class="p">:</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos"> 557</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos"> 558</span></a>        <span class="n">ujson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos"> 559</span></a>
</span><span id="L-560"><a href="#L-560"><span class="linenos"> 560</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos"> 561</span></a>    <span class="k">def</span> <span class="nf">_ujson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos"> 562</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_dumps_skip_parameters</span><span class="p">:</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos"> 563</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos"> 564</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos"> 565</span></a>
</span><span id="L-566"><a href="#L-566"><span class="linenos"> 566</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos"> 567</span></a>    <span class="k">def</span> <span class="nf">_ujson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos"> 568</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_load_skip_parameters</span><span class="p">:</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos"> 569</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos"> 570</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos"> 571</span></a>
</span><span id="L-572"><a href="#L-572"><span class="linenos"> 572</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos"> 573</span></a>    <span class="k">def</span> <span class="nf">_ujson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos"> 574</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_loads_skip_parameters</span><span class="p">:</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos"> 575</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos"> 576</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos"> 577</span></a>
</span><span id="L-578"><a href="#L-578"><span class="linenos"> 578</span></a>    <span class="c1"># orjson</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos"> 579</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos"> 580</span></a>    <span class="k">def</span> <span class="nf">_orjson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos"> 581</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_dump_skip_parameters</span><span class="p">:</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos"> 582</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos"> 583</span></a>        <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;option&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">orjson</span><span class="o">.</span><span class="n">OPT_NON_STR_KEYS</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos"> 584</span></a>        <span class="n">orjson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos"> 585</span></a>
</span><span id="L-586"><a href="#L-586"><span class="linenos"> 586</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos"> 587</span></a>    <span class="k">def</span> <span class="nf">_orjson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos"> 588</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_dumps_skip_parameters</span><span class="p">:</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos"> 589</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos"> 590</span></a>        <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;option&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">orjson</span><span class="o">.</span><span class="n">OPT_NON_STR_KEYS</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos"> 591</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos"> 592</span></a>
</span><span id="L-593"><a href="#L-593"><span class="linenos"> 593</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos"> 594</span></a>    <span class="k">def</span> <span class="nf">_orjson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos"> 595</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_load_skip_parameters</span><span class="p">:</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos"> 596</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos"> 597</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos"> 598</span></a>
</span><span id="L-599"><a href="#L-599"><span class="linenos"> 599</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos"> 600</span></a>    <span class="k">def</span> <span class="nf">_orjson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos"> 601</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_loads_skip_parameters</span><span class="p">:</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos"> 602</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos"> 603</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos"> 604</span></a>
</span><span id="L-605"><a href="#L-605"><span class="linenos"> 605</span></a>    <span class="c1"># tnetstring</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos"> 606</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos"> 607</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos"> 608</span></a>        <span class="n">tnetstring</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos"> 609</span></a>
</span><span id="L-610"><a href="#L-610"><span class="linenos"> 610</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos"> 611</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos"> 612</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos"> 613</span></a>
</span><span id="L-614"><a href="#L-614"><span class="linenos"> 614</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos"> 615</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos"> 616</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos"> 617</span></a>
</span><span id="L-618"><a href="#L-618"><span class="linenos"> 618</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos"> 619</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos"> 620</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos"> 621</span></a>
</span><span id="L-622"><a href="#L-622"><span class="linenos"> 622</span></a>    <span class="c1"># msgpack</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos"> 623</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos"> 624</span></a>    <span class="k">def</span> <span class="nf">_msgpack__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos"> 625</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos"> 626</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated.</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos"> 627</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos"> 628</span></a>        <span class="p">}</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos"> 629</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos"> 630</span></a>        <span class="n">msgpack</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos"> 631</span></a>
</span><span id="L-632"><a href="#L-632"><span class="linenos"> 632</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos"> 633</span></a>    <span class="k">def</span> <span class="nf">_msgpack__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos"> 634</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos"> 635</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated.</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos"> 636</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos"> 637</span></a>        <span class="p">}</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos"> 638</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos"> 639</span></a>        <span class="k">return</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos"> 640</span></a>
</span><span id="L-641"><a href="#L-641"><span class="linenos"> 641</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos"> 642</span></a>    <span class="k">def</span> <span class="nf">_msgpack__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos"> 643</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos"> 644</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos"> 645</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos"> 646</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos"> 647</span></a>            <span class="s1">&#39;strict_map_key&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos"> 648</span></a>        <span class="p">}</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos"> 649</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos"> 650</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos"> 651</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos"> 652</span></a>        
</span><span id="L-653"><a href="#L-653"><span class="linenos"> 653</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos"> 654</span></a>
</span><span id="L-655"><a href="#L-655"><span class="linenos"> 655</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos"> 656</span></a>    <span class="k">def</span> <span class="nf">_msgpack__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos"> 657</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos"> 658</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos"> 659</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos"> 660</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos"> 661</span></a>            <span class="s1">&#39;strict_map_key&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos"> 662</span></a>        <span class="p">}</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos"> 663</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos"> 664</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos"> 665</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos"> 666</span></a>        
</span><span id="L-667"><a href="#L-667"><span class="linenos"> 667</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos"> 668</span></a>
</span><span id="L-669"><a href="#L-669"><span class="linenos"> 669</span></a>    <span class="c1"># msgpack_fast</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos"> 670</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos"> 671</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos"> 672</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos"> 673</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos"> 674</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos"> 675</span></a>        <span class="p">}</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos"> 676</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos"> 677</span></a>        <span class="n">msgpack</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos"> 678</span></a>
</span><span id="L-679"><a href="#L-679"><span class="linenos"> 679</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos"> 680</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos"> 681</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos"> 682</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos"> 683</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos"> 684</span></a>        <span class="p">}</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos"> 685</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos"> 686</span></a>        <span class="k">return</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos"> 687</span></a>
</span><span id="L-688"><a href="#L-688"><span class="linenos"> 688</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos"> 689</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos"> 690</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos"> 691</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos"> 692</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos"> 693</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">False</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos"> 694</span></a>        <span class="p">}</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos"> 695</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos"> 696</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos"> 697</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-698"><a href="#L-698"><span class="linenos"> 698</span></a>        
</span><span id="L-699"><a href="#L-699"><span class="linenos"> 699</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos"> 700</span></a>
</span><span id="L-701"><a href="#L-701"><span class="linenos"> 701</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos"> 702</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos"> 703</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos"> 704</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos"> 705</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos"> 706</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">False</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos"> 707</span></a>        <span class="p">}</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos"> 708</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos"> 709</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos"> 710</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos"> 711</span></a>        
</span><span id="L-712"><a href="#L-712"><span class="linenos"> 712</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos"> 713</span></a>
</span><span id="L-714"><a href="#L-714"><span class="linenos"> 714</span></a>    <span class="c1"># msgspec_messagepack</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos"> 715</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-716"><a href="#L-716"><span class="linenos"> 716</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos"> 717</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos"> 718</span></a>
</span><span id="L-719"><a href="#L-719"><span class="linenos"> 719</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos"> 720</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos"> 721</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos"> 722</span></a>
</span><span id="L-723"><a href="#L-723"><span class="linenos"> 723</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos"> 724</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-725"><a href="#L-725"><span class="linenos"> 725</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos"> 726</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos"> 727</span></a>        
</span><span id="L-728"><a href="#L-728"><span class="linenos"> 728</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos"> 729</span></a>
</span><span id="L-730"><a href="#L-730"><span class="linenos"> 730</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos"> 731</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos"> 732</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos"> 733</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos"> 734</span></a>        
</span><span id="L-735"><a href="#L-735"><span class="linenos"> 735</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos"> 736</span></a>
</span><span id="L-737"><a href="#L-737"><span class="linenos"> 737</span></a>    <span class="c1"># msgspec_json</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos"> 738</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos"> 739</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-740"><a href="#L-740"><span class="linenos"> 740</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos"> 741</span></a>
</span><span id="L-742"><a href="#L-742"><span class="linenos"> 742</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos"> 743</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos"> 744</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-745"><a href="#L-745"><span class="linenos"> 745</span></a>
</span><span id="L-746"><a href="#L-746"><span class="linenos"> 746</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-747"><a href="#L-747"><span class="linenos"> 747</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-748"><a href="#L-748"><span class="linenos"> 748</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos"> 749</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos"> 750</span></a>        
</span><span id="L-751"><a href="#L-751"><span class="linenos"> 751</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-752"><a href="#L-752"><span class="linenos"> 752</span></a>
</span><span id="L-753"><a href="#L-753"><span class="linenos"> 753</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos"> 754</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-755"><a href="#L-755"><span class="linenos"> 755</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos"> 756</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos"> 757</span></a>        
</span><span id="L-758"><a href="#L-758"><span class="linenos"> 758</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-759"><a href="#L-759"><span class="linenos"> 759</span></a>
</span><span id="L-760"><a href="#L-760"><span class="linenos"> 760</span></a>    <span class="c1"># msgspec_yaml</span>
</span><span id="L-761"><a href="#L-761"><span class="linenos"> 761</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-762"><a href="#L-762"><span class="linenos"> 762</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos"> 763</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos"> 764</span></a>
</span><span id="L-765"><a href="#L-765"><span class="linenos"> 765</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-766"><a href="#L-766"><span class="linenos"> 766</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos"> 767</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos"> 768</span></a>
</span><span id="L-769"><a href="#L-769"><span class="linenos"> 769</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos"> 770</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-771"><a href="#L-771"><span class="linenos"> 771</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-772"><a href="#L-772"><span class="linenos"> 772</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos"> 773</span></a>        
</span><span id="L-774"><a href="#L-774"><span class="linenos"> 774</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos"> 775</span></a>
</span><span id="L-776"><a href="#L-776"><span class="linenos"> 776</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-777"><a href="#L-777"><span class="linenos"> 777</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos"> 778</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-779"><a href="#L-779"><span class="linenos"> 779</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos"> 780</span></a>        
</span><span id="L-781"><a href="#L-781"><span class="linenos"> 781</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-782"><a href="#L-782"><span class="linenos"> 782</span></a>
</span><span id="L-783"><a href="#L-783"><span class="linenos"> 783</span></a>    <span class="c1"># msgspec_toml</span>
</span><span id="L-784"><a href="#L-784"><span class="linenos"> 784</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-785"><a href="#L-785"><span class="linenos"> 785</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-786"><a href="#L-786"><span class="linenos"> 786</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos"> 787</span></a>
</span><span id="L-788"><a href="#L-788"><span class="linenos"> 788</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-789"><a href="#L-789"><span class="linenos"> 789</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-790"><a href="#L-790"><span class="linenos"> 790</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos"> 791</span></a>
</span><span id="L-792"><a href="#L-792"><span class="linenos"> 792</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos"> 793</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos"> 794</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-795"><a href="#L-795"><span class="linenos"> 795</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos"> 796</span></a>        
</span><span id="L-797"><a href="#L-797"><span class="linenos"> 797</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-798"><a href="#L-798"><span class="linenos"> 798</span></a>
</span><span id="L-799"><a href="#L-799"><span class="linenos"> 799</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos"> 800</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-801"><a href="#L-801"><span class="linenos"> 801</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos"> 802</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos"> 803</span></a>        
</span><span id="L-804"><a href="#L-804"><span class="linenos"> 804</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-805"><a href="#L-805"><span class="linenos"> 805</span></a>
</span><span id="L-806"><a href="#L-806"><span class="linenos"> 806</span></a>    <span class="c1"># cbor</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos"> 807</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-808"><a href="#L-808"><span class="linenos"> 808</span></a>    <span class="k">def</span> <span class="nf">_cbor__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos"> 809</span></a>        <span class="n">cbor</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos"> 810</span></a>
</span><span id="L-811"><a href="#L-811"><span class="linenos"> 811</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-812"><a href="#L-812"><span class="linenos"> 812</span></a>    <span class="k">def</span> <span class="nf">_cbor__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-813"><a href="#L-813"><span class="linenos"> 813</span></a>        <span class="k">return</span> <span class="n">cbor</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos"> 814</span></a>
</span><span id="L-815"><a href="#L-815"><span class="linenos"> 815</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-816"><a href="#L-816"><span class="linenos"> 816</span></a>    <span class="k">def</span> <span class="nf">_cbor__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos"> 817</span></a>        <span class="n">cbor</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos"> 818</span></a>
</span><span id="L-819"><a href="#L-819"><span class="linenos"> 819</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-820"><a href="#L-820"><span class="linenos"> 820</span></a>    <span class="k">def</span> <span class="nf">_cbor__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-821"><a href="#L-821"><span class="linenos"> 821</span></a>        <span class="k">return</span> <span class="n">cbor</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos"> 822</span></a>
</span><span id="L-823"><a href="#L-823"><span class="linenos"> 823</span></a>    <span class="c1"># cbor2</span>
</span><span id="L-824"><a href="#L-824"><span class="linenos"> 824</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-825"><a href="#L-825"><span class="linenos"> 825</span></a>    <span class="k">def</span> <span class="nf">_cbor2__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-826"><a href="#L-826"><span class="linenos"> 826</span></a>        <span class="n">cbor2</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos"> 827</span></a>
</span><span id="L-828"><a href="#L-828"><span class="linenos"> 828</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-829"><a href="#L-829"><span class="linenos"> 829</span></a>    <span class="k">def</span> <span class="nf">_cbor2__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-830"><a href="#L-830"><span class="linenos"> 830</span></a>        <span class="k">return</span> <span class="n">cbor2</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-831"><a href="#L-831"><span class="linenos"> 831</span></a>
</span><span id="L-832"><a href="#L-832"><span class="linenos"> 832</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos"> 833</span></a>    <span class="k">def</span> <span class="nf">_cbor2__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos"> 834</span></a>        <span class="n">cbor2</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-835"><a href="#L-835"><span class="linenos"> 835</span></a>
</span><span id="L-836"><a href="#L-836"><span class="linenos"> 836</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-837"><a href="#L-837"><span class="linenos"> 837</span></a>    <span class="k">def</span> <span class="nf">_cbor2__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos"> 838</span></a>        <span class="k">return</span> <span class="n">cbor2</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-839"><a href="#L-839"><span class="linenos"> 839</span></a>
</span><span id="L-840"><a href="#L-840"><span class="linenos"> 840</span></a>    <span class="c1"># marshal</span>
</span><span id="L-841"><a href="#L-841"><span class="linenos"> 841</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-842"><a href="#L-842"><span class="linenos"> 842</span></a>    <span class="k">def</span> <span class="nf">_marshal__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-843"><a href="#L-843"><span class="linenos"> 843</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="L-844"><a href="#L-844"><span class="linenos"> 844</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-845"><a href="#L-845"><span class="linenos"> 845</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-846"><a href="#L-846"><span class="linenos"> 846</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">args</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="L-847"><a href="#L-847"><span class="linenos"> 847</span></a>        <span class="n">marshal</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">result_args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-848"><a href="#L-848"><span class="linenos"> 848</span></a>
</span><span id="L-849"><a href="#L-849"><span class="linenos"> 849</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-850"><a href="#L-850"><span class="linenos"> 850</span></a>    <span class="k">def</span> <span class="nf">_marshal__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-851"><a href="#L-851"><span class="linenos"> 851</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-852"><a href="#L-852"><span class="linenos"> 852</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-853"><a href="#L-853"><span class="linenos"> 853</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-854"><a href="#L-854"><span class="linenos"> 854</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="L-855"><a href="#L-855"><span class="linenos"> 855</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">result_args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-856"><a href="#L-856"><span class="linenos"> 856</span></a>
</span><span id="L-857"><a href="#L-857"><span class="linenos"> 857</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-858"><a href="#L-858"><span class="linenos"> 858</span></a>    <span class="k">def</span> <span class="nf">_marshal__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-859"><a href="#L-859"><span class="linenos"> 859</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-860"><a href="#L-860"><span class="linenos"> 860</span></a>
</span><span id="L-861"><a href="#L-861"><span class="linenos"> 861</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-862"><a href="#L-862"><span class="linenos"> 862</span></a>    <span class="k">def</span> <span class="nf">_marshal__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-863"><a href="#L-863"><span class="linenos"> 863</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-864"><a href="#L-864"><span class="linenos"> 864</span></a>
</span><span id="L-865"><a href="#L-865"><span class="linenos"> 865</span></a>    <span class="c1"># pickle</span>
</span><span id="L-866"><a href="#L-866"><span class="linenos"> 866</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-867"><a href="#L-867"><span class="linenos"> 867</span></a>    <span class="k">def</span> <span class="nf">_pickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-868"><a href="#L-868"><span class="linenos"> 868</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-869"><a href="#L-869"><span class="linenos"> 869</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-870"><a href="#L-870"><span class="linenos"> 870</span></a>        <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-871"><a href="#L-871"><span class="linenos"> 871</span></a>
</span><span id="L-872"><a href="#L-872"><span class="linenos"> 872</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-873"><a href="#L-873"><span class="linenos"> 873</span></a>    <span class="k">def</span> <span class="nf">_pickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-874"><a href="#L-874"><span class="linenos"> 874</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-875"><a href="#L-875"><span class="linenos"> 875</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-876"><a href="#L-876"><span class="linenos"> 876</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-877"><a href="#L-877"><span class="linenos"> 877</span></a>
</span><span id="L-878"><a href="#L-878"><span class="linenos"> 878</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-879"><a href="#L-879"><span class="linenos"> 879</span></a>    <span class="k">def</span> <span class="nf">_pickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-880"><a href="#L-880"><span class="linenos"> 880</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-881"><a href="#L-881"><span class="linenos"> 881</span></a>
</span><span id="L-882"><a href="#L-882"><span class="linenos"> 882</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-883"><a href="#L-883"><span class="linenos"> 883</span></a>    <span class="k">def</span> <span class="nf">_pickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-884"><a href="#L-884"><span class="linenos"> 884</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-885"><a href="#L-885"><span class="linenos"> 885</span></a>
</span><span id="L-886"><a href="#L-886"><span class="linenos"> 886</span></a>    <span class="c1"># cPickle</span>
</span><span id="L-887"><a href="#L-887"><span class="linenos"> 887</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-888"><a href="#L-888"><span class="linenos"> 888</span></a>    <span class="k">def</span> <span class="nf">_cpickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-889"><a href="#L-889"><span class="linenos"> 889</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-890"><a href="#L-890"><span class="linenos"> 890</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-891"><a href="#L-891"><span class="linenos"> 891</span></a>        <span class="n">cPickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-892"><a href="#L-892"><span class="linenos"> 892</span></a>
</span><span id="L-893"><a href="#L-893"><span class="linenos"> 893</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-894"><a href="#L-894"><span class="linenos"> 894</span></a>    <span class="k">def</span> <span class="nf">_cpickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-895"><a href="#L-895"><span class="linenos"> 895</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-896"><a href="#L-896"><span class="linenos"> 896</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-897"><a href="#L-897"><span class="linenos"> 897</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-898"><a href="#L-898"><span class="linenos"> 898</span></a>
</span><span id="L-899"><a href="#L-899"><span class="linenos"> 899</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-900"><a href="#L-900"><span class="linenos"> 900</span></a>    <span class="k">def</span> <span class="nf">_cpickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-901"><a href="#L-901"><span class="linenos"> 901</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-902"><a href="#L-902"><span class="linenos"> 902</span></a>
</span><span id="L-903"><a href="#L-903"><span class="linenos"> 903</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-904"><a href="#L-904"><span class="linenos"> 904</span></a>    <span class="k">def</span> <span class="nf">_cpickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-905"><a href="#L-905"><span class="linenos"> 905</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-906"><a href="#L-906"><span class="linenos"> 906</span></a>
</span><span id="L-907"><a href="#L-907"><span class="linenos"> 907</span></a>    <span class="c1"># cloudpickle</span>
</span><span id="L-908"><a href="#L-908"><span class="linenos"> 908</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-909"><a href="#L-909"><span class="linenos"> 909</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-910"><a href="#L-910"><span class="linenos"> 910</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-911"><a href="#L-911"><span class="linenos"> 911</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-912"><a href="#L-912"><span class="linenos"> 912</span></a>        <span class="n">cloudpickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-913"><a href="#L-913"><span class="linenos"> 913</span></a>
</span><span id="L-914"><a href="#L-914"><span class="linenos"> 914</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-915"><a href="#L-915"><span class="linenos"> 915</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-916"><a href="#L-916"><span class="linenos"> 916</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="L-917"><a href="#L-917"><span class="linenos"> 917</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-918"><a href="#L-918"><span class="linenos"> 918</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="L-919"><a href="#L-919"><span class="linenos"> 919</span></a>
</span><span id="L-920"><a href="#L-920"><span class="linenos"> 920</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-921"><a href="#L-921"><span class="linenos"> 921</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-922"><a href="#L-922"><span class="linenos"> 922</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-923"><a href="#L-923"><span class="linenos"> 923</span></a>
</span><span id="L-924"><a href="#L-924"><span class="linenos"> 924</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-925"><a href="#L-925"><span class="linenos"> 925</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-926"><a href="#L-926"><span class="linenos"> 926</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-927"><a href="#L-927"><span class="linenos"> 927</span></a>
</span><span id="L-928"><a href="#L-928"><span class="linenos"> 928</span></a>
</span><span id="L-929"><a href="#L-929"><span class="linenos"> 929</span></a><span class="k">def</span> <span class="nf">get_an_appropriate_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Serializers</span><span class="p">]:</span>
</span><span id="L-930"><a href="#L-930"><span class="linenos"> 930</span></a>    <span class="n">appropriate_serializers</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-931"><a href="#L-931"><span class="linenos"> 931</span></a>    <span class="k">for</span> <span class="n">serializer_type</span> <span class="ow">in</span> <span class="n">EXISTING_SERIALIZERS</span><span class="p">:</span>
</span><span id="L-932"><a href="#L-932"><span class="linenos"> 932</span></a>        <span class="n">serializer_features</span> <span class="o">=</span> <span class="n">SERIALIZERS_DESCRIPTION</span><span class="p">[</span><span class="n">serializer_type</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-933"><a href="#L-933"><span class="linenos"> 933</span></a>        <span class="k">if</span> <span class="n">desired_features</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">serializer_features</span><span class="p">):</span>
</span><span id="L-934"><a href="#L-934"><span class="linenos"> 934</span></a>            <span class="n">appropriate_serializers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="L-935"><a href="#L-935"><span class="linenos"> 935</span></a>    <span class="k">return</span> <span class="n">appropriate_serializers</span>
</span><span id="L-936"><a href="#L-936"><span class="linenos"> 936</span></a>
</span><span id="L-937"><a href="#L-937"><span class="linenos"> 937</span></a>
</span><span id="L-938"><a href="#L-938"><span class="linenos"> 938</span></a><span class="n">SerializerPerformance</span> <span class="o">=</span> <span class="nb">float</span>
</span><span id="L-939"><a href="#L-939"><span class="linenos"> 939</span></a><span class="n">SerializerFootprint</span> <span class="o">=</span> <span class="nb">int</span>
</span><span id="L-940"><a href="#L-940"><span class="linenos"> 940</span></a>
</span><span id="L-941"><a href="#L-941"><span class="linenos"> 941</span></a>
</span><span id="L-942"><a href="#L-942"><span class="linenos"> 942</span></a><span class="k">def</span> <span class="nf">serializer_benchmark</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">:</span> <span class="n">Serializers</span><span class="p">,</span> <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="L-943"><a href="#L-943"><span class="linenos"> 943</span></a>                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">SerializerPerformance</span><span class="p">,</span> <span class="n">SerializerFootprint</span><span class="p">]:</span>
</span><span id="L-944"><a href="#L-944"><span class="linenos"> 944</span></a>    <span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="L-945"><a href="#L-945"><span class="linenos"> 945</span></a>    <span class="n">measurements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-946"><a href="#L-946"><span class="linenos"> 946</span></a>    <span class="n">tr</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">test_time</span><span class="p">)</span>
</span><span id="L-947"><a href="#L-947"><span class="linenos"> 947</span></a>    <span class="k">while</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-948"><a href="#L-948"><span class="linenos"> 948</span></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="L-949"><a href="#L-949"><span class="linenos"> 949</span></a>        <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">test_data</span><span class="p">))</span>
</span><span id="L-950"><a href="#L-950"><span class="linenos"> 950</span></a>        <span class="n">measurements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span>
</span><span id="L-951"><a href="#L-951"><span class="linenos"> 951</span></a>
</span><span id="L-952"><a href="#L-952"><span class="linenos"> 952</span></a>    <span class="n">best_measurement</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">measurements</span><span class="p">)</span>
</span><span id="L-953"><a href="#L-953"><span class="linenos"> 953</span></a>    <span class="n">best_performance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">/</span> <span class="n">best_measurement</span><span class="p">)</span> <span class="k">if</span> <span class="n">best_measurement</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-954"><a href="#L-954"><span class="linenos"> 954</span></a>    <span class="n">data_dump</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">test_data</span><span class="p">)</span>
</span><span id="L-955"><a href="#L-955"><span class="linenos"> 955</span></a>    <span class="k">return</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter_per_time_unit</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">data_dump</span><span class="p">)</span>
</span><span id="L-956"><a href="#L-956"><span class="linenos"> 956</span></a>
</span><span id="L-957"><a href="#L-957"><span class="linenos"> 957</span></a>
</span><span id="L-958"><a href="#L-958"><span class="linenos"> 958</span></a><span class="k">def</span> <span class="nf">get_most_efficient_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">,</span>
</span><span id="L-959"><a href="#L-959"><span class="linenos"> 959</span></a>                                   <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
</span><span id="L-960"><a href="#L-960"><span class="linenos"> 960</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="L-961"><a href="#L-961"><span class="linenos"> 961</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">Serializers</span><span class="p">],</span>
</span><span id="L-962"><a href="#L-962"><span class="linenos"> 962</span></a>                                              <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Serializers</span><span class="p">,</span> <span class="n">SerializerPerformance</span><span class="p">,</span> <span class="n">SerializerFootprint</span><span class="p">]]]:</span>
</span><span id="L-963"><a href="#L-963"><span class="linenos"> 963</span></a>    <span class="c1"># TODO: сделать класс, который бы подбирал количество итераций под нужное время выдержки в секундах (float)</span>
</span><span id="L-964"><a href="#L-964"><span class="linenos"> 964</span></a>    <span class="c1"># это необходимо для того чтобы правильно протестировать производительность под PyPy</span>
</span><span id="L-965"><a href="#L-965"><span class="linenos"> 965</span></a>    <span class="c1"># в дальнейшем этот функционал стоит перенести в модуль performance_test_lib</span>
</span><span id="L-966"><a href="#L-966"><span class="linenos"> 966</span></a>    <span class="c1"># TODO: make some caching algorithm. Lru can not be used since it requires all function parameters be hashable and both desired_features and test_data are not</span>
</span><span id="L-967"><a href="#L-967"><span class="linenos"> 967</span></a>
</span><span id="L-968"><a href="#L-968"><span class="linenos"> 968</span></a>    <span class="n">appropriate_serializers</span> <span class="o">=</span> <span class="n">get_an_appropriate_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">)</span>
</span><span id="L-969"><a href="#L-969"><span class="linenos"> 969</span></a>
</span><span id="L-970"><a href="#L-970"><span class="linenos"> 970</span></a>    <span class="n">benchmark_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[float, Set[Serializers]]</span>
</span><span id="L-971"><a href="#L-971"><span class="linenos"> 971</span></a>    <span class="n">serializers_data</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>  <span class="c1"># type: Set[Tuple[Serializers, SerializerPerformance, SerializerFootprint]]</span>
</span><span id="L-972"><a href="#L-972"><span class="linenos"> 972</span></a>    <span class="k">for</span> <span class="n">serializer_type</span> <span class="ow">in</span> <span class="n">appropriate_serializers</span><span class="p">:</span>
</span><span id="L-973"><a href="#L-973"><span class="linenos"> 973</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="L-974"><a href="#L-974"><span class="linenos"> 974</span></a>            <span class="n">performance</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="n">dump_size</span> <span class="o">=</span> <span class="n">serializer_benchmark</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">,</span> <span class="n">test_data</span><span class="p">,</span> <span class="n">test_time</span><span class="p">)</span>
</span><span id="L-975"><a href="#L-975"><span class="linenos"> 975</span></a>        
</span><span id="L-976"><a href="#L-976"><span class="linenos"> 976</span></a>        <span class="k">if</span> <span class="n">best_performance</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">benchmark_results</span><span class="p">:</span>
</span><span id="L-977"><a href="#L-977"><span class="linenos"> 977</span></a>            <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-978"><a href="#L-978"><span class="linenos"> 978</span></a>        
</span><span id="L-979"><a href="#L-979"><span class="linenos"> 979</span></a>        <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="L-980"><a href="#L-980"><span class="linenos"> 980</span></a>        <span class="n">serializers_data</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">serializer_type</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="n">dump_size</span><span class="p">))</span>
</span><span id="L-981"><a href="#L-981"><span class="linenos"> 981</span></a>    
</span><span id="L-982"><a href="#L-982"><span class="linenos"> 982</span></a>    <span class="n">best_performance</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">benchmark_results</span><span class="p">)</span>
</span><span id="L-983"><a href="#L-983"><span class="linenos"> 983</span></a>    <span class="n">best_serializers</span> <span class="o">=</span> <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span>
</span><span id="L-984"><a href="#L-984"><span class="linenos"> 984</span></a>    <span class="k">return</span> <span class="n">best_serializers</span><span class="p">,</span> <span class="n">serializers_data</span>
</span><span id="L-985"><a href="#L-985"><span class="linenos"> 985</span></a>
</span><span id="L-986"><a href="#L-986"><span class="linenos"> 986</span></a>
</span><span id="L-987"><a href="#L-987"><span class="linenos"> 987</span></a><span class="k">def</span> <span class="nf">best_serializer</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">,</span>
</span><span id="L-988"><a href="#L-988"><span class="linenos"> 988</span></a>                                   <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
</span><span id="L-989"><a href="#L-989"><span class="linenos"> 989</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="L-990"><a href="#L-990"><span class="linenos"> 990</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Serializer</span><span class="p">:</span>
</span><span id="L-991"><a href="#L-991"><span class="linenos"> 991</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_most_efficient_serializers</span><span class="p">(</span>
</span><span id="L-992"><a href="#L-992"><span class="linenos"> 992</span></a>        <span class="n">desired_features</span><span class="p">,</span>
</span><span id="L-993"><a href="#L-993"><span class="linenos"> 993</span></a>        <span class="n">test_data</span><span class="p">,</span>
</span><span id="L-994"><a href="#L-994"><span class="linenos"> 994</span></a>        <span class="n">test_time</span><span class="p">)</span>
</span><span id="L-995"><a href="#L-995"><span class="linenos"> 995</span></a>    <span class="n">best_serializers</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-996"><a href="#L-996"><span class="linenos"> 996</span></a>    <span class="k">return</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">best_serializers</span><span class="o">.</span><span class="n">pop</span><span class="p">())</span>
</span><span id="L-997"><a href="#L-997"><span class="linenos"> 997</span></a>
</span><span id="L-998"><a href="#L-998"><span class="linenos"> 998</span></a>
</span><span id="L-999"><a href="#L-999"><span class="linenos"> 999</span></a><span class="k">class</span> <span class="nc">TestDataType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-1000"><a href="#L-1000"><span class="linenos">1000</span></a>    <span class="n">small</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-1001"><a href="#L-1001"><span class="linenos">1001</span></a>    <span class="n">deep_small</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-1002"><a href="#L-1002"><span class="linenos">1002</span></a>    <span class="n">large</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-1003"><a href="#L-1003"><span class="linenos">1003</span></a>    <span class="n">deep_large</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-1004"><a href="#L-1004"><span class="linenos">1004</span></a>
</span><span id="L-1005"><a href="#L-1005"><span class="linenos">1005</span></a>
</span><span id="L-1006"><a href="#L-1006"><span class="linenos">1006</span></a><span class="k">def</span> <span class="nf">test_data_factory</span><span class="p">(</span><span class="n">test_data_type</span><span class="p">:</span> <span class="n">TestDataType</span><span class="p">):</span>
</span><span id="L-1007"><a href="#L-1007"><span class="linenos">1007</span></a>    <span class="k">if</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">small</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="L-1008"><a href="#L-1008"><span class="linenos">1008</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-1009"><a href="#L-1009"><span class="linenos">1009</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="p">,</span>
</span><span id="L-1010"><a href="#L-1010"><span class="linenos">1010</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-1011"><a href="#L-1011"><span class="linenos">1011</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="L-1012"><a href="#L-1012"><span class="linenos">1012</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="L-1013"><a href="#L-1013"><span class="linenos">1013</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="L-1014"><a href="#L-1014"><span class="linenos">1014</span></a>                <span class="p">{</span>
</span><span id="L-1015"><a href="#L-1015"><span class="linenos">1015</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="L-1016"><a href="#L-1016"><span class="linenos">1016</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">2</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1017"><a href="#L-1017"><span class="linenos">1017</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="L-1018"><a href="#L-1018"><span class="linenos">1018</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1019"><a href="#L-1019"><span class="linenos">1019</span></a>                            <span class="s1">&#39;world&#39;</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="L-1020"><a href="#L-1020"><span class="linenos">1020</span></a>                        <span class="p">}</span>
</span><span id="L-1021"><a href="#L-1021"><span class="linenos">1021</span></a>                    <span class="p">}</span>
</span><span id="L-1022"><a href="#L-1022"><span class="linenos">1022</span></a>                <span class="p">}</span>
</span><span id="L-1023"><a href="#L-1023"><span class="linenos">1023</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="L-1024"><a href="#L-1024"><span class="linenos">1024</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span>
</span><span id="L-1025"><a href="#L-1025"><span class="linenos">1025</span></a>        <span class="p">}</span>
</span><span id="L-1026"><a href="#L-1026"><span class="linenos">1026</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_small</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="L-1027"><a href="#L-1027"><span class="linenos">1027</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-1028"><a href="#L-1028"><span class="linenos">1028</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="p">,</span>
</span><span id="L-1029"><a href="#L-1029"><span class="linenos">1029</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-1030"><a href="#L-1030"><span class="linenos">1030</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="L-1031"><a href="#L-1031"><span class="linenos">1031</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="L-1032"><a href="#L-1032"><span class="linenos">1032</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="L-1033"><a href="#L-1033"><span class="linenos">1033</span></a>                <span class="p">{</span>
</span><span id="L-1034"><a href="#L-1034"><span class="linenos">1034</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="L-1035"><a href="#L-1035"><span class="linenos">1035</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">2</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1036"><a href="#L-1036"><span class="linenos">1036</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">1000</span><span class="p">,</span>
</span><span id="L-1037"><a href="#L-1037"><span class="linenos">1037</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1038"><a href="#L-1038"><span class="linenos">1038</span></a>                            <span class="s1">&#39;world&#39;</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="L-1039"><a href="#L-1039"><span class="linenos">1039</span></a>                        <span class="p">}</span>
</span><span id="L-1040"><a href="#L-1040"><span class="linenos">1040</span></a>                    <span class="p">}</span>
</span><span id="L-1041"><a href="#L-1041"><span class="linenos">1041</span></a>                <span class="p">}</span>
</span><span id="L-1042"><a href="#L-1042"><span class="linenos">1042</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">20</span><span class="p">,</span>
</span><span id="L-1043"><a href="#L-1043"><span class="linenos">1043</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span>
</span><span id="L-1044"><a href="#L-1044"><span class="linenos">1044</span></a>        <span class="p">}</span>
</span><span id="L-1045"><a href="#L-1045"><span class="linenos">1045</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">large</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="L-1046"><a href="#L-1046"><span class="linenos">1046</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-1047"><a href="#L-1047"><span class="linenos">1047</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span>
</span><span id="L-1048"><a href="#L-1048"><span class="linenos">1048</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-1049"><a href="#L-1049"><span class="linenos">1049</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="L-1050"><a href="#L-1050"><span class="linenos">1050</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="L-1051"><a href="#L-1051"><span class="linenos">1051</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="L-1052"><a href="#L-1052"><span class="linenos">1052</span></a>                <span class="p">{</span>
</span><span id="L-1053"><a href="#L-1053"><span class="linenos">1053</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="L-1054"><a href="#L-1054"><span class="linenos">1054</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1055"><a href="#L-1055"><span class="linenos">1055</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="L-1056"><a href="#L-1056"><span class="linenos">1056</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1057"><a href="#L-1057"><span class="linenos">1057</span></a>                            <span class="s1">&#39;world&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="L-1058"><a href="#L-1058"><span class="linenos">1058</span></a>                        <span class="p">}</span>
</span><span id="L-1059"><a href="#L-1059"><span class="linenos">1059</span></a>                    <span class="p">}</span>
</span><span id="L-1060"><a href="#L-1060"><span class="linenos">1060</span></a>                <span class="p">}</span>
</span><span id="L-1061"><a href="#L-1061"><span class="linenos">1061</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="L-1062"><a href="#L-1062"><span class="linenos">1062</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span><span class="o">*</span><span class="mi">100</span>
</span><span id="L-1063"><a href="#L-1063"><span class="linenos">1063</span></a>        <span class="p">}</span>
</span><span id="L-1064"><a href="#L-1064"><span class="linenos">1064</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_large</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="L-1065"><a href="#L-1065"><span class="linenos">1065</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-1066"><a href="#L-1066"><span class="linenos">1066</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span>
</span><span id="L-1067"><a href="#L-1067"><span class="linenos">1067</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-1068"><a href="#L-1068"><span class="linenos">1068</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="L-1069"><a href="#L-1069"><span class="linenos">1069</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="L-1070"><a href="#L-1070"><span class="linenos">1070</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="L-1071"><a href="#L-1071"><span class="linenos">1071</span></a>                <span class="p">{</span>
</span><span id="L-1072"><a href="#L-1072"><span class="linenos">1072</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="L-1073"><a href="#L-1073"><span class="linenos">1073</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1074"><a href="#L-1074"><span class="linenos">1074</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">1000</span><span class="p">,</span>
</span><span id="L-1075"><a href="#L-1075"><span class="linenos">1075</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="L-1076"><a href="#L-1076"><span class="linenos">1076</span></a>                            <span class="s1">&#39;world&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="L-1077"><a href="#L-1077"><span class="linenos">1077</span></a>                        <span class="p">}</span>
</span><span id="L-1078"><a href="#L-1078"><span class="linenos">1078</span></a>                    <span class="p">}</span>
</span><span id="L-1079"><a href="#L-1079"><span class="linenos">1079</span></a>                <span class="p">}</span>
</span><span id="L-1080"><a href="#L-1080"><span class="linenos">1080</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">20</span><span class="p">,</span>
</span><span id="L-1081"><a href="#L-1081"><span class="linenos">1081</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span><span class="o">*</span><span class="mi">100</span>
</span><span id="L-1082"><a href="#L-1082"><span class="linenos">1082</span></a>        <span class="p">}</span>
</span><span id="L-1083"><a href="#L-1083"><span class="linenos">1083</span></a>
</span><span id="L-1084"><a href="#L-1084"><span class="linenos">1084</span></a>
</span><span id="L-1085"><a href="#L-1085"><span class="linenos">1085</span></a><span class="nd">@lru_cache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
</span><span id="L-1086"><a href="#L-1086"><span class="linenos">1086</span></a><span class="k">def</span> <span class="nf">best_serializer_for_standard_data</span><span class="p">(</span><span class="n">desired_features_tuple</span><span class="p">:</span> <span class="n">SerializerFeaturesTuple</span><span class="p">,</span>
</span><span id="L-1087"><a href="#L-1087"><span class="linenos">1087</span></a>                                   <span class="n">test_data_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TestDataType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-1088"><a href="#L-1088"><span class="linenos">1088</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="L-1089"><a href="#L-1089"><span class="linenos">1089</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Serializer</span><span class="p">:</span>
</span><span id="L-1090"><a href="#L-1090"><span class="linenos">1090</span></a>    <span class="n">test_data_type</span> <span class="o">=</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">small</span> <span class="k">if</span> <span class="n">test_data_type</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">test_data_type</span>
</span><span id="L-1091"><a href="#L-1091"><span class="linenos">1091</span></a>    <span class="k">return</span> <span class="n">best_serializer</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">desired_features_tuple</span><span class="p">),</span> <span class="n">test_data_factory</span><span class="p">(</span><span class="n">test_data_type</span><span class="p">),</span> <span class="n">test_time</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="Tags">
                            <input id="Tags-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Tags</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="Tags-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Tags"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Tags-45"><a href="#Tags-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">Tags</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="Tags-46"><a href="#Tags-46"><span class="linenos">46</span></a>    <span class="n">tested</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Tags-47"><a href="#Tags-47"><span class="linenos">47</span></a>    <span class="n">deep</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># can work with nested data structures</span>
</span><span id="Tags-48"><a href="#Tags-48"><span class="linenos">48</span></a>    <span class="n">superficial</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># can work with only single-layer of data</span>
</span><span id="Tags-49"><a href="#Tags-49"><span class="linenos">49</span></a>    <span class="n">multi_platform</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># serialized data can be deserialized by other languages/interpreters</span>
</span><span id="Tags-50"><a href="#Tags-50"><span class="linenos">50</span></a>    <span class="n">current_platform</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># serialized data can be deserialized by current type of python interpreter (only by CPython or only by PyPy for example)</span>
</span><span id="Tags-51"><a href="#Tags-51"><span class="linenos">51</span></a>    <span class="n">multicast</span> <span class="o">=</span> <span class="mi">5</span>  <span class="c1"># ?</span>
</span><span id="Tags-52"><a href="#Tags-52"><span class="linenos">52</span></a>    <span class="n">unique</span> <span class="o">=</span> <span class="mi">6</span>  <span class="c1"># ?</span>
</span><span id="Tags-53"><a href="#Tags-53"><span class="linenos">53</span></a>    <span class="n">can_use_set</span> <span class="o">=</span> <span class="mi">7</span>  <span class="c1"># can serialize set type</span>
</span><span id="Tags-54"><a href="#Tags-54"><span class="linenos">54</span></a>    <span class="n">can_use_bytes</span> <span class="o">=</span> <span class="mi">8</span>  <span class="c1"># can serialize bytes type</span>
</span><span id="Tags-55"><a href="#Tags-55"><span class="linenos">55</span></a>    <span class="n">can_use_custom_types</span> <span class="o">=</span> <span class="mi">9</span>  <span class="c1"># can serialize custom types</span>
</span><span id="Tags-56"><a href="#Tags-56"><span class="linenos">56</span></a>    <span class="n">can_use_lambda_functions</span> <span class="o">=</span> <span class="mi">10</span>
</span><span id="Tags-57"><a href="#Tags-57"><span class="linenos">57</span></a>    <span class="n">decode_str_as_str</span> <span class="o">=</span> <span class="mi">11</span>  <span class="c1"># does not convert strings to bytes</span>
</span><span id="Tags-58"><a href="#Tags-58"><span class="linenos">58</span></a>    <span class="n">decode_bytes_as_bytes</span> <span class="o">=</span> <span class="mi">12</span>  <span class="c1"># does not convert bytes to strings</span>
</span><span id="Tags-59"><a href="#Tags-59"><span class="linenos">59</span></a>    <span class="n">decode_str_and_bytes_as_requested</span> <span class="o">=</span> <span class="mi">13</span>  <span class="c1"># can chose: convert all str/bytes to str or to convert all str/bytes to bytes.</span>
</span><span id="Tags-60"><a href="#Tags-60"><span class="linenos">60</span></a>    <span class="n">decode_list_and_tuple_as_requested</span> <span class="o">=</span> <span class="mi">14</span>  <span class="c1"># can chose: convert all list/tuple to list or to convert all list/tuple to tuple.</span>
</span><span id="Tags-61"><a href="#Tags-61"><span class="linenos">61</span></a>    <span class="n">decode_tuple_as_tuple</span> <span class="o">=</span> <span class="mi">15</span>  <span class="c1"># does not conver tuples to list/set</span>
</span><span id="Tags-62"><a href="#Tags-62"><span class="linenos">62</span></a>    <span class="n">decode_list_as_list</span> <span class="o">=</span> <span class="mi">16</span>  <span class="c1"># does not convert lists to tuple/set</span>
</span><span id="Tags-63"><a href="#Tags-63"><span class="linenos">63</span></a>    <span class="n">explicit_format_version</span> <span class="o">=</span> <span class="mi">17</span>  <span class="c1"># Example: pickle can be of a different versions since python-version depent so it is Not tagged as an explicit_format_version.</span>
</span><span id="Tags-64"><a href="#Tags-64"><span class="linenos">64</span></a>    <span class="n">fast</span> <span class="o">=</span> <span class="mi">17</span>
</span><span id="Tags-65"><a href="#Tags-65"><span class="linenos">65</span></a>    <span class="n">compat</span> <span class="o">=</span> <span class="mi">18</span>
</span><span id="Tags-66"><a href="#Tags-66"><span class="linenos">66</span></a>    <span class="n">compat_with_python_below_3_8</span> <span class="o">=</span> <span class="mi">19</span>
</span><span id="Tags-67"><a href="#Tags-67"><span class="linenos">67</span></a>    <span class="n">compat_with_python_abowe_3_8</span> <span class="o">=</span> <span class="mi">20</span>
</span><span id="Tags-68"><a href="#Tags-68"><span class="linenos">68</span></a>    <span class="n">decode_set_as_set</span> <span class="o">=</span> <span class="mi">21</span>  <span class="c1"># does not convert sets to tuple/list</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="Tags.tested" class="classattr">
                                <div class="attr variable">
            <span class="name">tested</span>        =
<span class="default_value">&lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.tested"></a>
    
    

                            </div>
                            <div id="Tags.deep" class="classattr">
                                <div class="attr variable">
            <span class="name">deep</span>        =
<span class="default_value">&lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.deep"></a>
    
    

                            </div>
                            <div id="Tags.superficial" class="classattr">
                                <div class="attr variable">
            <span class="name">superficial</span>        =
<span class="default_value">&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.superficial"></a>
    
    

                            </div>
                            <div id="Tags.multi_platform" class="classattr">
                                <div class="attr variable">
            <span class="name">multi_platform</span>        =
<span class="default_value">&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.multi_platform"></a>
    
    

                            </div>
                            <div id="Tags.current_platform" class="classattr">
                                <div class="attr variable">
            <span class="name">current_platform</span>        =
<span class="default_value">&lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.current_platform"></a>
    
    

                            </div>
                            <div id="Tags.multicast" class="classattr">
                                <div class="attr variable">
            <span class="name">multicast</span>        =
<span class="default_value">&lt;<a href="#Tags.multicast">Tags.multicast</a>: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.multicast"></a>
    
    

                            </div>
                            <div id="Tags.unique" class="classattr">
                                <div class="attr variable">
            <span class="name">unique</span>        =
<span class="default_value">&lt;<a href="#Tags.unique">Tags.unique</a>: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.unique"></a>
    
    

                            </div>
                            <div id="Tags.can_use_set" class="classattr">
                                <div class="attr variable">
            <span class="name">can_use_set</span>        =
<span class="default_value">&lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.can_use_set"></a>
    
    

                            </div>
                            <div id="Tags.can_use_bytes" class="classattr">
                                <div class="attr variable">
            <span class="name">can_use_bytes</span>        =
<span class="default_value">&lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.can_use_bytes"></a>
    
    

                            </div>
                            <div id="Tags.can_use_custom_types" class="classattr">
                                <div class="attr variable">
            <span class="name">can_use_custom_types</span>        =
<span class="default_value">&lt;<a href="#Tags.can_use_custom_types">Tags.can_use_custom_types</a>: 9&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.can_use_custom_types"></a>
    
    

                            </div>
                            <div id="Tags.can_use_lambda_functions" class="classattr">
                                <div class="attr variable">
            <span class="name">can_use_lambda_functions</span>        =
<span class="default_value">&lt;<a href="#Tags.can_use_lambda_functions">Tags.can_use_lambda_functions</a>: 10&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.can_use_lambda_functions"></a>
    
    

                            </div>
                            <div id="Tags.decode_str_as_str" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_str_as_str</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_str_as_str"></a>
    
    

                            </div>
                            <div id="Tags.decode_bytes_as_bytes" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_bytes_as_bytes</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_bytes_as_bytes"></a>
    
    

                            </div>
                            <div id="Tags.decode_str_and_bytes_as_requested" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_str_and_bytes_as_requested</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_str_and_bytes_as_requested">Tags.decode_str_and_bytes_as_requested</a>: 13&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_str_and_bytes_as_requested"></a>
    
    

                            </div>
                            <div id="Tags.decode_list_and_tuple_as_requested" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_list_and_tuple_as_requested</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_list_and_tuple_as_requested">Tags.decode_list_and_tuple_as_requested</a>: 14&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_list_and_tuple_as_requested"></a>
    
    

                            </div>
                            <div id="Tags.decode_tuple_as_tuple" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_tuple_as_tuple</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_tuple_as_tuple"></a>
    
    

                            </div>
                            <div id="Tags.decode_list_as_list" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_list_as_list</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_list_as_list"></a>
    
    

                            </div>
                            <div id="Tags.explicit_format_version" class="classattr">
                                <div class="attr variable">
            <span class="name">explicit_format_version</span>        =
<span class="default_value">&lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.explicit_format_version"></a>
    
    

                            </div>
                            <div id="Tags.fast" class="classattr">
                                <div class="attr variable">
            <span class="name">fast</span>        =
<span class="default_value">&lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.fast"></a>
    
    

                            </div>
                            <div id="Tags.compat" class="classattr">
                                <div class="attr variable">
            <span class="name">compat</span>        =
<span class="default_value">&lt;<a href="#Tags.compat">Tags.compat</a>: 18&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.compat"></a>
    
    

                            </div>
                            <div id="Tags.compat_with_python_below_3_8" class="classattr">
                                <div class="attr variable">
            <span class="name">compat_with_python_below_3_8</span>        =
<span class="default_value">&lt;<a href="#Tags.compat_with_python_below_3_8">Tags.compat_with_python_below_3_8</a>: 19&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.compat_with_python_below_3_8"></a>
    
    

                            </div>
                            <div id="Tags.compat_with_python_abowe_3_8" class="classattr">
                                <div class="attr variable">
            <span class="name">compat_with_python_abowe_3_8</span>        =
<span class="default_value">&lt;<a href="#Tags.compat_with_python_abowe_3_8">Tags.compat_with_python_abowe_3_8</a>: 20&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.compat_with_python_abowe_3_8"></a>
    
    

                            </div>
                            <div id="Tags.decode_set_as_set" class="classattr">
                                <div class="attr variable">
            <span class="name">decode_set_as_set</span>        =
<span class="default_value">&lt;<a href="#Tags.decode_set_as_set">Tags.decode_set_as_set</a>: 21&gt;</span>

        
    </div>
    <a class="headerlink" href="#Tags.decode_set_as_set"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Tags.name" class="variable">name</dd>
                <dd id="Tags.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="DataFormats">
                            <input id="DataFormats-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">DataFormats</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="DataFormats-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#DataFormats"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="DataFormats-71"><a href="#DataFormats-71"><span class="linenos">71</span></a><span class="k">class</span> <span class="nc">DataFormats</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="DataFormats-72"><a href="#DataFormats-72"><span class="linenos">72</span></a>    <span class="nb">any</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># we don&#39;t care about the serialized data format</span>
</span><span id="DataFormats-73"><a href="#DataFormats-73"><span class="linenos">73</span></a>    <span class="n">json</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># serialized data is json</span>
</span><span id="DataFormats-74"><a href="#DataFormats-74"><span class="linenos">74</span></a>    <span class="n">binary</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># serialized data is binary (not really human-readable)</span>
</span><span id="DataFormats-75"><a href="#DataFormats-75"><span class="linenos">75</span></a>    <span class="n">text</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># serialized data is human-readable</span>
</span><span id="DataFormats-76"><a href="#DataFormats-76"><span class="linenos">76</span></a>    <span class="n">yaml</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="DataFormats-77"><a href="#DataFormats-77"><span class="linenos">77</span></a>    <span class="n">toml</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="DataFormats-78"><a href="#DataFormats-78"><span class="linenos">78</span></a>    <span class="n">messagepack</span> <span class="o">=</span> <span class="mi">6</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="DataFormats.any" class="classattr">
                                <div class="attr variable">
            <span class="name">any</span>        =
<span class="default_value">&lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.any"></a>
    
    

                            </div>
                            <div id="DataFormats.json" class="classattr">
                                <div class="attr variable">
            <span class="name">json</span>        =
<span class="default_value">&lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.json"></a>
    
    

                            </div>
                            <div id="DataFormats.binary" class="classattr">
                                <div class="attr variable">
            <span class="name">binary</span>        =
<span class="default_value">&lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.binary"></a>
    
    

                            </div>
                            <div id="DataFormats.text" class="classattr">
                                <div class="attr variable">
            <span class="name">text</span>        =
<span class="default_value">&lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.text"></a>
    
    

                            </div>
                            <div id="DataFormats.yaml" class="classattr">
                                <div class="attr variable">
            <span class="name">yaml</span>        =
<span class="default_value">&lt;<a href="#DataFormats.yaml">DataFormats.yaml</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.yaml"></a>
    
    

                            </div>
                            <div id="DataFormats.toml" class="classattr">
                                <div class="attr variable">
            <span class="name">toml</span>        =
<span class="default_value">&lt;<a href="#DataFormats.toml">DataFormats.toml</a>: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.toml"></a>
    
    

                            </div>
                            <div id="DataFormats.messagepack" class="classattr">
                                <div class="attr variable">
            <span class="name">messagepack</span>        =
<span class="default_value">&lt;<a href="#DataFormats.messagepack">DataFormats.messagepack</a>: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#DataFormats.messagepack"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="DataFormats.name" class="variable">name</dd>
                <dd id="DataFormats.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="SerializerFeatures">
                    <div class="attr variable">
            <span class="name">SerializerFeatures</span>        =
<input id="SerializerFeatures-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="SerializerFeatures-view-value"></label><span class="default_value">typing.Set[typing.Union[<a href="#Tags">Tags</a>, <a href="#DataFormats">DataFormats</a>]]</span>

        
    </div>
    <a class="headerlink" href="#SerializerFeatures"></a>
    
    

                </section>
                <section id="SerializerFeaturesTuple">
                    <div class="attr variable">
            <span class="name">SerializerFeaturesTuple</span>        =
<input id="SerializerFeaturesTuple-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="SerializerFeaturesTuple-view-value"></label><span class="default_value">typing.Tuple[typing.Union[<a href="#Tags">Tags</a>, <a href="#DataFormats">DataFormats</a>]]</span>

        
    </div>
    <a class="headerlink" href="#SerializerFeaturesTuple"></a>
    
    

                </section>
                <section id="Serializers">
                            <input id="Serializers-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Serializers</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="Serializers-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Serializers"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Serializers-86"><a href="#Serializers-86"><span class="linenos"> 86</span></a><span class="k">class</span> <span class="nc">Serializers</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="Serializers-87"><a href="#Serializers-87"><span class="linenos"> 87</span></a>    <span class="n">json</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="Serializers-88"><a href="#Serializers-88"><span class="linenos"> 88</span></a>    <span class="n">simplejson</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Serializers-89"><a href="#Serializers-89"><span class="linenos"> 89</span></a>    <span class="n">ujson</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="Serializers-90"><a href="#Serializers-90"><span class="linenos"> 90</span></a>    <span class="n">orjson</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="Serializers-91"><a href="#Serializers-91"><span class="linenos"> 91</span></a>    <span class="n">tnetstring</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="Serializers-92"><a href="#Serializers-92"><span class="linenos"> 92</span></a>    <span class="n">pynetstring</span> <span class="o">=</span> <span class="mi">5</span>
</span><span id="Serializers-93"><a href="#Serializers-93"><span class="linenos"> 93</span></a>    <span class="n">msgpack_fast</span> <span class="o">=</span> <span class="mi">6</span>
</span><span id="Serializers-94"><a href="#Serializers-94"><span class="linenos"> 94</span></a>    <span class="n">msgpack</span> <span class="o">=</span> <span class="mi">7</span>
</span><span id="Serializers-95"><a href="#Serializers-95"><span class="linenos"> 95</span></a>    <span class="n">cbor</span> <span class="o">=</span> <span class="mi">8</span>
</span><span id="Serializers-96"><a href="#Serializers-96"><span class="linenos"> 96</span></a>    <span class="n">cbor2</span> <span class="o">=</span> <span class="mi">9</span>
</span><span id="Serializers-97"><a href="#Serializers-97"><span class="linenos"> 97</span></a>    <span class="n">marshal</span> <span class="o">=</span> <span class="mi">10</span>
</span><span id="Serializers-98"><a href="#Serializers-98"><span class="linenos"> 98</span></a>    <span class="n">marshal_compat_4</span> <span class="o">=</span> <span class="mi">11</span>
</span><span id="Serializers-99"><a href="#Serializers-99"><span class="linenos"> 99</span></a>    <span class="n">marshal_compat_3</span> <span class="o">=</span> <span class="mi">12</span>
</span><span id="Serializers-100"><a href="#Serializers-100"><span class="linenos">100</span></a>    <span class="n">marshal_compat_2</span> <span class="o">=</span> <span class="mi">13</span>
</span><span id="Serializers-101"><a href="#Serializers-101"><span class="linenos">101</span></a>    <span class="n">marshal_compat_1</span> <span class="o">=</span> <span class="mi">14</span>
</span><span id="Serializers-102"><a href="#Serializers-102"><span class="linenos">102</span></a>    <span class="n">marshal_compat_0</span> <span class="o">=</span> <span class="mi">15</span>
</span><span id="Serializers-103"><a href="#Serializers-103"><span class="linenos">103</span></a>    <span class="n">pickle</span> <span class="o">=</span> <span class="mi">16</span>
</span><span id="Serializers-104"><a href="#Serializers-104"><span class="linenos">104</span></a>    <span class="n">pickle_default</span> <span class="o">=</span> <span class="mi">17</span>
</span><span id="Serializers-105"><a href="#Serializers-105"><span class="linenos">105</span></a>    <span class="n">pickle_compat_5</span> <span class="o">=</span> <span class="mi">18</span>
</span><span id="Serializers-106"><a href="#Serializers-106"><span class="linenos">106</span></a>    <span class="n">pickle_compat_4</span> <span class="o">=</span> <span class="mi">19</span>
</span><span id="Serializers-107"><a href="#Serializers-107"><span class="linenos">107</span></a>    <span class="n">pickle_compat_3</span> <span class="o">=</span> <span class="mi">20</span>
</span><span id="Serializers-108"><a href="#Serializers-108"><span class="linenos">108</span></a>    <span class="n">pickle_compat_2</span> <span class="o">=</span> <span class="mi">21</span>
</span><span id="Serializers-109"><a href="#Serializers-109"><span class="linenos">109</span></a>    <span class="n">pickle_compat_1</span> <span class="o">=</span> <span class="mi">22</span>
</span><span id="Serializers-110"><a href="#Serializers-110"><span class="linenos">110</span></a>    <span class="n">cpickle</span> <span class="o">=</span> <span class="mi">23</span>
</span><span id="Serializers-111"><a href="#Serializers-111"><span class="linenos">111</span></a>    <span class="n">cpickle_default</span> <span class="o">=</span> <span class="mi">24</span>
</span><span id="Serializers-112"><a href="#Serializers-112"><span class="linenos">112</span></a>    <span class="n">cpickle_compat_5</span> <span class="o">=</span> <span class="mi">25</span>
</span><span id="Serializers-113"><a href="#Serializers-113"><span class="linenos">113</span></a>    <span class="n">cpickle_compat_4</span> <span class="o">=</span> <span class="mi">26</span>
</span><span id="Serializers-114"><a href="#Serializers-114"><span class="linenos">114</span></a>    <span class="n">cpickle_compat_3</span> <span class="o">=</span> <span class="mi">27</span>
</span><span id="Serializers-115"><a href="#Serializers-115"><span class="linenos">115</span></a>    <span class="n">cpickle_compat_2</span> <span class="o">=</span> <span class="mi">28</span>
</span><span id="Serializers-116"><a href="#Serializers-116"><span class="linenos">116</span></a>    <span class="n">cpickle_compat_1</span> <span class="o">=</span> <span class="mi">29</span>
</span><span id="Serializers-117"><a href="#Serializers-117"><span class="linenos">117</span></a>    <span class="n">cloudpickle</span> <span class="o">=</span> <span class="mi">30</span>
</span><span id="Serializers-118"><a href="#Serializers-118"><span class="linenos">118</span></a>    <span class="n">cloudpickle_compat_5</span> <span class="o">=</span> <span class="mi">31</span>
</span><span id="Serializers-119"><a href="#Serializers-119"><span class="linenos">119</span></a>    <span class="n">cloudpickle_compat_4</span> <span class="o">=</span> <span class="mi">32</span>
</span><span id="Serializers-120"><a href="#Serializers-120"><span class="linenos">120</span></a>    <span class="n">cloudpickle_compat_3</span> <span class="o">=</span> <span class="mi">33</span>
</span><span id="Serializers-121"><a href="#Serializers-121"><span class="linenos">121</span></a>    <span class="n">cloudpickle_compat_2</span> <span class="o">=</span> <span class="mi">34</span>
</span><span id="Serializers-122"><a href="#Serializers-122"><span class="linenos">122</span></a>    <span class="n">cloudpickle_compat_1</span> <span class="o">=</span> <span class="mi">35</span>
</span><span id="Serializers-123"><a href="#Serializers-123"><span class="linenos">123</span></a>    <span class="n">msgspec_json</span> <span class="o">=</span> <span class="mi">36</span>
</span><span id="Serializers-124"><a href="#Serializers-124"><span class="linenos">124</span></a>    <span class="n">msgspec_messagepack</span> <span class="o">=</span> <span class="mi">37</span>
</span><span id="Serializers-125"><a href="#Serializers-125"><span class="linenos">125</span></a>    <span class="n">msgspec_yaml</span> <span class="o">=</span> <span class="mi">38</span>
</span><span id="Serializers-126"><a href="#Serializers-126"><span class="linenos">126</span></a>    <span class="n">msgspec_toml</span> <span class="o">=</span> <span class="mi">39</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="Serializers.json" class="classattr">
                                <div class="attr variable">
            <span class="name">json</span>        =
<span class="default_value">&lt;<a href="#Serializers.json">Serializers.json</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.json"></a>
    
    

                            </div>
                            <div id="Serializers.simplejson" class="classattr">
                                <div class="attr variable">
            <span class="name">simplejson</span>        =
<span class="default_value">&lt;<a href="#Serializers.simplejson">Serializers.simplejson</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.simplejson"></a>
    
    

                            </div>
                            <div id="Serializers.ujson" class="classattr">
                                <div class="attr variable">
            <span class="name">ujson</span>        =
<span class="default_value">&lt;<a href="#Serializers.ujson">Serializers.ujson</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.ujson"></a>
    
    

                            </div>
                            <div id="Serializers.orjson" class="classattr">
                                <div class="attr variable">
            <span class="name">orjson</span>        =
<span class="default_value">&lt;<a href="#Serializers.orjson">Serializers.orjson</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.orjson"></a>
    
    

                            </div>
                            <div id="Serializers.tnetstring" class="classattr">
                                <div class="attr variable">
            <span class="name">tnetstring</span>        =
<span class="default_value">&lt;<a href="#Serializers.tnetstring">Serializers.tnetstring</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.tnetstring"></a>
    
    

                            </div>
                            <div id="Serializers.pynetstring" class="classattr">
                                <div class="attr variable">
            <span class="name">pynetstring</span>        =
<span class="default_value">&lt;<a href="#Serializers.pynetstring">Serializers.pynetstring</a>: 5&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pynetstring"></a>
    
    

                            </div>
                            <div id="Serializers.msgpack_fast" class="classattr">
                                <div class="attr variable">
            <span class="name">msgpack_fast</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgpack_fast">Serializers.msgpack_fast</a>: 6&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgpack_fast"></a>
    
    

                            </div>
                            <div id="Serializers.msgpack" class="classattr">
                                <div class="attr variable">
            <span class="name">msgpack</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgpack">Serializers.msgpack</a>: 7&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgpack"></a>
    
    

                            </div>
                            <div id="Serializers.cbor" class="classattr">
                                <div class="attr variable">
            <span class="name">cbor</span>        =
<span class="default_value">&lt;<a href="#Serializers.cbor">Serializers.cbor</a>: 8&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cbor"></a>
    
    

                            </div>
                            <div id="Serializers.cbor2" class="classattr">
                                <div class="attr variable">
            <span class="name">cbor2</span>        =
<span class="default_value">&lt;<a href="#Serializers.cbor2">Serializers.cbor2</a>: 9&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cbor2"></a>
    
    

                            </div>
                            <div id="Serializers.marshal" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal">Serializers.marshal</a>: 10&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal"></a>
    
    

                            </div>
                            <div id="Serializers.marshal_compat_4" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal_compat_4</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal_compat_4">Serializers.marshal_compat_4</a>: 11&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal_compat_4"></a>
    
    

                            </div>
                            <div id="Serializers.marshal_compat_3" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal_compat_3</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal_compat_3">Serializers.marshal_compat_3</a>: 12&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal_compat_3"></a>
    
    

                            </div>
                            <div id="Serializers.marshal_compat_2" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal_compat_2</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal_compat_2">Serializers.marshal_compat_2</a>: 13&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal_compat_2"></a>
    
    

                            </div>
                            <div id="Serializers.marshal_compat_1" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal_compat_1</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal_compat_1">Serializers.marshal_compat_1</a>: 14&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal_compat_1"></a>
    
    

                            </div>
                            <div id="Serializers.marshal_compat_0" class="classattr">
                                <div class="attr variable">
            <span class="name">marshal_compat_0</span>        =
<span class="default_value">&lt;<a href="#Serializers.marshal_compat_0">Serializers.marshal_compat_0</a>: 15&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.marshal_compat_0"></a>
    
    

                            </div>
                            <div id="Serializers.pickle" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle">Serializers.pickle</a>: 16&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_default" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_default</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_default">Serializers.pickle_default</a>: 17&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_default"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_compat_5" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_compat_5</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_compat_5">Serializers.pickle_compat_5</a>: 18&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_compat_5"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_compat_4" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_compat_4</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_compat_4">Serializers.pickle_compat_4</a>: 19&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_compat_4"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_compat_3" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_compat_3</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_compat_3">Serializers.pickle_compat_3</a>: 20&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_compat_3"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_compat_2" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_compat_2</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_compat_2">Serializers.pickle_compat_2</a>: 21&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_compat_2"></a>
    
    

                            </div>
                            <div id="Serializers.pickle_compat_1" class="classattr">
                                <div class="attr variable">
            <span class="name">pickle_compat_1</span>        =
<span class="default_value">&lt;<a href="#Serializers.pickle_compat_1">Serializers.pickle_compat_1</a>: 22&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.pickle_compat_1"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle">Serializers.cpickle</a>: 23&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_default" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_default</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_default">Serializers.cpickle_default</a>: 24&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_default"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_compat_5" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_compat_5</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_compat_5">Serializers.cpickle_compat_5</a>: 25&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_compat_5"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_compat_4" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_compat_4</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_compat_4">Serializers.cpickle_compat_4</a>: 26&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_compat_4"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_compat_3" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_compat_3</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_compat_3">Serializers.cpickle_compat_3</a>: 27&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_compat_3"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_compat_2" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_compat_2</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_compat_2">Serializers.cpickle_compat_2</a>: 28&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_compat_2"></a>
    
    

                            </div>
                            <div id="Serializers.cpickle_compat_1" class="classattr">
                                <div class="attr variable">
            <span class="name">cpickle_compat_1</span>        =
<span class="default_value">&lt;<a href="#Serializers.cpickle_compat_1">Serializers.cpickle_compat_1</a>: 29&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cpickle_compat_1"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle">Serializers.cloudpickle</a>: 30&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle_compat_5" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle_compat_5</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle_compat_5">Serializers.cloudpickle_compat_5</a>: 31&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle_compat_5"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle_compat_4" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle_compat_4</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle_compat_4">Serializers.cloudpickle_compat_4</a>: 32&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle_compat_4"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle_compat_3" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle_compat_3</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle_compat_3">Serializers.cloudpickle_compat_3</a>: 33&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle_compat_3"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle_compat_2" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle_compat_2</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle_compat_2">Serializers.cloudpickle_compat_2</a>: 34&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle_compat_2"></a>
    
    

                            </div>
                            <div id="Serializers.cloudpickle_compat_1" class="classattr">
                                <div class="attr variable">
            <span class="name">cloudpickle_compat_1</span>        =
<span class="default_value">&lt;<a href="#Serializers.cloudpickle_compat_1">Serializers.cloudpickle_compat_1</a>: 35&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.cloudpickle_compat_1"></a>
    
    

                            </div>
                            <div id="Serializers.msgspec_json" class="classattr">
                                <div class="attr variable">
            <span class="name">msgspec_json</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgspec_json">Serializers.msgspec_json</a>: 36&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgspec_json"></a>
    
    

                            </div>
                            <div id="Serializers.msgspec_messagepack" class="classattr">
                                <div class="attr variable">
            <span class="name">msgspec_messagepack</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgspec_messagepack">Serializers.msgspec_messagepack</a>: 37&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgspec_messagepack"></a>
    
    

                            </div>
                            <div id="Serializers.msgspec_yaml" class="classattr">
                                <div class="attr variable">
            <span class="name">msgspec_yaml</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgspec_yaml">Serializers.msgspec_yaml</a>: 38&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgspec_yaml"></a>
    
    

                            </div>
                            <div id="Serializers.msgspec_toml" class="classattr">
                                <div class="attr variable">
            <span class="name">msgspec_toml</span>        =
<span class="default_value">&lt;<a href="#Serializers.msgspec_toml">Serializers.msgspec_toml</a>: 39&gt;</span>

        
    </div>
    <a class="headerlink" href="#Serializers.msgspec_toml"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="Serializers.name" class="variable">name</dd>
                <dd id="Serializers.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="none_type">
                    <div class="attr variable">
            <span class="name">none_type</span>        =
<span class="default_value">&lt;class &#39;NoneType&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#none_type"></a>
    
    

                </section>
                <section id="SUPPORTED_TYPES">
                    <div class="attr variable">
            <span class="name">SUPPORTED_TYPES</span>        =
<input id="SUPPORTED_TYPES-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="SUPPORTED_TYPES-view-value"></label><span class="default_value">{&lt;<a href="#Serializers.json">Serializers.json</a>: 0&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.simplejson">Serializers.simplejson</a>: 1&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.ujson">Serializers.ujson</a>: 2&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.orjson">Serializers.orjson</a>: 3&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.tnetstring">Serializers.tnetstring</a>: 4&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.pynetstring">Serializers.pynetstring</a>: 5&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.msgpack">Serializers.msgpack</a>: 7&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;bytes&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.msgpack_fast">Serializers.msgpack_fast</a>: 6&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;bytes&#39;&gt;, &lt;class &#39;tuple&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.cbor">Serializers.cbor</a>: 8&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.cbor2">Serializers.cbor2</a>: 9&gt;: {&lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;datetime.date&#39;&gt;, &lt;class &#39;ipaddress.IPv4Address&#39;&gt;, &lt;class &#39;fractions.Fraction&#39;&gt;, &lt;class &#39;ipaddress.IPv6Network&#39;&gt;, &lt;class &#39;uuid.UUID&#39;&gt;, &lt;class &#39;set&#39;&gt;, &lt;class &#39;bool&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;int&#39;&gt;, &lt;class &#39;decimal.Decimal&#39;&gt;, &lt;class &#39;ipaddress.IPv6Address&#39;&gt;, &lt;class &#39;ipaddress.IPv4Network&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;datetime.datetime&#39;&gt;, &lt;class &#39;re.Pattern&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;email.message.Message&#39;&gt;}, &lt;<a href="#Serializers.marshal">Serializers.marshal</a>: 10&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;complex&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;frozenset&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, Ellipsis, &lt;class &#39;str&#39;&gt;, &lt;class &#39;bytes&#39;&gt;, &lt;class &#39;tuple&#39;&gt;, &lt;class &#39;code&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;set&#39;&gt;, &lt;class &#39;bool&#39;&gt;, &lt;class &#39;bytearray&#39;&gt;, &lt;class &#39;StopIteration&#39;&gt;}, &lt;<a href="#Serializers.pickle">Serializers.pickle</a>: 16&gt;: {}, &lt;<a href="#Serializers.cpickle">Serializers.cpickle</a>: 23&gt;: {}, &lt;<a href="#Serializers.cloudpickle">Serializers.cloudpickle</a>: 30&gt;: {}, &lt;<a href="#Serializers.msgspec_messagepack">Serializers.msgspec_messagepack</a>: 37&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;bytes&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.msgspec_json">Serializers.msgspec_json</a>: 36&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.msgspec_yaml">Serializers.msgspec_yaml</a>: 38&gt;: {&lt;class &#39;int&#39;&gt;, &lt;class &#39;NoneType&#39;&gt;, &lt;class &#39;list&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;datetime.date&#39;&gt;, &lt;class &#39;datetime.datetime&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;float&#39;&gt;, &lt;class &#39;bool&#39;&gt;}, &lt;<a href="#Serializers.msgspec_toml">Serializers.msgspec_toml</a>: 39&gt;: {&lt;class &#39;datetime.date&#39;&gt;, &lt;class &#39;str&#39;&gt;, &lt;class &#39;datetime.datetime&#39;&gt;, &lt;class &#39;dict&#39;&gt;, &lt;class &#39;datetime.time&#39;&gt;}}</span>

        
    </div>
    <a class="headerlink" href="#SUPPORTED_TYPES"></a>
    
    

                </section>
                <section id="SERIALIZERS_DESCRIPTION">
                    <div class="attr variable">
            <span class="name">SERIALIZERS_DESCRIPTION</span>        =
<input id="SERIALIZERS_DESCRIPTION-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="SERIALIZERS_DESCRIPTION-view-value"></label><span class="default_value">{&lt;<a href="#Serializers.json">Serializers.json</a>: 0&gt;: (&#39;json&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;}), &lt;<a href="#Serializers.simplejson">Serializers.simplejson</a>: 1&gt;: (&#39;simplejson&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.ujson">Serializers.ujson</a>: 2&gt;: (&#39;ujson&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.orjson">Serializers.orjson</a>: 3&gt;: (&#39;orjson&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.tnetstring">Serializers.tnetstring</a>: 4&gt;: (&#39;tnetstring&#39;, {&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;}), &lt;<a href="#Serializers.pynetstring">Serializers.pynetstring</a>: 5&gt;: (&#39;pynetstring&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;}), &lt;<a href="#Serializers.msgpack">Serializers.msgpack</a>: 7&gt;: (&#39;msgpack&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#Tags.decode_list_and_tuple_as_requested">Tags.decode_list_and_tuple_as_requested</a>: 14&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.messagepack">DataFormats.messagepack</a>: 6&gt;, &lt;<a href="#Tags.decode_str_and_bytes_as_requested">Tags.decode_str_and_bytes_as_requested</a>: 13&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.msgpack_fast">Serializers.msgpack_fast</a>: 6&gt;: (&#39;msgpack_fast&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#Tags.decode_list_and_tuple_as_requested">Tags.decode_list_and_tuple_as_requested</a>: 14&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#DataFormats.messagepack">DataFormats.messagepack</a>: 6&gt;, &lt;<a href="#Tags.decode_str_and_bytes_as_requested">Tags.decode_str_and_bytes_as_requested</a>: 13&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.cbor">Serializers.cbor</a>: 8&gt;: (&#39;cbor&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.cbor2">Serializers.cbor2</a>: 9&gt;: (&#39;cbor2&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.marshal">Serializers.marshal</a>: 10&gt;: (&#39;marshal&#39;, {&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.pickle">Serializers.pickle</a>: 16&gt;: (&#39;pickle&#39;, {&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;, &lt;<a href="#Tags.can_use_custom_types">Tags.can_use_custom_types</a>: 9&gt;}), &lt;<a href="#Serializers.cpickle">Serializers.cpickle</a>: 23&gt;: (&#39;cPickle&#39;, {&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;, &lt;<a href="#Tags.can_use_custom_types">Tags.can_use_custom_types</a>: 9&gt;}), &lt;<a href="#Serializers.cloudpickle">Serializers.cloudpickle</a>: 30&gt;: (&#39;cloudpickle&#39;, {&lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.can_use_lambda_functions">Tags.can_use_lambda_functions</a>: 10&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.decode_tuple_as_tuple">Tags.decode_tuple_as_tuple</a>: 15&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;, &lt;<a href="#Tags.can_use_custom_types">Tags.can_use_custom_types</a>: 9&gt;}), &lt;<a href="#Serializers.msgspec_messagepack">Serializers.msgspec_messagepack</a>: 37&gt;: (&#39;msgspec_messagepack&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#Tags.decode_bytes_as_bytes">Tags.decode_bytes_as_bytes</a>: 12&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;, &lt;<a href="#DataFormats.binary">DataFormats.binary</a>: 2&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.messagepack">DataFormats.messagepack</a>: 6&gt;, &lt;<a href="#Tags.can_use_bytes">Tags.can_use_bytes</a>: 8&gt;}), &lt;<a href="#Serializers.msgspec_json">Serializers.msgspec_json</a>: 36&gt;: (&#39;msgspec_json&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#DataFormats.json">DataFormats.json</a>: 1&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;}), &lt;<a href="#Serializers.msgspec_yaml">Serializers.msgspec_yaml</a>: 38&gt;: (&#39;msgspec_yaml&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.yaml">DataFormats.yaml</a>: 4&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;}), &lt;<a href="#Serializers.msgspec_toml">Serializers.msgspec_toml</a>: 39&gt;: (&#39;msgspec_toml&#39;, {&lt;<a href="#Tags.multi_platform">Tags.multi_platform</a>: 3&gt;, &lt;<a href="#Tags.superficial">Tags.superficial</a>: 2&gt;, &lt;<a href="#Tags.current_platform">Tags.current_platform</a>: 4&gt;, &lt;<a href="#Tags.deep">Tags.deep</a>: 1&gt;, &lt;<a href="#DataFormats.any">DataFormats.any</a>: 0&gt;, &lt;<a href="#Tags.tested">Tags.tested</a>: 0&gt;, &lt;<a href="#DataFormats.toml">DataFormats.toml</a>: 5&gt;, &lt;<a href="#Tags.explicit_format_version">Tags.explicit_format_version</a>: 17&gt;, &lt;<a href="#Tags.can_use_set">Tags.can_use_set</a>: 7&gt;, &lt;<a href="#Tags.decode_list_as_list">Tags.decode_list_as_list</a>: 16&gt;, &lt;<a href="#DataFormats.text">DataFormats.text</a>: 3&gt;, &lt;<a href="#Tags.decode_str_as_str">Tags.decode_str_as_str</a>: 11&gt;})}</span>

        
    </div>
    <a class="headerlink" href="#SERIALIZERS_DESCRIPTION"></a>
    
    

                </section>
                <section id="ujson_dump_skip_parameters">
                    <div class="attr variable">
            <span class="name">ujson_dump_skip_parameters</span>        =
<span class="default_value">{&#39;allow_nan&#39;, &#39;cls&#39;, &#39;check_circular&#39;, &#39;default&#39;, &#39;separators&#39;, &#39;skipkeys&#39;}</span>

        
    </div>
    <a class="headerlink" href="#ujson_dump_skip_parameters"></a>
    
    

                </section>
                <section id="ujson_dumps_skip_parameters">
                    <div class="attr variable">
            <span class="name">ujson_dumps_skip_parameters</span>        =
<span class="default_value">{&#39;allow_nan&#39;, &#39;cls&#39;, &#39;check_circular&#39;, &#39;default&#39;, &#39;separators&#39;, &#39;skipkeys&#39;}</span>

        
    </div>
    <a class="headerlink" href="#ujson_dumps_skip_parameters"></a>
    
    

                </section>
                <section id="ujson_load_skip_parameters">
                    <div class="attr variable">
            <span class="name">ujson_load_skip_parameters</span>        =
<span class="default_value">{&#39;object_pairs_hook&#39;, &#39;cls&#39;, &#39;object_hook&#39;, &#39;parse_int&#39;, &#39;parse_constant&#39;, &#39;parse_float&#39;}</span>

        
    </div>
    <a class="headerlink" href="#ujson_load_skip_parameters"></a>
    
    

                </section>
                <section id="ujson_loads_skip_parameters">
                    <div class="attr variable">
            <span class="name">ujson_loads_skip_parameters</span>        =
<span class="default_value">{&#39;object_pairs_hook&#39;, &#39;cls&#39;, &#39;object_hook&#39;, &#39;parse_int&#39;, &#39;parse_constant&#39;, &#39;parse_float&#39;}</span>

        
    </div>
    <a class="headerlink" href="#ujson_loads_skip_parameters"></a>
    
    

                </section>
                <section id="orjson_dump_skip_parameters">
                    <div class="attr variable">
            <span class="name">orjson_dump_skip_parameters</span>        =
<span class="default_value">{&#39;allow_nan&#39;, &#39;cls&#39;, &#39;check_circular&#39;, &#39;default&#39;, &#39;separators&#39;, &#39;skipkeys&#39;}</span>

        
    </div>
    <a class="headerlink" href="#orjson_dump_skip_parameters"></a>
    
    

                </section>
                <section id="orjson_dumps_skip_parameters">
                    <div class="attr variable">
            <span class="name">orjson_dumps_skip_parameters</span>        =
<span class="default_value">{&#39;allow_nan&#39;, &#39;cls&#39;, &#39;check_circular&#39;, &#39;default&#39;, &#39;separators&#39;, &#39;skipkeys&#39;}</span>

        
    </div>
    <a class="headerlink" href="#orjson_dumps_skip_parameters"></a>
    
    

                </section>
                <section id="orjson_load_skip_parameters">
                    <div class="attr variable">
            <span class="name">orjson_load_skip_parameters</span>        =
<span class="default_value">{&#39;object_pairs_hook&#39;, &#39;cls&#39;, &#39;object_hook&#39;, &#39;parse_int&#39;, &#39;parse_constant&#39;, &#39;parse_float&#39;}</span>

        
    </div>
    <a class="headerlink" href="#orjson_load_skip_parameters"></a>
    
    

                </section>
                <section id="orjson_loads_skip_parameters">
                    <div class="attr variable">
            <span class="name">orjson_loads_skip_parameters</span>        =
<span class="default_value">{&#39;object_pairs_hook&#39;, &#39;cls&#39;, &#39;object_hook&#39;, &#39;parse_int&#39;, &#39;parse_constant&#39;, &#39;parse_float&#39;}</span>

        
    </div>
    <a class="headerlink" href="#orjson_loads_skip_parameters"></a>
    
    

                </section>
                <section id="EXISTING_SERIALIZERS">
                    <div class="attr variable">
            <span class="name">EXISTING_SERIALIZERS</span>        =
<input id="EXISTING_SERIALIZERS-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="EXISTING_SERIALIZERS-view-value"></label><span class="default_value">{&lt;<a href="#Serializers.cbor">Serializers.cbor</a>: 8&gt;, &lt;<a href="#Serializers.cbor2">Serializers.cbor2</a>: 9&gt;, &lt;<a href="#Serializers.msgpack">Serializers.msgpack</a>: 7&gt;, &lt;<a href="#Serializers.msgspec_toml">Serializers.msgspec_toml</a>: 39&gt;, &lt;<a href="#Serializers.msgpack_fast">Serializers.msgpack_fast</a>: 6&gt;, &lt;<a href="#Serializers.msgspec_messagepack">Serializers.msgspec_messagepack</a>: 37&gt;, &lt;<a href="#Serializers.marshal">Serializers.marshal</a>: 10&gt;, &lt;<a href="#Serializers.cloudpickle">Serializers.cloudpickle</a>: 30&gt;, &lt;<a href="#Serializers.json">Serializers.json</a>: 0&gt;, &lt;<a href="#Serializers.msgspec_yaml">Serializers.msgspec_yaml</a>: 38&gt;, &lt;<a href="#Serializers.simplejson">Serializers.simplejson</a>: 1&gt;, &lt;<a href="#Serializers.ujson">Serializers.ujson</a>: 2&gt;, &lt;<a href="#Serializers.pickle">Serializers.pickle</a>: 16&gt;, &lt;<a href="#Serializers.orjson">Serializers.orjson</a>: 3&gt;, &lt;<a href="#Serializers.msgspec_json">Serializers.msgspec_json</a>: 36&gt;}</span>

        
    </div>
    <a class="headerlink" href="#EXISTING_SERIALIZERS"></a>
    
    

                </section>
                <section id="Serializer">
                            <input id="Serializer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Serializer</span>:

                <label class="view-source-button" for="Serializer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Serializer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Serializer-492"><a href="#Serializer-492"><span class="linenos">492</span></a><span class="k">class</span> <span class="nc">Serializer</span><span class="p">:</span>
</span><span id="Serializer-493"><a href="#Serializer-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serializer</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="n">Serializers</span><span class="p">]):</span>
</span><span id="Serializer-494"><a href="#Serializer-494"><span class="linenos">494</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-495"><a href="#Serializer-495"><span class="linenos">495</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-496"><a href="#Serializer-496"><span class="linenos">496</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-497"><a href="#Serializer-497"><span class="linenos">497</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-498"><a href="#Serializer-498"><span class="linenos">498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-499"><a href="#Serializer-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">serializer</span>
</span><span id="Serializer-500"><a href="#Serializer-500"><span class="linenos">500</span></a>
</span><span id="Serializer-501"><a href="#Serializer-501"><span class="linenos">501</span></a>    <span class="nd">@property</span>
</span><span id="Serializer-502"><a href="#Serializer-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="nf">serializer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Serializer-503"><a href="#Serializer-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span>
</span><span id="Serializer-504"><a href="#Serializer-504"><span class="linenos">504</span></a>
</span><span id="Serializer-505"><a href="#Serializer-505"><span class="linenos">505</span></a>    <span class="nd">@serializer</span><span class="o">.</span><span class="n">setter</span>
</span><span id="Serializer-506"><a href="#Serializer-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">serializer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serializer</span><span class="p">:</span> <span class="n">Serializers</span><span class="p">):</span>
</span><span id="Serializer-507"><a href="#Serializer-507"><span class="linenos">507</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="o">=</span> <span class="n">serializer</span>
</span><span id="Serializer-508"><a href="#Serializer-508"><span class="linenos">508</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Serializer-509"><a href="#Serializer-509"><span class="linenos">509</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-510"><a href="#Serializer-510"><span class="linenos">510</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-511"><a href="#Serializer-511"><span class="linenos">511</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-512"><a href="#Serializer-512"><span class="linenos">512</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer-513"><a href="#Serializer-513"><span class="linenos">513</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Serializer-514"><a href="#Serializer-514"><span class="linenos">514</span></a>            <span class="n">serializer_name</span><span class="p">,</span> <span class="n">serializer_tags</span> <span class="o">=</span> <span class="n">SERIALIZERS_DESCRIPTION</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span><span class="p">]</span>
</span><span id="Serializer-515"><a href="#Serializer-515"><span class="linenos">515</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__dump&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="Serializer-516"><a href="#Serializer-516"><span class="linenos">516</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__dumps&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="Serializer-517"><a href="#Serializer-517"><span class="linenos">517</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__load&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="Serializer-518"><a href="#Serializer-518"><span class="linenos">518</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s1">&#39;_</span><span class="si">{}</span><span class="s1">__loads&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">serializer_name</span><span class="p">))</span>
</span><span id="Serializer-519"><a href="#Serializer-519"><span class="linenos">519</span></a>
</span><span id="Serializer-520"><a href="#Serializer-520"><span class="linenos">520</span></a>    <span class="c1"># json</span>
</span><span id="Serializer-521"><a href="#Serializer-521"><span class="linenos">521</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-522"><a href="#Serializer-522"><span class="linenos">522</span></a>    <span class="k">def</span> <span class="nf">_json__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-523"><a href="#Serializer-523"><span class="linenos">523</span></a>        <span class="n">json</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-524"><a href="#Serializer-524"><span class="linenos">524</span></a>
</span><span id="Serializer-525"><a href="#Serializer-525"><span class="linenos">525</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-526"><a href="#Serializer-526"><span class="linenos">526</span></a>    <span class="k">def</span> <span class="nf">_json__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-527"><a href="#Serializer-527"><span class="linenos">527</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-528"><a href="#Serializer-528"><span class="linenos">528</span></a>
</span><span id="Serializer-529"><a href="#Serializer-529"><span class="linenos">529</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-530"><a href="#Serializer-530"><span class="linenos">530</span></a>    <span class="k">def</span> <span class="nf">_json__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-531"><a href="#Serializer-531"><span class="linenos">531</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-532"><a href="#Serializer-532"><span class="linenos">532</span></a>
</span><span id="Serializer-533"><a href="#Serializer-533"><span class="linenos">533</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-534"><a href="#Serializer-534"><span class="linenos">534</span></a>    <span class="k">def</span> <span class="nf">_json__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-535"><a href="#Serializer-535"><span class="linenos">535</span></a>        <span class="k">return</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-536"><a href="#Serializer-536"><span class="linenos">536</span></a>
</span><span id="Serializer-537"><a href="#Serializer-537"><span class="linenos">537</span></a>    <span class="c1"># simplejson</span>
</span><span id="Serializer-538"><a href="#Serializer-538"><span class="linenos">538</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-539"><a href="#Serializer-539"><span class="linenos">539</span></a>    <span class="k">def</span> <span class="nf">_simplejson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-540"><a href="#Serializer-540"><span class="linenos">540</span></a>        <span class="n">simplejson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-541"><a href="#Serializer-541"><span class="linenos">541</span></a>
</span><span id="Serializer-542"><a href="#Serializer-542"><span class="linenos">542</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-543"><a href="#Serializer-543"><span class="linenos">543</span></a>    <span class="k">def</span> <span class="nf">_simplejson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-544"><a href="#Serializer-544"><span class="linenos">544</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-545"><a href="#Serializer-545"><span class="linenos">545</span></a>
</span><span id="Serializer-546"><a href="#Serializer-546"><span class="linenos">546</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-547"><a href="#Serializer-547"><span class="linenos">547</span></a>    <span class="k">def</span> <span class="nf">_simplejson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-548"><a href="#Serializer-548"><span class="linenos">548</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-549"><a href="#Serializer-549"><span class="linenos">549</span></a>
</span><span id="Serializer-550"><a href="#Serializer-550"><span class="linenos">550</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-551"><a href="#Serializer-551"><span class="linenos">551</span></a>    <span class="k">def</span> <span class="nf">_simplejson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-552"><a href="#Serializer-552"><span class="linenos">552</span></a>        <span class="k">return</span> <span class="n">simplejson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-553"><a href="#Serializer-553"><span class="linenos">553</span></a>
</span><span id="Serializer-554"><a href="#Serializer-554"><span class="linenos">554</span></a>    <span class="c1"># ujson</span>
</span><span id="Serializer-555"><a href="#Serializer-555"><span class="linenos">555</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-556"><a href="#Serializer-556"><span class="linenos">556</span></a>    <span class="k">def</span> <span class="nf">_ujson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-557"><a href="#Serializer-557"><span class="linenos">557</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_dump_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-558"><a href="#Serializer-558"><span class="linenos">558</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-559"><a href="#Serializer-559"><span class="linenos">559</span></a>        <span class="n">ujson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-560"><a href="#Serializer-560"><span class="linenos">560</span></a>
</span><span id="Serializer-561"><a href="#Serializer-561"><span class="linenos">561</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-562"><a href="#Serializer-562"><span class="linenos">562</span></a>    <span class="k">def</span> <span class="nf">_ujson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-563"><a href="#Serializer-563"><span class="linenos">563</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_dumps_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-564"><a href="#Serializer-564"><span class="linenos">564</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-565"><a href="#Serializer-565"><span class="linenos">565</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-566"><a href="#Serializer-566"><span class="linenos">566</span></a>
</span><span id="Serializer-567"><a href="#Serializer-567"><span class="linenos">567</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-568"><a href="#Serializer-568"><span class="linenos">568</span></a>    <span class="k">def</span> <span class="nf">_ujson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-569"><a href="#Serializer-569"><span class="linenos">569</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_load_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-570"><a href="#Serializer-570"><span class="linenos">570</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-571"><a href="#Serializer-571"><span class="linenos">571</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-572"><a href="#Serializer-572"><span class="linenos">572</span></a>
</span><span id="Serializer-573"><a href="#Serializer-573"><span class="linenos">573</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-574"><a href="#Serializer-574"><span class="linenos">574</span></a>    <span class="k">def</span> <span class="nf">_ujson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-575"><a href="#Serializer-575"><span class="linenos">575</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">ujson_loads_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-576"><a href="#Serializer-576"><span class="linenos">576</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-577"><a href="#Serializer-577"><span class="linenos">577</span></a>        <span class="k">return</span> <span class="n">ujson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-578"><a href="#Serializer-578"><span class="linenos">578</span></a>
</span><span id="Serializer-579"><a href="#Serializer-579"><span class="linenos">579</span></a>    <span class="c1"># orjson</span>
</span><span id="Serializer-580"><a href="#Serializer-580"><span class="linenos">580</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-581"><a href="#Serializer-581"><span class="linenos">581</span></a>    <span class="k">def</span> <span class="nf">_orjson__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-582"><a href="#Serializer-582"><span class="linenos">582</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_dump_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-583"><a href="#Serializer-583"><span class="linenos">583</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-584"><a href="#Serializer-584"><span class="linenos">584</span></a>        <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;option&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">orjson</span><span class="o">.</span><span class="n">OPT_NON_STR_KEYS</span>
</span><span id="Serializer-585"><a href="#Serializer-585"><span class="linenos">585</span></a>        <span class="n">orjson</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-586"><a href="#Serializer-586"><span class="linenos">586</span></a>
</span><span id="Serializer-587"><a href="#Serializer-587"><span class="linenos">587</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-588"><a href="#Serializer-588"><span class="linenos">588</span></a>    <span class="k">def</span> <span class="nf">_orjson__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-589"><a href="#Serializer-589"><span class="linenos">589</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_dumps_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-590"><a href="#Serializer-590"><span class="linenos">590</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-591"><a href="#Serializer-591"><span class="linenos">591</span></a>        <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;option&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">orjson</span><span class="o">.</span><span class="n">OPT_NON_STR_KEYS</span>
</span><span id="Serializer-592"><a href="#Serializer-592"><span class="linenos">592</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="Serializer-593"><a href="#Serializer-593"><span class="linenos">593</span></a>
</span><span id="Serializer-594"><a href="#Serializer-594"><span class="linenos">594</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-595"><a href="#Serializer-595"><span class="linenos">595</span></a>    <span class="k">def</span> <span class="nf">_orjson__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-596"><a href="#Serializer-596"><span class="linenos">596</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_load_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-597"><a href="#Serializer-597"><span class="linenos">597</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-598"><a href="#Serializer-598"><span class="linenos">598</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-599"><a href="#Serializer-599"><span class="linenos">599</span></a>
</span><span id="Serializer-600"><a href="#Serializer-600"><span class="linenos">600</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-601"><a href="#Serializer-601"><span class="linenos">601</span></a>    <span class="k">def</span> <span class="nf">_orjson__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-602"><a href="#Serializer-602"><span class="linenos">602</span></a>        <span class="k">for</span> <span class="n">unnecessary_parameter</span> <span class="ow">in</span> <span class="n">orjson_loads_skip_parameters</span><span class="p">:</span>
</span><span id="Serializer-603"><a href="#Serializer-603"><span class="linenos">603</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">unnecessary_parameter</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="Serializer-604"><a href="#Serializer-604"><span class="linenos">604</span></a>        <span class="k">return</span> <span class="n">orjson</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-605"><a href="#Serializer-605"><span class="linenos">605</span></a>
</span><span id="Serializer-606"><a href="#Serializer-606"><span class="linenos">606</span></a>    <span class="c1"># tnetstring</span>
</span><span id="Serializer-607"><a href="#Serializer-607"><span class="linenos">607</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-608"><a href="#Serializer-608"><span class="linenos">608</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-609"><a href="#Serializer-609"><span class="linenos">609</span></a>        <span class="n">tnetstring</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-610"><a href="#Serializer-610"><span class="linenos">610</span></a>
</span><span id="Serializer-611"><a href="#Serializer-611"><span class="linenos">611</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-612"><a href="#Serializer-612"><span class="linenos">612</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-613"><a href="#Serializer-613"><span class="linenos">613</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-614"><a href="#Serializer-614"><span class="linenos">614</span></a>
</span><span id="Serializer-615"><a href="#Serializer-615"><span class="linenos">615</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-616"><a href="#Serializer-616"><span class="linenos">616</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-617"><a href="#Serializer-617"><span class="linenos">617</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-618"><a href="#Serializer-618"><span class="linenos">618</span></a>
</span><span id="Serializer-619"><a href="#Serializer-619"><span class="linenos">619</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-620"><a href="#Serializer-620"><span class="linenos">620</span></a>    <span class="k">def</span> <span class="nf">_tnetstring__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-621"><a href="#Serializer-621"><span class="linenos">621</span></a>        <span class="k">return</span> <span class="n">tnetstring</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-622"><a href="#Serializer-622"><span class="linenos">622</span></a>
</span><span id="Serializer-623"><a href="#Serializer-623"><span class="linenos">623</span></a>    <span class="c1"># msgpack</span>
</span><span id="Serializer-624"><a href="#Serializer-624"><span class="linenos">624</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-625"><a href="#Serializer-625"><span class="linenos">625</span></a>    <span class="k">def</span> <span class="nf">_msgpack__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-626"><a href="#Serializer-626"><span class="linenos">626</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-627"><a href="#Serializer-627"><span class="linenos">627</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated.</span>
</span><span id="Serializer-628"><a href="#Serializer-628"><span class="linenos">628</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="Serializer-629"><a href="#Serializer-629"><span class="linenos">629</span></a>        <span class="p">}</span>
</span><span id="Serializer-630"><a href="#Serializer-630"><span class="linenos">630</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-631"><a href="#Serializer-631"><span class="linenos">631</span></a>        <span class="n">msgpack</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-632"><a href="#Serializer-632"><span class="linenos">632</span></a>
</span><span id="Serializer-633"><a href="#Serializer-633"><span class="linenos">633</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-634"><a href="#Serializer-634"><span class="linenos">634</span></a>    <span class="k">def</span> <span class="nf">_msgpack__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-635"><a href="#Serializer-635"><span class="linenos">635</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-636"><a href="#Serializer-636"><span class="linenos">636</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated.</span>
</span><span id="Serializer-637"><a href="#Serializer-637"><span class="linenos">637</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="Serializer-638"><a href="#Serializer-638"><span class="linenos">638</span></a>        <span class="p">}</span>
</span><span id="Serializer-639"><a href="#Serializer-639"><span class="linenos">639</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-640"><a href="#Serializer-640"><span class="linenos">640</span></a>        <span class="k">return</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-641"><a href="#Serializer-641"><span class="linenos">641</span></a>
</span><span id="Serializer-642"><a href="#Serializer-642"><span class="linenos">642</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-643"><a href="#Serializer-643"><span class="linenos">643</span></a>    <span class="k">def</span> <span class="nf">_msgpack__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-644"><a href="#Serializer-644"><span class="linenos">644</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-645"><a href="#Serializer-645"><span class="linenos">645</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.</span>
</span><span id="Serializer-646"><a href="#Serializer-646"><span class="linenos">646</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-647"><a href="#Serializer-647"><span class="linenos">647</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="Serializer-648"><a href="#Serializer-648"><span class="linenos">648</span></a>            <span class="s1">&#39;strict_map_key&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-649"><a href="#Serializer-649"><span class="linenos">649</span></a>        <span class="p">}</span>
</span><span id="Serializer-650"><a href="#Serializer-650"><span class="linenos">650</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-651"><a href="#Serializer-651"><span class="linenos">651</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-652"><a href="#Serializer-652"><span class="linenos">652</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-653"><a href="#Serializer-653"><span class="linenos">653</span></a>        
</span><span id="Serializer-654"><a href="#Serializer-654"><span class="linenos">654</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-655"><a href="#Serializer-655"><span class="linenos">655</span></a>
</span><span id="Serializer-656"><a href="#Serializer-656"><span class="linenos">656</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-657"><a href="#Serializer-657"><span class="linenos">657</span></a>    <span class="k">def</span> <span class="nf">_msgpack__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-658"><a href="#Serializer-658"><span class="linenos">658</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-659"><a href="#Serializer-659"><span class="linenos">659</span></a>            <span class="c1"># &#39;encoding&#39;: &#39;utf-8&#39;,  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.</span>
</span><span id="Serializer-660"><a href="#Serializer-660"><span class="linenos">660</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-661"><a href="#Serializer-661"><span class="linenos">661</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
</span><span id="Serializer-662"><a href="#Serializer-662"><span class="linenos">662</span></a>            <span class="s1">&#39;strict_map_key&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-663"><a href="#Serializer-663"><span class="linenos">663</span></a>        <span class="p">}</span>
</span><span id="Serializer-664"><a href="#Serializer-664"><span class="linenos">664</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-665"><a href="#Serializer-665"><span class="linenos">665</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-666"><a href="#Serializer-666"><span class="linenos">666</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-667"><a href="#Serializer-667"><span class="linenos">667</span></a>        
</span><span id="Serializer-668"><a href="#Serializer-668"><span class="linenos">668</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-669"><a href="#Serializer-669"><span class="linenos">669</span></a>
</span><span id="Serializer-670"><a href="#Serializer-670"><span class="linenos">670</span></a>    <span class="c1"># msgpack_fast</span>
</span><span id="Serializer-671"><a href="#Serializer-671"><span class="linenos">671</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-672"><a href="#Serializer-672"><span class="linenos">672</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-673"><a href="#Serializer-673"><span class="linenos">673</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-674"><a href="#Serializer-674"><span class="linenos">674</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="Serializer-675"><a href="#Serializer-675"><span class="linenos">675</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span>
</span><span id="Serializer-676"><a href="#Serializer-676"><span class="linenos">676</span></a>        <span class="p">}</span>
</span><span id="Serializer-677"><a href="#Serializer-677"><span class="linenos">677</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-678"><a href="#Serializer-678"><span class="linenos">678</span></a>        <span class="n">msgpack</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-679"><a href="#Serializer-679"><span class="linenos">679</span></a>
</span><span id="Serializer-680"><a href="#Serializer-680"><span class="linenos">680</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-681"><a href="#Serializer-681"><span class="linenos">681</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-682"><a href="#Serializer-682"><span class="linenos">682</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-683"><a href="#Serializer-683"><span class="linenos">683</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="Serializer-684"><a href="#Serializer-684"><span class="linenos">684</span></a>            <span class="s1">&#39;use_bin_type&#39;</span><span class="p">:</span> <span class="kc">True</span>
</span><span id="Serializer-685"><a href="#Serializer-685"><span class="linenos">685</span></a>        <span class="p">}</span>
</span><span id="Serializer-686"><a href="#Serializer-686"><span class="linenos">686</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-687"><a href="#Serializer-687"><span class="linenos">687</span></a>        <span class="k">return</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-688"><a href="#Serializer-688"><span class="linenos">688</span></a>
</span><span id="Serializer-689"><a href="#Serializer-689"><span class="linenos">689</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-690"><a href="#Serializer-690"><span class="linenos">690</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-691"><a href="#Serializer-691"><span class="linenos">691</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-692"><a href="#Serializer-692"><span class="linenos">692</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="Serializer-693"><a href="#Serializer-693"><span class="linenos">693</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-694"><a href="#Serializer-694"><span class="linenos">694</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">False</span>
</span><span id="Serializer-695"><a href="#Serializer-695"><span class="linenos">695</span></a>        <span class="p">}</span>
</span><span id="Serializer-696"><a href="#Serializer-696"><span class="linenos">696</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-697"><a href="#Serializer-697"><span class="linenos">697</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-698"><a href="#Serializer-698"><span class="linenos">698</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-699"><a href="#Serializer-699"><span class="linenos">699</span></a>        
</span><span id="Serializer-700"><a href="#Serializer-700"><span class="linenos">700</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-701"><a href="#Serializer-701"><span class="linenos">701</span></a>
</span><span id="Serializer-702"><a href="#Serializer-702"><span class="linenos">702</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-703"><a href="#Serializer-703"><span class="linenos">703</span></a>    <span class="k">def</span> <span class="nf">_msgpack_fast__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-704"><a href="#Serializer-704"><span class="linenos">704</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="Serializer-705"><a href="#Serializer-705"><span class="linenos">705</span></a>            <span class="s1">&#39;encoding&#39;</span><span class="p">:</span> <span class="s1">&#39;utf-8&#39;</span><span class="p">,</span>
</span><span id="Serializer-706"><a href="#Serializer-706"><span class="linenos">706</span></a>            <span class="s1">&#39;raw&#39;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
</span><span id="Serializer-707"><a href="#Serializer-707"><span class="linenos">707</span></a>            <span class="s1">&#39;use_list&#39;</span><span class="p">:</span> <span class="kc">False</span>
</span><span id="Serializer-708"><a href="#Serializer-708"><span class="linenos">708</span></a>        <span class="p">}</span>
</span><span id="Serializer-709"><a href="#Serializer-709"><span class="linenos">709</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-710"><a href="#Serializer-710"><span class="linenos">710</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-711"><a href="#Serializer-711"><span class="linenos">711</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgpack</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-712"><a href="#Serializer-712"><span class="linenos">712</span></a>        
</span><span id="Serializer-713"><a href="#Serializer-713"><span class="linenos">713</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-714"><a href="#Serializer-714"><span class="linenos">714</span></a>
</span><span id="Serializer-715"><a href="#Serializer-715"><span class="linenos">715</span></a>    <span class="c1"># msgspec_messagepack</span>
</span><span id="Serializer-716"><a href="#Serializer-716"><span class="linenos">716</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-717"><a href="#Serializer-717"><span class="linenos">717</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-718"><a href="#Serializer-718"><span class="linenos">718</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="Serializer-719"><a href="#Serializer-719"><span class="linenos">719</span></a>
</span><span id="Serializer-720"><a href="#Serializer-720"><span class="linenos">720</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-721"><a href="#Serializer-721"><span class="linenos">721</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-722"><a href="#Serializer-722"><span class="linenos">722</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-723"><a href="#Serializer-723"><span class="linenos">723</span></a>
</span><span id="Serializer-724"><a href="#Serializer-724"><span class="linenos">724</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-725"><a href="#Serializer-725"><span class="linenos">725</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-726"><a href="#Serializer-726"><span class="linenos">726</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-727"><a href="#Serializer-727"><span class="linenos">727</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-728"><a href="#Serializer-728"><span class="linenos">728</span></a>        
</span><span id="Serializer-729"><a href="#Serializer-729"><span class="linenos">729</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-730"><a href="#Serializer-730"><span class="linenos">730</span></a>
</span><span id="Serializer-731"><a href="#Serializer-731"><span class="linenos">731</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-732"><a href="#Serializer-732"><span class="linenos">732</span></a>    <span class="k">def</span> <span class="nf">_msgspec_messagepack__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-733"><a href="#Serializer-733"><span class="linenos">733</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-734"><a href="#Serializer-734"><span class="linenos">734</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">msgpack</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-735"><a href="#Serializer-735"><span class="linenos">735</span></a>        
</span><span id="Serializer-736"><a href="#Serializer-736"><span class="linenos">736</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-737"><a href="#Serializer-737"><span class="linenos">737</span></a>
</span><span id="Serializer-738"><a href="#Serializer-738"><span class="linenos">738</span></a>    <span class="c1"># msgspec_json</span>
</span><span id="Serializer-739"><a href="#Serializer-739"><span class="linenos">739</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-740"><a href="#Serializer-740"><span class="linenos">740</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-741"><a href="#Serializer-741"><span class="linenos">741</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="Serializer-742"><a href="#Serializer-742"><span class="linenos">742</span></a>
</span><span id="Serializer-743"><a href="#Serializer-743"><span class="linenos">743</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-744"><a href="#Serializer-744"><span class="linenos">744</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-745"><a href="#Serializer-745"><span class="linenos">745</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-746"><a href="#Serializer-746"><span class="linenos">746</span></a>
</span><span id="Serializer-747"><a href="#Serializer-747"><span class="linenos">747</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-748"><a href="#Serializer-748"><span class="linenos">748</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-749"><a href="#Serializer-749"><span class="linenos">749</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-750"><a href="#Serializer-750"><span class="linenos">750</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-751"><a href="#Serializer-751"><span class="linenos">751</span></a>        
</span><span id="Serializer-752"><a href="#Serializer-752"><span class="linenos">752</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-753"><a href="#Serializer-753"><span class="linenos">753</span></a>
</span><span id="Serializer-754"><a href="#Serializer-754"><span class="linenos">754</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-755"><a href="#Serializer-755"><span class="linenos">755</span></a>    <span class="k">def</span> <span class="nf">_msgspec_json__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-756"><a href="#Serializer-756"><span class="linenos">756</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-757"><a href="#Serializer-757"><span class="linenos">757</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">json</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-758"><a href="#Serializer-758"><span class="linenos">758</span></a>        
</span><span id="Serializer-759"><a href="#Serializer-759"><span class="linenos">759</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-760"><a href="#Serializer-760"><span class="linenos">760</span></a>
</span><span id="Serializer-761"><a href="#Serializer-761"><span class="linenos">761</span></a>    <span class="c1"># msgspec_yaml</span>
</span><span id="Serializer-762"><a href="#Serializer-762"><span class="linenos">762</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-763"><a href="#Serializer-763"><span class="linenos">763</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-764"><a href="#Serializer-764"><span class="linenos">764</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="Serializer-765"><a href="#Serializer-765"><span class="linenos">765</span></a>
</span><span id="Serializer-766"><a href="#Serializer-766"><span class="linenos">766</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-767"><a href="#Serializer-767"><span class="linenos">767</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-768"><a href="#Serializer-768"><span class="linenos">768</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-769"><a href="#Serializer-769"><span class="linenos">769</span></a>
</span><span id="Serializer-770"><a href="#Serializer-770"><span class="linenos">770</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-771"><a href="#Serializer-771"><span class="linenos">771</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-772"><a href="#Serializer-772"><span class="linenos">772</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-773"><a href="#Serializer-773"><span class="linenos">773</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-774"><a href="#Serializer-774"><span class="linenos">774</span></a>        
</span><span id="Serializer-775"><a href="#Serializer-775"><span class="linenos">775</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-776"><a href="#Serializer-776"><span class="linenos">776</span></a>
</span><span id="Serializer-777"><a href="#Serializer-777"><span class="linenos">777</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-778"><a href="#Serializer-778"><span class="linenos">778</span></a>    <span class="k">def</span> <span class="nf">_msgspec_yaml__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-779"><a href="#Serializer-779"><span class="linenos">779</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-780"><a href="#Serializer-780"><span class="linenos">780</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">yaml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-781"><a href="#Serializer-781"><span class="linenos">781</span></a>        
</span><span id="Serializer-782"><a href="#Serializer-782"><span class="linenos">782</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-783"><a href="#Serializer-783"><span class="linenos">783</span></a>
</span><span id="Serializer-784"><a href="#Serializer-784"><span class="linenos">784</span></a>    <span class="c1"># msgspec_toml</span>
</span><span id="Serializer-785"><a href="#Serializer-785"><span class="linenos">785</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-786"><a href="#Serializer-786"><span class="linenos">786</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__dump</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-787"><a href="#Serializer-787"><span class="linenos">787</span></a>        <span class="n">fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="Serializer-788"><a href="#Serializer-788"><span class="linenos">788</span></a>
</span><span id="Serializer-789"><a href="#Serializer-789"><span class="linenos">789</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-790"><a href="#Serializer-790"><span class="linenos">790</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-791"><a href="#Serializer-791"><span class="linenos">791</span></a>        <span class="k">return</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-792"><a href="#Serializer-792"><span class="linenos">792</span></a>
</span><span id="Serializer-793"><a href="#Serializer-793"><span class="linenos">793</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-794"><a href="#Serializer-794"><span class="linenos">794</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__load</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-795"><a href="#Serializer-795"><span class="linenos">795</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-796"><a href="#Serializer-796"><span class="linenos">796</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-797"><a href="#Serializer-797"><span class="linenos">797</span></a>        
</span><span id="Serializer-798"><a href="#Serializer-798"><span class="linenos">798</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-799"><a href="#Serializer-799"><span class="linenos">799</span></a>
</span><span id="Serializer-800"><a href="#Serializer-800"><span class="linenos">800</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-801"><a href="#Serializer-801"><span class="linenos">801</span></a>    <span class="k">def</span> <span class="nf">_msgspec_toml__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-802"><a href="#Serializer-802"><span class="linenos">802</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="Serializer-803"><a href="#Serializer-803"><span class="linenos">803</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">msgspec</span><span class="o">.</span><span class="n">toml</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-804"><a href="#Serializer-804"><span class="linenos">804</span></a>        
</span><span id="Serializer-805"><a href="#Serializer-805"><span class="linenos">805</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="Serializer-806"><a href="#Serializer-806"><span class="linenos">806</span></a>
</span><span id="Serializer-807"><a href="#Serializer-807"><span class="linenos">807</span></a>    <span class="c1"># cbor</span>
</span><span id="Serializer-808"><a href="#Serializer-808"><span class="linenos">808</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-809"><a href="#Serializer-809"><span class="linenos">809</span></a>    <span class="k">def</span> <span class="nf">_cbor__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-810"><a href="#Serializer-810"><span class="linenos">810</span></a>        <span class="n">cbor</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-811"><a href="#Serializer-811"><span class="linenos">811</span></a>
</span><span id="Serializer-812"><a href="#Serializer-812"><span class="linenos">812</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-813"><a href="#Serializer-813"><span class="linenos">813</span></a>    <span class="k">def</span> <span class="nf">_cbor__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-814"><a href="#Serializer-814"><span class="linenos">814</span></a>        <span class="k">return</span> <span class="n">cbor</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-815"><a href="#Serializer-815"><span class="linenos">815</span></a>
</span><span id="Serializer-816"><a href="#Serializer-816"><span class="linenos">816</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-817"><a href="#Serializer-817"><span class="linenos">817</span></a>    <span class="k">def</span> <span class="nf">_cbor__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-818"><a href="#Serializer-818"><span class="linenos">818</span></a>        <span class="n">cbor</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-819"><a href="#Serializer-819"><span class="linenos">819</span></a>
</span><span id="Serializer-820"><a href="#Serializer-820"><span class="linenos">820</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-821"><a href="#Serializer-821"><span class="linenos">821</span></a>    <span class="k">def</span> <span class="nf">_cbor__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-822"><a href="#Serializer-822"><span class="linenos">822</span></a>        <span class="k">return</span> <span class="n">cbor</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-823"><a href="#Serializer-823"><span class="linenos">823</span></a>
</span><span id="Serializer-824"><a href="#Serializer-824"><span class="linenos">824</span></a>    <span class="c1"># cbor2</span>
</span><span id="Serializer-825"><a href="#Serializer-825"><span class="linenos">825</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-826"><a href="#Serializer-826"><span class="linenos">826</span></a>    <span class="k">def</span> <span class="nf">_cbor2__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-827"><a href="#Serializer-827"><span class="linenos">827</span></a>        <span class="n">cbor2</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-828"><a href="#Serializer-828"><span class="linenos">828</span></a>
</span><span id="Serializer-829"><a href="#Serializer-829"><span class="linenos">829</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-830"><a href="#Serializer-830"><span class="linenos">830</span></a>    <span class="k">def</span> <span class="nf">_cbor2__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-831"><a href="#Serializer-831"><span class="linenos">831</span></a>        <span class="k">return</span> <span class="n">cbor2</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-832"><a href="#Serializer-832"><span class="linenos">832</span></a>
</span><span id="Serializer-833"><a href="#Serializer-833"><span class="linenos">833</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-834"><a href="#Serializer-834"><span class="linenos">834</span></a>    <span class="k">def</span> <span class="nf">_cbor2__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-835"><a href="#Serializer-835"><span class="linenos">835</span></a>        <span class="n">cbor2</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-836"><a href="#Serializer-836"><span class="linenos">836</span></a>
</span><span id="Serializer-837"><a href="#Serializer-837"><span class="linenos">837</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-838"><a href="#Serializer-838"><span class="linenos">838</span></a>    <span class="k">def</span> <span class="nf">_cbor2__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-839"><a href="#Serializer-839"><span class="linenos">839</span></a>        <span class="k">return</span> <span class="n">cbor2</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-840"><a href="#Serializer-840"><span class="linenos">840</span></a>
</span><span id="Serializer-841"><a href="#Serializer-841"><span class="linenos">841</span></a>    <span class="c1"># marshal</span>
</span><span id="Serializer-842"><a href="#Serializer-842"><span class="linenos">842</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-843"><a href="#Serializer-843"><span class="linenos">843</span></a>    <span class="k">def</span> <span class="nf">_marshal__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-844"><a href="#Serializer-844"><span class="linenos">844</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="Serializer-845"><a href="#Serializer-845"><span class="linenos">845</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="Serializer-846"><a href="#Serializer-846"><span class="linenos">846</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Serializer-847"><a href="#Serializer-847"><span class="linenos">847</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">args</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="Serializer-848"><a href="#Serializer-848"><span class="linenos">848</span></a>        <span class="n">marshal</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">result_args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-849"><a href="#Serializer-849"><span class="linenos">849</span></a>
</span><span id="Serializer-850"><a href="#Serializer-850"><span class="linenos">850</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-851"><a href="#Serializer-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">_marshal__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-852"><a href="#Serializer-852"><span class="linenos">852</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="Serializer-853"><a href="#Serializer-853"><span class="linenos">853</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="Serializer-854"><a href="#Serializer-854"><span class="linenos">854</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Serializer-855"><a href="#Serializer-855"><span class="linenos">855</span></a>            <span class="n">result_args</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="Serializer-856"><a href="#Serializer-856"><span class="linenos">856</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">result_args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-857"><a href="#Serializer-857"><span class="linenos">857</span></a>
</span><span id="Serializer-858"><a href="#Serializer-858"><span class="linenos">858</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-859"><a href="#Serializer-859"><span class="linenos">859</span></a>    <span class="k">def</span> <span class="nf">_marshal__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-860"><a href="#Serializer-860"><span class="linenos">860</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-861"><a href="#Serializer-861"><span class="linenos">861</span></a>
</span><span id="Serializer-862"><a href="#Serializer-862"><span class="linenos">862</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-863"><a href="#Serializer-863"><span class="linenos">863</span></a>    <span class="k">def</span> <span class="nf">_marshal__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-864"><a href="#Serializer-864"><span class="linenos">864</span></a>        <span class="k">return</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-865"><a href="#Serializer-865"><span class="linenos">865</span></a>
</span><span id="Serializer-866"><a href="#Serializer-866"><span class="linenos">866</span></a>    <span class="c1"># pickle</span>
</span><span id="Serializer-867"><a href="#Serializer-867"><span class="linenos">867</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-868"><a href="#Serializer-868"><span class="linenos">868</span></a>    <span class="k">def</span> <span class="nf">_pickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-869"><a href="#Serializer-869"><span class="linenos">869</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-870"><a href="#Serializer-870"><span class="linenos">870</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-871"><a href="#Serializer-871"><span class="linenos">871</span></a>        <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-872"><a href="#Serializer-872"><span class="linenos">872</span></a>
</span><span id="Serializer-873"><a href="#Serializer-873"><span class="linenos">873</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-874"><a href="#Serializer-874"><span class="linenos">874</span></a>    <span class="k">def</span> <span class="nf">_pickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-875"><a href="#Serializer-875"><span class="linenos">875</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-876"><a href="#Serializer-876"><span class="linenos">876</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-877"><a href="#Serializer-877"><span class="linenos">877</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-878"><a href="#Serializer-878"><span class="linenos">878</span></a>
</span><span id="Serializer-879"><a href="#Serializer-879"><span class="linenos">879</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-880"><a href="#Serializer-880"><span class="linenos">880</span></a>    <span class="k">def</span> <span class="nf">_pickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-881"><a href="#Serializer-881"><span class="linenos">881</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-882"><a href="#Serializer-882"><span class="linenos">882</span></a>
</span><span id="Serializer-883"><a href="#Serializer-883"><span class="linenos">883</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-884"><a href="#Serializer-884"><span class="linenos">884</span></a>    <span class="k">def</span> <span class="nf">_pickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-885"><a href="#Serializer-885"><span class="linenos">885</span></a>        <span class="k">return</span> <span class="n">pickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-886"><a href="#Serializer-886"><span class="linenos">886</span></a>
</span><span id="Serializer-887"><a href="#Serializer-887"><span class="linenos">887</span></a>    <span class="c1"># cPickle</span>
</span><span id="Serializer-888"><a href="#Serializer-888"><span class="linenos">888</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-889"><a href="#Serializer-889"><span class="linenos">889</span></a>    <span class="k">def</span> <span class="nf">_cpickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-890"><a href="#Serializer-890"><span class="linenos">890</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-891"><a href="#Serializer-891"><span class="linenos">891</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-892"><a href="#Serializer-892"><span class="linenos">892</span></a>        <span class="n">cPickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-893"><a href="#Serializer-893"><span class="linenos">893</span></a>
</span><span id="Serializer-894"><a href="#Serializer-894"><span class="linenos">894</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-895"><a href="#Serializer-895"><span class="linenos">895</span></a>    <span class="k">def</span> <span class="nf">_cpickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-896"><a href="#Serializer-896"><span class="linenos">896</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-897"><a href="#Serializer-897"><span class="linenos">897</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-898"><a href="#Serializer-898"><span class="linenos">898</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-899"><a href="#Serializer-899"><span class="linenos">899</span></a>
</span><span id="Serializer-900"><a href="#Serializer-900"><span class="linenos">900</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-901"><a href="#Serializer-901"><span class="linenos">901</span></a>    <span class="k">def</span> <span class="nf">_cpickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-902"><a href="#Serializer-902"><span class="linenos">902</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-903"><a href="#Serializer-903"><span class="linenos">903</span></a>
</span><span id="Serializer-904"><a href="#Serializer-904"><span class="linenos">904</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-905"><a href="#Serializer-905"><span class="linenos">905</span></a>    <span class="k">def</span> <span class="nf">_cpickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-906"><a href="#Serializer-906"><span class="linenos">906</span></a>        <span class="k">return</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-907"><a href="#Serializer-907"><span class="linenos">907</span></a>
</span><span id="Serializer-908"><a href="#Serializer-908"><span class="linenos">908</span></a>    <span class="c1"># cloudpickle</span>
</span><span id="Serializer-909"><a href="#Serializer-909"><span class="linenos">909</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-910"><a href="#Serializer-910"><span class="linenos">910</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-911"><a href="#Serializer-911"><span class="linenos">911</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-912"><a href="#Serializer-912"><span class="linenos">912</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-913"><a href="#Serializer-913"><span class="linenos">913</span></a>        <span class="n">cloudpickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-914"><a href="#Serializer-914"><span class="linenos">914</span></a>
</span><span id="Serializer-915"><a href="#Serializer-915"><span class="linenos">915</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-916"><a href="#Serializer-916"><span class="linenos">916</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-917"><a href="#Serializer-917"><span class="linenos">917</span></a>        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;protocol&#39;</span><span class="p">:</span> <span class="o">-</span><span class="mi">1</span><span class="p">}</span>
</span><span id="Serializer-918"><a href="#Serializer-918"><span class="linenos">918</span></a>        <span class="n">result_kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-919"><a href="#Serializer-919"><span class="linenos">919</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">result_kwargs</span><span class="p">)</span>
</span><span id="Serializer-920"><a href="#Serializer-920"><span class="linenos">920</span></a>
</span><span id="Serializer-921"><a href="#Serializer-921"><span class="linenos">921</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-922"><a href="#Serializer-922"><span class="linenos">922</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-923"><a href="#Serializer-923"><span class="linenos">923</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="Serializer-924"><a href="#Serializer-924"><span class="linenos">924</span></a>
</span><span id="Serializer-925"><a href="#Serializer-925"><span class="linenos">925</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Serializer-926"><a href="#Serializer-926"><span class="linenos">926</span></a>    <span class="k">def</span> <span class="nf">_cloudpickle__loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="Serializer-927"><a href="#Serializer-927"><span class="linenos">927</span></a>        <span class="k">return</span> <span class="n">cloudpickle</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="Serializer.__init__" class="classattr">
                                        <input id="Serializer.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Serializer</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">serializer</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">NoneType</span><span class="p">,</span> <span class="n"><a href="#Serializers">Serializers</a></span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Serializer.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Serializer.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Serializer.__init__-493"><a href="#Serializer.__init__-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">serializer</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="n">Serializers</span><span class="p">]):</span>
</span><span id="Serializer.__init__-494"><a href="#Serializer.__init__-494"><span class="linenos">494</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dump</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer.__init__-495"><a href="#Serializer.__init__-495"><span class="linenos">495</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dumps</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer.__init__-496"><a href="#Serializer.__init__-496"><span class="linenos">496</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">load</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer.__init__-497"><a href="#Serializer.__init__-497"><span class="linenos">497</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loads</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer.__init__-498"><a href="#Serializer.__init__-498"><span class="linenos">498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="Serializer.__init__-499"><a href="#Serializer.__init__-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">serializer</span> <span class="o">=</span> <span class="n">serializer</span>
</span></pre></div>


    

                            </div>
                            <div id="Serializer.dump" class="classattr">
                                <div class="attr variable">
            <span class="name">dump</span>

        
    </div>
    <a class="headerlink" href="#Serializer.dump"></a>
    
    

                            </div>
                            <div id="Serializer.dumps" class="classattr">
                                <div class="attr variable">
            <span class="name">dumps</span>

        
    </div>
    <a class="headerlink" href="#Serializer.dumps"></a>
    
    

                            </div>
                            <div id="Serializer.load" class="classattr">
                                <div class="attr variable">
            <span class="name">load</span>

        
    </div>
    <a class="headerlink" href="#Serializer.load"></a>
    
    

                            </div>
                            <div id="Serializer.loads" class="classattr">
                                <div class="attr variable">
            <span class="name">loads</span>

        
    </div>
    <a class="headerlink" href="#Serializer.loads"></a>
    
    

                            </div>
                            <div id="Serializer.serializer" class="classattr">
                                        <input id="Serializer.serializer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">serializer</span>

                <label class="view-source-button" for="Serializer.serializer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Serializer.serializer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Serializer.serializer-501"><a href="#Serializer.serializer-501"><span class="linenos">501</span></a>    <span class="nd">@property</span>
</span><span id="Serializer.serializer-502"><a href="#Serializer.serializer-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="nf">serializer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Serializer.serializer-503"><a href="#Serializer.serializer-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_serializer</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="get_an_appropriate_serializers">
                            <input id="get_an_appropriate_serializers-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_an_appropriate_serializers</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">desired_features</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Set</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#Tags">Tags</a></span><span class="p">,</span> <span class="n"><a href="#DataFormats">DataFormats</a></span><span class="p">]]</span></span><span class="return-annotation">) -> <span class="n">Set</span><span class="p">[</span><span class="n"><a href="#Serializers">Serializers</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_an_appropriate_serializers-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_an_appropriate_serializers"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_an_appropriate_serializers-930"><a href="#get_an_appropriate_serializers-930"><span class="linenos">930</span></a><span class="k">def</span> <span class="nf">get_an_appropriate_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Serializers</span><span class="p">]:</span>
</span><span id="get_an_appropriate_serializers-931"><a href="#get_an_appropriate_serializers-931"><span class="linenos">931</span></a>    <span class="n">appropriate_serializers</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="get_an_appropriate_serializers-932"><a href="#get_an_appropriate_serializers-932"><span class="linenos">932</span></a>    <span class="k">for</span> <span class="n">serializer_type</span> <span class="ow">in</span> <span class="n">EXISTING_SERIALIZERS</span><span class="p">:</span>
</span><span id="get_an_appropriate_serializers-933"><a href="#get_an_appropriate_serializers-933"><span class="linenos">933</span></a>        <span class="n">serializer_features</span> <span class="o">=</span> <span class="n">SERIALIZERS_DESCRIPTION</span><span class="p">[</span><span class="n">serializer_type</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="get_an_appropriate_serializers-934"><a href="#get_an_appropriate_serializers-934"><span class="linenos">934</span></a>        <span class="k">if</span> <span class="n">desired_features</span><span class="o">.</span><span class="n">issubset</span><span class="p">(</span><span class="n">serializer_features</span><span class="p">):</span>
</span><span id="get_an_appropriate_serializers-935"><a href="#get_an_appropriate_serializers-935"><span class="linenos">935</span></a>            <span class="n">appropriate_serializers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="get_an_appropriate_serializers-936"><a href="#get_an_appropriate_serializers-936"><span class="linenos">936</span></a>    <span class="k">return</span> <span class="n">appropriate_serializers</span>
</span></pre></div>


    

                </section>
                <section id="SerializerPerformance">
                    <div class="attr variable">
            <span class="name">SerializerPerformance</span>        =
<span class="default_value">&lt;class &#39;float&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#SerializerPerformance"></a>
    
    

                </section>
                <section id="SerializerFootprint">
                    <div class="attr variable">
            <span class="name">SerializerFootprint</span>        =
<span class="default_value">&lt;class &#39;int&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#SerializerFootprint"></a>
    
    

                </section>
                <section id="serializer_benchmark">
                            <input id="serializer_benchmark-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serializer_benchmark</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">serializer_type</span><span class="p">:</span> <span class="n"><a href="#Serializers">Serializers</a></span>,</span><span class="param">	<span class="n">test_data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="serializer_benchmark-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#serializer_benchmark"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="serializer_benchmark-943"><a href="#serializer_benchmark-943"><span class="linenos">943</span></a><span class="k">def</span> <span class="nf">serializer_benchmark</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">:</span> <span class="n">Serializers</span><span class="p">,</span> <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="serializer_benchmark-944"><a href="#serializer_benchmark-944"><span class="linenos">944</span></a>                         <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">SerializerPerformance</span><span class="p">,</span> <span class="n">SerializerFootprint</span><span class="p">]:</span>
</span><span id="serializer_benchmark-945"><a href="#serializer_benchmark-945"><span class="linenos">945</span></a>    <span class="n">serializer</span> <span class="o">=</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="serializer_benchmark-946"><a href="#serializer_benchmark-946"><span class="linenos">946</span></a>    <span class="n">measurements</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="serializer_benchmark-947"><a href="#serializer_benchmark-947"><span class="linenos">947</span></a>    <span class="n">tr</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">test_time</span><span class="p">)</span>
</span><span id="serializer_benchmark-948"><a href="#serializer_benchmark-948"><span class="linenos">948</span></a>    <span class="k">while</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="serializer_benchmark-949"><a href="#serializer_benchmark-949"><span class="linenos">949</span></a>        <span class="n">start_time</span> <span class="o">=</span> <span class="n">perf_counter</span><span class="p">()</span>
</span><span id="serializer_benchmark-950"><a href="#serializer_benchmark-950"><span class="linenos">950</span></a>        <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">test_data</span><span class="p">))</span>
</span><span id="serializer_benchmark-951"><a href="#serializer_benchmark-951"><span class="linenos">951</span></a>        <span class="n">measurements</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">perf_counter</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span><span class="p">)</span>
</span><span id="serializer_benchmark-952"><a href="#serializer_benchmark-952"><span class="linenos">952</span></a>
</span><span id="serializer_benchmark-953"><a href="#serializer_benchmark-953"><span class="linenos">953</span></a>    <span class="n">best_measurement</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">measurements</span><span class="p">)</span>
</span><span id="serializer_benchmark-954"><a href="#serializer_benchmark-954"><span class="linenos">954</span></a>    <span class="n">best_performance</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">/</span> <span class="n">best_measurement</span><span class="p">)</span> <span class="k">if</span> <span class="n">best_measurement</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="serializer_benchmark-955"><a href="#serializer_benchmark-955"><span class="linenos">955</span></a>    <span class="n">data_dump</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">test_data</span><span class="p">)</span>
</span><span id="serializer_benchmark-956"><a href="#serializer_benchmark-956"><span class="linenos">956</span></a>    <span class="k">return</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter_per_time_unit</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">data_dump</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_most_efficient_serializers">
                            <input id="get_most_efficient_serializers-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_most_efficient_serializers</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">desired_features</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Set</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#Tags">Tags</a></span><span class="p">,</span> <span class="n"><a href="#DataFormats">DataFormats</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">test_data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n"><a href="#Serializers">Serializers</a></span><span class="p">],</span> <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n"><a href="#Serializers">Serializers</a></span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>:</span></span>

                <label class="view-source-button" for="get_most_efficient_serializers-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_most_efficient_serializers"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_most_efficient_serializers-959"><a href="#get_most_efficient_serializers-959"><span class="linenos">959</span></a><span class="k">def</span> <span class="nf">get_most_efficient_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">,</span>
</span><span id="get_most_efficient_serializers-960"><a href="#get_most_efficient_serializers-960"><span class="linenos">960</span></a>                                   <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
</span><span id="get_most_efficient_serializers-961"><a href="#get_most_efficient_serializers-961"><span class="linenos">961</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="get_most_efficient_serializers-962"><a href="#get_most_efficient_serializers-962"><span class="linenos">962</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="n">Serializers</span><span class="p">],</span>
</span><span id="get_most_efficient_serializers-963"><a href="#get_most_efficient_serializers-963"><span class="linenos">963</span></a>                                              <span class="n">Set</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Serializers</span><span class="p">,</span> <span class="n">SerializerPerformance</span><span class="p">,</span> <span class="n">SerializerFootprint</span><span class="p">]]]:</span>
</span><span id="get_most_efficient_serializers-964"><a href="#get_most_efficient_serializers-964"><span class="linenos">964</span></a>    <span class="c1"># TODO: сделать класс, который бы подбирал количество итераций под нужное время выдержки в секундах (float)</span>
</span><span id="get_most_efficient_serializers-965"><a href="#get_most_efficient_serializers-965"><span class="linenos">965</span></a>    <span class="c1"># это необходимо для того чтобы правильно протестировать производительность под PyPy</span>
</span><span id="get_most_efficient_serializers-966"><a href="#get_most_efficient_serializers-966"><span class="linenos">966</span></a>    <span class="c1"># в дальнейшем этот функционал стоит перенести в модуль performance_test_lib</span>
</span><span id="get_most_efficient_serializers-967"><a href="#get_most_efficient_serializers-967"><span class="linenos">967</span></a>    <span class="c1"># TODO: make some caching algorithm. Lru can not be used since it requires all function parameters be hashable and both desired_features and test_data are not</span>
</span><span id="get_most_efficient_serializers-968"><a href="#get_most_efficient_serializers-968"><span class="linenos">968</span></a>
</span><span id="get_most_efficient_serializers-969"><a href="#get_most_efficient_serializers-969"><span class="linenos">969</span></a>    <span class="n">appropriate_serializers</span> <span class="o">=</span> <span class="n">get_an_appropriate_serializers</span><span class="p">(</span><span class="n">desired_features</span><span class="p">)</span>
</span><span id="get_most_efficient_serializers-970"><a href="#get_most_efficient_serializers-970"><span class="linenos">970</span></a>
</span><span id="get_most_efficient_serializers-971"><a href="#get_most_efficient_serializers-971"><span class="linenos">971</span></a>    <span class="n">benchmark_results</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>  <span class="c1"># type: Dict[float, Set[Serializers]]</span>
</span><span id="get_most_efficient_serializers-972"><a href="#get_most_efficient_serializers-972"><span class="linenos">972</span></a>    <span class="n">serializers_data</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>  <span class="c1"># type: Set[Tuple[Serializers, SerializerPerformance, SerializerFootprint]]</span>
</span><span id="get_most_efficient_serializers-973"><a href="#get_most_efficient_serializers-973"><span class="linenos">973</span></a>    <span class="k">for</span> <span class="n">serializer_type</span> <span class="ow">in</span> <span class="n">appropriate_serializers</span><span class="p">:</span>
</span><span id="get_most_efficient_serializers-974"><a href="#get_most_efficient_serializers-974"><span class="linenos">974</span></a>        <span class="k">with</span> <span class="n">DisableGC</span><span class="p">():</span>
</span><span id="get_most_efficient_serializers-975"><a href="#get_most_efficient_serializers-975"><span class="linenos">975</span></a>            <span class="n">performance</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="n">dump_size</span> <span class="o">=</span> <span class="n">serializer_benchmark</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">,</span> <span class="n">test_data</span><span class="p">,</span> <span class="n">test_time</span><span class="p">)</span>
</span><span id="get_most_efficient_serializers-976"><a href="#get_most_efficient_serializers-976"><span class="linenos">976</span></a>        
</span><span id="get_most_efficient_serializers-977"><a href="#get_most_efficient_serializers-977"><span class="linenos">977</span></a>        <span class="k">if</span> <span class="n">best_performance</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">benchmark_results</span><span class="p">:</span>
</span><span id="get_most_efficient_serializers-978"><a href="#get_most_efficient_serializers-978"><span class="linenos">978</span></a>            <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="get_most_efficient_serializers-979"><a href="#get_most_efficient_serializers-979"><span class="linenos">979</span></a>        
</span><span id="get_most_efficient_serializers-980"><a href="#get_most_efficient_serializers-980"><span class="linenos">980</span></a>        <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">serializer_type</span><span class="p">)</span>
</span><span id="get_most_efficient_serializers-981"><a href="#get_most_efficient_serializers-981"><span class="linenos">981</span></a>        <span class="n">serializers_data</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">serializer_type</span><span class="p">,</span> <span class="n">best_performance</span><span class="p">,</span> <span class="n">dump_size</span><span class="p">))</span>
</span><span id="get_most_efficient_serializers-982"><a href="#get_most_efficient_serializers-982"><span class="linenos">982</span></a>    
</span><span id="get_most_efficient_serializers-983"><a href="#get_most_efficient_serializers-983"><span class="linenos">983</span></a>    <span class="n">best_performance</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">benchmark_results</span><span class="p">)</span>
</span><span id="get_most_efficient_serializers-984"><a href="#get_most_efficient_serializers-984"><span class="linenos">984</span></a>    <span class="n">best_serializers</span> <span class="o">=</span> <span class="n">benchmark_results</span><span class="p">[</span><span class="n">best_performance</span><span class="p">]</span>
</span><span id="get_most_efficient_serializers-985"><a href="#get_most_efficient_serializers-985"><span class="linenos">985</span></a>    <span class="k">return</span> <span class="n">best_serializers</span><span class="p">,</span> <span class="n">serializers_data</span>
</span></pre></div>


    

                </section>
                <section id="best_serializer">
                            <input id="best_serializer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">best_serializer</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">desired_features</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Set</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#Tags">Tags</a></span><span class="p">,</span> <span class="n"><a href="#DataFormats">DataFormats</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">test_data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Any</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span></span><span class="return-annotation">) -> <span class="n"><a href="#Serializer">Serializer</a></span>:</span></span>

                <label class="view-source-button" for="best_serializer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#best_serializer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="best_serializer-988"><a href="#best_serializer-988"><span class="linenos">988</span></a><span class="k">def</span> <span class="nf">best_serializer</span><span class="p">(</span><span class="n">desired_features</span><span class="p">:</span> <span class="n">SerializerFeatures</span><span class="p">,</span>
</span><span id="best_serializer-989"><a href="#best_serializer-989"><span class="linenos">989</span></a>                                   <span class="n">test_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span>
</span><span id="best_serializer-990"><a href="#best_serializer-990"><span class="linenos">990</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="best_serializer-991"><a href="#best_serializer-991"><span class="linenos">991</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Serializer</span><span class="p">:</span>
</span><span id="best_serializer-992"><a href="#best_serializer-992"><span class="linenos">992</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_most_efficient_serializers</span><span class="p">(</span>
</span><span id="best_serializer-993"><a href="#best_serializer-993"><span class="linenos">993</span></a>        <span class="n">desired_features</span><span class="p">,</span>
</span><span id="best_serializer-994"><a href="#best_serializer-994"><span class="linenos">994</span></a>        <span class="n">test_data</span><span class="p">,</span>
</span><span id="best_serializer-995"><a href="#best_serializer-995"><span class="linenos">995</span></a>        <span class="n">test_time</span><span class="p">)</span>
</span><span id="best_serializer-996"><a href="#best_serializer-996"><span class="linenos">996</span></a>    <span class="n">best_serializers</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="best_serializer-997"><a href="#best_serializer-997"><span class="linenos">997</span></a>    <span class="k">return</span> <span class="n">Serializer</span><span class="p">(</span><span class="n">best_serializers</span><span class="o">.</span><span class="n">pop</span><span class="p">())</span>
</span></pre></div>


    

                </section>
                <section id="TestDataType">
                            <input id="TestDataType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TestDataType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="TestDataType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestDataType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestDataType-1000"><a href="#TestDataType-1000"><span class="linenos">1000</span></a><span class="k">class</span> <span class="nc">TestDataType</span><span class="p">(</span><span class="n">enum</span><span class="o">.</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="TestDataType-1001"><a href="#TestDataType-1001"><span class="linenos">1001</span></a>    <span class="n">small</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TestDataType-1002"><a href="#TestDataType-1002"><span class="linenos">1002</span></a>    <span class="n">deep_small</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="TestDataType-1003"><a href="#TestDataType-1003"><span class="linenos">1003</span></a>    <span class="n">large</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="TestDataType-1004"><a href="#TestDataType-1004"><span class="linenos">1004</span></a>    <span class="n">deep_large</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="TestDataType.small" class="classattr">
                                <div class="attr variable">
            <span class="name">small</span>        =
<span class="default_value">&lt;<a href="#TestDataType.small">TestDataType.small</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#TestDataType.small"></a>
    
    

                            </div>
                            <div id="TestDataType.deep_small" class="classattr">
                                <div class="attr variable">
            <span class="name">deep_small</span>        =
<span class="default_value">&lt;<a href="#TestDataType.deep_small">TestDataType.deep_small</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#TestDataType.deep_small"></a>
    
    

                            </div>
                            <div id="TestDataType.large" class="classattr">
                                <div class="attr variable">
            <span class="name">large</span>        =
<span class="default_value">&lt;<a href="#TestDataType.large">TestDataType.large</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#TestDataType.large"></a>
    
    

                            </div>
                            <div id="TestDataType.deep_large" class="classattr">
                                <div class="attr variable">
            <span class="name">deep_large</span>        =
<span class="default_value">&lt;<a href="#TestDataType.deep_large">TestDataType.deep_large</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#TestDataType.deep_large"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="TestDataType.name" class="variable">name</dd>
                <dd id="TestDataType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="test_data_factory">
                            <input id="test_data_factory-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">test_data_factory</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">test_data_type</span><span class="p">:</span> <span class="n"><a href="#TestDataType">TestDataType</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="test_data_factory-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#test_data_factory"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="test_data_factory-1007"><a href="#test_data_factory-1007"><span class="linenos">1007</span></a><span class="k">def</span> <span class="nf">test_data_factory</span><span class="p">(</span><span class="n">test_data_type</span><span class="p">:</span> <span class="n">TestDataType</span><span class="p">):</span>
</span><span id="test_data_factory-1008"><a href="#test_data_factory-1008"><span class="linenos">1008</span></a>    <span class="k">if</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">small</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="test_data_factory-1009"><a href="#test_data_factory-1009"><span class="linenos">1009</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="test_data_factory-1010"><a href="#test_data_factory-1010"><span class="linenos">1010</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1011"><a href="#test_data_factory-1011"><span class="linenos">1011</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="test_data_factory-1012"><a href="#test_data_factory-1012"><span class="linenos">1012</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="test_data_factory-1013"><a href="#test_data_factory-1013"><span class="linenos">1013</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1014"><a href="#test_data_factory-1014"><span class="linenos">1014</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="test_data_factory-1015"><a href="#test_data_factory-1015"><span class="linenos">1015</span></a>                <span class="p">{</span>
</span><span id="test_data_factory-1016"><a href="#test_data_factory-1016"><span class="linenos">1016</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1017"><a href="#test_data_factory-1017"><span class="linenos">1017</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">2</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1018"><a href="#test_data_factory-1018"><span class="linenos">1018</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="test_data_factory-1019"><a href="#test_data_factory-1019"><span class="linenos">1019</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1020"><a href="#test_data_factory-1020"><span class="linenos">1020</span></a>                            <span class="s1">&#39;world&#39;</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="test_data_factory-1021"><a href="#test_data_factory-1021"><span class="linenos">1021</span></a>                        <span class="p">}</span>
</span><span id="test_data_factory-1022"><a href="#test_data_factory-1022"><span class="linenos">1022</span></a>                    <span class="p">}</span>
</span><span id="test_data_factory-1023"><a href="#test_data_factory-1023"><span class="linenos">1023</span></a>                <span class="p">}</span>
</span><span id="test_data_factory-1024"><a href="#test_data_factory-1024"><span class="linenos">1024</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="test_data_factory-1025"><a href="#test_data_factory-1025"><span class="linenos">1025</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span>
</span><span id="test_data_factory-1026"><a href="#test_data_factory-1026"><span class="linenos">1026</span></a>        <span class="p">}</span>
</span><span id="test_data_factory-1027"><a href="#test_data_factory-1027"><span class="linenos">1027</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_small</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="test_data_factory-1028"><a href="#test_data_factory-1028"><span class="linenos">1028</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="test_data_factory-1029"><a href="#test_data_factory-1029"><span class="linenos">1029</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1030"><a href="#test_data_factory-1030"><span class="linenos">1030</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="test_data_factory-1031"><a href="#test_data_factory-1031"><span class="linenos">1031</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="test_data_factory-1032"><a href="#test_data_factory-1032"><span class="linenos">1032</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1033"><a href="#test_data_factory-1033"><span class="linenos">1033</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="test_data_factory-1034"><a href="#test_data_factory-1034"><span class="linenos">1034</span></a>                <span class="p">{</span>
</span><span id="test_data_factory-1035"><a href="#test_data_factory-1035"><span class="linenos">1035</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1036"><a href="#test_data_factory-1036"><span class="linenos">1036</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">2</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1037"><a href="#test_data_factory-1037"><span class="linenos">1037</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">1000</span><span class="p">,</span>
</span><span id="test_data_factory-1038"><a href="#test_data_factory-1038"><span class="linenos">1038</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1039"><a href="#test_data_factory-1039"><span class="linenos">1039</span></a>                            <span class="s1">&#39;world&#39;</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="test_data_factory-1040"><a href="#test_data_factory-1040"><span class="linenos">1040</span></a>                        <span class="p">}</span>
</span><span id="test_data_factory-1041"><a href="#test_data_factory-1041"><span class="linenos">1041</span></a>                    <span class="p">}</span>
</span><span id="test_data_factory-1042"><a href="#test_data_factory-1042"><span class="linenos">1042</span></a>                <span class="p">}</span>
</span><span id="test_data_factory-1043"><a href="#test_data_factory-1043"><span class="linenos">1043</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">20</span><span class="p">,</span>
</span><span id="test_data_factory-1044"><a href="#test_data_factory-1044"><span class="linenos">1044</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span>
</span><span id="test_data_factory-1045"><a href="#test_data_factory-1045"><span class="linenos">1045</span></a>        <span class="p">}</span>
</span><span id="test_data_factory-1046"><a href="#test_data_factory-1046"><span class="linenos">1046</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">large</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="test_data_factory-1047"><a href="#test_data_factory-1047"><span class="linenos">1047</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="test_data_factory-1048"><a href="#test_data_factory-1048"><span class="linenos">1048</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span>
</span><span id="test_data_factory-1049"><a href="#test_data_factory-1049"><span class="linenos">1049</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="test_data_factory-1050"><a href="#test_data_factory-1050"><span class="linenos">1050</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="test_data_factory-1051"><a href="#test_data_factory-1051"><span class="linenos">1051</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1052"><a href="#test_data_factory-1052"><span class="linenos">1052</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="test_data_factory-1053"><a href="#test_data_factory-1053"><span class="linenos">1053</span></a>                <span class="p">{</span>
</span><span id="test_data_factory-1054"><a href="#test_data_factory-1054"><span class="linenos">1054</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1055"><a href="#test_data_factory-1055"><span class="linenos">1055</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1056"><a href="#test_data_factory-1056"><span class="linenos">1056</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="test_data_factory-1057"><a href="#test_data_factory-1057"><span class="linenos">1057</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1058"><a href="#test_data_factory-1058"><span class="linenos">1058</span></a>                            <span class="s1">&#39;world&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="test_data_factory-1059"><a href="#test_data_factory-1059"><span class="linenos">1059</span></a>                        <span class="p">}</span>
</span><span id="test_data_factory-1060"><a href="#test_data_factory-1060"><span class="linenos">1060</span></a>                    <span class="p">}</span>
</span><span id="test_data_factory-1061"><a href="#test_data_factory-1061"><span class="linenos">1061</span></a>                <span class="p">}</span>
</span><span id="test_data_factory-1062"><a href="#test_data_factory-1062"><span class="linenos">1062</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">2</span><span class="p">,</span>
</span><span id="test_data_factory-1063"><a href="#test_data_factory-1063"><span class="linenos">1063</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span><span class="o">*</span><span class="mi">100</span>
</span><span id="test_data_factory-1064"><a href="#test_data_factory-1064"><span class="linenos">1064</span></a>        <span class="p">}</span>
</span><span id="test_data_factory-1065"><a href="#test_data_factory-1065"><span class="linenos">1065</span></a>    <span class="k">elif</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_large</span> <span class="o">==</span> <span class="n">test_data_type</span><span class="p">:</span>
</span><span id="test_data_factory-1066"><a href="#test_data_factory-1066"><span class="linenos">1066</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="test_data_factory-1067"><a href="#test_data_factory-1067"><span class="linenos">1067</span></a>            <span class="mi">1</span><span class="p">:</span> <span class="s1">&#39;Hello&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">,</span>
</span><span id="test_data_factory-1068"><a href="#test_data_factory-1068"><span class="linenos">1068</span></a>            <span class="mi">2</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;W&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="test_data_factory-1069"><a href="#test_data_factory-1069"><span class="linenos">1069</span></a>            <span class="mi">3</span><span class="p">:</span> <span class="p">[</span>
</span><span id="test_data_factory-1070"><a href="#test_data_factory-1070"><span class="linenos">1070</span></a>                <span class="s1">&#39;r&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1071"><a href="#test_data_factory-1071"><span class="linenos">1071</span></a>                <span class="mi">1</span><span class="p">,</span>
</span><span id="test_data_factory-1072"><a href="#test_data_factory-1072"><span class="linenos">1072</span></a>                <span class="p">{</span>
</span><span id="test_data_factory-1073"><a href="#test_data_factory-1073"><span class="linenos">1073</span></a>                    <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="s1">&#39;.&#39;</span><span class="p">,</span>
</span><span id="test_data_factory-1074"><a href="#test_data_factory-1074"><span class="linenos">1074</span></a>                    <span class="s1">&#39;d&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1075"><a href="#test_data_factory-1075"><span class="linenos">1075</span></a>                        <span class="mi">43</span><span class="p">:</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">*</span><span class="mi">1000</span><span class="p">,</span>
</span><span id="test_data_factory-1076"><a href="#test_data_factory-1076"><span class="linenos">1076</span></a>                        <span class="mi">15</span><span class="p">:</span> <span class="p">{</span>
</span><span id="test_data_factory-1077"><a href="#test_data_factory-1077"><span class="linenos">1077</span></a>                            <span class="s1">&#39;world&#39;</span><span class="o">*</span><span class="mi">100</span><span class="p">:</span> <span class="mi">42</span>
</span><span id="test_data_factory-1078"><a href="#test_data_factory-1078"><span class="linenos">1078</span></a>                        <span class="p">}</span>
</span><span id="test_data_factory-1079"><a href="#test_data_factory-1079"><span class="linenos">1079</span></a>                    <span class="p">}</span>
</span><span id="test_data_factory-1080"><a href="#test_data_factory-1080"><span class="linenos">1080</span></a>                <span class="p">}</span>
</span><span id="test_data_factory-1081"><a href="#test_data_factory-1081"><span class="linenos">1081</span></a>            <span class="p">]</span><span class="o">*</span><span class="mi">20</span><span class="p">,</span>
</span><span id="test_data_factory-1082"><a href="#test_data_factory-1082"><span class="linenos">1082</span></a>            <span class="s1">&#39;To all!&#39;</span><span class="p">:</span> <span class="s1">&#39;!!1&#39;</span><span class="o">*</span><span class="mi">100</span>
</span><span id="test_data_factory-1083"><a href="#test_data_factory-1083"><span class="linenos">1083</span></a>        <span class="p">}</span>
</span></pre></div>


    

                </section>
                <section id="best_serializer_for_standard_data">
                            <input id="best_serializer_for_standard_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@lru_cache(maxsize=100)</div>

        <span class="def">def</span>
        <span class="name">best_serializer_for_standard_data</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">desired_features_tuple</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#Tags">Tags</a></span><span class="p">,</span> <span class="n"><a href="#DataFormats">DataFormats</a></span><span class="p">]]</span>,</span><span class="param">	<span class="n">test_data_type</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#TestDataType">TestDataType</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span></span><span class="return-annotation">) -> <span class="n"><a href="#Serializer">Serializer</a></span>:</span></span>

                <label class="view-source-button" for="best_serializer_for_standard_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#best_serializer_for_standard_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="best_serializer_for_standard_data-1086"><a href="#best_serializer_for_standard_data-1086"><span class="linenos">1086</span></a><span class="nd">@lru_cache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>
</span><span id="best_serializer_for_standard_data-1087"><a href="#best_serializer_for_standard_data-1087"><span class="linenos">1087</span></a><span class="k">def</span> <span class="nf">best_serializer_for_standard_data</span><span class="p">(</span><span class="n">desired_features_tuple</span><span class="p">:</span> <span class="n">SerializerFeaturesTuple</span><span class="p">,</span>
</span><span id="best_serializer_for_standard_data-1088"><a href="#best_serializer_for_standard_data-1088"><span class="linenos">1088</span></a>                                   <span class="n">test_data_type</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TestDataType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="best_serializer_for_standard_data-1089"><a href="#best_serializer_for_standard_data-1089"><span class="linenos">1089</span></a>                                   <span class="n">test_time</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">1.0</span>
</span><span id="best_serializer_for_standard_data-1090"><a href="#best_serializer_for_standard_data-1090"><span class="linenos">1090</span></a>                                   <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Serializer</span><span class="p">:</span>
</span><span id="best_serializer_for_standard_data-1091"><a href="#best_serializer_for_standard_data-1091"><span class="linenos">1091</span></a>    <span class="n">test_data_type</span> <span class="o">=</span> <span class="n">TestDataType</span><span class="o">.</span><span class="n">small</span> <span class="k">if</span> <span class="n">test_data_type</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">test_data_type</span>
</span><span id="best_serializer_for_standard_data-1092"><a href="#best_serializer_for_standard_data-1092"><span class="linenos">1092</span></a>    <span class="k">return</span> <span class="n">best_serializer</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">desired_features_tuple</span><span class="p">),</span> <span class="n">test_data_factory</span><span class="p">(</span><span class="n">test_data_type</span><span class="p">),</span> <span class="n">test_time</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>