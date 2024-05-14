---
title: ellipse
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.math<wbr>.geometry<wbr>.ellipse<wbr>.versions<wbr>.v_0<wbr>.ellipse    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-ellipse-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-ellipse-view-source"><span>View Source</span></label>

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
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">cengal.math.numbers</span> <span class="kn">import</span> <span class="n">RationalNumber</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.time_management.repeat_for_a_time</span> <span class="kn">import</span> <span class="n">Tracer</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">math</span> <span class="kn">import</span> <span class="n">sqrt</span><span class="p">,</span> <span class="n">pi</span><span class="p">,</span> <span class="n">factorial</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="k">class</span> <span class="nc">Ellipse</span><span class="p">:</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="sd">    https://www.youtube.com/watch?v=5nW3nJhBHL0</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">    http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">b</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">=</span> <span class="n">a</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">=</span> <span class="n">b</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="k">def</span> <span class="nf">y</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RationalNumber</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="n">x</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="nd">@property</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="k">def</span> <span class="nf">area</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="nd">@property</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="k">def</span> <span class="nf">h</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="k">return</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="nd">@property</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    <span class="k">def</span> <span class="nf">e</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="k">return</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="nd">@property</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="k">def</span> <span class="nf">c</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>    <span class="nd">@property</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>    <span class="k">def</span> <span class="nf">perimeter__kepler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="nd">@property</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="k">def</span> <span class="nf">perimeter__naive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="nd">@property</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="k">def</span> <span class="nf">perimeter__euler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="nd">@property</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Computationly efficient. Not more that 6.1% deviation (less than 5% for `1 / 75` ellipses)</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="sd">        Returns:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">6</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">5</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="nd">@property</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__euler__and__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">0.8</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__lazy</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__euler</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="nd">@property</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_1</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">((</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)))</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="nd">@property</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">53</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span> <span class="o">+</span> <span class="p">(</span><span class="mi">717</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">35</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">269</span> <span class="o">*</span> <span class="n">a</span> <span class="o">**</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">667</span> <span class="o">*</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span> <span class="o">+</span> <span class="mi">371</span> <span class="o">*</span> <span class="n">b</span> <span class="o">**</span> <span class="mi">2</span><span class="p">))</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="nd">@property</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__ramanujan_1__and__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">2.4</span><span class="p">:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__precise</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__ramanujan_1</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="nd">@property</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="mi">10</span> <span class="o">+</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">4</span> <span class="o">-</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)))</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__time_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">desired_approximation_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">return_iterations_num</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="n">tr</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">desired_approximation_time</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="k">while</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>            <span class="n">i</span> <span class="o">=</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="k">if</span> <span class="n">return_iterations_num</span><span class="p">:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span><span class="p">,</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>    
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__iter_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterations_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">iterations_num</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">from_r1_r2</span><span class="p">(</span><span class="n">r1</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">r2</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="k">return</span> <span class="n">Ellipse</span><span class="p">((</span><span class="n">r1</span> <span class="o">+</span> <span class="n">r2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="Ellipse">
                            <input id="Ellipse-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">Ellipse</span>:

                <label class="view-source-button" for="Ellipse-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse-40"><a href="#Ellipse-40"><span class="linenos"> 40</span></a><span class="k">class</span> <span class="nc">Ellipse</span><span class="p">:</span>
</span><span id="Ellipse-41"><a href="#Ellipse-41"><span class="linenos"> 41</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="Ellipse-42"><a href="#Ellipse-42"><span class="linenos"> 42</span></a><span class="sd">    https://www.youtube.com/watch?v=5nW3nJhBHL0</span>
</span><span id="Ellipse-43"><a href="#Ellipse-43"><span class="linenos"> 43</span></a><span class="sd">    http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html</span>
</span><span id="Ellipse-44"><a href="#Ellipse-44"><span class="linenos"> 44</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="Ellipse-45"><a href="#Ellipse-45"><span class="linenos"> 45</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">b</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="Ellipse-46"><a href="#Ellipse-46"><span class="linenos"> 46</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">=</span> <span class="n">a</span>
</span><span id="Ellipse-47"><a href="#Ellipse-47"><span class="linenos"> 47</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">=</span> <span class="n">b</span>
</span><span id="Ellipse-48"><a href="#Ellipse-48"><span class="linenos"> 48</span></a>    
</span><span id="Ellipse-49"><a href="#Ellipse-49"><span class="linenos"> 49</span></a>    <span class="k">def</span> <span class="nf">y</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RationalNumber</span><span class="p">:</span>
</span><span id="Ellipse-50"><a href="#Ellipse-50"><span class="linenos"> 50</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="n">x</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="Ellipse-51"><a href="#Ellipse-51"><span class="linenos"> 51</span></a>    
</span><span id="Ellipse-52"><a href="#Ellipse-52"><span class="linenos"> 52</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-53"><a href="#Ellipse-53"><span class="linenos"> 53</span></a>    <span class="k">def</span> <span class="nf">area</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-54"><a href="#Ellipse-54"><span class="linenos"> 54</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span>
</span><span id="Ellipse-55"><a href="#Ellipse-55"><span class="linenos"> 55</span></a>    
</span><span id="Ellipse-56"><a href="#Ellipse-56"><span class="linenos"> 56</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-57"><a href="#Ellipse-57"><span class="linenos"> 57</span></a>    <span class="k">def</span> <span class="nf">h</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-58"><a href="#Ellipse-58"><span class="linenos"> 58</span></a>        <span class="k">return</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span><span id="Ellipse-59"><a href="#Ellipse-59"><span class="linenos"> 59</span></a>    
</span><span id="Ellipse-60"><a href="#Ellipse-60"><span class="linenos"> 60</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-61"><a href="#Ellipse-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">e</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-62"><a href="#Ellipse-62"><span class="linenos"> 62</span></a>        <span class="k">return</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span>
</span><span id="Ellipse-63"><a href="#Ellipse-63"><span class="linenos"> 63</span></a>    
</span><span id="Ellipse-64"><a href="#Ellipse-64"><span class="linenos"> 64</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-65"><a href="#Ellipse-65"><span class="linenos"> 65</span></a>    <span class="k">def</span> <span class="nf">c</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-66"><a href="#Ellipse-66"><span class="linenos"> 66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="Ellipse-67"><a href="#Ellipse-67"><span class="linenos"> 67</span></a>    
</span><span id="Ellipse-68"><a href="#Ellipse-68"><span class="linenos"> 68</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-69"><a href="#Ellipse-69"><span class="linenos"> 69</span></a>    <span class="k">def</span> <span class="nf">perimeter__kepler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-70"><a href="#Ellipse-70"><span class="linenos"> 70</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-71"><a href="#Ellipse-71"><span class="linenos"> 71</span></a>    
</span><span id="Ellipse-72"><a href="#Ellipse-72"><span class="linenos"> 72</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-73"><a href="#Ellipse-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="nf">perimeter__naive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-74"><a href="#Ellipse-74"><span class="linenos"> 74</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="Ellipse-75"><a href="#Ellipse-75"><span class="linenos"> 75</span></a>    
</span><span id="Ellipse-76"><a href="#Ellipse-76"><span class="linenos"> 76</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-77"><a href="#Ellipse-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="nf">perimeter__euler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-78"><a href="#Ellipse-78"><span class="linenos"> 78</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="Ellipse-79"><a href="#Ellipse-79"><span class="linenos"> 79</span></a>    
</span><span id="Ellipse-80"><a href="#Ellipse-80"><span class="linenos"> 80</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-81"><a href="#Ellipse-81"><span class="linenos"> 81</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-82"><a href="#Ellipse-82"><span class="linenos"> 82</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Computationly efficient. Not more that 6.1% deviation (less than 5% for `1 / 75` ellipses)</span>
</span><span id="Ellipse-83"><a href="#Ellipse-83"><span class="linenos"> 83</span></a>
</span><span id="Ellipse-84"><a href="#Ellipse-84"><span class="linenos"> 84</span></a><span class="sd">        Returns:</span>
</span><span id="Ellipse-85"><a href="#Ellipse-85"><span class="linenos"> 85</span></a><span class="sd">            _type_: _description_</span>
</span><span id="Ellipse-86"><a href="#Ellipse-86"><span class="linenos"> 86</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Ellipse-87"><a href="#Ellipse-87"><span class="linenos"> 87</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-88"><a href="#Ellipse-88"><span class="linenos"> 88</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-89"><a href="#Ellipse-89"><span class="linenos"> 89</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">6</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">5</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span><span class="p">)</span>
</span><span id="Ellipse-90"><a href="#Ellipse-90"><span class="linenos"> 90</span></a>    
</span><span id="Ellipse-91"><a href="#Ellipse-91"><span class="linenos"> 91</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-92"><a href="#Ellipse-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__euler__and__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-93"><a href="#Ellipse-93"><span class="linenos"> 93</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-94"><a href="#Ellipse-94"><span class="linenos"> 94</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-95"><a href="#Ellipse-95"><span class="linenos"> 95</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">0.8</span><span class="p">:</span>
</span><span id="Ellipse-96"><a href="#Ellipse-96"><span class="linenos"> 96</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__lazy</span>
</span><span id="Ellipse-97"><a href="#Ellipse-97"><span class="linenos"> 97</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse-98"><a href="#Ellipse-98"><span class="linenos"> 98</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__euler</span>
</span><span id="Ellipse-99"><a href="#Ellipse-99"><span class="linenos"> 99</span></a>    
</span><span id="Ellipse-100"><a href="#Ellipse-100"><span class="linenos">100</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-101"><a href="#Ellipse-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_1</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-102"><a href="#Ellipse-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">((</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)))</span>
</span><span id="Ellipse-103"><a href="#Ellipse-103"><span class="linenos">103</span></a>    
</span><span id="Ellipse-104"><a href="#Ellipse-104"><span class="linenos">104</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-105"><a href="#Ellipse-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-106"><a href="#Ellipse-106"><span class="linenos">106</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-107"><a href="#Ellipse-107"><span class="linenos">107</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-108"><a href="#Ellipse-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">53</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span> <span class="o">+</span> <span class="p">(</span><span class="mi">717</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">35</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">269</span> <span class="o">*</span> <span class="n">a</span> <span class="o">**</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">667</span> <span class="o">*</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span> <span class="o">+</span> <span class="mi">371</span> <span class="o">*</span> <span class="n">b</span> <span class="o">**</span> <span class="mi">2</span><span class="p">))</span>
</span><span id="Ellipse-109"><a href="#Ellipse-109"><span class="linenos">109</span></a>    
</span><span id="Ellipse-110"><a href="#Ellipse-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-111"><a href="#Ellipse-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__ramanujan_1__and__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-112"><a href="#Ellipse-112"><span class="linenos">112</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-113"><a href="#Ellipse-113"><span class="linenos">113</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse-114"><a href="#Ellipse-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">2.4</span><span class="p">:</span>
</span><span id="Ellipse-115"><a href="#Ellipse-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__precise</span>
</span><span id="Ellipse-116"><a href="#Ellipse-116"><span class="linenos">116</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse-117"><a href="#Ellipse-117"><span class="linenos">117</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__ramanujan_1</span>
</span><span id="Ellipse-118"><a href="#Ellipse-118"><span class="linenos">118</span></a>    
</span><span id="Ellipse-119"><a href="#Ellipse-119"><span class="linenos">119</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse-120"><a href="#Ellipse-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse-121"><a href="#Ellipse-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="mi">10</span> <span class="o">+</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">4</span> <span class="o">-</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)))</span>
</span><span id="Ellipse-122"><a href="#Ellipse-122"><span class="linenos">122</span></a>    
</span><span id="Ellipse-123"><a href="#Ellipse-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__time_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">desired_approximation_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">return_iterations_num</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="Ellipse-124"><a href="#Ellipse-124"><span class="linenos">124</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="Ellipse-125"><a href="#Ellipse-125"><span class="linenos">125</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="Ellipse-126"><a href="#Ellipse-126"><span class="linenos">126</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Ellipse-127"><a href="#Ellipse-127"><span class="linenos">127</span></a>        <span class="n">tr</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">desired_approximation_time</span><span class="p">)</span>
</span><span id="Ellipse-128"><a href="#Ellipse-128"><span class="linenos">128</span></a>        <span class="k">while</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="Ellipse-129"><a href="#Ellipse-129"><span class="linenos">129</span></a>            <span class="n">i</span> <span class="o">=</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="Ellipse-130"><a href="#Ellipse-130"><span class="linenos">130</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="Ellipse-131"><a href="#Ellipse-131"><span class="linenos">131</span></a>
</span><span id="Ellipse-132"><a href="#Ellipse-132"><span class="linenos">132</span></a>        <span class="k">if</span> <span class="n">return_iterations_num</span><span class="p">:</span>
</span><span id="Ellipse-133"><a href="#Ellipse-133"><span class="linenos">133</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span><span class="p">,</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="Ellipse-134"><a href="#Ellipse-134"><span class="linenos">134</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse-135"><a href="#Ellipse-135"><span class="linenos">135</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span><span id="Ellipse-136"><a href="#Ellipse-136"><span class="linenos">136</span></a>    
</span><span id="Ellipse-137"><a href="#Ellipse-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__iter_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterations_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="Ellipse-138"><a href="#Ellipse-138"><span class="linenos">138</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="Ellipse-139"><a href="#Ellipse-139"><span class="linenos">139</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="Ellipse-140"><a href="#Ellipse-140"><span class="linenos">140</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Ellipse-141"><a href="#Ellipse-141"><span class="linenos">141</span></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">iterations_num</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="Ellipse-142"><a href="#Ellipse-142"><span class="linenos">142</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="Ellipse-143"><a href="#Ellipse-143"><span class="linenos">143</span></a>
</span><span id="Ellipse-144"><a href="#Ellipse-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span><span id="Ellipse-145"><a href="#Ellipse-145"><span class="linenos">145</span></a>    
</span><span id="Ellipse-146"><a href="#Ellipse-146"><span class="linenos">146</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Ellipse-147"><a href="#Ellipse-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">from_r1_r2</span><span class="p">(</span><span class="n">r1</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">r2</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="Ellipse-148"><a href="#Ellipse-148"><span class="linenos">148</span></a>        <span class="k">return</span> <span class="n">Ellipse</span><span class="p">((</span><span class="n">r1</span> <span class="o">+</span> <span class="n">r2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p><a href="https://www.youtube.com/watch?v=5nW3nJhBHL0">https://www.youtube.com/watch?v=5nW3nJhBHL0</a>
<a href="http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html">http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html</a></p>
</div>


                            <div id="Ellipse.__init__" class="classattr">
                                        <input id="Ellipse.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">Ellipse</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">a</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span>, </span><span class="param"><span class="n">b</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span></span>)</span>

                <label class="view-source-button" for="Ellipse.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.__init__-45"><a href="#Ellipse.__init__-45"><span class="linenos">45</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">a</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">b</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="Ellipse.__init__-46"><a href="#Ellipse.__init__-46"><span class="linenos">46</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">=</span> <span class="n">a</span>
</span><span id="Ellipse.__init__-47"><a href="#Ellipse.__init__-47"><span class="linenos">47</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">=</span> <span class="n">b</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.a" class="classattr">
                                <div class="attr variable">
            <span class="name">a</span>

        
    </div>
    <a class="headerlink" href="#Ellipse.a"></a>
    
    

                            </div>
                            <div id="Ellipse.b" class="classattr">
                                <div class="attr variable">
            <span class="name">b</span>

        
    </div>
    <a class="headerlink" href="#Ellipse.b"></a>
    
    

                            </div>
                            <div id="Ellipse.y" class="classattr">
                                        <input id="Ellipse.y-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">y</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">x</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="Ellipse.y-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.y"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.y-49"><a href="#Ellipse.y-49"><span class="linenos">49</span></a>    <span class="k">def</span> <span class="nf">y</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">RationalNumber</span><span class="p">:</span>
</span><span id="Ellipse.y-50"><a href="#Ellipse.y-50"><span class="linenos">50</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="n">x</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.area" class="classattr">
                                        <input id="Ellipse.area-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">area</span>

                <label class="view-source-button" for="Ellipse.area-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.area"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.area-52"><a href="#Ellipse.area-52"><span class="linenos">52</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.area-53"><a href="#Ellipse.area-53"><span class="linenos">53</span></a>    <span class="k">def</span> <span class="nf">area</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.area-54"><a href="#Ellipse.area-54"><span class="linenos">54</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.h" class="classattr">
                                        <input id="Ellipse.h-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">h</span>

                <label class="view-source-button" for="Ellipse.h-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.h"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.h-56"><a href="#Ellipse.h-56"><span class="linenos">56</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.h-57"><a href="#Ellipse.h-57"><span class="linenos">57</span></a>    <span class="k">def</span> <span class="nf">h</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.h-58"><a href="#Ellipse.h-58"><span class="linenos">58</span></a>        <span class="k">return</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.e" class="classattr">
                                        <input id="Ellipse.e-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">e</span>

                <label class="view-source-button" for="Ellipse.e-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.e"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.e-60"><a href="#Ellipse.e-60"><span class="linenos">60</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.e-61"><a href="#Ellipse.e-61"><span class="linenos">61</span></a>    <span class="k">def</span> <span class="nf">e</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.e-62"><a href="#Ellipse.e-62"><span class="linenos">62</span></a>        <span class="k">return</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.c" class="classattr">
                                        <input id="Ellipse.c-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">c</span>

                <label class="view-source-button" for="Ellipse.c-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.c"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.c-64"><a href="#Ellipse.c-64"><span class="linenos">64</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.c-65"><a href="#Ellipse.c-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="nf">c</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.c-66"><a href="#Ellipse.c-66"><span class="linenos">66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__kepler" class="classattr">
                                        <input id="Ellipse.perimeter__kepler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__kepler</span>

                <label class="view-source-button" for="Ellipse.perimeter__kepler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__kepler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__kepler-68"><a href="#Ellipse.perimeter__kepler-68"><span class="linenos">68</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__kepler-69"><a href="#Ellipse.perimeter__kepler-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">perimeter__kepler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__kepler-70"><a href="#Ellipse.perimeter__kepler-70"><span class="linenos">70</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__naive" class="classattr">
                                        <input id="Ellipse.perimeter__naive-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__naive</span>

                <label class="view-source-button" for="Ellipse.perimeter__naive-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__naive"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__naive-72"><a href="#Ellipse.perimeter__naive-72"><span class="linenos">72</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__naive-73"><a href="#Ellipse.perimeter__naive-73"><span class="linenos">73</span></a>    <span class="k">def</span> <span class="nf">perimeter__naive</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__naive-74"><a href="#Ellipse.perimeter__naive-74"><span class="linenos">74</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__euler" class="classattr">
                                        <input id="Ellipse.perimeter__euler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__euler</span>

                <label class="view-source-button" for="Ellipse.perimeter__euler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__euler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__euler-76"><a href="#Ellipse.perimeter__euler-76"><span class="linenos">76</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__euler-77"><a href="#Ellipse.perimeter__euler-77"><span class="linenos">77</span></a>    <span class="k">def</span> <span class="nf">perimeter__euler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__euler-78"><a href="#Ellipse.perimeter__euler-78"><span class="linenos">78</span></a>        <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">pi</span> <span class="o">*</span> <span class="n">sqrt</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__matt_parker__lazy" class="classattr">
                                        <input id="Ellipse.perimeter__matt_parker__lazy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__matt_parker__lazy</span>

                <label class="view-source-button" for="Ellipse.perimeter__matt_parker__lazy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__matt_parker__lazy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__matt_parker__lazy-80"><a href="#Ellipse.perimeter__matt_parker__lazy-80"><span class="linenos">80</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-81"><a href="#Ellipse.perimeter__matt_parker__lazy-81"><span class="linenos">81</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-82"><a href="#Ellipse.perimeter__matt_parker__lazy-82"><span class="linenos">82</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Computationly efficient. Not more that 6.1% deviation (less than 5% for `1 / 75` ellipses)</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-83"><a href="#Ellipse.perimeter__matt_parker__lazy-83"><span class="linenos">83</span></a>
</span><span id="Ellipse.perimeter__matt_parker__lazy-84"><a href="#Ellipse.perimeter__matt_parker__lazy-84"><span class="linenos">84</span></a><span class="sd">        Returns:</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-85"><a href="#Ellipse.perimeter__matt_parker__lazy-85"><span class="linenos">85</span></a><span class="sd">            _type_: _description_</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-86"><a href="#Ellipse.perimeter__matt_parker__lazy-86"><span class="linenos">86</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-87"><a href="#Ellipse.perimeter__matt_parker__lazy-87"><span class="linenos">87</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-88"><a href="#Ellipse.perimeter__matt_parker__lazy-88"><span class="linenos">88</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__matt_parker__lazy-89"><a href="#Ellipse.perimeter__matt_parker__lazy-89"><span class="linenos">89</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">6</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">5</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">4</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Computationly efficient. Not more that 6.1% deviation (less than 5% for <code>1 / 75</code> ellipses)</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy" class="classattr">
                                        <input id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__best_of__euler__and__matt_parker__lazy</span>

                <label class="view-source-button" for="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-91"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-91"><span class="linenos">91</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-92"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__euler__and__matt_parker__lazy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-93"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-93"><span class="linenos">93</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-94"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-94"><span class="linenos">94</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-95"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-95"><span class="linenos">95</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">0.8</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-96"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-96"><span class="linenos">96</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__lazy</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-97"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-97"><span class="linenos">97</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-98"><a href="#Ellipse.perimeter__best_of__euler__and__matt_parker__lazy-98"><span class="linenos">98</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__euler</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__ramanujan_1" class="classattr">
                                        <input id="Ellipse.perimeter__ramanujan_1-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__ramanujan_1</span>

                <label class="view-source-button" for="Ellipse.perimeter__ramanujan_1-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__ramanujan_1"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__ramanujan_1-100"><a href="#Ellipse.perimeter__ramanujan_1-100"><span class="linenos">100</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__ramanujan_1-101"><a href="#Ellipse.perimeter__ramanujan_1-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_1</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__ramanujan_1-102"><a href="#Ellipse.perimeter__ramanujan_1-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">((</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)))</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__matt_parker__precise" class="classattr">
                                        <input id="Ellipse.perimeter__matt_parker__precise-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__matt_parker__precise</span>

                <label class="view-source-button" for="Ellipse.perimeter__matt_parker__precise-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__matt_parker__precise"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__matt_parker__precise-104"><a href="#Ellipse.perimeter__matt_parker__precise-104"><span class="linenos">104</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__matt_parker__precise-105"><a href="#Ellipse.perimeter__matt_parker__precise-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">perimeter__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__matt_parker__precise-106"><a href="#Ellipse.perimeter__matt_parker__precise-106"><span class="linenos">106</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__matt_parker__precise-107"><a href="#Ellipse.perimeter__matt_parker__precise-107"><span class="linenos">107</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__matt_parker__precise-108"><a href="#Ellipse.perimeter__matt_parker__precise-108"><span class="linenos">108</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">((</span><span class="mi">53</span> <span class="o">*</span> <span class="n">a</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span> <span class="o">+</span> <span class="p">(</span><span class="mi">717</span> <span class="o">*</span> <span class="n">b</span><span class="p">)</span> <span class="o">/</span> <span class="mi">35</span> <span class="o">-</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">269</span> <span class="o">*</span> <span class="n">a</span> <span class="o">**</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">667</span> <span class="o">*</span> <span class="n">a</span> <span class="o">*</span> <span class="n">b</span> <span class="o">+</span> <span class="mi">371</span> <span class="o">*</span> <span class="n">b</span> <span class="o">**</span> <span class="mi">2</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise" class="classattr">
                                        <input id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__best_of__ramanujan_1__and__matt_parker__precise</span>

                <label class="view-source-button" for="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-110"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-110"><span class="linenos">110</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-111"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">perimeter__best_of__ramanujan_1__and__matt_parker__precise</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-112"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-112"><span class="linenos">112</span></a>        <span class="n">a</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-113"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-113"><span class="linenos">113</span></a>        <span class="n">b</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-114"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">a</span> <span class="o">/</span> <span class="n">b</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mf">2.4</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-115"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-115"><span class="linenos">115</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__matt_parker__precise</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-116"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-116"><span class="linenos">116</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-117"><a href="#Ellipse.perimeter__best_of__ramanujan_1__and__matt_parker__precise-117"><span class="linenos">117</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">perimeter__ramanujan_1</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__ramanujan_2" class="classattr">
                                        <input id="Ellipse.perimeter__ramanujan_2-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">perimeter__ramanujan_2</span>

                <label class="view-source-button" for="Ellipse.perimeter__ramanujan_2-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__ramanujan_2"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__ramanujan_2-119"><a href="#Ellipse.perimeter__ramanujan_2-119"><span class="linenos">119</span></a>    <span class="nd">@property</span>
</span><span id="Ellipse.perimeter__ramanujan_2-120"><a href="#Ellipse.perimeter__ramanujan_2-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">perimeter__ramanujan_2</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__ramanujan_2-121"><a href="#Ellipse.perimeter__ramanujan_2-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="n">pi</span> <span class="o">*</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">b</span><span class="p">)</span> <span class="o">*</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="p">(</span><span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="mi">10</span> <span class="o">+</span> <span class="n">sqrt</span><span class="p">(</span><span class="mi">4</span> <span class="o">-</span> <span class="mi">3</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">h</span><span class="p">)))</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__infinite_sum__time_lim" class="classattr">
                                        <input id="Ellipse.perimeter__infinite_sum__time_lim-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">perimeter__infinite_sum__time_lim</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">desired_approximation_time</span><span class="p">:</span> <span class="nb">float</span>,</span><span class="param">	<span class="n">return_iterations_num</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Ellipse.perimeter__infinite_sum__time_lim-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__infinite_sum__time_lim"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__infinite_sum__time_lim-123"><a href="#Ellipse.perimeter__infinite_sum__time_lim-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__time_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">desired_approximation_time</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="n">return_iterations_num</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-124"><a href="#Ellipse.perimeter__infinite_sum__time_lim-124"><span class="linenos">124</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-125"><a href="#Ellipse.perimeter__infinite_sum__time_lim-125"><span class="linenos">125</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-126"><a href="#Ellipse.perimeter__infinite_sum__time_lim-126"><span class="linenos">126</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-127"><a href="#Ellipse.perimeter__infinite_sum__time_lim-127"><span class="linenos">127</span></a>        <span class="n">tr</span> <span class="o">=</span> <span class="n">Tracer</span><span class="p">(</span><span class="n">desired_approximation_time</span><span class="p">)</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-128"><a href="#Ellipse.perimeter__infinite_sum__time_lim-128"><span class="linenos">128</span></a>        <span class="k">while</span> <span class="n">tr</span><span class="o">.</span><span class="n">iter</span><span class="p">():</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-129"><a href="#Ellipse.perimeter__infinite_sum__time_lim-129"><span class="linenos">129</span></a>            <span class="n">i</span> <span class="o">=</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-130"><a href="#Ellipse.perimeter__infinite_sum__time_lim-130"><span class="linenos">130</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-131"><a href="#Ellipse.perimeter__infinite_sum__time_lim-131"><span class="linenos">131</span></a>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-132"><a href="#Ellipse.perimeter__infinite_sum__time_lim-132"><span class="linenos">132</span></a>        <span class="k">if</span> <span class="n">return_iterations_num</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-133"><a href="#Ellipse.perimeter__infinite_sum__time_lim-133"><span class="linenos">133</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span><span class="p">,</span> <span class="n">tr</span><span class="o">.</span><span class="n">total_number_of_iterations_made</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-134"><a href="#Ellipse.perimeter__infinite_sum__time_lim-134"><span class="linenos">134</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="Ellipse.perimeter__infinite_sum__time_lim-135"><a href="#Ellipse.perimeter__infinite_sum__time_lim-135"><span class="linenos">135</span></a>            <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.perimeter__infinite_sum__iter_lim" class="classattr">
                                        <input id="Ellipse.perimeter__infinite_sum__iter_lim-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">perimeter__infinite_sum__iter_lim</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">iterations_num</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Ellipse.perimeter__infinite_sum__iter_lim-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.perimeter__infinite_sum__iter_lim"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.perimeter__infinite_sum__iter_lim-137"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">perimeter__infinite_sum__iter_lim</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">iterations_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-138"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-138"><span class="linenos">138</span></a>        <span class="n">e</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">e</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-139"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-139"><span class="linenos">139</span></a>        <span class="n">first_multiplier</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">a</span> <span class="o">*</span> <span class="n">pi</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-140"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-140"><span class="linenos">140</span></a>        <span class="n">second_multiplier</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-141"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-141"><span class="linenos">141</span></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">iterations_num</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-142"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-142"><span class="linenos">142</span></a>            <span class="n">second_multiplier</span> <span class="o">-=</span> <span class="p">((</span><span class="n">factorial</span><span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">/</span> <span class="p">((</span><span class="mi">2</span> <span class="o">**</span> <span class="n">i</span> <span class="o">*</span> <span class="n">factorial</span><span class="p">(</span><span class="n">i</span><span class="p">))</span> <span class="o">**</span> <span class="mi">4</span><span class="p">))</span> <span class="o">*</span> <span class="p">((</span><span class="n">e</span> <span class="o">**</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span><span class="p">))</span> <span class="o">/</span> <span class="p">(</span><span class="mi">2</span> <span class="o">*</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-143"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-143"><span class="linenos">143</span></a>
</span><span id="Ellipse.perimeter__infinite_sum__iter_lim-144"><a href="#Ellipse.perimeter__infinite_sum__iter_lim-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="n">first_multiplier</span> <span class="o">*</span> <span class="n">second_multiplier</span>
</span></pre></div>


    

                            </div>
                            <div id="Ellipse.from_r1_r2" class="classattr">
                                        <input id="Ellipse.from_r1_r2-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@staticmethod</div>

        <span class="def">def</span>
        <span class="name">from_r1_r2</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">r1</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span>, </span><span class="param"><span class="n">r2</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="Ellipse.from_r1_r2-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#Ellipse.from_r1_r2"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="Ellipse.from_r1_r2-146"><a href="#Ellipse.from_r1_r2-146"><span class="linenos">146</span></a>    <span class="nd">@staticmethod</span>
</span><span id="Ellipse.from_r1_r2-147"><a href="#Ellipse.from_r1_r2-147"><span class="linenos">147</span></a>    <span class="k">def</span> <span class="nf">from_r1_r2</span><span class="p">(</span><span class="n">r1</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">,</span> <span class="n">r2</span><span class="p">:</span> <span class="n">RationalNumber</span><span class="p">):</span>
</span><span id="Ellipse.from_r1_r2-148"><a href="#Ellipse.from_r1_r2-148"><span class="linenos">148</span></a>        <span class="k">return</span> <span class="n">Ellipse</span><span class="p">((</span><span class="n">r1</span> <span class="o">+</span> <span class="n">r2</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>