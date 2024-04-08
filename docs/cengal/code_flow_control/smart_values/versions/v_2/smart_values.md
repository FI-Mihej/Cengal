---
title: smart_values
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.smart_values<wbr>.versions<wbr>.v_2<wbr>.smart_values    </h1>

                
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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a>        <span class="s1">&#39;ValueExistenceNamedTuple&#39;</span><span class="p">,</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>        <span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>        <span class="s1">&#39;ValueHolder&#39;</span><span class="p">,</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>        <span class="s1">&#39;ResultExistence&#39;</span><span class="p">,</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>        <span class="s1">&#39;ResultHolder&#39;</span><span class="p">,</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>        <span class="s1">&#39;ErrorExistence&#39;</span><span class="p">,</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>        <span class="s1">&#39;ErrorHolder&#39;</span><span class="p">,</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>        <span class="s1">&#39;ValueCache&#39;</span><span class="p">,</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>        <span class="s1">&#39;ValueTypeNamedTuple&#39;</span><span class="p">,</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>        <span class="s1">&#39;ValueType&#39;</span><span class="p">,</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a>        <span class="s1">&#39;ValueWithTypeNamedTuple&#39;</span><span class="p">,</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>        <span class="s1">&#39;ValueWithType&#39;</span><span class="p">,</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>    <span class="p">]</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">,</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">from</span> <span class="nn">collections.abc</span> <span class="kn">import</span> <span class="n">Sequence</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">TypeVar</span><span class="p">,</span> <span class="n">Generic</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">NamedTuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="sd">Module Docstring</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.3&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="c1"># TODO: implement Cython version (smart_values are used by our Cython code)</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="n">VT</span> <span class="o">=</span> <span class="n">TypeVar</span><span class="p">(</span><span class="s1">&#39;VT&#39;</span><span class="p">)</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="n">ValueExistenceNamedTuple</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s1">&#39;ValueExistenceNamedTuple&#39;</span><span class="p">,</span> <span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="k">class</span> <span class="nc">ValueExistence</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;existence&#39;</span><span class="p">,</span> <span class="s1">&#39;_value&#39;</span><span class="p">)</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_value</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="nd">@property</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_value</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="nd">@value</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">:</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="p">}</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="p">}</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">):</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="k">class</span> <span class="nc">ValueHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="k">class</span> <span class="nc">ResultExistence</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a><span class="k">class</span> <span class="nc">ResultHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a><span class="k">class</span> <span class="nc">ErrorExistence</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="k">class</span> <span class="nc">ErrorHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="k">class</span> <span class="nc">ValueCache</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ValueCache</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VT</span><span class="p">:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">new_value</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>    
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>    
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a><span class="n">TT</span> <span class="o">=</span> <span class="n">TypeVar</span><span class="p">(</span><span class="s1">&#39;TT&#39;</span><span class="p">)</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a><span class="n">ValueTypeNamedTuple</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s1">&#39;ValueTypeNamedTuple&#39;</span><span class="p">,</span> <span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a><span class="k">class</span> <span class="nc">ValueType</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">TT</span><span class="p">,</span> <span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the value&quot;</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="p">(</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">ValueWithType</span><span class="p">)):</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueTypeNamedTuple</span><span class="p">:</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="k">return</span> <span class="n">ValueTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>    
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>        <span class="p">}</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>    
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="p">}</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>    
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>    
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>    
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>    
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>    
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">):</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a><span class="n">ValueWithTypeNamedTuple</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s1">&#39;ValueWithTypeNamedTuple&#39;</span><span class="p">,</span> <span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a><span class="k">class</span> <span class="nc">ValueWithType</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">TT</span><span class="p">,</span> <span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the value&quot;</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueType</span><span class="p">):</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueWithType</span><span class="p">):</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>    
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">:</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        <span class="k">return</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>    
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="p">}</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>    
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="p">}</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>    
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>    
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>    
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>    
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>    
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">):</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="ValueExistenceNamedTuple">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueExistenceNamedTuple</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#ValueExistenceNamedTuple"></a>
    
            <div class="docstring"><p>ValueExistenceNamedTuple(existence, value)</p>
</div>


                            <div id="ValueExistenceNamedTuple.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">ValueExistenceNamedTuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span>, </span><span class="param"><span class="n">value</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#ValueExistenceNamedTuple.__init__"></a>
    
            <div class="docstring"><p>Create new instance of ValueExistenceNamedTuple(existence, value)</p>
</div>


                            </div>
                            <div id="ValueExistenceNamedTuple.existence" class="classattr">
                                <div class="attr variable">
            <span class="name">existence</span>

        
    </div>
    <a class="headerlink" href="#ValueExistenceNamedTuple.existence"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="ValueExistenceNamedTuple.value" class="classattr">
                                <div class="attr variable">
            <span class="name">value</span>

        
    </div>
    <a class="headerlink" href="#ValueExistenceNamedTuple.value"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="ValueExistenceNamedTuple.index" class="function">index</dd>
                <dd id="ValueExistenceNamedTuple.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueExistence">
                            <input id="ValueExistence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueExistence</span><wbr>(<span class="base">typing.Generic[~VT]</span>, <span class="base">collections.abc.Sequence</span>):

                <label class="view-source-button" for="ValueExistence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence-66"><a href="#ValueExistence-66"><span class="linenos"> 66</span></a><span class="k">class</span> <span class="nc">ValueExistence</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="ValueExistence-67"><a href="#ValueExistence-67"><span class="linenos"> 67</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;existence&#39;</span><span class="p">,</span> <span class="s1">&#39;_value&#39;</span><span class="p">)</span>
</span><span id="ValueExistence-68"><a href="#ValueExistence-68"><span class="linenos"> 68</span></a>
</span><span id="ValueExistence-69"><a href="#ValueExistence-69"><span class="linenos"> 69</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueExistence-70"><a href="#ValueExistence-70"><span class="linenos"> 70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence-71"><a href="#ValueExistence-71"><span class="linenos"> 71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueExistence-72"><a href="#ValueExistence-72"><span class="linenos"> 72</span></a>
</span><span id="ValueExistence-73"><a href="#ValueExistence-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-74"><a href="#ValueExistence-74"><span class="linenos"> 74</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="ValueExistence-75"><a href="#ValueExistence-75"><span class="linenos"> 75</span></a>
</span><span id="ValueExistence-76"><a href="#ValueExistence-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="ValueExistence-77"><a href="#ValueExistence-77"><span class="linenos"> 77</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueExistence-78"><a href="#ValueExistence-78"><span class="linenos"> 78</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="ValueExistence-79"><a href="#ValueExistence-79"><span class="linenos"> 79</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueExistence-80"><a href="#ValueExistence-80"><span class="linenos"> 80</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_value</span>
</span><span id="ValueExistence-81"><a href="#ValueExistence-81"><span class="linenos"> 81</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-82"><a href="#ValueExistence-82"><span class="linenos"> 82</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="ValueExistence-83"><a href="#ValueExistence-83"><span class="linenos"> 83</span></a>    
</span><span id="ValueExistence-84"><a href="#ValueExistence-84"><span class="linenos"> 84</span></a>    <span class="nd">@property</span>
</span><span id="ValueExistence-85"><a href="#ValueExistence-85"><span class="linenos"> 85</span></a>    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-86"><a href="#ValueExistence-86"><span class="linenos"> 86</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_value</span>
</span><span id="ValueExistence-87"><a href="#ValueExistence-87"><span class="linenos"> 87</span></a>    
</span><span id="ValueExistence-88"><a href="#ValueExistence-88"><span class="linenos"> 88</span></a>    <span class="nd">@value</span><span class="o">.</span><span class="n">setter</span>
</span><span id="ValueExistence-89"><a href="#ValueExistence-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="ValueExistence-90"><a href="#ValueExistence-90"><span class="linenos"> 90</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ValueExistence-91"><a href="#ValueExistence-91"><span class="linenos"> 91</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueExistence-92"><a href="#ValueExistence-92"><span class="linenos"> 92</span></a>
</span><span id="ValueExistence-93"><a href="#ValueExistence-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-94"><a href="#ValueExistence-94"><span class="linenos"> 94</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span>
</span><span id="ValueExistence-95"><a href="#ValueExistence-95"><span class="linenos"> 95</span></a>
</span><span id="ValueExistence-96"><a href="#ValueExistence-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-97"><a href="#ValueExistence-97"><span class="linenos"> 97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="ValueExistence-98"><a href="#ValueExistence-98"><span class="linenos"> 98</span></a>
</span><span id="ValueExistence-99"><a href="#ValueExistence-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-100"><a href="#ValueExistence-100"><span class="linenos">100</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="ValueExistence-101"><a href="#ValueExistence-101"><span class="linenos">101</span></a>
</span><span id="ValueExistence-102"><a href="#ValueExistence-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-103"><a href="#ValueExistence-103"><span class="linenos">103</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="ValueExistence-104"><a href="#ValueExistence-104"><span class="linenos">104</span></a>
</span><span id="ValueExistence-105"><a href="#ValueExistence-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence-106"><a href="#ValueExistence-106"><span class="linenos">106</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueExistence-107"><a href="#ValueExistence-107"><span class="linenos">107</span></a>
</span><span id="ValueExistence-108"><a href="#ValueExistence-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueExistence-109"><a href="#ValueExistence-109"><span class="linenos">109</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueExistence-110"><a href="#ValueExistence-110"><span class="linenos">110</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueExistence-111"><a href="#ValueExistence-111"><span class="linenos">111</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence-112"><a href="#ValueExistence-112"><span class="linenos">112</span></a>    
</span><span id="ValueExistence-113"><a href="#ValueExistence-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueExistence-114"><a href="#ValueExistence-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueExistence-115"><a href="#ValueExistence-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-116"><a href="#ValueExistence-116"><span class="linenos">116</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-117"><a href="#ValueExistence-117"><span class="linenos">117</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="ValueExistence-118"><a href="#ValueExistence-118"><span class="linenos">118</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="ValueExistence-119"><a href="#ValueExistence-119"><span class="linenos">119</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-120"><a href="#ValueExistence-120"><span class="linenos">120</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="ValueExistence-121"><a href="#ValueExistence-121"><span class="linenos">121</span></a>    
</span><span id="ValueExistence-122"><a href="#ValueExistence-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueExistence-123"><a href="#ValueExistence-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span><span id="ValueExistence-124"><a href="#ValueExistence-124"><span class="linenos">124</span></a>    
</span><span id="ValueExistence-125"><a href="#ValueExistence-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">:</span>
</span><span id="ValueExistence-126"><a href="#ValueExistence-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-127"><a href="#ValueExistence-127"><span class="linenos">127</span></a>    
</span><span id="ValueExistence-128"><a href="#ValueExistence-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueExistence-129"><a href="#ValueExistence-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueExistence-130"><a href="#ValueExistence-130"><span class="linenos">130</span></a>    
</span><span id="ValueExistence-131"><a href="#ValueExistence-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueExistence-132"><a href="#ValueExistence-132"><span class="linenos">132</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueExistence-133"><a href="#ValueExistence-133"><span class="linenos">133</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="ValueExistence-134"><a href="#ValueExistence-134"><span class="linenos">134</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueExistence-135"><a href="#ValueExistence-135"><span class="linenos">135</span></a>        <span class="p">}</span>
</span><span id="ValueExistence-136"><a href="#ValueExistence-136"><span class="linenos">136</span></a>    
</span><span id="ValueExistence-137"><a href="#ValueExistence-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueExistence-138"><a href="#ValueExistence-138"><span class="linenos">138</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueExistence-139"><a href="#ValueExistence-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueExistence-140"><a href="#ValueExistence-140"><span class="linenos">140</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="ValueExistence-141"><a href="#ValueExistence-141"><span class="linenos">141</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueExistence-142"><a href="#ValueExistence-142"><span class="linenos">142</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueExistence-143"><a href="#ValueExistence-143"><span class="linenos">143</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueExistence-144"><a href="#ValueExistence-144"><span class="linenos">144</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueExistence-145"><a href="#ValueExistence-145"><span class="linenos">145</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueExistence-146"><a href="#ValueExistence-146"><span class="linenos">146</span></a>        <span class="p">}</span>
</span><span id="ValueExistence-147"><a href="#ValueExistence-147"><span class="linenos">147</span></a>    
</span><span id="ValueExistence-148"><a href="#ValueExistence-148"><span class="linenos">148</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence-149"><a href="#ValueExistence-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence-150"><a href="#ValueExistence-150"><span class="linenos">150</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-151"><a href="#ValueExistence-151"><span class="linenos">151</span></a>    
</span><span id="ValueExistence-152"><a href="#ValueExistence-152"><span class="linenos">152</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence-153"><a href="#ValueExistence-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence-154"><a href="#ValueExistence-154"><span class="linenos">154</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="ValueExistence-155"><a href="#ValueExistence-155"><span class="linenos">155</span></a>    
</span><span id="ValueExistence-156"><a href="#ValueExistence-156"><span class="linenos">156</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence-157"><a href="#ValueExistence-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence-158"><a href="#ValueExistence-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueExistence-159"><a href="#ValueExistence-159"><span class="linenos">159</span></a>    
</span><span id="ValueExistence-160"><a href="#ValueExistence-160"><span class="linenos">160</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence-161"><a href="#ValueExistence-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence-162"><a href="#ValueExistence-162"><span class="linenos">162</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueExistence-163"><a href="#ValueExistence-163"><span class="linenos">163</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueExistence-164"><a href="#ValueExistence-164"><span class="linenos">164</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-165"><a href="#ValueExistence-165"><span class="linenos">165</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueExistence-166"><a href="#ValueExistence-166"><span class="linenos">166</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueExistence-167"><a href="#ValueExistence-167"><span class="linenos">167</span></a>    
</span><span id="ValueExistence-168"><a href="#ValueExistence-168"><span class="linenos">168</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence-169"><a href="#ValueExistence-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence-170"><a href="#ValueExistence-170"><span class="linenos">170</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueExistence-171"><a href="#ValueExistence-171"><span class="linenos">171</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-172"><a href="#ValueExistence-172"><span class="linenos">172</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">):</span>
</span><span id="ValueExistence-173"><a href="#ValueExistence-173"><span class="linenos">173</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-174"><a href="#ValueExistence-174"><span class="linenos">174</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueExistence-175"><a href="#ValueExistence-175"><span class="linenos">175</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-176"><a href="#ValueExistence-176"><span class="linenos">176</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueExistence-177"><a href="#ValueExistence-177"><span class="linenos">177</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-178"><a href="#ValueExistence-178"><span class="linenos">178</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence-179"><a href="#ValueExistence-179"><span class="linenos">179</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueExistence-180"><a href="#ValueExistence-180"><span class="linenos">180</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence-181"><a href="#ValueExistence-181"><span class="linenos">181</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueExistence-182"><a href="#ValueExistence-182"><span class="linenos">182</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ValueExistence.__init__" class="classattr">
                                        <input id="ValueExistence.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueExistence</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ValueExistence.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.__init__-69"><a href="#ValueExistence.__init__-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueExistence.__init__-70"><a href="#ValueExistence.__init__-70"><span class="linenos">70</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueExistence.__init__-71"><a href="#ValueExistence.__init__-71"><span class="linenos">71</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.existence" class="classattr">
                                <div class="attr variable">
            <span class="name">existence</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#ValueExistence.existence"></a>
    
    

                            </div>
                            <div id="ValueExistence.value" class="classattr">
                                        <input id="ValueExistence.value-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">value</span>

                <label class="view-source-button" for="ValueExistence.value-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.value"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.value-84"><a href="#ValueExistence.value-84"><span class="linenos">84</span></a>    <span class="nd">@property</span>
</span><span id="ValueExistence.value-85"><a href="#ValueExistence.value-85"><span class="linenos">85</span></a>    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueExistence.value-86"><a href="#ValueExistence.value-86"><span class="linenos">86</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.to_namedtuple" class="classattr">
                                        <input id="ValueExistence.to_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistenceNamedTuple">ValueExistenceNamedTuple</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.to_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.to_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.to_namedtuple-125"><a href="#ValueExistence.to_namedtuple-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">:</span>
</span><span id="ValueExistence.to_namedtuple-126"><a href="#ValueExistence.to_namedtuple-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.to_tuple" class="classattr">
                                        <input id="ValueExistence.to_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span>:</span></span>

                <label class="view-source-button" for="ValueExistence.to_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.to_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.to_tuple-128"><a href="#ValueExistence.to_tuple-128"><span class="linenos">128</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueExistence.to_tuple-129"><a href="#ValueExistence.to_tuple-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.to_dict" class="classattr">
                                        <input id="ValueExistence.to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">dict</span>:</span></span>

                <label class="view-source-button" for="ValueExistence.to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.to_dict-131"><a href="#ValueExistence.to_dict-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueExistence.to_dict-132"><a href="#ValueExistence.to_dict-132"><span class="linenos">132</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueExistence.to_dict-133"><a href="#ValueExistence.to_dict-133"><span class="linenos">133</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="ValueExistence.to_dict-134"><a href="#ValueExistence.to_dict-134"><span class="linenos">134</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueExistence.to_dict-135"><a href="#ValueExistence.to_dict-135"><span class="linenos">135</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.serialize_to_dict" class="classattr">
                                        <input id="ValueExistence.serialize_to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serialize_to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ValueExistence.serialize_to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.serialize_to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.serialize_to_dict-137"><a href="#ValueExistence.serialize_to_dict-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueExistence.serialize_to_dict-138"><a href="#ValueExistence.serialize_to_dict-138"><span class="linenos">138</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueExistence.serialize_to_dict-139"><a href="#ValueExistence.serialize_to_dict-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueExistence.serialize_to_dict-140"><a href="#ValueExistence.serialize_to_dict-140"><span class="linenos">140</span></a>            <span class="s1">&#39;existence&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span>
</span><span id="ValueExistence.serialize_to_dict-141"><a href="#ValueExistence.serialize_to_dict-141"><span class="linenos">141</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueExistence.serialize_to_dict-142"><a href="#ValueExistence.serialize_to_dict-142"><span class="linenos">142</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueExistence.serialize_to_dict-143"><a href="#ValueExistence.serialize_to_dict-143"><span class="linenos">143</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueExistence.serialize_to_dict-144"><a href="#ValueExistence.serialize_to_dict-144"><span class="linenos">144</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueExistence.serialize_to_dict-145"><a href="#ValueExistence.serialize_to_dict-145"><span class="linenos">145</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueExistence.serialize_to_dict-146"><a href="#ValueExistence.serialize_to_dict-146"><span class="linenos">146</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.from_namedtuple" class="classattr">
                                        <input id="ValueExistence.from_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">named_tuple</span><span class="p">:</span> <span class="n"><a href="#ValueExistenceNamedTuple">ValueExistenceNamedTuple</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.from_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.from_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.from_namedtuple-148"><a href="#ValueExistence.from_namedtuple-148"><span class="linenos">148</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence.from_namedtuple-149"><a href="#ValueExistence.from_namedtuple-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence.from_namedtuple-150"><a href="#ValueExistence.from_namedtuple-150"><span class="linenos">150</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.from_tuple" class="classattr">
                                        <input id="ValueExistence.from_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_tuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.from_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.from_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.from_tuple-152"><a href="#ValueExistence.from_tuple-152"><span class="linenos">152</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence.from_tuple-153"><a href="#ValueExistence.from_tuple-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence.from_tuple-154"><a href="#ValueExistence.from_tuple-154"><span class="linenos">154</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.from_dict" class="classattr">
                                        <input id="ValueExistence.from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.from_dict-156"><a href="#ValueExistence.from_dict-156"><span class="linenos">156</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence.from_dict-157"><a href="#ValueExistence.from_dict-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence.from_dict-158"><a href="#ValueExistence.from_dict-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.deserialize_from_dict" class="classattr">
                                        <input id="ValueExistence.deserialize_from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">deserialize_from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span>,</span><span class="param">	<span class="n">owning_info</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.deserialize_from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.deserialize_from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.deserialize_from_dict-160"><a href="#ValueExistence.deserialize_from_dict-160"><span class="linenos">160</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence.deserialize_from_dict-161"><a href="#ValueExistence.deserialize_from_dict-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence.deserialize_from_dict-162"><a href="#ValueExistence.deserialize_from_dict-162"><span class="linenos">162</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueExistence.deserialize_from_dict-163"><a href="#ValueExistence.deserialize_from_dict-163"><span class="linenos">163</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueExistence.deserialize_from_dict-164"><a href="#ValueExistence.deserialize_from_dict-164"><span class="linenos">164</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence.deserialize_from_dict-165"><a href="#ValueExistence.deserialize_from_dict-165"><span class="linenos">165</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueExistence.deserialize_from_dict-166"><a href="#ValueExistence.deserialize_from_dict-166"><span class="linenos">166</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;existence&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueExistence.from_other" class="classattr">
                                        <input id="ValueExistence.from_other-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_other</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#ValueExistence">ValueExistence</a></span><span class="p">,</span> <span class="n"><a href="#ValueExistenceNamedTuple">ValueExistenceNamedTuple</a></span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="o">~</span><span class="n">VT</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueExistence.from_other-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueExistence.from_other"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueExistence.from_other-168"><a href="#ValueExistence.from_other-168"><span class="linenos">168</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueExistence.from_other-169"><a href="#ValueExistence.from_other-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueExistence.from_other-170"><a href="#ValueExistence.from_other-170"><span class="linenos">170</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueExistence.from_other-171"><a href="#ValueExistence.from_other-171"><span class="linenos">171</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence.from_other-172"><a href="#ValueExistence.from_other-172"><span class="linenos">172</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistenceNamedTuple</span><span class="p">):</span>
</span><span id="ValueExistence.from_other-173"><a href="#ValueExistence.from_other-173"><span class="linenos">173</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence.from_other-174"><a href="#ValueExistence.from_other-174"><span class="linenos">174</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueExistence.from_other-175"><a href="#ValueExistence.from_other-175"><span class="linenos">175</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence.from_other-176"><a href="#ValueExistence.from_other-176"><span class="linenos">176</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueExistence.from_other-177"><a href="#ValueExistence.from_other-177"><span class="linenos">177</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence.from_other-178"><a href="#ValueExistence.from_other-178"><span class="linenos">178</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueExistence.from_other-179"><a href="#ValueExistence.from_other-179"><span class="linenos">179</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueExistence.from_other-180"><a href="#ValueExistence.from_other-180"><span class="linenos">180</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueExistence.from_other-181"><a href="#ValueExistence.from_other-181"><span class="linenos">181</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueExistence.from_other-182"><a href="#ValueExistence.from_other-182"><span class="linenos">182</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>collections.abc.Sequence</dt>
                                <dd id="ValueExistence.index" class="function">index</dd>
                <dd id="ValueExistence.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueHolder">
                            <input id="ValueHolder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueHolder</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ValueHolder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueHolder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueHolder-185"><a href="#ValueHolder-185"><span class="linenos">185</span></a><span class="k">class</span> <span class="nc">ValueHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ValueHolder-186"><a href="#ValueHolder-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueHolder-187"><a href="#ValueHolder-187"><span class="linenos">187</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ValueHolder.__init__" class="classattr">
                                        <input id="ValueHolder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueHolder</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ValueHolder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueHolder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueHolder.__init__-186"><a href="#ValueHolder.__init__-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueHolder.__init__-187"><a href="#ValueHolder.__init__-187"><span class="linenos">187</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ValueHolder.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ValueHolder.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ValueHolder.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ValueHolder.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ValueHolder.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ValueHolder.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ValueHolder.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ValueHolder.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ValueHolder.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ValueHolder.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ValueHolder.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ValueHolder.index" class="function">index</dd>
                <dd id="ValueHolder.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ResultExistence">
                            <input id="ResultExistence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ResultExistence</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ResultExistence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResultExistence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResultExistence-190"><a href="#ResultExistence-190"><span class="linenos">190</span></a><span class="k">class</span> <span class="nc">ResultExistence</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ResultExistence-191"><a href="#ResultExistence-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResultExistence-192"><a href="#ResultExistence-192"><span class="linenos">192</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ResultExistence.__init__" class="classattr">
                                        <input id="ResultExistence.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ResultExistence</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ResultExistence.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResultExistence.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResultExistence.__init__-191"><a href="#ResultExistence.__init__-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResultExistence.__init__-192"><a href="#ResultExistence.__init__-192"><span class="linenos">192</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ResultExistence.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ResultExistence.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ResultExistence.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ResultExistence.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ResultExistence.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ResultExistence.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ResultExistence.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ResultExistence.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ResultExistence.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ResultExistence.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ResultExistence.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ResultExistence.index" class="function">index</dd>
                <dd id="ResultExistence.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ResultHolder">
                            <input id="ResultHolder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ResultHolder</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ResultHolder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResultHolder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResultHolder-195"><a href="#ResultHolder-195"><span class="linenos">195</span></a><span class="k">class</span> <span class="nc">ResultHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ResultHolder-196"><a href="#ResultHolder-196"><span class="linenos">196</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResultHolder-197"><a href="#ResultHolder-197"><span class="linenos">197</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ResultHolder.__init__" class="classattr">
                                        <input id="ResultHolder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ResultHolder</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ResultHolder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResultHolder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResultHolder.__init__-196"><a href="#ResultHolder.__init__-196"><span class="linenos">196</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ResultHolder.__init__-197"><a href="#ResultHolder.__init__-197"><span class="linenos">197</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ResultHolder.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ResultHolder.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ResultHolder.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ResultHolder.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ResultHolder.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ResultHolder.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ResultHolder.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ResultHolder.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ResultHolder.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ResultHolder.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ResultHolder.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ResultHolder.index" class="function">index</dd>
                <dd id="ResultHolder.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ErrorExistence">
                            <input id="ErrorExistence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ErrorExistence</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ErrorExistence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ErrorExistence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ErrorExistence-200"><a href="#ErrorExistence-200"><span class="linenos">200</span></a><span class="k">class</span> <span class="nc">ErrorExistence</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ErrorExistence-201"><a href="#ErrorExistence-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ErrorExistence-202"><a href="#ErrorExistence-202"><span class="linenos">202</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ErrorExistence.__init__" class="classattr">
                                        <input id="ErrorExistence.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ErrorExistence</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ErrorExistence.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ErrorExistence.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ErrorExistence.__init__-201"><a href="#ErrorExistence.__init__-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ErrorExistence.__init__-202"><a href="#ErrorExistence.__init__-202"><span class="linenos">202</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ErrorExistence.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ErrorExistence.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ErrorExistence.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ErrorExistence.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ErrorExistence.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ErrorExistence.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ErrorExistence.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ErrorExistence.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ErrorExistence.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ErrorExistence.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ErrorExistence.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ErrorExistence.index" class="function">index</dd>
                <dd id="ErrorExistence.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ErrorHolder">
                            <input id="ErrorHolder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ErrorHolder</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ErrorHolder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ErrorHolder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ErrorHolder-205"><a href="#ErrorHolder-205"><span class="linenos">205</span></a><span class="k">class</span> <span class="nc">ErrorHolder</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ErrorHolder-206"><a href="#ErrorHolder-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ErrorHolder-207"><a href="#ErrorHolder-207"><span class="linenos">207</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ErrorHolder.__init__" class="classattr">
                                        <input id="ErrorHolder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ErrorHolder</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ErrorHolder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ErrorHolder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ErrorHolder.__init__-206"><a href="#ErrorHolder.__init__-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ErrorHolder.__init__-207"><a href="#ErrorHolder.__init__-207"><span class="linenos">207</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ErrorHolder.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ErrorHolder.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ErrorHolder.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ErrorHolder.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ErrorHolder.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ErrorHolder.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ErrorHolder.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ErrorHolder.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ErrorHolder.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ErrorHolder.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ErrorHolder.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ErrorHolder.index" class="function">index</dd>
                <dd id="ErrorHolder.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueCache">
                            <input id="ValueCache-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueCache</span><wbr>(<span class="base"><a href="#ValueExistence">cengal.code_flow_control.smart_values.versions.v_2.smart_values.ValueExistence[~VT]</a></span>):

                <label class="view-source-button" for="ValueCache-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache-210"><a href="#ValueCache-210"><span class="linenos">210</span></a><span class="k">class</span> <span class="nc">ValueCache</span><span class="p">(</span><span class="n">ValueExistence</span><span class="p">[</span><span class="n">VT</span><span class="p">]):</span>
</span><span id="ValueCache-211"><a href="#ValueCache-211"><span class="linenos">211</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="ValueCache-212"><a href="#ValueCache-212"><span class="linenos">212</span></a>
</span><span id="ValueCache-213"><a href="#ValueCache-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueCache-214"><a href="#ValueCache-214"><span class="linenos">214</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ValueCache</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span><span id="ValueCache-215"><a href="#ValueCache-215"><span class="linenos">215</span></a>
</span><span id="ValueCache-216"><a href="#ValueCache-216"><span class="linenos">216</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ValueCache-217"><a href="#ValueCache-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ValueCache-218"><a href="#ValueCache-218"><span class="linenos">218</span></a>
</span><span id="ValueCache-219"><a href="#ValueCache-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VT</span><span class="p">:</span>
</span><span id="ValueCache-220"><a href="#ValueCache-220"><span class="linenos">220</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueCache-221"><a href="#ValueCache-221"><span class="linenos">221</span></a>
</span><span id="ValueCache-222"><a href="#ValueCache-222"><span class="linenos">222</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueCache-223"><a href="#ValueCache-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ValueCache-224"><a href="#ValueCache-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">new_value</span>
</span><span id="ValueCache-225"><a href="#ValueCache-225"><span class="linenos">225</span></a>
</span><span id="ValueCache-226"><a href="#ValueCache-226"><span class="linenos">226</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache-227"><a href="#ValueCache-227"><span class="linenos">227</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ValueCache-228"><a href="#ValueCache-228"><span class="linenos">228</span></a>
</span><span id="ValueCache-229"><a href="#ValueCache-229"><span class="linenos">229</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache-230"><a href="#ValueCache-230"><span class="linenos">230</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueCache-231"><a href="#ValueCache-231"><span class="linenos">231</span></a>
</span><span id="ValueCache-232"><a href="#ValueCache-232"><span class="linenos">232</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueCache-233"><a href="#ValueCache-233"><span class="linenos">233</span></a>        <span class="n">existence</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueCache-234"><a href="#ValueCache-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueCache-235"><a href="#ValueCache-235"><span class="linenos">235</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="n">existence</span>
</span><span id="ValueCache-236"><a href="#ValueCache-236"><span class="linenos">236</span></a>    
</span><span id="ValueCache-237"><a href="#ValueCache-237"><span class="linenos">237</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueCache-238"><a href="#ValueCache-238"><span class="linenos">238</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">__value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueCache-239"><a href="#ValueCache-239"><span class="linenos">239</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">existence</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueCache-240"><a href="#ValueCache-240"><span class="linenos">240</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueCache-241"><a href="#ValueCache-241"><span class="linenos">241</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">existence</span><span class="p">:</span>
</span><span id="ValueCache-242"><a href="#ValueCache-242"><span class="linenos">242</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">__value</span>
</span><span id="ValueCache-243"><a href="#ValueCache-243"><span class="linenos">243</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ValueCache-244"><a href="#ValueCache-244"><span class="linenos">244</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="ValueCache-245"><a href="#ValueCache-245"><span class="linenos">245</span></a>    
</span><span id="ValueCache-246"><a href="#ValueCache-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="nb">object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="ValueCache-247"><a href="#ValueCache-247"><span class="linenos">247</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">__value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ValueCache.__init__" class="classattr">
                                        <input id="ValueCache.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueCache</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="ValueCache.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.__init__-213"><a href="#ValueCache.__init__-213"><span class="linenos">213</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">existence</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="ValueCache.__init__-214"><a href="#ValueCache.__init__-214"><span class="linenos">214</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">ValueCache</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">existence</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueCache.get" class="classattr">
                                        <input id="ValueCache.get-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="o">~</span><span class="n">VT</span>:</span></span>

                <label class="view-source-button" for="ValueCache.get-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.get"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.get-219"><a href="#ValueCache.get-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">VT</span><span class="p">:</span>
</span><span id="ValueCache.get-220"><a href="#ValueCache.get-220"><span class="linenos">220</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueCache.set" class="classattr">
                                        <input id="ValueCache.set-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">new_value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ValueCache.set-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.set"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.set-222"><a href="#ValueCache.set-222"><span class="linenos">222</span></a>    <span class="k">def</span> <span class="nf">set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">new_value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueCache.set-223"><a href="#ValueCache.set-223"><span class="linenos">223</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="ValueCache.set-224"><a href="#ValueCache.set-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">new_value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueCache.reset" class="classattr">
                                        <input id="ValueCache.reset-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">reset</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ValueCache.reset-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueCache.reset"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueCache.reset-226"><a href="#ValueCache.reset-226"><span class="linenos">226</span></a>    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueCache.reset-227"><a href="#ValueCache.reset-227"><span class="linenos">227</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">existence</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ValueExistence">ValueExistence</a></dt>
                                <dd id="ValueCache.existence" class="variable"><a href="#ValueExistence.existence">existence</a></dd>
                <dd id="ValueCache.value" class="variable"><a href="#ValueExistence.value">value</a></dd>
                <dd id="ValueCache.to_namedtuple" class="function"><a href="#ValueExistence.to_namedtuple">to_namedtuple</a></dd>
                <dd id="ValueCache.to_tuple" class="function"><a href="#ValueExistence.to_tuple">to_tuple</a></dd>
                <dd id="ValueCache.to_dict" class="function"><a href="#ValueExistence.to_dict">to_dict</a></dd>
                <dd id="ValueCache.serialize_to_dict" class="function"><a href="#ValueExistence.serialize_to_dict">serialize_to_dict</a></dd>
                <dd id="ValueCache.from_namedtuple" class="function"><a href="#ValueExistence.from_namedtuple">from_namedtuple</a></dd>
                <dd id="ValueCache.from_tuple" class="function"><a href="#ValueExistence.from_tuple">from_tuple</a></dd>
                <dd id="ValueCache.from_dict" class="function"><a href="#ValueExistence.from_dict">from_dict</a></dd>
                <dd id="ValueCache.deserialize_from_dict" class="function"><a href="#ValueExistence.deserialize_from_dict">deserialize_from_dict</a></dd>
                <dd id="ValueCache.from_other" class="function"><a href="#ValueExistence.from_other">from_other</a></dd>

            </div>
            <div><dt>collections.abc.Sequence</dt>
                                <dd id="ValueCache.index" class="function">index</dd>
                <dd id="ValueCache.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueTypeNamedTuple">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueTypeNamedTuple</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#ValueTypeNamedTuple"></a>
    
            <div class="docstring"><p>ValueTypeNamedTuple(type_id, value)</p>
</div>


                            <div id="ValueTypeNamedTuple.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">ValueTypeNamedTuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span>, </span><span class="param"><span class="n">value</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#ValueTypeNamedTuple.__init__"></a>
    
            <div class="docstring"><p>Create new instance of ValueTypeNamedTuple(type_id, value)</p>
</div>


                            </div>
                            <div id="ValueTypeNamedTuple.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span>

        
    </div>
    <a class="headerlink" href="#ValueTypeNamedTuple.type_id"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="ValueTypeNamedTuple.value" class="classattr">
                                <div class="attr variable">
            <span class="name">value</span>

        
    </div>
    <a class="headerlink" href="#ValueTypeNamedTuple.value"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="ValueTypeNamedTuple.index" class="function">index</dd>
                <dd id="ValueTypeNamedTuple.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueType">
                            <input id="ValueType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueType</span><wbr>(<span class="base">typing.Generic[~TT, ~VT]</span>, <span class="base">collections.abc.Sequence</span>):

                <label class="view-source-button" for="ValueType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType-256"><a href="#ValueType-256"><span class="linenos">256</span></a><span class="k">class</span> <span class="nc">ValueType</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">TT</span><span class="p">,</span> <span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="ValueType-257"><a href="#ValueType-257"><span class="linenos">257</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">)</span>
</span><span id="ValueType-258"><a href="#ValueType-258"><span class="linenos">258</span></a>
</span><span id="ValueType-259"><a href="#ValueType-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueType-260"><a href="#ValueType-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueType-261"><a href="#ValueType-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueType-262"><a href="#ValueType-262"><span class="linenos">262</span></a>
</span><span id="ValueType-263"><a href="#ValueType-263"><span class="linenos">263</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueType-264"><a href="#ValueType-264"><span class="linenos">264</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="ValueType-265"><a href="#ValueType-265"><span class="linenos">265</span></a>
</span><span id="ValueType-266"><a href="#ValueType-266"><span class="linenos">266</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="ValueType-267"><a href="#ValueType-267"><span class="linenos">267</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueType-268"><a href="#ValueType-268"><span class="linenos">268</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="ValueType-269"><a href="#ValueType-269"><span class="linenos">269</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueType-270"><a href="#ValueType-270"><span class="linenos">270</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueType-271"><a href="#ValueType-271"><span class="linenos">271</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType-272"><a href="#ValueType-272"><span class="linenos">272</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="ValueType-273"><a href="#ValueType-273"><span class="linenos">273</span></a>
</span><span id="ValueType-274"><a href="#ValueType-274"><span class="linenos">274</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="ValueType-275"><a href="#ValueType-275"><span class="linenos">275</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the value&quot;</span>
</span><span id="ValueType-276"><a href="#ValueType-276"><span class="linenos">276</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="p">(</span><span class="n">ValueType</span><span class="p">,</span> <span class="n">ValueWithType</span><span class="p">)):</span>
</span><span id="ValueType-277"><a href="#ValueType-277"><span class="linenos">277</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="ValueType-278"><a href="#ValueType-278"><span class="linenos">278</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType-279"><a href="#ValueType-279"><span class="linenos">279</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="ValueType-280"><a href="#ValueType-280"><span class="linenos">280</span></a>
</span><span id="ValueType-281"><a href="#ValueType-281"><span class="linenos">281</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueType-282"><a href="#ValueType-282"><span class="linenos">282</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueType-283"><a href="#ValueType-283"><span class="linenos">283</span></a>
</span><span id="ValueType-284"><a href="#ValueType-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueType-285"><a href="#ValueType-285"><span class="linenos">285</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueType-286"><a href="#ValueType-286"><span class="linenos">286</span></a>
</span><span id="ValueType-287"><a href="#ValueType-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueType-288"><a href="#ValueType-288"><span class="linenos">288</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="ValueType-289"><a href="#ValueType-289"><span class="linenos">289</span></a>
</span><span id="ValueType-290"><a href="#ValueType-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueType-291"><a href="#ValueType-291"><span class="linenos">291</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="ValueType-292"><a href="#ValueType-292"><span class="linenos">292</span></a>    
</span><span id="ValueType-293"><a href="#ValueType-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueTypeNamedTuple</span><span class="p">:</span>
</span><span id="ValueType-294"><a href="#ValueType-294"><span class="linenos">294</span></a>        <span class="k">return</span> <span class="n">ValueTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-295"><a href="#ValueType-295"><span class="linenos">295</span></a>    
</span><span id="ValueType-296"><a href="#ValueType-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueType-297"><a href="#ValueType-297"><span class="linenos">297</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueType-298"><a href="#ValueType-298"><span class="linenos">298</span></a>    
</span><span id="ValueType-299"><a href="#ValueType-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueType-300"><a href="#ValueType-300"><span class="linenos">300</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueType-301"><a href="#ValueType-301"><span class="linenos">301</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueType-302"><a href="#ValueType-302"><span class="linenos">302</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueType-303"><a href="#ValueType-303"><span class="linenos">303</span></a>        <span class="p">}</span>
</span><span id="ValueType-304"><a href="#ValueType-304"><span class="linenos">304</span></a>    
</span><span id="ValueType-305"><a href="#ValueType-305"><span class="linenos">305</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueType-306"><a href="#ValueType-306"><span class="linenos">306</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueType-307"><a href="#ValueType-307"><span class="linenos">307</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueType-308"><a href="#ValueType-308"><span class="linenos">308</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueType-309"><a href="#ValueType-309"><span class="linenos">309</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueType-310"><a href="#ValueType-310"><span class="linenos">310</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueType-311"><a href="#ValueType-311"><span class="linenos">311</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueType-312"><a href="#ValueType-312"><span class="linenos">312</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueType-313"><a href="#ValueType-313"><span class="linenos">313</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueType-314"><a href="#ValueType-314"><span class="linenos">314</span></a>        <span class="p">}</span>
</span><span id="ValueType-315"><a href="#ValueType-315"><span class="linenos">315</span></a>    
</span><span id="ValueType-316"><a href="#ValueType-316"><span class="linenos">316</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType-317"><a href="#ValueType-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType-318"><a href="#ValueType-318"><span class="linenos">318</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-319"><a href="#ValueType-319"><span class="linenos">319</span></a>    
</span><span id="ValueType-320"><a href="#ValueType-320"><span class="linenos">320</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType-321"><a href="#ValueType-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType-322"><a href="#ValueType-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="ValueType-323"><a href="#ValueType-323"><span class="linenos">323</span></a>    
</span><span id="ValueType-324"><a href="#ValueType-324"><span class="linenos">324</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType-325"><a href="#ValueType-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType-326"><a href="#ValueType-326"><span class="linenos">326</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueType-327"><a href="#ValueType-327"><span class="linenos">327</span></a>    
</span><span id="ValueType-328"><a href="#ValueType-328"><span class="linenos">328</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType-329"><a href="#ValueType-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType-330"><a href="#ValueType-330"><span class="linenos">330</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueType-331"><a href="#ValueType-331"><span class="linenos">331</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueType-332"><a href="#ValueType-332"><span class="linenos">332</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType-333"><a href="#ValueType-333"><span class="linenos">333</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueType-334"><a href="#ValueType-334"><span class="linenos">334</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueType-335"><a href="#ValueType-335"><span class="linenos">335</span></a>    
</span><span id="ValueType-336"><a href="#ValueType-336"><span class="linenos">336</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType-337"><a href="#ValueType-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType-338"><a href="#ValueType-338"><span class="linenos">338</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueType-339"><a href="#ValueType-339"><span class="linenos">339</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-340"><a href="#ValueType-340"><span class="linenos">340</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">):</span>
</span><span id="ValueType-341"><a href="#ValueType-341"><span class="linenos">341</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-342"><a href="#ValueType-342"><span class="linenos">342</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueType-343"><a href="#ValueType-343"><span class="linenos">343</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-344"><a href="#ValueType-344"><span class="linenos">344</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueType-345"><a href="#ValueType-345"><span class="linenos">345</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-346"><a href="#ValueType-346"><span class="linenos">346</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType-347"><a href="#ValueType-347"><span class="linenos">347</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueType-348"><a href="#ValueType-348"><span class="linenos">348</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType-349"><a href="#ValueType-349"><span class="linenos">349</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueType-350"><a href="#ValueType-350"><span class="linenos">350</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ValueType.__init__" class="classattr">
                                        <input id="ValueType.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueType</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span><span class="p">:</span> <span class="o">~</span><span class="n">TT</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span></span>)</span>

                <label class="view-source-button" for="ValueType.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.__init__-259"><a href="#ValueType.__init__-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueType.__init__-260"><a href="#ValueType.__init__-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueType.__init__-261"><a href="#ValueType.__init__-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span><span class="annotation">: ~TT</span>

        
    </div>
    <a class="headerlink" href="#ValueType.type_id"></a>
    
    

                            </div>
                            <div id="ValueType.value" class="classattr">
                                <div class="attr variable">
            <span class="name">value</span><span class="annotation">: ~VT</span>

        
    </div>
    <a class="headerlink" href="#ValueType.value"></a>
    
    

                            </div>
                            <div id="ValueType.to_namedtuple" class="classattr">
                                        <input id="ValueType.to_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueTypeNamedTuple">ValueTypeNamedTuple</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.to_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.to_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.to_namedtuple-293"><a href="#ValueType.to_namedtuple-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueTypeNamedTuple</span><span class="p">:</span>
</span><span id="ValueType.to_namedtuple-294"><a href="#ValueType.to_namedtuple-294"><span class="linenos">294</span></a>        <span class="k">return</span> <span class="n">ValueTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.to_tuple" class="classattr">
                                        <input id="ValueType.to_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span>:</span></span>

                <label class="view-source-button" for="ValueType.to_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.to_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.to_tuple-296"><a href="#ValueType.to_tuple-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueType.to_tuple-297"><a href="#ValueType.to_tuple-297"><span class="linenos">297</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.to_dict" class="classattr">
                                        <input id="ValueType.to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">dict</span>:</span></span>

                <label class="view-source-button" for="ValueType.to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.to_dict-299"><a href="#ValueType.to_dict-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueType.to_dict-300"><a href="#ValueType.to_dict-300"><span class="linenos">300</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueType.to_dict-301"><a href="#ValueType.to_dict-301"><span class="linenos">301</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueType.to_dict-302"><a href="#ValueType.to_dict-302"><span class="linenos">302</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueType.to_dict-303"><a href="#ValueType.to_dict-303"><span class="linenos">303</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.serialize_to_dict" class="classattr">
                                        <input id="ValueType.serialize_to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serialize_to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ValueType.serialize_to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.serialize_to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.serialize_to_dict-305"><a href="#ValueType.serialize_to_dict-305"><span class="linenos">305</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueType.serialize_to_dict-306"><a href="#ValueType.serialize_to_dict-306"><span class="linenos">306</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueType.serialize_to_dict-307"><a href="#ValueType.serialize_to_dict-307"><span class="linenos">307</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueType.serialize_to_dict-308"><a href="#ValueType.serialize_to_dict-308"><span class="linenos">308</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueType.serialize_to_dict-309"><a href="#ValueType.serialize_to_dict-309"><span class="linenos">309</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueType.serialize_to_dict-310"><a href="#ValueType.serialize_to_dict-310"><span class="linenos">310</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueType.serialize_to_dict-311"><a href="#ValueType.serialize_to_dict-311"><span class="linenos">311</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueType.serialize_to_dict-312"><a href="#ValueType.serialize_to_dict-312"><span class="linenos">312</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueType.serialize_to_dict-313"><a href="#ValueType.serialize_to_dict-313"><span class="linenos">313</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueType.serialize_to_dict-314"><a href="#ValueType.serialize_to_dict-314"><span class="linenos">314</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.from_namedtuple" class="classattr">
                                        <input id="ValueType.from_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">named_tuple</span><span class="p">:</span> <span class="n"><a href="#ValueTypeNamedTuple">ValueTypeNamedTuple</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.from_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.from_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.from_namedtuple-316"><a href="#ValueType.from_namedtuple-316"><span class="linenos">316</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType.from_namedtuple-317"><a href="#ValueType.from_namedtuple-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType.from_namedtuple-318"><a href="#ValueType.from_namedtuple-318"><span class="linenos">318</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.from_tuple" class="classattr">
                                        <input id="ValueType.from_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_tuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.from_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.from_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.from_tuple-320"><a href="#ValueType.from_tuple-320"><span class="linenos">320</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType.from_tuple-321"><a href="#ValueType.from_tuple-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType.from_tuple-322"><a href="#ValueType.from_tuple-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.from_dict" class="classattr">
                                        <input id="ValueType.from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.from_dict-324"><a href="#ValueType.from_dict-324"><span class="linenos">324</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType.from_dict-325"><a href="#ValueType.from_dict-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType.from_dict-326"><a href="#ValueType.from_dict-326"><span class="linenos">326</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.deserialize_from_dict" class="classattr">
                                        <input id="ValueType.deserialize_from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">deserialize_from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span>,</span><span class="param">	<span class="n">owning_info</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.deserialize_from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.deserialize_from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.deserialize_from_dict-328"><a href="#ValueType.deserialize_from_dict-328"><span class="linenos">328</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType.deserialize_from_dict-329"><a href="#ValueType.deserialize_from_dict-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType.deserialize_from_dict-330"><a href="#ValueType.deserialize_from_dict-330"><span class="linenos">330</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueType.deserialize_from_dict-331"><a href="#ValueType.deserialize_from_dict-331"><span class="linenos">331</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueType.deserialize_from_dict-332"><a href="#ValueType.deserialize_from_dict-332"><span class="linenos">332</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType.deserialize_from_dict-333"><a href="#ValueType.deserialize_from_dict-333"><span class="linenos">333</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueType.deserialize_from_dict-334"><a href="#ValueType.deserialize_from_dict-334"><span class="linenos">334</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueType.from_other" class="classattr">
                                        <input id="ValueType.from_other-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_other</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#ValueExistence">ValueExistence</a></span><span class="p">,</span> <span class="n"><a href="#ValueTypeNamedTuple">ValueTypeNamedTuple</a></span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="o">~</span><span class="n">VT</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueType.from_other-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueType.from_other"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueType.from_other-336"><a href="#ValueType.from_other-336"><span class="linenos">336</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueType.from_other-337"><a href="#ValueType.from_other-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueType.from_other-338"><a href="#ValueType.from_other-338"><span class="linenos">338</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueType.from_other-339"><a href="#ValueType.from_other-339"><span class="linenos">339</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType.from_other-340"><a href="#ValueType.from_other-340"><span class="linenos">340</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueTypeNamedTuple</span><span class="p">):</span>
</span><span id="ValueType.from_other-341"><a href="#ValueType.from_other-341"><span class="linenos">341</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType.from_other-342"><a href="#ValueType.from_other-342"><span class="linenos">342</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueType.from_other-343"><a href="#ValueType.from_other-343"><span class="linenos">343</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType.from_other-344"><a href="#ValueType.from_other-344"><span class="linenos">344</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueType.from_other-345"><a href="#ValueType.from_other-345"><span class="linenos">345</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType.from_other-346"><a href="#ValueType.from_other-346"><span class="linenos">346</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueType.from_other-347"><a href="#ValueType.from_other-347"><span class="linenos">347</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueType.from_other-348"><a href="#ValueType.from_other-348"><span class="linenos">348</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueType.from_other-349"><a href="#ValueType.from_other-349"><span class="linenos">349</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueType.from_other-350"><a href="#ValueType.from_other-350"><span class="linenos">350</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>collections.abc.Sequence</dt>
                                <dd id="ValueType.index" class="function">index</dd>
                <dd id="ValueType.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueWithTypeNamedTuple">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueWithTypeNamedTuple</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#ValueWithTypeNamedTuple"></a>
    
            <div class="docstring"><p>ValueWithTypeNamedTuple(type_id, value)</p>
</div>


                            <div id="ValueWithTypeNamedTuple.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">ValueWithTypeNamedTuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span>, </span><span class="param"><span class="n">value</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#ValueWithTypeNamedTuple.__init__"></a>
    
            <div class="docstring"><p>Create new instance of ValueWithTypeNamedTuple(type_id, value)</p>
</div>


                            </div>
                            <div id="ValueWithTypeNamedTuple.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span>

        
    </div>
    <a class="headerlink" href="#ValueWithTypeNamedTuple.type_id"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="ValueWithTypeNamedTuple.value" class="classattr">
                                <div class="attr variable">
            <span class="name">value</span>

        
    </div>
    <a class="headerlink" href="#ValueWithTypeNamedTuple.value"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="ValueWithTypeNamedTuple.index" class="function">index</dd>
                <dd id="ValueWithTypeNamedTuple.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ValueWithType">
                            <input id="ValueWithType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ValueWithType</span><wbr>(<span class="base">typing.Generic[~TT, ~VT]</span>, <span class="base">collections.abc.Sequence</span>):

                <label class="view-source-button" for="ValueWithType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType-356"><a href="#ValueWithType-356"><span class="linenos">356</span></a><span class="k">class</span> <span class="nc">ValueWithType</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">TT</span><span class="p">,</span> <span class="n">VT</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">):</span>
</span><span id="ValueWithType-357"><a href="#ValueWithType-357"><span class="linenos">357</span></a>    <span class="vm">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="s1">&#39;type_id&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">)</span>
</span><span id="ValueWithType-358"><a href="#ValueWithType-358"><span class="linenos">358</span></a>
</span><span id="ValueWithType-359"><a href="#ValueWithType-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueWithType-360"><a href="#ValueWithType-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueWithType-361"><a href="#ValueWithType-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="ValueWithType-362"><a href="#ValueWithType-362"><span class="linenos">362</span></a>
</span><span id="ValueWithType-363"><a href="#ValueWithType-363"><span class="linenos">363</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueWithType-364"><a href="#ValueWithType-364"><span class="linenos">364</span></a>        <span class="k">return</span> <span class="mi">2</span>
</span><span id="ValueWithType-365"><a href="#ValueWithType-365"><span class="linenos">365</span></a>
</span><span id="ValueWithType-366"><a href="#ValueWithType-366"><span class="linenos">366</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
</span><span id="ValueWithType-367"><a href="#ValueWithType-367"><span class="linenos">367</span></a>        <span class="k">if</span> <span class="mi">0</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueWithType-368"><a href="#ValueWithType-368"><span class="linenos">368</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="ValueWithType-369"><a href="#ValueWithType-369"><span class="linenos">369</span></a>        <span class="k">elif</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">index</span><span class="p">:</span>
</span><span id="ValueWithType-370"><a href="#ValueWithType-370"><span class="linenos">370</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueWithType-371"><a href="#ValueWithType-371"><span class="linenos">371</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType-372"><a href="#ValueWithType-372"><span class="linenos">372</span></a>            <span class="k">raise</span> <span class="ne">IndexError</span>
</span><span id="ValueWithType-373"><a href="#ValueWithType-373"><span class="linenos">373</span></a>
</span><span id="ValueWithType-374"><a href="#ValueWithType-374"><span class="linenos">374</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
</span><span id="ValueWithType-375"><a href="#ValueWithType-375"><span class="linenos">375</span></a>        <span class="c1"># &quot;__ne__() delegates to __eq__() and inverts the value&quot;</span>
</span><span id="ValueWithType-376"><a href="#ValueWithType-376"><span class="linenos">376</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueType</span><span class="p">):</span>
</span><span id="ValueWithType-377"><a href="#ValueWithType-377"><span class="linenos">377</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span>
</span><span id="ValueWithType-378"><a href="#ValueWithType-378"><span class="linenos">378</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">ValueWithType</span><span class="p">):</span>
</span><span id="ValueWithType-379"><a href="#ValueWithType-379"><span class="linenos">379</span></a>            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-380"><a href="#ValueWithType-380"><span class="linenos">380</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType-381"><a href="#ValueWithType-381"><span class="linenos">381</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="n">other</span>
</span><span id="ValueWithType-382"><a href="#ValueWithType-382"><span class="linenos">382</span></a>
</span><span id="ValueWithType-383"><a href="#ValueWithType-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">__getstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueWithType-384"><a href="#ValueWithType-384"><span class="linenos">384</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueWithType-385"><a href="#ValueWithType-385"><span class="linenos">385</span></a>
</span><span id="ValueWithType-386"><a href="#ValueWithType-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">__setstate__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
</span><span id="ValueWithType-387"><a href="#ValueWithType-387"><span class="linenos">387</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">state</span>
</span><span id="ValueWithType-388"><a href="#ValueWithType-388"><span class="linenos">388</span></a>
</span><span id="ValueWithType-389"><a href="#ValueWithType-389"><span class="linenos">389</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueWithType-390"><a href="#ValueWithType-390"><span class="linenos">390</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">)</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="ValueWithType-391"><a href="#ValueWithType-391"><span class="linenos">391</span></a>
</span><span id="ValueWithType-392"><a href="#ValueWithType-392"><span class="linenos">392</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ValueWithType-393"><a href="#ValueWithType-393"><span class="linenos">393</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__str__</span><span class="p">()</span>
</span><span id="ValueWithType-394"><a href="#ValueWithType-394"><span class="linenos">394</span></a>    
</span><span id="ValueWithType-395"><a href="#ValueWithType-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">:</span>
</span><span id="ValueWithType-396"><a href="#ValueWithType-396"><span class="linenos">396</span></a>        <span class="k">return</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-397"><a href="#ValueWithType-397"><span class="linenos">397</span></a>    
</span><span id="ValueWithType-398"><a href="#ValueWithType-398"><span class="linenos">398</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueWithType-399"><a href="#ValueWithType-399"><span class="linenos">399</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span><span id="ValueWithType-400"><a href="#ValueWithType-400"><span class="linenos">400</span></a>    
</span><span id="ValueWithType-401"><a href="#ValueWithType-401"><span class="linenos">401</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueWithType-402"><a href="#ValueWithType-402"><span class="linenos">402</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueWithType-403"><a href="#ValueWithType-403"><span class="linenos">403</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueWithType-404"><a href="#ValueWithType-404"><span class="linenos">404</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueWithType-405"><a href="#ValueWithType-405"><span class="linenos">405</span></a>        <span class="p">}</span>
</span><span id="ValueWithType-406"><a href="#ValueWithType-406"><span class="linenos">406</span></a>    
</span><span id="ValueWithType-407"><a href="#ValueWithType-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueWithType-408"><a href="#ValueWithType-408"><span class="linenos">408</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueWithType-409"><a href="#ValueWithType-409"><span class="linenos">409</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueWithType-410"><a href="#ValueWithType-410"><span class="linenos">410</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueWithType-411"><a href="#ValueWithType-411"><span class="linenos">411</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueWithType-412"><a href="#ValueWithType-412"><span class="linenos">412</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueWithType-413"><a href="#ValueWithType-413"><span class="linenos">413</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueWithType-414"><a href="#ValueWithType-414"><span class="linenos">414</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueWithType-415"><a href="#ValueWithType-415"><span class="linenos">415</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueWithType-416"><a href="#ValueWithType-416"><span class="linenos">416</span></a>        <span class="p">}</span>
</span><span id="ValueWithType-417"><a href="#ValueWithType-417"><span class="linenos">417</span></a>    
</span><span id="ValueWithType-418"><a href="#ValueWithType-418"><span class="linenos">418</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType-419"><a href="#ValueWithType-419"><span class="linenos">419</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType-420"><a href="#ValueWithType-420"><span class="linenos">420</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-421"><a href="#ValueWithType-421"><span class="linenos">421</span></a>    
</span><span id="ValueWithType-422"><a href="#ValueWithType-422"><span class="linenos">422</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType-423"><a href="#ValueWithType-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType-424"><a href="#ValueWithType-424"><span class="linenos">424</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span><span id="ValueWithType-425"><a href="#ValueWithType-425"><span class="linenos">425</span></a>    
</span><span id="ValueWithType-426"><a href="#ValueWithType-426"><span class="linenos">426</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType-427"><a href="#ValueWithType-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType-428"><a href="#ValueWithType-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueWithType-429"><a href="#ValueWithType-429"><span class="linenos">429</span></a>    
</span><span id="ValueWithType-430"><a href="#ValueWithType-430"><span class="linenos">430</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType-431"><a href="#ValueWithType-431"><span class="linenos">431</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType-432"><a href="#ValueWithType-432"><span class="linenos">432</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueWithType-433"><a href="#ValueWithType-433"><span class="linenos">433</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueWithType-434"><a href="#ValueWithType-434"><span class="linenos">434</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType-435"><a href="#ValueWithType-435"><span class="linenos">435</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueWithType-436"><a href="#ValueWithType-436"><span class="linenos">436</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueWithType-437"><a href="#ValueWithType-437"><span class="linenos">437</span></a>    
</span><span id="ValueWithType-438"><a href="#ValueWithType-438"><span class="linenos">438</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType-439"><a href="#ValueWithType-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType-440"><a href="#ValueWithType-440"><span class="linenos">440</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueWithType-441"><a href="#ValueWithType-441"><span class="linenos">441</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-442"><a href="#ValueWithType-442"><span class="linenos">442</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">):</span>
</span><span id="ValueWithType-443"><a href="#ValueWithType-443"><span class="linenos">443</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-444"><a href="#ValueWithType-444"><span class="linenos">444</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueWithType-445"><a href="#ValueWithType-445"><span class="linenos">445</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-446"><a href="#ValueWithType-446"><span class="linenos">446</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueWithType-447"><a href="#ValueWithType-447"><span class="linenos">447</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-448"><a href="#ValueWithType-448"><span class="linenos">448</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType-449"><a href="#ValueWithType-449"><span class="linenos">449</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueWithType-450"><a href="#ValueWithType-450"><span class="linenos">450</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType-451"><a href="#ValueWithType-451"><span class="linenos">451</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueWithType-452"><a href="#ValueWithType-452"><span class="linenos">452</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Abstract base class for generic types.</p>

<p>A generic type is typically declared by inheriting from
this class parameterized with one or more type variables.
For example, a generic mapping type might be defined as::</p>

<p>class Mapping(Generic[KT, VT]):
      def __getitem__(self, key: KT) -> VT:
          ...
      # Etc.</p>

<p>This class can then be used as follows::</p>

<p>def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
      try:
          return mapping[key]
      except KeyError:
          return default</p>
</div>


                            <div id="ValueWithType.__init__" class="classattr">
                                        <input id="ValueWithType.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ValueWithType</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span><span class="p">:</span> <span class="o">~</span><span class="n">TT</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="o">~</span><span class="n">VT</span></span>)</span>

                <label class="view-source-button" for="ValueWithType.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.__init__-359"><a href="#ValueWithType.__init__-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">VT</span><span class="p">):</span>
</span><span id="ValueWithType.__init__-360"><a href="#ValueWithType.__init__-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">:</span> <span class="n">TT</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="ValueWithType.__init__-361"><a href="#ValueWithType.__init__-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">:</span> <span class="n">VT</span> <span class="o">=</span> <span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span><span class="annotation">: ~TT</span>

        
    </div>
    <a class="headerlink" href="#ValueWithType.type_id"></a>
    
    

                            </div>
                            <div id="ValueWithType.value" class="classattr">
                                <div class="attr variable">
            <span class="name">value</span><span class="annotation">: ~VT</span>

        
    </div>
    <a class="headerlink" href="#ValueWithType.value"></a>
    
    

                            </div>
                            <div id="ValueWithType.to_namedtuple" class="classattr">
                                        <input id="ValueWithType.to_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueWithTypeNamedTuple">ValueWithTypeNamedTuple</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.to_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.to_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.to_namedtuple-395"><a href="#ValueWithType.to_namedtuple-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="nf">to_namedtuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">:</span>
</span><span id="ValueWithType.to_namedtuple-396"><a href="#ValueWithType.to_namedtuple-396"><span class="linenos">396</span></a>        <span class="k">return</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.to_tuple" class="classattr">
                                        <input id="ValueWithType.to_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span>:</span></span>

                <label class="view-source-button" for="ValueWithType.to_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.to_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.to_tuple-398"><a href="#ValueWithType.to_tuple-398"><span class="linenos">398</span></a>    <span class="k">def</span> <span class="nf">to_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="ValueWithType.to_tuple-399"><a href="#ValueWithType.to_tuple-399"><span class="linenos">399</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.to_dict" class="classattr">
                                        <input id="ValueWithType.to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">dict</span>:</span></span>

                <label class="view-source-button" for="ValueWithType.to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.to_dict-401"><a href="#ValueWithType.to_dict-401"><span class="linenos">401</span></a>    <span class="k">def</span> <span class="nf">to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">:</span>
</span><span id="ValueWithType.to_dict-402"><a href="#ValueWithType.to_dict-402"><span class="linenos">402</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueWithType.to_dict-403"><a href="#ValueWithType.to_dict-403"><span class="linenos">403</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueWithType.to_dict-404"><a href="#ValueWithType.to_dict-404"><span class="linenos">404</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueWithType.to_dict-405"><a href="#ValueWithType.to_dict-405"><span class="linenos">405</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.serialize_to_dict" class="classattr">
                                        <input id="ValueWithType.serialize_to_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">serialize_to_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ValueWithType.serialize_to_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.serialize_to_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.serialize_to_dict-407"><a href="#ValueWithType.serialize_to_dict-407"><span class="linenos">407</span></a>    <span class="k">def</span> <span class="nf">serialize_to_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">dict</span><span class="p">,</span> <span class="nb">dict</span><span class="p">]:</span>
</span><span id="ValueWithType.serialize_to_dict-408"><a href="#ValueWithType.serialize_to_dict-408"><span class="linenos">408</span></a>        <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span> <span class="o">=</span> <span class="n">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">)</span>
</span><span id="ValueWithType.serialize_to_dict-409"><a href="#ValueWithType.serialize_to_dict-409"><span class="linenos">409</span></a>        <span class="k">return</span> <span class="p">{</span>
</span><span id="ValueWithType.serialize_to_dict-410"><a href="#ValueWithType.serialize_to_dict-410"><span class="linenos">410</span></a>            <span class="s1">&#39;type_id&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span>
</span><span id="ValueWithType.serialize_to_dict-411"><a href="#ValueWithType.serialize_to_dict-411"><span class="linenos">411</span></a>            <span class="s1">&#39;value&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">,</span>
</span><span id="ValueWithType.serialize_to_dict-412"><a href="#ValueWithType.serialize_to_dict-412"><span class="linenos">412</span></a>        <span class="p">},</span> <span class="p">{</span>
</span><span id="ValueWithType.serialize_to_dict-413"><a href="#ValueWithType.serialize_to_dict-413"><span class="linenos">413</span></a>            <span class="s1">&#39;class_name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="p">,</span>
</span><span id="ValueWithType.serialize_to_dict-414"><a href="#ValueWithType.serialize_to_dict-414"><span class="linenos">414</span></a>            <span class="s1">&#39;module_importable_str&#39;</span><span class="p">:</span> <span class="n">module_importable_str</span><span class="p">,</span>
</span><span id="ValueWithType.serialize_to_dict-415"><a href="#ValueWithType.serialize_to_dict-415"><span class="linenos">415</span></a>            <span class="s1">&#39;owning_names_path&#39;</span><span class="p">:</span> <span class="n">owning_names_path</span><span class="p">,</span>
</span><span id="ValueWithType.serialize_to_dict-416"><a href="#ValueWithType.serialize_to_dict-416"><span class="linenos">416</span></a>        <span class="p">}</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.from_namedtuple" class="classattr">
                                        <input id="ValueWithType.from_namedtuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_namedtuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">named_tuple</span><span class="p">:</span> <span class="n"><a href="#ValueWithTypeNamedTuple">ValueWithTypeNamedTuple</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.from_namedtuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.from_namedtuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.from_namedtuple-418"><a href="#ValueWithType.from_namedtuple-418"><span class="linenos">418</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType.from_namedtuple-419"><a href="#ValueWithType.from_namedtuple-419"><span class="linenos">419</span></a>    <span class="k">def</span> <span class="nf">from_namedtuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">named_tuple</span><span class="p">:</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType.from_namedtuple-420"><a href="#ValueWithType.from_namedtuple-420"><span class="linenos">420</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">named_tuple</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">named_tuple</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.from_tuple" class="classattr">
                                        <input id="ValueWithType.from_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_tuple</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.from_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.from_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.from_tuple-422"><a href="#ValueWithType.from_tuple-422"><span class="linenos">422</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType.from_tuple-423"><a href="#ValueWithType.from_tuple-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="nf">from_tuple</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">tuple_</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType.from_tuple-424"><a href="#ValueWithType.from_tuple-424"><span class="linenos">424</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="o">*</span><span class="n">tuple_</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.from_dict" class="classattr">
                                        <input id="ValueWithType.from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.from_dict-426"><a href="#ValueWithType.from_dict-426"><span class="linenos">426</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType.from_dict-427"><a href="#ValueWithType.from_dict-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="nf">from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType.from_dict-428"><a href="#ValueWithType.from_dict-428"><span class="linenos">428</span></a>        <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.deserialize_from_dict" class="classattr">
                                        <input id="ValueWithType.deserialize_from_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">deserialize_from_dict</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span>,</span><span class="param">	<span class="n">owning_info</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.deserialize_from_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.deserialize_from_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.deserialize_from_dict-430"><a href="#ValueWithType.deserialize_from_dict-430"><span class="linenos">430</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType.deserialize_from_dict-431"><a href="#ValueWithType.deserialize_from_dict-431"><span class="linenos">431</span></a>    <span class="k">def</span> <span class="nf">deserialize_from_dict</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">dict_</span><span class="p">:</span> <span class="nb">dict</span><span class="p">,</span> <span class="n">owning_info</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType.deserialize_from_dict-432"><a href="#ValueWithType.deserialize_from_dict-432"><span class="linenos">432</span></a>        <span class="k">if</span> <span class="n">owning_info</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ValueWithType.deserialize_from_dict-433"><a href="#ValueWithType.deserialize_from_dict-433"><span class="linenos">433</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span><span id="ValueWithType.deserialize_from_dict-434"><a href="#ValueWithType.deserialize_from_dict-434"><span class="linenos">434</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType.deserialize_from_dict-435"><a href="#ValueWithType.deserialize_from_dict-435"><span class="linenos">435</span></a>            <span class="n">class_type</span> <span class="o">=</span> <span class="n">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;class_name&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;module_importable_str&#39;</span><span class="p">],</span> <span class="n">owning_info</span><span class="p">[</span><span class="s1">&#39;owning_names_path&#39;</span><span class="p">])</span>
</span><span id="ValueWithType.deserialize_from_dict-436"><a href="#ValueWithType.deserialize_from_dict-436"><span class="linenos">436</span></a>            <span class="k">return</span> <span class="n">class_type</span><span class="p">(</span><span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;type_id&#39;</span><span class="p">],</span> <span class="n">dict_</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="ValueWithType.from_other" class="classattr">
                                        <input id="ValueWithType.from_other-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_other</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#ValueExistence">ValueExistence</a></span><span class="p">,</span> <span class="n"><a href="#ValueWithTypeNamedTuple">ValueWithTypeNamedTuple</a></span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="o">~</span><span class="n">VT</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n"><a href="#ValueExistence">ValueExistence</a></span>:</span></span>

                <label class="view-source-button" for="ValueWithType.from_other-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ValueWithType.from_other"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ValueWithType.from_other-438"><a href="#ValueWithType.from_other-438"><span class="linenos">438</span></a>    <span class="nd">@classmethod</span>
</span><span id="ValueWithType.from_other-439"><a href="#ValueWithType.from_other-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="nf">from_other</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="s1">&#39;ValueExistence&#39;</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">VT</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;ValueExistence&#39;</span><span class="p">:</span>
</span><span id="ValueWithType.from_other-440"><a href="#ValueWithType.from_other-440"><span class="linenos">440</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueExistence</span><span class="p">):</span>
</span><span id="ValueWithType.from_other-441"><a href="#ValueWithType.from_other-441"><span class="linenos">441</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType.from_other-442"><a href="#ValueWithType.from_other-442"><span class="linenos">442</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">ValueWithTypeNamedTuple</span><span class="p">):</span>
</span><span id="ValueWithType.from_other-443"><a href="#ValueWithType.from_other-443"><span class="linenos">443</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_namedtuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType.from_other-444"><a href="#ValueWithType.from_other-444"><span class="linenos">444</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="ValueWithType.from_other-445"><a href="#ValueWithType.from_other-445"><span class="linenos">445</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_tuple</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType.from_other-446"><a href="#ValueWithType.from_other-446"><span class="linenos">446</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
</span><span id="ValueWithType.from_other-447"><a href="#ValueWithType.from_other-447"><span class="linenos">447</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="o">.</span><span class="n">from_dict</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType.from_other-448"><a href="#ValueWithType.from_other-448"><span class="linenos">448</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="ValueWithType.from_other-449"><a href="#ValueWithType.from_other-449"><span class="linenos">449</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="ValueWithType.from_other-450"><a href="#ValueWithType.from_other-450"><span class="linenos">450</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">type_id</span><span class="p">,</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="ValueWithType.from_other-451"><a href="#ValueWithType.from_other-451"><span class="linenos">451</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ValueWithType.from_other-452"><a href="#ValueWithType.from_other-452"><span class="linenos">452</span></a>                <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>collections.abc.Sequence</dt>
                                <dd id="ValueWithType.index" class="function">index</dd>
                <dd id="ValueWithType.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>