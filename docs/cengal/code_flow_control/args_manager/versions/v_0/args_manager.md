---
title: args_manager
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.args_manager<wbr>.versions<wbr>.v_0<wbr>.args_manager    </h1>

                
                        <input id="mod-args_manager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-args_manager-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;EntityWithExtendableArgs&#39;</span><span class="p">,</span> <span class="s1">&#39;ArgsManagerMixin&#39;</span><span class="p">,</span> <span class="s1">&#39;EntityArgsHolder&#39;</span><span class="p">,</span> <span class="s1">&#39;EAH&#39;</span><span class="p">,</span> <span class="s1">&#39;EntityArgsHolderExplicit&#39;</span><span class="p">,</span> <span class="s1">&#39;EAHE&#39;</span><span class="p">,</span> <span class="s1">&#39;ExtendKwargsManager&#39;</span><span class="p">,</span> 
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a>           <span class="s1">&#39;EKwargs&#39;</span><span class="p">,</span> <span class="s1">&#39;ExtendArgsManager&#39;</span><span class="p">,</span> <span class="s1">&#39;EArgs&#39;</span><span class="p">,</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">,</span> <span class="s1">&#39;merge_func_args&#39;</span><span class="p">,</span> <span class="s1">&#39;interested_args_to_kwargs&#39;</span><span class="p">,</span> <span class="s1">&#39;func_args_to_kwargs&#39;</span><span class="p">,</span> 
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>           <span class="s1">&#39;number_of_provided_args&#39;</span><span class="p">,</span> <span class="s1">&#39;args_kwargs&#39;</span><span class="p">,</span> <span class="s1">&#39;args_kwargs_to_str&#39;</span><span class="p">,</span> <span class="s1">&#39;ArgsKwargs&#39;</span><span class="p">,</span> <span class="s1">&#39;AK&#39;</span><span class="p">,</span> <span class="s1">&#39;prepare_arguments_positions&#39;</span><span class="p">,</span> <span class="s1">&#39;UnknownArgumentError&#39;</span><span class="p">,</span> 
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>           <span class="s1">&#39;find_arg_position_and_value&#39;</span><span class="p">,</span> <span class="s1">&#39;try_find_arg_position_and_value&#39;</span><span class="p">]</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">List</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">import</span> <span class="nn">inspect</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">import</span> <span class="nn">copy</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="sd">Module Docstring</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">EntityWithExtendableArgs</span> <span class="o">=</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">class</span> <span class="nc">ArgsManagerMixin</span><span class="p">:</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="k">class</span> <span class="nc">EntityArgsHolder</span><span class="p">:</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="k">def</span> <span class="nf">args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>    <span class="k">def</span> <span class="nf">entity_args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="n">EAH</span> <span class="o">=</span> <span class="n">EntityArgsHolder</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="k">class</span> <span class="nc">EntityArgsHolderExplicit</span><span class="p">(</span><span class="n">EntityArgsHolder</span><span class="p">):</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="n">EAHE</span> <span class="o">=</span> <span class="n">EntityArgsHolderExplicit</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="k">class</span> <span class="nc">ExtendKwargsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="sd">    Usage: </span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="sd">            EKwargs({&#39;a&#39;: &#39;hello&#39;, &#39;next&#39;: &#39;world}),</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="sd">            EKwargs(a=&#39;hello&#39;, b=&#39;world&#39;)</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="sd">        )</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="n">EKwargs</span> <span class="o">=</span> <span class="n">ExtendKwargsManager</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="k">class</span> <span class="nc">ExtendArgsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="sd">    Usage: </span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a><span class="sd">        def my_func(first, second, third, fourth, a, b, c):</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="sd">            ...</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="sd">        </span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">            EArgs(first, second, a=&#39;hello&#39;, b=&#39;world&#39;),</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">        )</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="sd">        am(my_func, third, fourth, c=&#39;!&#39;)</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="sd">        </span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="sd">            EArgs(first, second, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.prefix),</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">        )</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">        am(my_func, third, fourth, c=&#39;!&#39;)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="sd">        </span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">            EArgs(third, fourth, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.suffix),</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a><span class="sd">        )</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">        am(my_func, first, second, c=&#39;!&#39;)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">        </span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="sd">            EArgs(first, second, third, fourth, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.manager),</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="sd">        )</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a><span class="sd">        am(my_func, c=&#39;!&#39;)</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="sd">        # Or:</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="sd">        # am(my_func, ignored, ignored, ignored, ignored, c=&#39;!&#39;)</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a><span class="sd">        </span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="sd">            EArgs(a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.original),</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="sd">        )</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="sd">        # Or:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        # am = ArgsManager(</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="sd">        #     EArgs(ignored, ignored, ignored, ignored, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.original),</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="sd">        # )</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">        am(my_func, first, second, third, fourth, c=&#39;!&#39;)</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="k">class</span> <span class="nc">ArgsState</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="n">original</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="n">prefix</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="n">suffix</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="n">manager</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span> <span class="o">=</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">prefix</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">args_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ExtendArgsManager&#39;</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span> <span class="o">=</span> <span class="n">args_state</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">if</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">original</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">pass</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">prefix</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">suffix</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">manager</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="n">EArgs</span> <span class="o">=</span> <span class="n">ExtendArgsManager</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="k">class</span> <span class="nc">ArgsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="sd">    Usage:</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="sd">            EKwargs({&#39;a&#39;: &#39;hello&#39;, &#39;next&#39;: &#39;world}),</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="sd">            EKwargs(a=&#39;hello&#39;, b=&#39;world&#39;)</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">        )</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">    Example:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">        class Item(Enum):</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">            Div = 0</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">            Button = 1</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">        </span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">        def html(item, color, size, step=None, length=None, strength=None) -&gt; Any:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">            ...</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="sd">        </span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">            EKwargs({&#39;size&#39;: 12, &#39;step&#39;: &#39;one&#39;}),</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a><span class="sd">            EKwargs(color=&#39;green&#39;, strength=24)</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a><span class="sd">        )</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a><span class="sd">        </span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a><span class="sd">        page = list()</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a><span class="sd">        page.append(am(html, Item.Div))</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a><span class="sd">        page.append(am(html, Item.Button))</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="sd">        # The same as:</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="sd">        # page = list()</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a><span class="sd">        # page.append(html(Item.Div, &#39;green&#39;, 12, &#39;one&#39;, strength=24))</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="sd">        # page.append(html(Item.Button, &#39;green&#39;, 12, &#39;one&#39;, strength=24))</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>    
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    <span class="k">def</span> <span class="nf">append</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="k">def</span> <span class="nf">append_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>    <span class="k">def</span> <span class="nf">add_interceptor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>    
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    <span class="k">def</span> <span class="nf">add_interceptor_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="nf">callable</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="k">def</span> <span class="nf">callable_entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="n">original_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">args</span><span class="p">),</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="p">:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="n">one_shot_managers_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_managers_buff</span><span class="p">)()</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="n">one_shot_managers_buff</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="n">resulting_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="n">instance</span> <span class="o">=</span> <span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="p">:</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            <span class="n">one_shot_interceptors_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_interceptors_buff</span><span class="p">)()</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="n">one_shot_interceptors_buff</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="k">return</span> <span class="n">instance</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="k">return</span> <span class="n">callable_entity</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>    
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>        <span class="n">original_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">args</span><span class="p">),</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="n">one_shot_managers_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_managers_buff</span><span class="p">)()</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="n">one_shot_managers_buff</span><span class="p">:</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="n">resulting_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="n">instance</span> <span class="o">=</span> <span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="p">:</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>            <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="k">return</span> <span class="n">instance</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a><span class="k">def</span> <span class="nf">merge_func_args</span><span class="p">(</span><span class="n">func_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Callable</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>    <span class="n">args</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>    <span class="n">default_args</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>    <span class="k">for</span> <span class="n">func</span> <span class="ow">in</span> <span class="n">func_list</span><span class="p">:</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="n">is_method</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">elif</span> <span class="nb">callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>            <span class="n">is_method</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Is not callable: </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">func</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="n">varnames</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="k">if</span> <span class="n">is_method</span><span class="p">:</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">varnames</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                <span class="k">if</span> <span class="s1">&#39;self&#39;</span> <span class="o">==</span> <span class="n">varnames</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>                    <span class="n">varnames</span> <span class="o">=</span> <span class="n">varnames</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="n">spec</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getfullargspec</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>        <span class="c1"># print(f&#39;ArgSpec:&#39;)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="c1"># pprint(spec)</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>        
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="k">if</span> <span class="n">spec</span><span class="o">.</span><span class="n">defaults</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">)</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="n">defaults_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">spec</span><span class="o">.</span><span class="n">defaults</span><span class="p">)</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>            <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">[:</span><span class="o">-</span><span class="n">defaults_len</span><span class="p">])</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>            <span class="n">default_args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">[</span><span class="o">-</span><span class="n">defaults_len</span><span class="p">:])</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="c1"># print(f&#39;Args:&#39;)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>    <span class="c1"># pprint(args)</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="c1"># print(f&#39;Default args:&#39;)</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    <span class="c1"># pprint(default_args)</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>    <span class="k">return</span> <span class="n">args</span> <span class="o">+</span> <span class="n">default_args</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="k">def</span> <span class="nf">interested_args_to_kwargs</span><span class="p">(</span><span class="n">interested_args</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>    <span class="n">absent_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>    <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">interested_args</span><span class="p">:</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="n">absent_args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">absent_args</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>    <span class="k">return</span> <span class="n">kwargs</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="k">def</span> <span class="nf">func_args_to_kwargs</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>    <span class="n">interested_names</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="n">is_method</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    <span class="k">elif</span> <span class="nb">callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Is not callable: </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">func</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">interested_names</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>    <span class="n">not_needed_names</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">interested_names</span><span class="p">)</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">not_needed_names</span><span class="p">:</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>    <span class="k">if</span> <span class="n">is_method</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;self&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    <span class="k">return</span> <span class="n">kwargs</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a><span class="k">def</span> <span class="nf">number_of_provided_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>    <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a><span class="k">def</span> <span class="nf">args_kwargs</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>    <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a><span class="k">def</span> <span class="nf">args_kwargs_to_str</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>    <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="n">args_str</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">])</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="n">args_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>    
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>    <span class="k">if</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="n">kwargs_str</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="n">kwargs_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>    
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    <span class="k">if</span> <span class="n">kwargs_str</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">args_str</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">kwargs_str</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        <span class="k">return</span> <span class="n">args_str</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a><span class="k">class</span> <span class="nc">ArgsKwargs</span><span class="p">:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>    
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a><span class="n">AK</span> <span class="o">=</span> <span class="n">ArgsKwargs</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="k">def</span> <span class="nf">prepare_arguments_positions</span><span class="p">(</span><span class="n">positional</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">keyword_only</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]]:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="n">positions</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">):</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="n">positions</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>    <span class="k">return</span> <span class="n">positions</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a><span class="k">class</span> <span class="nc">UnknownArgumentError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>    <span class="k">pass</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a><span class="k">def</span> <span class="nf">find_arg_position_and_value</span><span class="p">(</span><span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]],</span> <span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="w">    </span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">    Example:</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a><span class="sd">        from cengal.introspection.inspect import func_param_names, CodeParamNames</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">        from cengal.code_flow_control.args_manager import prepare_arguments_positions, find_arg_position_and_value, UnknownArgumentError</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">        </span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a><span class="sd">        def wrapper(arg_name: str = &#39;b&#39;, *args, **kwargs):</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a><span class="sd">            def my_func(a, b, *, c, d):</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a><span class="sd">                ...</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a><span class="sd">            params: CodeParamNames = func_param_names(my_func)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a><span class="sd">            positoins: Dict[str, Optional[int]] = prepare_arguments_positions(params.positional, params.keyword_only)</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a><span class="sd">            found, pos, value = find_arg_position_and_value(arg_name, positoins)</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a><span class="sd">            if found:</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a><span class="sd">                print(f&#39;Value of &lt;{arg_name}&gt; : {value}&#39;)</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a><span class="sd">            </span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a><span class="sd">            if pos is not None:</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a><span class="sd">                print(f&#39;&lt;{arg_name}&gt; found as a positional argument at position {pos}&#39;)</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="sd">            </span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a><span class="sd">            return my_func(*args, **kwargs)</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a><span class="sd">        wrapper(&#39;a&#39;)</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a><span class="sd">        wrapper(&#39;a&#39;, 1, 2, 3, 4)</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a><span class="sd">        wrapper(&#39;d&#39;)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a><span class="sd">        wrapper(&#39;d&#39;, 1, 2, 3, 4)</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a><span class="sd">        try:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a><span class="sd">            wrapper(&#39;asdf&#39;)</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a><span class="sd">        except UnknownArgumentError as ex:</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a><span class="sd">            print(&#39;&lt;{ex.args[1]}&gt; is not a valid argument for my_func(). Valid arguments are: {ex.args[2]}&#39;)</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a><span class="sd">            raise</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a><span class="sd">    Args:</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a><span class="sd">        arg_name (str): _description_</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a><span class="sd">        positions (Dict[str, Optional[int]]): _description_</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a><span class="sd">        args (Tuple): _description_</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a><span class="sd">        kwargs (Dict): _description_</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a><span class="sd">    Raises:</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a><span class="sd">        UnknownArgumentError: _description_</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a><span class="sd">    Returns:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a><span class="sd">        Tuple[bool, bool, Optional[int], Any]: _description_</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>    <span class="n">found</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>    <span class="n">pos</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>    <span class="n">value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>    <span class="n">original_arg_pos</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="n">original_arg_pos</span> <span class="o">=</span> <span class="n">positions</span><span class="p">[</span><span class="n">arg_name</span><span class="p">]</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="n">valid_arguments</span> <span class="o">=</span> <span class="n">positions</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="k">raise</span> <span class="n">UnknownArgumentError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;&lt;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">&gt; is not in </span><span class="si">{</span><span class="n">valid_arguments</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">arg_name</span><span class="p">,</span> <span class="n">valid_arguments</span><span class="p">)</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>    
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>    <span class="k">if</span> <span class="n">original_arg_pos</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">original_arg_pos</span><span class="p">:</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>    
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>    <span class="k">if</span> <span class="n">found_in_args</span><span class="p">:</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="n">pos</span> <span class="o">=</span> <span class="n">original_arg_pos</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="n">value</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">pos</span><span class="p">]</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>            <span class="n">value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">arg_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="k">pass</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>    
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">return</span> <span class="n">found</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">value</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a><span class="k">def</span> <span class="nf">try_find_arg_position_and_value</span><span class="p">(</span><span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]],</span> <span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a><span class="w">    </span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a><span class="sd">    Example:</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a><span class="sd">        from cengal.introspection.inspect import func_param_names, CodeParamNames</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a><span class="sd">        from cengal.code_flow_control.args_manager import prepare_arguments_positions, try_find_arg_position_and_value</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a><span class="sd">        </span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a><span class="sd">        def wrapper(arg_name: str = &#39;b&#39;, *args, **kwargs):</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a><span class="sd">            def my_func(a, b, *, c, d):</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a><span class="sd">                ...</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a><span class="sd">            params: CodeParamNames = func_param_names(my_func)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a><span class="sd">            positoins: Dict[str, Optional[int]] = find_entity_arguments_positions(params.positional, params.keyword_only)</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a><span class="sd">            valid, found, pos, value = find_arg_position_and_value(arg_name, positoins)</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a><span class="sd">            if valid:</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a><span class="sd">                if found:</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a><span class="sd">                    print(f&#39;Value of &lt;{arg_name}&gt; : {value}&#39;)</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a><span class="sd">                </span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a><span class="sd">                if pos is not None:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a><span class="sd">                    print(f&#39;&lt;{arg_name}&gt; found as a positional argument at position {pos}&#39;)</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a><span class="sd">            else:</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a><span class="sd">                print(&#39;&lt;{arg_name}&gt; is not a valid argument for my_func(). Valid arguments are: {positoins.keys()}&#39;)</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a><span class="sd">            </span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a><span class="sd">            return my_func(*args, **kwargs)</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a><span class="sd">        wrapper(&#39;a&#39;)</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a><span class="sd">        wrapper(&#39;a&#39;, 1, 2, 3, 4)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a><span class="sd">        wrapper(&#39;d&#39;)</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a><span class="sd">        wrapper(&#39;d&#39;, 1, 2, 3, 4)</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a><span class="sd">        wrapper(&#39;asdf&#39;)</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a><span class="sd">    Args:</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a><span class="sd">        arg_name (str): _description_</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a><span class="sd">        positions (Dict[str, Optional[int]]): _description_</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a><span class="sd">        args (Tuple): _description_</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a><span class="sd">        kwargs (Dict): _description_</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a><span class="sd">    Returns:</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a><span class="sd">        Tuple[bool, bool, Optional[int], Any]: _description_</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    <span class="n">valid</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>    <span class="n">found</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>    <span class="n">pos</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="n">value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>    <span class="n">original_arg_pos</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>        <span class="n">original_arg_pos</span> <span class="o">=</span> <span class="n">positions</span><span class="p">[</span><span class="n">arg_name</span><span class="p">]</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>        <span class="n">valid</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">pass</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>    
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>    <span class="k">if</span> <span class="n">original_arg_pos</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">original_arg_pos</span><span class="p">:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>    
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>    <span class="k">if</span> <span class="n">found_in_args</span><span class="p">:</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="n">pos</span> <span class="o">=</span> <span class="n">original_arg_pos</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>        <span class="n">value</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">pos</span><span class="p">]</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>        <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>            <span class="n">value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">arg_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>            <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>            <span class="k">pass</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>    
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>    <span class="k">return</span> <span class="n">valid</span><span class="p">,</span> <span class="n">found</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">value</span>
</span></pre></div>


            </section>
                <section id="EntityWithExtendableArgs">
                    <div class="attr variable">
            <span class="name">EntityWithExtendableArgs</span>        =
<span class="default_value">typing.Union[typing.Type, typing.Callable]</span>

        
    </div>
    <a class="headerlink" href="#EntityWithExtendableArgs"></a>
    
    

                </section>
                <section id="ArgsManagerMixin">
                            <input id="ArgsManagerMixin-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ArgsManagerMixin</span>:

                <label class="view-source-button" for="ArgsManagerMixin-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManagerMixin"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManagerMixin-49"><a href="#ArgsManagerMixin-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">ArgsManagerMixin</span><span class="p">:</span>
</span><span id="ArgsManagerMixin-50"><a href="#ArgsManagerMixin-50"><span class="linenos">50</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ArgsManagerMixin-51"><a href="#ArgsManagerMixin-51"><span class="linenos">51</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                </section>
                <section id="EntityArgsHolder">
                            <input id="EntityArgsHolder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EntityArgsHolder</span>:

                <label class="view-source-button" for="EntityArgsHolder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolder-54"><a href="#EntityArgsHolder-54"><span class="linenos">54</span></a><span class="k">class</span> <span class="nc">EntityArgsHolder</span><span class="p">:</span>
</span><span id="EntityArgsHolder-55"><a href="#EntityArgsHolder-55"><span class="linenos">55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EntityArgsHolder-56"><a href="#EntityArgsHolder-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="EntityArgsHolder-57"><a href="#EntityArgsHolder-57"><span class="linenos">57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="EntityArgsHolder-58"><a href="#EntityArgsHolder-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="EntityArgsHolder-59"><a href="#EntityArgsHolder-59"><span class="linenos">59</span></a>    
</span><span id="EntityArgsHolder-60"><a href="#EntityArgsHolder-60"><span class="linenos">60</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="EntityArgsHolder-61"><a href="#EntityArgsHolder-61"><span class="linenos">61</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EntityArgsHolder-62"><a href="#EntityArgsHolder-62"><span class="linenos">62</span></a>    
</span><span id="EntityArgsHolder-63"><a href="#EntityArgsHolder-63"><span class="linenos">63</span></a>    <span class="k">def</span> <span class="nf">args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="EntityArgsHolder-64"><a href="#EntityArgsHolder-64"><span class="linenos">64</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span><span id="EntityArgsHolder-65"><a href="#EntityArgsHolder-65"><span class="linenos">65</span></a>    
</span><span id="EntityArgsHolder-66"><a href="#EntityArgsHolder-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="nf">entity_args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="EntityArgsHolder-67"><a href="#EntityArgsHolder-67"><span class="linenos">67</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="EntityArgsHolder.__init__" class="classattr">
                                        <input id="EntityArgsHolder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">EntityArgsHolder</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">]</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="EntityArgsHolder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolder.__init__-55"><a href="#EntityArgsHolder.__init__-55"><span class="linenos">55</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EntityArgsHolder.__init__-56"><a href="#EntityArgsHolder.__init__-56"><span class="linenos">56</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="EntityArgsHolder.__init__-57"><a href="#EntityArgsHolder.__init__-57"><span class="linenos">57</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="EntityArgsHolder.__init__-58"><a href="#EntityArgsHolder.__init__-58"><span class="linenos">58</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="EntityArgsHolder.entity" class="classattr">
                                <div class="attr variable">
            <span class="name">entity</span><span class="annotation">: Union[Type, Callable]</span>

        
    </div>
    <a class="headerlink" href="#EntityArgsHolder.entity"></a>
    
    

                            </div>
                            <div id="EntityArgsHolder.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span><span class="annotation">: Tuple</span>

        
    </div>
    <a class="headerlink" href="#EntityArgsHolder.args"></a>
    
    

                            </div>
                            <div id="EntityArgsHolder.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span><span class="annotation">: Dict</span>

        
    </div>
    <a class="headerlink" href="#EntityArgsHolder.kwargs"></a>
    
    

                            </div>
                            <div id="EntityArgsHolder.args_kwargs" class="classattr">
                                        <input id="EntityArgsHolder.args_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">args_kwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="EntityArgsHolder.args_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolder.args_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolder.args_kwargs-63"><a href="#EntityArgsHolder.args_kwargs-63"><span class="linenos">63</span></a>    <span class="k">def</span> <span class="nf">args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="EntityArgsHolder.args_kwargs-64"><a href="#EntityArgsHolder.args_kwargs-64"><span class="linenos">64</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="EntityArgsHolder.entity_args_kwargs" class="classattr">
                                        <input id="EntityArgsHolder.entity_args_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_args_kwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">Callable</span><span class="p">],</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="EntityArgsHolder.entity_args_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolder.entity_args_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolder.entity_args_kwargs-66"><a href="#EntityArgsHolder.entity_args_kwargs-66"><span class="linenos">66</span></a>    <span class="k">def</span> <span class="nf">entity_args_kwargs</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="EntityArgsHolder.entity_args_kwargs-67"><a href="#EntityArgsHolder.entity_args_kwargs-67"><span class="linenos">67</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="EAH">
                    <div class="attr variable">
            <span class="name">EAH</span>        =
<span class="default_value">&lt;class &#39;<a href="#EntityArgsHolder">EntityArgsHolder</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#EAH"></a>
    
    

                </section>
                <section id="EntityArgsHolderExplicit">
                            <input id="EntityArgsHolderExplicit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EntityArgsHolderExplicit</span><wbr>(<span class="base"><a href="#EntityArgsHolder">EntityArgsHolder</a></span>):

                <label class="view-source-button" for="EntityArgsHolderExplicit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolderExplicit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolderExplicit-73"><a href="#EntityArgsHolderExplicit-73"><span class="linenos">73</span></a><span class="k">class</span> <span class="nc">EntityArgsHolderExplicit</span><span class="p">(</span><span class="n">EntityArgsHolder</span><span class="p">):</span>
</span><span id="EntityArgsHolderExplicit-74"><a href="#EntityArgsHolderExplicit-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="EntityArgsHolderExplicit-75"><a href="#EntityArgsHolderExplicit-75"><span class="linenos">75</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="EntityArgsHolderExplicit-76"><a href="#EntityArgsHolderExplicit-76"><span class="linenos">76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="EntityArgsHolderExplicit-77"><a href="#EntityArgsHolderExplicit-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="EntityArgsHolderExplicit.__init__" class="classattr">
                                        <input id="EntityArgsHolderExplicit.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">EntityArgsHolderExplicit</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">]</span>, </span><span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="EntityArgsHolderExplicit.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityArgsHolderExplicit.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityArgsHolderExplicit.__init__-74"><a href="#EntityArgsHolderExplicit.__init__-74"><span class="linenos">74</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="EntityArgsHolderExplicit.__init__-75"><a href="#EntityArgsHolderExplicit.__init__-75"><span class="linenos">75</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="EntityArgsHolderExplicit.__init__-76"><a href="#EntityArgsHolderExplicit.__init__-76"><span class="linenos">76</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="EntityArgsHolderExplicit.__init__-77"><a href="#EntityArgsHolderExplicit.__init__-77"><span class="linenos">77</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="EntityArgsHolderExplicit.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span><span class="annotation">: Tuple</span>

        
    </div>
    <a class="headerlink" href="#EntityArgsHolderExplicit.args"></a>
    
    

                            </div>
                            <div id="EntityArgsHolderExplicit.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span><span class="annotation">: Dict</span>

        
    </div>
    <a class="headerlink" href="#EntityArgsHolderExplicit.kwargs"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#EntityArgsHolder">EntityArgsHolder</a></dt>
                                <dd id="EntityArgsHolderExplicit.entity" class="variable"><a href="#EntityArgsHolder.entity">entity</a></dd>
                <dd id="EntityArgsHolderExplicit.args_kwargs" class="function"><a href="#EntityArgsHolder.args_kwargs">args_kwargs</a></dd>
                <dd id="EntityArgsHolderExplicit.entity_args_kwargs" class="function"><a href="#EntityArgsHolder.entity_args_kwargs">entity_args_kwargs</a></dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EAHE">
                    <div class="attr variable">
            <span class="name">EAHE</span>        =
<span class="default_value">&lt;class &#39;<a href="#EntityArgsHolderExplicit">EntityArgsHolderExplicit</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#EAHE"></a>
    
    

                </section>
                <section id="ExtendKwargsManager">
                            <input id="ExtendKwargsManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExtendKwargsManager</span><wbr>(<span class="base"><a href="#ArgsManagerMixin">ArgsManagerMixin</a></span>):

                <label class="view-source-button" for="ExtendKwargsManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendKwargsManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendKwargsManager-83"><a href="#ExtendKwargsManager-83"><span class="linenos"> 83</span></a><span class="k">class</span> <span class="nc">ExtendKwargsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="ExtendKwargsManager-84"><a href="#ExtendKwargsManager-84"><span class="linenos"> 84</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ExtendKwargsManager-85"><a href="#ExtendKwargsManager-85"><span class="linenos"> 85</span></a><span class="sd">    Usage: </span>
</span><span id="ExtendKwargsManager-86"><a href="#ExtendKwargsManager-86"><span class="linenos"> 86</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendKwargsManager-87"><a href="#ExtendKwargsManager-87"><span class="linenos"> 87</span></a><span class="sd">            EKwargs({&#39;a&#39;: &#39;hello&#39;, &#39;next&#39;: &#39;world}),</span>
</span><span id="ExtendKwargsManager-88"><a href="#ExtendKwargsManager-88"><span class="linenos"> 88</span></a><span class="sd">            EKwargs(a=&#39;hello&#39;, b=&#39;world&#39;)</span>
</span><span id="ExtendKwargsManager-89"><a href="#ExtendKwargsManager-89"><span class="linenos"> 89</span></a><span class="sd">        )</span>
</span><span id="ExtendKwargsManager-90"><a href="#ExtendKwargsManager-90"><span class="linenos"> 90</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ExtendKwargsManager-91"><a href="#ExtendKwargsManager-91"><span class="linenos"> 91</span></a>    
</span><span id="ExtendKwargsManager-92"><a href="#ExtendKwargsManager-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ExtendKwargsManager-93"><a href="#ExtendKwargsManager-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="ExtendKwargsManager-94"><a href="#ExtendKwargsManager-94"><span class="linenos"> 94</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span>
</span><span id="ExtendKwargsManager-95"><a href="#ExtendKwargsManager-95"><span class="linenos"> 95</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="ExtendKwargsManager-96"><a href="#ExtendKwargsManager-96"><span class="linenos"> 96</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="ExtendKwargsManager-97"><a href="#ExtendKwargsManager-97"><span class="linenos"> 97</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span><span id="ExtendKwargsManager-98"><a href="#ExtendKwargsManager-98"><span class="linenos"> 98</span></a>    
</span><span id="ExtendKwargsManager-99"><a href="#ExtendKwargsManager-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ExtendKwargsManager-100"><a href="#ExtendKwargsManager-100"><span class="linenos">100</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ExtendKwargsManager-101"><a href="#ExtendKwargsManager-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span></pre></div>


            <div class="docstring"><p>Usage: 
    am = ArgsManager(
        EKwargs({'a': 'hello', 'next': 'world}),
        EKwargs(a='hello', b='world')
    )</p>
</div>


                            <div id="ExtendKwargsManager.__init__" class="classattr">
                                        <input id="ExtendKwargsManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ExtendKwargsManager</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="ExtendKwargsManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendKwargsManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendKwargsManager.__init__-92"><a href="#ExtendKwargsManager.__init__-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ExtendKwargsManager.__init__-93"><a href="#ExtendKwargsManager.__init__-93"><span class="linenos">93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="ExtendKwargsManager.__init__-94"><a href="#ExtendKwargsManager.__init__-94"><span class="linenos">94</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span>
</span><span id="ExtendKwargsManager.__init__-95"><a href="#ExtendKwargsManager.__init__-95"><span class="linenos">95</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="ExtendKwargsManager.__init__-96"><a href="#ExtendKwargsManager.__init__-96"><span class="linenos">96</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="ExtendKwargsManager.__init__-97"><a href="#ExtendKwargsManager.__init__-97"><span class="linenos">97</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ExtendKwargsManager.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#ExtendKwargsManager.kwargs"></a>
    
    

                            </div>
                </section>
                <section id="EKwargs">
                    <div class="attr variable">
            <span class="name">EKwargs</span>        =
<span class="default_value">&lt;class &#39;<a href="#ExtendKwargsManager">ExtendKwargsManager</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#EKwargs"></a>
    
    

                </section>
                <section id="ExtendArgsManager">
                            <input id="ExtendArgsManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExtendArgsManager</span><wbr>(<span class="base"><a href="#ArgsManagerMixin">ArgsManagerMixin</a></span>):

                <label class="view-source-button" for="ExtendArgsManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendArgsManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendArgsManager-107"><a href="#ExtendArgsManager-107"><span class="linenos">107</span></a><span class="k">class</span> <span class="nc">ExtendArgsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="ExtendArgsManager-108"><a href="#ExtendArgsManager-108"><span class="linenos">108</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ExtendArgsManager-109"><a href="#ExtendArgsManager-109"><span class="linenos">109</span></a><span class="sd">    Usage: </span>
</span><span id="ExtendArgsManager-110"><a href="#ExtendArgsManager-110"><span class="linenos">110</span></a><span class="sd">        def my_func(first, second, third, fourth, a, b, c):</span>
</span><span id="ExtendArgsManager-111"><a href="#ExtendArgsManager-111"><span class="linenos">111</span></a><span class="sd">            ...</span>
</span><span id="ExtendArgsManager-112"><a href="#ExtendArgsManager-112"><span class="linenos">112</span></a><span class="sd">        </span>
</span><span id="ExtendArgsManager-113"><a href="#ExtendArgsManager-113"><span class="linenos">113</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendArgsManager-114"><a href="#ExtendArgsManager-114"><span class="linenos">114</span></a><span class="sd">            EArgs(first, second, a=&#39;hello&#39;, b=&#39;world&#39;),</span>
</span><span id="ExtendArgsManager-115"><a href="#ExtendArgsManager-115"><span class="linenos">115</span></a><span class="sd">        )</span>
</span><span id="ExtendArgsManager-116"><a href="#ExtendArgsManager-116"><span class="linenos">116</span></a><span class="sd">        am(my_func, third, fourth, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-117"><a href="#ExtendArgsManager-117"><span class="linenos">117</span></a><span class="sd">        </span>
</span><span id="ExtendArgsManager-118"><a href="#ExtendArgsManager-118"><span class="linenos">118</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendArgsManager-119"><a href="#ExtendArgsManager-119"><span class="linenos">119</span></a><span class="sd">            EArgs(first, second, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.prefix),</span>
</span><span id="ExtendArgsManager-120"><a href="#ExtendArgsManager-120"><span class="linenos">120</span></a><span class="sd">        )</span>
</span><span id="ExtendArgsManager-121"><a href="#ExtendArgsManager-121"><span class="linenos">121</span></a><span class="sd">        am(my_func, third, fourth, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-122"><a href="#ExtendArgsManager-122"><span class="linenos">122</span></a><span class="sd">        </span>
</span><span id="ExtendArgsManager-123"><a href="#ExtendArgsManager-123"><span class="linenos">123</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendArgsManager-124"><a href="#ExtendArgsManager-124"><span class="linenos">124</span></a><span class="sd">            EArgs(third, fourth, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.suffix),</span>
</span><span id="ExtendArgsManager-125"><a href="#ExtendArgsManager-125"><span class="linenos">125</span></a><span class="sd">        )</span>
</span><span id="ExtendArgsManager-126"><a href="#ExtendArgsManager-126"><span class="linenos">126</span></a><span class="sd">        am(my_func, first, second, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-127"><a href="#ExtendArgsManager-127"><span class="linenos">127</span></a><span class="sd">        </span>
</span><span id="ExtendArgsManager-128"><a href="#ExtendArgsManager-128"><span class="linenos">128</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendArgsManager-129"><a href="#ExtendArgsManager-129"><span class="linenos">129</span></a><span class="sd">            EArgs(first, second, third, fourth, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.manager),</span>
</span><span id="ExtendArgsManager-130"><a href="#ExtendArgsManager-130"><span class="linenos">130</span></a><span class="sd">        )</span>
</span><span id="ExtendArgsManager-131"><a href="#ExtendArgsManager-131"><span class="linenos">131</span></a><span class="sd">        am(my_func, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-132"><a href="#ExtendArgsManager-132"><span class="linenos">132</span></a><span class="sd">        # Or:</span>
</span><span id="ExtendArgsManager-133"><a href="#ExtendArgsManager-133"><span class="linenos">133</span></a><span class="sd">        # am(my_func, ignored, ignored, ignored, ignored, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-134"><a href="#ExtendArgsManager-134"><span class="linenos">134</span></a><span class="sd">        </span>
</span><span id="ExtendArgsManager-135"><a href="#ExtendArgsManager-135"><span class="linenos">135</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ExtendArgsManager-136"><a href="#ExtendArgsManager-136"><span class="linenos">136</span></a><span class="sd">            EArgs(a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.original),</span>
</span><span id="ExtendArgsManager-137"><a href="#ExtendArgsManager-137"><span class="linenos">137</span></a><span class="sd">        )</span>
</span><span id="ExtendArgsManager-138"><a href="#ExtendArgsManager-138"><span class="linenos">138</span></a><span class="sd">        # Or:</span>
</span><span id="ExtendArgsManager-139"><a href="#ExtendArgsManager-139"><span class="linenos">139</span></a><span class="sd">        # am = ArgsManager(</span>
</span><span id="ExtendArgsManager-140"><a href="#ExtendArgsManager-140"><span class="linenos">140</span></a><span class="sd">        #     EArgs(ignored, ignored, ignored, ignored, a=&#39;hello&#39;, b=&#39;world&#39;).args_state(ExtendArgsManager.ArgsState.original),</span>
</span><span id="ExtendArgsManager-141"><a href="#ExtendArgsManager-141"><span class="linenos">141</span></a><span class="sd">        # )</span>
</span><span id="ExtendArgsManager-142"><a href="#ExtendArgsManager-142"><span class="linenos">142</span></a><span class="sd">        am(my_func, first, second, third, fourth, c=&#39;!&#39;)</span>
</span><span id="ExtendArgsManager-143"><a href="#ExtendArgsManager-143"><span class="linenos">143</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ExtendArgsManager-144"><a href="#ExtendArgsManager-144"><span class="linenos">144</span></a>    <span class="k">class</span> <span class="nc">ArgsState</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="ExtendArgsManager-145"><a href="#ExtendArgsManager-145"><span class="linenos">145</span></a>        <span class="n">original</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ExtendArgsManager-146"><a href="#ExtendArgsManager-146"><span class="linenos">146</span></a>        <span class="n">prefix</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="ExtendArgsManager-147"><a href="#ExtendArgsManager-147"><span class="linenos">147</span></a>        <span class="n">suffix</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="ExtendArgsManager-148"><a href="#ExtendArgsManager-148"><span class="linenos">148</span></a>        <span class="n">manager</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="ExtendArgsManager-149"><a href="#ExtendArgsManager-149"><span class="linenos">149</span></a>    
</span><span id="ExtendArgsManager-150"><a href="#ExtendArgsManager-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ExtendArgsManager-151"><a href="#ExtendArgsManager-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ExtendArgsManager-152"><a href="#ExtendArgsManager-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span> <span class="o">=</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">prefix</span>
</span><span id="ExtendArgsManager-153"><a href="#ExtendArgsManager-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="ExtendArgsManager-154"><a href="#ExtendArgsManager-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="ExtendArgsManager-155"><a href="#ExtendArgsManager-155"><span class="linenos">155</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span><span id="ExtendArgsManager-156"><a href="#ExtendArgsManager-156"><span class="linenos">156</span></a>    
</span><span id="ExtendArgsManager-157"><a href="#ExtendArgsManager-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">args_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ExtendArgsManager&#39;</span><span class="p">:</span>
</span><span id="ExtendArgsManager-158"><a href="#ExtendArgsManager-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span> <span class="o">=</span> <span class="n">args_state</span>
</span><span id="ExtendArgsManager-159"><a href="#ExtendArgsManager-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="ExtendArgsManager-160"><a href="#ExtendArgsManager-160"><span class="linenos">160</span></a>    
</span><span id="ExtendArgsManager-161"><a href="#ExtendArgsManager-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ExtendArgsManager-162"><a href="#ExtendArgsManager-162"><span class="linenos">162</span></a>        <span class="k">if</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">original</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="ExtendArgsManager-163"><a href="#ExtendArgsManager-163"><span class="linenos">163</span></a>            <span class="k">pass</span>
</span><span id="ExtendArgsManager-164"><a href="#ExtendArgsManager-164"><span class="linenos">164</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">prefix</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="ExtendArgsManager-165"><a href="#ExtendArgsManager-165"><span class="linenos">165</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>
</span><span id="ExtendArgsManager-166"><a href="#ExtendArgsManager-166"><span class="linenos">166</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">suffix</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="ExtendArgsManager-167"><a href="#ExtendArgsManager-167"><span class="linenos">167</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="ExtendArgsManager-168"><a href="#ExtendArgsManager-168"><span class="linenos">168</span></a>        <span class="k">elif</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">manager</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span>
</span><span id="ExtendArgsManager-169"><a href="#ExtendArgsManager-169"><span class="linenos">169</span></a>            <span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</span><span id="ExtendArgsManager-170"><a href="#ExtendArgsManager-170"><span class="linenos">170</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ExtendArgsManager-171"><a href="#ExtendArgsManager-171"><span class="linenos">171</span></a>        <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span></pre></div>


            <div class="docstring"><p>Usage: 
    def my_func(first, second, third, fourth, a, b, c):
        ...</p>

<pre><code>am = ArgsManager(
    EArgs(first, second, a='hello', b='world'),
)
am(my_func, third, fourth, c='!')

am = ArgsManager(
    EArgs(first, second, a='hello', b='world').args_state(<a href="#ExtendArgsManager.ArgsState.prefix">ExtendArgsManager.ArgsState.prefix</a>),
)
am(my_func, third, fourth, c='!')

am = ArgsManager(
    EArgs(third, fourth, a='hello', b='world').args_state(<a href="#ExtendArgsManager.ArgsState.suffix">ExtendArgsManager.ArgsState.suffix</a>),
)
am(my_func, first, second, c='!')

am = ArgsManager(
    EArgs(first, second, third, fourth, a='hello', b='world').args_state(<a href="#ExtendArgsManager.ArgsState.manager">ExtendArgsManager.ArgsState.manager</a>),
)
am(my_func, c='!')
# Or:
# am(my_func, ignored, ignored, ignored, ignored, c='!')

am = ArgsManager(
    EArgs(a='hello', b='world').args_state(<a href="#ExtendArgsManager.ArgsState.original">ExtendArgsManager.ArgsState.original</a>),
)
# Or:
# am = ArgsManager(
#     EArgs(ignored, ignored, ignored, ignored, a='hello', b='world').args_state(<a href="#ExtendArgsManager.ArgsState.original">ExtendArgsManager.ArgsState.original</a>),
# )
am(my_func, first, second, third, fourth, c='!')
</code></pre>
</div>


                            <div id="ExtendArgsManager.__init__" class="classattr">
                                        <input id="ExtendArgsManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ExtendArgsManager</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="ExtendArgsManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendArgsManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendArgsManager.__init__-150"><a href="#ExtendArgsManager.__init__-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="ExtendArgsManager.__init__-151"><a href="#ExtendArgsManager.__init__-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ExtendArgsManager.__init__-152"><a href="#ExtendArgsManager.__init__-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span> <span class="o">=</span> <span class="n">ExtendArgsManager</span><span class="o">.</span><span class="n">ArgsState</span><span class="o">.</span><span class="n">prefix</span>
</span><span id="ExtendArgsManager.__init__-153"><a href="#ExtendArgsManager.__init__-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="n">kwargs</span> <span class="ow">or</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="ExtendArgsManager.__init__-154"><a href="#ExtendArgsManager.__init__-154"><span class="linenos">154</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">Dict</span><span class="p">):</span>
</span><span id="ExtendArgsManager.__init__-155"><a href="#ExtendArgsManager.__init__-155"><span class="linenos">155</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Wrong parameters&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="ExtendArgsManager.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.args"></a>
    
    

                            </div>
                            <div id="ExtendArgsManager.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.kwargs"></a>
    
    

                            </div>
                            <div id="ExtendArgsManager.args_state" class="classattr">
                                        <input id="ExtendArgsManager.args_state-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">args_state</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">args_state</span><span class="p">:</span> <span class="n"><a href="#ExtendArgsManager.ArgsState">ExtendArgsManager.ArgsState</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#ExtendArgsManager">ExtendArgsManager</a></span>:</span></span>

                <label class="view-source-button" for="ExtendArgsManager.args_state-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendArgsManager.args_state"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendArgsManager.args_state-157"><a href="#ExtendArgsManager.args_state-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">args_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">args_state</span><span class="p">:</span> <span class="s1">&#39;ExtendArgsManager.ArgsState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ExtendArgsManager&#39;</span><span class="p">:</span>
</span><span id="ExtendArgsManager.args_state-158"><a href="#ExtendArgsManager.args_state-158"><span class="linenos">158</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_args_state</span> <span class="o">=</span> <span class="n">args_state</span>
</span><span id="ExtendArgsManager.args_state-159"><a href="#ExtendArgsManager.args_state-159"><span class="linenos">159</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="ExtendArgsManager.ArgsState">
                            <input id="ExtendArgsManager.ArgsState-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExtendArgsManager.ArgsState</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="ExtendArgsManager.ArgsState-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExtendArgsManager.ArgsState"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExtendArgsManager.ArgsState-144"><a href="#ExtendArgsManager.ArgsState-144"><span class="linenos">144</span></a>    <span class="k">class</span> <span class="nc">ArgsState</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="ExtendArgsManager.ArgsState-145"><a href="#ExtendArgsManager.ArgsState-145"><span class="linenos">145</span></a>        <span class="n">original</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="ExtendArgsManager.ArgsState-146"><a href="#ExtendArgsManager.ArgsState-146"><span class="linenos">146</span></a>        <span class="n">prefix</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="ExtendArgsManager.ArgsState-147"><a href="#ExtendArgsManager.ArgsState-147"><span class="linenos">147</span></a>        <span class="n">suffix</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="ExtendArgsManager.ArgsState-148"><a href="#ExtendArgsManager.ArgsState-148"><span class="linenos">148</span></a>        <span class="n">manager</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="ExtendArgsManager.ArgsState.original" class="classattr">
                                <div class="attr variable">
            <span class="name">original</span>        =
<span class="default_value">&lt;ArgsState.original: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.ArgsState.original"></a>
    
    

                            </div>
                            <div id="ExtendArgsManager.ArgsState.prefix" class="classattr">
                                <div class="attr variable">
            <span class="name">prefix</span>        =
<span class="default_value">&lt;ArgsState.prefix: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.ArgsState.prefix"></a>
    
    

                            </div>
                            <div id="ExtendArgsManager.ArgsState.suffix" class="classattr">
                                <div class="attr variable">
            <span class="name">suffix</span>        =
<span class="default_value">&lt;ArgsState.suffix: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.ArgsState.suffix"></a>
    
    

                            </div>
                            <div id="ExtendArgsManager.ArgsState.manager" class="classattr">
                                <div class="attr variable">
            <span class="name">manager</span>        =
<span class="default_value">&lt;ArgsState.manager: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#ExtendArgsManager.ArgsState.manager"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="ExtendArgsManager.ArgsState.name" class="variable">name</dd>
                <dd id="ExtendArgsManager.ArgsState.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EArgs">
                    <div class="attr variable">
            <span class="name">EArgs</span>        =
<span class="default_value">&lt;class &#39;<a href="#ExtendArgsManager">ExtendArgsManager</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#EArgs"></a>
    
    

                </section>
                <section id="ArgsManager">
                            <input id="ArgsManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ArgsManager</span><wbr>(<span class="base"><a href="#ArgsManagerMixin">ArgsManagerMixin</a></span>):

                <label class="view-source-button" for="ArgsManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager-177"><a href="#ArgsManager-177"><span class="linenos">177</span></a><span class="k">class</span> <span class="nc">ArgsManager</span><span class="p">(</span><span class="n">ArgsManagerMixin</span><span class="p">):</span>
</span><span id="ArgsManager-178"><a href="#ArgsManager-178"><span class="linenos">178</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="ArgsManager-179"><a href="#ArgsManager-179"><span class="linenos">179</span></a><span class="sd">    Usage:</span>
</span><span id="ArgsManager-180"><a href="#ArgsManager-180"><span class="linenos">180</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ArgsManager-181"><a href="#ArgsManager-181"><span class="linenos">181</span></a><span class="sd">            EKwargs({&#39;a&#39;: &#39;hello&#39;, &#39;next&#39;: &#39;world}),</span>
</span><span id="ArgsManager-182"><a href="#ArgsManager-182"><span class="linenos">182</span></a><span class="sd">            EKwargs(a=&#39;hello&#39;, b=&#39;world&#39;)</span>
</span><span id="ArgsManager-183"><a href="#ArgsManager-183"><span class="linenos">183</span></a><span class="sd">        )</span>
</span><span id="ArgsManager-184"><a href="#ArgsManager-184"><span class="linenos">184</span></a>
</span><span id="ArgsManager-185"><a href="#ArgsManager-185"><span class="linenos">185</span></a><span class="sd">    Example:</span>
</span><span id="ArgsManager-186"><a href="#ArgsManager-186"><span class="linenos">186</span></a><span class="sd">        class Item(Enum):</span>
</span><span id="ArgsManager-187"><a href="#ArgsManager-187"><span class="linenos">187</span></a><span class="sd">            Div = 0</span>
</span><span id="ArgsManager-188"><a href="#ArgsManager-188"><span class="linenos">188</span></a><span class="sd">            Button = 1</span>
</span><span id="ArgsManager-189"><a href="#ArgsManager-189"><span class="linenos">189</span></a><span class="sd">        </span>
</span><span id="ArgsManager-190"><a href="#ArgsManager-190"><span class="linenos">190</span></a><span class="sd">        def html(item, color, size, step=None, length=None, strength=None) -&gt; Any:</span>
</span><span id="ArgsManager-191"><a href="#ArgsManager-191"><span class="linenos">191</span></a><span class="sd">            ...</span>
</span><span id="ArgsManager-192"><a href="#ArgsManager-192"><span class="linenos">192</span></a><span class="sd">        </span>
</span><span id="ArgsManager-193"><a href="#ArgsManager-193"><span class="linenos">193</span></a><span class="sd">        am = ArgsManager(</span>
</span><span id="ArgsManager-194"><a href="#ArgsManager-194"><span class="linenos">194</span></a><span class="sd">            EKwargs({&#39;size&#39;: 12, &#39;step&#39;: &#39;one&#39;}),</span>
</span><span id="ArgsManager-195"><a href="#ArgsManager-195"><span class="linenos">195</span></a><span class="sd">            EKwargs(color=&#39;green&#39;, strength=24)</span>
</span><span id="ArgsManager-196"><a href="#ArgsManager-196"><span class="linenos">196</span></a><span class="sd">        )</span>
</span><span id="ArgsManager-197"><a href="#ArgsManager-197"><span class="linenos">197</span></a><span class="sd">        </span>
</span><span id="ArgsManager-198"><a href="#ArgsManager-198"><span class="linenos">198</span></a><span class="sd">        page = list()</span>
</span><span id="ArgsManager-199"><a href="#ArgsManager-199"><span class="linenos">199</span></a><span class="sd">        page.append(am(html, Item.Div))</span>
</span><span id="ArgsManager-200"><a href="#ArgsManager-200"><span class="linenos">200</span></a><span class="sd">        page.append(am(html, Item.Button))</span>
</span><span id="ArgsManager-201"><a href="#ArgsManager-201"><span class="linenos">201</span></a><span class="sd">        # The same as:</span>
</span><span id="ArgsManager-202"><a href="#ArgsManager-202"><span class="linenos">202</span></a><span class="sd">        # page = list()</span>
</span><span id="ArgsManager-203"><a href="#ArgsManager-203"><span class="linenos">203</span></a><span class="sd">        # page.append(html(Item.Div, &#39;green&#39;, 12, &#39;one&#39;, strength=24))</span>
</span><span id="ArgsManager-204"><a href="#ArgsManager-204"><span class="linenos">204</span></a><span class="sd">        # page.append(html(Item.Button, &#39;green&#39;, 12, &#39;one&#39;, strength=24))</span>
</span><span id="ArgsManager-205"><a href="#ArgsManager-205"><span class="linenos">205</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="ArgsManager-206"><a href="#ArgsManager-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="ArgsManager-207"><a href="#ArgsManager-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span>
</span><span id="ArgsManager-208"><a href="#ArgsManager-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ArgsManager-209"><a href="#ArgsManager-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ArgsManager-210"><a href="#ArgsManager-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ArgsManager-211"><a href="#ArgsManager-211"><span class="linenos">211</span></a>    
</span><span id="ArgsManager-212"><a href="#ArgsManager-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="nf">append</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager-213"><a href="#ArgsManager-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="ArgsManager-214"><a href="#ArgsManager-214"><span class="linenos">214</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="ArgsManager-215"><a href="#ArgsManager-215"><span class="linenos">215</span></a>    
</span><span id="ArgsManager-216"><a href="#ArgsManager-216"><span class="linenos">216</span></a>    <span class="k">def</span> <span class="nf">append_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager-217"><a href="#ArgsManager-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="ArgsManager-218"><a href="#ArgsManager-218"><span class="linenos">218</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="ArgsManager-219"><a href="#ArgsManager-219"><span class="linenos">219</span></a>    
</span><span id="ArgsManager-220"><a href="#ArgsManager-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">add_interceptor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager-221"><a href="#ArgsManager-221"><span class="linenos">221</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="ArgsManager-222"><a href="#ArgsManager-222"><span class="linenos">222</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="ArgsManager-223"><a href="#ArgsManager-223"><span class="linenos">223</span></a>    
</span><span id="ArgsManager-224"><a href="#ArgsManager-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">add_interceptor_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager-225"><a href="#ArgsManager-225"><span class="linenos">225</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="ArgsManager-226"><a href="#ArgsManager-226"><span class="linenos">226</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="ArgsManager-227"><a href="#ArgsManager-227"><span class="linenos">227</span></a>    
</span><span id="ArgsManager-228"><a href="#ArgsManager-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="nf">callable</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="ArgsManager-229"><a href="#ArgsManager-229"><span class="linenos">229</span></a>        <span class="k">def</span> <span class="nf">callable_entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ArgsManager-230"><a href="#ArgsManager-230"><span class="linenos">230</span></a>            <span class="n">original_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">args</span><span class="p">),</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="ArgsManager-231"><a href="#ArgsManager-231"><span class="linenos">231</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="p">:</span>
</span><span id="ArgsManager-232"><a href="#ArgsManager-232"><span class="linenos">232</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-233"><a href="#ArgsManager-233"><span class="linenos">233</span></a>                
</span><span id="ArgsManager-234"><a href="#ArgsManager-234"><span class="linenos">234</span></a>            <span class="n">one_shot_managers_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span>
</span><span id="ArgsManager-235"><a href="#ArgsManager-235"><span class="linenos">235</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_managers_buff</span><span class="p">)()</span>
</span><span id="ArgsManager-236"><a href="#ArgsManager-236"><span class="linenos">236</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="n">one_shot_managers_buff</span><span class="p">:</span>
</span><span id="ArgsManager-237"><a href="#ArgsManager-237"><span class="linenos">237</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-238"><a href="#ArgsManager-238"><span class="linenos">238</span></a>            
</span><span id="ArgsManager-239"><a href="#ArgsManager-239"><span class="linenos">239</span></a>            <span class="n">resulting_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-240"><a href="#ArgsManager-240"><span class="linenos">240</span></a>            <span class="n">instance</span> <span class="o">=</span> <span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-241"><a href="#ArgsManager-241"><span class="linenos">241</span></a>            
</span><span id="ArgsManager-242"><a href="#ArgsManager-242"><span class="linenos">242</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="p">:</span>
</span><span id="ArgsManager-243"><a href="#ArgsManager-243"><span class="linenos">243</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="ArgsManager-244"><a href="#ArgsManager-244"><span class="linenos">244</span></a>            
</span><span id="ArgsManager-245"><a href="#ArgsManager-245"><span class="linenos">245</span></a>            <span class="n">one_shot_interceptors_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span>
</span><span id="ArgsManager-246"><a href="#ArgsManager-246"><span class="linenos">246</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_interceptors_buff</span><span class="p">)()</span>
</span><span id="ArgsManager-247"><a href="#ArgsManager-247"><span class="linenos">247</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="n">one_shot_interceptors_buff</span><span class="p">:</span>
</span><span id="ArgsManager-248"><a href="#ArgsManager-248"><span class="linenos">248</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="ArgsManager-249"><a href="#ArgsManager-249"><span class="linenos">249</span></a>            
</span><span id="ArgsManager-250"><a href="#ArgsManager-250"><span class="linenos">250</span></a>            <span class="k">return</span> <span class="n">instance</span>
</span><span id="ArgsManager-251"><a href="#ArgsManager-251"><span class="linenos">251</span></a>        <span class="k">return</span> <span class="n">callable_entity</span>
</span><span id="ArgsManager-252"><a href="#ArgsManager-252"><span class="linenos">252</span></a>    
</span><span id="ArgsManager-253"><a href="#ArgsManager-253"><span class="linenos">253</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ArgsManager-254"><a href="#ArgsManager-254"><span class="linenos">254</span></a>        <span class="n">original_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">args</span><span class="p">),</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="ArgsManager-255"><a href="#ArgsManager-255"><span class="linenos">255</span></a>        <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="p">:</span>
</span><span id="ArgsManager-256"><a href="#ArgsManager-256"><span class="linenos">256</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-257"><a href="#ArgsManager-257"><span class="linenos">257</span></a>            
</span><span id="ArgsManager-258"><a href="#ArgsManager-258"><span class="linenos">258</span></a>        <span class="n">one_shot_managers_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span>
</span><span id="ArgsManager-259"><a href="#ArgsManager-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_managers_buff</span><span class="p">)()</span>
</span><span id="ArgsManager-260"><a href="#ArgsManager-260"><span class="linenos">260</span></a>        <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="n">one_shot_managers_buff</span><span class="p">:</span>
</span><span id="ArgsManager-261"><a href="#ArgsManager-261"><span class="linenos">261</span></a>            <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-262"><a href="#ArgsManager-262"><span class="linenos">262</span></a>        
</span><span id="ArgsManager-263"><a href="#ArgsManager-263"><span class="linenos">263</span></a>        <span class="n">resulting_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-264"><a href="#ArgsManager-264"><span class="linenos">264</span></a>        <span class="n">instance</span> <span class="o">=</span> <span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager-265"><a href="#ArgsManager-265"><span class="linenos">265</span></a>        <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="p">:</span>
</span><span id="ArgsManager-266"><a href="#ArgsManager-266"><span class="linenos">266</span></a>            <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="ArgsManager-267"><a href="#ArgsManager-267"><span class="linenos">267</span></a>        
</span><span id="ArgsManager-268"><a href="#ArgsManager-268"><span class="linenos">268</span></a>        <span class="k">return</span> <span class="n">instance</span>
</span></pre></div>


            <div class="docstring"><p>Usage:
    am = ArgsManager(
        EKwargs({'a': 'hello', 'next': 'world}),
        EKwargs(a='hello', b='world')
    )</p>

<p>Example:
    class Item(Enum):
        Div = 0
        Button = 1</p>

<pre><code>def html(item, color, size, step=None, length=None, strength=None) -&gt; Any:
    ...

am = ArgsManager(
    EKwargs({'size': 12, 'step': 'one'}),
    EKwargs(color='green', strength=24)
)

page = list()
page.append(am(html, Item.Div))
page.append(am(html, Item.Button))
# The same as:
# page = list()
# page.append(html(Item.Div, 'green', 12, 'one', strength=24))
# page.append(html(Item.Button, 'green', 12, 'one', strength=24))
</code></pre>
</div>


                            <div id="ArgsManager.__init__" class="classattr">
                                        <input id="ArgsManager.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ArgsManager</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span></span>)</span>

                <label class="view-source-button" for="ArgsManager.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.__init__-206"><a href="#ArgsManager.__init__-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
</span><span id="ArgsManager.__init__-207"><a href="#ArgsManager.__init__-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">)</span>
</span><span id="ArgsManager.__init__-208"><a href="#ArgsManager.__init__-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ArgsManager.__init__-209"><a href="#ArgsManager.__init__-209"><span class="linenos">209</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="ArgsManager.__init__-210"><a href="#ArgsManager.__init__-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsManager.managers" class="classattr">
                                <div class="attr variable">
            <span class="name">managers</span>

        
    </div>
    <a class="headerlink" href="#ArgsManager.managers"></a>
    
    

                            </div>
                            <div id="ArgsManager.one_shot_managers" class="classattr">
                                <div class="attr variable">
            <span class="name">one_shot_managers</span>

        
    </div>
    <a class="headerlink" href="#ArgsManager.one_shot_managers"></a>
    
    

                            </div>
                            <div id="ArgsManager.interceptors" class="classattr">
                                <div class="attr variable">
            <span class="name">interceptors</span>

        
    </div>
    <a class="headerlink" href="#ArgsManager.interceptors"></a>
    
    

                            </div>
                            <div id="ArgsManager.one_shot_interceptors" class="classattr">
                                <div class="attr variable">
            <span class="name">one_shot_interceptors</span>

        
    </div>
    <a class="headerlink" href="#ArgsManager.one_shot_interceptors"></a>
    
    

                            </div>
                            <div id="ArgsManager.append" class="classattr">
                                        <input id="ArgsManager.append-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">append</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">manager</span></span><span class="return-annotation">) -> <span class="n"><a href="#ArgsManager">ArgsManager</a></span>:</span></span>

                <label class="view-source-button" for="ArgsManager.append-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.append"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.append-212"><a href="#ArgsManager.append-212"><span class="linenos">212</span></a>    <span class="k">def</span> <span class="nf">append</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager.append-213"><a href="#ArgsManager.append-213"><span class="linenos">213</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="ArgsManager.append-214"><a href="#ArgsManager.append-214"><span class="linenos">214</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsManager.append_one_shot" class="classattr">
                                        <input id="ArgsManager.append_one_shot-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">append_one_shot</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">manager</span></span><span class="return-annotation">) -> <span class="n"><a href="#ArgsManager">ArgsManager</a></span>:</span></span>

                <label class="view-source-button" for="ArgsManager.append_one_shot-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.append_one_shot"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.append_one_shot-216"><a href="#ArgsManager.append_one_shot-216"><span class="linenos">216</span></a>    <span class="k">def</span> <span class="nf">append_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager.append_one_shot-217"><a href="#ArgsManager.append_one_shot-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">manager</span><span class="p">)</span>
</span><span id="ArgsManager.append_one_shot-218"><a href="#ArgsManager.append_one_shot-218"><span class="linenos">218</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsManager.add_interceptor" class="classattr">
                                        <input id="ArgsManager.add_interceptor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_interceptor</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interceptor</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n"><a href="#ArgsManager">ArgsManager</a></span>:</span></span>

                <label class="view-source-button" for="ArgsManager.add_interceptor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.add_interceptor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.add_interceptor-220"><a href="#ArgsManager.add_interceptor-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="nf">add_interceptor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager.add_interceptor-221"><a href="#ArgsManager.add_interceptor-221"><span class="linenos">221</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="ArgsManager.add_interceptor-222"><a href="#ArgsManager.add_interceptor-222"><span class="linenos">222</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsManager.add_interceptor_one_shot" class="classattr">
                                        <input id="ArgsManager.add_interceptor_one_shot-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_interceptor_one_shot</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interceptor</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n"><a href="#ArgsManager">ArgsManager</a></span>:</span></span>

                <label class="view-source-button" for="ArgsManager.add_interceptor_one_shot-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.add_interceptor_one_shot"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.add_interceptor_one_shot-224"><a href="#ArgsManager.add_interceptor_one_shot-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">add_interceptor_one_shot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interceptor</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;ArgsManager&#39;</span><span class="p">:</span>
</span><span id="ArgsManager.add_interceptor_one_shot-225"><a href="#ArgsManager.add_interceptor_one_shot-225"><span class="linenos">225</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">interceptor</span><span class="p">)</span>
</span><span id="ArgsManager.add_interceptor_one_shot-226"><a href="#ArgsManager.add_interceptor_one_shot-226"><span class="linenos">226</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsManager.callable" class="classattr">
                                        <input id="ArgsManager.callable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">callable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="ArgsManager.callable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsManager.callable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsManager.callable-228"><a href="#ArgsManager.callable-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="nf">callable</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity</span><span class="p">:</span> <span class="n">EntityWithExtendableArgs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="ArgsManager.callable-229"><a href="#ArgsManager.callable-229"><span class="linenos">229</span></a>        <span class="k">def</span> <span class="nf">callable_entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ArgsManager.callable-230"><a href="#ArgsManager.callable-230"><span class="linenos">230</span></a>            <span class="n">original_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">args</span><span class="p">),</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">))</span>
</span><span id="ArgsManager.callable-231"><a href="#ArgsManager.callable-231"><span class="linenos">231</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">managers</span><span class="p">:</span>
</span><span id="ArgsManager.callable-232"><a href="#ArgsManager.callable-232"><span class="linenos">232</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager.callable-233"><a href="#ArgsManager.callable-233"><span class="linenos">233</span></a>                
</span><span id="ArgsManager.callable-234"><a href="#ArgsManager.callable-234"><span class="linenos">234</span></a>            <span class="n">one_shot_managers_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span>
</span><span id="ArgsManager.callable-235"><a href="#ArgsManager.callable-235"><span class="linenos">235</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_managers</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_managers_buff</span><span class="p">)()</span>
</span><span id="ArgsManager.callable-236"><a href="#ArgsManager.callable-236"><span class="linenos">236</span></a>            <span class="k">for</span> <span class="n">manager</span> <span class="ow">in</span> <span class="n">one_shot_managers_buff</span><span class="p">:</span>
</span><span id="ArgsManager.callable-237"><a href="#ArgsManager.callable-237"><span class="linenos">237</span></a>                <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">manager</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager.callable-238"><a href="#ArgsManager.callable-238"><span class="linenos">238</span></a>            
</span><span id="ArgsManager.callable-239"><a href="#ArgsManager.callable-239"><span class="linenos">239</span></a>            <span class="n">resulting_args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager.callable-240"><a href="#ArgsManager.callable-240"><span class="linenos">240</span></a>            <span class="n">instance</span> <span class="o">=</span> <span class="n">entity</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="ArgsManager.callable-241"><a href="#ArgsManager.callable-241"><span class="linenos">241</span></a>            
</span><span id="ArgsManager.callable-242"><a href="#ArgsManager.callable-242"><span class="linenos">242</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">interceptors</span><span class="p">:</span>
</span><span id="ArgsManager.callable-243"><a href="#ArgsManager.callable-243"><span class="linenos">243</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="ArgsManager.callable-244"><a href="#ArgsManager.callable-244"><span class="linenos">244</span></a>            
</span><span id="ArgsManager.callable-245"><a href="#ArgsManager.callable-245"><span class="linenos">245</span></a>            <span class="n">one_shot_interceptors_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span>
</span><span id="ArgsManager.callable-246"><a href="#ArgsManager.callable-246"><span class="linenos">246</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">one_shot_interceptors</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">one_shot_interceptors_buff</span><span class="p">)()</span>
</span><span id="ArgsManager.callable-247"><a href="#ArgsManager.callable-247"><span class="linenos">247</span></a>            <span class="k">for</span> <span class="n">interceptor</span> <span class="ow">in</span> <span class="n">one_shot_interceptors_buff</span><span class="p">:</span>
</span><span id="ArgsManager.callable-248"><a href="#ArgsManager.callable-248"><span class="linenos">248</span></a>                <span class="n">interceptor</span><span class="p">(</span><span class="n">instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">,</span> <span class="n">original_args</span><span class="p">,</span> <span class="n">resulting_args</span><span class="p">)</span>
</span><span id="ArgsManager.callable-249"><a href="#ArgsManager.callable-249"><span class="linenos">249</span></a>            
</span><span id="ArgsManager.callable-250"><a href="#ArgsManager.callable-250"><span class="linenos">250</span></a>            <span class="k">return</span> <span class="n">instance</span>
</span><span id="ArgsManager.callable-251"><a href="#ArgsManager.callable-251"><span class="linenos">251</span></a>        <span class="k">return</span> <span class="n">callable_entity</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="merge_func_args">
                            <input id="merge_func_args-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">merge_func_args</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func_list</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Tuple</span>:</span></span>

                <label class="view-source-button" for="merge_func_args-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#merge_func_args"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="merge_func_args-271"><a href="#merge_func_args-271"><span class="linenos">271</span></a><span class="k">def</span> <span class="nf">merge_func_args</span><span class="p">(</span><span class="n">func_list</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Callable</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">:</span>
</span><span id="merge_func_args-272"><a href="#merge_func_args-272"><span class="linenos">272</span></a>    <span class="n">args</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="merge_func_args-273"><a href="#merge_func_args-273"><span class="linenos">273</span></a>    <span class="n">default_args</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="merge_func_args-274"><a href="#merge_func_args-274"><span class="linenos">274</span></a>    <span class="k">for</span> <span class="n">func</span> <span class="ow">in</span> <span class="n">func_list</span><span class="p">:</span>
</span><span id="merge_func_args-275"><a href="#merge_func_args-275"><span class="linenos">275</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="merge_func_args-276"><a href="#merge_func_args-276"><span class="linenos">276</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="merge_func_args-277"><a href="#merge_func_args-277"><span class="linenos">277</span></a>            <span class="n">is_method</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="merge_func_args-278"><a href="#merge_func_args-278"><span class="linenos">278</span></a>        <span class="k">elif</span> <span class="nb">callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="merge_func_args-279"><a href="#merge_func_args-279"><span class="linenos">279</span></a>            <span class="n">is_method</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="merge_func_args-280"><a href="#merge_func_args-280"><span class="linenos">280</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="merge_func_args-281"><a href="#merge_func_args-281"><span class="linenos">281</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Is not callable: </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">func</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="merge_func_args-282"><a href="#merge_func_args-282"><span class="linenos">282</span></a>        <span class="n">varnames</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="merge_func_args-283"><a href="#merge_func_args-283"><span class="linenos">283</span></a>        <span class="k">if</span> <span class="n">is_method</span><span class="p">:</span>
</span><span id="merge_func_args-284"><a href="#merge_func_args-284"><span class="linenos">284</span></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">varnames</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="merge_func_args-285"><a href="#merge_func_args-285"><span class="linenos">285</span></a>                <span class="k">if</span> <span class="s1">&#39;self&#39;</span> <span class="o">==</span> <span class="n">varnames</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="merge_func_args-286"><a href="#merge_func_args-286"><span class="linenos">286</span></a>                    <span class="n">varnames</span> <span class="o">=</span> <span class="n">varnames</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="merge_func_args-287"><a href="#merge_func_args-287"><span class="linenos">287</span></a>        <span class="n">spec</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getfullargspec</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="merge_func_args-288"><a href="#merge_func_args-288"><span class="linenos">288</span></a>        <span class="c1"># print(f&#39;ArgSpec:&#39;)</span>
</span><span id="merge_func_args-289"><a href="#merge_func_args-289"><span class="linenos">289</span></a>        <span class="c1"># pprint(spec)</span>
</span><span id="merge_func_args-290"><a href="#merge_func_args-290"><span class="linenos">290</span></a>        
</span><span id="merge_func_args-291"><a href="#merge_func_args-291"><span class="linenos">291</span></a>        <span class="k">if</span> <span class="n">spec</span><span class="o">.</span><span class="n">defaults</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="merge_func_args-292"><a href="#merge_func_args-292"><span class="linenos">292</span></a>            <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">)</span>
</span><span id="merge_func_args-293"><a href="#merge_func_args-293"><span class="linenos">293</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="merge_func_args-294"><a href="#merge_func_args-294"><span class="linenos">294</span></a>            <span class="n">defaults_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">spec</span><span class="o">.</span><span class="n">defaults</span><span class="p">)</span>
</span><span id="merge_func_args-295"><a href="#merge_func_args-295"><span class="linenos">295</span></a>            <span class="n">args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">[:</span><span class="o">-</span><span class="n">defaults_len</span><span class="p">])</span>
</span><span id="merge_func_args-296"><a href="#merge_func_args-296"><span class="linenos">296</span></a>            <span class="n">default_args</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">varnames</span><span class="p">[</span><span class="o">-</span><span class="n">defaults_len</span><span class="p">:])</span>
</span><span id="merge_func_args-297"><a href="#merge_func_args-297"><span class="linenos">297</span></a>    <span class="c1"># print(f&#39;Args:&#39;)</span>
</span><span id="merge_func_args-298"><a href="#merge_func_args-298"><span class="linenos">298</span></a>    <span class="c1"># pprint(args)</span>
</span><span id="merge_func_args-299"><a href="#merge_func_args-299"><span class="linenos">299</span></a>    <span class="c1"># print(f&#39;Default args:&#39;)</span>
</span><span id="merge_func_args-300"><a href="#merge_func_args-300"><span class="linenos">300</span></a>    <span class="c1"># pprint(default_args)</span>
</span><span id="merge_func_args-301"><a href="#merge_func_args-301"><span class="linenos">301</span></a>    <span class="k">return</span> <span class="n">args</span> <span class="o">+</span> <span class="n">default_args</span>
</span></pre></div>


    

                </section>
                <section id="interested_args_to_kwargs">
                            <input id="interested_args_to_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">interested_args_to_kwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">interested_args</span>, </span><span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="interested_args_to_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#interested_args_to_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="interested_args_to_kwargs-304"><a href="#interested_args_to_kwargs-304"><span class="linenos">304</span></a><span class="k">def</span> <span class="nf">interested_args_to_kwargs</span><span class="p">(</span><span class="n">interested_args</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="interested_args_to_kwargs-305"><a href="#interested_args_to_kwargs-305"><span class="linenos">305</span></a>    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="interested_args_to_kwargs-306"><a href="#interested_args_to_kwargs-306"><span class="linenos">306</span></a>    <span class="n">absent_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="interested_args_to_kwargs-307"><a href="#interested_args_to_kwargs-307"><span class="linenos">307</span></a>    <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">interested_args</span><span class="p">:</span>
</span><span id="interested_args_to_kwargs-308"><a href="#interested_args_to_kwargs-308"><span class="linenos">308</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="interested_args_to_kwargs-309"><a href="#interested_args_to_kwargs-309"><span class="linenos">309</span></a>            <span class="n">absent_args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="interested_args_to_kwargs-310"><a href="#interested_args_to_kwargs-310"><span class="linenos">310</span></a>    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">absent_args</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>
</span><span id="interested_args_to_kwargs-311"><a href="#interested_args_to_kwargs-311"><span class="linenos">311</span></a>    <span class="k">return</span> <span class="n">kwargs</span>
</span></pre></div>


    

                </section>
                <section id="func_args_to_kwargs">
                            <input id="func_args_to_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_args_to_kwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span>, </span><span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="func_args_to_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_args_to_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_args_to_kwargs-314"><a href="#func_args_to_kwargs-314"><span class="linenos">314</span></a><span class="k">def</span> <span class="nf">func_args_to_kwargs</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="func_args_to_kwargs-315"><a href="#func_args_to_kwargs-315"><span class="linenos">315</span></a>    <span class="n">kwargs</span> <span class="o">=</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="func_args_to_kwargs-316"><a href="#func_args_to_kwargs-316"><span class="linenos">316</span></a>    <span class="n">interested_names</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="func_args_to_kwargs-317"><a href="#func_args_to_kwargs-317"><span class="linenos">317</span></a>    <span class="n">is_method</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="func_args_to_kwargs-318"><a href="#func_args_to_kwargs-318"><span class="linenos">318</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="func_args_to_kwargs-319"><a href="#func_args_to_kwargs-319"><span class="linenos">319</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="func_args_to_kwargs-320"><a href="#func_args_to_kwargs-320"><span class="linenos">320</span></a>    <span class="k">elif</span> <span class="nb">callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="func_args_to_kwargs-321"><a href="#func_args_to_kwargs-321"><span class="linenos">321</span></a>        <span class="n">is_method</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="func_args_to_kwargs-322"><a href="#func_args_to_kwargs-322"><span class="linenos">322</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="func_args_to_kwargs-323"><a href="#func_args_to_kwargs-323"><span class="linenos">323</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Is not callable: </span><span class="si">{</span><span class="nb">repr</span><span class="p">(</span><span class="n">func</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="func_args_to_kwargs-324"><a href="#func_args_to_kwargs-324"><span class="linenos">324</span></a>    
</span><span id="func_args_to_kwargs-325"><a href="#func_args_to_kwargs-325"><span class="linenos">325</span></a>    <span class="n">kwargs</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">interested_names</span><span class="p">,</span> <span class="n">args</span><span class="p">))</span>
</span><span id="func_args_to_kwargs-326"><a href="#func_args_to_kwargs-326"><span class="linenos">326</span></a>    <span class="n">not_needed_names</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">interested_names</span><span class="p">)</span>
</span><span id="func_args_to_kwargs-327"><a href="#func_args_to_kwargs-327"><span class="linenos">327</span></a>    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">not_needed_names</span><span class="p">:</span>
</span><span id="func_args_to_kwargs-328"><a href="#func_args_to_kwargs-328"><span class="linenos">328</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="func_args_to_kwargs-329"><a href="#func_args_to_kwargs-329"><span class="linenos">329</span></a>    <span class="k">if</span> <span class="n">is_method</span><span class="p">:</span>
</span><span id="func_args_to_kwargs-330"><a href="#func_args_to_kwargs-330"><span class="linenos">330</span></a>        <span class="n">kwargs</span><span class="o">.</span><span class="n">pop</span><span class="p">(</span><span class="s1">&#39;self&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="func_args_to_kwargs-331"><a href="#func_args_to_kwargs-331"><span class="linenos">331</span></a>    <span class="k">return</span> <span class="n">kwargs</span>
</span></pre></div>


    

                </section>
                <section id="number_of_provided_args">
                            <input id="number_of_provided_args-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">number_of_provided_args</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="number_of_provided_args-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#number_of_provided_args"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="number_of_provided_args-334"><a href="#number_of_provided_args-334"><span class="linenos">334</span></a><span class="k">def</span> <span class="nf">number_of_provided_args</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
</span><span id="number_of_provided_args-335"><a href="#number_of_provided_args-335"><span class="linenos">335</span></a>    <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="args_kwargs">
                            <input id="args_kwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">args_kwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="args_kwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#args_kwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="args_kwargs-338"><a href="#args_kwargs-338"><span class="linenos">338</span></a><span class="k">def</span> <span class="nf">args_kwargs</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="args_kwargs-339"><a href="#args_kwargs-339"><span class="linenos">339</span></a>    <span class="k">return</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span>
</span></pre></div>


    

                </section>
                <section id="args_kwargs_to_str">
                            <input id="args_kwargs_to_str-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">args_kwargs_to_str</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">args</span>, </span><span class="param"><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="args_kwargs_to_str-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#args_kwargs_to_str"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="args_kwargs_to_str-342"><a href="#args_kwargs_to_str-342"><span class="linenos">342</span></a><span class="k">def</span> <span class="nf">args_kwargs_to_str</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-343"><a href="#args_kwargs_to_str-343"><span class="linenos">343</span></a>    <span class="k">if</span> <span class="n">args</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-344"><a href="#args_kwargs_to_str-344"><span class="linenos">344</span></a>        <span class="n">args_str</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">])</span>
</span><span id="args_kwargs_to_str-345"><a href="#args_kwargs_to_str-345"><span class="linenos">345</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-346"><a href="#args_kwargs_to_str-346"><span class="linenos">346</span></a>        <span class="n">args_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="args_kwargs_to_str-347"><a href="#args_kwargs_to_str-347"><span class="linenos">347</span></a>    
</span><span id="args_kwargs_to_str-348"><a href="#args_kwargs_to_str-348"><span class="linenos">348</span></a>    <span class="k">if</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-349"><a href="#args_kwargs_to_str-349"><span class="linenos">349</span></a>        <span class="n">kwargs_str</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
</span><span id="args_kwargs_to_str-350"><a href="#args_kwargs_to_str-350"><span class="linenos">350</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-351"><a href="#args_kwargs_to_str-351"><span class="linenos">351</span></a>        <span class="n">kwargs_str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="args_kwargs_to_str-352"><a href="#args_kwargs_to_str-352"><span class="linenos">352</span></a>    
</span><span id="args_kwargs_to_str-353"><a href="#args_kwargs_to_str-353"><span class="linenos">353</span></a>    <span class="k">if</span> <span class="n">kwargs_str</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-354"><a href="#args_kwargs_to_str-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">args_str</span><span class="si">}</span><span class="s1">, </span><span class="si">{</span><span class="n">kwargs_str</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="args_kwargs_to_str-355"><a href="#args_kwargs_to_str-355"><span class="linenos">355</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="args_kwargs_to_str-356"><a href="#args_kwargs_to_str-356"><span class="linenos">356</span></a>        <span class="k">return</span> <span class="n">args_str</span>
</span></pre></div>


    

                </section>
                <section id="ArgsKwargs">
                            <input id="ArgsKwargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ArgsKwargs</span>:

                <label class="view-source-button" for="ArgsKwargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsKwargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsKwargs-359"><a href="#ArgsKwargs-359"><span class="linenos">359</span></a><span class="k">class</span> <span class="nc">ArgsKwargs</span><span class="p">:</span>
</span><span id="ArgsKwargs-360"><a href="#ArgsKwargs-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ArgsKwargs-361"><a href="#ArgsKwargs-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ArgsKwargs-362"><a href="#ArgsKwargs-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span><span id="ArgsKwargs-363"><a href="#ArgsKwargs-363"><span class="linenos">363</span></a>    
</span><span id="ArgsKwargs-364"><a href="#ArgsKwargs-364"><span class="linenos">364</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="ArgsKwargs-365"><a href="#ArgsKwargs-365"><span class="linenos">365</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="ArgsKwargs.__init__" class="classattr">
                                        <input id="ArgsKwargs.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">ArgsKwargs</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="ArgsKwargs.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ArgsKwargs.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ArgsKwargs.__init__-360"><a href="#ArgsKwargs.__init__-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="ArgsKwargs.__init__-361"><a href="#ArgsKwargs.__init__-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="ArgsKwargs.__init__-362"><a href="#ArgsKwargs.__init__-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div id="ArgsKwargs.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span><span class="annotation">: Tuple</span>

        
    </div>
    <a class="headerlink" href="#ArgsKwargs.args"></a>
    
    

                            </div>
                            <div id="ArgsKwargs.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span><span class="annotation">: Dict</span>

        
    </div>
    <a class="headerlink" href="#ArgsKwargs.kwargs"></a>
    
    

                            </div>
                </section>
                <section id="AK">
                    <div class="attr variable">
            <span class="name">AK</span>        =
<span class="default_value">&lt;class &#39;<a href="#ArgsKwargs">ArgsKwargs</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#AK"></a>
    
    

                </section>
                <section id="prepare_arguments_positions">
                            <input id="prepare_arguments_positions-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">prepare_arguments_positions</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">positional</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">keyword_only</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="prepare_arguments_positions-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#prepare_arguments_positions"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="prepare_arguments_positions-371"><a href="#prepare_arguments_positions-371"><span class="linenos">371</span></a><span class="k">def</span> <span class="nf">prepare_arguments_positions</span><span class="p">(</span><span class="n">positional</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">keyword_only</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]]:</span>
</span><span id="prepare_arguments_positions-372"><a href="#prepare_arguments_positions-372"><span class="linenos">372</span></a>    <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="prepare_arguments_positions-373"><a href="#prepare_arguments_positions-373"><span class="linenos">373</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="prepare_arguments_positions-374"><a href="#prepare_arguments_positions-374"><span class="linenos">374</span></a>        <span class="n">positions</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="prepare_arguments_positions-375"><a href="#prepare_arguments_positions-375"><span class="linenos">375</span></a>    
</span><span id="prepare_arguments_positions-376"><a href="#prepare_arguments_positions-376"><span class="linenos">376</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">):</span>
</span><span id="prepare_arguments_positions-377"><a href="#prepare_arguments_positions-377"><span class="linenos">377</span></a>        <span class="n">positions</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="prepare_arguments_positions-378"><a href="#prepare_arguments_positions-378"><span class="linenos">378</span></a>
</span><span id="prepare_arguments_positions-379"><a href="#prepare_arguments_positions-379"><span class="linenos">379</span></a>    <span class="k">return</span> <span class="n">positions</span>
</span></pre></div>


    

                </section>
                <section id="UnknownArgumentError">
                            <input id="UnknownArgumentError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnknownArgumentError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="UnknownArgumentError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnknownArgumentError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnknownArgumentError-382"><a href="#UnknownArgumentError-382"><span class="linenos">382</span></a><span class="k">class</span> <span class="nc">UnknownArgumentError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="UnknownArgumentError-383"><a href="#UnknownArgumentError-383"><span class="linenos">383</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="UnknownArgumentError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnknownArgumentError.with_traceback" class="function">with_traceback</dd>
                <dd id="UnknownArgumentError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="find_arg_position_and_value">
                            <input id="find_arg_position_and_value-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_arg_position_and_value</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">positions</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>,</span><span class="param">	<span class="n">args</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span>,</span><span class="param">	<span class="n">kwargs</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="find_arg_position_and_value-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_arg_position_and_value"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_arg_position_and_value-386"><a href="#find_arg_position_and_value-386"><span class="linenos">386</span></a><span class="k">def</span> <span class="nf">find_arg_position_and_value</span><span class="p">(</span><span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]],</span> <span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="find_arg_position_and_value-387"><a href="#find_arg_position_and_value-387"><span class="linenos">387</span></a><span class="w">    </span>
</span><span id="find_arg_position_and_value-388"><a href="#find_arg_position_and_value-388"><span class="linenos">388</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="find_arg_position_and_value-389"><a href="#find_arg_position_and_value-389"><span class="linenos">389</span></a><span class="sd">    Example:</span>
</span><span id="find_arg_position_and_value-390"><a href="#find_arg_position_and_value-390"><span class="linenos">390</span></a><span class="sd">        from cengal.introspection.inspect import func_param_names, CodeParamNames</span>
</span><span id="find_arg_position_and_value-391"><a href="#find_arg_position_and_value-391"><span class="linenos">391</span></a><span class="sd">        from cengal.code_flow_control.args_manager import prepare_arguments_positions, find_arg_position_and_value, UnknownArgumentError</span>
</span><span id="find_arg_position_and_value-392"><a href="#find_arg_position_and_value-392"><span class="linenos">392</span></a><span class="sd">        </span>
</span><span id="find_arg_position_and_value-393"><a href="#find_arg_position_and_value-393"><span class="linenos">393</span></a><span class="sd">        def wrapper(arg_name: str = &#39;b&#39;, *args, **kwargs):</span>
</span><span id="find_arg_position_and_value-394"><a href="#find_arg_position_and_value-394"><span class="linenos">394</span></a><span class="sd">            def my_func(a, b, *, c, d):</span>
</span><span id="find_arg_position_and_value-395"><a href="#find_arg_position_and_value-395"><span class="linenos">395</span></a><span class="sd">                ...</span>
</span><span id="find_arg_position_and_value-396"><a href="#find_arg_position_and_value-396"><span class="linenos">396</span></a>
</span><span id="find_arg_position_and_value-397"><a href="#find_arg_position_and_value-397"><span class="linenos">397</span></a><span class="sd">            params: CodeParamNames = func_param_names(my_func)</span>
</span><span id="find_arg_position_and_value-398"><a href="#find_arg_position_and_value-398"><span class="linenos">398</span></a><span class="sd">            positoins: Dict[str, Optional[int]] = prepare_arguments_positions(params.positional, params.keyword_only)</span>
</span><span id="find_arg_position_and_value-399"><a href="#find_arg_position_and_value-399"><span class="linenos">399</span></a><span class="sd">            found, pos, value = find_arg_position_and_value(arg_name, positoins)</span>
</span><span id="find_arg_position_and_value-400"><a href="#find_arg_position_and_value-400"><span class="linenos">400</span></a><span class="sd">            if found:</span>
</span><span id="find_arg_position_and_value-401"><a href="#find_arg_position_and_value-401"><span class="linenos">401</span></a><span class="sd">                print(f&#39;Value of &lt;{arg_name}&gt; : {value}&#39;)</span>
</span><span id="find_arg_position_and_value-402"><a href="#find_arg_position_and_value-402"><span class="linenos">402</span></a><span class="sd">            </span>
</span><span id="find_arg_position_and_value-403"><a href="#find_arg_position_and_value-403"><span class="linenos">403</span></a><span class="sd">            if pos is not None:</span>
</span><span id="find_arg_position_and_value-404"><a href="#find_arg_position_and_value-404"><span class="linenos">404</span></a><span class="sd">                print(f&#39;&lt;{arg_name}&gt; found as a positional argument at position {pos}&#39;)</span>
</span><span id="find_arg_position_and_value-405"><a href="#find_arg_position_and_value-405"><span class="linenos">405</span></a><span class="sd">            </span>
</span><span id="find_arg_position_and_value-406"><a href="#find_arg_position_and_value-406"><span class="linenos">406</span></a><span class="sd">            return my_func(*args, **kwargs)</span>
</span><span id="find_arg_position_and_value-407"><a href="#find_arg_position_and_value-407"><span class="linenos">407</span></a>
</span><span id="find_arg_position_and_value-408"><a href="#find_arg_position_and_value-408"><span class="linenos">408</span></a><span class="sd">        wrapper(&#39;a&#39;)</span>
</span><span id="find_arg_position_and_value-409"><a href="#find_arg_position_and_value-409"><span class="linenos">409</span></a><span class="sd">        wrapper(&#39;a&#39;, 1, 2, 3, 4)</span>
</span><span id="find_arg_position_and_value-410"><a href="#find_arg_position_and_value-410"><span class="linenos">410</span></a><span class="sd">        wrapper(&#39;d&#39;)</span>
</span><span id="find_arg_position_and_value-411"><a href="#find_arg_position_and_value-411"><span class="linenos">411</span></a><span class="sd">        wrapper(&#39;d&#39;, 1, 2, 3, 4)</span>
</span><span id="find_arg_position_and_value-412"><a href="#find_arg_position_and_value-412"><span class="linenos">412</span></a><span class="sd">        try:</span>
</span><span id="find_arg_position_and_value-413"><a href="#find_arg_position_and_value-413"><span class="linenos">413</span></a><span class="sd">            wrapper(&#39;asdf&#39;)</span>
</span><span id="find_arg_position_and_value-414"><a href="#find_arg_position_and_value-414"><span class="linenos">414</span></a><span class="sd">        except UnknownArgumentError as ex:</span>
</span><span id="find_arg_position_and_value-415"><a href="#find_arg_position_and_value-415"><span class="linenos">415</span></a><span class="sd">            print(&#39;&lt;{ex.args[1]}&gt; is not a valid argument for my_func(). Valid arguments are: {ex.args[2]}&#39;)</span>
</span><span id="find_arg_position_and_value-416"><a href="#find_arg_position_and_value-416"><span class="linenos">416</span></a><span class="sd">            raise</span>
</span><span id="find_arg_position_and_value-417"><a href="#find_arg_position_and_value-417"><span class="linenos">417</span></a>
</span><span id="find_arg_position_and_value-418"><a href="#find_arg_position_and_value-418"><span class="linenos">418</span></a><span class="sd">    Args:</span>
</span><span id="find_arg_position_and_value-419"><a href="#find_arg_position_and_value-419"><span class="linenos">419</span></a><span class="sd">        arg_name (str): _description_</span>
</span><span id="find_arg_position_and_value-420"><a href="#find_arg_position_and_value-420"><span class="linenos">420</span></a><span class="sd">        positions (Dict[str, Optional[int]]): _description_</span>
</span><span id="find_arg_position_and_value-421"><a href="#find_arg_position_and_value-421"><span class="linenos">421</span></a><span class="sd">        args (Tuple): _description_</span>
</span><span id="find_arg_position_and_value-422"><a href="#find_arg_position_and_value-422"><span class="linenos">422</span></a><span class="sd">        kwargs (Dict): _description_</span>
</span><span id="find_arg_position_and_value-423"><a href="#find_arg_position_and_value-423"><span class="linenos">423</span></a>
</span><span id="find_arg_position_and_value-424"><a href="#find_arg_position_and_value-424"><span class="linenos">424</span></a><span class="sd">    Raises:</span>
</span><span id="find_arg_position_and_value-425"><a href="#find_arg_position_and_value-425"><span class="linenos">425</span></a><span class="sd">        UnknownArgumentError: _description_</span>
</span><span id="find_arg_position_and_value-426"><a href="#find_arg_position_and_value-426"><span class="linenos">426</span></a>
</span><span id="find_arg_position_and_value-427"><a href="#find_arg_position_and_value-427"><span class="linenos">427</span></a><span class="sd">    Returns:</span>
</span><span id="find_arg_position_and_value-428"><a href="#find_arg_position_and_value-428"><span class="linenos">428</span></a><span class="sd">        Tuple[bool, bool, Optional[int], Any]: _description_</span>
</span><span id="find_arg_position_and_value-429"><a href="#find_arg_position_and_value-429"><span class="linenos">429</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="find_arg_position_and_value-430"><a href="#find_arg_position_and_value-430"><span class="linenos">430</span></a>    <span class="n">found</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_arg_position_and_value-431"><a href="#find_arg_position_and_value-431"><span class="linenos">431</span></a>    <span class="n">pos</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_arg_position_and_value-432"><a href="#find_arg_position_and_value-432"><span class="linenos">432</span></a>    <span class="n">value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_arg_position_and_value-433"><a href="#find_arg_position_and_value-433"><span class="linenos">433</span></a>
</span><span id="find_arg_position_and_value-434"><a href="#find_arg_position_and_value-434"><span class="linenos">434</span></a>    <span class="n">original_arg_pos</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_arg_position_and_value-435"><a href="#find_arg_position_and_value-435"><span class="linenos">435</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-436"><a href="#find_arg_position_and_value-436"><span class="linenos">436</span></a>        <span class="n">original_arg_pos</span> <span class="o">=</span> <span class="n">positions</span><span class="p">[</span><span class="n">arg_name</span><span class="p">]</span>
</span><span id="find_arg_position_and_value-437"><a href="#find_arg_position_and_value-437"><span class="linenos">437</span></a>    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-438"><a href="#find_arg_position_and_value-438"><span class="linenos">438</span></a>        <span class="n">valid_arguments</span> <span class="o">=</span> <span class="n">positions</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
</span><span id="find_arg_position_and_value-439"><a href="#find_arg_position_and_value-439"><span class="linenos">439</span></a>        <span class="k">raise</span> <span class="n">UnknownArgumentError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;&lt;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">&gt; is not in </span><span class="si">{</span><span class="n">valid_arguments</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">arg_name</span><span class="p">,</span> <span class="n">valid_arguments</span><span class="p">)</span>
</span><span id="find_arg_position_and_value-440"><a href="#find_arg_position_and_value-440"><span class="linenos">440</span></a>    
</span><span id="find_arg_position_and_value-441"><a href="#find_arg_position_and_value-441"><span class="linenos">441</span></a>    <span class="k">if</span> <span class="n">original_arg_pos</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-442"><a href="#find_arg_position_and_value-442"><span class="linenos">442</span></a>        <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_arg_position_and_value-443"><a href="#find_arg_position_and_value-443"><span class="linenos">443</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-444"><a href="#find_arg_position_and_value-444"><span class="linenos">444</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">original_arg_pos</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-445"><a href="#find_arg_position_and_value-445"><span class="linenos">445</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_arg_position_and_value-446"><a href="#find_arg_position_and_value-446"><span class="linenos">446</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-447"><a href="#find_arg_position_and_value-447"><span class="linenos">447</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_arg_position_and_value-448"><a href="#find_arg_position_and_value-448"><span class="linenos">448</span></a>    
</span><span id="find_arg_position_and_value-449"><a href="#find_arg_position_and_value-449"><span class="linenos">449</span></a>    <span class="k">if</span> <span class="n">found_in_args</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-450"><a href="#find_arg_position_and_value-450"><span class="linenos">450</span></a>        <span class="n">pos</span> <span class="o">=</span> <span class="n">original_arg_pos</span>
</span><span id="find_arg_position_and_value-451"><a href="#find_arg_position_and_value-451"><span class="linenos">451</span></a>        <span class="n">value</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">pos</span><span class="p">]</span>
</span><span id="find_arg_position_and_value-452"><a href="#find_arg_position_and_value-452"><span class="linenos">452</span></a>        <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_arg_position_and_value-453"><a href="#find_arg_position_and_value-453"><span class="linenos">453</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-454"><a href="#find_arg_position_and_value-454"><span class="linenos">454</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-455"><a href="#find_arg_position_and_value-455"><span class="linenos">455</span></a>            <span class="n">value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">arg_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="find_arg_position_and_value-456"><a href="#find_arg_position_and_value-456"><span class="linenos">456</span></a>            <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_arg_position_and_value-457"><a href="#find_arg_position_and_value-457"><span class="linenos">457</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="find_arg_position_and_value-458"><a href="#find_arg_position_and_value-458"><span class="linenos">458</span></a>            <span class="k">pass</span>
</span><span id="find_arg_position_and_value-459"><a href="#find_arg_position_and_value-459"><span class="linenos">459</span></a>    
</span><span id="find_arg_position_and_value-460"><a href="#find_arg_position_and_value-460"><span class="linenos">460</span></a>    <span class="k">return</span> <span class="n">found</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">value</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    from cengal.introspection.inspect import func_param_names, CodeParamNames
    from cengal.code_flow_control.args_manager import prepare_arguments_positions, find_arg_position_and_value, UnknownArgumentError</p>

<pre><code>def wrapper(arg_name: str = 'b', *args, **kwargs):
    def my_func(a, b, *, c, d):
        ...

    params: CodeParamNames = func_param_names(my_func)
    positoins: Dict[str, Optional[int]] = prepare_arguments_positions(params.positional, params.keyword_only)
    found, pos, value = find_arg_position_and_value(arg_name, positoins)
    if found:
        print(f'Value of &lt;{arg_name}&gt; : {value}')

    if pos is not None:
        print(f'&lt;{arg_name}&gt; found as a positional argument at position {pos}')

    return my_func(*args, **kwargs)

wrapper('a')
wrapper('a', 1, 2, 3, 4)
wrapper('d')
wrapper('d', 1, 2, 3, 4)
try:
    wrapper('asdf')
except UnknownArgumentError as ex:
    print('&lt;{ex.args[1]}&gt; is not a valid argument for my_func(). Valid arguments are: {ex.args[2]}')
    raise
</code></pre>

<p>Args:
    arg_name (str): _description_
    positions (Dict[str, Optional[int]]): _description_
    args (Tuple): _description_
    kwargs (Dict): _description_</p>

<p>Raises:
    UnknownArgumentError: _description_</p>

<p>Returns:
    Tuple[bool, bool, Optional[int], Any]: _description_</p>
</div>


                </section>
                <section id="try_find_arg_position_and_value">
                            <input id="try_find_arg_position_and_value-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_find_arg_position_and_value</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">positions</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]]</span>,</span><span class="param">	<span class="n">args</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span>,</span><span class="param">	<span class="n">kwargs</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">],</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="try_find_arg_position_and_value-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#try_find_arg_position_and_value"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="try_find_arg_position_and_value-463"><a href="#try_find_arg_position_and_value-463"><span class="linenos">463</span></a><span class="k">def</span> <span class="nf">try_find_arg_position_and_value</span><span class="p">(</span><span class="n">arg_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">positions</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]],</span> <span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="try_find_arg_position_and_value-464"><a href="#try_find_arg_position_and_value-464"><span class="linenos">464</span></a><span class="w">    </span>
</span><span id="try_find_arg_position_and_value-465"><a href="#try_find_arg_position_and_value-465"><span class="linenos">465</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="try_find_arg_position_and_value-466"><a href="#try_find_arg_position_and_value-466"><span class="linenos">466</span></a><span class="sd">    Example:</span>
</span><span id="try_find_arg_position_and_value-467"><a href="#try_find_arg_position_and_value-467"><span class="linenos">467</span></a><span class="sd">        from cengal.introspection.inspect import func_param_names, CodeParamNames</span>
</span><span id="try_find_arg_position_and_value-468"><a href="#try_find_arg_position_and_value-468"><span class="linenos">468</span></a><span class="sd">        from cengal.code_flow_control.args_manager import prepare_arguments_positions, try_find_arg_position_and_value</span>
</span><span id="try_find_arg_position_and_value-469"><a href="#try_find_arg_position_and_value-469"><span class="linenos">469</span></a><span class="sd">        </span>
</span><span id="try_find_arg_position_and_value-470"><a href="#try_find_arg_position_and_value-470"><span class="linenos">470</span></a><span class="sd">        def wrapper(arg_name: str = &#39;b&#39;, *args, **kwargs):</span>
</span><span id="try_find_arg_position_and_value-471"><a href="#try_find_arg_position_and_value-471"><span class="linenos">471</span></a><span class="sd">            def my_func(a, b, *, c, d):</span>
</span><span id="try_find_arg_position_and_value-472"><a href="#try_find_arg_position_and_value-472"><span class="linenos">472</span></a><span class="sd">                ...</span>
</span><span id="try_find_arg_position_and_value-473"><a href="#try_find_arg_position_and_value-473"><span class="linenos">473</span></a>
</span><span id="try_find_arg_position_and_value-474"><a href="#try_find_arg_position_and_value-474"><span class="linenos">474</span></a><span class="sd">            params: CodeParamNames = func_param_names(my_func)</span>
</span><span id="try_find_arg_position_and_value-475"><a href="#try_find_arg_position_and_value-475"><span class="linenos">475</span></a><span class="sd">            positoins: Dict[str, Optional[int]] = find_entity_arguments_positions(params.positional, params.keyword_only)</span>
</span><span id="try_find_arg_position_and_value-476"><a href="#try_find_arg_position_and_value-476"><span class="linenos">476</span></a><span class="sd">            valid, found, pos, value = find_arg_position_and_value(arg_name, positoins)</span>
</span><span id="try_find_arg_position_and_value-477"><a href="#try_find_arg_position_and_value-477"><span class="linenos">477</span></a><span class="sd">            if valid:</span>
</span><span id="try_find_arg_position_and_value-478"><a href="#try_find_arg_position_and_value-478"><span class="linenos">478</span></a><span class="sd">                if found:</span>
</span><span id="try_find_arg_position_and_value-479"><a href="#try_find_arg_position_and_value-479"><span class="linenos">479</span></a><span class="sd">                    print(f&#39;Value of &lt;{arg_name}&gt; : {value}&#39;)</span>
</span><span id="try_find_arg_position_and_value-480"><a href="#try_find_arg_position_and_value-480"><span class="linenos">480</span></a><span class="sd">                </span>
</span><span id="try_find_arg_position_and_value-481"><a href="#try_find_arg_position_and_value-481"><span class="linenos">481</span></a><span class="sd">                if pos is not None:</span>
</span><span id="try_find_arg_position_and_value-482"><a href="#try_find_arg_position_and_value-482"><span class="linenos">482</span></a><span class="sd">                    print(f&#39;&lt;{arg_name}&gt; found as a positional argument at position {pos}&#39;)</span>
</span><span id="try_find_arg_position_and_value-483"><a href="#try_find_arg_position_and_value-483"><span class="linenos">483</span></a><span class="sd">            else:</span>
</span><span id="try_find_arg_position_and_value-484"><a href="#try_find_arg_position_and_value-484"><span class="linenos">484</span></a><span class="sd">                print(&#39;&lt;{arg_name}&gt; is not a valid argument for my_func(). Valid arguments are: {positoins.keys()}&#39;)</span>
</span><span id="try_find_arg_position_and_value-485"><a href="#try_find_arg_position_and_value-485"><span class="linenos">485</span></a><span class="sd">            </span>
</span><span id="try_find_arg_position_and_value-486"><a href="#try_find_arg_position_and_value-486"><span class="linenos">486</span></a><span class="sd">            return my_func(*args, **kwargs)</span>
</span><span id="try_find_arg_position_and_value-487"><a href="#try_find_arg_position_and_value-487"><span class="linenos">487</span></a>
</span><span id="try_find_arg_position_and_value-488"><a href="#try_find_arg_position_and_value-488"><span class="linenos">488</span></a><span class="sd">        wrapper(&#39;a&#39;)</span>
</span><span id="try_find_arg_position_and_value-489"><a href="#try_find_arg_position_and_value-489"><span class="linenos">489</span></a><span class="sd">        wrapper(&#39;a&#39;, 1, 2, 3, 4)</span>
</span><span id="try_find_arg_position_and_value-490"><a href="#try_find_arg_position_and_value-490"><span class="linenos">490</span></a><span class="sd">        wrapper(&#39;d&#39;)</span>
</span><span id="try_find_arg_position_and_value-491"><a href="#try_find_arg_position_and_value-491"><span class="linenos">491</span></a><span class="sd">        wrapper(&#39;d&#39;, 1, 2, 3, 4)</span>
</span><span id="try_find_arg_position_and_value-492"><a href="#try_find_arg_position_and_value-492"><span class="linenos">492</span></a><span class="sd">        wrapper(&#39;asdf&#39;)</span>
</span><span id="try_find_arg_position_and_value-493"><a href="#try_find_arg_position_and_value-493"><span class="linenos">493</span></a>
</span><span id="try_find_arg_position_and_value-494"><a href="#try_find_arg_position_and_value-494"><span class="linenos">494</span></a><span class="sd">    Args:</span>
</span><span id="try_find_arg_position_and_value-495"><a href="#try_find_arg_position_and_value-495"><span class="linenos">495</span></a><span class="sd">        arg_name (str): _description_</span>
</span><span id="try_find_arg_position_and_value-496"><a href="#try_find_arg_position_and_value-496"><span class="linenos">496</span></a><span class="sd">        positions (Dict[str, Optional[int]]): _description_</span>
</span><span id="try_find_arg_position_and_value-497"><a href="#try_find_arg_position_and_value-497"><span class="linenos">497</span></a><span class="sd">        args (Tuple): _description_</span>
</span><span id="try_find_arg_position_and_value-498"><a href="#try_find_arg_position_and_value-498"><span class="linenos">498</span></a><span class="sd">        kwargs (Dict): _description_</span>
</span><span id="try_find_arg_position_and_value-499"><a href="#try_find_arg_position_and_value-499"><span class="linenos">499</span></a>
</span><span id="try_find_arg_position_and_value-500"><a href="#try_find_arg_position_and_value-500"><span class="linenos">500</span></a><span class="sd">    Returns:</span>
</span><span id="try_find_arg_position_and_value-501"><a href="#try_find_arg_position_and_value-501"><span class="linenos">501</span></a><span class="sd">        Tuple[bool, bool, Optional[int], Any]: _description_</span>
</span><span id="try_find_arg_position_and_value-502"><a href="#try_find_arg_position_and_value-502"><span class="linenos">502</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="try_find_arg_position_and_value-503"><a href="#try_find_arg_position_and_value-503"><span class="linenos">503</span></a>    <span class="n">valid</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="try_find_arg_position_and_value-504"><a href="#try_find_arg_position_and_value-504"><span class="linenos">504</span></a>    <span class="n">found</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="try_find_arg_position_and_value-505"><a href="#try_find_arg_position_and_value-505"><span class="linenos">505</span></a>    <span class="n">pos</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="try_find_arg_position_and_value-506"><a href="#try_find_arg_position_and_value-506"><span class="linenos">506</span></a>    <span class="n">value</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="try_find_arg_position_and_value-507"><a href="#try_find_arg_position_and_value-507"><span class="linenos">507</span></a>
</span><span id="try_find_arg_position_and_value-508"><a href="#try_find_arg_position_and_value-508"><span class="linenos">508</span></a>    <span class="n">original_arg_pos</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="try_find_arg_position_and_value-509"><a href="#try_find_arg_position_and_value-509"><span class="linenos">509</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-510"><a href="#try_find_arg_position_and_value-510"><span class="linenos">510</span></a>        <span class="n">original_arg_pos</span> <span class="o">=</span> <span class="n">positions</span><span class="p">[</span><span class="n">arg_name</span><span class="p">]</span>
</span><span id="try_find_arg_position_and_value-511"><a href="#try_find_arg_position_and_value-511"><span class="linenos">511</span></a>        <span class="n">valid</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="try_find_arg_position_and_value-512"><a href="#try_find_arg_position_and_value-512"><span class="linenos">512</span></a>    <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-513"><a href="#try_find_arg_position_and_value-513"><span class="linenos">513</span></a>        <span class="k">pass</span>
</span><span id="try_find_arg_position_and_value-514"><a href="#try_find_arg_position_and_value-514"><span class="linenos">514</span></a>    
</span><span id="try_find_arg_position_and_value-515"><a href="#try_find_arg_position_and_value-515"><span class="linenos">515</span></a>    <span class="k">if</span> <span class="n">original_arg_pos</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-516"><a href="#try_find_arg_position_and_value-516"><span class="linenos">516</span></a>        <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="try_find_arg_position_and_value-517"><a href="#try_find_arg_position_and_value-517"><span class="linenos">517</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-518"><a href="#try_find_arg_position_and_value-518"><span class="linenos">518</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">original_arg_pos</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-519"><a href="#try_find_arg_position_and_value-519"><span class="linenos">519</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="try_find_arg_position_and_value-520"><a href="#try_find_arg_position_and_value-520"><span class="linenos">520</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-521"><a href="#try_find_arg_position_and_value-521"><span class="linenos">521</span></a>            <span class="n">found_in_args</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="try_find_arg_position_and_value-522"><a href="#try_find_arg_position_and_value-522"><span class="linenos">522</span></a>    
</span><span id="try_find_arg_position_and_value-523"><a href="#try_find_arg_position_and_value-523"><span class="linenos">523</span></a>    <span class="k">if</span> <span class="n">found_in_args</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-524"><a href="#try_find_arg_position_and_value-524"><span class="linenos">524</span></a>        <span class="n">pos</span> <span class="o">=</span> <span class="n">original_arg_pos</span>
</span><span id="try_find_arg_position_and_value-525"><a href="#try_find_arg_position_and_value-525"><span class="linenos">525</span></a>        <span class="n">value</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">pos</span><span class="p">]</span>
</span><span id="try_find_arg_position_and_value-526"><a href="#try_find_arg_position_and_value-526"><span class="linenos">526</span></a>        <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="try_find_arg_position_and_value-527"><a href="#try_find_arg_position_and_value-527"><span class="linenos">527</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-528"><a href="#try_find_arg_position_and_value-528"><span class="linenos">528</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-529"><a href="#try_find_arg_position_and_value-529"><span class="linenos">529</span></a>            <span class="n">value</span> <span class="o">=</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">arg_name</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="try_find_arg_position_and_value-530"><a href="#try_find_arg_position_and_value-530"><span class="linenos">530</span></a>            <span class="n">found</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="try_find_arg_position_and_value-531"><a href="#try_find_arg_position_and_value-531"><span class="linenos">531</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="try_find_arg_position_and_value-532"><a href="#try_find_arg_position_and_value-532"><span class="linenos">532</span></a>            <span class="k">pass</span>
</span><span id="try_find_arg_position_and_value-533"><a href="#try_find_arg_position_and_value-533"><span class="linenos">533</span></a>    
</span><span id="try_find_arg_position_and_value-534"><a href="#try_find_arg_position_and_value-534"><span class="linenos">534</span></a>    <span class="k">return</span> <span class="n">valid</span><span class="p">,</span> <span class="n">found</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">value</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    from cengal.introspection.inspect import func_param_names, CodeParamNames
    from cengal.code_flow_control.args_manager import prepare_arguments_positions, try_find_arg_position_and_value</p>

<pre><code>def wrapper(arg_name: str = 'b', *args, **kwargs):
    def my_func(a, b, *, c, d):
        ...

    params: CodeParamNames = func_param_names(my_func)
    positoins: Dict[str, Optional[int]] = find_entity_arguments_positions(params.positional, params.keyword_only)
    valid, found, pos, value = find_arg_position_and_value(arg_name, positoins)
    if valid:
        if found:
            print(f'Value of &lt;{arg_name}&gt; : {value}')

        if pos is not None:
            print(f'&lt;{arg_name}&gt; found as a positional argument at position {pos}')
    else:
        print('&lt;{arg_name}&gt; is not a valid argument for my_func(). Valid arguments are: {positoins.keys()}')

    return my_func(*args, **kwargs)

wrapper('a')
wrapper('a', 1, 2, 3, 4)
wrapper('d')
wrapper('d', 1, 2, 3, 4)
wrapper('asdf')
</code></pre>

<p>Args:
    arg_name (str): _description_
    positions (Dict[str, Optional[int]]): _description_
    args (Tuple): _description_
    kwargs (Dict): _description_</p>

<p>Returns:
    Tuple[bool, bool, Optional[int], Any]: _description_</p>
</div>


                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>