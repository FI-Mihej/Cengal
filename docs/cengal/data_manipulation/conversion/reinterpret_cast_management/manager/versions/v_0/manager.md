---
title: manager
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.data_manipulation<wbr>.conversion<wbr>.reinterpret_cast_management<wbr>.manager<wbr>.versions<wbr>.v_0<wbr>.manager    </h1>

                
                        <input id="mod-manager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-manager-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;AutoDerivedClass&#39;</span><span class="p">,</span> <span class="s1">&#39;BaseAutoDerivedObjWrapper&#39;</span><span class="p">,</span> <span class="s1">&#39;ClassWrappingFactory&#39;</span><span class="p">,</span> <span class="s1">&#39;ClassWrappingFactoryWithObjDataSizeLog&#39;</span><span class="p">]</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="sd">Module Docstring</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>
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
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="n">getsizeof</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="kn">from</span> <span class="nn">cengal.data_generation.id_generator</span> <span class="kn">import</span> <span class="n">IDGenerator</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.conversion.reinterpret_cast</span> <span class="kn">import</span> <span class="n">TemporaryReinterpretCast</span><span class="p">,</span> <span class="n">reinterpret_cast</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="kn">from</span> <span class="nn">cengal.entities.copyable</span> <span class="kn">import</span> <span class="n">copy__impl</span><span class="p">,</span> <span class="n">deepcopy__impl</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">FrozenSet</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Optional</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">Error</span> <span class="k">as</span> <span class="n">CopyError</span><span class="p">,</span> <span class="n">copy</span><span class="p">,</span> <span class="n">deepcopy</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="kn">from</span> <span class="nn">socket</span> <span class="kn">import</span> <span class="n">SocketIO</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="k">class</span> <span class="nc">AutoDerivedClass</span><span class="p">:</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="nd">@property</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>    
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">):</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_classes</span><span class="p">(</span><span class="n">base_type</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">methods</span><span class="p">)</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="k">class</span> <span class="nc">BaseAutoDerivedObjWrapper</span><span class="p">:</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">def</span> <span class="nf">wrapping_required</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>            <span class="k">pass</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">def</span> <span class="nf">type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="n">base_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>            <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_fields_tuple</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>            <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">wrapping_required</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">,</span> <span class="n">planned_type_name</span><span class="p">):</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>                <span class="n">result</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">planned_type_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_classes</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">methods</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">))</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>                <span class="k">return</span> <span class="n">base_type</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="n">obj</span><span class="o">.</span><span class="vm">__class__</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="k">return</span> <span class="n">obj</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">temporary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="n">TemporaryReinterpretCast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">persistent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="k">return</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="c1"># class ClassWrapper:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="c1">#     def __init__(self, auto_derived_types: AutoDerivedTyped) -&gt; None:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="c1">#         self._class_wrapper__data_size: int = 0</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="c1">#         self._class_wrapper__auto_derived_types: AutoDerivedTyped = auto_derived_types</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="c1">#     def __call__(self, *args: Any, **kwds: Any) -&gt; Any:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="c1">#         pass</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="k">class</span> <span class="nc">ClassWrappingFactory</span><span class="p">:</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_attributes_and_methods</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>            <span class="s1">&#39;_class_wrapper__field_names&#39;</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>            <span class="s1">&#39;_class_wrapper__factory&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="p">}</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="nd">@property</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">attributes_and_methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_attributes_and_methods</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="sd">        Args:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="sd">        Returns:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">            Dict[str, Any]: _description_</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="k">def</span> <span class="nf">gen_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="sd">        Args:</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">        Returns:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">            Optional[Dict[str, Any]]: _description_</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="n">base_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>            <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_fields_tuple</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>            
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>            <span class="n">attributes_and_methods</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">attributes_and_methods</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>            <span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__field_names&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">field_names</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>            <span class="n">attributes_and_methods</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">edit_derived_type</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">)</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>            <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_kwargs</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">)</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>            
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>            <span class="k">if</span> <span class="n">kwargs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>                <span class="n">derived</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,),</span> <span class="n">attributes_and_methods</span><span class="p">)</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>                <span class="n">derived</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,),</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">derived</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="k">return</span> <span class="n">derived</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>            <span class="k">pass</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="k">pass</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a><span class="k">class</span> <span class="nc">ClassWrappingFactoryWithObjDataSizeLog</span><span class="p">(</span><span class="n">ClassWrappingFactory</span><span class="p">):</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__obj_data_size_log&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">data_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">field_names</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="n">data_size</span> <span class="o">+=</span> <span class="n">getsizeof</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">field_name</span><span class="p">))</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__obj_data_size_log&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_size</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span></pre></div>


            </section>
                <section id="AutoDerivedClass">
                            <input id="AutoDerivedClass-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AutoDerivedClass</span>:

                <label class="view-source-button" for="AutoDerivedClass-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AutoDerivedClass"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AutoDerivedClass-50"><a href="#AutoDerivedClass-50"><span class="linenos">50</span></a><span class="k">class</span> <span class="nc">AutoDerivedClass</span><span class="p">:</span>
</span><span id="AutoDerivedClass-51"><a href="#AutoDerivedClass-51"><span class="linenos">51</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="AutoDerivedClass-52"><a href="#AutoDerivedClass-52"><span class="linenos">52</span></a>
</span><span id="AutoDerivedClass-53"><a href="#AutoDerivedClass-53"><span class="linenos">53</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="AutoDerivedClass-54"><a href="#AutoDerivedClass-54"><span class="linenos">54</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="AutoDerivedClass-55"><a href="#AutoDerivedClass-55"><span class="linenos">55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="AutoDerivedClass-56"><a href="#AutoDerivedClass-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="AutoDerivedClass-57"><a href="#AutoDerivedClass-57"><span class="linenos">57</span></a>    
</span><span id="AutoDerivedClass-58"><a href="#AutoDerivedClass-58"><span class="linenos">58</span></a>    <span class="nd">@property</span>
</span><span id="AutoDerivedClass-59"><a href="#AutoDerivedClass-59"><span class="linenos">59</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="AutoDerivedClass-60"><a href="#AutoDerivedClass-60"><span class="linenos">60</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="AutoDerivedClass-61"><a href="#AutoDerivedClass-61"><span class="linenos">61</span></a>    
</span><span id="AutoDerivedClass-62"><a href="#AutoDerivedClass-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="AutoDerivedClass-63"><a href="#AutoDerivedClass-63"><span class="linenos">63</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span><span id="AutoDerivedClass-64"><a href="#AutoDerivedClass-64"><span class="linenos">64</span></a>    
</span><span id="AutoDerivedClass-65"><a href="#AutoDerivedClass-65"><span class="linenos">65</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">):</span>
</span><span id="AutoDerivedClass-66"><a href="#AutoDerivedClass-66"><span class="linenos">66</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="AutoDerivedClass-67"><a href="#AutoDerivedClass-67"><span class="linenos">67</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="AutoDerivedClass-68"><a href="#AutoDerivedClass-68"><span class="linenos">68</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="AutoDerivedClass-69"><a href="#AutoDerivedClass-69"><span class="linenos">69</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="AutoDerivedClass-70"><a href="#AutoDerivedClass-70"><span class="linenos">70</span></a>            <span class="n">result</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_classes</span><span class="p">(</span><span class="n">base_type</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">methods</span><span class="p">)</span>
</span><span id="AutoDerivedClass-71"><a href="#AutoDerivedClass-71"><span class="linenos">71</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="AutoDerivedClass-72"><a href="#AutoDerivedClass-72"><span class="linenos">72</span></a>            <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="AutoDerivedClass.instance_id" class="classattr">
                                <div class="attr variable">
            <span class="name">instance_id</span>        =
<input id="AutoDerivedClass.instance_id-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="AutoDerivedClass.instance_id-view-value"></label><span class="default_value">&lt;cengal.data_generation.id_generator.versions.v_1.compilable.id_generator__cython.IDGeneratorInt object&gt;</span>

        
    </div>
    <a class="headerlink" href="#AutoDerivedClass.instance_id"></a>
    
    

                            </div>
                            <div id="AutoDerivedClass.class_name" class="classattr">
                                <div class="attr variable">
            <span class="name">class_name</span>

        
    </div>
    <a class="headerlink" href="#AutoDerivedClass.class_name"></a>
    
    

                            </div>
                            <div id="AutoDerivedClass.derived" class="classattr">
                                <div class="attr variable">
            <span class="name">derived</span><span class="annotation">: Dict[Type, Type]</span>

        
    </div>
    <a class="headerlink" href="#AutoDerivedClass.derived"></a>
    
    

                            </div>
                            <div id="AutoDerivedClass.methods" class="classattr">
                                        <input id="AutoDerivedClass.methods-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">methods</span><span class="annotation">: Dict[str, Callable]</span>

                <label class="view-source-button" for="AutoDerivedClass.methods-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AutoDerivedClass.methods"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AutoDerivedClass.methods-58"><a href="#AutoDerivedClass.methods-58"><span class="linenos">58</span></a>    <span class="nd">@property</span>
</span><span id="AutoDerivedClass.methods-59"><a href="#AutoDerivedClass.methods-59"><span class="linenos">59</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="AutoDerivedClass.methods-60"><a href="#AutoDerivedClass.methods-60"><span class="linenos">60</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="AutoDerivedClass.base_classes" class="classattr">
                                        <input id="AutoDerivedClass.base_classes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">base_classes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">base_type</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="AutoDerivedClass.base_classes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AutoDerivedClass.base_classes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AutoDerivedClass.base_classes-62"><a href="#AutoDerivedClass.base_classes-62"><span class="linenos">62</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="AutoDerivedClass.base_classes-63"><a href="#AutoDerivedClass.base_classes-63"><span class="linenos">63</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="BaseAutoDerivedObjWrapper">
                            <input id="BaseAutoDerivedObjWrapper-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">BaseAutoDerivedObjWrapper</span>:

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper-75"><a href="#BaseAutoDerivedObjWrapper-75"><span class="linenos"> 75</span></a><span class="k">class</span> <span class="nc">BaseAutoDerivedObjWrapper</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-76"><a href="#BaseAutoDerivedObjWrapper-76"><span class="linenos"> 76</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="BaseAutoDerivedObjWrapper-77"><a href="#BaseAutoDerivedObjWrapper-77"><span class="linenos"> 77</span></a>
</span><span id="BaseAutoDerivedObjWrapper-78"><a href="#BaseAutoDerivedObjWrapper-78"><span class="linenos"> 78</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-79"><a href="#BaseAutoDerivedObjWrapper-79"><span class="linenos"> 79</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="BaseAutoDerivedObjWrapper-80"><a href="#BaseAutoDerivedObjWrapper-80"><span class="linenos"> 80</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="BaseAutoDerivedObjWrapper-81"><a href="#BaseAutoDerivedObjWrapper-81"><span class="linenos"> 81</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="BaseAutoDerivedObjWrapper-82"><a href="#BaseAutoDerivedObjWrapper-82"><span class="linenos"> 82</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span>
</span><span id="BaseAutoDerivedObjWrapper-83"><a href="#BaseAutoDerivedObjWrapper-83"><span class="linenos"> 83</span></a>    
</span><span id="BaseAutoDerivedObjWrapper-84"><a href="#BaseAutoDerivedObjWrapper-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="nf">wrapping_required</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-85"><a href="#BaseAutoDerivedObjWrapper-85"><span class="linenos"> 85</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="BaseAutoDerivedObjWrapper-86"><a href="#BaseAutoDerivedObjWrapper-86"><span class="linenos"> 86</span></a>    
</span><span id="BaseAutoDerivedObjWrapper-87"><a href="#BaseAutoDerivedObjWrapper-87"><span class="linenos"> 87</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="BaseAutoDerivedObjWrapper-88"><a href="#BaseAutoDerivedObjWrapper-88"><span class="linenos"> 88</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="BaseAutoDerivedObjWrapper-89"><a href="#BaseAutoDerivedObjWrapper-89"><span class="linenos"> 89</span></a>
</span><span id="BaseAutoDerivedObjWrapper-90"><a href="#BaseAutoDerivedObjWrapper-90"><span class="linenos"> 90</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="BaseAutoDerivedObjWrapper-91"><a href="#BaseAutoDerivedObjWrapper-91"><span class="linenos"> 91</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span><span id="BaseAutoDerivedObjWrapper-92"><a href="#BaseAutoDerivedObjWrapper-92"><span class="linenos"> 92</span></a>    
</span><span id="BaseAutoDerivedObjWrapper-93"><a href="#BaseAutoDerivedObjWrapper-93"><span class="linenos"> 93</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-94"><a href="#BaseAutoDerivedObjWrapper-94"><span class="linenos"> 94</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-95"><a href="#BaseAutoDerivedObjWrapper-95"><span class="linenos"> 95</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="BaseAutoDerivedObjWrapper-96"><a href="#BaseAutoDerivedObjWrapper-96"><span class="linenos"> 96</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-97"><a href="#BaseAutoDerivedObjWrapper-97"><span class="linenos"> 97</span></a>            <span class="k">pass</span>
</span><span id="BaseAutoDerivedObjWrapper-98"><a href="#BaseAutoDerivedObjWrapper-98"><span class="linenos"> 98</span></a>
</span><span id="BaseAutoDerivedObjWrapper-99"><a href="#BaseAutoDerivedObjWrapper-99"><span class="linenos"> 99</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="BaseAutoDerivedObjWrapper-100"><a href="#BaseAutoDerivedObjWrapper-100"><span class="linenos">100</span></a>    
</span><span id="BaseAutoDerivedObjWrapper-101"><a href="#BaseAutoDerivedObjWrapper-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-102"><a href="#BaseAutoDerivedObjWrapper-102"><span class="linenos">102</span></a>        <span class="n">base_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper-103"><a href="#BaseAutoDerivedObjWrapper-103"><span class="linenos">103</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="BaseAutoDerivedObjWrapper-104"><a href="#BaseAutoDerivedObjWrapper-104"><span class="linenos">104</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-105"><a href="#BaseAutoDerivedObjWrapper-105"><span class="linenos">105</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="BaseAutoDerivedObjWrapper-106"><a href="#BaseAutoDerivedObjWrapper-106"><span class="linenos">106</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-107"><a href="#BaseAutoDerivedObjWrapper-107"><span class="linenos">107</span></a>            <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_fields_tuple</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper-108"><a href="#BaseAutoDerivedObjWrapper-108"><span class="linenos">108</span></a>            <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="BaseAutoDerivedObjWrapper-109"><a href="#BaseAutoDerivedObjWrapper-109"><span class="linenos">109</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">wrapping_required</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">,</span> <span class="n">planned_type_name</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-110"><a href="#BaseAutoDerivedObjWrapper-110"><span class="linenos">110</span></a>                <span class="n">result</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">planned_type_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_classes</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">methods</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">))</span>
</span><span id="BaseAutoDerivedObjWrapper-111"><a href="#BaseAutoDerivedObjWrapper-111"><span class="linenos">111</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="BaseAutoDerivedObjWrapper-112"><a href="#BaseAutoDerivedObjWrapper-112"><span class="linenos">112</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="BaseAutoDerivedObjWrapper-113"><a href="#BaseAutoDerivedObjWrapper-113"><span class="linenos">113</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper-114"><a href="#BaseAutoDerivedObjWrapper-114"><span class="linenos">114</span></a>                <span class="k">return</span> <span class="n">base_type</span>
</span><span id="BaseAutoDerivedObjWrapper-115"><a href="#BaseAutoDerivedObjWrapper-115"><span class="linenos">115</span></a>    
</span><span id="BaseAutoDerivedObjWrapper-116"><a href="#BaseAutoDerivedObjWrapper-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-117"><a href="#BaseAutoDerivedObjWrapper-117"><span class="linenos">117</span></a>        <span class="n">obj</span><span class="o">.</span><span class="vm">__class__</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper-118"><a href="#BaseAutoDerivedObjWrapper-118"><span class="linenos">118</span></a>        <span class="k">return</span> <span class="n">obj</span>
</span><span id="BaseAutoDerivedObjWrapper-119"><a href="#BaseAutoDerivedObjWrapper-119"><span class="linenos">119</span></a>
</span><span id="BaseAutoDerivedObjWrapper-120"><a href="#BaseAutoDerivedObjWrapper-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">temporary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-121"><a href="#BaseAutoDerivedObjWrapper-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="n">TemporaryReinterpretCast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper-122"><a href="#BaseAutoDerivedObjWrapper-122"><span class="linenos">122</span></a>
</span><span id="BaseAutoDerivedObjWrapper-123"><a href="#BaseAutoDerivedObjWrapper-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">persistent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper-124"><a href="#BaseAutoDerivedObjWrapper-124"><span class="linenos">124</span></a>        <span class="k">return</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="BaseAutoDerivedObjWrapper.instance_id" class="classattr">
                                <div class="attr variable">
            <span class="name">instance_id</span>        =
<input id="BaseAutoDerivedObjWrapper.instance_id-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="BaseAutoDerivedObjWrapper.instance_id-view-value"></label><span class="default_value">&lt;cengal.data_generation.id_generator.versions.v_1.compilable.id_generator__cython.IDGeneratorInt object&gt;</span>

        
    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.instance_id"></a>
    
    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.class_name" class="classattr">
                                <div class="attr variable">
            <span class="name">class_name</span>

        
    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.class_name"></a>
    
    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.derived" class="classattr">
                                <div class="attr variable">
            <span class="name">derived</span><span class="annotation">: Dict[Type, Type]</span>

        
    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.derived"></a>
    
    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.t" class="classattr">
                                <div class="attr variable">
            <span class="name">t</span>

        
    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.t"></a>
    
    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.wrapping_required" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.wrapping_required-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">wrapping_required</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">base_type</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span>,</span><span class="param">	<span class="n">fields</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.wrapping_required-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.wrapping_required"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.wrapping_required-84"><a href="#BaseAutoDerivedObjWrapper.wrapping_required-84"><span class="linenos">84</span></a>    <span class="k">def</span> <span class="nf">wrapping_required</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.wrapping_required-85"><a href="#BaseAutoDerivedObjWrapper.wrapping_required-85"><span class="linenos">85</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.methods" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.methods-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">methods</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">base_type</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span>,</span><span class="param">	<span class="n">fields</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.methods-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.methods"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.methods-87"><a href="#BaseAutoDerivedObjWrapper.methods-87"><span class="linenos">87</span></a>    <span class="k">def</span> <span class="nf">methods</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="BaseAutoDerivedObjWrapper.methods-88"><a href="#BaseAutoDerivedObjWrapper.methods-88"><span class="linenos">88</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.base_classes" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.base_classes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">base_classes</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">base_type</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span>,</span><span class="param">	<span class="n">fields</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.base_classes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.base_classes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.base_classes-90"><a href="#BaseAutoDerivedObjWrapper.base_classes-90"><span class="linenos">90</span></a>    <span class="k">def</span> <span class="nf">base_classes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">base_type</span><span class="p">:</span> <span class="n">Type</span><span class="p">,</span> <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="BaseAutoDerivedObjWrapper.base_classes-91"><a href="#BaseAutoDerivedObjWrapper.base_classes-91"><span class="linenos">91</span></a>        <span class="k">return</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,)</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.gen_fields_tuple" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.gen_fields_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gen_fields_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.gen_fields_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.gen_fields_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-93"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-93"><span class="linenos">93</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-94"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-94"><span class="linenos">94</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-95"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-95"><span class="linenos">95</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-96"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-96"><span class="linenos">96</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-97"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-97"><span class="linenos">97</span></a>            <span class="k">pass</span>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-98"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-98"><span class="linenos">98</span></a>
</span><span id="BaseAutoDerivedObjWrapper.gen_fields_tuple-99"><a href="#BaseAutoDerivedObjWrapper.gen_fields_tuple-99"><span class="linenos">99</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.type" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.type-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">type</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.type-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.type"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.type-101"><a href="#BaseAutoDerivedObjWrapper.type-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper.type-102"><a href="#BaseAutoDerivedObjWrapper.type-102"><span class="linenos">102</span></a>        <span class="n">base_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper.type-103"><a href="#BaseAutoDerivedObjWrapper.type-103"><span class="linenos">103</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="BaseAutoDerivedObjWrapper.type-104"><a href="#BaseAutoDerivedObjWrapper.type-104"><span class="linenos">104</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.type-105"><a href="#BaseAutoDerivedObjWrapper.type-105"><span class="linenos">105</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="BaseAutoDerivedObjWrapper.type-106"><a href="#BaseAutoDerivedObjWrapper.type-106"><span class="linenos">106</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.type-107"><a href="#BaseAutoDerivedObjWrapper.type-107"><span class="linenos">107</span></a>            <span class="n">fields</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_fields_tuple</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="BaseAutoDerivedObjWrapper.type-108"><a href="#BaseAutoDerivedObjWrapper.type-108"><span class="linenos">108</span></a>            <span class="n">planned_type_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="BaseAutoDerivedObjWrapper.type-109"><a href="#BaseAutoDerivedObjWrapper.type-109"><span class="linenos">109</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">wrapping_required</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">,</span> <span class="n">planned_type_name</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper.type-110"><a href="#BaseAutoDerivedObjWrapper.type-110"><span class="linenos">110</span></a>                <span class="n">result</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">planned_type_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_classes</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">methods</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">base_type</span><span class="p">,</span> <span class="n">fields</span><span class="p">))</span>
</span><span id="BaseAutoDerivedObjWrapper.type-111"><a href="#BaseAutoDerivedObjWrapper.type-111"><span class="linenos">111</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="BaseAutoDerivedObjWrapper.type-112"><a href="#BaseAutoDerivedObjWrapper.type-112"><span class="linenos">112</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="BaseAutoDerivedObjWrapper.type-113"><a href="#BaseAutoDerivedObjWrapper.type-113"><span class="linenos">113</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="BaseAutoDerivedObjWrapper.type-114"><a href="#BaseAutoDerivedObjWrapper.type-114"><span class="linenos">114</span></a>                <span class="k">return</span> <span class="n">base_type</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.temporary" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.temporary-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">temporary</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.temporary-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.temporary"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.temporary-120"><a href="#BaseAutoDerivedObjWrapper.temporary-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">temporary</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper.temporary-121"><a href="#BaseAutoDerivedObjWrapper.temporary-121"><span class="linenos">121</span></a>        <span class="k">return</span> <span class="n">TemporaryReinterpretCast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="BaseAutoDerivedObjWrapper.persistent" class="classattr">
                                        <input id="BaseAutoDerivedObjWrapper.persistent-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">persistent</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="BaseAutoDerivedObjWrapper.persistent-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#BaseAutoDerivedObjWrapper.persistent"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="BaseAutoDerivedObjWrapper.persistent-123"><a href="#BaseAutoDerivedObjWrapper.persistent-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">persistent</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="BaseAutoDerivedObjWrapper.persistent-124"><a href="#BaseAutoDerivedObjWrapper.persistent-124"><span class="linenos">124</span></a>        <span class="k">return</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">type</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">obj</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="ClassWrappingFactory">
                            <input id="ClassWrappingFactory-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ClassWrappingFactory</span>:

                <label class="view-source-button" for="ClassWrappingFactory-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactory"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactory-136"><a href="#ClassWrappingFactory-136"><span class="linenos">136</span></a><span class="k">class</span> <span class="nc">ClassWrappingFactory</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-137"><a href="#ClassWrappingFactory-137"><span class="linenos">137</span></a>    <span class="n">instance_id</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="ClassWrappingFactory-138"><a href="#ClassWrappingFactory-138"><span class="linenos">138</span></a>
</span><span id="ClassWrappingFactory-139"><a href="#ClassWrappingFactory-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ClassWrappingFactory-140"><a href="#ClassWrappingFactory-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">instance_id</span><span class="p">()</span>
</span><span id="ClassWrappingFactory-141"><a href="#ClassWrappingFactory-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="ClassWrappingFactory-142"><a href="#ClassWrappingFactory-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="ClassWrappingFactory-143"><a href="#ClassWrappingFactory-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_attributes_and_methods</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="ClassWrappingFactory-144"><a href="#ClassWrappingFactory-144"><span class="linenos">144</span></a>            <span class="s1">&#39;_class_wrapper__field_names&#39;</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="ClassWrappingFactory-145"><a href="#ClassWrappingFactory-145"><span class="linenos">145</span></a>            <span class="s1">&#39;_class_wrapper__factory&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="ClassWrappingFactory-146"><a href="#ClassWrappingFactory-146"><span class="linenos">146</span></a>        <span class="p">}</span>
</span><span id="ClassWrappingFactory-147"><a href="#ClassWrappingFactory-147"><span class="linenos">147</span></a>    
</span><span id="ClassWrappingFactory-148"><a href="#ClassWrappingFactory-148"><span class="linenos">148</span></a>    <span class="nd">@property</span>
</span><span id="ClassWrappingFactory-149"><a href="#ClassWrappingFactory-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">attributes_and_methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="ClassWrappingFactory-150"><a href="#ClassWrappingFactory-150"><span class="linenos">150</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_attributes_and_methods</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="ClassWrappingFactory-151"><a href="#ClassWrappingFactory-151"><span class="linenos">151</span></a>    
</span><span id="ClassWrappingFactory-152"><a href="#ClassWrappingFactory-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="ClassWrappingFactory-153"><a href="#ClassWrappingFactory-153"><span class="linenos">153</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="ClassWrappingFactory-154"><a href="#ClassWrappingFactory-154"><span class="linenos">154</span></a>
</span><span id="ClassWrappingFactory-155"><a href="#ClassWrappingFactory-155"><span class="linenos">155</span></a><span class="sd">        Args:</span>
</span><span id="ClassWrappingFactory-156"><a href="#ClassWrappingFactory-156"><span class="linenos">156</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="ClassWrappingFactory-157"><a href="#ClassWrappingFactory-157"><span class="linenos">157</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="ClassWrappingFactory-158"><a href="#ClassWrappingFactory-158"><span class="linenos">158</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="ClassWrappingFactory-159"><a href="#ClassWrappingFactory-159"><span class="linenos">159</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="ClassWrappingFactory-160"><a href="#ClassWrappingFactory-160"><span class="linenos">160</span></a>
</span><span id="ClassWrappingFactory-161"><a href="#ClassWrappingFactory-161"><span class="linenos">161</span></a><span class="sd">        Returns:</span>
</span><span id="ClassWrappingFactory-162"><a href="#ClassWrappingFactory-162"><span class="linenos">162</span></a><span class="sd">            Dict[str, Any]: _description_</span>
</span><span id="ClassWrappingFactory-163"><a href="#ClassWrappingFactory-163"><span class="linenos">163</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="ClassWrappingFactory-164"><a href="#ClassWrappingFactory-164"><span class="linenos">164</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span><span id="ClassWrappingFactory-165"><a href="#ClassWrappingFactory-165"><span class="linenos">165</span></a>    
</span><span id="ClassWrappingFactory-166"><a href="#ClassWrappingFactory-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">gen_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="ClassWrappingFactory-167"><a href="#ClassWrappingFactory-167"><span class="linenos">167</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="ClassWrappingFactory-168"><a href="#ClassWrappingFactory-168"><span class="linenos">168</span></a>
</span><span id="ClassWrappingFactory-169"><a href="#ClassWrappingFactory-169"><span class="linenos">169</span></a><span class="sd">        Args:</span>
</span><span id="ClassWrappingFactory-170"><a href="#ClassWrappingFactory-170"><span class="linenos">170</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="ClassWrappingFactory-171"><a href="#ClassWrappingFactory-171"><span class="linenos">171</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="ClassWrappingFactory-172"><a href="#ClassWrappingFactory-172"><span class="linenos">172</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="ClassWrappingFactory-173"><a href="#ClassWrappingFactory-173"><span class="linenos">173</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="ClassWrappingFactory-174"><a href="#ClassWrappingFactory-174"><span class="linenos">174</span></a>
</span><span id="ClassWrappingFactory-175"><a href="#ClassWrappingFactory-175"><span class="linenos">175</span></a><span class="sd">        Returns:</span>
</span><span id="ClassWrappingFactory-176"><a href="#ClassWrappingFactory-176"><span class="linenos">176</span></a><span class="sd">            Optional[Dict[str, Any]]: _description_</span>
</span><span id="ClassWrappingFactory-177"><a href="#ClassWrappingFactory-177"><span class="linenos">177</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="ClassWrappingFactory-178"><a href="#ClassWrappingFactory-178"><span class="linenos">178</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="ClassWrappingFactory-179"><a href="#ClassWrappingFactory-179"><span class="linenos">179</span></a>    
</span><span id="ClassWrappingFactory-180"><a href="#ClassWrappingFactory-180"><span class="linenos">180</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="ClassWrappingFactory-181"><a href="#ClassWrappingFactory-181"><span class="linenos">181</span></a>        <span class="n">base_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-182"><a href="#ClassWrappingFactory-182"><span class="linenos">182</span></a>        <span class="n">base_type_name</span> <span class="o">=</span> <span class="n">base_type</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="ClassWrappingFactory-183"><a href="#ClassWrappingFactory-183"><span class="linenos">183</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-184"><a href="#ClassWrappingFactory-184"><span class="linenos">184</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span>
</span><span id="ClassWrappingFactory-185"><a href="#ClassWrappingFactory-185"><span class="linenos">185</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-186"><a href="#ClassWrappingFactory-186"><span class="linenos">186</span></a>            <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_fields_tuple</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-187"><a href="#ClassWrappingFactory-187"><span class="linenos">187</span></a>            
</span><span id="ClassWrappingFactory-188"><a href="#ClassWrappingFactory-188"><span class="linenos">188</span></a>            <span class="n">attributes_and_methods</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">attributes_and_methods</span>
</span><span id="ClassWrappingFactory-189"><a href="#ClassWrappingFactory-189"><span class="linenos">189</span></a>            <span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__field_names&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">field_names</span>
</span><span id="ClassWrappingFactory-190"><a href="#ClassWrappingFactory-190"><span class="linenos">190</span></a>            <span class="n">attributes_and_methods</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">edit_derived_type</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-191"><a href="#ClassWrappingFactory-191"><span class="linenos">191</span></a>            <span class="n">kwargs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">gen_kwargs</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-192"><a href="#ClassWrappingFactory-192"><span class="linenos">192</span></a>            
</span><span id="ClassWrappingFactory-193"><a href="#ClassWrappingFactory-193"><span class="linenos">193</span></a>            <span class="k">if</span> <span class="n">kwargs</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-194"><a href="#ClassWrappingFactory-194"><span class="linenos">194</span></a>                <span class="n">derived</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,),</span> <span class="n">attributes_and_methods</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-195"><a href="#ClassWrappingFactory-195"><span class="linenos">195</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-196"><a href="#ClassWrappingFactory-196"><span class="linenos">196</span></a>                <span class="n">derived</span><span class="p">:</span> <span class="n">Type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_instance_id</span><span class="si">}</span><span class="s1">__from__</span><span class="si">{</span><span class="n">base_type_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="p">(</span><span class="n">base_type</span><span class="p">,),</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ClassWrappingFactory-197"><a href="#ClassWrappingFactory-197"><span class="linenos">197</span></a>
</span><span id="ClassWrappingFactory-198"><a href="#ClassWrappingFactory-198"><span class="linenos">198</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">derived</span><span class="p">[</span><span class="n">base_type_name</span><span class="p">]</span> <span class="o">=</span> <span class="n">derived</span>
</span><span id="ClassWrappingFactory-199"><a href="#ClassWrappingFactory-199"><span class="linenos">199</span></a>            <span class="k">return</span> <span class="n">derived</span>
</span><span id="ClassWrappingFactory-200"><a href="#ClassWrappingFactory-200"><span class="linenos">200</span></a>    
</span><span id="ClassWrappingFactory-201"><a href="#ClassWrappingFactory-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="ClassWrappingFactory-202"><a href="#ClassWrappingFactory-202"><span class="linenos">202</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-203"><a href="#ClassWrappingFactory-203"><span class="linenos">203</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="ClassWrappingFactory-204"><a href="#ClassWrappingFactory-204"><span class="linenos">204</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-205"><a href="#ClassWrappingFactory-205"><span class="linenos">205</span></a>            <span class="k">pass</span>
</span><span id="ClassWrappingFactory-206"><a href="#ClassWrappingFactory-206"><span class="linenos">206</span></a>
</span><span id="ClassWrappingFactory-207"><a href="#ClassWrappingFactory-207"><span class="linenos">207</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-208"><a href="#ClassWrappingFactory-208"><span class="linenos">208</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="ClassWrappingFactory-209"><a href="#ClassWrappingFactory-209"><span class="linenos">209</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ClassWrappingFactory-210"><a href="#ClassWrappingFactory-210"><span class="linenos">210</span></a>            <span class="k">pass</span>
</span><span id="ClassWrappingFactory-211"><a href="#ClassWrappingFactory-211"><span class="linenos">211</span></a>        
</span><span id="ClassWrappingFactory-212"><a href="#ClassWrappingFactory-212"><span class="linenos">212</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="ClassWrappingFactory.instance_id" class="classattr">
                                <div class="attr variable">
            <span class="name">instance_id</span>        =
<input id="ClassWrappingFactory.instance_id-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="ClassWrappingFactory.instance_id-view-value"></label><span class="default_value">&lt;cengal.data_generation.id_generator.versions.v_1.compilable.id_generator__cython.IDGeneratorInt object&gt;</span>

        
    </div>
    <a class="headerlink" href="#ClassWrappingFactory.instance_id"></a>
    
    

                            </div>
                            <div id="ClassWrappingFactory.class_name" class="classattr">
                                <div class="attr variable">
            <span class="name">class_name</span>

        
    </div>
    <a class="headerlink" href="#ClassWrappingFactory.class_name"></a>
    
    

                            </div>
                            <div id="ClassWrappingFactory.derived" class="classattr">
                                <div class="attr variable">
            <span class="name">derived</span><span class="annotation">: Dict[Type, Type]</span>

        
    </div>
    <a class="headerlink" href="#ClassWrappingFactory.derived"></a>
    
    

                            </div>
                            <div id="ClassWrappingFactory.attributes_and_methods" class="classattr">
                                        <input id="ClassWrappingFactory.attributes_and_methods-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">attributes_and_methods</span><span class="annotation">: Dict[str, Callable]</span>

                <label class="view-source-button" for="ClassWrappingFactory.attributes_and_methods-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactory.attributes_and_methods"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactory.attributes_and_methods-148"><a href="#ClassWrappingFactory.attributes_and_methods-148"><span class="linenos">148</span></a>    <span class="nd">@property</span>
</span><span id="ClassWrappingFactory.attributes_and_methods-149"><a href="#ClassWrappingFactory.attributes_and_methods-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">attributes_and_methods</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]:</span>
</span><span id="ClassWrappingFactory.attributes_and_methods-150"><a href="#ClassWrappingFactory.attributes_and_methods-150"><span class="linenos">150</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_attributes_and_methods</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ClassWrappingFactory.edit_derived_type" class="classattr">
                                        <input id="ClassWrappingFactory.edit_derived_type-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">edit_derived_type</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">attributes_and_methods</span>,</span><span class="param">	<span class="n">field_names</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ClassWrappingFactory.edit_derived_type-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactory.edit_derived_type"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactory.edit_derived_type-152"><a href="#ClassWrappingFactory.edit_derived_type-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="ClassWrappingFactory.edit_derived_type-153"><a href="#ClassWrappingFactory.edit_derived_type-153"><span class="linenos">153</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="ClassWrappingFactory.edit_derived_type-154"><a href="#ClassWrappingFactory.edit_derived_type-154"><span class="linenos">154</span></a>
</span><span id="ClassWrappingFactory.edit_derived_type-155"><a href="#ClassWrappingFactory.edit_derived_type-155"><span class="linenos">155</span></a><span class="sd">        Args:</span>
</span><span id="ClassWrappingFactory.edit_derived_type-156"><a href="#ClassWrappingFactory.edit_derived_type-156"><span class="linenos">156</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="ClassWrappingFactory.edit_derived_type-157"><a href="#ClassWrappingFactory.edit_derived_type-157"><span class="linenos">157</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="ClassWrappingFactory.edit_derived_type-158"><a href="#ClassWrappingFactory.edit_derived_type-158"><span class="linenos">158</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="ClassWrappingFactory.edit_derived_type-159"><a href="#ClassWrappingFactory.edit_derived_type-159"><span class="linenos">159</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="ClassWrappingFactory.edit_derived_type-160"><a href="#ClassWrappingFactory.edit_derived_type-160"><span class="linenos">160</span></a>
</span><span id="ClassWrappingFactory.edit_derived_type-161"><a href="#ClassWrappingFactory.edit_derived_type-161"><span class="linenos">161</span></a><span class="sd">        Returns:</span>
</span><span id="ClassWrappingFactory.edit_derived_type-162"><a href="#ClassWrappingFactory.edit_derived_type-162"><span class="linenos">162</span></a><span class="sd">            Dict[str, Any]: _description_</span>
</span><span id="ClassWrappingFactory.edit_derived_type-163"><a href="#ClassWrappingFactory.edit_derived_type-163"><span class="linenos">163</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="ClassWrappingFactory.edit_derived_type-164"><a href="#ClassWrappingFactory.edit_derived_type-164"><span class="linenos">164</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span></pre></div>


            <div class="docstring"><p>Might be overloaded in a derived class if needed</p>

<p>Args:
    obj (Any): _description_
    attributes_and_methods (_type_): _description_
    field_names (Tuple[str]): _description_
    data_size (int): _description_</p>

<p>Returns:
    Dict[str, Any]: _description_</p>
</div>


                            </div>
                            <div id="ClassWrappingFactory.gen_kwargs" class="classattr">
                                        <input id="ClassWrappingFactory.gen_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gen_kwargs</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">attributes_and_methods</span>,</span><span class="param">	<span class="n">field_names</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ClassWrappingFactory.gen_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactory.gen_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactory.gen_kwargs-166"><a href="#ClassWrappingFactory.gen_kwargs-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">gen_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]:</span>
</span><span id="ClassWrappingFactory.gen_kwargs-167"><a href="#ClassWrappingFactory.gen_kwargs-167"><span class="linenos">167</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in a derived class if needed</span>
</span><span id="ClassWrappingFactory.gen_kwargs-168"><a href="#ClassWrappingFactory.gen_kwargs-168"><span class="linenos">168</span></a>
</span><span id="ClassWrappingFactory.gen_kwargs-169"><a href="#ClassWrappingFactory.gen_kwargs-169"><span class="linenos">169</span></a><span class="sd">        Args:</span>
</span><span id="ClassWrappingFactory.gen_kwargs-170"><a href="#ClassWrappingFactory.gen_kwargs-170"><span class="linenos">170</span></a><span class="sd">            obj (Any): _description_</span>
</span><span id="ClassWrappingFactory.gen_kwargs-171"><a href="#ClassWrappingFactory.gen_kwargs-171"><span class="linenos">171</span></a><span class="sd">            attributes_and_methods (_type_): _description_</span>
</span><span id="ClassWrappingFactory.gen_kwargs-172"><a href="#ClassWrappingFactory.gen_kwargs-172"><span class="linenos">172</span></a><span class="sd">            field_names (Tuple[str]): _description_</span>
</span><span id="ClassWrappingFactory.gen_kwargs-173"><a href="#ClassWrappingFactory.gen_kwargs-173"><span class="linenos">173</span></a><span class="sd">            data_size (int): _description_</span>
</span><span id="ClassWrappingFactory.gen_kwargs-174"><a href="#ClassWrappingFactory.gen_kwargs-174"><span class="linenos">174</span></a>
</span><span id="ClassWrappingFactory.gen_kwargs-175"><a href="#ClassWrappingFactory.gen_kwargs-175"><span class="linenos">175</span></a><span class="sd">        Returns:</span>
</span><span id="ClassWrappingFactory.gen_kwargs-176"><a href="#ClassWrappingFactory.gen_kwargs-176"><span class="linenos">176</span></a><span class="sd">            Optional[Dict[str, Any]]: _description_</span>
</span><span id="ClassWrappingFactory.gen_kwargs-177"><a href="#ClassWrappingFactory.gen_kwargs-177"><span class="linenos">177</span></a><span class="sd">        &quot;&quot;&quot;</span>        
</span><span id="ClassWrappingFactory.gen_kwargs-178"><a href="#ClassWrappingFactory.gen_kwargs-178"><span class="linenos">178</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Might be overloaded in a derived class if needed</p>

<p>Args:
    obj (Any): _description_
    attributes_and_methods (_type_): _description_
    field_names (Tuple[str]): _description_
    data_size (int): _description_</p>

<p>Returns:
    Optional[Dict[str, Any]]: _description_</p>
</div>


                            </div>
                            <div id="ClassWrappingFactory.gen_fields_tuple" class="classattr">
                                        <input id="ClassWrappingFactory.gen_fields_tuple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gen_fields_tuple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ClassWrappingFactory.gen_fields_tuple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactory.gen_fields_tuple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactory.gen_fields_tuple-201"><a href="#ClassWrappingFactory.gen_fields_tuple-201"><span class="linenos">201</span></a>    <span class="k">def</span> <span class="nf">gen_fields_tuple</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">):</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-202"><a href="#ClassWrappingFactory.gen_fields_tuple-202"><span class="linenos">202</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-203"><a href="#ClassWrappingFactory.gen_fields_tuple-203"><span class="linenos">203</span></a>            <span class="k">return</span> <span class="n">obj</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-204"><a href="#ClassWrappingFactory.gen_fields_tuple-204"><span class="linenos">204</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-205"><a href="#ClassWrappingFactory.gen_fields_tuple-205"><span class="linenos">205</span></a>            <span class="k">pass</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-206"><a href="#ClassWrappingFactory.gen_fields_tuple-206"><span class="linenos">206</span></a>
</span><span id="ClassWrappingFactory.gen_fields_tuple-207"><a href="#ClassWrappingFactory.gen_fields_tuple-207"><span class="linenos">207</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-208"><a href="#ClassWrappingFactory.gen_fields_tuple-208"><span class="linenos">208</span></a>            <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">obj</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-209"><a href="#ClassWrappingFactory.gen_fields_tuple-209"><span class="linenos">209</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-210"><a href="#ClassWrappingFactory.gen_fields_tuple-210"><span class="linenos">210</span></a>            <span class="k">pass</span>
</span><span id="ClassWrappingFactory.gen_fields_tuple-211"><a href="#ClassWrappingFactory.gen_fields_tuple-211"><span class="linenos">211</span></a>        
</span><span id="ClassWrappingFactory.gen_fields_tuple-212"><a href="#ClassWrappingFactory.gen_fields_tuple-212"><span class="linenos">212</span></a>        <span class="k">return</span> <span class="nb">tuple</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="ClassWrappingFactoryWithObjDataSizeLog">
                            <input id="ClassWrappingFactoryWithObjDataSizeLog-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ClassWrappingFactoryWithObjDataSizeLog</span><wbr>(<span class="base"><a href="#ClassWrappingFactory">ClassWrappingFactory</a></span>):

                <label class="view-source-button" for="ClassWrappingFactoryWithObjDataSizeLog-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactoryWithObjDataSizeLog"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactoryWithObjDataSizeLog-215"><a href="#ClassWrappingFactoryWithObjDataSizeLog-215"><span class="linenos">215</span></a><span class="k">class</span> <span class="nc">ClassWrappingFactoryWithObjDataSizeLog</span><span class="p">(</span><span class="n">ClassWrappingFactory</span><span class="p">):</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-216"><a href="#ClassWrappingFactoryWithObjDataSizeLog-216"><span class="linenos">216</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-217"><a href="#ClassWrappingFactoryWithObjDataSizeLog-217"><span class="linenos">217</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-218"><a href="#ClassWrappingFactoryWithObjDataSizeLog-218"><span class="linenos">218</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__obj_data_size_log&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-219"><a href="#ClassWrappingFactoryWithObjDataSizeLog-219"><span class="linenos">219</span></a>    
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-220"><a href="#ClassWrappingFactoryWithObjDataSizeLog-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">data_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-221"><a href="#ClassWrappingFactoryWithObjDataSizeLog-221"><span class="linenos">221</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-222"><a href="#ClassWrappingFactoryWithObjDataSizeLog-222"><span class="linenos">222</span></a>        <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">field_names</span><span class="p">:</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-223"><a href="#ClassWrappingFactoryWithObjDataSizeLog-223"><span class="linenos">223</span></a>            <span class="n">data_size</span> <span class="o">+=</span> <span class="n">getsizeof</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">field_name</span><span class="p">))</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-224"><a href="#ClassWrappingFactoryWithObjDataSizeLog-224"><span class="linenos">224</span></a>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-225"><a href="#ClassWrappingFactoryWithObjDataSizeLog-225"><span class="linenos">225</span></a>        <span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__obj_data_size_log&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_size</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog-226"><a href="#ClassWrappingFactoryWithObjDataSizeLog-226"><span class="linenos">226</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span></pre></div>


    

                            <div id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type" class="classattr">
                                        <input id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">edit_derived_type</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">attributes_and_methods</span>,</span><span class="param">	<span class="n">field_names</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">data_size</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-220"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">edit_derived_type</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">attributes_and_methods</span><span class="p">,</span> <span class="n">field_names</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">data_size</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-221"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-221"><span class="linenos">221</span></a>        <span class="n">data_size</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-222"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-222"><span class="linenos">222</span></a>        <span class="k">for</span> <span class="n">field_name</span> <span class="ow">in</span> <span class="n">field_names</span><span class="p">:</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-223"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-223"><span class="linenos">223</span></a>            <span class="n">data_size</span> <span class="o">+=</span> <span class="n">getsizeof</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">field_name</span><span class="p">))</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-224"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-224"><span class="linenos">224</span></a>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-225"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-225"><span class="linenos">225</span></a>        <span class="n">attributes_and_methods</span><span class="p">[</span><span class="s1">&#39;_class_wrapper__obj_data_size_log&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">data_size</span>
</span><span id="ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-226"><a href="#ClassWrappingFactoryWithObjDataSizeLog.edit_derived_type-226"><span class="linenos">226</span></a>        <span class="k">return</span> <span class="n">attributes_and_methods</span>
</span></pre></div>


            <div class="docstring"><p>Might be overloaded in a derived class if needed</p>

<p>Args:
    obj (Any): _description_
    attributes_and_methods (_type_): _description_
    field_names (Tuple[str]): _description_
    data_size (int): _description_</p>

<p>Returns:
    Dict[str, Any]: _description_</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#ClassWrappingFactory">ClassWrappingFactory</a></dt>
                                <dd id="ClassWrappingFactoryWithObjDataSizeLog.instance_id" class="variable"><a href="#ClassWrappingFactory.instance_id">instance_id</a></dd>
                <dd id="ClassWrappingFactoryWithObjDataSizeLog.class_name" class="variable"><a href="#ClassWrappingFactory.class_name">class_name</a></dd>
                <dd id="ClassWrappingFactoryWithObjDataSizeLog.derived" class="variable"><a href="#ClassWrappingFactory.derived">derived</a></dd>
                <dd id="ClassWrappingFactoryWithObjDataSizeLog.attributes_and_methods" class="variable"><a href="#ClassWrappingFactory.attributes_and_methods">attributes_and_methods</a></dd>
                <dd id="ClassWrappingFactoryWithObjDataSizeLog.gen_kwargs" class="function"><a href="#ClassWrappingFactory.gen_kwargs">gen_kwargs</a></dd>
                <dd id="ClassWrappingFactoryWithObjDataSizeLog.gen_fields_tuple" class="function"><a href="#ClassWrappingFactory.gen_fields_tuple">gen_fields_tuple</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>