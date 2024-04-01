---
title: point
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.math<wbr>.geometry<wbr>.point<wbr>.versions<wbr>.v_0<wbr>.point    </h1>

                
                        <input id="mod-point-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-point-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;PointBase&#39;</span><span class="p">,</span> <span class="s1">&#39;PointDimensionIndexError&#39;</span><span class="p">,</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">,</span> <span class="s1">&#39;Point1d&#39;</span><span class="p">,</span> <span class="s1">&#39;Point2d&#39;</span><span class="p">,</span> <span class="s1">&#39;Point3d&#39;</span><span class="p">,</span> <span class="s1">&#39;PointNdXYZ&#39;</span><span class="p">,</span> <span class="s1">&#39;convert_point_to_xyz&#39;</span><span class="p">]</span>
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
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">copy</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.entities.copyable</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Union</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">numpy_present</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>    <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>    <span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="n">array_equal</span><span class="p">,</span> <span class="n">array</span><span class="p">,</span> <span class="n">ndarray</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">except</span><span class="p">:</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="n">numpy_present</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">RawListPointType</span> <span class="o">=</span> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="n">RawNdarrayPointType</span> <span class="o">=</span> <span class="n">ndarray</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="n">RawUniversalPointType</span> <span class="o">=</span> <span class="n">Union</span><span class="p">[</span><span class="n">RawListPointType</span><span class="p">,</span> <span class="n">RawNdarrayPointType</span><span class="p">]</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="k">else</span><span class="p">:</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="n">RawUniversalPointType</span> <span class="o">=</span> <span class="n">RawListPointType</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="k">class</span> <span class="nc">PointBase</span><span class="p">(</span><span class="n">CopyableMixin</span><span class="p">):</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="nd">@property</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    <span class="k">def</span> <span class="nf">dim</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawListPointType</span><span class="p">:</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="k">class</span> <span class="nc">PointDimensionIndexError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">pass</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="k">class</span> <span class="nc">PointWrongNdarrayTypeError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">pass</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="k">class</span> <span class="nc">PointNd</span><span class="p">(</span><span class="n">PointBase</span><span class="p">):</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="n">_default_ndarray_type</span> <span class="o">=</span> <span class="nb">float</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="n">_default_shallow_copy</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        <span class="n">shallow_copy</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_shallow_copy</span><span class="p">)</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">if</span> <span class="n">shallow_copy</span> <span class="ow">and</span> <span class="n">args</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>            <span class="n">first_element</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_point</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>            <span class="k">if</span> <span class="n">dimension</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dimension</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">:</span> <span class="n">RawListPointType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_ndarray_type</span><span class="p">)</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">}:</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong type: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>                <span class="k">raise</span> <span class="n">PointWrongNdarrayTypeError</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="bp">self</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(dimension=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="si">}</span><span class="s1">, point=(</span><span class="si">{</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">)</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">item</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">))</span><span class="si">}</span><span class="s1">), ndarray_type=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>    
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_dict_key_with_callable_default</span><span class="p">(</span><span class="n">update</span><span class="p">,</span> <span class="s1">&#39;_point&#39;</span><span class="p">,</span> <span class="k">lambda</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">())</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="p">()]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawUniversalPointType</span><span class="p">:</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">first_element</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_element</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_element</span><span class="p">,</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">first_element</span><span class="p">()</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_element</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">)):</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>                    <span class="k">break</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">elif</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>                <span class="k">for</span> <span class="n">dim_name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>                    <span class="k">if</span> <span class="n">dim_name</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>                        <span class="n">kwargs</span><span class="p">[</span><span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">dim_index</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">dim_name</span><span class="p">]</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>                        <span class="k">break</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>            <span class="k">for</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="p">):</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>                <span class="n">dim_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">dim_index</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                <span class="n">dim_value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">dim_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>                <span class="k">if</span> <span class="n">dim_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">dim_value</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">as_list</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawListPointType</span><span class="p">:</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="k">def</span> <span class="fm">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="k">if</span> <span class="n">__name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">__value</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>                <span class="k">return</span> <span class="n">__value</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="k">if</span> <span class="n">__name</span> <span class="ow">and</span> <span class="n">__name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="n">index_str</span> <span class="o">=</span> <span class="n">__name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>            <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">__value</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>                    <span class="k">return</span> <span class="n">__value</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>                    <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__setattr__</span><span class="p">(</span><span class="n">__name</span><span class="p">,</span> <span class="n">__value</span><span class="p">)</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="fm">__getattribute__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_dim_names_translation_table&#39;</span><span class="p">):</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="k">if</span> <span class="n">__name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>                <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_point&#39;</span><span class="p">)[</span><span class="n">dim_index</span><span class="p">]</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="k">if</span> <span class="n">__name</span> <span class="ow">and</span> <span class="n">__name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="n">index_str</span> <span class="o">=</span> <span class="n">__name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;dim&#39;</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                    <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_point&#39;</span><span class="p">)[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>                    <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="n">__name</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_or_key</span><span class="p">):</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index_or_key</span><span class="p">]</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>            <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>                <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>                <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                    <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                        <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="fm">__setitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_or_key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index_or_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>                <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>                <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>                <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>                    <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>                        <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">crop_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a><span class="sd">        &gt;&gt; p4 = Point3d(3, 5, 2, 8)</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p4.crop_to(&#39;z&#39;, &#39;n0&#39;, 3))</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a><span class="sd">        Point3d(2, 3, 8)</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a><span class="sd">        Raises:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">            PointDimensionIndexError: _description_</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a><span class="sd">            KeyError: _description_</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a><span class="sd">        Returns:</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>            
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                    <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                        <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>                            <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dim_index</span><span class="p">)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>            
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            <span class="n">croped_data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">index_sequence</span><span class="p">:</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>                <span class="n">croped_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>            
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">croped_data</span><span class="p">),</span> <span class="n">croped_data</span><span class="p">)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">expand_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a><span class="sd">        &gt;&gt; p2 = Point2d(2, 3)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p2.expand_to(3, 2, &#39;n0&#39;))</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="sd">        Point3d(3, 0, 2)</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="sd">        Args:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="sd">            dimension (int): _description_</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a><span class="sd">            *args (Union[Tuple[int], Tuple[str]]): list used to map `point item` with index equal to `list&#39;s item index` to `result point item` with index equals to `list&#39;s item value`. If value is str: it should starts from &#39;n&#39; char and continue with (positive) numeric chars only</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a><span class="sd">        Raises:</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a><span class="sd">            PointDimensionIndexError: when `len(args) &gt; len(self)`</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a><span class="sd">            KeyError: wrong type of *args or type/format of it&#39;s value(s)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a><span class="sd">        Returns:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>            
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="n">dimension</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>                            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>                        <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>            <span class="n">expansion_data</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>            <span class="k">for</span> <span class="n">source_index</span><span class="p">,</span> <span class="n">destination_index</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">index_sequence</span><span class="p">):</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>                <span class="n">expansion_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">destination_index</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">source_index</span><span class="p">]</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">**</span><span class="n">expansion_data</span><span class="p">)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>    
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>            <span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">dim</span><span class="p">)</span> <span class="ow">and</span> <span class="n">array_equal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">dim</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>    
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">other</span><span class="p">)</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>    <span class="k">def</span> <span class="fm">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="k">return</span> <span class="nb">hash</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)))</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;If not zero point</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a><span class="sd">        Returns:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a><span class="sd">            bool: _description_</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">:</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>            <span class="k">if</span> <span class="n">item</span><span class="p">:</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="k">class</span> <span class="nc">Point1d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>    <span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a><span class="k">class</span> <span class="nc">Point2d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>    <span class="p">)</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a><span class="k">class</span> <span class="nc">Point3d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="p">({</span><span class="s1">&#39;z&#39;</span><span class="p">,</span> <span class="s1">&#39;Z&#39;</span><span class="p">},</span> <span class="mi">2</span><span class="p">),</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>    <span class="p">)</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a><span class="k">class</span> <span class="nc">PointNdXYZ</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="p">({</span><span class="s1">&#39;z&#39;</span><span class="p">,</span> <span class="s1">&#39;Z&#39;</span><span class="p">},</span> <span class="mi">2</span><span class="p">),</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>    <span class="p">)</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a><span class="k">def</span> <span class="nf">convert_point_to_xyz</span><span class="p">(</span><span class="n">point</span><span class="p">:</span> <span class="n">PointNd</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PointNd</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>    <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="k">return</span> <span class="n">Point1d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>    <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="k">return</span> <span class="n">Point2d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>    <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="n">Point3d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>    <span class="k">elif</span> <span class="mi">3</span> <span class="o">&lt;</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="k">return</span> <span class="n">PointNdXYZ</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="PointBase">
                            <input id="PointBase-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PointBase</span><wbr>(<span class="base">cengal.entities.copyable.versions.v_0.copyable.CopyableMixin</span>):

                <label class="view-source-button" for="PointBase-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase-56"><a href="#PointBase-56"><span class="linenos">56</span></a><span class="k">class</span> <span class="nc">PointBase</span><span class="p">(</span><span class="n">CopyableMixin</span><span class="p">):</span>
</span><span id="PointBase-57"><a href="#PointBase-57"><span class="linenos">57</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="PointBase-58"><a href="#PointBase-58"><span class="linenos">58</span></a>
</span><span id="PointBase-59"><a href="#PointBase-59"><span class="linenos">59</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase-60"><a href="#PointBase-60"><span class="linenos">60</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="PointBase-61"><a href="#PointBase-61"><span class="linenos">61</span></a>
</span><span id="PointBase-62"><a href="#PointBase-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase-63"><a href="#PointBase-63"><span class="linenos">63</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="PointBase-64"><a href="#PointBase-64"><span class="linenos">64</span></a>    
</span><span id="PointBase-65"><a href="#PointBase-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase-66"><a href="#PointBase-66"><span class="linenos">66</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="PointBase-67"><a href="#PointBase-67"><span class="linenos">67</span></a>
</span><span id="PointBase-68"><a href="#PointBase-68"><span class="linenos">68</span></a>    <span class="nd">@property</span>
</span><span id="PointBase-69"><a href="#PointBase-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">dim</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="PointBase-70"><a href="#PointBase-70"><span class="linenos">70</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointBase-71"><a href="#PointBase-71"><span class="linenos">71</span></a>
</span><span id="PointBase-72"><a href="#PointBase-72"><span class="linenos">72</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawListPointType</span><span class="p">:</span>
</span><span id="PointBase-73"><a href="#PointBase-73"><span class="linenos">73</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="PointBase-74"><a href="#PointBase-74"><span class="linenos">74</span></a>    
</span><span id="PointBase-75"><a href="#PointBase-75"><span class="linenos">75</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointBase-76"><a href="#PointBase-76"><span class="linenos">76</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="PointBase.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">0</span>

        
    </div>
    <a class="headerlink" href="#PointBase.dimension"></a>
    
    

                            </div>
                            <div id="PointBase.copy" class="classattr">
                                        <input id="PointBase.copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointBase">PointBase</a></span>:</span></span>

                <label class="view-source-button" for="PointBase.copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase.copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase.copy-59"><a href="#PointBase.copy-59"><span class="linenos">59</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase.copy-60"><a href="#PointBase.copy-60"><span class="linenos">60</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Should make relevant copy of an object (not so general and deep as a deepcopy()). should copy only known object fields.
Example:
    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point.copy()
        return result</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointBase.shallow_copy" class="classattr">
                                        <input id="PointBase.shallow_copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shallow_copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointBase">PointBase</a></span>:</span></span>

                <label class="view-source-button" for="PointBase.shallow_copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase.shallow_copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase.shallow_copy-62"><a href="#PointBase.shallow_copy-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase.shallow_copy-63"><a href="#PointBase.shallow_copy-63"><span class="linenos">63</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Same as copy.copy(self), but should copy only known object fields.
Example:
    def shallow_copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point
        return result</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointBase.updated_copy" class="classattr">
                                        <input id="PointBase.updated_copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">updated_copy</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">update</span><span class="p">:</span> <span class="n">Dict</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointBase">PointBase</a></span>:</span></span>

                <label class="view-source-button" for="PointBase.updated_copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase.updated_copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase.updated_copy-65"><a href="#PointBase.updated_copy-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointBase&#39;</span><span class="p">:</span>
</span><span id="PointBase.updated_copy-66"><a href="#PointBase.updated_copy-66"><span class="linenos">66</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            <div class="docstring"><p>Will make updated copy of an object. Other behavior should be the same as in the <code>def copy(self)</code> method.
Example:
    # from cengal.data_manipulation.get_dict_key_with_callable_default import get_dict_key_with_callable_default
    from cengal.entities.copyable import CopyableMixin, get_dict_key_with_callable_default</p>

<pre><code>def updated_copy(self, update: Dict):
    cls = self.__class__
    result = cls.__new__(cls)
    result.__dict__['dimension'] = update.get('dimension', self.dimension)
    result.__dict__['_point'] = get_dict_key_with_callable_default(update, '_point', lambda: self._point.copy())
    return result
</code></pre>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointBase.dim" class="classattr">
                                        <input id="PointBase.dim-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">dim</span><span class="annotation">: int</span>

                <label class="view-source-button" for="PointBase.dim-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase.dim"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase.dim-68"><a href="#PointBase.dim-68"><span class="linenos">68</span></a>    <span class="nd">@property</span>
</span><span id="PointBase.dim-69"><a href="#PointBase.dim-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">dim</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="PointBase.dim-70"><a href="#PointBase.dim-70"><span class="linenos">70</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span></pre></div>


    

                            </div>
                            <div id="PointBase.clear" class="classattr">
                                        <input id="PointBase.clear-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="PointBase.clear-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointBase.clear"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointBase.clear-75"><a href="#PointBase.clear-75"><span class="linenos">75</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointBase.clear-76"><a href="#PointBase.clear-76"><span class="linenos">76</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="PointDimensionIndexError">
                            <input id="PointDimensionIndexError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PointDimensionIndexError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="PointDimensionIndexError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointDimensionIndexError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointDimensionIndexError-79"><a href="#PointDimensionIndexError-79"><span class="linenos">79</span></a><span class="k">class</span> <span class="nc">PointDimensionIndexError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="PointDimensionIndexError-80"><a href="#PointDimensionIndexError-80"><span class="linenos">80</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="PointDimensionIndexError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="PointDimensionIndexError.with_traceback" class="function">with_traceback</dd>
                <dd id="PointDimensionIndexError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PointNd">
                            <input id="PointNd-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PointNd</span><wbr>(<span class="base"><a href="#PointBase">PointBase</a></span>):

                <label class="view-source-button" for="PointNd-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd-87"><a href="#PointNd-87"><span class="linenos"> 87</span></a><span class="k">class</span> <span class="nc">PointNd</span><span class="p">(</span><span class="n">PointBase</span><span class="p">):</span>
</span><span id="PointNd-88"><a href="#PointNd-88"><span class="linenos"> 88</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PointNd-89"><a href="#PointNd-89"><span class="linenos"> 89</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="PointNd-90"><a href="#PointNd-90"><span class="linenos"> 90</span></a>    <span class="n">_default_ndarray_type</span> <span class="o">=</span> <span class="nb">float</span>
</span><span id="PointNd-91"><a href="#PointNd-91"><span class="linenos"> 91</span></a>    <span class="n">_default_shallow_copy</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="PointNd-92"><a href="#PointNd-92"><span class="linenos"> 92</span></a>
</span><span id="PointNd-93"><a href="#PointNd-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="PointNd-94"><a href="#PointNd-94"><span class="linenos"> 94</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="PointNd-95"><a href="#PointNd-95"><span class="linenos"> 95</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="PointNd-96"><a href="#PointNd-96"><span class="linenos"> 96</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="PointNd-97"><a href="#PointNd-97"><span class="linenos"> 97</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd-98"><a href="#PointNd-98"><span class="linenos"> 98</span></a>        <span class="n">shallow_copy</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_shallow_copy</span><span class="p">)</span>
</span><span id="PointNd-99"><a href="#PointNd-99"><span class="linenos"> 99</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="PointNd-100"><a href="#PointNd-100"><span class="linenos">100</span></a>        <span class="k">if</span> <span class="n">shallow_copy</span> <span class="ow">and</span> <span class="n">args</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="PointNd-101"><a href="#PointNd-101"><span class="linenos">101</span></a>            <span class="n">first_element</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd-102"><a href="#PointNd-102"><span class="linenos">102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd-103"><a href="#PointNd-103"><span class="linenos">103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_point</span>
</span><span id="PointNd-104"><a href="#PointNd-104"><span class="linenos">104</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd-105"><a href="#PointNd-105"><span class="linenos">105</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-106"><a href="#PointNd-106"><span class="linenos">106</span></a>            <span class="k">if</span> <span class="n">dimension</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd-107"><a href="#PointNd-107"><span class="linenos">107</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dimension</span>
</span><span id="PointNd-108"><a href="#PointNd-108"><span class="linenos">108</span></a>            
</span><span id="PointNd-109"><a href="#PointNd-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">:</span> <span class="n">RawListPointType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PointNd-110"><a href="#PointNd-110"><span class="linenos">110</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_ndarray_type</span><span class="p">)</span>
</span><span id="PointNd-111"><a href="#PointNd-111"><span class="linenos">111</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="PointNd-112"><a href="#PointNd-112"><span class="linenos">112</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">}:</span>
</span><span id="PointNd-113"><a href="#PointNd-113"><span class="linenos">113</span></a>                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong type: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="PointNd-114"><a href="#PointNd-114"><span class="linenos">114</span></a>                <span class="k">raise</span> <span class="n">PointWrongNdarrayTypeError</span>
</span><span id="PointNd-115"><a href="#PointNd-115"><span class="linenos">115</span></a>            
</span><span id="PointNd-116"><a href="#PointNd-116"><span class="linenos">116</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="PointNd-117"><a href="#PointNd-117"><span class="linenos">117</span></a>            <span class="bp">self</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="PointNd-118"><a href="#PointNd-118"><span class="linenos">118</span></a>    
</span><span id="PointNd-119"><a href="#PointNd-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointNd-120"><a href="#PointNd-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">(dimension=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="si">}</span><span class="s1">, point=(</span><span class="si">{</span><span class="s2">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="nb">str</span><span class="p">(</span><span class="n">item</span><span class="p">)</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">item</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">))</span><span class="si">}</span><span class="s1">), ndarray_type=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="PointNd-121"><a href="#PointNd-121"><span class="linenos">121</span></a>    
</span><span id="PointNd-122"><a href="#PointNd-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd-123"><a href="#PointNd-123"><span class="linenos">123</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd-124"><a href="#PointNd-124"><span class="linenos">124</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd-125"><a href="#PointNd-125"><span class="linenos">125</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd-126"><a href="#PointNd-126"><span class="linenos">126</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="PointNd-127"><a href="#PointNd-127"><span class="linenos">127</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd-128"><a href="#PointNd-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="PointNd-129"><a href="#PointNd-129"><span class="linenos">129</span></a>    
</span><span id="PointNd-130"><a href="#PointNd-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd-131"><a href="#PointNd-131"><span class="linenos">131</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd-132"><a href="#PointNd-132"><span class="linenos">132</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd-133"><a href="#PointNd-133"><span class="linenos">133</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd-134"><a href="#PointNd-134"><span class="linenos">134</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span>
</span><span id="PointNd-135"><a href="#PointNd-135"><span class="linenos">135</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd-136"><a href="#PointNd-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="PointNd-137"><a href="#PointNd-137"><span class="linenos">137</span></a>    
</span><span id="PointNd-138"><a href="#PointNd-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd-139"><a href="#PointNd-139"><span class="linenos">139</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd-140"><a href="#PointNd-140"><span class="linenos">140</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd-141"><a href="#PointNd-141"><span class="linenos">141</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd-142"><a href="#PointNd-142"><span class="linenos">142</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_dict_key_with_callable_default</span><span class="p">(</span><span class="n">update</span><span class="p">,</span> <span class="s1">&#39;_point&#39;</span><span class="p">,</span> <span class="k">lambda</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">())</span>
</span><span id="PointNd-143"><a href="#PointNd-143"><span class="linenos">143</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd-144"><a href="#PointNd-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="PointNd-145"><a href="#PointNd-145"><span class="linenos">145</span></a>    
</span><span id="PointNd-146"><a href="#PointNd-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointNd-147"><a href="#PointNd-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="p">()]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span>
</span><span id="PointNd-148"><a href="#PointNd-148"><span class="linenos">148</span></a>        <span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="PointNd-149"><a href="#PointNd-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="PointNd-150"><a href="#PointNd-150"><span class="linenos">150</span></a>
</span><span id="PointNd-151"><a href="#PointNd-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="PointNd-152"><a href="#PointNd-152"><span class="linenos">152</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="PointNd-153"><a href="#PointNd-153"><span class="linenos">153</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="PointNd-154"><a href="#PointNd-154"><span class="linenos">154</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawUniversalPointType</span><span class="p">:</span>
</span><span id="PointNd-155"><a href="#PointNd-155"><span class="linenos">155</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="PointNd-156"><a href="#PointNd-156"><span class="linenos">156</span></a>            <span class="n">first_element</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd-157"><a href="#PointNd-157"><span class="linenos">157</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_element</span>
</span><span id="PointNd-158"><a href="#PointNd-158"><span class="linenos">158</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_element</span><span class="p">,</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="PointNd-159"><a href="#PointNd-159"><span class="linenos">159</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">first_element</span><span class="p">()</span>
</span><span id="PointNd-160"><a href="#PointNd-160"><span class="linenos">160</span></a>            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_element</span><span class="p">,</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">)):</span>
</span><span id="PointNd-161"><a href="#PointNd-161"><span class="linenos">161</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PointNd-162"><a href="#PointNd-162"><span class="linenos">162</span></a>
</span><span id="PointNd-163"><a href="#PointNd-163"><span class="linenos">163</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">item</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="PointNd-164"><a href="#PointNd-164"><span class="linenos">164</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd-165"><a href="#PointNd-165"><span class="linenos">165</span></a>                    <span class="k">break</span>
</span><span id="PointNd-166"><a href="#PointNd-166"><span class="linenos">166</span></a>
</span><span id="PointNd-167"><a href="#PointNd-167"><span class="linenos">167</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="PointNd-168"><a href="#PointNd-168"><span class="linenos">168</span></a>        <span class="k">elif</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="PointNd-169"><a href="#PointNd-169"><span class="linenos">169</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd-170"><a href="#PointNd-170"><span class="linenos">170</span></a>                <span class="k">for</span> <span class="n">dim_name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-171"><a href="#PointNd-171"><span class="linenos">171</span></a>                    <span class="k">if</span> <span class="n">dim_name</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="PointNd-172"><a href="#PointNd-172"><span class="linenos">172</span></a>                        <span class="n">kwargs</span><span class="p">[</span><span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">dim_index</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">dim_name</span><span class="p">]</span>
</span><span id="PointNd-173"><a href="#PointNd-173"><span class="linenos">173</span></a>                        <span class="k">break</span>
</span><span id="PointNd-174"><a href="#PointNd-174"><span class="linenos">174</span></a>
</span><span id="PointNd-175"><a href="#PointNd-175"><span class="linenos">175</span></a>            <span class="k">for</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="p">):</span>
</span><span id="PointNd-176"><a href="#PointNd-176"><span class="linenos">176</span></a>                <span class="n">dim_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">dim_index</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="PointNd-177"><a href="#PointNd-177"><span class="linenos">177</span></a>                <span class="n">dim_value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">dim_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="PointNd-178"><a href="#PointNd-178"><span class="linenos">178</span></a>                <span class="k">if</span> <span class="n">dim_value</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd-179"><a href="#PointNd-179"><span class="linenos">179</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">dim_value</span>
</span><span id="PointNd-180"><a href="#PointNd-180"><span class="linenos">180</span></a>        
</span><span id="PointNd-181"><a href="#PointNd-181"><span class="linenos">181</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span>
</span><span id="PointNd-182"><a href="#PointNd-182"><span class="linenos">182</span></a>    
</span><span id="PointNd-183"><a href="#PointNd-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">as_list</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawListPointType</span><span class="p">:</span>
</span><span id="PointNd-184"><a href="#PointNd-184"><span class="linenos">184</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="PointNd-185"><a href="#PointNd-185"><span class="linenos">185</span></a>    
</span><span id="PointNd-186"><a href="#PointNd-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="fm">__setattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">__value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd-187"><a href="#PointNd-187"><span class="linenos">187</span></a>        <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd-188"><a href="#PointNd-188"><span class="linenos">188</span></a>            <span class="k">if</span> <span class="n">__name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-189"><a href="#PointNd-189"><span class="linenos">189</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">__value</span>
</span><span id="PointNd-190"><a href="#PointNd-190"><span class="linenos">190</span></a>                <span class="k">return</span> <span class="n">__value</span>
</span><span id="PointNd-191"><a href="#PointNd-191"><span class="linenos">191</span></a>
</span><span id="PointNd-192"><a href="#PointNd-192"><span class="linenos">192</span></a>        <span class="k">if</span> <span class="n">__name</span> <span class="ow">and</span> <span class="n">__name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-193"><a href="#PointNd-193"><span class="linenos">193</span></a>            <span class="n">index_str</span> <span class="o">=</span> <span class="n">__name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-194"><a href="#PointNd-194"><span class="linenos">194</span></a>            <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-195"><a href="#PointNd-195"><span class="linenos">195</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-196"><a href="#PointNd-196"><span class="linenos">196</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd-197"><a href="#PointNd-197"><span class="linenos">197</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">__value</span>
</span><span id="PointNd-198"><a href="#PointNd-198"><span class="linenos">198</span></a>                    <span class="k">return</span> <span class="n">__value</span>
</span><span id="PointNd-199"><a href="#PointNd-199"><span class="linenos">199</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-200"><a href="#PointNd-200"><span class="linenos">200</span></a>                    <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-201"><a href="#PointNd-201"><span class="linenos">201</span></a>
</span><span id="PointNd-202"><a href="#PointNd-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__setattr__</span><span class="p">(</span><span class="n">__name</span><span class="p">,</span> <span class="n">__value</span><span class="p">)</span>
</span><span id="PointNd-203"><a href="#PointNd-203"><span class="linenos">203</span></a>    
</span><span id="PointNd-204"><a href="#PointNd-204"><span class="linenos">204</span></a>    <span class="k">def</span> <span class="fm">__getattribute__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">__name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="PointNd-205"><a href="#PointNd-205"><span class="linenos">205</span></a>        <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_dim_names_translation_table&#39;</span><span class="p">):</span>
</span><span id="PointNd-206"><a href="#PointNd-206"><span class="linenos">206</span></a>            <span class="k">if</span> <span class="n">__name</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-207"><a href="#PointNd-207"><span class="linenos">207</span></a>                <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_point&#39;</span><span class="p">)[</span><span class="n">dim_index</span><span class="p">]</span>
</span><span id="PointNd-208"><a href="#PointNd-208"><span class="linenos">208</span></a>
</span><span id="PointNd-209"><a href="#PointNd-209"><span class="linenos">209</span></a>        <span class="k">if</span> <span class="n">__name</span> <span class="ow">and</span> <span class="n">__name</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-210"><a href="#PointNd-210"><span class="linenos">210</span></a>            <span class="n">index_str</span> <span class="o">=</span> <span class="n">__name</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-211"><a href="#PointNd-211"><span class="linenos">211</span></a>            <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-212"><a href="#PointNd-212"><span class="linenos">212</span></a>                <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-213"><a href="#PointNd-213"><span class="linenos">213</span></a>                <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;dim&#39;</span><span class="p">):</span>
</span><span id="PointNd-214"><a href="#PointNd-214"><span class="linenos">214</span></a>                    <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="s1">&#39;_point&#39;</span><span class="p">)[</span><span class="n">index</span><span class="p">]</span>
</span><span id="PointNd-215"><a href="#PointNd-215"><span class="linenos">215</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-216"><a href="#PointNd-216"><span class="linenos">216</span></a>                    <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-217"><a href="#PointNd-217"><span class="linenos">217</span></a>
</span><span id="PointNd-218"><a href="#PointNd-218"><span class="linenos">218</span></a>        <span class="k">return</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__getattribute__</span><span class="p">(</span><span class="n">__name</span><span class="p">)</span>
</span><span id="PointNd-219"><a href="#PointNd-219"><span class="linenos">219</span></a>    
</span><span id="PointNd-220"><a href="#PointNd-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_or_key</span><span class="p">):</span>
</span><span id="PointNd-221"><a href="#PointNd-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd-222"><a href="#PointNd-222"><span class="linenos">222</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index_or_key</span><span class="p">]</span>
</span><span id="PointNd-223"><a href="#PointNd-223"><span class="linenos">223</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd-224"><a href="#PointNd-224"><span class="linenos">224</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd-225"><a href="#PointNd-225"><span class="linenos">225</span></a>                <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-226"><a href="#PointNd-226"><span class="linenos">226</span></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span>
</span><span id="PointNd-227"><a href="#PointNd-227"><span class="linenos">227</span></a>
</span><span id="PointNd-228"><a href="#PointNd-228"><span class="linenos">228</span></a>            <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-229"><a href="#PointNd-229"><span class="linenos">229</span></a>                <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-230"><a href="#PointNd-230"><span class="linenos">230</span></a>                <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-231"><a href="#PointNd-231"><span class="linenos">231</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-232"><a href="#PointNd-232"><span class="linenos">232</span></a>                    <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd-233"><a href="#PointNd-233"><span class="linenos">233</span></a>                        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="PointNd-234"><a href="#PointNd-234"><span class="linenos">234</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-235"><a href="#PointNd-235"><span class="linenos">235</span></a>                        <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-236"><a href="#PointNd-236"><span class="linenos">236</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-237"><a href="#PointNd-237"><span class="linenos">237</span></a>            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-238"><a href="#PointNd-238"><span class="linenos">238</span></a>
</span><span id="PointNd-239"><a href="#PointNd-239"><span class="linenos">239</span></a>    <span class="k">def</span> <span class="fm">__setitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index_or_key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
</span><span id="PointNd-240"><a href="#PointNd-240"><span class="linenos">240</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd-241"><a href="#PointNd-241"><span class="linenos">241</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index_or_key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="PointNd-242"><a href="#PointNd-242"><span class="linenos">242</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd-243"><a href="#PointNd-243"><span class="linenos">243</span></a>            <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd-244"><a href="#PointNd-244"><span class="linenos">244</span></a>                <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-245"><a href="#PointNd-245"><span class="linenos">245</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">dim_index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="PointNd-246"><a href="#PointNd-246"><span class="linenos">246</span></a>
</span><span id="PointNd-247"><a href="#PointNd-247"><span class="linenos">247</span></a>            <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-248"><a href="#PointNd-248"><span class="linenos">248</span></a>                <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-249"><a href="#PointNd-249"><span class="linenos">249</span></a>                <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-250"><a href="#PointNd-250"><span class="linenos">250</span></a>                    <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-251"><a href="#PointNd-251"><span class="linenos">251</span></a>                    <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd-252"><a href="#PointNd-252"><span class="linenos">252</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="PointNd-253"><a href="#PointNd-253"><span class="linenos">253</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-254"><a href="#PointNd-254"><span class="linenos">254</span></a>                        <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-255"><a href="#PointNd-255"><span class="linenos">255</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-256"><a href="#PointNd-256"><span class="linenos">256</span></a>            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-257"><a href="#PointNd-257"><span class="linenos">257</span></a>    
</span><span id="PointNd-258"><a href="#PointNd-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointNd-259"><a href="#PointNd-259"><span class="linenos">259</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span>
</span><span id="PointNd-260"><a href="#PointNd-260"><span class="linenos">260</span></a>
</span><span id="PointNd-261"><a href="#PointNd-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">crop_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd-262"><a href="#PointNd-262"><span class="linenos">262</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="PointNd-263"><a href="#PointNd-263"><span class="linenos">263</span></a><span class="sd">        &gt;&gt; p4 = Point3d(3, 5, 2, 8)</span>
</span><span id="PointNd-264"><a href="#PointNd-264"><span class="linenos">264</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p4.crop_to(&#39;z&#39;, &#39;n0&#39;, 3))</span>
</span><span id="PointNd-265"><a href="#PointNd-265"><span class="linenos">265</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="PointNd-266"><a href="#PointNd-266"><span class="linenos">266</span></a><span class="sd">        Point3d(2, 3, 8)</span>
</span><span id="PointNd-267"><a href="#PointNd-267"><span class="linenos">267</span></a>
</span><span id="PointNd-268"><a href="#PointNd-268"><span class="linenos">268</span></a><span class="sd">        Raises:</span>
</span><span id="PointNd-269"><a href="#PointNd-269"><span class="linenos">269</span></a><span class="sd">            PointDimensionIndexError: _description_</span>
</span><span id="PointNd-270"><a href="#PointNd-270"><span class="linenos">270</span></a><span class="sd">            KeyError: _description_</span>
</span><span id="PointNd-271"><a href="#PointNd-271"><span class="linenos">271</span></a>
</span><span id="PointNd-272"><a href="#PointNd-272"><span class="linenos">272</span></a><span class="sd">        Returns:</span>
</span><span id="PointNd-273"><a href="#PointNd-273"><span class="linenos">273</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="PointNd-274"><a href="#PointNd-274"><span class="linenos">274</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="PointNd-275"><a href="#PointNd-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="PointNd-276"><a href="#PointNd-276"><span class="linenos">276</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd-277"><a href="#PointNd-277"><span class="linenos">277</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="PointNd-278"><a href="#PointNd-278"><span class="linenos">278</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="PointNd-279"><a href="#PointNd-279"><span class="linenos">279</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PointNd-280"><a href="#PointNd-280"><span class="linenos">280</span></a>            
</span><span id="PointNd-281"><a href="#PointNd-281"><span class="linenos">281</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd-282"><a href="#PointNd-282"><span class="linenos">282</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="PointNd-283"><a href="#PointNd-283"><span class="linenos">283</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd-284"><a href="#PointNd-284"><span class="linenos">284</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="PointNd-285"><a href="#PointNd-285"><span class="linenos">285</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd-286"><a href="#PointNd-286"><span class="linenos">286</span></a>                    <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd-287"><a href="#PointNd-287"><span class="linenos">287</span></a>                        <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd-288"><a href="#PointNd-288"><span class="linenos">288</span></a>                            <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dim_index</span><span class="p">)</span>
</span><span id="PointNd-289"><a href="#PointNd-289"><span class="linenos">289</span></a>
</span><span id="PointNd-290"><a href="#PointNd-290"><span class="linenos">290</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-291"><a href="#PointNd-291"><span class="linenos">291</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-292"><a href="#PointNd-292"><span class="linenos">292</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-293"><a href="#PointNd-293"><span class="linenos">293</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-294"><a href="#PointNd-294"><span class="linenos">294</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd-295"><a href="#PointNd-295"><span class="linenos">295</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="PointNd-296"><a href="#PointNd-296"><span class="linenos">296</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-297"><a href="#PointNd-297"><span class="linenos">297</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-298"><a href="#PointNd-298"><span class="linenos">298</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-299"><a href="#PointNd-299"><span class="linenos">299</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-300"><a href="#PointNd-300"><span class="linenos">300</span></a>            
</span><span id="PointNd-301"><a href="#PointNd-301"><span class="linenos">301</span></a>            <span class="n">croped_data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd-302"><a href="#PointNd-302"><span class="linenos">302</span></a>            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">index_sequence</span><span class="p">:</span>
</span><span id="PointNd-303"><a href="#PointNd-303"><span class="linenos">303</span></a>                <span class="n">croped_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="PointNd-304"><a href="#PointNd-304"><span class="linenos">304</span></a>            
</span><span id="PointNd-305"><a href="#PointNd-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">croped_data</span><span class="p">),</span> <span class="n">croped_data</span><span class="p">)</span>
</span><span id="PointNd-306"><a href="#PointNd-306"><span class="linenos">306</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-307"><a href="#PointNd-307"><span class="linenos">307</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="PointNd-308"><a href="#PointNd-308"><span class="linenos">308</span></a>
</span><span id="PointNd-309"><a href="#PointNd-309"><span class="linenos">309</span></a>    <span class="k">def</span> <span class="nf">expand_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd-310"><a href="#PointNd-310"><span class="linenos">310</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="PointNd-311"><a href="#PointNd-311"><span class="linenos">311</span></a><span class="sd">        &gt;&gt; p2 = Point2d(2, 3)</span>
</span><span id="PointNd-312"><a href="#PointNd-312"><span class="linenos">312</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p2.expand_to(3, 2, &#39;n0&#39;))</span>
</span><span id="PointNd-313"><a href="#PointNd-313"><span class="linenos">313</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="PointNd-314"><a href="#PointNd-314"><span class="linenos">314</span></a><span class="sd">        Point3d(3, 0, 2)</span>
</span><span id="PointNd-315"><a href="#PointNd-315"><span class="linenos">315</span></a>
</span><span id="PointNd-316"><a href="#PointNd-316"><span class="linenos">316</span></a><span class="sd">        Args:</span>
</span><span id="PointNd-317"><a href="#PointNd-317"><span class="linenos">317</span></a><span class="sd">            dimension (int): _description_</span>
</span><span id="PointNd-318"><a href="#PointNd-318"><span class="linenos">318</span></a><span class="sd">            *args (Union[Tuple[int], Tuple[str]]): list used to map `point item` with index equal to `list&#39;s item index` to `result point item` with index equals to `list&#39;s item value`. If value is str: it should starts from &#39;n&#39; char and continue with (positive) numeric chars only</span>
</span><span id="PointNd-319"><a href="#PointNd-319"><span class="linenos">319</span></a>
</span><span id="PointNd-320"><a href="#PointNd-320"><span class="linenos">320</span></a><span class="sd">        Raises:</span>
</span><span id="PointNd-321"><a href="#PointNd-321"><span class="linenos">321</span></a><span class="sd">            PointDimensionIndexError: when `len(args) &gt; len(self)`</span>
</span><span id="PointNd-322"><a href="#PointNd-322"><span class="linenos">322</span></a><span class="sd">            KeyError: wrong type of *args or type/format of it&#39;s value(s)</span>
</span><span id="PointNd-323"><a href="#PointNd-323"><span class="linenos">323</span></a>
</span><span id="PointNd-324"><a href="#PointNd-324"><span class="linenos">324</span></a><span class="sd">        Returns:</span>
</span><span id="PointNd-325"><a href="#PointNd-325"><span class="linenos">325</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="PointNd-326"><a href="#PointNd-326"><span class="linenos">326</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="PointNd-327"><a href="#PointNd-327"><span class="linenos">327</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="PointNd-328"><a href="#PointNd-328"><span class="linenos">328</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd-329"><a href="#PointNd-329"><span class="linenos">329</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="PointNd-330"><a href="#PointNd-330"><span class="linenos">330</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="PointNd-331"><a href="#PointNd-331"><span class="linenos">331</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PointNd-332"><a href="#PointNd-332"><span class="linenos">332</span></a>            
</span><span id="PointNd-333"><a href="#PointNd-333"><span class="linenos">333</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd-334"><a href="#PointNd-334"><span class="linenos">334</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="PointNd-335"><a href="#PointNd-335"><span class="linenos">335</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd-336"><a href="#PointNd-336"><span class="linenos">336</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="PointNd-337"><a href="#PointNd-337"><span class="linenos">337</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd-338"><a href="#PointNd-338"><span class="linenos">338</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd-339"><a href="#PointNd-339"><span class="linenos">339</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd-340"><a href="#PointNd-340"><span class="linenos">340</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd-341"><a href="#PointNd-341"><span class="linenos">341</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd-342"><a href="#PointNd-342"><span class="linenos">342</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="n">dimension</span><span class="p">:</span>
</span><span id="PointNd-343"><a href="#PointNd-343"><span class="linenos">343</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="PointNd-344"><a href="#PointNd-344"><span class="linenos">344</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-345"><a href="#PointNd-345"><span class="linenos">345</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd-346"><a href="#PointNd-346"><span class="linenos">346</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-347"><a href="#PointNd-347"><span class="linenos">347</span></a>                            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-348"><a href="#PointNd-348"><span class="linenos">348</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-349"><a href="#PointNd-349"><span class="linenos">349</span></a>                        <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-350"><a href="#PointNd-350"><span class="linenos">350</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-351"><a href="#PointNd-351"><span class="linenos">351</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd-352"><a href="#PointNd-352"><span class="linenos">352</span></a>            
</span><span id="PointNd-353"><a href="#PointNd-353"><span class="linenos">353</span></a>            <span class="n">expansion_data</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="PointNd-354"><a href="#PointNd-354"><span class="linenos">354</span></a>            <span class="k">for</span> <span class="n">source_index</span><span class="p">,</span> <span class="n">destination_index</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">index_sequence</span><span class="p">):</span>
</span><span id="PointNd-355"><a href="#PointNd-355"><span class="linenos">355</span></a>                <span class="n">expansion_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">destination_index</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">source_index</span><span class="p">]</span>
</span><span id="PointNd-356"><a href="#PointNd-356"><span class="linenos">356</span></a>            
</span><span id="PointNd-357"><a href="#PointNd-357"><span class="linenos">357</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">**</span><span class="n">expansion_data</span><span class="p">)</span>
</span><span id="PointNd-358"><a href="#PointNd-358"><span class="linenos">358</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-359"><a href="#PointNd-359"><span class="linenos">359</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="PointNd-360"><a href="#PointNd-360"><span class="linenos">360</span></a>    
</span><span id="PointNd-361"><a href="#PointNd-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="fm">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="PointNd-362"><a href="#PointNd-362"><span class="linenos">362</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="PointNd-363"><a href="#PointNd-363"><span class="linenos">363</span></a>            <span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="PointNd-364"><a href="#PointNd-364"><span class="linenos">364</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">dim</span><span class="p">)</span> <span class="ow">and</span> <span class="n">array_equal</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="PointNd-365"><a href="#PointNd-365"><span class="linenos">365</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd-366"><a href="#PointNd-366"><span class="linenos">366</span></a>                <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">dim</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span><span id="PointNd-367"><a href="#PointNd-367"><span class="linenos">367</span></a>        
</span><span id="PointNd-368"><a href="#PointNd-368"><span class="linenos">368</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="PointNd-369"><a href="#PointNd-369"><span class="linenos">369</span></a>    
</span><span id="PointNd-370"><a href="#PointNd-370"><span class="linenos">370</span></a>    <span class="k">def</span> <span class="fm">__ne__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="PointNd-371"><a href="#PointNd-371"><span class="linenos">371</span></a>        <span class="k">return</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__eq__</span><span class="p">(</span><span class="n">other</span><span class="p">)</span>
</span><span id="PointNd-372"><a href="#PointNd-372"><span class="linenos">372</span></a>    
</span><span id="PointNd-373"><a href="#PointNd-373"><span class="linenos">373</span></a>    <span class="k">def</span> <span class="fm">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="PointNd-374"><a href="#PointNd-374"><span class="linenos">374</span></a>        <span class="k">return</span> <span class="nb">hash</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)))</span>
</span><span id="PointNd-375"><a href="#PointNd-375"><span class="linenos">375</span></a>    
</span><span id="PointNd-376"><a href="#PointNd-376"><span class="linenos">376</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="PointNd-377"><a href="#PointNd-377"><span class="linenos">377</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;If not zero point</span>
</span><span id="PointNd-378"><a href="#PointNd-378"><span class="linenos">378</span></a>
</span><span id="PointNd-379"><a href="#PointNd-379"><span class="linenos">379</span></a><span class="sd">        Returns:</span>
</span><span id="PointNd-380"><a href="#PointNd-380"><span class="linenos">380</span></a><span class="sd">            bool: _description_</span>
</span><span id="PointNd-381"><a href="#PointNd-381"><span class="linenos">381</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="PointNd-382"><a href="#PointNd-382"><span class="linenos">382</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">:</span>
</span><span id="PointNd-383"><a href="#PointNd-383"><span class="linenos">383</span></a>            <span class="k">if</span> <span class="n">item</span><span class="p">:</span>
</span><span id="PointNd-384"><a href="#PointNd-384"><span class="linenos">384</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="PointNd-385"><a href="#PointNd-385"><span class="linenos">385</span></a>        
</span><span id="PointNd-386"><a href="#PointNd-386"><span class="linenos">386</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            <div id="PointNd.__init__" class="classattr">
                                        <input id="PointNd.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">PointNd</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="PointNd.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.__init__-93"><a href="#PointNd.__init__-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="PointNd.__init__-94"><a href="#PointNd.__init__-94"><span class="linenos"> 94</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="PointNd.__init__-95"><a href="#PointNd.__init__-95"><span class="linenos"> 95</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="PointNd.__init__-96"><a href="#PointNd.__init__-96"><span class="linenos"> 96</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="PointNd.__init__-97"><a href="#PointNd.__init__-97"><span class="linenos"> 97</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd.__init__-98"><a href="#PointNd.__init__-98"><span class="linenos"> 98</span></a>        <span class="n">shallow_copy</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_shallow_copy</span><span class="p">)</span>
</span><span id="PointNd.__init__-99"><a href="#PointNd.__init__-99"><span class="linenos"> 99</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;shallow_copy&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="PointNd.__init__-100"><a href="#PointNd.__init__-100"><span class="linenos">100</span></a>        <span class="k">if</span> <span class="n">shallow_copy</span> <span class="ow">and</span> <span class="n">args</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">PointNd</span><span class="p">):</span>
</span><span id="PointNd.__init__-101"><a href="#PointNd.__init__-101"><span class="linenos">101</span></a>            <span class="n">first_element</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd.__init__-102"><a href="#PointNd.__init__-102"><span class="linenos">102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd.__init__-103"><a href="#PointNd.__init__-103"><span class="linenos">103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_point</span>
</span><span id="PointNd.__init__-104"><a href="#PointNd.__init__-104"><span class="linenos">104</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">first_element</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd.__init__-105"><a href="#PointNd.__init__-105"><span class="linenos">105</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.__init__-106"><a href="#PointNd.__init__-106"><span class="linenos">106</span></a>            <span class="k">if</span> <span class="n">dimension</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNd.__init__-107"><a href="#PointNd.__init__-107"><span class="linenos">107</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">dimension</span>
</span><span id="PointNd.__init__-108"><a href="#PointNd.__init__-108"><span class="linenos">108</span></a>            
</span><span id="PointNd.__init__-109"><a href="#PointNd.__init__-109"><span class="linenos">109</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">:</span> <span class="n">RawListPointType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PointNd.__init__-110"><a href="#PointNd.__init__-110"><span class="linenos">110</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_default_ndarray_type</span><span class="p">)</span>
</span><span id="PointNd.__init__-111"><a href="#PointNd.__init__-111"><span class="linenos">111</span></a>            <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;ndarray_type&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="PointNd.__init__-112"><a href="#PointNd.__init__-112"><span class="linenos">112</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">{</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">}:</span>
</span><span id="PointNd.__init__-113"><a href="#PointNd.__init__-113"><span class="linenos">113</span></a>                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong type: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="PointNd.__init__-114"><a href="#PointNd.__init__-114"><span class="linenos">114</span></a>                <span class="k">raise</span> <span class="n">PointWrongNdarrayTypeError</span>
</span><span id="PointNd.__init__-115"><a href="#PointNd.__init__-115"><span class="linenos">115</span></a>            
</span><span id="PointNd.__init__-116"><a href="#PointNd.__init__-116"><span class="linenos">116</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="PointNd.__init__-117"><a href="#PointNd.__init__-117"><span class="linenos">117</span></a>            <span class="bp">self</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="PointNd.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">None</span>

        
    </div>
    <a class="headerlink" href="#PointNd.dimension"></a>
    
    

                            </div>
                            <div id="PointNd.copy" class="classattr">
                                        <input id="PointNd.copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="PointNd.copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.copy-122"><a href="#PointNd.copy-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd.copy-123"><a href="#PointNd.copy-123"><span class="linenos">123</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd.copy-124"><a href="#PointNd.copy-124"><span class="linenos">124</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd.copy-125"><a href="#PointNd.copy-125"><span class="linenos">125</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd.copy-126"><a href="#PointNd.copy-126"><span class="linenos">126</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="PointNd.copy-127"><a href="#PointNd.copy-127"><span class="linenos">127</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd.copy-128"><a href="#PointNd.copy-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>Should make relevant copy of an object (not so general and deep as a deepcopy()). should copy only known object fields.
Example:
    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point.copy()
        return result</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointNd.shallow_copy" class="classattr">
                                        <input id="PointNd.shallow_copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shallow_copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="PointNd.shallow_copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.shallow_copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.shallow_copy-130"><a href="#PointNd.shallow_copy-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">shallow_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd.shallow_copy-131"><a href="#PointNd.shallow_copy-131"><span class="linenos">131</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd.shallow_copy-132"><a href="#PointNd.shallow_copy-132"><span class="linenos">132</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd.shallow_copy-133"><a href="#PointNd.shallow_copy-133"><span class="linenos">133</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd.shallow_copy-134"><a href="#PointNd.shallow_copy-134"><span class="linenos">134</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span>
</span><span id="PointNd.shallow_copy-135"><a href="#PointNd.shallow_copy-135"><span class="linenos">135</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd.shallow_copy-136"><a href="#PointNd.shallow_copy-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>Same as copy.copy(self), but should copy only known object fields.
Example:
    def shallow_copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point
        return result</p>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointNd.updated_copy" class="classattr">
                                        <input id="PointNd.updated_copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">updated_copy</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">update</span><span class="p">:</span> <span class="n">Dict</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="PointNd.updated_copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.updated_copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.updated_copy-138"><a href="#PointNd.updated_copy-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">updated_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">update</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd.updated_copy-139"><a href="#PointNd.updated_copy-139"><span class="linenos">139</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="PointNd.updated_copy-140"><a href="#PointNd.updated_copy-140"><span class="linenos">140</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="PointNd.updated_copy-141"><a href="#PointNd.updated_copy-141"><span class="linenos">141</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;dimension&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dimension</span>
</span><span id="PointNd.updated_copy-142"><a href="#PointNd.updated_copy-142"><span class="linenos">142</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_point&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">get_dict_key_with_callable_default</span><span class="p">(</span><span class="n">update</span><span class="p">,</span> <span class="s1">&#39;_point&#39;</span><span class="p">,</span> <span class="k">lambda</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="o">.</span><span class="n">copy</span><span class="p">())</span>
</span><span id="PointNd.updated_copy-143"><a href="#PointNd.updated_copy-143"><span class="linenos">143</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;_ndarray_type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span>
</span><span id="PointNd.updated_copy-144"><a href="#PointNd.updated_copy-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>Will make updated copy of an object. Other behavior should be the same as in the <code>def copy(self)</code> method.
Example:
    # from cengal.data_manipulation.get_dict_key_with_callable_default import get_dict_key_with_callable_default
    from cengal.entities.copyable import CopyableMixin, get_dict_key_with_callable_default</p>

<pre><code>def updated_copy(self, update: Dict):
    cls = self.__class__
    result = cls.__new__(cls)
    result.__dict__['dimension'] = update.get('dimension', self.dimension)
    result.__dict__['_point'] = get_dict_key_with_callable_default(update, '_point', lambda: self._point.copy())
    return result
</code></pre>

<p>Raises:
    NotImplementedError: _description_</p>
</div>


                            </div>
                            <div id="PointNd.clear" class="classattr">
                                        <input id="PointNd.clear-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">clear</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="PointNd.clear-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.clear"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.clear-146"><a href="#PointNd.clear-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">clear</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="PointNd.clear-147"><a href="#PointNd.clear-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_ndarray_type</span><span class="p">()]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span>
</span><span id="PointNd.clear-148"><a href="#PointNd.clear-148"><span class="linenos">148</span></a>        <span class="k">if</span> <span class="n">numpy_present</span><span class="p">:</span>
</span><span id="PointNd.clear-149"><a href="#PointNd.clear-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_point</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="PointNd.as_list" class="classattr">
                                        <input id="PointNd.as_list-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">as_list</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="PointNd.as_list-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.as_list"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.as_list-183"><a href="#PointNd.as_list-183"><span class="linenos">183</span></a>    <span class="k">def</span> <span class="nf">as_list</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RawListPointType</span><span class="p">:</span>
</span><span id="PointNd.as_list-184"><a href="#PointNd.as_list-184"><span class="linenos">184</span></a>        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="PointNd.crop_to" class="classattr">
                                        <input id="PointNd.crop_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">crop_to</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="PointNd.crop_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.crop_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.crop_to-261"><a href="#PointNd.crop_to-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">crop_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd.crop_to-262"><a href="#PointNd.crop_to-262"><span class="linenos">262</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="PointNd.crop_to-263"><a href="#PointNd.crop_to-263"><span class="linenos">263</span></a><span class="sd">        &gt;&gt; p4 = Point3d(3, 5, 2, 8)</span>
</span><span id="PointNd.crop_to-264"><a href="#PointNd.crop_to-264"><span class="linenos">264</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p4.crop_to(&#39;z&#39;, &#39;n0&#39;, 3))</span>
</span><span id="PointNd.crop_to-265"><a href="#PointNd.crop_to-265"><span class="linenos">265</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="PointNd.crop_to-266"><a href="#PointNd.crop_to-266"><span class="linenos">266</span></a><span class="sd">        Point3d(2, 3, 8)</span>
</span><span id="PointNd.crop_to-267"><a href="#PointNd.crop_to-267"><span class="linenos">267</span></a>
</span><span id="PointNd.crop_to-268"><a href="#PointNd.crop_to-268"><span class="linenos">268</span></a><span class="sd">        Raises:</span>
</span><span id="PointNd.crop_to-269"><a href="#PointNd.crop_to-269"><span class="linenos">269</span></a><span class="sd">            PointDimensionIndexError: _description_</span>
</span><span id="PointNd.crop_to-270"><a href="#PointNd.crop_to-270"><span class="linenos">270</span></a><span class="sd">            KeyError: _description_</span>
</span><span id="PointNd.crop_to-271"><a href="#PointNd.crop_to-271"><span class="linenos">271</span></a>
</span><span id="PointNd.crop_to-272"><a href="#PointNd.crop_to-272"><span class="linenos">272</span></a><span class="sd">        Returns:</span>
</span><span id="PointNd.crop_to-273"><a href="#PointNd.crop_to-273"><span class="linenos">273</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="PointNd.crop_to-274"><a href="#PointNd.crop_to-274"><span class="linenos">274</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="PointNd.crop_to-275"><a href="#PointNd.crop_to-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="PointNd.crop_to-276"><a href="#PointNd.crop_to-276"><span class="linenos">276</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd.crop_to-277"><a href="#PointNd.crop_to-277"><span class="linenos">277</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="PointNd.crop_to-278"><a href="#PointNd.crop_to-278"><span class="linenos">278</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="PointNd.crop_to-279"><a href="#PointNd.crop_to-279"><span class="linenos">279</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PointNd.crop_to-280"><a href="#PointNd.crop_to-280"><span class="linenos">280</span></a>            
</span><span id="PointNd.crop_to-281"><a href="#PointNd.crop_to-281"><span class="linenos">281</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd.crop_to-282"><a href="#PointNd.crop_to-282"><span class="linenos">282</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="PointNd.crop_to-283"><a href="#PointNd.crop_to-283"><span class="linenos">283</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd.crop_to-284"><a href="#PointNd.crop_to-284"><span class="linenos">284</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="PointNd.crop_to-285"><a href="#PointNd.crop_to-285"><span class="linenos">285</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd.crop_to-286"><a href="#PointNd.crop_to-286"><span class="linenos">286</span></a>                    <span class="k">for</span> <span class="n">dim_name_variants</span><span class="p">,</span> <span class="n">dim_index</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_dim_names_translation_table</span><span class="p">:</span>
</span><span id="PointNd.crop_to-287"><a href="#PointNd.crop_to-287"><span class="linenos">287</span></a>                        <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">dim_name_variants</span><span class="p">:</span>
</span><span id="PointNd.crop_to-288"><a href="#PointNd.crop_to-288"><span class="linenos">288</span></a>                            <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dim_index</span><span class="p">)</span>
</span><span id="PointNd.crop_to-289"><a href="#PointNd.crop_to-289"><span class="linenos">289</span></a>
</span><span id="PointNd.crop_to-290"><a href="#PointNd.crop_to-290"><span class="linenos">290</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd.crop_to-291"><a href="#PointNd.crop_to-291"><span class="linenos">291</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd.crop_to-292"><a href="#PointNd.crop_to-292"><span class="linenos">292</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd.crop_to-293"><a href="#PointNd.crop_to-293"><span class="linenos">293</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd.crop_to-294"><a href="#PointNd.crop_to-294"><span class="linenos">294</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="PointNd.crop_to-295"><a href="#PointNd.crop_to-295"><span class="linenos">295</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="PointNd.crop_to-296"><a href="#PointNd.crop_to-296"><span class="linenos">296</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.crop_to-297"><a href="#PointNd.crop_to-297"><span class="linenos">297</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd.crop_to-298"><a href="#PointNd.crop_to-298"><span class="linenos">298</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.crop_to-299"><a href="#PointNd.crop_to-299"><span class="linenos">299</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd.crop_to-300"><a href="#PointNd.crop_to-300"><span class="linenos">300</span></a>            
</span><span id="PointNd.crop_to-301"><a href="#PointNd.crop_to-301"><span class="linenos">301</span></a>            <span class="n">croped_data</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd.crop_to-302"><a href="#PointNd.crop_to-302"><span class="linenos">302</span></a>            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">index_sequence</span><span class="p">:</span>
</span><span id="PointNd.crop_to-303"><a href="#PointNd.crop_to-303"><span class="linenos">303</span></a>                <span class="n">croped_data</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</span><span id="PointNd.crop_to-304"><a href="#PointNd.crop_to-304"><span class="linenos">304</span></a>            
</span><span id="PointNd.crop_to-305"><a href="#PointNd.crop_to-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">croped_data</span><span class="p">),</span> <span class="n">croped_data</span><span class="p">)</span>
</span><span id="PointNd.crop_to-306"><a href="#PointNd.crop_to-306"><span class="linenos">306</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.crop_to-307"><a href="#PointNd.crop_to-307"><span class="linenos">307</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Example:</p>

<blockquote>
  <blockquote>
    <p>p4 = Point3d(3, 5, 2, 8)
    p3 = convert_point_to_xyz(p4.crop_to('z', 'n0', 3))
    print(p3)
    Point3d(2, 3, 8)</p>
  </blockquote>
</blockquote>

<p>Raises:
    PointDimensionIndexError: _description_
    KeyError: _description_</p>

<p>Returns:
    PointNd: _description_</p>
</div>


                            </div>
                            <div id="PointNd.expand_to" class="classattr">
                                        <input id="PointNd.expand_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">expand_to</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="PointNd.expand_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNd.expand_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNd.expand_to-309"><a href="#PointNd.expand_to-309"><span class="linenos">309</span></a>    <span class="k">def</span> <span class="nf">expand_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;PointNd&#39;</span><span class="p">:</span>
</span><span id="PointNd.expand_to-310"><a href="#PointNd.expand_to-310"><span class="linenos">310</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="PointNd.expand_to-311"><a href="#PointNd.expand_to-311"><span class="linenos">311</span></a><span class="sd">        &gt;&gt; p2 = Point2d(2, 3)</span>
</span><span id="PointNd.expand_to-312"><a href="#PointNd.expand_to-312"><span class="linenos">312</span></a><span class="sd">        &gt;&gt; p3 = convert_point_to_xyz(p2.expand_to(3, 2, &#39;n0&#39;))</span>
</span><span id="PointNd.expand_to-313"><a href="#PointNd.expand_to-313"><span class="linenos">313</span></a><span class="sd">        &gt;&gt; print(p3)</span>
</span><span id="PointNd.expand_to-314"><a href="#PointNd.expand_to-314"><span class="linenos">314</span></a><span class="sd">        Point3d(3, 0, 2)</span>
</span><span id="PointNd.expand_to-315"><a href="#PointNd.expand_to-315"><span class="linenos">315</span></a>
</span><span id="PointNd.expand_to-316"><a href="#PointNd.expand_to-316"><span class="linenos">316</span></a><span class="sd">        Args:</span>
</span><span id="PointNd.expand_to-317"><a href="#PointNd.expand_to-317"><span class="linenos">317</span></a><span class="sd">            dimension (int): _description_</span>
</span><span id="PointNd.expand_to-318"><a href="#PointNd.expand_to-318"><span class="linenos">318</span></a><span class="sd">            *args (Union[Tuple[int], Tuple[str]]): list used to map `point item` with index equal to `list&#39;s item index` to `result point item` with index equals to `list&#39;s item value`. If value is str: it should starts from &#39;n&#39; char and continue with (positive) numeric chars only</span>
</span><span id="PointNd.expand_to-319"><a href="#PointNd.expand_to-319"><span class="linenos">319</span></a>
</span><span id="PointNd.expand_to-320"><a href="#PointNd.expand_to-320"><span class="linenos">320</span></a><span class="sd">        Raises:</span>
</span><span id="PointNd.expand_to-321"><a href="#PointNd.expand_to-321"><span class="linenos">321</span></a><span class="sd">            PointDimensionIndexError: when `len(args) &gt; len(self)`</span>
</span><span id="PointNd.expand_to-322"><a href="#PointNd.expand_to-322"><span class="linenos">322</span></a><span class="sd">            KeyError: wrong type of *args or type/format of it&#39;s value(s)</span>
</span><span id="PointNd.expand_to-323"><a href="#PointNd.expand_to-323"><span class="linenos">323</span></a>
</span><span id="PointNd.expand_to-324"><a href="#PointNd.expand_to-324"><span class="linenos">324</span></a><span class="sd">        Returns:</span>
</span><span id="PointNd.expand_to-325"><a href="#PointNd.expand_to-325"><span class="linenos">325</span></a><span class="sd">            PointNd: _description_</span>
</span><span id="PointNd.expand_to-326"><a href="#PointNd.expand_to-326"><span class="linenos">326</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="PointNd.expand_to-327"><a href="#PointNd.expand_to-327"><span class="linenos">327</span></a>        <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="PointNd.expand_to-328"><a href="#PointNd.expand_to-328"><span class="linenos">328</span></a>            <span class="n">first_item</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="PointNd.expand_to-329"><a href="#PointNd.expand_to-329"><span class="linenos">329</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="n">first_item</span>
</span><span id="PointNd.expand_to-330"><a href="#PointNd.expand_to-330"><span class="linenos">330</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">first_item</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">)):</span>
</span><span id="PointNd.expand_to-331"><a href="#PointNd.expand_to-331"><span class="linenos">331</span></a>                <span class="n">data</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="PointNd.expand_to-332"><a href="#PointNd.expand_to-332"><span class="linenos">332</span></a>            
</span><span id="PointNd.expand_to-333"><a href="#PointNd.expand_to-333"><span class="linenos">333</span></a>            <span class="n">index_sequence</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="PointNd.expand_to-334"><a href="#PointNd.expand_to-334"><span class="linenos">334</span></a>            <span class="k">for</span> <span class="n">index_or_key</span> <span class="ow">in</span> <span class="n">data</span><span class="p">:</span>
</span><span id="PointNd.expand_to-335"><a href="#PointNd.expand_to-335"><span class="linenos">335</span></a>                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="PointNd.expand_to-336"><a href="#PointNd.expand_to-336"><span class="linenos">336</span></a>                    <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">)</span>
</span><span id="PointNd.expand_to-337"><a href="#PointNd.expand_to-337"><span class="linenos">337</span></a>                <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index_or_key</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>
</span><span id="PointNd.expand_to-338"><a href="#PointNd.expand_to-338"><span class="linenos">338</span></a>                    <span class="k">if</span> <span class="n">index_or_key</span> <span class="ow">and</span> <span class="n">index_or_key</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s1">&#39;n&#39;</span><span class="p">):</span>
</span><span id="PointNd.expand_to-339"><a href="#PointNd.expand_to-339"><span class="linenos">339</span></a>                        <span class="n">index_str</span> <span class="o">=</span> <span class="n">index_or_key</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="PointNd.expand_to-340"><a href="#PointNd.expand_to-340"><span class="linenos">340</span></a>                        <span class="k">if</span> <span class="n">index_str</span><span class="o">.</span><span class="n">isnumeric</span><span class="p">():</span>
</span><span id="PointNd.expand_to-341"><a href="#PointNd.expand_to-341"><span class="linenos">341</span></a>                            <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="PointNd.expand_to-342"><a href="#PointNd.expand_to-342"><span class="linenos">342</span></a>                            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="n">dimension</span><span class="p">:</span>
</span><span id="PointNd.expand_to-343"><a href="#PointNd.expand_to-343"><span class="linenos">343</span></a>                                <span class="n">index_sequence</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="PointNd.expand_to-344"><a href="#PointNd.expand_to-344"><span class="linenos">344</span></a>                            <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.expand_to-345"><a href="#PointNd.expand_to-345"><span class="linenos">345</span></a>                                <span class="k">raise</span> <span class="n">PointDimensionIndexError</span>
</span><span id="PointNd.expand_to-346"><a href="#PointNd.expand_to-346"><span class="linenos">346</span></a>                        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.expand_to-347"><a href="#PointNd.expand_to-347"><span class="linenos">347</span></a>                            <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd.expand_to-348"><a href="#PointNd.expand_to-348"><span class="linenos">348</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.expand_to-349"><a href="#PointNd.expand_to-349"><span class="linenos">349</span></a>                        <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd.expand_to-350"><a href="#PointNd.expand_to-350"><span class="linenos">350</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.expand_to-351"><a href="#PointNd.expand_to-351"><span class="linenos">351</span></a>                    <span class="k">raise</span> <span class="ne">KeyError</span>
</span><span id="PointNd.expand_to-352"><a href="#PointNd.expand_to-352"><span class="linenos">352</span></a>            
</span><span id="PointNd.expand_to-353"><a href="#PointNd.expand_to-353"><span class="linenos">353</span></a>            <span class="n">expansion_data</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="PointNd.expand_to-354"><a href="#PointNd.expand_to-354"><span class="linenos">354</span></a>            <span class="k">for</span> <span class="n">source_index</span><span class="p">,</span> <span class="n">destination_index</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">index_sequence</span><span class="p">):</span>
</span><span id="PointNd.expand_to-355"><a href="#PointNd.expand_to-355"><span class="linenos">355</span></a>                <span class="n">expansion_data</span><span class="p">[</span><span class="sa">f</span><span class="s1">&#39;n</span><span class="si">{</span><span class="n">destination_index</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_point</span><span class="p">[</span><span class="n">source_index</span><span class="p">]</span>
</span><span id="PointNd.expand_to-356"><a href="#PointNd.expand_to-356"><span class="linenos">356</span></a>            
</span><span id="PointNd.expand_to-357"><a href="#PointNd.expand_to-357"><span class="linenos">357</span></a>            <span class="k">return</span> <span class="n">PointNd</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">**</span><span class="n">expansion_data</span><span class="p">)</span>
</span><span id="PointNd.expand_to-358"><a href="#PointNd.expand_to-358"><span class="linenos">358</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="PointNd.expand_to-359"><a href="#PointNd.expand_to-359"><span class="linenos">359</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Example:</p>

<blockquote>
  <blockquote>
    <p>p2 = Point2d(2, 3)
    p3 = convert_point_to_xyz(p2.expand_to(3, 2, 'n0'))
    print(p3)
    Point3d(3, 0, 2)</p>
  </blockquote>
</blockquote>

<p>Args:
    dimension (int): _description_
    *args (Union[Tuple[int], Tuple[str]]): list used to map <code>point item</code> with index equal to <code>list's item index</code> to <code>result point item</code> with index equals to <code>list's item value</code>. If value is str: it should starts from 'n' char and continue with (positive) numeric chars only</p>

<p>Raises:
    PointDimensionIndexError: when <code>len(args) &gt; len(self)</code>
    KeyError: wrong type of *args or type/format of it's value(s)</p>

<p>Returns:
    PointNd: _description_</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#PointBase">PointBase</a></dt>
                                <dd id="PointNd.dim" class="variable"><a href="#PointBase.dim">dim</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Point1d">
                            <input id="Point1d-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Point1d</span><wbr>(<span class="base"><a href="#PointNd">PointNd</a></span>):

                <label class="view-source-button" for="Point1d-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point1d"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point1d-389"><a href="#Point1d-389"><span class="linenos">389</span></a><span class="k">class</span> <span class="nc">Point1d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="Point1d-390"><a href="#Point1d-390"><span class="linenos">390</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Point1d-391"><a href="#Point1d-391"><span class="linenos">391</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="Point1d-392"><a href="#Point1d-392"><span class="linenos">392</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="Point1d-393"><a href="#Point1d-393"><span class="linenos">393</span></a>    <span class="p">)</span>
</span><span id="Point1d-394"><a href="#Point1d-394"><span class="linenos">394</span></a>
</span><span id="Point1d-395"><a href="#Point1d-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point1d-396"><a href="#Point1d-396"><span class="linenos">396</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point1d-397"><a href="#Point1d-397"><span class="linenos">397</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point1d-398"><a href="#Point1d-398"><span class="linenos">398</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point1d-399"><a href="#Point1d-399"><span class="linenos">399</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="Point1d.__init__" class="classattr">
                                        <input id="Point1d.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Point1d</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="Point1d.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point1d.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point1d.__init__-395"><a href="#Point1d.__init__-395"><span class="linenos">395</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point1d.__init__-396"><a href="#Point1d.__init__-396"><span class="linenos">396</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point1d.__init__-397"><a href="#Point1d.__init__-397"><span class="linenos">397</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point1d.__init__-398"><a href="#Point1d.__init__-398"><span class="linenos">398</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point1d.__init__-399"><a href="#Point1d.__init__-399"><span class="linenos">399</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Point1d.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">1</span>

        
    </div>
    <a class="headerlink" href="#Point1d.dimension"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#PointNd">PointNd</a></dt>
                                <dd id="Point1d.copy" class="function"><a href="#PointNd.copy">copy</a></dd>
                <dd id="Point1d.shallow_copy" class="function"><a href="#PointNd.shallow_copy">shallow_copy</a></dd>
                <dd id="Point1d.updated_copy" class="function"><a href="#PointNd.updated_copy">updated_copy</a></dd>
                <dd id="Point1d.clear" class="function"><a href="#PointNd.clear">clear</a></dd>
                <dd id="Point1d.as_list" class="function"><a href="#PointNd.as_list">as_list</a></dd>
                <dd id="Point1d.crop_to" class="function"><a href="#PointNd.crop_to">crop_to</a></dd>
                <dd id="Point1d.expand_to" class="function"><a href="#PointNd.expand_to">expand_to</a></dd>

            </div>
            <div><dt><a href="#PointBase">PointBase</a></dt>
                                <dd id="Point1d.dim" class="variable"><a href="#PointBase.dim">dim</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Point2d">
                            <input id="Point2d-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Point2d</span><wbr>(<span class="base"><a href="#PointNd">PointNd</a></span>):

                <label class="view-source-button" for="Point2d-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point2d"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point2d-402"><a href="#Point2d-402"><span class="linenos">402</span></a><span class="k">class</span> <span class="nc">Point2d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="Point2d-403"><a href="#Point2d-403"><span class="linenos">403</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="Point2d-404"><a href="#Point2d-404"><span class="linenos">404</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="Point2d-405"><a href="#Point2d-405"><span class="linenos">405</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="Point2d-406"><a href="#Point2d-406"><span class="linenos">406</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="Point2d-407"><a href="#Point2d-407"><span class="linenos">407</span></a>    <span class="p">)</span>
</span><span id="Point2d-408"><a href="#Point2d-408"><span class="linenos">408</span></a>
</span><span id="Point2d-409"><a href="#Point2d-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point2d-410"><a href="#Point2d-410"><span class="linenos">410</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point2d-411"><a href="#Point2d-411"><span class="linenos">411</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point2d-412"><a href="#Point2d-412"><span class="linenos">412</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point2d-413"><a href="#Point2d-413"><span class="linenos">413</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="Point2d.__init__" class="classattr">
                                        <input id="Point2d.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Point2d</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="Point2d.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point2d.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point2d.__init__-409"><a href="#Point2d.__init__-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point2d.__init__-410"><a href="#Point2d.__init__-410"><span class="linenos">410</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point2d.__init__-411"><a href="#Point2d.__init__-411"><span class="linenos">411</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point2d.__init__-412"><a href="#Point2d.__init__-412"><span class="linenos">412</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point2d.__init__-413"><a href="#Point2d.__init__-413"><span class="linenos">413</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Point2d.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">2</span>

        
    </div>
    <a class="headerlink" href="#Point2d.dimension"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#PointNd">PointNd</a></dt>
                                <dd id="Point2d.copy" class="function"><a href="#PointNd.copy">copy</a></dd>
                <dd id="Point2d.shallow_copy" class="function"><a href="#PointNd.shallow_copy">shallow_copy</a></dd>
                <dd id="Point2d.updated_copy" class="function"><a href="#PointNd.updated_copy">updated_copy</a></dd>
                <dd id="Point2d.clear" class="function"><a href="#PointNd.clear">clear</a></dd>
                <dd id="Point2d.as_list" class="function"><a href="#PointNd.as_list">as_list</a></dd>
                <dd id="Point2d.crop_to" class="function"><a href="#PointNd.crop_to">crop_to</a></dd>
                <dd id="Point2d.expand_to" class="function"><a href="#PointNd.expand_to">expand_to</a></dd>

            </div>
            <div><dt><a href="#PointBase">PointBase</a></dt>
                                <dd id="Point2d.dim" class="variable"><a href="#PointBase.dim">dim</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="Point3d">
                            <input id="Point3d-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Point3d</span><wbr>(<span class="base"><a href="#PointNd">PointNd</a></span>):

                <label class="view-source-button" for="Point3d-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point3d"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point3d-416"><a href="#Point3d-416"><span class="linenos">416</span></a><span class="k">class</span> <span class="nc">Point3d</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="Point3d-417"><a href="#Point3d-417"><span class="linenos">417</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="Point3d-418"><a href="#Point3d-418"><span class="linenos">418</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="Point3d-419"><a href="#Point3d-419"><span class="linenos">419</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="Point3d-420"><a href="#Point3d-420"><span class="linenos">420</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="Point3d-421"><a href="#Point3d-421"><span class="linenos">421</span></a>        <span class="p">({</span><span class="s1">&#39;z&#39;</span><span class="p">,</span> <span class="s1">&#39;Z&#39;</span><span class="p">},</span> <span class="mi">2</span><span class="p">),</span>
</span><span id="Point3d-422"><a href="#Point3d-422"><span class="linenos">422</span></a>    <span class="p">)</span>
</span><span id="Point3d-423"><a href="#Point3d-423"><span class="linenos">423</span></a>
</span><span id="Point3d-424"><a href="#Point3d-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point3d-425"><a href="#Point3d-425"><span class="linenos">425</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point3d-426"><a href="#Point3d-426"><span class="linenos">426</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point3d-427"><a href="#Point3d-427"><span class="linenos">427</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point3d-428"><a href="#Point3d-428"><span class="linenos">428</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="Point3d.__init__" class="classattr">
                                        <input id="Point3d.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Point3d</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="Point3d.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Point3d.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Point3d.__init__-424"><a href="#Point3d.__init__-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="Point3d.__init__-425"><a href="#Point3d.__init__-425"><span class="linenos">425</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="Point3d.__init__-426"><a href="#Point3d.__init__-426"><span class="linenos">426</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="Point3d.__init__-427"><a href="#Point3d.__init__-427"><span class="linenos">427</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="Point3d.__init__-428"><a href="#Point3d.__init__-428"><span class="linenos">428</span></a>        <span class="n">PointNd</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Point3d.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">3</span>

        
    </div>
    <a class="headerlink" href="#Point3d.dimension"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#PointNd">PointNd</a></dt>
                                <dd id="Point3d.copy" class="function"><a href="#PointNd.copy">copy</a></dd>
                <dd id="Point3d.shallow_copy" class="function"><a href="#PointNd.shallow_copy">shallow_copy</a></dd>
                <dd id="Point3d.updated_copy" class="function"><a href="#PointNd.updated_copy">updated_copy</a></dd>
                <dd id="Point3d.clear" class="function"><a href="#PointNd.clear">clear</a></dd>
                <dd id="Point3d.as_list" class="function"><a href="#PointNd.as_list">as_list</a></dd>
                <dd id="Point3d.crop_to" class="function"><a href="#PointNd.crop_to">crop_to</a></dd>
                <dd id="Point3d.expand_to" class="function"><a href="#PointNd.expand_to">expand_to</a></dd>

            </div>
            <div><dt><a href="#PointBase">PointBase</a></dt>
                                <dd id="Point3d.dim" class="variable"><a href="#PointBase.dim">dim</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PointNdXYZ">
                            <input id="PointNdXYZ-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PointNdXYZ</span><wbr>(<span class="base"><a href="#PointNd">PointNd</a></span>):

                <label class="view-source-button" for="PointNdXYZ-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNdXYZ"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNdXYZ-431"><a href="#PointNdXYZ-431"><span class="linenos">431</span></a><span class="k">class</span> <span class="nc">PointNdXYZ</span><span class="p">(</span><span class="n">PointNd</span><span class="p">):</span>
</span><span id="PointNdXYZ-432"><a href="#PointNdXYZ-432"><span class="linenos">432</span></a>    <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="PointNdXYZ-433"><a href="#PointNdXYZ-433"><span class="linenos">433</span></a>    <span class="n">_dim_names_translation_table</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="p">(</span>
</span><span id="PointNdXYZ-434"><a href="#PointNdXYZ-434"><span class="linenos">434</span></a>        <span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;X&#39;</span><span class="p">},</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="PointNdXYZ-435"><a href="#PointNdXYZ-435"><span class="linenos">435</span></a>        <span class="p">({</span><span class="s1">&#39;y&#39;</span><span class="p">,</span> <span class="s1">&#39;Y&#39;</span><span class="p">},</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="PointNdXYZ-436"><a href="#PointNdXYZ-436"><span class="linenos">436</span></a>        <span class="p">({</span><span class="s1">&#39;z&#39;</span><span class="p">,</span> <span class="s1">&#39;Z&#39;</span><span class="p">},</span> <span class="mi">2</span><span class="p">),</span>
</span><span id="PointNdXYZ-437"><a href="#PointNdXYZ-437"><span class="linenos">437</span></a>    <span class="p">)</span>
</span><span id="PointNdXYZ-438"><a href="#PointNdXYZ-438"><span class="linenos">438</span></a>
</span><span id="PointNdXYZ-439"><a href="#PointNdXYZ-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="PointNdXYZ-440"><a href="#PointNdXYZ-440"><span class="linenos">440</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="PointNdXYZ-441"><a href="#PointNdXYZ-441"><span class="linenos">441</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="PointNdXYZ-442"><a href="#PointNdXYZ-442"><span class="linenos">442</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="PointNdXYZ-443"><a href="#PointNdXYZ-443"><span class="linenos">443</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNdXYZ-444"><a href="#PointNdXYZ-444"><span class="linenos">444</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="PointNdXYZ.__init__" class="classattr">
                                        <input id="PointNdXYZ.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">PointNdXYZ</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span></span>)</span>

                <label class="view-source-button" for="PointNdXYZ.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PointNdXYZ.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PointNdXYZ.__init__-439"><a href="#PointNdXYZ.__init__-439"><span class="linenos">439</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span>
</span><span id="PointNdXYZ.__init__-440"><a href="#PointNdXYZ.__init__-440"><span class="linenos">440</span></a>            <span class="p">,</span> <span class="n">dimension</span><span class="p">:</span> <span class="nb">int</span>
</span><span id="PointNdXYZ.__init__-441"><a href="#PointNdXYZ.__init__-441"><span class="linenos">441</span></a>            <span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]],</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span>
</span><span id="PointNdXYZ.__init__-442"><a href="#PointNdXYZ.__init__-442"><span class="linenos">442</span></a>            <span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span>
</span><span id="PointNdXYZ.__init__-443"><a href="#PointNdXYZ.__init__-443"><span class="linenos">443</span></a>            <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="PointNdXYZ.__init__-444"><a href="#PointNdXYZ.__init__-444"><span class="linenos">444</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">dimension</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="PointNdXYZ.dimension" class="classattr">
                                <div class="attr variable">
            <span class="name">dimension</span><span class="annotation">: int</span>        =
<span class="default_value">None</span>

        
    </div>
    <a class="headerlink" href="#PointNdXYZ.dimension"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#PointNd">PointNd</a></dt>
                                <dd id="PointNdXYZ.copy" class="function"><a href="#PointNd.copy">copy</a></dd>
                <dd id="PointNdXYZ.shallow_copy" class="function"><a href="#PointNd.shallow_copy">shallow_copy</a></dd>
                <dd id="PointNdXYZ.updated_copy" class="function"><a href="#PointNd.updated_copy">updated_copy</a></dd>
                <dd id="PointNdXYZ.clear" class="function"><a href="#PointNd.clear">clear</a></dd>
                <dd id="PointNdXYZ.as_list" class="function"><a href="#PointNd.as_list">as_list</a></dd>
                <dd id="PointNdXYZ.crop_to" class="function"><a href="#PointNd.crop_to">crop_to</a></dd>
                <dd id="PointNdXYZ.expand_to" class="function"><a href="#PointNd.expand_to">expand_to</a></dd>

            </div>
            <div><dt><a href="#PointBase">PointBase</a></dt>
                                <dd id="PointNdXYZ.dim" class="variable"><a href="#PointBase.dim">dim</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="convert_point_to_xyz">
                            <input id="convert_point_to_xyz-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">convert_point_to_xyz</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">point</span><span class="p">:</span> <span class="n"><a href="#PointNd">PointNd</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#PointNd">PointNd</a></span>:</span></span>

                <label class="view-source-button" for="convert_point_to_xyz-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#convert_point_to_xyz"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="convert_point_to_xyz-447"><a href="#convert_point_to_xyz-447"><span class="linenos">447</span></a><span class="k">def</span> <span class="nf">convert_point_to_xyz</span><span class="p">(</span><span class="n">point</span><span class="p">:</span> <span class="n">PointNd</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">PointNd</span><span class="p">:</span>
</span><span id="convert_point_to_xyz-448"><a href="#convert_point_to_xyz-448"><span class="linenos">448</span></a>    <span class="k">if</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="convert_point_to_xyz-449"><a href="#convert_point_to_xyz-449"><span class="linenos">449</span></a>        <span class="k">return</span> <span class="n">Point1d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="convert_point_to_xyz-450"><a href="#convert_point_to_xyz-450"><span class="linenos">450</span></a>    <span class="k">elif</span> <span class="mi">2</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="convert_point_to_xyz-451"><a href="#convert_point_to_xyz-451"><span class="linenos">451</span></a>        <span class="k">return</span> <span class="n">Point2d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="convert_point_to_xyz-452"><a href="#convert_point_to_xyz-452"><span class="linenos">452</span></a>    <span class="k">elif</span> <span class="mi">3</span> <span class="o">==</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="convert_point_to_xyz-453"><a href="#convert_point_to_xyz-453"><span class="linenos">453</span></a>        <span class="k">return</span> <span class="n">Point3d</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span><span id="convert_point_to_xyz-454"><a href="#convert_point_to_xyz-454"><span class="linenos">454</span></a>    <span class="k">elif</span> <span class="mi">3</span> <span class="o">&lt;</span> <span class="n">point</span><span class="o">.</span><span class="n">dim</span><span class="p">:</span>
</span><span id="convert_point_to_xyz-455"><a href="#convert_point_to_xyz-455"><span class="linenos">455</span></a>        <span class="k">return</span> <span class="n">PointNdXYZ</span><span class="p">(</span><span class="n">point</span><span class="p">,</span> <span class="n">shallow_copy</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>