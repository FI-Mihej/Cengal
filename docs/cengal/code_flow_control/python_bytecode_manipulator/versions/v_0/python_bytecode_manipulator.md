---
title: python_bytecode_manipulator
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.python_bytecode_manipulator<wbr>.versions<wbr>.v_0<wbr>.python_bytecode_manipulator    </h1>

                
                        <input id="mod-python_bytecode_manipulator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-python_bytecode_manipulator-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">from</span> <span class="nn">dis</span> <span class="kn">import</span> <span class="n">Instruction</span><span class="p">,</span> <span class="n">dis</span><span class="p">,</span> <span class="n">get_instructions</span><span class="p">,</span> <span class="n">_get_code_object</span><span class="p">,</span> <span class="n">code_info</span><span class="p">,</span> <span class="n">show_code</span><span class="p">,</span> <span class="n">findlabels</span><span class="p">,</span> <span class="n">_unpack_opargs</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">from</span> <span class="nn">opcode</span> <span class="kn">import</span> <span class="n">hasjrel</span><span class="p">,</span> <span class="n">hasjabs</span><span class="p">,</span> <span class="n">opname</span><span class="p">,</span> <span class="n">opmap</span><span class="p">,</span> <span class="n">HAVE_ARGUMENT</span><span class="p">,</span> <span class="n">EXTENDED_ARG</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">cengal.system</span> <span class="kn">import</span> <span class="n">PYTHON_VERSION_INT</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Sequence</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">CodeType</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">copy</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">from</span> <span class="nn">cengal.entities.copyable</span> <span class="kn">import</span> <span class="n">CopyableMixin</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.front_triggerable_variable</span> <span class="kn">import</span> <span class="n">FrontTriggerableVariableType</span><span class="p">,</span> <span class="n">FrontTriggerableVariable</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="sd">Module Docstring</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">BytecodeSequence</span> <span class="o">=</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]]]</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="k">def</span> <span class="nf">patch_function</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">co_code</span><span class="p">):</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span> <span class="o">=</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="n">co_code</span><span class="p">,</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_consts</span><span class="p">,</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_names</span><span class="p">,</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">,</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="p">)</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="n">CodeParamNames</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s2">&quot;CodeParamNames&quot;</span><span class="p">,</span> <span class="s2">&quot;positional positional_only keyword_only&quot;</span><span class="p">)</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="k">def</span> <span class="nf">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="n">pos_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_argcount</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="n">arg_names</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="n">positional</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[:</span><span class="n">pos_count</span><span class="p">]</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="n">posonly_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_posonlyargcount</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    <span class="n">positional_only</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[:</span><span class="n">posonly_count</span><span class="p">]</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="n">keyword_only_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[</span><span class="n">pos_count</span><span class="p">:</span><span class="n">pos_count</span> <span class="o">+</span> <span class="n">keyword_only_count</span><span class="p">]</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">return</span> <span class="n">CodeParamNames</span><span class="p">(</span><span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="k">def</span> <span class="nf">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="k">return</span> <span class="n">code</span><span class="o">.</span><span class="n">co_name</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&gt;=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>    <span class="k">def</span> <span class="nf">code_qualname</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="k">return</span> <span class="n">code</span><span class="o">.</span><span class="n">co_qualname</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="k">def</span> <span class="nf">get_code</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeType</span><span class="p">:</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>        <span class="k">return</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>        <span class="k">return</span> <span class="n">x</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="vm">__code__</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">gi_code</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">ag_code</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine, or</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cr_code</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;f_code&#39;</span><span class="p">):</span>  <span class="c1">#...a frame.</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>    <span class="c1"># else:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>    <span class="c1">#     raise TypeError(f&#39;Expected a code object or an entity with code, but got {type(x)}&#39;)</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">return</span> <span class="n">x</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="k">def</span> <span class="nf">has_code</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine, or</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;f_code&#39;</span><span class="p">):</span>  <span class="c1">#...a frame.</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="c1"># else:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="c1">#     raise TypeError(f&#39;Expected a code object or an entity with code, but got {type(x)}&#39;)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>    
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>    <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a><span class="k">class</span> <span class="nc">CodeTypeEnum</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="n">class_or_module</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="n">code_object</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="n">raw_bytecode</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="n">source_code</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="n">unknown</span> <span class="o">=</span> <span class="mi">4</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">code_type</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeTypeEnum</span><span class="p">]:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">    Args:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">        x (_type_, optional): result of get_code() function. Defaults to None.</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="sd">    Returns:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="sd">        Optional[CodeTypeEnum]: _description_</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="k">return</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    <span class="c1"># Perform the disassembly.</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__dict__&#39;</span><span class="p">):</span>  <span class="c1"># Class or module</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">class_or_module</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;co_code&#39;</span><span class="p">):</span> <span class="c1"># Code object</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">code_object</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">)):</span> <span class="c1"># Raw bytecode</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">raw_bytecode</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>    <span class="c1"># Source code</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">source_code</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">unknown</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="k">def</span> <span class="nf">set_code</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="n">x</span><span class="o">.</span><span class="vm">__func__</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="n">x</span><span class="o">.</span><span class="vm">__code__</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">gi_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">ag_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine.</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">cr_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="k">return</span> <span class="n">x</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&lt;</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a><span class="c1"># if (3, 11) &gt; PYTHON_VERSION_INT[:1]:</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    <span class="k">def</span> <span class="nf">modify_code</span><span class="p">(</span><span class="n">original_code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">,</span> <span class="n">co_code</span><span class="p">,</span> <span class="n">co_consts</span><span class="p">,</span> <span class="n">co_names</span><span class="p">,</span> <span class="n">co_varnames</span><span class="p">):</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="n">co_nlocals</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">return</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_posonlyargcount</span><span class="p">,</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>            <span class="n">co_code</span><span class="p">,</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_consts</span><span class="p">),</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_names</span><span class="p">),</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">),</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    <span class="c1"># def unpack_opargs_original(code, denormalize_values: bool = False):</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>    <span class="c1">#     ftv: FrontTriggerableVariable = FrontTriggerableVariable(FrontTriggerableVariableType.equal, EXTENDED_ARG)</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="c1">#     extended_arg = 0</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="c1">#     real_op_index: Optional[int] = None</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="c1">#     real_byte_index: Optional[int] = None</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>    <span class="c1">#     need_to_clear_real_data: bool = False</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>    <span class="c1">#     op_index = -1</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>    <span class="c1">#     for i in range(0, len(code), 2):</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>    <span class="c1">#         op_index += 1</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>    <span class="c1">#         op = code[i]</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>    <span class="c1">#         if op &gt;= HAVE_ARGUMENT:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>    <span class="c1">#             ftv_result: Optional[bool] = ftv(op)</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="c1">#             if ftv_result is True:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>    <span class="c1">#                 real_op_index = op_index</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>    <span class="c1">#                 real_byte_index = i</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>    <span class="c1">#             elif ftv_result is False:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>    <span class="c1">#                 need_to_clear_real_data = True</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="c1">#             arg = code[i+1] | extended_arg</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>    <span class="c1">#             if denormalize_values:</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    <span class="c1">#                 extended_arg = (arg &lt;&lt; 8) if op == EXTENDED_ARG else 0</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>    <span class="c1">#         else:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>    <span class="c1">#             arg = None</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="c1">#         yield (op, arg, op_index, i, real_op_index, real_byte_index)</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>    <span class="c1">#         if need_to_clear_real_data:</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>    <span class="c1">#             real_op_index = None</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>    <span class="c1">#             real_byte_index = None</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>    <span class="c1">#             need_to_clear_real_data = False</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">,</span> <span class="n">denormalize_values</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="n">ftv</span><span class="p">:</span> <span class="n">FrontTriggerableVariable</span> <span class="o">=</span> <span class="n">FrontTriggerableVariable</span><span class="p">(</span><span class="n">FrontTriggerableVariableType</span><span class="o">.</span><span class="n">equal</span><span class="p">,</span> <span class="n">EXTENDED_ARG</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="n">extended_arg</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="n">real_op_index</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="n">real_offset</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="n">need_to_clear_real_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="n">op</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="n">op_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="n">i</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">code</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>                <span class="n">item</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>                <span class="n">op</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>                <span class="n">op_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">i</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>                <span class="k">continue</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>            <span class="k">if</span> <span class="n">op</span> <span class="o">&gt;=</span> <span class="n">HAVE_ARGUMENT</span><span class="p">:</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>                <span class="n">ftv_result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ftv</span><span class="p">(</span><span class="n">op</span><span class="p">)</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="k">if</span> <span class="n">ftv_result</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>                    <span class="n">real_op_index</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>                    <span class="n">real_offset</span> <span class="o">=</span> <span class="n">offset</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>                <span class="k">elif</span> <span class="n">ftv_result</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>                    <span class="n">need_to_clear_real_data</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="n">item</span> <span class="o">|</span> <span class="n">extended_arg</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>                <span class="k">if</span> <span class="n">denormalize_values</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>                    <span class="n">extended_arg</span> <span class="o">=</span> <span class="p">(</span><span class="n">arg</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="k">if</span> <span class="n">op</span> <span class="o">==</span> <span class="n">EXTENDED_ARG</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>            <span class="k">yield</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span><span class="p">)</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="k">if</span> <span class="n">need_to_clear_real_data</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                <span class="n">real_op_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>                <span class="n">real_offset</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>                <span class="n">need_to_clear_real_data</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]]:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="n">labels</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>        <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>        <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span> <span class="ow">in</span> <span class="n">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>                <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">offset</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">+</span> <span class="n">arg</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>                <span class="k">elif</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjabs</span><span class="p">:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                    <span class="k">continue</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>                <span class="k">if</span> <span class="n">label</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="p">:</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>                    <span class="n">labels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>                    <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>                <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span><span class="p">))</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>        <span class="k">return</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>    
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    <span class="k">def</span> <span class="nf">op_index_to_arg</span><span class="p">(</span><span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>        <span class="k">return</span> <span class="n">op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    <span class="k">def</span> <span class="nf">arg_to_op_index</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="k">return</span> <span class="n">arg</span> <span class="o">//</span> <span class="mi">2</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a><span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">==</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>    <span class="kn">from</span> <span class="nn">dis</span> <span class="kn">import</span> <span class="n">_is_backward_jump</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">):</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="n">labels</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="n">op_by_label</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        <span class="k">for</span> <span class="n">offset</span><span class="p">,</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">_unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">):</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>                <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>                    <span class="k">if</span> <span class="n">_is_backward_jump</span><span class="p">(</span><span class="n">op</span><span class="p">):</span>  <span class="c1"># inefficient implementation of the _is_backward_jump() function. Need to use set or list instead of string manipulations</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>                        <span class="n">arg</span> <span class="o">=</span> <span class="o">-</span><span class="n">arg</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">offset</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">+</span> <span class="n">arg</span><span class="o">*</span><span class="mi">2</span>  <span class="c1"># In 3.10: this is an instruction index - not a byte index. Need to be fixed and tested</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>                <span class="k">elif</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjabs</span><span class="p">:</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">arg</span><span class="o">*</span><span class="mi">2</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>                    <span class="k">continue</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>                <span class="k">if</span> <span class="n">label</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="p">:</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>                    <span class="n">labels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>                    <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>                <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">))</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="k">return</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a><span class="k">else</span><span class="p">:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>    <span class="kn">import</span> <span class="nn">warnings</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported Python Version: </span><span class="si">{</span><span class="n">PYTHON_VERSION_INT</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="c1"># raise RuntimeError(f&#39;Unsupported Python Version: {PYTHON_VERSION_INT}&#39;)</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a><span class="k">class</span> <span class="nc">OpSequenceOffsetMap</span><span class="p">(</span><span class="n">CopyableMixin</span><span class="p">):</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_num</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">op_num</span><span class="p">)</span> <span class="k">if</span> <span class="n">op_num</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="k">if</span> <span class="n">op_num</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>            <span class="n">op_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>        <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">op_num</span><span class="p">):</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="c1"># bindex = index * 2</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>            <span class="n">bindex</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>    
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>    <span class="k">def</span> <span class="nf">mapped_range</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">slice</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">))</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>    
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">return</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="n">del_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="n">del_stop</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">op_num</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="n">to_be_deleted</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">original</span><span class="p">,</span> <span class="n">new</span><span class="p">))</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>        
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>        <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">new</span><span class="p">,</span> <span class="n">original</span><span class="p">))</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="n">ignored</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[:</span><span class="n">preserver_index_for_first_x_op</span><span class="p">]</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>            <span class="k">if</span> <span class="n">ignored</span><span class="p">:</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>                <span class="n">last_ignored</span> <span class="o">=</span> <span class="n">ignored</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>                <span class="n">last_ignored_new</span> <span class="o">=</span> <span class="n">last_ignored</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>                <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">last_ignored_new</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>            
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="o">-</span><span class="n">op_num</span><span class="p">,</span> <span class="n">offset_change_start</span><span class="p">)</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">-=</span> <span class="n">op_num</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_num</span><span class="p">)</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>    
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="nf">insert_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="k">return</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_num</span><span class="p">,</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">+=</span> <span class="n">op_num</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_num</span><span class="p">)</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>    
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">insertion_id</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="k">return</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="n">sequence_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">range</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="n">sequence_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">insert_slice</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="n">op_num</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span> <span class="o">+</span> <span class="n">offset</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">insertion_id</span><span class="p">,</span> <span class="n">new</span><span class="p">)</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>    
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>    <span class="k">def</span> <span class="nf">add_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_start</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>            <span class="k">return</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>            
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>            
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span> <span class="o">=</span> <span class="n">original</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>    
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>    
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>    <span class="k">def</span> <span class="nf">shift_to_absolute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>    
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>        <span class="k">if</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>            <span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>            <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>        
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>    
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>            <span class="n">index</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>        <span class="n">op_num</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_by_original_buff</span><span class="p">)()</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>            <span class="k">if</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>                <span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>        <span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">original_by_new_buff</span><span class="p">)()</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="k">if</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>                <span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span> <span class="o">=</span> <span class="n">original</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequenceOffsetMap</span><span class="p">()</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_num</span> <span class="o">=</span> <span class="n">op_num</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="n">new_by_original</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="n">original_by_new</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;new_by_original&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;original_by_new&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;op_num&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;range&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">)</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="k">def</span> <span class="nf">opcode</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>    <span class="k">return</span> <span class="n">opmap</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a><span class="k">def</span> <span class="nf">opcode_name</span><span class="p">(</span><span class="n">opcode</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>    <span class="k">return</span> <span class="n">opname</span><span class="p">[</span><span class="n">opcode</span><span class="p">]</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a><span class="k">class</span> <span class="nc">OpSequence</span><span class="p">:</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>    <span class="n">extended_arg_opcode_int</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">)</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>    <span class="n">extended_arg_opcode_byte</span> <span class="o">=</span> <span class="n">extended_arg_opcode_int</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span> <span class="k">if</span> <span class="n">op_sequence</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">op_sequence</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="n">OpSequenceOffsetMap</span> <span class="o">=</span> <span class="n">OpSequenceOffsetMap</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">))</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>    
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>    
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>    <span class="k">def</span> <span class="nf">read_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">:</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">()</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>    
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">place</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>    
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">:</span> <span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>        <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">insert_op_sequence_offset</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        <span class="k">return</span> <span class="n">op_sequence</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>    
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>    <span class="k">def</span> <span class="nf">normalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>                <span class="k">break</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>            <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>                <span class="k">if</span> <span class="n">arg</span> <span class="o">&gt;</span> <span class="mi">255</span><span class="p">:</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>                    <span class="k">if</span> <span class="n">real_op_index</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>                        <span class="n">real_op_index_delta</span> <span class="o">=</span> <span class="n">real_op_index</span> <span class="o">-</span> <span class="n">op_index</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>                        <span class="n">real_op_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">-</span> <span class="n">real_op_index_delta</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>                        <span class="n">slice_to_delete</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">real_op_index</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">slice_to_delete</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>                        <span class="n">index</span> <span class="o">=</span> <span class="n">real_op_index</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>                    <span class="n">extended_arg</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>                    <span class="n">extended_arg_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">,</span> <span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="n">index</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>                    <span class="n">op_sub_sequence_instructions</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>                    <span class="k">for</span> <span class="n">extended_arg_int</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">):</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>                        <span class="n">op_sub_sequence_instructions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">make_instruction</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">,</span> <span class="n">extended_arg_int</span><span class="p">))</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>                    
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>                    <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions_fast</span><span class="p">(</span><span class="n">op_sub_sequence_instructions</span><span class="p">)</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>                    <span class="n">index</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>    
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>    <span class="k">def</span> <span class="nf">denormalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>    
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>    <span class="k">def</span> <span class="nf">find_op</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>        <span class="n">start_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>        <span class="n">end_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>                <span class="k">break</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>                <span class="k">continue</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>                <span class="n">end_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>                <span class="k">break</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>        
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>        <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>            <span class="n">index</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                <span class="k">if</span> <span class="n">previous_op_is_extended_arg</span><span class="p">:</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>                    <span class="n">start_index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>                
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>                <span class="k">break</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>            
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>                <span class="k">continue</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>                <span class="n">start_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>                <span class="k">break</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>        
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">start_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">end_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>        
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="n">start_index</span><span class="p">,</span> <span class="n">end_index</span><span class="p">)</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>    
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>    <span class="k">def</span> <span class="nf">get_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>        
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>        
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>        <span class="n">op_slice</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>            <span class="n">arg_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>            <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">op_slice</span><span class="p">):</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>                <span class="n">arg_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>            
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>            <span class="k">return</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">arg_list</span><span class="p">))</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>            <span class="k">return</span> <span class="n">op_slice</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>    
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>    <span class="k">def</span> <span class="nf">set_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">],</span> <span class="n">new_arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]):</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>        
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>        <span class="n">op_index_len</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">op_index_len</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>        
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">new_arg</span><span class="p">)</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>        <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>        <span class="n">sub_op_sequence_bytes</span> <span class="o">=</span> <span class="p">[</span><span class="n">current_op</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">]</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>        <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">sub_op_sequence_bytes</span><span class="p">)))</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>        <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>        <span class="n">real_arg</span> <span class="o">=</span> <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>        <span class="n">sub_op_sequence_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>        <span class="n">extended_args_len</span> <span class="o">=</span> <span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>        <span class="k">if</span> <span class="n">extended_args_len</span><span class="p">:</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">+</span> <span class="n">extended_args_len</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_op</span><span class="p">,</span> <span class="n">real_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span><span class="p">)</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>        <span class="k">if</span> <span class="n">sub_op_sequence_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>            <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">sub_op_sequence_len</span><span class="p">))</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>            <span class="k">if</span> <span class="n">op_index_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>            
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>    <span class="k">def</span> <span class="nf">fix_labels</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]):</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        <span class="n">labels</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">op_by_label</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>        <span class="n">labels</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>        <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>            <span class="n">data</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>        
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>        <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">labels</span><span class="p">:</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>            <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>            <span class="n">label_data</span> <span class="o">=</span> <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>                <span class="k">for</span> <span class="n">op_index</span> <span class="ow">in</span> <span class="n">label_data</span><span class="p">:</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>                    <span class="n">op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>                    <span class="n">op</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index_new</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>                    <span class="n">new_arg</span> <span class="o">=</span> <span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">labeled_op_index_new</span><span class="p">)</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>                    <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>                        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">new_arg</span> <span class="o">-</span> <span class="p">(</span><span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">)</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>                    
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">set_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">)</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>                
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>                <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>                <span class="k">if</span> <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">==</span> <span class="n">labeled_op_index_new</span><span class="p">:</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>                    <span class="k">break</span>
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>                    <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="n">labeled_op_index_new_after_value_change</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>    <span class="k">def</span> <span class="nf">to_sequence_of_ints</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>        <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>            <span class="k">yield</span> <span class="n">op</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>                <span class="k">yield</span> <span class="mi">0</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>                <span class="k">yield</span> <span class="n">arg</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a>    <span class="k">def</span> <span class="nf">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos">713</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">to_sequence_of_ints</span><span class="p">())</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos">714</span></a>        
</span><span id="L-715"><a href="#L-715"><span class="linenos">715</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-716"><a href="#L-716"><span class="linenos">716</span></a>    <span class="k">def</span> <span class="nf">from_bytecode_sequence</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">):</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos">717</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos">718</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">))),</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="L-719"><a href="#L-719"><span class="linenos">719</span></a>    
</span><span id="L-720"><a href="#L-720"><span class="linenos">720</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos">721</span></a>    <span class="k">def</span> <span class="nf">from_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos">722</span></a>        <span class="n">code_bytes</span><span class="p">:</span> <span class="n">BytecodeSequence</span> <span class="o">=</span> <span class="n">_get_code_object</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="o">.</span><span class="n">co_code</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos">723</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_bytecode_sequence</span><span class="p">(</span><span class="n">code_bytes</span><span class="p">)</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos">724</span></a>    
</span><span id="L-725"><a href="#L-725"><span class="linenos">725</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos">726</span></a>    <span class="k">def</span> <span class="nf">from_instructions</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos">727</span></a>        <span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-728"><a href="#L-728"><span class="linenos">728</span></a>        <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos">729</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="L-730"><a href="#L-730"><span class="linenos">730</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos">731</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos">732</span></a>
</span><span id="L-733"><a href="#L-733"><span class="linenos">733</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">))</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos">734</span></a>
</span><span id="L-735"><a href="#L-735"><span class="linenos">735</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos">736</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)))</span>
</span><span id="L-737"><a href="#L-737"><span class="linenos">737</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos">738</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos">739</span></a>    
</span><span id="L-740"><a href="#L-740"><span class="linenos">740</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos">741</span></a>    <span class="k">def</span> <span class="nf">from_instructions_fast</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="L-742"><a href="#L-742"><span class="linenos">742</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">normalize_instructions_arg</span><span class="p">(</span><span class="n">instructions</span><span class="p">)))))</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos">743</span></a>
</span><span id="L-744"><a href="#L-744"><span class="linenos">744</span></a>
</span><span id="L-745"><a href="#L-745"><span class="linenos">745</span></a><span class="k">def</span> <span class="nf">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-746"><a href="#L-746"><span class="linenos">746</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-747"><a href="#L-747"><span class="linenos">747</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-748"><a href="#L-748"><span class="linenos">748</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos">749</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\x00</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos">750</span></a>            
</span><span id="L-751"><a href="#L-751"><span class="linenos">751</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">arg</span><span class="p">:</span>
</span><span id="L-752"><a href="#L-752"><span class="linenos">752</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\x00</span><span class="s1">&#39;</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos">753</span></a>    
</span><span id="L-754"><a href="#L-754"><span class="linenos">754</span></a>    <span class="k">return</span> <span class="n">arg</span>
</span><span id="L-755"><a href="#L-755"><span class="linenos">755</span></a>
</span><span id="L-756"><a href="#L-756"><span class="linenos">756</span></a>
</span><span id="L-757"><a href="#L-757"><span class="linenos">757</span></a><span class="k">def</span> <span class="nf">arg_to_int</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-758"><a href="#L-758"><span class="linenos">758</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="L-759"><a href="#L-759"><span class="linenos">759</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos">760</span></a>    
</span><span id="L-761"><a href="#L-761"><span class="linenos">761</span></a>    <span class="k">return</span> <span class="n">arg</span>
</span><span id="L-762"><a href="#L-762"><span class="linenos">762</span></a>
</span><span id="L-763"><a href="#L-763"><span class="linenos">763</span></a>
</span><span id="L-764"><a href="#L-764"><span class="linenos">764</span></a><span class="k">def</span> <span class="nf">get_raw_instructions</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">first_line</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-765"><a href="#L-765"><span class="linenos">765</span></a>    <span class="n">readable_instructions</span> <span class="o">=</span> <span class="n">get_instructions</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">first_line</span><span class="p">)</span>
</span><span id="L-766"><a href="#L-766"><span class="linenos">766</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">readable_instructions</span><span class="p">:</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos">767</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos">768</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-769"><a href="#L-769"><span class="linenos">769</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos">770</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-771"><a href="#L-771"><span class="linenos">771</span></a>            
</span><span id="L-772"><a href="#L-772"><span class="linenos">772</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos">773</span></a>
</span><span id="L-774"><a href="#L-774"><span class="linenos">774</span></a>        <span class="k">yield</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">instruction</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argval</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argrepr</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">offset</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">starts_line</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">is_jump_target</span><span class="p">)</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos">775</span></a>
</span><span id="L-776"><a href="#L-776"><span class="linenos">776</span></a>
</span><span id="L-777"><a href="#L-777"><span class="linenos">777</span></a><span class="k">def</span> <span class="nf">normalize_instructions_arg</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos">778</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="L-779"><a href="#L-779"><span class="linenos">779</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos">780</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-781"><a href="#L-781"><span class="linenos">781</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="L-782"><a href="#L-782"><span class="linenos">782</span></a>            <span class="n">extended_arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos">783</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-784"><a href="#L-784"><span class="linenos">784</span></a>            <span class="k">for</span> <span class="n">extended_arg_int</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">):</span>
</span><span id="L-785"><a href="#L-785"><span class="linenos">785</span></a>                <span class="k">yield</span> <span class="n">make_instruction</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">,</span> <span class="n">extended_arg_int</span><span class="p">)</span>
</span><span id="L-786"><a href="#L-786"><span class="linenos">786</span></a>
</span><span id="L-787"><a href="#L-787"><span class="linenos">787</span></a>        <span class="k">yield</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">instruction</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argval</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argrepr</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">offset</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">starts_line</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">is_jump_target</span><span class="p">)</span>
</span><span id="L-788"><a href="#L-788"><span class="linenos">788</span></a>
</span><span id="L-789"><a href="#L-789"><span class="linenos">789</span></a>
</span><span id="L-790"><a href="#L-790"><span class="linenos">790</span></a><span class="k">def</span> <span class="nf">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos">791</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos">792</span></a>        <span class="n">op</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos">793</span></a>        <span class="k">yield</span> <span class="n">op</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos">794</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="L-795"><a href="#L-795"><span class="linenos">795</span></a>        <span class="k">yield</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">arg</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos">796</span></a>
</span><span id="L-797"><a href="#L-797"><span class="linenos">797</span></a>
</span><span id="L-798"><a href="#L-798"><span class="linenos">798</span></a><span class="k">def</span> <span class="nf">instructions_to_bytes</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="L-799"><a href="#L-799"><span class="linenos">799</span></a>    <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">instructions</span><span class="p">))</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos">800</span></a>
</span><span id="L-801"><a href="#L-801"><span class="linenos">801</span></a>
</span><span id="L-802"><a href="#L-802"><span class="linenos">802</span></a><span class="k">def</span> <span class="nf">make_instruction</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Instruction</span><span class="p">:</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos">803</span></a>    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</span><span id="L-804"><a href="#L-804"><span class="linenos">804</span></a>    <span class="n">op</span> <span class="o">=</span> <span class="n">opmap</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-805"><a href="#L-805"><span class="linenos">805</span></a>    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos">806</span></a>    <span class="k">return</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos">807</span></a>
</span><span id="L-808"><a href="#L-808"><span class="linenos">808</span></a>
</span><span id="L-809"><a href="#L-809"><span class="linenos">809</span></a><span class="n">mi</span> <span class="o">=</span> <span class="n">make_instruction</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos">810</span></a>
</span><span id="L-811"><a href="#L-811"><span class="linenos">811</span></a>
</span><span id="L-812"><a href="#L-812"><span class="linenos">812</span></a><span class="k">def</span> <span class="nf">fix_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]):</span>
</span><span id="L-813"><a href="#L-813"><span class="linenos">813</span></a>    <span class="n">op_sequence</span><span class="o">.</span><span class="n">fix_labels</span><span class="p">({</span><span class="n">arg_to_op_index</span><span class="p">(</span><span class="n">label</span><span class="p">):</span> <span class="p">[</span><span class="n">op_info</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="k">for</span> <span class="n">op_info</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span> <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="o">.</span><span class="n">items</span><span class="p">()})</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos">814</span></a>
</span><span id="L-815"><a href="#L-815"><span class="linenos">815</span></a>
</span><span id="L-816"><a href="#L-816"><span class="linenos">816</span></a><span class="k">def</span> <span class="nf">code_info</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos">817</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Formatted details of methods, functions, or code.&quot;&quot;&quot;</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos">818</span></a>    <span class="k">return</span> <span class="n">_format_code_info</span><span class="p">(</span><span class="n">_get_code_object</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos">819</span></a>
</span><span id="L-820"><a href="#L-820"><span class="linenos">820</span></a>
</span><span id="L-821"><a href="#L-821"><span class="linenos">821</span></a><span class="k">def</span> <span class="nf">_pr</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos">822</span></a>    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;&lt;&lt;</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">&gt;&gt; type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-823"><a href="#L-823"><span class="linenos">823</span></a>
</span><span id="L-824"><a href="#L-824"><span class="linenos">824</span></a>
</span><span id="L-825"><a href="#L-825"><span class="linenos">825</span></a><span class="k">def</span> <span class="nf">_format_code_info</span><span class="p">(</span><span class="n">co</span><span class="p">):</span>
</span><span id="L-826"><a href="#L-826"><span class="linenos">826</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Name&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_name</span><span class="p">)</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos">827</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Filename&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_filename</span><span class="p">)</span>
</span><span id="L-828"><a href="#L-828"><span class="linenos">828</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Argument count&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">)</span>
</span><span id="L-829"><a href="#L-829"><span class="linenos">829</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Positional-only arguments&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_posonlyargcount</span><span class="p">)</span>
</span><span id="L-830"><a href="#L-830"><span class="linenos">830</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Kw-only arguments&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">)</span>
</span><span id="L-831"><a href="#L-831"><span class="linenos">831</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Number of locals&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_nlocals</span><span class="p">)</span>
</span><span id="L-832"><a href="#L-832"><span class="linenos">832</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Stack size&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">)</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos">833</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Flags&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_flags</span><span class="p">)</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos">834</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Constants&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_consts</span><span class="p">)</span>
</span><span id="L-835"><a href="#L-835"><span class="linenos">835</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Names&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_names</span><span class="p">)</span>
</span><span id="L-836"><a href="#L-836"><span class="linenos">836</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Variable names&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="L-837"><a href="#L-837"><span class="linenos">837</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Free variables&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">)</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos">838</span></a>    <span class="n">_pr</span><span class="p">(</span><span class="s1">&#39;Cell variables&#39;</span><span class="p">,</span> <span class="n">co</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">)</span>
</span></pre></div>


            </section>
                <section id="BytecodeSequence">
                    <div class="attr variable">
            <span class="name">BytecodeSequence</span>        =
<span class="default_value">typing.Union[bytes, typing.Sequence[typing.Union[int, bytes]]]</span>

        
    </div>
    <a class="headerlink" href="#BytecodeSequence"></a>
    
    

                </section>
                <section id="patch_function">
                            <input id="patch_function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">patch_function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span>, </span><span class="param"><span class="n">co_code</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="patch_function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#patch_function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="patch_function-53"><a href="#patch_function-53"><span class="linenos">53</span></a><span class="k">def</span> <span class="nf">patch_function</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">co_code</span><span class="p">):</span>
</span><span id="patch_function-54"><a href="#patch_function-54"><span class="linenos">54</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span>
</span><span id="patch_function-55"><a href="#patch_function-55"><span class="linenos">55</span></a>    <span class="n">func</span><span class="o">.</span><span class="vm">__code__</span> <span class="o">=</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="patch_function-56"><a href="#patch_function-56"><span class="linenos">56</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="patch_function-57"><a href="#patch_function-57"><span class="linenos">57</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="patch_function-58"><a href="#patch_function-58"><span class="linenos">58</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="patch_function-59"><a href="#patch_function-59"><span class="linenos">59</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="patch_function-60"><a href="#patch_function-60"><span class="linenos">60</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="patch_function-61"><a href="#patch_function-61"><span class="linenos">61</span></a>        <span class="n">co_code</span><span class="p">,</span>
</span><span id="patch_function-62"><a href="#patch_function-62"><span class="linenos">62</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_consts</span><span class="p">,</span>
</span><span id="patch_function-63"><a href="#patch_function-63"><span class="linenos">63</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_names</span><span class="p">,</span>
</span><span id="patch_function-64"><a href="#patch_function-64"><span class="linenos">64</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">,</span>
</span><span id="patch_function-65"><a href="#patch_function-65"><span class="linenos">65</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="patch_function-66"><a href="#patch_function-66"><span class="linenos">66</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="patch_function-67"><a href="#patch_function-67"><span class="linenos">67</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="patch_function-68"><a href="#patch_function-68"><span class="linenos">68</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="patch_function-69"><a href="#patch_function-69"><span class="linenos">69</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="patch_function-70"><a href="#patch_function-70"><span class="linenos">70</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="patch_function-71"><a href="#patch_function-71"><span class="linenos">71</span></a>    <span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="CodeParamNames">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CodeParamNames</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#CodeParamNames"></a>
    
            <div class="docstring"><p>CodeParamNames(positional, positional_only, keyword_only)</p>
</div>


                            <div id="CodeParamNames.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">CodeParamNames</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">positional</span>, </span><span class="param"><span class="n">positional_only</span>, </span><span class="param"><span class="n">keyword_only</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#CodeParamNames.__init__"></a>
    
            <div class="docstring"><p>Create new instance of CodeParamNames(positional, positional_only, keyword_only)</p>
</div>


                            </div>
                            <div id="CodeParamNames.positional" class="classattr">
                                <div class="attr variable">
            <span class="name">positional</span>

        
    </div>
    <a class="headerlink" href="#CodeParamNames.positional"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="CodeParamNames.positional_only" class="classattr">
                                <div class="attr variable">
            <span class="name">positional_only</span>

        
    </div>
    <a class="headerlink" href="#CodeParamNames.positional_only"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div id="CodeParamNames.keyword_only" class="classattr">
                                <div class="attr variable">
            <span class="name">keyword_only</span>

        
    </div>
    <a class="headerlink" href="#CodeParamNames.keyword_only"></a>
    
            <div class="docstring"><p>Alias for field number 2</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="CodeParamNames.index" class="function">index</dd>
                <dd id="CodeParamNames.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="code_param_names">
                            <input id="code_param_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_param_names</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code</span></span><span class="return-annotation">) -> <span class="n"><a href="#CodeParamNames">CodeParamNames</a></span>:</span></span>

                <label class="view-source-button" for="code_param_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_param_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_param_names-77"><a href="#code_param_names-77"><span class="linenos">77</span></a><span class="k">def</span> <span class="nf">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="code_param_names-78"><a href="#code_param_names-78"><span class="linenos">78</span></a>    <span class="n">pos_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_argcount</span>
</span><span id="code_param_names-79"><a href="#code_param_names-79"><span class="linenos">79</span></a>    <span class="n">arg_names</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_varnames</span>
</span><span id="code_param_names-80"><a href="#code_param_names-80"><span class="linenos">80</span></a>    <span class="n">positional</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[:</span><span class="n">pos_count</span><span class="p">]</span>
</span><span id="code_param_names-81"><a href="#code_param_names-81"><span class="linenos">81</span></a>    <span class="n">posonly_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_posonlyargcount</span>
</span><span id="code_param_names-82"><a href="#code_param_names-82"><span class="linenos">82</span></a>    <span class="n">positional_only</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[:</span><span class="n">posonly_count</span><span class="p">]</span>
</span><span id="code_param_names-83"><a href="#code_param_names-83"><span class="linenos">83</span></a>    <span class="n">keyword_only_count</span> <span class="o">=</span> <span class="n">code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span>
</span><span id="code_param_names-84"><a href="#code_param_names-84"><span class="linenos">84</span></a>    <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">arg_names</span><span class="p">[</span><span class="n">pos_count</span><span class="p">:</span><span class="n">pos_count</span> <span class="o">+</span> <span class="n">keyword_only_count</span><span class="p">]</span>
</span><span id="code_param_names-85"><a href="#code_param_names-85"><span class="linenos">85</span></a>    <span class="k">return</span> <span class="n">CodeParamNames</span><span class="p">(</span><span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="code_name">
                            <input id="code_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">code</span><span class="p">:</span> <span class="n">code</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="code_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_name-88"><a href="#code_name-88"><span class="linenos">88</span></a><span class="k">def</span> <span class="nf">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="code_name-89"><a href="#code_name-89"><span class="linenos">89</span></a>    <span class="k">return</span> <span class="n">code</span><span class="o">.</span><span class="n">co_name</span>
</span></pre></div>


    

                </section>
                <section id="get_code">
                            <input id="get_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">x</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">code</span>:</span></span>

                <label class="view-source-button" for="get_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_code-97"><a href="#get_code-97"><span class="linenos"> 97</span></a><span class="k">def</span> <span class="nf">get_code</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeType</span><span class="p">:</span>
</span><span id="get_code-98"><a href="#get_code-98"><span class="linenos"> 98</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_code-99"><a href="#get_code-99"><span class="linenos"> 99</span></a>        <span class="k">return</span>
</span><span id="get_code-100"><a href="#get_code-100"><span class="linenos">100</span></a>    
</span><span id="get_code-101"><a href="#get_code-101"><span class="linenos">101</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="get_code-102"><a href="#get_code-102"><span class="linenos">102</span></a>        <span class="k">return</span> <span class="n">x</span>
</span><span id="get_code-103"><a href="#get_code-103"><span class="linenos">103</span></a>    
</span><span id="get_code-104"><a href="#get_code-104"><span class="linenos">104</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="get_code-105"><a href="#get_code-105"><span class="linenos">105</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="get_code-106"><a href="#get_code-106"><span class="linenos">106</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="get_code-107"><a href="#get_code-107"><span class="linenos">107</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="get_code-108"><a href="#get_code-108"><span class="linenos">108</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="get_code-109"><a href="#get_code-109"><span class="linenos">109</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="vm">__code__</span>
</span><span id="get_code-110"><a href="#get_code-110"><span class="linenos">110</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="get_code-111"><a href="#get_code-111"><span class="linenos">111</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">gi_code</span>
</span><span id="get_code-112"><a href="#get_code-112"><span class="linenos">112</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="get_code-113"><a href="#get_code-113"><span class="linenos">113</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">ag_code</span>
</span><span id="get_code-114"><a href="#get_code-114"><span class="linenos">114</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine, or</span>
</span><span id="get_code-115"><a href="#get_code-115"><span class="linenos">115</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">cr_code</span>
</span><span id="get_code-116"><a href="#get_code-116"><span class="linenos">116</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;f_code&#39;</span><span class="p">):</span>  <span class="c1">#...a frame.</span>
</span><span id="get_code-117"><a href="#get_code-117"><span class="linenos">117</span></a>        <span class="n">x</span> <span class="o">=</span> <span class="n">x</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="get_code-118"><a href="#get_code-118"><span class="linenos">118</span></a>    <span class="c1"># else:</span>
</span><span id="get_code-119"><a href="#get_code-119"><span class="linenos">119</span></a>    <span class="c1">#     raise TypeError(f&#39;Expected a code object or an entity with code, but got {type(x)}&#39;)</span>
</span><span id="get_code-120"><a href="#get_code-120"><span class="linenos">120</span></a>    
</span><span id="get_code-121"><a href="#get_code-121"><span class="linenos">121</span></a>    <span class="k">return</span> <span class="n">x</span>
</span></pre></div>


    

                </section>
                <section id="has_code">
                            <input id="has_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">has_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">x</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="has_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#has_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="has_code-124"><a href="#has_code-124"><span class="linenos">124</span></a><span class="k">def</span> <span class="nf">has_code</span><span class="p">(</span><span class="n">x</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="has_code-125"><a href="#has_code-125"><span class="linenos">125</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="has_code-126"><a href="#has_code-126"><span class="linenos">126</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="has_code-127"><a href="#has_code-127"><span class="linenos">127</span></a>    
</span><span id="has_code-128"><a href="#has_code-128"><span class="linenos">128</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="has_code-129"><a href="#has_code-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-130"><a href="#has_code-130"><span class="linenos">130</span></a>    
</span><span id="has_code-131"><a href="#has_code-131"><span class="linenos">131</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="has_code-132"><a href="#has_code-132"><span class="linenos">132</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="has_code-133"><a href="#has_code-133"><span class="linenos">133</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-134"><a href="#has_code-134"><span class="linenos">134</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="has_code-135"><a href="#has_code-135"><span class="linenos">135</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="has_code-136"><a href="#has_code-136"><span class="linenos">136</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-137"><a href="#has_code-137"><span class="linenos">137</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="has_code-138"><a href="#has_code-138"><span class="linenos">138</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-139"><a href="#has_code-139"><span class="linenos">139</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="has_code-140"><a href="#has_code-140"><span class="linenos">140</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-141"><a href="#has_code-141"><span class="linenos">141</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine, or</span>
</span><span id="has_code-142"><a href="#has_code-142"><span class="linenos">142</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-143"><a href="#has_code-143"><span class="linenos">143</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;f_code&#39;</span><span class="p">):</span>  <span class="c1">#...a frame.</span>
</span><span id="has_code-144"><a href="#has_code-144"><span class="linenos">144</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="has_code-145"><a href="#has_code-145"><span class="linenos">145</span></a>    <span class="c1"># else:</span>
</span><span id="has_code-146"><a href="#has_code-146"><span class="linenos">146</span></a>    <span class="c1">#     raise TypeError(f&#39;Expected a code object or an entity with code, but got {type(x)}&#39;)</span>
</span><span id="has_code-147"><a href="#has_code-147"><span class="linenos">147</span></a>    
</span><span id="has_code-148"><a href="#has_code-148"><span class="linenos">148</span></a>    <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="CodeTypeEnum">
                            <input id="CodeTypeEnum-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CodeTypeEnum</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="CodeTypeEnum-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CodeTypeEnum"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CodeTypeEnum-151"><a href="#CodeTypeEnum-151"><span class="linenos">151</span></a><span class="k">class</span> <span class="nc">CodeTypeEnum</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="CodeTypeEnum-152"><a href="#CodeTypeEnum-152"><span class="linenos">152</span></a>    <span class="n">class_or_module</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="CodeTypeEnum-153"><a href="#CodeTypeEnum-153"><span class="linenos">153</span></a>    <span class="n">code_object</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="CodeTypeEnum-154"><a href="#CodeTypeEnum-154"><span class="linenos">154</span></a>    <span class="n">raw_bytecode</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="CodeTypeEnum-155"><a href="#CodeTypeEnum-155"><span class="linenos">155</span></a>    <span class="n">source_code</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="CodeTypeEnum-156"><a href="#CodeTypeEnum-156"><span class="linenos">156</span></a>    <span class="n">unknown</span> <span class="o">=</span> <span class="mi">4</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="CodeTypeEnum.class_or_module" class="classattr">
                                <div class="attr variable">
            <span class="name">class_or_module</span>        =
<span class="default_value">&lt;<a href="#CodeTypeEnum.class_or_module">CodeTypeEnum.class_or_module</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeTypeEnum.class_or_module"></a>
    
    

                            </div>
                            <div id="CodeTypeEnum.code_object" class="classattr">
                                <div class="attr variable">
            <span class="name">code_object</span>        =
<span class="default_value">&lt;<a href="#CodeTypeEnum.code_object">CodeTypeEnum.code_object</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeTypeEnum.code_object"></a>
    
    

                            </div>
                            <div id="CodeTypeEnum.raw_bytecode" class="classattr">
                                <div class="attr variable">
            <span class="name">raw_bytecode</span>        =
<span class="default_value">&lt;<a href="#CodeTypeEnum.raw_bytecode">CodeTypeEnum.raw_bytecode</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeTypeEnum.raw_bytecode"></a>
    
    

                            </div>
                            <div id="CodeTypeEnum.source_code" class="classattr">
                                <div class="attr variable">
            <span class="name">source_code</span>        =
<span class="default_value">&lt;<a href="#CodeTypeEnum.source_code">CodeTypeEnum.source_code</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeTypeEnum.source_code"></a>
    
    

                            </div>
                            <div id="CodeTypeEnum.unknown" class="classattr">
                                <div class="attr variable">
            <span class="name">unknown</span>        =
<span class="default_value">&lt;<a href="#CodeTypeEnum.unknown">CodeTypeEnum.unknown</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeTypeEnum.unknown"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="CodeTypeEnum.name" class="variable">name</dd>
                <dd id="CodeTypeEnum.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="code_type">
                            <input id="code_type-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_type</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">x</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#CodeTypeEnum">CodeTypeEnum</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="code_type-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_type"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_type-159"><a href="#code_type-159"><span class="linenos">159</span></a><span class="k">def</span> <span class="nf">code_type</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeTypeEnum</span><span class="p">]:</span>
</span><span id="code_type-160"><a href="#code_type-160"><span class="linenos">160</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="code_type-161"><a href="#code_type-161"><span class="linenos">161</span></a>
</span><span id="code_type-162"><a href="#code_type-162"><span class="linenos">162</span></a><span class="sd">    Args:</span>
</span><span id="code_type-163"><a href="#code_type-163"><span class="linenos">163</span></a><span class="sd">        x (_type_, optional): result of get_code() function. Defaults to None.</span>
</span><span id="code_type-164"><a href="#code_type-164"><span class="linenos">164</span></a>
</span><span id="code_type-165"><a href="#code_type-165"><span class="linenos">165</span></a><span class="sd">    Returns:</span>
</span><span id="code_type-166"><a href="#code_type-166"><span class="linenos">166</span></a><span class="sd">        Optional[CodeTypeEnum]: _description_</span>
</span><span id="code_type-167"><a href="#code_type-167"><span class="linenos">167</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="code_type-168"><a href="#code_type-168"><span class="linenos">168</span></a>    <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="code_type-169"><a href="#code_type-169"><span class="linenos">169</span></a>        <span class="k">return</span>
</span><span id="code_type-170"><a href="#code_type-170"><span class="linenos">170</span></a>    
</span><span id="code_type-171"><a href="#code_type-171"><span class="linenos">171</span></a>    <span class="c1"># Perform the disassembly.</span>
</span><span id="code_type-172"><a href="#code_type-172"><span class="linenos">172</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__dict__&#39;</span><span class="p">):</span>  <span class="c1"># Class or module</span>
</span><span id="code_type-173"><a href="#code_type-173"><span class="linenos">173</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">class_or_module</span>
</span><span id="code_type-174"><a href="#code_type-174"><span class="linenos">174</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;co_code&#39;</span><span class="p">):</span> <span class="c1"># Code object</span>
</span><span id="code_type-175"><a href="#code_type-175"><span class="linenos">175</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">code_object</span>
</span><span id="code_type-176"><a href="#code_type-176"><span class="linenos">176</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="p">(</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">bytearray</span><span class="p">)):</span> <span class="c1"># Raw bytecode</span>
</span><span id="code_type-177"><a href="#code_type-177"><span class="linenos">177</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">raw_bytecode</span>
</span><span id="code_type-178"><a href="#code_type-178"><span class="linenos">178</span></a>    <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span>    <span class="c1"># Source code</span>
</span><span id="code_type-179"><a href="#code_type-179"><span class="linenos">179</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">source_code</span>
</span><span id="code_type-180"><a href="#code_type-180"><span class="linenos">180</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="code_type-181"><a href="#code_type-181"><span class="linenos">181</span></a>        <span class="k">return</span> <span class="n">CodeTypeEnum</span><span class="o">.</span><span class="n">unknown</span>
</span></pre></div>


            <div class="docstring"><p>_summary_</p>

<p>Args:
    x (_type_, optional): result of get_code() function. Defaults to None.</p>

<p>Returns:
    Optional[CodeTypeEnum]: _description_</p>
</div>


                </section>
                <section id="set_code">
                            <input id="set_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">x</span>, </span><span class="param"><span class="n">code</span><span class="p">:</span> <span class="n">code</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="set_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#set_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="set_code-184"><a href="#set_code-184"><span class="linenos">184</span></a><span class="k">def</span> <span class="nf">set_code</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="set_code-185"><a href="#set_code-185"><span class="linenos">185</span></a>    <span class="c1"># Extract functions from methods.</span>
</span><span id="set_code-186"><a href="#set_code-186"><span class="linenos">186</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__func__&#39;</span><span class="p">):</span>
</span><span id="set_code-187"><a href="#set_code-187"><span class="linenos">187</span></a>        <span class="n">x</span><span class="o">.</span><span class="vm">__func__</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="set_code-188"><a href="#set_code-188"><span class="linenos">188</span></a>    <span class="c1"># Extract compiled code objects from...</span>
</span><span id="set_code-189"><a href="#set_code-189"><span class="linenos">189</span></a>    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;__code__&#39;</span><span class="p">):</span>  <span class="c1"># ...a function, or</span>
</span><span id="set_code-190"><a href="#set_code-190"><span class="linenos">190</span></a>        <span class="n">x</span><span class="o">.</span><span class="vm">__code__</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="set_code-191"><a href="#set_code-191"><span class="linenos">191</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;gi_code&#39;</span><span class="p">):</span>  <span class="c1">#...a generator object, or</span>
</span><span id="set_code-192"><a href="#set_code-192"><span class="linenos">192</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">gi_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="set_code-193"><a href="#set_code-193"><span class="linenos">193</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;ag_code&#39;</span><span class="p">):</span>  <span class="c1">#...an asynchronous generator object, or</span>
</span><span id="set_code-194"><a href="#set_code-194"><span class="linenos">194</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">ag_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="set_code-195"><a href="#set_code-195"><span class="linenos">195</span></a>    <span class="k">elif</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="s1">&#39;cr_code&#39;</span><span class="p">):</span>  <span class="c1">#...a coroutine.</span>
</span><span id="set_code-196"><a href="#set_code-196"><span class="linenos">196</span></a>        <span class="n">x</span><span class="o">.</span><span class="n">cr_code</span> <span class="o">=</span> <span class="n">code</span>
</span><span id="set_code-197"><a href="#set_code-197"><span class="linenos">197</span></a>    
</span><span id="set_code-198"><a href="#set_code-198"><span class="linenos">198</span></a>    <span class="k">return</span> <span class="n">x</span>
</span></pre></div>


    

                </section>
                <section id="OpSequenceOffsetMap">
                            <input id="OpSequenceOffsetMap-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">OpSequenceOffsetMap</span><wbr>(<span class="base">cengal.entities.copyable.versions.v_0.copyable.CopyableMixin</span>):

                <label class="view-source-button" for="OpSequenceOffsetMap-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap-360"><a href="#OpSequenceOffsetMap-360"><span class="linenos">360</span></a><span class="k">class</span> <span class="nc">OpSequenceOffsetMap</span><span class="p">(</span><span class="n">CopyableMixin</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-361"><a href="#OpSequenceOffsetMap-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-362"><a href="#OpSequenceOffsetMap-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-363"><a href="#OpSequenceOffsetMap-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">op_num</span><span class="p">)</span> <span class="k">if</span> <span class="n">op_num</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="OpSequenceOffsetMap-364"><a href="#OpSequenceOffsetMap-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-365"><a href="#OpSequenceOffsetMap-365"><span class="linenos">365</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-366"><a href="#OpSequenceOffsetMap-366"><span class="linenos">366</span></a>        <span class="k">if</span> <span class="n">op_num</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-367"><a href="#OpSequenceOffsetMap-367"><span class="linenos">367</span></a>            <span class="n">op_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequenceOffsetMap-368"><a href="#OpSequenceOffsetMap-368"><span class="linenos">368</span></a>        
</span><span id="OpSequenceOffsetMap-369"><a href="#OpSequenceOffsetMap-369"><span class="linenos">369</span></a>        <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">op_num</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-370"><a href="#OpSequenceOffsetMap-370"><span class="linenos">370</span></a>            <span class="c1"># bindex = index * 2</span>
</span><span id="OpSequenceOffsetMap-371"><a href="#OpSequenceOffsetMap-371"><span class="linenos">371</span></a>            <span class="n">bindex</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="OpSequenceOffsetMap-372"><a href="#OpSequenceOffsetMap-372"><span class="linenos">372</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span><span id="OpSequenceOffsetMap-373"><a href="#OpSequenceOffsetMap-373"><span class="linenos">373</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span><span id="OpSequenceOffsetMap-374"><a href="#OpSequenceOffsetMap-374"><span class="linenos">374</span></a>    
</span><span id="OpSequenceOffsetMap-375"><a href="#OpSequenceOffsetMap-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">mapped_range</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">slice</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-376"><a href="#OpSequenceOffsetMap-376"><span class="linenos">376</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">))</span>
</span><span id="OpSequenceOffsetMap-377"><a href="#OpSequenceOffsetMap-377"><span class="linenos">377</span></a>
</span><span id="OpSequenceOffsetMap-378"><a href="#OpSequenceOffsetMap-378"><span class="linenos">378</span></a>    
</span><span id="OpSequenceOffsetMap-379"><a href="#OpSequenceOffsetMap-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-380"><a href="#OpSequenceOffsetMap-380"><span class="linenos">380</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-381"><a href="#OpSequenceOffsetMap-381"><span class="linenos">381</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap-382"><a href="#OpSequenceOffsetMap-382"><span class="linenos">382</span></a>        
</span><span id="OpSequenceOffsetMap-383"><a href="#OpSequenceOffsetMap-383"><span class="linenos">383</span></a>        <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequenceOffsetMap-384"><a href="#OpSequenceOffsetMap-384"><span class="linenos">384</span></a>        <span class="n">del_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequenceOffsetMap-385"><a href="#OpSequenceOffsetMap-385"><span class="linenos">385</span></a>        <span class="n">del_stop</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-386"><a href="#OpSequenceOffsetMap-386"><span class="linenos">386</span></a>
</span><span id="OpSequenceOffsetMap-387"><a href="#OpSequenceOffsetMap-387"><span class="linenos">387</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap-388"><a href="#OpSequenceOffsetMap-388"><span class="linenos">388</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-389"><a href="#OpSequenceOffsetMap-389"><span class="linenos">389</span></a>        <span class="n">to_be_deleted</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-390"><a href="#OpSequenceOffsetMap-390"><span class="linenos">390</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-391"><a href="#OpSequenceOffsetMap-391"><span class="linenos">391</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-392"><a href="#OpSequenceOffsetMap-392"><span class="linenos">392</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">original</span><span class="p">,</span> <span class="n">new</span><span class="p">))</span>
</span><span id="OpSequenceOffsetMap-393"><a href="#OpSequenceOffsetMap-393"><span class="linenos">393</span></a>        
</span><span id="OpSequenceOffsetMap-394"><a href="#OpSequenceOffsetMap-394"><span class="linenos">394</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="OpSequenceOffsetMap-395"><a href="#OpSequenceOffsetMap-395"><span class="linenos">395</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-396"><a href="#OpSequenceOffsetMap-396"><span class="linenos">396</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="OpSequenceOffsetMap-397"><a href="#OpSequenceOffsetMap-397"><span class="linenos">397</span></a>        
</span><span id="OpSequenceOffsetMap-398"><a href="#OpSequenceOffsetMap-398"><span class="linenos">398</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-399"><a href="#OpSequenceOffsetMap-399"><span class="linenos">399</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap-400"><a href="#OpSequenceOffsetMap-400"><span class="linenos">400</span></a>        
</span><span id="OpSequenceOffsetMap-401"><a href="#OpSequenceOffsetMap-401"><span class="linenos">401</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap-402"><a href="#OpSequenceOffsetMap-402"><span class="linenos">402</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-403"><a href="#OpSequenceOffsetMap-403"><span class="linenos">403</span></a>        <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-404"><a href="#OpSequenceOffsetMap-404"><span class="linenos">404</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-405"><a href="#OpSequenceOffsetMap-405"><span class="linenos">405</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-406"><a href="#OpSequenceOffsetMap-406"><span class="linenos">406</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">new</span><span class="p">,</span> <span class="n">original</span><span class="p">))</span>
</span><span id="OpSequenceOffsetMap-407"><a href="#OpSequenceOffsetMap-407"><span class="linenos">407</span></a>        
</span><span id="OpSequenceOffsetMap-408"><a href="#OpSequenceOffsetMap-408"><span class="linenos">408</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="OpSequenceOffsetMap-409"><a href="#OpSequenceOffsetMap-409"><span class="linenos">409</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-410"><a href="#OpSequenceOffsetMap-410"><span class="linenos">410</span></a>            <span class="n">ignored</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[:</span><span class="n">preserver_index_for_first_x_op</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap-411"><a href="#OpSequenceOffsetMap-411"><span class="linenos">411</span></a>            <span class="k">if</span> <span class="n">ignored</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-412"><a href="#OpSequenceOffsetMap-412"><span class="linenos">412</span></a>                <span class="n">last_ignored</span> <span class="o">=</span> <span class="n">ignored</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap-413"><a href="#OpSequenceOffsetMap-413"><span class="linenos">413</span></a>                <span class="n">last_ignored_new</span> <span class="o">=</span> <span class="n">last_ignored</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap-414"><a href="#OpSequenceOffsetMap-414"><span class="linenos">414</span></a>                <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">last_ignored_new</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequenceOffsetMap-415"><a href="#OpSequenceOffsetMap-415"><span class="linenos">415</span></a>            
</span><span id="OpSequenceOffsetMap-416"><a href="#OpSequenceOffsetMap-416"><span class="linenos">416</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="OpSequenceOffsetMap-417"><a href="#OpSequenceOffsetMap-417"><span class="linenos">417</span></a>        
</span><span id="OpSequenceOffsetMap-418"><a href="#OpSequenceOffsetMap-418"><span class="linenos">418</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-419"><a href="#OpSequenceOffsetMap-419"><span class="linenos">419</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap-420"><a href="#OpSequenceOffsetMap-420"><span class="linenos">420</span></a>        
</span><span id="OpSequenceOffsetMap-421"><a href="#OpSequenceOffsetMap-421"><span class="linenos">421</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="o">-</span><span class="n">op_num</span><span class="p">,</span> <span class="n">offset_change_start</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-422"><a href="#OpSequenceOffsetMap-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">-=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-423"><a href="#OpSequenceOffsetMap-423"><span class="linenos">423</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_num</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-424"><a href="#OpSequenceOffsetMap-424"><span class="linenos">424</span></a>    
</span><span id="OpSequenceOffsetMap-425"><a href="#OpSequenceOffsetMap-425"><span class="linenos">425</span></a>    <span class="k">def</span> <span class="nf">insert_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-426"><a href="#OpSequenceOffsetMap-426"><span class="linenos">426</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-427"><a href="#OpSequenceOffsetMap-427"><span class="linenos">427</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap-428"><a href="#OpSequenceOffsetMap-428"><span class="linenos">428</span></a>        
</span><span id="OpSequenceOffsetMap-429"><a href="#OpSequenceOffsetMap-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_num</span><span class="p">,</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-430"><a href="#OpSequenceOffsetMap-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">+=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-431"><a href="#OpSequenceOffsetMap-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_num</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-432"><a href="#OpSequenceOffsetMap-432"><span class="linenos">432</span></a>    
</span><span id="OpSequenceOffsetMap-433"><a href="#OpSequenceOffsetMap-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">insertion_id</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-434"><a href="#OpSequenceOffsetMap-434"><span class="linenos">434</span></a>        <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-435"><a href="#OpSequenceOffsetMap-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-436"><a href="#OpSequenceOffsetMap-436"><span class="linenos">436</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap-437"><a href="#OpSequenceOffsetMap-437"><span class="linenos">437</span></a>        
</span><span id="OpSequenceOffsetMap-438"><a href="#OpSequenceOffsetMap-438"><span class="linenos">438</span></a>        <span class="n">sequence_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">range</span>
</span><span id="OpSequenceOffsetMap-439"><a href="#OpSequenceOffsetMap-439"><span class="linenos">439</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="n">sequence_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequenceOffsetMap-440"><a href="#OpSequenceOffsetMap-440"><span class="linenos">440</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">insert_slice</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="n">op_num</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-441"><a href="#OpSequenceOffsetMap-441"><span class="linenos">441</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-442"><a href="#OpSequenceOffsetMap-442"><span class="linenos">442</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span> <span class="o">+</span> <span class="n">offset</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">insertion_id</span><span class="p">,</span> <span class="n">new</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-443"><a href="#OpSequenceOffsetMap-443"><span class="linenos">443</span></a>    
</span><span id="OpSequenceOffsetMap-444"><a href="#OpSequenceOffsetMap-444"><span class="linenos">444</span></a>    <span class="k">def</span> <span class="nf">add_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_start</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-445"><a href="#OpSequenceOffsetMap-445"><span class="linenos">445</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-446"><a href="#OpSequenceOffsetMap-446"><span class="linenos">446</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap-447"><a href="#OpSequenceOffsetMap-447"><span class="linenos">447</span></a>        
</span><span id="OpSequenceOffsetMap-448"><a href="#OpSequenceOffsetMap-448"><span class="linenos">448</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap-449"><a href="#OpSequenceOffsetMap-449"><span class="linenos">449</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-450"><a href="#OpSequenceOffsetMap-450"><span class="linenos">450</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-451"><a href="#OpSequenceOffsetMap-451"><span class="linenos">451</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-452"><a href="#OpSequenceOffsetMap-452"><span class="linenos">452</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="OpSequenceOffsetMap-453"><a href="#OpSequenceOffsetMap-453"><span class="linenos">453</span></a>            
</span><span id="OpSequenceOffsetMap-454"><a href="#OpSequenceOffsetMap-454"><span class="linenos">454</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span>
</span><span id="OpSequenceOffsetMap-455"><a href="#OpSequenceOffsetMap-455"><span class="linenos">455</span></a>        
</span><span id="OpSequenceOffsetMap-456"><a href="#OpSequenceOffsetMap-456"><span class="linenos">456</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap-457"><a href="#OpSequenceOffsetMap-457"><span class="linenos">457</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-458"><a href="#OpSequenceOffsetMap-458"><span class="linenos">458</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-459"><a href="#OpSequenceOffsetMap-459"><span class="linenos">459</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-460"><a href="#OpSequenceOffsetMap-460"><span class="linenos">460</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="OpSequenceOffsetMap-461"><a href="#OpSequenceOffsetMap-461"><span class="linenos">461</span></a>            
</span><span id="OpSequenceOffsetMap-462"><a href="#OpSequenceOffsetMap-462"><span class="linenos">462</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span> <span class="o">=</span> <span class="n">original</span>
</span><span id="OpSequenceOffsetMap-463"><a href="#OpSequenceOffsetMap-463"><span class="linenos">463</span></a>    
</span><span id="OpSequenceOffsetMap-464"><a href="#OpSequenceOffsetMap-464"><span class="linenos">464</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-465"><a href="#OpSequenceOffsetMap-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-466"><a href="#OpSequenceOffsetMap-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-467"><a href="#OpSequenceOffsetMap-467"><span class="linenos">467</span></a>    
</span><span id="OpSequenceOffsetMap-468"><a href="#OpSequenceOffsetMap-468"><span class="linenos">468</span></a>    <span class="k">def</span> <span class="nf">shift_to_absolute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-469"><a href="#OpSequenceOffsetMap-469"><span class="linenos">469</span></a>        <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequenceOffsetMap-470"><a href="#OpSequenceOffsetMap-470"><span class="linenos">470</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-471"><a href="#OpSequenceOffsetMap-471"><span class="linenos">471</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-472"><a href="#OpSequenceOffsetMap-472"><span class="linenos">472</span></a>    
</span><span id="OpSequenceOffsetMap-473"><a href="#OpSequenceOffsetMap-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-474"><a href="#OpSequenceOffsetMap-474"><span class="linenos">474</span></a>        <span class="k">if</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-475"><a href="#OpSequenceOffsetMap-475"><span class="linenos">475</span></a>            <span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-476"><a href="#OpSequenceOffsetMap-476"><span class="linenos">476</span></a>            <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-477"><a href="#OpSequenceOffsetMap-477"><span class="linenos">477</span></a>        
</span><span id="OpSequenceOffsetMap-478"><a href="#OpSequenceOffsetMap-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-479"><a href="#OpSequenceOffsetMap-479"><span class="linenos">479</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-480"><a href="#OpSequenceOffsetMap-480"><span class="linenos">480</span></a>    
</span><span id="OpSequenceOffsetMap-481"><a href="#OpSequenceOffsetMap-481"><span class="linenos">481</span></a>    <span class="k">def</span> <span class="fm">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-482"><a href="#OpSequenceOffsetMap-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-483"><a href="#OpSequenceOffsetMap-483"><span class="linenos">483</span></a>            <span class="n">index</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-484"><a href="#OpSequenceOffsetMap-484"><span class="linenos">484</span></a>        
</span><span id="OpSequenceOffsetMap-485"><a href="#OpSequenceOffsetMap-485"><span class="linenos">485</span></a>        <span class="n">op_num</span> <span class="o">=</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequenceOffsetMap-486"><a href="#OpSequenceOffsetMap-486"><span class="linenos">486</span></a>
</span><span id="OpSequenceOffsetMap-487"><a href="#OpSequenceOffsetMap-487"><span class="linenos">487</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap-488"><a href="#OpSequenceOffsetMap-488"><span class="linenos">488</span></a>        <span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">new_by_original_buff</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-489"><a href="#OpSequenceOffsetMap-489"><span class="linenos">489</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-490"><a href="#OpSequenceOffsetMap-490"><span class="linenos">490</span></a>            <span class="k">if</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-491"><a href="#OpSequenceOffsetMap-491"><span class="linenos">491</span></a>                <span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span>
</span><span id="OpSequenceOffsetMap-492"><a href="#OpSequenceOffsetMap-492"><span class="linenos">492</span></a>        
</span><span id="OpSequenceOffsetMap-493"><a href="#OpSequenceOffsetMap-493"><span class="linenos">493</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap-494"><a href="#OpSequenceOffsetMap-494"><span class="linenos">494</span></a>        <span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">original_by_new_buff</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap-495"><a href="#OpSequenceOffsetMap-495"><span class="linenos">495</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap-496"><a href="#OpSequenceOffsetMap-496"><span class="linenos">496</span></a>            <span class="k">if</span> <span class="n">index</span><span class="o">.</span><span class="n">start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">index</span><span class="o">.</span><span class="n">stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap-497"><a href="#OpSequenceOffsetMap-497"><span class="linenos">497</span></a>                <span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span> <span class="o">=</span> <span class="n">original</span>
</span><span id="OpSequenceOffsetMap-498"><a href="#OpSequenceOffsetMap-498"><span class="linenos">498</span></a>
</span><span id="OpSequenceOffsetMap-499"><a href="#OpSequenceOffsetMap-499"><span class="linenos">499</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequenceOffsetMap</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap-500"><a href="#OpSequenceOffsetMap-500"><span class="linenos">500</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_num</span> <span class="o">=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-501"><a href="#OpSequenceOffsetMap-501"><span class="linenos">501</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="OpSequenceOffsetMap-502"><a href="#OpSequenceOffsetMap-502"><span class="linenos">502</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap-503"><a href="#OpSequenceOffsetMap-503"><span class="linenos">503</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap-504"><a href="#OpSequenceOffsetMap-504"><span class="linenos">504</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="OpSequenceOffsetMap-505"><a href="#OpSequenceOffsetMap-505"><span class="linenos">505</span></a>
</span><span id="OpSequenceOffsetMap-506"><a href="#OpSequenceOffsetMap-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap-507"><a href="#OpSequenceOffsetMap-507"><span class="linenos">507</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="OpSequenceOffsetMap-508"><a href="#OpSequenceOffsetMap-508"><span class="linenos">508</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-509"><a href="#OpSequenceOffsetMap-509"><span class="linenos">509</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;new_by_original&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-510"><a href="#OpSequenceOffsetMap-510"><span class="linenos">510</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;original_by_new&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-511"><a href="#OpSequenceOffsetMap-511"><span class="linenos">511</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;op_num&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap-512"><a href="#OpSequenceOffsetMap-512"><span class="linenos">512</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;range&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap-513"><a href="#OpSequenceOffsetMap-513"><span class="linenos">513</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="OpSequenceOffsetMap.__init__" class="classattr">
                                        <input id="OpSequenceOffsetMap.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">OpSequenceOffsetMap</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span>)</span>

                <label class="view-source-button" for="OpSequenceOffsetMap.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.__init__-361"><a href="#OpSequenceOffsetMap.__init__-361"><span class="linenos">361</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.__init__-362"><a href="#OpSequenceOffsetMap.__init__-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.__init__-363"><a href="#OpSequenceOffsetMap.__init__-363"><span class="linenos">363</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">op_num</span><span class="p">)</span> <span class="k">if</span> <span class="n">op_num</span> <span class="k">else</span> <span class="kc">None</span>
</span><span id="OpSequenceOffsetMap.__init__-364"><a href="#OpSequenceOffsetMap.__init__-364"><span class="linenos">364</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap.__init__-365"><a href="#OpSequenceOffsetMap.__init__-365"><span class="linenos">365</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap.__init__-366"><a href="#OpSequenceOffsetMap.__init__-366"><span class="linenos">366</span></a>        <span class="k">if</span> <span class="n">op_num</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.__init__-367"><a href="#OpSequenceOffsetMap.__init__-367"><span class="linenos">367</span></a>            <span class="n">op_num</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequenceOffsetMap.__init__-368"><a href="#OpSequenceOffsetMap.__init__-368"><span class="linenos">368</span></a>        
</span><span id="OpSequenceOffsetMap.__init__-369"><a href="#OpSequenceOffsetMap.__init__-369"><span class="linenos">369</span></a>        <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">op_num</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.__init__-370"><a href="#OpSequenceOffsetMap.__init__-370"><span class="linenos">370</span></a>            <span class="c1"># bindex = index * 2</span>
</span><span id="OpSequenceOffsetMap.__init__-371"><a href="#OpSequenceOffsetMap.__init__-371"><span class="linenos">371</span></a>            <span class="n">bindex</span> <span class="o">=</span> <span class="n">index</span>
</span><span id="OpSequenceOffsetMap.__init__-372"><a href="#OpSequenceOffsetMap.__init__-372"><span class="linenos">372</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span><span id="OpSequenceOffsetMap.__init__-373"><a href="#OpSequenceOffsetMap.__init__-373"><span class="linenos">373</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">bindex</span><span class="p">]</span> <span class="o">=</span> <span class="n">bindex</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.op_num" class="classattr">
                                <div class="attr variable">
            <span class="name">op_num</span><span class="annotation">: int</span>

        
    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.op_num"></a>
    
    

                            </div>
                            <div id="OpSequenceOffsetMap.range" class="classattr">
                                <div class="attr variable">
            <span class="name">range</span><span class="annotation">: Union[slice, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.range"></a>
    
    

                            </div>
                            <div id="OpSequenceOffsetMap.new_by_original" class="classattr">
                                <div class="attr variable">
            <span class="name">new_by_original</span><span class="annotation">: Dict[int, int]</span>

        
    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.new_by_original"></a>
    
    

                            </div>
                            <div id="OpSequenceOffsetMap.original_by_new" class="classattr">
                                <div class="attr variable">
            <span class="name">original_by_new</span><span class="annotation">: Dict[int, int]</span>

        
    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.original_by_new"></a>
    
    

                            </div>
                            <div id="OpSequenceOffsetMap.mapped_range" class="classattr">
                                        <input id="OpSequenceOffsetMap.mapped_range-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mapped_range</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">slice</span>:</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.mapped_range-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.mapped_range"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.mapped_range-375"><a href="#OpSequenceOffsetMap.mapped_range-375"><span class="linenos">375</span></a>    <span class="k">def</span> <span class="nf">mapped_range</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">slice</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.mapped_range-376"><a href="#OpSequenceOffsetMap.mapped_range-376"><span class="linenos">376</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.remove_slice" class="classattr">
                                        <input id="OpSequenceOffsetMap.remove_slice-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_slice</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.remove_slice-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.remove_slice"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.remove_slice-379"><a href="#OpSequenceOffsetMap.remove_slice-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.remove_slice-380"><a href="#OpSequenceOffsetMap.remove_slice-380"><span class="linenos">380</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-381"><a href="#OpSequenceOffsetMap.remove_slice-381"><span class="linenos">381</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap.remove_slice-382"><a href="#OpSequenceOffsetMap.remove_slice-382"><span class="linenos">382</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-383"><a href="#OpSequenceOffsetMap.remove_slice-383"><span class="linenos">383</span></a>        <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequenceOffsetMap.remove_slice-384"><a href="#OpSequenceOffsetMap.remove_slice-384"><span class="linenos">384</span></a>        <span class="n">del_start</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequenceOffsetMap.remove_slice-385"><a href="#OpSequenceOffsetMap.remove_slice-385"><span class="linenos">385</span></a>        <span class="n">del_stop</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.remove_slice-386"><a href="#OpSequenceOffsetMap.remove_slice-386"><span class="linenos">386</span></a>
</span><span id="OpSequenceOffsetMap.remove_slice-387"><a href="#OpSequenceOffsetMap.remove_slice-387"><span class="linenos">387</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap.remove_slice-388"><a href="#OpSequenceOffsetMap.remove_slice-388"><span class="linenos">388</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap.remove_slice-389"><a href="#OpSequenceOffsetMap.remove_slice-389"><span class="linenos">389</span></a>        <span class="n">to_be_deleted</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap.remove_slice-390"><a href="#OpSequenceOffsetMap.remove_slice-390"><span class="linenos">390</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap.remove_slice-391"><a href="#OpSequenceOffsetMap.remove_slice-391"><span class="linenos">391</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-392"><a href="#OpSequenceOffsetMap.remove_slice-392"><span class="linenos">392</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">original</span><span class="p">,</span> <span class="n">new</span><span class="p">))</span>
</span><span id="OpSequenceOffsetMap.remove_slice-393"><a href="#OpSequenceOffsetMap.remove_slice-393"><span class="linenos">393</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-394"><a href="#OpSequenceOffsetMap.remove_slice-394"><span class="linenos">394</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="OpSequenceOffsetMap.remove_slice-395"><a href="#OpSequenceOffsetMap.remove_slice-395"><span class="linenos">395</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-396"><a href="#OpSequenceOffsetMap.remove_slice-396"><span class="linenos">396</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-397"><a href="#OpSequenceOffsetMap.remove_slice-397"><span class="linenos">397</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-398"><a href="#OpSequenceOffsetMap.remove_slice-398"><span class="linenos">398</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-399"><a href="#OpSequenceOffsetMap.remove_slice-399"><span class="linenos">399</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-400"><a href="#OpSequenceOffsetMap.remove_slice-400"><span class="linenos">400</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-401"><a href="#OpSequenceOffsetMap.remove_slice-401"><span class="linenos">401</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap.remove_slice-402"><a href="#OpSequenceOffsetMap.remove_slice-402"><span class="linenos">402</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap.remove_slice-403"><a href="#OpSequenceOffsetMap.remove_slice-403"><span class="linenos">403</span></a>        <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap.remove_slice-404"><a href="#OpSequenceOffsetMap.remove_slice-404"><span class="linenos">404</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap.remove_slice-405"><a href="#OpSequenceOffsetMap.remove_slice-405"><span class="linenos">405</span></a>            <span class="k">if</span> <span class="n">del_start</span> <span class="o">&lt;=</span> <span class="n">new</span> <span class="o">&lt;</span> <span class="n">del_stop</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-406"><a href="#OpSequenceOffsetMap.remove_slice-406"><span class="linenos">406</span></a>                <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">new</span><span class="p">,</span> <span class="n">original</span><span class="p">))</span>
</span><span id="OpSequenceOffsetMap.remove_slice-407"><a href="#OpSequenceOffsetMap.remove_slice-407"><span class="linenos">407</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-408"><a href="#OpSequenceOffsetMap.remove_slice-408"><span class="linenos">408</span></a>        <span class="n">to_be_deleted</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="n">key</span><span class="o">=</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="OpSequenceOffsetMap.remove_slice-409"><a href="#OpSequenceOffsetMap.remove_slice-409"><span class="linenos">409</span></a>        <span class="k">if</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-410"><a href="#OpSequenceOffsetMap.remove_slice-410"><span class="linenos">410</span></a>            <span class="n">ignored</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[:</span><span class="n">preserver_index_for_first_x_op</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-411"><a href="#OpSequenceOffsetMap.remove_slice-411"><span class="linenos">411</span></a>            <span class="k">if</span> <span class="n">ignored</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-412"><a href="#OpSequenceOffsetMap.remove_slice-412"><span class="linenos">412</span></a>                <span class="n">last_ignored</span> <span class="o">=</span> <span class="n">ignored</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-413"><a href="#OpSequenceOffsetMap.remove_slice-413"><span class="linenos">413</span></a>                <span class="n">last_ignored_new</span> <span class="o">=</span> <span class="n">last_ignored</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-414"><a href="#OpSequenceOffsetMap.remove_slice-414"><span class="linenos">414</span></a>                <span class="n">offset_change_start</span> <span class="o">=</span> <span class="n">last_ignored_new</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequenceOffsetMap.remove_slice-415"><a href="#OpSequenceOffsetMap.remove_slice-415"><span class="linenos">415</span></a>            
</span><span id="OpSequenceOffsetMap.remove_slice-416"><a href="#OpSequenceOffsetMap.remove_slice-416"><span class="linenos">416</span></a>            <span class="n">to_be_deleted</span> <span class="o">=</span> <span class="n">to_be_deleted</span><span class="p">[</span><span class="n">preserver_index_for_first_x_op</span><span class="p">:]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-417"><a href="#OpSequenceOffsetMap.remove_slice-417"><span class="linenos">417</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-418"><a href="#OpSequenceOffsetMap.remove_slice-418"><span class="linenos">418</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">to_be_deleted</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.remove_slice-419"><a href="#OpSequenceOffsetMap.remove_slice-419"><span class="linenos">419</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span>
</span><span id="OpSequenceOffsetMap.remove_slice-420"><a href="#OpSequenceOffsetMap.remove_slice-420"><span class="linenos">420</span></a>        
</span><span id="OpSequenceOffsetMap.remove_slice-421"><a href="#OpSequenceOffsetMap.remove_slice-421"><span class="linenos">421</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="o">-</span><span class="n">op_num</span><span class="p">,</span> <span class="n">offset_change_start</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.remove_slice-422"><a href="#OpSequenceOffsetMap.remove_slice-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">-=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.remove_slice-423"><a href="#OpSequenceOffsetMap.remove_slice-423"><span class="linenos">423</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_num</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.insert_slice" class="classattr">
                                        <input id="OpSequenceOffsetMap.insert_slice-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">insert_slice</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.insert_slice-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.insert_slice"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.insert_slice-425"><a href="#OpSequenceOffsetMap.insert_slice-425"><span class="linenos">425</span></a>    <span class="k">def</span> <span class="nf">insert_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.insert_slice-426"><a href="#OpSequenceOffsetMap.insert_slice-426"><span class="linenos">426</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.insert_slice-427"><a href="#OpSequenceOffsetMap.insert_slice-427"><span class="linenos">427</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap.insert_slice-428"><a href="#OpSequenceOffsetMap.insert_slice-428"><span class="linenos">428</span></a>        
</span><span id="OpSequenceOffsetMap.insert_slice-429"><a href="#OpSequenceOffsetMap.insert_slice-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_num</span><span class="p">,</span> <span class="n">op_index</span> <span class="o">+</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.insert_slice-430"><a href="#OpSequenceOffsetMap.insert_slice-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span> <span class="o">+=</span> <span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.insert_slice-431"><a href="#OpSequenceOffsetMap.insert_slice-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_num</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.insert_op_sequence_offset" class="classattr">
                                        <input id="OpSequenceOffsetMap.insert_op_sequence_offset-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">insert_op_sequence_offset</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="n"><a href="#OpSequenceOffsetMap">OpSequenceOffsetMap</a></span>,</span><span class="param">	<span class="n">insertion_id</span><span class="p">:</span> <span class="n">Any</span>,</span><span class="param">	<span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.insert_op_sequence_offset-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.insert_op_sequence_offset"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-433"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">insertion_id</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-434"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-434"><span class="linenos">434</span></a>        <span class="n">op_num</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-435"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_num</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-436"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-436"><span class="linenos">436</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-437"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-437"><span class="linenos">437</span></a>        
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-438"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-438"><span class="linenos">438</span></a>        <span class="n">sequence_range</span><span class="p">:</span> <span class="nb">slice</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">range</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-439"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-439"><span class="linenos">439</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="n">sequence_range</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-440"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-440"><span class="linenos">440</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">insert_slice</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="n">op_num</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-441"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-441"><span class="linenos">441</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap.insert_op_sequence_offset-442"><a href="#OpSequenceOffsetMap.insert_op_sequence_offset-442"><span class="linenos">442</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span> <span class="o">+</span> <span class="n">offset</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">insertion_id</span><span class="p">,</span> <span class="n">new</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.add_offset" class="classattr">
                                        <input id="OpSequenceOffsetMap.add_offset-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_offset</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">op_start</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.add_offset-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.add_offset"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.add_offset-444"><a href="#OpSequenceOffsetMap.add_offset-444"><span class="linenos">444</span></a>    <span class="k">def</span> <span class="nf">add_offset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_start</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.add_offset-445"><a href="#OpSequenceOffsetMap.add_offset-445"><span class="linenos">445</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.add_offset-446"><a href="#OpSequenceOffsetMap.add_offset-446"><span class="linenos">446</span></a>            <span class="k">return</span>
</span><span id="OpSequenceOffsetMap.add_offset-447"><a href="#OpSequenceOffsetMap.add_offset-447"><span class="linenos">447</span></a>        
</span><span id="OpSequenceOffsetMap.add_offset-448"><a href="#OpSequenceOffsetMap.add_offset-448"><span class="linenos">448</span></a>        <span class="n">new_by_original_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span>
</span><span id="OpSequenceOffsetMap.add_offset-449"><a href="#OpSequenceOffsetMap.add_offset-449"><span class="linenos">449</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap.add_offset-450"><a href="#OpSequenceOffsetMap.add_offset-450"><span class="linenos">450</span></a>        <span class="k">for</span> <span class="n">original</span><span class="p">,</span> <span class="n">new</span> <span class="ow">in</span> <span class="n">new_by_original_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap.add_offset-451"><a href="#OpSequenceOffsetMap.add_offset-451"><span class="linenos">451</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.add_offset-452"><a href="#OpSequenceOffsetMap.add_offset-452"><span class="linenos">452</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="OpSequenceOffsetMap.add_offset-453"><a href="#OpSequenceOffsetMap.add_offset-453"><span class="linenos">453</span></a>            
</span><span id="OpSequenceOffsetMap.add_offset-454"><a href="#OpSequenceOffsetMap.add_offset-454"><span class="linenos">454</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">original</span><span class="p">]</span> <span class="o">=</span> <span class="n">new</span>
</span><span id="OpSequenceOffsetMap.add_offset-455"><a href="#OpSequenceOffsetMap.add_offset-455"><span class="linenos">455</span></a>        
</span><span id="OpSequenceOffsetMap.add_offset-456"><a href="#OpSequenceOffsetMap.add_offset-456"><span class="linenos">456</span></a>        <span class="n">original_by_new_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span>
</span><span id="OpSequenceOffsetMap.add_offset-457"><a href="#OpSequenceOffsetMap.add_offset-457"><span class="linenos">457</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)()</span>
</span><span id="OpSequenceOffsetMap.add_offset-458"><a href="#OpSequenceOffsetMap.add_offset-458"><span class="linenos">458</span></a>        <span class="k">for</span> <span class="n">new</span><span class="p">,</span> <span class="n">original</span> <span class="ow">in</span> <span class="n">original_by_new_buff</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequenceOffsetMap.add_offset-459"><a href="#OpSequenceOffsetMap.add_offset-459"><span class="linenos">459</span></a>            <span class="k">if</span> <span class="n">new</span> <span class="o">&gt;=</span> <span class="n">op_start</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.add_offset-460"><a href="#OpSequenceOffsetMap.add_offset-460"><span class="linenos">460</span></a>                <span class="n">new</span> <span class="o">+=</span> <span class="n">op_offset</span>
</span><span id="OpSequenceOffsetMap.add_offset-461"><a href="#OpSequenceOffsetMap.add_offset-461"><span class="linenos">461</span></a>            
</span><span id="OpSequenceOffsetMap.add_offset-462"><a href="#OpSequenceOffsetMap.add_offset-462"><span class="linenos">462</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">[</span><span class="n">new</span><span class="p">]</span> <span class="o">=</span> <span class="n">original</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.shift" class="classattr">
                                        <input id="OpSequenceOffsetMap.shift-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shift</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.shift-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.shift"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.shift-464"><a href="#OpSequenceOffsetMap.shift-464"><span class="linenos">464</span></a>    <span class="k">def</span> <span class="nf">shift</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.shift-465"><a href="#OpSequenceOffsetMap.shift-465"><span class="linenos">465</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.shift-466"><a href="#OpSequenceOffsetMap.shift-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.shift_to_absolute" class="classattr">
                                        <input id="OpSequenceOffsetMap.shift_to_absolute-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">shift_to_absolute</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.shift_to_absolute-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.shift_to_absolute"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.shift_to_absolute-468"><a href="#OpSequenceOffsetMap.shift_to_absolute-468"><span class="linenos">468</span></a>    <span class="k">def</span> <span class="nf">shift_to_absolute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.shift_to_absolute-469"><a href="#OpSequenceOffsetMap.shift_to_absolute-469"><span class="linenos">469</span></a>        <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequenceOffsetMap.shift_to_absolute-470"><a href="#OpSequenceOffsetMap.shift_to_absolute-470"><span class="linenos">470</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.shift_to_absolute-471"><a href="#OpSequenceOffsetMap.shift_to_absolute-471"><span class="linenos">471</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">range</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">start</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="o">.</span><span class="n">stop</span> <span class="o">+</span> <span class="n">op_offset</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.update" class="classattr">
                                        <input id="OpSequenceOffsetMap.update-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">update</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="n"><a href="#OpSequenceOffsetMap">OpSequenceOffsetMap</a></span>,</span><span class="param">	<span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.update-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.update"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.update-473"><a href="#OpSequenceOffsetMap.update-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="s1">&#39;OpSequenceOffsetMap&#39;</span><span class="p">,</span> <span class="n">op_offset</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.update-474"><a href="#OpSequenceOffsetMap.update-474"><span class="linenos">474</span></a>        <span class="k">if</span> <span class="n">op_offset</span><span class="p">:</span>
</span><span id="OpSequenceOffsetMap.update-475"><a href="#OpSequenceOffsetMap.update-475"><span class="linenos">475</span></a>            <span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</span><span id="OpSequenceOffsetMap.update-476"><a href="#OpSequenceOffsetMap.update-476"><span class="linenos">476</span></a>            <span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">add_offset</span><span class="p">(</span><span class="n">op_offset</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.update-477"><a href="#OpSequenceOffsetMap.update-477"><span class="linenos">477</span></a>        
</span><span id="OpSequenceOffsetMap.update-478"><a href="#OpSequenceOffsetMap.update-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.update-479"><a href="#OpSequenceOffsetMap.update-479"><span class="linenos">479</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequenceOffsetMap.copy" class="classattr">
                                        <input id="OpSequenceOffsetMap.copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequenceOffsetMap.copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequenceOffsetMap.copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequenceOffsetMap.copy-506"><a href="#OpSequenceOffsetMap.copy-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequenceOffsetMap.copy-507"><a href="#OpSequenceOffsetMap.copy-507"><span class="linenos">507</span></a>        <span class="bp">cls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span>
</span><span id="OpSequenceOffsetMap.copy-508"><a href="#OpSequenceOffsetMap.copy-508"><span class="linenos">508</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">cls</span><span class="o">.</span><span class="fm">__new__</span><span class="p">(</span><span class="bp">cls</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.copy-509"><a href="#OpSequenceOffsetMap.copy-509"><span class="linenos">509</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;new_by_original&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.copy-510"><a href="#OpSequenceOffsetMap.copy-510"><span class="linenos">510</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;original_by_new&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">original_by_new</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.copy-511"><a href="#OpSequenceOffsetMap.copy-511"><span class="linenos">511</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;op_num&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_num</span>
</span><span id="OpSequenceOffsetMap.copy-512"><a href="#OpSequenceOffsetMap.copy-512"><span class="linenos">512</span></a>        <span class="n">result</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="s1">&#39;range&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">range</span><span class="p">)</span>
</span><span id="OpSequenceOffsetMap.copy-513"><a href="#OpSequenceOffsetMap.copy-513"><span class="linenos">513</span></a>        <span class="k">return</span> <span class="n">result</span>
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
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.entities.copyable.versions.v_0.copyable.CopyMethodsMixin</dt>
                                <dd id="OpSequenceOffsetMap.shallow_copy" class="function">shallow_copy</dd>
                <dd id="OpSequenceOffsetMap.updated_copy" class="function">updated_copy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="opcode">
                            <input id="opcode-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">opcode</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="opcode-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#opcode"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="opcode-516"><a href="#opcode-516"><span class="linenos">516</span></a><span class="k">def</span> <span class="nf">opcode</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="opcode-517"><a href="#opcode-517"><span class="linenos">517</span></a>    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</span><span id="opcode-518"><a href="#opcode-518"><span class="linenos">518</span></a>    <span class="k">return</span> <span class="n">opmap</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span></pre></div>


    

                </section>
                <section id="opcode_name">
                            <input id="opcode_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">opcode_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">opcode</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="opcode_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#opcode_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="opcode_name-521"><a href="#opcode_name-521"><span class="linenos">521</span></a><span class="k">def</span> <span class="nf">opcode_name</span><span class="p">(</span><span class="n">opcode</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="opcode_name-522"><a href="#opcode_name-522"><span class="linenos">522</span></a>    <span class="k">return</span> <span class="n">opname</span><span class="p">[</span><span class="n">opcode</span><span class="p">]</span>
</span></pre></div>


    

                </section>
                <section id="OpSequence">
                            <input id="OpSequence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">OpSequence</span>:

                <label class="view-source-button" for="OpSequence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence-525"><a href="#OpSequence-525"><span class="linenos">525</span></a><span class="k">class</span> <span class="nc">OpSequence</span><span class="p">:</span>
</span><span id="OpSequence-526"><a href="#OpSequence-526"><span class="linenos">526</span></a>    <span class="n">extended_arg_opcode_int</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">)</span>
</span><span id="OpSequence-527"><a href="#OpSequence-527"><span class="linenos">527</span></a>    <span class="n">extended_arg_opcode_byte</span> <span class="o">=</span> <span class="n">extended_arg_opcode_int</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="OpSequence-528"><a href="#OpSequence-528"><span class="linenos">528</span></a>
</span><span id="OpSequence-529"><a href="#OpSequence-529"><span class="linenos">529</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="OpSequence-530"><a href="#OpSequence-530"><span class="linenos">530</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span> <span class="k">if</span> <span class="n">op_sequence</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">op_sequence</span>
</span><span id="OpSequence-531"><a href="#OpSequence-531"><span class="linenos">531</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="n">OpSequenceOffsetMap</span> <span class="o">=</span> <span class="n">OpSequenceOffsetMap</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">))</span>
</span><span id="OpSequence-532"><a href="#OpSequence-532"><span class="linenos">532</span></a>    
</span><span id="OpSequence-533"><a href="#OpSequence-533"><span class="linenos">533</span></a>    <span class="k">def</span> <span class="fm">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence-534"><a href="#OpSequence-534"><span class="linenos">534</span></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence-535"><a href="#OpSequence-535"><span class="linenos">535</span></a>    
</span><span id="OpSequence-536"><a href="#OpSequence-536"><span class="linenos">536</span></a>    <span class="k">def</span> <span class="nf">read_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">:</span>
</span><span id="OpSequence-537"><a href="#OpSequence-537"><span class="linenos">537</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">()</span>
</span><span id="OpSequence-538"><a href="#OpSequence-538"><span class="linenos">538</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="OpSequence-539"><a href="#OpSequence-539"><span class="linenos">539</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="OpSequence-540"><a href="#OpSequence-540"><span class="linenos">540</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="OpSequence-541"><a href="#OpSequence-541"><span class="linenos">541</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="OpSequence-542"><a href="#OpSequence-542"><span class="linenos">542</span></a>    
</span><span id="OpSequence-543"><a href="#OpSequence-543"><span class="linenos">543</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequence-544"><a href="#OpSequence-544"><span class="linenos">544</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="OpSequence-545"><a href="#OpSequence-545"><span class="linenos">545</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">place</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequence-546"><a href="#OpSequence-546"><span class="linenos">546</span></a>    
</span><span id="OpSequence-547"><a href="#OpSequence-547"><span class="linenos">547</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequence-548"><a href="#OpSequence-548"><span class="linenos">548</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">:</span> <span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span>
</span><span id="OpSequence-549"><a href="#OpSequence-549"><span class="linenos">549</span></a>        <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="OpSequence-550"><a href="#OpSequence-550"><span class="linenos">550</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">insert_op_sequence_offset</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequence-551"><a href="#OpSequence-551"><span class="linenos">551</span></a>        <span class="k">return</span> <span class="n">op_sequence</span>
</span><span id="OpSequence-552"><a href="#OpSequence-552"><span class="linenos">552</span></a>    
</span><span id="OpSequence-553"><a href="#OpSequence-553"><span class="linenos">553</span></a>    <span class="k">def</span> <span class="nf">normalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence-554"><a href="#OpSequence-554"><span class="linenos">554</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="OpSequence-555"><a href="#OpSequence-555"><span class="linenos">555</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence-556"><a href="#OpSequence-556"><span class="linenos">556</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="OpSequence-557"><a href="#OpSequence-557"><span class="linenos">557</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="OpSequence-558"><a href="#OpSequence-558"><span class="linenos">558</span></a>                <span class="k">break</span>
</span><span id="OpSequence-559"><a href="#OpSequence-559"><span class="linenos">559</span></a>
</span><span id="OpSequence-560"><a href="#OpSequence-560"><span class="linenos">560</span></a>            <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence-561"><a href="#OpSequence-561"><span class="linenos">561</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence-562"><a href="#OpSequence-562"><span class="linenos">562</span></a>                <span class="k">if</span> <span class="n">arg</span> <span class="o">&gt;</span> <span class="mi">255</span><span class="p">:</span>
</span><span id="OpSequence-563"><a href="#OpSequence-563"><span class="linenos">563</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="OpSequence-564"><a href="#OpSequence-564"><span class="linenos">564</span></a>                    <span class="k">if</span> <span class="n">real_op_index</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence-565"><a href="#OpSequence-565"><span class="linenos">565</span></a>                        <span class="n">real_op_index_delta</span> <span class="o">=</span> <span class="n">real_op_index</span> <span class="o">-</span> <span class="n">op_index</span>
</span><span id="OpSequence-566"><a href="#OpSequence-566"><span class="linenos">566</span></a>                        <span class="n">real_op_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">-</span> <span class="n">real_op_index_delta</span>
</span><span id="OpSequence-567"><a href="#OpSequence-567"><span class="linenos">567</span></a>                        <span class="n">slice_to_delete</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">real_op_index</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
</span><span id="OpSequence-568"><a href="#OpSequence-568"><span class="linenos">568</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">slice_to_delete</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence-569"><a href="#OpSequence-569"><span class="linenos">569</span></a>                        <span class="n">index</span> <span class="o">=</span> <span class="n">real_op_index</span>
</span><span id="OpSequence-570"><a href="#OpSequence-570"><span class="linenos">570</span></a>
</span><span id="OpSequence-571"><a href="#OpSequence-571"><span class="linenos">571</span></a>                    <span class="n">extended_arg</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="OpSequence-572"><a href="#OpSequence-572"><span class="linenos">572</span></a>                    <span class="n">extended_arg_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">)</span>
</span><span id="OpSequence-573"><a href="#OpSequence-573"><span class="linenos">573</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequence-574"><a href="#OpSequence-574"><span class="linenos">574</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">,</span> <span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="n">index</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="OpSequence-575"><a href="#OpSequence-575"><span class="linenos">575</span></a>                    <span class="n">op_sub_sequence_instructions</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence-576"><a href="#OpSequence-576"><span class="linenos">576</span></a>                    <span class="k">for</span> <span class="n">extended_arg_int</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">):</span>
</span><span id="OpSequence-577"><a href="#OpSequence-577"><span class="linenos">577</span></a>                        <span class="n">op_sub_sequence_instructions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">make_instruction</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">,</span> <span class="n">extended_arg_int</span><span class="p">))</span>
</span><span id="OpSequence-578"><a href="#OpSequence-578"><span class="linenos">578</span></a>                    
</span><span id="OpSequence-579"><a href="#OpSequence-579"><span class="linenos">579</span></a>                    <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions_fast</span><span class="p">(</span><span class="n">op_sub_sequence_instructions</span><span class="p">)</span>
</span><span id="OpSequence-580"><a href="#OpSequence-580"><span class="linenos">580</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence-581"><a href="#OpSequence-581"><span class="linenos">581</span></a>                    <span class="n">index</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence-582"><a href="#OpSequence-582"><span class="linenos">582</span></a>    
</span><span id="OpSequence-583"><a href="#OpSequence-583"><span class="linenos">583</span></a>    <span class="k">def</span> <span class="nf">denormalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence-584"><a href="#OpSequence-584"><span class="linenos">584</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="OpSequence-585"><a href="#OpSequence-585"><span class="linenos">585</span></a>    
</span><span id="OpSequence-586"><a href="#OpSequence-586"><span class="linenos">586</span></a>    <span class="k">def</span> <span class="nf">find_op</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="OpSequence-587"><a href="#OpSequence-587"><span class="linenos">587</span></a>        <span class="n">start_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence-588"><a href="#OpSequence-588"><span class="linenos">588</span></a>        <span class="n">end_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence-589"><a href="#OpSequence-589"><span class="linenos">589</span></a>
</span><span id="OpSequence-590"><a href="#OpSequence-590"><span class="linenos">590</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="OpSequence-591"><a href="#OpSequence-591"><span class="linenos">591</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence-592"><a href="#OpSequence-592"><span class="linenos">592</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="OpSequence-593"><a href="#OpSequence-593"><span class="linenos">593</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="OpSequence-594"><a href="#OpSequence-594"><span class="linenos">594</span></a>                <span class="k">break</span>
</span><span id="OpSequence-595"><a href="#OpSequence-595"><span class="linenos">595</span></a>
</span><span id="OpSequence-596"><a href="#OpSequence-596"><span class="linenos">596</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence-597"><a href="#OpSequence-597"><span class="linenos">597</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="OpSequence-598"><a href="#OpSequence-598"><span class="linenos">598</span></a>                <span class="k">continue</span>
</span><span id="OpSequence-599"><a href="#OpSequence-599"><span class="linenos">599</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-600"><a href="#OpSequence-600"><span class="linenos">600</span></a>                <span class="n">end_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequence-601"><a href="#OpSequence-601"><span class="linenos">601</span></a>                <span class="k">break</span>
</span><span id="OpSequence-602"><a href="#OpSequence-602"><span class="linenos">602</span></a>        
</span><span id="OpSequence-603"><a href="#OpSequence-603"><span class="linenos">603</span></a>        <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence-604"><a href="#OpSequence-604"><span class="linenos">604</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequence-605"><a href="#OpSequence-605"><span class="linenos">605</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence-606"><a href="#OpSequence-606"><span class="linenos">606</span></a>            <span class="n">index</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="OpSequence-607"><a href="#OpSequence-607"><span class="linenos">607</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="OpSequence-608"><a href="#OpSequence-608"><span class="linenos">608</span></a>                <span class="k">if</span> <span class="n">previous_op_is_extended_arg</span><span class="p">:</span>
</span><span id="OpSequence-609"><a href="#OpSequence-609"><span class="linenos">609</span></a>                    <span class="n">start_index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequence-610"><a href="#OpSequence-610"><span class="linenos">610</span></a>                
</span><span id="OpSequence-611"><a href="#OpSequence-611"><span class="linenos">611</span></a>                <span class="k">break</span>
</span><span id="OpSequence-612"><a href="#OpSequence-612"><span class="linenos">612</span></a>            
</span><span id="OpSequence-613"><a href="#OpSequence-613"><span class="linenos">613</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence-614"><a href="#OpSequence-614"><span class="linenos">614</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="OpSequence-615"><a href="#OpSequence-615"><span class="linenos">615</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="OpSequence-616"><a href="#OpSequence-616"><span class="linenos">616</span></a>                <span class="k">continue</span>
</span><span id="OpSequence-617"><a href="#OpSequence-617"><span class="linenos">617</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-618"><a href="#OpSequence-618"><span class="linenos">618</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="OpSequence-619"><a href="#OpSequence-619"><span class="linenos">619</span></a>                <span class="n">start_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequence-620"><a href="#OpSequence-620"><span class="linenos">620</span></a>                <span class="k">break</span>
</span><span id="OpSequence-621"><a href="#OpSequence-621"><span class="linenos">621</span></a>        
</span><span id="OpSequence-622"><a href="#OpSequence-622"><span class="linenos">622</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">start_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">end_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="OpSequence-623"><a href="#OpSequence-623"><span class="linenos">623</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="OpSequence-624"><a href="#OpSequence-624"><span class="linenos">624</span></a>        
</span><span id="OpSequence-625"><a href="#OpSequence-625"><span class="linenos">625</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="n">start_index</span><span class="p">,</span> <span class="n">end_index</span><span class="p">)</span>
</span><span id="OpSequence-626"><a href="#OpSequence-626"><span class="linenos">626</span></a>    
</span><span id="OpSequence-627"><a href="#OpSequence-627"><span class="linenos">627</span></a>    <span class="k">def</span> <span class="nf">get_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="OpSequence-628"><a href="#OpSequence-628"><span class="linenos">628</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequence-629"><a href="#OpSequence-629"><span class="linenos">629</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="OpSequence-630"><a href="#OpSequence-630"><span class="linenos">630</span></a>        
</span><span id="OpSequence-631"><a href="#OpSequence-631"><span class="linenos">631</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="OpSequence-632"><a href="#OpSequence-632"><span class="linenos">632</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="OpSequence-633"><a href="#OpSequence-633"><span class="linenos">633</span></a>        
</span><span id="OpSequence-634"><a href="#OpSequence-634"><span class="linenos">634</span></a>        <span class="n">op_slice</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="OpSequence-635"><a href="#OpSequence-635"><span class="linenos">635</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence-636"><a href="#OpSequence-636"><span class="linenos">636</span></a>            <span class="n">arg_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence-637"><a href="#OpSequence-637"><span class="linenos">637</span></a>            <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">op_slice</span><span class="p">):</span>
</span><span id="OpSequence-638"><a href="#OpSequence-638"><span class="linenos">638</span></a>                <span class="n">arg_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="OpSequence-639"><a href="#OpSequence-639"><span class="linenos">639</span></a>            
</span><span id="OpSequence-640"><a href="#OpSequence-640"><span class="linenos">640</span></a>            <span class="k">return</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">arg_list</span><span class="p">))</span>
</span><span id="OpSequence-641"><a href="#OpSequence-641"><span class="linenos">641</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-642"><a href="#OpSequence-642"><span class="linenos">642</span></a>            <span class="k">return</span> <span class="n">op_slice</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequence-643"><a href="#OpSequence-643"><span class="linenos">643</span></a>    
</span><span id="OpSequence-644"><a href="#OpSequence-644"><span class="linenos">644</span></a>    <span class="k">def</span> <span class="nf">set_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">],</span> <span class="n">new_arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]):</span>
</span><span id="OpSequence-645"><a href="#OpSequence-645"><span class="linenos">645</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequence-646"><a href="#OpSequence-646"><span class="linenos">646</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="OpSequence-647"><a href="#OpSequence-647"><span class="linenos">647</span></a>        
</span><span id="OpSequence-648"><a href="#OpSequence-648"><span class="linenos">648</span></a>        <span class="n">op_index_len</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence-649"><a href="#OpSequence-649"><span class="linenos">649</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">op_index_len</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="OpSequence-650"><a href="#OpSequence-650"><span class="linenos">650</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="OpSequence-651"><a href="#OpSequence-651"><span class="linenos">651</span></a>        
</span><span id="OpSequence-652"><a href="#OpSequence-652"><span class="linenos">652</span></a>        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">new_arg</span><span class="p">)</span>
</span><span id="OpSequence-653"><a href="#OpSequence-653"><span class="linenos">653</span></a>        <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequence-654"><a href="#OpSequence-654"><span class="linenos">654</span></a>        <span class="n">sub_op_sequence_bytes</span> <span class="o">=</span> <span class="p">[</span><span class="n">current_op</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">]</span>
</span><span id="OpSequence-655"><a href="#OpSequence-655"><span class="linenos">655</span></a>        <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">sub_op_sequence_bytes</span><span class="p">)))</span>
</span><span id="OpSequence-656"><a href="#OpSequence-656"><span class="linenos">656</span></a>        <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="OpSequence-657"><a href="#OpSequence-657"><span class="linenos">657</span></a>        <span class="n">real_arg</span> <span class="o">=</span> <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequence-658"><a href="#OpSequence-658"><span class="linenos">658</span></a>        <span class="n">sub_op_sequence_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence-659"><a href="#OpSequence-659"><span class="linenos">659</span></a>        <span class="n">extended_args_len</span> <span class="o">=</span> <span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="OpSequence-660"><a href="#OpSequence-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">extended_args_len</span><span class="p">:</span>
</span><span id="OpSequence-661"><a href="#OpSequence-661"><span class="linenos">661</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence-662"><a href="#OpSequence-662"><span class="linenos">662</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence-663"><a href="#OpSequence-663"><span class="linenos">663</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">+</span> <span class="n">extended_args_len</span>
</span><span id="OpSequence-664"><a href="#OpSequence-664"><span class="linenos">664</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence-665"><a href="#OpSequence-665"><span class="linenos">665</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-666"><a href="#OpSequence-666"><span class="linenos">666</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence-667"><a href="#OpSequence-667"><span class="linenos">667</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence-668"><a href="#OpSequence-668"><span class="linenos">668</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence-669"><a href="#OpSequence-669"><span class="linenos">669</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence-670"><a href="#OpSequence-670"><span class="linenos">670</span></a>
</span><span id="OpSequence-671"><a href="#OpSequence-671"><span class="linenos">671</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_op</span><span class="p">,</span> <span class="n">real_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span><span class="p">)</span>
</span><span id="OpSequence-672"><a href="#OpSequence-672"><span class="linenos">672</span></a>
</span><span id="OpSequence-673"><a href="#OpSequence-673"><span class="linenos">673</span></a>        <span class="k">if</span> <span class="n">sub_op_sequence_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence-674"><a href="#OpSequence-674"><span class="linenos">674</span></a>            <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">sub_op_sequence_len</span><span class="p">))</span>
</span><span id="OpSequence-675"><a href="#OpSequence-675"><span class="linenos">675</span></a>            <span class="k">if</span> <span class="n">op_index_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence-676"><a href="#OpSequence-676"><span class="linenos">676</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence-677"><a href="#OpSequence-677"><span class="linenos">677</span></a>            
</span><span id="OpSequence-678"><a href="#OpSequence-678"><span class="linenos">678</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence-679"><a href="#OpSequence-679"><span class="linenos">679</span></a>
</span><span id="OpSequence-680"><a href="#OpSequence-680"><span class="linenos">680</span></a>    <span class="k">def</span> <span class="nf">fix_labels</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]):</span>
</span><span id="OpSequence-681"><a href="#OpSequence-681"><span class="linenos">681</span></a>        <span class="n">labels</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">op_by_label</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="OpSequence-682"><a href="#OpSequence-682"><span class="linenos">682</span></a>        <span class="n">labels</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="OpSequence-683"><a href="#OpSequence-683"><span class="linenos">683</span></a>        <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequence-684"><a href="#OpSequence-684"><span class="linenos">684</span></a>            <span class="n">data</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="OpSequence-685"><a href="#OpSequence-685"><span class="linenos">685</span></a>        
</span><span id="OpSequence-686"><a href="#OpSequence-686"><span class="linenos">686</span></a>        <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">labels</span><span class="p">:</span>
</span><span id="OpSequence-687"><a href="#OpSequence-687"><span class="linenos">687</span></a>            <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence-688"><a href="#OpSequence-688"><span class="linenos">688</span></a>            <span class="n">label_data</span> <span class="o">=</span> <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence-689"><a href="#OpSequence-689"><span class="linenos">689</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence-690"><a href="#OpSequence-690"><span class="linenos">690</span></a>                <span class="k">for</span> <span class="n">op_index</span> <span class="ow">in</span> <span class="n">label_data</span><span class="p">:</span>
</span><span id="OpSequence-691"><a href="#OpSequence-691"><span class="linenos">691</span></a>                    <span class="n">op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="OpSequence-692"><a href="#OpSequence-692"><span class="linenos">692</span></a>                    <span class="n">op</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index_new</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequence-693"><a href="#OpSequence-693"><span class="linenos">693</span></a>                    <span class="n">new_arg</span> <span class="o">=</span> <span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">labeled_op_index_new</span><span class="p">)</span>
</span><span id="OpSequence-694"><a href="#OpSequence-694"><span class="linenos">694</span></a>                    <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="OpSequence-695"><a href="#OpSequence-695"><span class="linenos">695</span></a>                        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">new_arg</span> <span class="o">-</span> <span class="p">(</span><span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">)</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="OpSequence-696"><a href="#OpSequence-696"><span class="linenos">696</span></a>                    
</span><span id="OpSequence-697"><a href="#OpSequence-697"><span class="linenos">697</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">set_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">)</span>
</span><span id="OpSequence-698"><a href="#OpSequence-698"><span class="linenos">698</span></a>                
</span><span id="OpSequence-699"><a href="#OpSequence-699"><span class="linenos">699</span></a>                <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence-700"><a href="#OpSequence-700"><span class="linenos">700</span></a>                <span class="k">if</span> <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">==</span> <span class="n">labeled_op_index_new</span><span class="p">:</span>
</span><span id="OpSequence-701"><a href="#OpSequence-701"><span class="linenos">701</span></a>                    <span class="k">break</span>
</span><span id="OpSequence-702"><a href="#OpSequence-702"><span class="linenos">702</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-703"><a href="#OpSequence-703"><span class="linenos">703</span></a>                    <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="n">labeled_op_index_new_after_value_change</span>
</span><span id="OpSequence-704"><a href="#OpSequence-704"><span class="linenos">704</span></a>
</span><span id="OpSequence-705"><a href="#OpSequence-705"><span class="linenos">705</span></a>    <span class="k">def</span> <span class="nf">to_sequence_of_ints</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence-706"><a href="#OpSequence-706"><span class="linenos">706</span></a>        <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span>
</span><span id="OpSequence-707"><a href="#OpSequence-707"><span class="linenos">707</span></a>            <span class="k">yield</span> <span class="n">op</span>
</span><span id="OpSequence-708"><a href="#OpSequence-708"><span class="linenos">708</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence-709"><a href="#OpSequence-709"><span class="linenos">709</span></a>                <span class="k">yield</span> <span class="mi">0</span>
</span><span id="OpSequence-710"><a href="#OpSequence-710"><span class="linenos">710</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence-711"><a href="#OpSequence-711"><span class="linenos">711</span></a>                <span class="k">yield</span> <span class="n">arg</span>
</span><span id="OpSequence-712"><a href="#OpSequence-712"><span class="linenos">712</span></a>
</span><span id="OpSequence-713"><a href="#OpSequence-713"><span class="linenos">713</span></a>    <span class="k">def</span> <span class="nf">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="OpSequence-714"><a href="#OpSequence-714"><span class="linenos">714</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">to_sequence_of_ints</span><span class="p">())</span>
</span><span id="OpSequence-715"><a href="#OpSequence-715"><span class="linenos">715</span></a>        
</span><span id="OpSequence-716"><a href="#OpSequence-716"><span class="linenos">716</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence-717"><a href="#OpSequence-717"><span class="linenos">717</span></a>    <span class="k">def</span> <span class="nf">from_bytecode_sequence</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">):</span>
</span><span id="OpSequence-718"><a href="#OpSequence-718"><span class="linenos">718</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="OpSequence-719"><a href="#OpSequence-719"><span class="linenos">719</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">))),</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="OpSequence-720"><a href="#OpSequence-720"><span class="linenos">720</span></a>    
</span><span id="OpSequence-721"><a href="#OpSequence-721"><span class="linenos">721</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence-722"><a href="#OpSequence-722"><span class="linenos">722</span></a>    <span class="k">def</span> <span class="nf">from_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="OpSequence-723"><a href="#OpSequence-723"><span class="linenos">723</span></a>        <span class="n">code_bytes</span><span class="p">:</span> <span class="n">BytecodeSequence</span> <span class="o">=</span> <span class="n">_get_code_object</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="o">.</span><span class="n">co_code</span>
</span><span id="OpSequence-724"><a href="#OpSequence-724"><span class="linenos">724</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_bytecode_sequence</span><span class="p">(</span><span class="n">code_bytes</span><span class="p">)</span>
</span><span id="OpSequence-725"><a href="#OpSequence-725"><span class="linenos">725</span></a>    
</span><span id="OpSequence-726"><a href="#OpSequence-726"><span class="linenos">726</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence-727"><a href="#OpSequence-727"><span class="linenos">727</span></a>    <span class="k">def</span> <span class="nf">from_instructions</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="OpSequence-728"><a href="#OpSequence-728"><span class="linenos">728</span></a>        <span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence-729"><a href="#OpSequence-729"><span class="linenos">729</span></a>        <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="OpSequence-730"><a href="#OpSequence-730"><span class="linenos">730</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="OpSequence-731"><a href="#OpSequence-731"><span class="linenos">731</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence-732"><a href="#OpSequence-732"><span class="linenos">732</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequence-733"><a href="#OpSequence-733"><span class="linenos">733</span></a>
</span><span id="OpSequence-734"><a href="#OpSequence-734"><span class="linenos">734</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">))</span>
</span><span id="OpSequence-735"><a href="#OpSequence-735"><span class="linenos">735</span></a>
</span><span id="OpSequence-736"><a href="#OpSequence-736"><span class="linenos">736</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence-737"><a href="#OpSequence-737"><span class="linenos">737</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)))</span>
</span><span id="OpSequence-738"><a href="#OpSequence-738"><span class="linenos">738</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="OpSequence-739"><a href="#OpSequence-739"><span class="linenos">739</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span><span id="OpSequence-740"><a href="#OpSequence-740"><span class="linenos">740</span></a>    
</span><span id="OpSequence-741"><a href="#OpSequence-741"><span class="linenos">741</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence-742"><a href="#OpSequence-742"><span class="linenos">742</span></a>    <span class="k">def</span> <span class="nf">from_instructions_fast</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="OpSequence-743"><a href="#OpSequence-743"><span class="linenos">743</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">normalize_instructions_arg</span><span class="p">(</span><span class="n">instructions</span><span class="p">)))))</span>
</span></pre></div>


    

                            <div id="OpSequence.__init__" class="classattr">
                                        <input id="OpSequence.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">OpSequence</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">op_sequence</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="OpSequence.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.__init__-529"><a href="#OpSequence.__init__-529"><span class="linenos">529</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="OpSequence.__init__-530"><a href="#OpSequence.__init__-530"><span class="linenos">530</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span> <span class="k">if</span> <span class="n">op_sequence</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">op_sequence</span>
</span><span id="OpSequence.__init__-531"><a href="#OpSequence.__init__-531"><span class="linenos">531</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">:</span> <span class="n">OpSequenceOffsetMap</span> <span class="o">=</span> <span class="n">OpSequenceOffsetMap</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.extended_arg_opcode_int" class="classattr">
                                <div class="attr variable">
            <span class="name">extended_arg_opcode_int</span>        =
<span class="default_value">144</span>

        
    </div>
    <a class="headerlink" href="#OpSequence.extended_arg_opcode_int"></a>
    
    

                            </div>
                            <div id="OpSequence.extended_arg_opcode_byte" class="classattr">
                                <div class="attr variable">
            <span class="name">extended_arg_opcode_byte</span>        =
<span class="default_value">b&#39;\x90&#39;</span>

        
    </div>
    <a class="headerlink" href="#OpSequence.extended_arg_opcode_byte"></a>
    
    

                            </div>
                            <div id="OpSequence.op_sequence" class="classattr">
                                <div class="attr variable">
            <span class="name">op_sequence</span><span class="annotation">: List[Tuple[int, int, int, int, int, int]]</span>

        
    </div>
    <a class="headerlink" href="#OpSequence.op_sequence"></a>
    
    

                            </div>
                            <div id="OpSequence.op_sequence_offset_map" class="classattr">
                                <div class="attr variable">
            <span class="name">op_sequence_offset_map</span><span class="annotation">: <a href="#OpSequenceOffsetMap">OpSequenceOffsetMap</a></span>

        
    </div>
    <a class="headerlink" href="#OpSequence.op_sequence_offset_map"></a>
    
    

                            </div>
                            <div id="OpSequence.read_slice" class="classattr">
                                        <input id="OpSequence.read_slice-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_slice</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">place</span><span class="p">:</span> <span class="nb">slice</span></span><span class="return-annotation">) -> <span class="n"><a href="#OpSequence">OpSequence</a></span>:</span></span>

                <label class="view-source-button" for="OpSequence.read_slice-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.read_slice"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.read_slice-536"><a href="#OpSequence.read_slice-536"><span class="linenos">536</span></a>    <span class="k">def</span> <span class="nf">read_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">:</span>
</span><span id="OpSequence.read_slice-537"><a href="#OpSequence.read_slice-537"><span class="linenos">537</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">()</span>
</span><span id="OpSequence.read_slice-538"><a href="#OpSequence.read_slice-538"><span class="linenos">538</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="OpSequence.read_slice-539"><a href="#OpSequence.read_slice-539"><span class="linenos">539</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">[</span><span class="n">place</span><span class="p">]</span>
</span><span id="OpSequence.read_slice-540"><a href="#OpSequence.read_slice-540"><span class="linenos">540</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="OpSequence.read_slice-541"><a href="#OpSequence.read_slice-541"><span class="linenos">541</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.remove_slice" class="classattr">
                                        <input id="OpSequence.remove_slice-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_slice</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">place</span><span class="p">:</span> <span class="nb">slice</span>, </span><span class="param"><span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.remove_slice-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.remove_slice"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.remove_slice-543"><a href="#OpSequence.remove_slice-543"><span class="linenos">543</span></a>    <span class="k">def</span> <span class="nf">remove_slice</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">place</span><span class="p">:</span> <span class="nb">slice</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequence.remove_slice-544"><a href="#OpSequence.remove_slice-544"><span class="linenos">544</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="OpSequence.remove_slice-545"><a href="#OpSequence.remove_slice-545"><span class="linenos">545</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">place</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">place</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.insert_op_sequence" class="classattr">
                                        <input id="OpSequence.insert_op_sequence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">insert_op_sequence</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">index</span><span class="p">:</span> <span class="nb">int</span>,</span><span class="param">	<span class="n">op_sequence</span><span class="p">:</span> <span class="n"><a href="#OpSequence">OpSequence</a></span>,</span><span class="param">	<span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.insert_op_sequence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.insert_op_sequence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.insert_op_sequence-547"><a href="#OpSequence.insert_op_sequence-547"><span class="linenos">547</span></a>    <span class="k">def</span> <span class="nf">insert_op_sequence</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="OpSequence.insert_op_sequence-548"><a href="#OpSequence.insert_op_sequence-548"><span class="linenos">548</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">:</span> <span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span>
</span><span id="OpSequence.insert_op_sequence-549"><a href="#OpSequence.insert_op_sequence-549"><span class="linenos">549</span></a>        <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">shift_to_absolute</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="OpSequence.insert_op_sequence-550"><a href="#OpSequence.insert_op_sequence-550"><span class="linenos">550</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">insert_op_sequence_offset</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="p">,</span> <span class="n">op_sequence</span><span class="p">,</span> <span class="n">preserver_index_for_first_x_op</span><span class="p">)</span>
</span><span id="OpSequence.insert_op_sequence-551"><a href="#OpSequence.insert_op_sequence-551"><span class="linenos">551</span></a>        <span class="k">return</span> <span class="n">op_sequence</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.normalize_instructions_arg" class="classattr">
                                        <input id="OpSequence.normalize_instructions_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">normalize_instructions_arg</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.normalize_instructions_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.normalize_instructions_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.normalize_instructions_arg-553"><a href="#OpSequence.normalize_instructions_arg-553"><span class="linenos">553</span></a>    <span class="k">def</span> <span class="nf">normalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence.normalize_instructions_arg-554"><a href="#OpSequence.normalize_instructions_arg-554"><span class="linenos">554</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="OpSequence.normalize_instructions_arg-555"><a href="#OpSequence.normalize_instructions_arg-555"><span class="linenos">555</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence.normalize_instructions_arg-556"><a href="#OpSequence.normalize_instructions_arg-556"><span class="linenos">556</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="OpSequence.normalize_instructions_arg-557"><a href="#OpSequence.normalize_instructions_arg-557"><span class="linenos">557</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="OpSequence.normalize_instructions_arg-558"><a href="#OpSequence.normalize_instructions_arg-558"><span class="linenos">558</span></a>                <span class="k">break</span>
</span><span id="OpSequence.normalize_instructions_arg-559"><a href="#OpSequence.normalize_instructions_arg-559"><span class="linenos">559</span></a>
</span><span id="OpSequence.normalize_instructions_arg-560"><a href="#OpSequence.normalize_instructions_arg-560"><span class="linenos">560</span></a>            <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence.normalize_instructions_arg-561"><a href="#OpSequence.normalize_instructions_arg-561"><span class="linenos">561</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence.normalize_instructions_arg-562"><a href="#OpSequence.normalize_instructions_arg-562"><span class="linenos">562</span></a>                <span class="k">if</span> <span class="n">arg</span> <span class="o">&gt;</span> <span class="mi">255</span><span class="p">:</span>
</span><span id="OpSequence.normalize_instructions_arg-563"><a href="#OpSequence.normalize_instructions_arg-563"><span class="linenos">563</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-564"><a href="#OpSequence.normalize_instructions_arg-564"><span class="linenos">564</span></a>                    <span class="k">if</span> <span class="n">real_op_index</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence.normalize_instructions_arg-565"><a href="#OpSequence.normalize_instructions_arg-565"><span class="linenos">565</span></a>                        <span class="n">real_op_index_delta</span> <span class="o">=</span> <span class="n">real_op_index</span> <span class="o">-</span> <span class="n">op_index</span>
</span><span id="OpSequence.normalize_instructions_arg-566"><a href="#OpSequence.normalize_instructions_arg-566"><span class="linenos">566</span></a>                        <span class="n">real_op_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">-</span> <span class="n">real_op_index_delta</span>
</span><span id="OpSequence.normalize_instructions_arg-567"><a href="#OpSequence.normalize_instructions_arg-567"><span class="linenos">567</span></a>                        <span class="n">slice_to_delete</span> <span class="o">=</span> <span class="nb">slice</span><span class="p">(</span><span class="n">real_op_index</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-568"><a href="#OpSequence.normalize_instructions_arg-568"><span class="linenos">568</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="n">slice_to_delete</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-569"><a href="#OpSequence.normalize_instructions_arg-569"><span class="linenos">569</span></a>                        <span class="n">index</span> <span class="o">=</span> <span class="n">real_op_index</span>
</span><span id="OpSequence.normalize_instructions_arg-570"><a href="#OpSequence.normalize_instructions_arg-570"><span class="linenos">570</span></a>
</span><span id="OpSequence.normalize_instructions_arg-571"><a href="#OpSequence.normalize_instructions_arg-571"><span class="linenos">571</span></a>                    <span class="n">extended_arg</span><span class="p">:</span> <span class="nb">bytes</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="OpSequence.normalize_instructions_arg-572"><a href="#OpSequence.normalize_instructions_arg-572"><span class="linenos">572</span></a>                    <span class="n">extended_arg_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-573"><a href="#OpSequence.normalize_instructions_arg-573"><span class="linenos">573</span></a>                    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequence.normalize_instructions_arg-574"><a href="#OpSequence.normalize_instructions_arg-574"><span class="linenos">574</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">,</span> <span class="p">(</span><span class="n">index</span> <span class="o">+</span> <span class="n">extended_arg_len</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="n">index</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-575"><a href="#OpSequence.normalize_instructions_arg-575"><span class="linenos">575</span></a>                    <span class="n">op_sub_sequence_instructions</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence.normalize_instructions_arg-576"><a href="#OpSequence.normalize_instructions_arg-576"><span class="linenos">576</span></a>                    <span class="k">for</span> <span class="n">extended_arg_int</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">):</span>
</span><span id="OpSequence.normalize_instructions_arg-577"><a href="#OpSequence.normalize_instructions_arg-577"><span class="linenos">577</span></a>                        <span class="n">op_sub_sequence_instructions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">make_instruction</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">,</span> <span class="n">extended_arg_int</span><span class="p">))</span>
</span><span id="OpSequence.normalize_instructions_arg-578"><a href="#OpSequence.normalize_instructions_arg-578"><span class="linenos">578</span></a>                    
</span><span id="OpSequence.normalize_instructions_arg-579"><a href="#OpSequence.normalize_instructions_arg-579"><span class="linenos">579</span></a>                    <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="s1">&#39;OpSequence&#39;</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions_fast</span><span class="p">(</span><span class="n">op_sub_sequence_instructions</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-580"><a href="#OpSequence.normalize_instructions_arg-580"><span class="linenos">580</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence.normalize_instructions_arg-581"><a href="#OpSequence.normalize_instructions_arg-581"><span class="linenos">581</span></a>                    <span class="n">index</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.denormalize_instructions_arg" class="classattr">
                                        <input id="OpSequence.denormalize_instructions_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">denormalize_instructions_arg</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.denormalize_instructions_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.denormalize_instructions_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.denormalize_instructions_arg-583"><a href="#OpSequence.denormalize_instructions_arg-583"><span class="linenos">583</span></a>    <span class="k">def</span> <span class="nf">denormalize_instructions_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence.denormalize_instructions_arg-584"><a href="#OpSequence.denormalize_instructions_arg-584"><span class="linenos">584</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.find_op" class="classattr">
                                        <input id="OpSequence.find_op-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_op</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="nb">slice</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="OpSequence.find_op-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.find_op"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.find_op-586"><a href="#OpSequence.find_op-586"><span class="linenos">586</span></a>    <span class="k">def</span> <span class="nf">find_op</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">slice</span><span class="p">]:</span>
</span><span id="OpSequence.find_op-587"><a href="#OpSequence.find_op-587"><span class="linenos">587</span></a>        <span class="n">start_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence.find_op-588"><a href="#OpSequence.find_op-588"><span class="linenos">588</span></a>        <span class="n">end_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence.find_op-589"><a href="#OpSequence.find_op-589"><span class="linenos">589</span></a>
</span><span id="OpSequence.find_op-590"><a href="#OpSequence.find_op-590"><span class="linenos">590</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="OpSequence.find_op-591"><a href="#OpSequence.find_op-591"><span class="linenos">591</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence.find_op-592"><a href="#OpSequence.find_op-592"><span class="linenos">592</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="OpSequence.find_op-593"><a href="#OpSequence.find_op-593"><span class="linenos">593</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="OpSequence.find_op-594"><a href="#OpSequence.find_op-594"><span class="linenos">594</span></a>                <span class="k">break</span>
</span><span id="OpSequence.find_op-595"><a href="#OpSequence.find_op-595"><span class="linenos">595</span></a>
</span><span id="OpSequence.find_op-596"><a href="#OpSequence.find_op-596"><span class="linenos">596</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence.find_op-597"><a href="#OpSequence.find_op-597"><span class="linenos">597</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="OpSequence.find_op-598"><a href="#OpSequence.find_op-598"><span class="linenos">598</span></a>                <span class="k">continue</span>
</span><span id="OpSequence.find_op-599"><a href="#OpSequence.find_op-599"><span class="linenos">599</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.find_op-600"><a href="#OpSequence.find_op-600"><span class="linenos">600</span></a>                <span class="n">end_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequence.find_op-601"><a href="#OpSequence.find_op-601"><span class="linenos">601</span></a>                <span class="k">break</span>
</span><span id="OpSequence.find_op-602"><a href="#OpSequence.find_op-602"><span class="linenos">602</span></a>        
</span><span id="OpSequence.find_op-603"><a href="#OpSequence.find_op-603"><span class="linenos">603</span></a>        <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence.find_op-604"><a href="#OpSequence.find_op-604"><span class="linenos">604</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="OpSequence.find_op-605"><a href="#OpSequence.find_op-605"><span class="linenos">605</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence.find_op-606"><a href="#OpSequence.find_op-606"><span class="linenos">606</span></a>            <span class="n">index</span> <span class="o">-=</span> <span class="mi">1</span>
</span><span id="OpSequence.find_op-607"><a href="#OpSequence.find_op-607"><span class="linenos">607</span></a>            <span class="k">if</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="OpSequence.find_op-608"><a href="#OpSequence.find_op-608"><span class="linenos">608</span></a>                <span class="k">if</span> <span class="n">previous_op_is_extended_arg</span><span class="p">:</span>
</span><span id="OpSequence.find_op-609"><a href="#OpSequence.find_op-609"><span class="linenos">609</span></a>                    <span class="n">start_index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequence.find_op-610"><a href="#OpSequence.find_op-610"><span class="linenos">610</span></a>                
</span><span id="OpSequence.find_op-611"><a href="#OpSequence.find_op-611"><span class="linenos">611</span></a>                <span class="k">break</span>
</span><span id="OpSequence.find_op-612"><a href="#OpSequence.find_op-612"><span class="linenos">612</span></a>            
</span><span id="OpSequence.find_op-613"><a href="#OpSequence.find_op-613"><span class="linenos">613</span></a>            <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="OpSequence.find_op-614"><a href="#OpSequence.find_op-614"><span class="linenos">614</span></a>            <span class="k">if</span> <span class="n">current_op</span> <span class="o">==</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">extended_arg_opcode_int</span><span class="p">:</span>
</span><span id="OpSequence.find_op-615"><a href="#OpSequence.find_op-615"><span class="linenos">615</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="OpSequence.find_op-616"><a href="#OpSequence.find_op-616"><span class="linenos">616</span></a>                <span class="k">continue</span>
</span><span id="OpSequence.find_op-617"><a href="#OpSequence.find_op-617"><span class="linenos">617</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.find_op-618"><a href="#OpSequence.find_op-618"><span class="linenos">618</span></a>                <span class="n">previous_op_is_extended_arg</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="OpSequence.find_op-619"><a href="#OpSequence.find_op-619"><span class="linenos">619</span></a>                <span class="n">start_index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="OpSequence.find_op-620"><a href="#OpSequence.find_op-620"><span class="linenos">620</span></a>                <span class="k">break</span>
</span><span id="OpSequence.find_op-621"><a href="#OpSequence.find_op-621"><span class="linenos">621</span></a>        
</span><span id="OpSequence.find_op-622"><a href="#OpSequence.find_op-622"><span class="linenos">622</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">start_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">end_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="OpSequence.find_op-623"><a href="#OpSequence.find_op-623"><span class="linenos">623</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="OpSequence.find_op-624"><a href="#OpSequence.find_op-624"><span class="linenos">624</span></a>        
</span><span id="OpSequence.find_op-625"><a href="#OpSequence.find_op-625"><span class="linenos">625</span></a>        <span class="k">return</span> <span class="nb">slice</span><span class="p">(</span><span class="n">start_index</span><span class="p">,</span> <span class="n">end_index</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.get_arg" class="classattr">
                                        <input id="OpSequence.get_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_arg</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="OpSequence.get_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.get_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.get_arg-627"><a href="#OpSequence.get_arg-627"><span class="linenos">627</span></a>    <span class="k">def</span> <span class="nf">get_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="OpSequence.get_arg-628"><a href="#OpSequence.get_arg-628"><span class="linenos">628</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequence.get_arg-629"><a href="#OpSequence.get_arg-629"><span class="linenos">629</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="OpSequence.get_arg-630"><a href="#OpSequence.get_arg-630"><span class="linenos">630</span></a>        
</span><span id="OpSequence.get_arg-631"><a href="#OpSequence.get_arg-631"><span class="linenos">631</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="OpSequence.get_arg-632"><a href="#OpSequence.get_arg-632"><span class="linenos">632</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="OpSequence.get_arg-633"><a href="#OpSequence.get_arg-633"><span class="linenos">633</span></a>        
</span><span id="OpSequence.get_arg-634"><a href="#OpSequence.get_arg-634"><span class="linenos">634</span></a>        <span class="n">op_slice</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="OpSequence.get_arg-635"><a href="#OpSequence.get_arg-635"><span class="linenos">635</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence.get_arg-636"><a href="#OpSequence.get_arg-636"><span class="linenos">636</span></a>            <span class="n">arg_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence.get_arg-637"><a href="#OpSequence.get_arg-637"><span class="linenos">637</span></a>            <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">op_slice</span><span class="p">):</span>
</span><span id="OpSequence.get_arg-638"><a href="#OpSequence.get_arg-638"><span class="linenos">638</span></a>                <span class="n">arg_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="OpSequence.get_arg-639"><a href="#OpSequence.get_arg-639"><span class="linenos">639</span></a>            
</span><span id="OpSequence.get_arg-640"><a href="#OpSequence.get_arg-640"><span class="linenos">640</span></a>            <span class="k">return</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="nb">bytes</span><span class="p">(</span><span class="n">arg_list</span><span class="p">))</span>
</span><span id="OpSequence.get_arg-641"><a href="#OpSequence.get_arg-641"><span class="linenos">641</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.get_arg-642"><a href="#OpSequence.get_arg-642"><span class="linenos">642</span></a>            <span class="k">return</span> <span class="n">op_slice</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.set_arg" class="classattr">
                                        <input id="OpSequence.set_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_arg</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">]</span>,</span><span class="param">	<span class="n">new_arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">NoneType</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.set_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.set_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.set_arg-644"><a href="#OpSequence.set_arg-644"><span class="linenos">644</span></a>    <span class="k">def</span> <span class="nf">set_arg</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_index</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">slice</span><span class="p">],</span> <span class="n">new_arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]):</span>
</span><span id="OpSequence.set_arg-645"><a href="#OpSequence.set_arg-645"><span class="linenos">645</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">op_index</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="OpSequence.set_arg-646"><a href="#OpSequence.set_arg-646"><span class="linenos">646</span></a>            <span class="n">op_index</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">find_op</span><span class="p">(</span><span class="n">op_index</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-647"><a href="#OpSequence.set_arg-647"><span class="linenos">647</span></a>        
</span><span id="OpSequence.set_arg-648"><a href="#OpSequence.set_arg-648"><span class="linenos">648</span></a>        <span class="n">op_index_len</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence.set_arg-649"><a href="#OpSequence.set_arg-649"><span class="linenos">649</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">op_index</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">op_index_len</span> <span class="o">&lt;</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="OpSequence.set_arg-650"><a href="#OpSequence.set_arg-650"><span class="linenos">650</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;OP not found by index&#39;</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-651"><a href="#OpSequence.set_arg-651"><span class="linenos">651</span></a>        
</span><span id="OpSequence.set_arg-652"><a href="#OpSequence.set_arg-652"><span class="linenos">652</span></a>        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">new_arg</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-653"><a href="#OpSequence.set_arg-653"><span class="linenos">653</span></a>        <span class="n">current_op</span><span class="p">,</span> <span class="n">current_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequence.set_arg-654"><a href="#OpSequence.set_arg-654"><span class="linenos">654</span></a>        <span class="n">sub_op_sequence_bytes</span> <span class="o">=</span> <span class="p">[</span><span class="n">current_op</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">]</span>
</span><span id="OpSequence.set_arg-655"><a href="#OpSequence.set_arg-655"><span class="linenos">655</span></a>        <span class="n">sub_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">sub_op_sequence_bytes</span><span class="p">)))</span>
</span><span id="OpSequence.set_arg-656"><a href="#OpSequence.set_arg-656"><span class="linenos">656</span></a>        <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="OpSequence.set_arg-657"><a href="#OpSequence.set_arg-657"><span class="linenos">657</span></a>        <span class="n">real_arg</span> <span class="o">=</span> <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="OpSequence.set_arg-658"><a href="#OpSequence.set_arg-658"><span class="linenos">658</span></a>        <span class="n">sub_op_sequence_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-659"><a href="#OpSequence.set_arg-659"><span class="linenos">659</span></a>        <span class="n">extended_args_len</span> <span class="o">=</span> <span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="OpSequence.set_arg-660"><a href="#OpSequence.set_arg-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">extended_args_len</span><span class="p">:</span>
</span><span id="OpSequence.set_arg-661"><a href="#OpSequence.set_arg-661"><span class="linenos">661</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence.set_arg-662"><a href="#OpSequence.set_arg-662"><span class="linenos">662</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence.set_arg-663"><a href="#OpSequence.set_arg-663"><span class="linenos">663</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">current_real_op_index</span> <span class="o">+</span> <span class="n">extended_args_len</span>
</span><span id="OpSequence.set_arg-664"><a href="#OpSequence.set_arg-664"><span class="linenos">664</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence.set_arg-665"><a href="#OpSequence.set_arg-665"><span class="linenos">665</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.set_arg-666"><a href="#OpSequence.set_arg-666"><span class="linenos">666</span></a>            <span class="n">current_op_index</span> <span class="o">=</span> <span class="n">op_index</span><span class="o">.</span><span class="n">start</span>
</span><span id="OpSequence.set_arg-667"><a href="#OpSequence.set_arg-667"><span class="linenos">667</span></a>            <span class="n">current_offset</span> <span class="o">=</span> <span class="n">current_op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span><span id="OpSequence.set_arg-668"><a href="#OpSequence.set_arg-668"><span class="linenos">668</span></a>            <span class="n">current_real_op_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence.set_arg-669"><a href="#OpSequence.set_arg-669"><span class="linenos">669</span></a>            <span class="n">current_real_offset</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="OpSequence.set_arg-670"><a href="#OpSequence.set_arg-670"><span class="linenos">670</span></a>
</span><span id="OpSequence.set_arg-671"><a href="#OpSequence.set_arg-671"><span class="linenos">671</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">current_op</span><span class="p">,</span> <span class="n">real_arg</span><span class="p">,</span> <span class="n">current_op_index</span><span class="p">,</span> <span class="n">current_offset</span><span class="p">,</span> <span class="n">current_real_op_index</span><span class="p">,</span> <span class="n">current_real_offset</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-672"><a href="#OpSequence.set_arg-672"><span class="linenos">672</span></a>
</span><span id="OpSequence.set_arg-673"><a href="#OpSequence.set_arg-673"><span class="linenos">673</span></a>        <span class="k">if</span> <span class="n">sub_op_sequence_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence.set_arg-674"><a href="#OpSequence.set_arg-674"><span class="linenos">674</span></a>            <span class="n">sub_op_sequence</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">sub_op_sequence_len</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">sub_op_sequence_len</span><span class="p">))</span>
</span><span id="OpSequence.set_arg-675"><a href="#OpSequence.set_arg-675"><span class="linenos">675</span></a>            <span class="k">if</span> <span class="n">op_index_len</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="OpSequence.set_arg-676"><a href="#OpSequence.set_arg-676"><span class="linenos">676</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">remove_slice</span><span class="p">(</span><span class="nb">slice</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">op_index</span><span class="o">.</span><span class="n">stop</span> <span class="o">-</span> <span class="mi">1</span><span class="p">),</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="OpSequence.set_arg-677"><a href="#OpSequence.set_arg-677"><span class="linenos">677</span></a>            
</span><span id="OpSequence.set_arg-678"><a href="#OpSequence.set_arg-678"><span class="linenos">678</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">op_index</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="n">sub_op_sequence</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.fix_labels" class="classattr">
                                        <input id="OpSequence.fix_labels-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fix_labels</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.fix_labels-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.fix_labels"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.fix_labels-680"><a href="#OpSequence.fix_labels-680"><span class="linenos">680</span></a>    <span class="k">def</span> <span class="nf">fix_labels</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]]):</span>
</span><span id="OpSequence.fix_labels-681"><a href="#OpSequence.fix_labels-681"><span class="linenos">681</span></a>        <span class="n">labels</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">op_by_label</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="OpSequence.fix_labels-682"><a href="#OpSequence.fix_labels-682"><span class="linenos">682</span></a>        <span class="n">labels</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="OpSequence.fix_labels-683"><a href="#OpSequence.fix_labels-683"><span class="linenos">683</span></a>        <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="OpSequence.fix_labels-684"><a href="#OpSequence.fix_labels-684"><span class="linenos">684</span></a>            <span class="n">data</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
</span><span id="OpSequence.fix_labels-685"><a href="#OpSequence.fix_labels-685"><span class="linenos">685</span></a>        
</span><span id="OpSequence.fix_labels-686"><a href="#OpSequence.fix_labels-686"><span class="linenos">686</span></a>        <span class="k">for</span> <span class="n">label</span> <span class="ow">in</span> <span class="n">labels</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-687"><a href="#OpSequence.fix_labels-687"><span class="linenos">687</span></a>            <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence.fix_labels-688"><a href="#OpSequence.fix_labels-688"><span class="linenos">688</span></a>            <span class="n">label_data</span> <span class="o">=</span> <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence.fix_labels-689"><a href="#OpSequence.fix_labels-689"><span class="linenos">689</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-690"><a href="#OpSequence.fix_labels-690"><span class="linenos">690</span></a>                <span class="k">for</span> <span class="n">op_index</span> <span class="ow">in</span> <span class="n">label_data</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-691"><a href="#OpSequence.fix_labels-691"><span class="linenos">691</span></a>                    <span class="n">op_index_new</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">op_index</span><span class="p">]</span>
</span><span id="OpSequence.fix_labels-692"><a href="#OpSequence.fix_labels-692"><span class="linenos">692</span></a>                    <span class="n">op</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">op_index_new</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>
</span><span id="OpSequence.fix_labels-693"><a href="#OpSequence.fix_labels-693"><span class="linenos">693</span></a>                    <span class="n">new_arg</span> <span class="o">=</span> <span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">labeled_op_index_new</span><span class="p">)</span>
</span><span id="OpSequence.fix_labels-694"><a href="#OpSequence.fix_labels-694"><span class="linenos">694</span></a>                    <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-695"><a href="#OpSequence.fix_labels-695"><span class="linenos">695</span></a>                        <span class="n">new_arg</span> <span class="o">=</span> <span class="n">new_arg</span> <span class="o">-</span> <span class="p">(</span><span class="n">op_index_to_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">)</span> <span class="o">+</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="OpSequence.fix_labels-696"><a href="#OpSequence.fix_labels-696"><span class="linenos">696</span></a>                    
</span><span id="OpSequence.fix_labels-697"><a href="#OpSequence.fix_labels-697"><span class="linenos">697</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">set_arg</span><span class="p">(</span><span class="n">op_index_new</span><span class="p">,</span> <span class="n">new_arg</span><span class="p">)</span>
</span><span id="OpSequence.fix_labels-698"><a href="#OpSequence.fix_labels-698"><span class="linenos">698</span></a>                
</span><span id="OpSequence.fix_labels-699"><a href="#OpSequence.fix_labels-699"><span class="linenos">699</span></a>                <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">label</span><span class="p">]</span>
</span><span id="OpSequence.fix_labels-700"><a href="#OpSequence.fix_labels-700"><span class="linenos">700</span></a>                <span class="k">if</span> <span class="n">labeled_op_index_new_after_value_change</span> <span class="o">==</span> <span class="n">labeled_op_index_new</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-701"><a href="#OpSequence.fix_labels-701"><span class="linenos">701</span></a>                    <span class="k">break</span>
</span><span id="OpSequence.fix_labels-702"><a href="#OpSequence.fix_labels-702"><span class="linenos">702</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.fix_labels-703"><a href="#OpSequence.fix_labels-703"><span class="linenos">703</span></a>                    <span class="n">labeled_op_index_new</span> <span class="o">=</span> <span class="n">labeled_op_index_new_after_value_change</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.to_sequence_of_ints" class="classattr">
                                        <input id="OpSequence.to_sequence_of_ints-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_sequence_of_ints</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.to_sequence_of_ints-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.to_sequence_of_ints"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.to_sequence_of_ints-705"><a href="#OpSequence.to_sequence_of_ints-705"><span class="linenos">705</span></a>    <span class="k">def</span> <span class="nf">to_sequence_of_ints</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="OpSequence.to_sequence_of_ints-706"><a href="#OpSequence.to_sequence_of_ints-706"><span class="linenos">706</span></a>        <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">:</span>
</span><span id="OpSequence.to_sequence_of_ints-707"><a href="#OpSequence.to_sequence_of_ints-707"><span class="linenos">707</span></a>            <span class="k">yield</span> <span class="n">op</span>
</span><span id="OpSequence.to_sequence_of_ints-708"><a href="#OpSequence.to_sequence_of_ints-708"><span class="linenos">708</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence.to_sequence_of_ints-709"><a href="#OpSequence.to_sequence_of_ints-709"><span class="linenos">709</span></a>                <span class="k">yield</span> <span class="mi">0</span>
</span><span id="OpSequence.to_sequence_of_ints-710"><a href="#OpSequence.to_sequence_of_ints-710"><span class="linenos">710</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="OpSequence.to_sequence_of_ints-711"><a href="#OpSequence.to_sequence_of_ints-711"><span class="linenos">711</span></a>                <span class="k">yield</span> <span class="n">arg</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.to_bytes" class="classattr">
                                        <input id="OpSequence.to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="OpSequence.to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.to_bytes-713"><a href="#OpSequence.to_bytes-713"><span class="linenos">713</span></a>    <span class="k">def</span> <span class="nf">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="OpSequence.to_bytes-714"><a href="#OpSequence.to_bytes-714"><span class="linenos">714</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">to_sequence_of_ints</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.from_bytecode_sequence" class="classattr">
                                        <input id="OpSequence.from_bytecode_sequence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@staticmethod</div>

        <span class="def">def</span>
        <span class="name">from_bytecode_sequence</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">code</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]]]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.from_bytecode_sequence-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.from_bytecode_sequence"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.from_bytecode_sequence-716"><a href="#OpSequence.from_bytecode_sequence-716"><span class="linenos">716</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence.from_bytecode_sequence-717"><a href="#OpSequence.from_bytecode_sequence-717"><span class="linenos">717</span></a>    <span class="k">def</span> <span class="nf">from_bytecode_sequence</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">):</span>
</span><span id="OpSequence.from_bytecode_sequence-718"><a href="#OpSequence.from_bytecode_sequence-718"><span class="linenos">718</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="OpSequence.from_bytecode_sequence-719"><a href="#OpSequence.from_bytecode_sequence-719"><span class="linenos">719</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">))),</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.from_entity" class="classattr">
                                        <input id="OpSequence.from_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@staticmethod</div>

        <span class="def">def</span>
        <span class="name">from_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.from_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.from_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.from_entity-721"><a href="#OpSequence.from_entity-721"><span class="linenos">721</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence.from_entity-722"><a href="#OpSequence.from_entity-722"><span class="linenos">722</span></a>    <span class="k">def</span> <span class="nf">from_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="OpSequence.from_entity-723"><a href="#OpSequence.from_entity-723"><span class="linenos">723</span></a>        <span class="n">code_bytes</span><span class="p">:</span> <span class="n">BytecodeSequence</span> <span class="o">=</span> <span class="n">_get_code_object</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="o">.</span><span class="n">co_code</span>
</span><span id="OpSequence.from_entity-724"><a href="#OpSequence.from_entity-724"><span class="linenos">724</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_bytecode_sequence</span><span class="p">(</span><span class="n">code_bytes</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.from_instructions" class="classattr">
                                        <input id="OpSequence.from_instructions-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@staticmethod</div>

        <span class="def">def</span>
        <span class="name">from_instructions</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.from_instructions-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.from_instructions"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.from_instructions-726"><a href="#OpSequence.from_instructions-726"><span class="linenos">726</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence.from_instructions-727"><a href="#OpSequence.from_instructions-727"><span class="linenos">727</span></a>    <span class="k">def</span> <span class="nf">from_instructions</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="OpSequence.from_instructions-728"><a href="#OpSequence.from_instructions-728"><span class="linenos">728</span></a>        <span class="n">op_sequence</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="OpSequence.from_instructions-729"><a href="#OpSequence.from_instructions-729"><span class="linenos">729</span></a>        <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="OpSequence.from_instructions-730"><a href="#OpSequence.from_instructions-730"><span class="linenos">730</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="OpSequence.from_instructions-731"><a href="#OpSequence.from_instructions-731"><span class="linenos">731</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="OpSequence.from_instructions-732"><a href="#OpSequence.from_instructions-732"><span class="linenos">732</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="OpSequence.from_instructions-733"><a href="#OpSequence.from_instructions-733"><span class="linenos">733</span></a>
</span><span id="OpSequence.from_instructions-734"><a href="#OpSequence.from_instructions-734"><span class="linenos">734</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">))</span>
</span><span id="OpSequence.from_instructions-735"><a href="#OpSequence.from_instructions-735"><span class="linenos">735</span></a>
</span><span id="OpSequence.from_instructions-736"><a href="#OpSequence.from_instructions-736"><span class="linenos">736</span></a>        <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">find_ops_with_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)</span>
</span><span id="OpSequence.from_instructions-737"><a href="#OpSequence.from_instructions-737"><span class="linenos">737</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">)))</span>
</span><span id="OpSequence.from_instructions-738"><a href="#OpSequence.from_instructions-738"><span class="linenos">738</span></a>        <span class="n">result</span><span class="o">.</span><span class="n">normalize_instructions_arg</span><span class="p">()</span>
</span><span id="OpSequence.from_instructions-739"><a href="#OpSequence.from_instructions-739"><span class="linenos">739</span></a>        <span class="k">return</span> <span class="n">result</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span></pre></div>


    

                            </div>
                            <div id="OpSequence.from_instructions_fast" class="classattr">
                                        <input id="OpSequence.from_instructions_fast-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@staticmethod</div>

        <span class="def">def</span>
        <span class="name">from_instructions_fast</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="OpSequence.from_instructions_fast-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#OpSequence.from_instructions_fast"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="OpSequence.from_instructions_fast-741"><a href="#OpSequence.from_instructions_fast-741"><span class="linenos">741</span></a>    <span class="nd">@staticmethod</span>
</span><span id="OpSequence.from_instructions_fast-742"><a href="#OpSequence.from_instructions_fast-742"><span class="linenos">742</span></a>    <span class="k">def</span> <span class="nf">from_instructions_fast</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="OpSequence.from_instructions_fast-743"><a href="#OpSequence.from_instructions_fast-743"><span class="linenos">743</span></a>        <span class="k">return</span> <span class="n">OpSequence</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">unpack_opargs</span><span class="p">(</span><span class="n">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">normalize_instructions_arg</span><span class="p">(</span><span class="n">instructions</span><span class="p">)))))</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="arg_to_bytes">
                            <input id="arg_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">arg_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="arg_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#arg_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="arg_to_bytes-746"><a href="#arg_to_bytes-746"><span class="linenos">746</span></a><span class="k">def</span> <span class="nf">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="arg_to_bytes-747"><a href="#arg_to_bytes-747"><span class="linenos">747</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="arg_to_bytes-748"><a href="#arg_to_bytes-748"><span class="linenos">748</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="arg_to_bytes-749"><a href="#arg_to_bytes-749"><span class="linenos">749</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
</span><span id="arg_to_bytes-750"><a href="#arg_to_bytes-750"><span class="linenos">750</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\x00</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="arg_to_bytes-751"><a href="#arg_to_bytes-751"><span class="linenos">751</span></a>            
</span><span id="arg_to_bytes-752"><a href="#arg_to_bytes-752"><span class="linenos">752</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">arg</span><span class="p">:</span>
</span><span id="arg_to_bytes-753"><a href="#arg_to_bytes-753"><span class="linenos">753</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\x00</span><span class="s1">&#39;</span>
</span><span id="arg_to_bytes-754"><a href="#arg_to_bytes-754"><span class="linenos">754</span></a>    
</span><span id="arg_to_bytes-755"><a href="#arg_to_bytes-755"><span class="linenos">755</span></a>    <span class="k">return</span> <span class="n">arg</span>
</span></pre></div>


    

                </section>
                <section id="arg_to_int">
                            <input id="arg_to_int-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">arg_to_int</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="arg_to_int-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#arg_to_int"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="arg_to_int-758"><a href="#arg_to_int-758"><span class="linenos">758</span></a><span class="k">def</span> <span class="nf">arg_to_int</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="arg_to_int-759"><a href="#arg_to_int-759"><span class="linenos">759</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="arg_to_int-760"><a href="#arg_to_int-760"><span class="linenos">760</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="arg_to_int-761"><a href="#arg_to_int-761"><span class="linenos">761</span></a>    
</span><span id="arg_to_int-762"><a href="#arg_to_int-762"><span class="linenos">762</span></a>    <span class="k">return</span> <span class="n">arg</span>
</span></pre></div>


    

                </section>
                <section id="get_raw_instructions">
                            <input id="get_raw_instructions-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_raw_instructions</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">x</span>, </span><span class="param"><span class="o">*</span>, </span><span class="param"><span class="n">first_line</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_raw_instructions-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_raw_instructions"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_raw_instructions-765"><a href="#get_raw_instructions-765"><span class="linenos">765</span></a><span class="k">def</span> <span class="nf">get_raw_instructions</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">first_line</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="get_raw_instructions-766"><a href="#get_raw_instructions-766"><span class="linenos">766</span></a>    <span class="n">readable_instructions</span> <span class="o">=</span> <span class="n">get_instructions</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">first_line</span><span class="p">)</span>
</span><span id="get_raw_instructions-767"><a href="#get_raw_instructions-767"><span class="linenos">767</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">readable_instructions</span><span class="p">:</span>
</span><span id="get_raw_instructions-768"><a href="#get_raw_instructions-768"><span class="linenos">768</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="get_raw_instructions-769"><a href="#get_raw_instructions-769"><span class="linenos">769</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_raw_instructions-770"><a href="#get_raw_instructions-770"><span class="linenos">770</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="get_raw_instructions-771"><a href="#get_raw_instructions-771"><span class="linenos">771</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="get_raw_instructions-772"><a href="#get_raw_instructions-772"><span class="linenos">772</span></a>            
</span><span id="get_raw_instructions-773"><a href="#get_raw_instructions-773"><span class="linenos">773</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="get_raw_instructions-774"><a href="#get_raw_instructions-774"><span class="linenos">774</span></a>
</span><span id="get_raw_instructions-775"><a href="#get_raw_instructions-775"><span class="linenos">775</span></a>        <span class="k">yield</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">instruction</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argval</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argrepr</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">offset</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">starts_line</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">is_jump_target</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="normalize_instructions_arg">
                            <input id="normalize_instructions_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">normalize_instructions_arg</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="normalize_instructions_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#normalize_instructions_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="normalize_instructions_arg-778"><a href="#normalize_instructions_arg-778"><span class="linenos">778</span></a><span class="k">def</span> <span class="nf">normalize_instructions_arg</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="normalize_instructions_arg-779"><a href="#normalize_instructions_arg-779"><span class="linenos">779</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="normalize_instructions_arg-780"><a href="#normalize_instructions_arg-780"><span class="linenos">780</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="normalize_instructions_arg-781"><a href="#normalize_instructions_arg-781"><span class="linenos">781</span></a>        <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="normalize_instructions_arg-782"><a href="#normalize_instructions_arg-782"><span class="linenos">782</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_bytes</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="normalize_instructions_arg-783"><a href="#normalize_instructions_arg-783"><span class="linenos">783</span></a>            <span class="n">extended_arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="normalize_instructions_arg-784"><a href="#normalize_instructions_arg-784"><span class="linenos">784</span></a>            <span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="normalize_instructions_arg-785"><a href="#normalize_instructions_arg-785"><span class="linenos">785</span></a>            <span class="k">for</span> <span class="n">extended_arg_int</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">extended_arg</span><span class="p">):</span>
</span><span id="normalize_instructions_arg-786"><a href="#normalize_instructions_arg-786"><span class="linenos">786</span></a>                <span class="k">yield</span> <span class="n">make_instruction</span><span class="p">(</span><span class="s1">&#39;EXTENDED_ARG&#39;</span><span class="p">,</span> <span class="n">extended_arg_int</span><span class="p">)</span>
</span><span id="normalize_instructions_arg-787"><a href="#normalize_instructions_arg-787"><span class="linenos">787</span></a>
</span><span id="normalize_instructions_arg-788"><a href="#normalize_instructions_arg-788"><span class="linenos">788</span></a>        <span class="k">yield</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">instruction</span><span class="o">.</span><span class="n">opname</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argval</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">argrepr</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">offset</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">starts_line</span><span class="p">,</span> <span class="n">instruction</span><span class="o">.</span><span class="n">is_jump_target</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="instructions_to_sequence_of_ints">
                            <input id="instructions_to_sequence_of_ints-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">instructions_to_sequence_of_ints</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="instructions_to_sequence_of_ints-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#instructions_to_sequence_of_ints"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="instructions_to_sequence_of_ints-791"><a href="#instructions_to_sequence_of_ints-791"><span class="linenos">791</span></a><span class="k">def</span> <span class="nf">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]):</span>
</span><span id="instructions_to_sequence_of_ints-792"><a href="#instructions_to_sequence_of_ints-792"><span class="linenos">792</span></a>    <span class="k">for</span> <span class="n">instruction</span> <span class="ow">in</span> <span class="n">instructions</span><span class="p">:</span>
</span><span id="instructions_to_sequence_of_ints-793"><a href="#instructions_to_sequence_of_ints-793"><span class="linenos">793</span></a>        <span class="n">op</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">opcode</span>
</span><span id="instructions_to_sequence_of_ints-794"><a href="#instructions_to_sequence_of_ints-794"><span class="linenos">794</span></a>        <span class="k">yield</span> <span class="n">op</span>
</span><span id="instructions_to_sequence_of_ints-795"><a href="#instructions_to_sequence_of_ints-795"><span class="linenos">795</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">instruction</span><span class="o">.</span><span class="n">arg</span>
</span><span id="instructions_to_sequence_of_ints-796"><a href="#instructions_to_sequence_of_ints-796"><span class="linenos">796</span></a>        <span class="k">yield</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">arg</span>
</span></pre></div>


    

                </section>
                <section id="instructions_to_bytes">
                            <input id="instructions_to_bytes-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">instructions_to_bytes</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bytes</span>:</span></span>

                <label class="view-source-button" for="instructions_to_bytes-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#instructions_to_bytes"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="instructions_to_bytes-799"><a href="#instructions_to_bytes-799"><span class="linenos">799</span></a><span class="k">def</span> <span class="nf">instructions_to_bytes</span><span class="p">(</span><span class="n">instructions</span><span class="p">:</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Instruction</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
</span><span id="instructions_to_bytes-800"><a href="#instructions_to_bytes-800"><span class="linenos">800</span></a>    <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">instructions_to_sequence_of_ints</span><span class="p">(</span><span class="n">instructions</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="make_instruction">
                            <input id="make_instruction-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">make_instruction</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span><span class="p">:</span> <span class="nb">str</span>, </span><span class="param"><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">NoneType</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span>:</span></span>

                <label class="view-source-button" for="make_instruction-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#make_instruction"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="make_instruction-803"><a href="#make_instruction-803"><span class="linenos">803</span></a><span class="k">def</span> <span class="nf">make_instruction</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Instruction</span><span class="p">:</span>
</span><span id="make_instruction-804"><a href="#make_instruction-804"><span class="linenos">804</span></a>    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</span><span id="make_instruction-805"><a href="#make_instruction-805"><span class="linenos">805</span></a>    <span class="n">op</span> <span class="o">=</span> <span class="n">opmap</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="make_instruction-806"><a href="#make_instruction-806"><span class="linenos">806</span></a>    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="make_instruction-807"><a href="#make_instruction-807"><span class="linenos">807</span></a>    <span class="k">return</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="mi">
                            <input id="mi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">mi</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span><span class="p">:</span> <span class="nb">str</span>, </span><span class="param"><span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">NoneType</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">dis</span><span class="o">.</span><span class="n">Instruction</span>:</span></span>

                <label class="view-source-button" for="mi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#mi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="mi-803"><a href="#mi-803"><span class="linenos">803</span></a><span class="k">def</span> <span class="nf">make_instruction</span><span class="p">(</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">arg</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="kc">None</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Instruction</span><span class="p">:</span>
</span><span id="mi-804"><a href="#mi-804"><span class="linenos">804</span></a>    <span class="n">name</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>
</span><span id="mi-805"><a href="#mi-805"><span class="linenos">805</span></a>    <span class="n">op</span> <span class="o">=</span> <span class="n">opmap</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="mi-806"><a href="#mi-806"><span class="linenos">806</span></a>    <span class="n">arg</span> <span class="o">=</span> <span class="n">arg_to_int</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>
</span><span id="mi-807"><a href="#mi-807"><span class="linenos">807</span></a>    <span class="k">return</span> <span class="n">Instruction</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="fix_labels">
                            <input id="fix_labels-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fix_labels</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">op_sequence</span><span class="p">:</span> <span class="n"><a href="#OpSequence">OpSequence</a></span>,</span><span class="param">	<span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="fix_labels-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#fix_labels"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="fix_labels-813"><a href="#fix_labels-813"><span class="linenos">813</span></a><span class="k">def</span> <span class="nf">fix_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]):</span>
</span><span id="fix_labels-814"><a href="#fix_labels-814"><span class="linenos">814</span></a>    <span class="n">op_sequence</span><span class="o">.</span><span class="n">fix_labels</span><span class="p">({</span><span class="n">arg_to_op_index</span><span class="p">(</span><span class="n">label</span><span class="p">):</span> <span class="p">[</span><span class="n">op_info</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="k">for</span> <span class="n">op_info</span> <span class="ow">in</span> <span class="n">data</span><span class="p">]</span> <span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">data</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="o">.</span><span class="n">items</span><span class="p">()})</span>
</span></pre></div>


    

                </section>
                <section id="code_info">
                            <input id="code_info-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_info</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">x</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="code_info-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_info"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_info-817"><a href="#code_info-817"><span class="linenos">817</span></a><span class="k">def</span> <span class="nf">code_info</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
</span><span id="code_info-818"><a href="#code_info-818"><span class="linenos">818</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Formatted details of methods, functions, or code.&quot;&quot;&quot;</span>
</span><span id="code_info-819"><a href="#code_info-819"><span class="linenos">819</span></a>    <span class="k">return</span> <span class="n">_format_code_info</span><span class="p">(</span><span class="n">_get_code_object</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
</span></pre></div>


            <div class="docstring"><p>Formatted details of methods, functions, or code.</p>
</div>


                </section>
                <section id="modify_code">
                            <input id="modify_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">modify_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">original_code</span><span class="p">:</span> <span class="n">code</span>, </span><span class="param"><span class="n">co_code</span>, </span><span class="param"><span class="n">co_consts</span>, </span><span class="param"><span class="n">co_names</span>, </span><span class="param"><span class="n">co_varnames</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="modify_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#modify_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="modify_code-203"><a href="#modify_code-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="nf">modify_code</span><span class="p">(</span><span class="n">original_code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">,</span> <span class="n">co_code</span><span class="p">,</span> <span class="n">co_consts</span><span class="p">,</span> <span class="n">co_names</span><span class="p">,</span> <span class="n">co_varnames</span><span class="p">):</span>
</span><span id="modify_code-204"><a href="#modify_code-204"><span class="linenos">204</span></a>        <span class="n">co_nlocals</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="modify_code-205"><a href="#modify_code-205"><span class="linenos">205</span></a>        <span class="k">return</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="modify_code-206"><a href="#modify_code-206"><span class="linenos">206</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="modify_code-207"><a href="#modify_code-207"><span class="linenos">207</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_posonlyargcount</span><span class="p">,</span>
</span><span id="modify_code-208"><a href="#modify_code-208"><span class="linenos">208</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="modify_code-209"><a href="#modify_code-209"><span class="linenos">209</span></a>            <span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="modify_code-210"><a href="#modify_code-210"><span class="linenos">210</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="modify_code-211"><a href="#modify_code-211"><span class="linenos">211</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="modify_code-212"><a href="#modify_code-212"><span class="linenos">212</span></a>            <span class="n">co_code</span><span class="p">,</span>
</span><span id="modify_code-213"><a href="#modify_code-213"><span class="linenos">213</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_consts</span><span class="p">),</span>
</span><span id="modify_code-214"><a href="#modify_code-214"><span class="linenos">214</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_names</span><span class="p">),</span>
</span><span id="modify_code-215"><a href="#modify_code-215"><span class="linenos">215</span></a>            <span class="nb">tuple</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">),</span>
</span><span id="modify_code-216"><a href="#modify_code-216"><span class="linenos">216</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="modify_code-217"><a href="#modify_code-217"><span class="linenos">217</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="modify_code-218"><a href="#modify_code-218"><span class="linenos">218</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="modify_code-219"><a href="#modify_code-219"><span class="linenos">219</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="modify_code-220"><a href="#modify_code-220"><span class="linenos">220</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="modify_code-221"><a href="#modify_code-221"><span class="linenos">221</span></a>            <span class="n">original_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="modify_code-222"><a href="#modify_code-222"><span class="linenos">222</span></a>        <span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="unpack_opargs">
                            <input id="unpack_opargs-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unpack_opargs</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]]]</span>,</span><span class="param">	<span class="n">denormalize_values</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="unpack_opargs-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#unpack_opargs"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="unpack_opargs-256"><a href="#unpack_opargs-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="nf">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">,</span> <span class="n">denormalize_values</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="unpack_opargs-257"><a href="#unpack_opargs-257"><span class="linenos">257</span></a>        <span class="n">ftv</span><span class="p">:</span> <span class="n">FrontTriggerableVariable</span> <span class="o">=</span> <span class="n">FrontTriggerableVariable</span><span class="p">(</span><span class="n">FrontTriggerableVariableType</span><span class="o">.</span><span class="n">equal</span><span class="p">,</span> <span class="n">EXTENDED_ARG</span><span class="p">)</span>
</span><span id="unpack_opargs-258"><a href="#unpack_opargs-258"><span class="linenos">258</span></a>        <span class="n">extended_arg</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="unpack_opargs-259"><a href="#unpack_opargs-259"><span class="linenos">259</span></a>        <span class="n">real_op_index</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-260"><a href="#unpack_opargs-260"><span class="linenos">260</span></a>        <span class="n">real_offset</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-261"><a href="#unpack_opargs-261"><span class="linenos">261</span></a>        <span class="n">need_to_clear_real_data</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="unpack_opargs-262"><a href="#unpack_opargs-262"><span class="linenos">262</span></a>
</span><span id="unpack_opargs-263"><a href="#unpack_opargs-263"><span class="linenos">263</span></a>        <span class="n">op</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-264"><a href="#unpack_opargs-264"><span class="linenos">264</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-265"><a href="#unpack_opargs-265"><span class="linenos">265</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="unpack_opargs-266"><a href="#unpack_opargs-266"><span class="linenos">266</span></a>        <span class="n">op_index</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="unpack_opargs-267"><a href="#unpack_opargs-267"><span class="linenos">267</span></a>        <span class="n">i</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
</span><span id="unpack_opargs-268"><a href="#unpack_opargs-268"><span class="linenos">268</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">code</span><span class="p">:</span>
</span><span id="unpack_opargs-269"><a href="#unpack_opargs-269"><span class="linenos">269</span></a>            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="unpack_opargs-270"><a href="#unpack_opargs-270"><span class="linenos">270</span></a>                <span class="n">item</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">byteorder</span><span class="o">=</span><span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="unpack_opargs-271"><a href="#unpack_opargs-271"><span class="linenos">271</span></a>            
</span><span id="unpack_opargs-272"><a href="#unpack_opargs-272"><span class="linenos">272</span></a>            <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="unpack_opargs-273"><a href="#unpack_opargs-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">i</span> <span class="o">%</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="unpack_opargs-274"><a href="#unpack_opargs-274"><span class="linenos">274</span></a>                <span class="n">op</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="unpack_opargs-275"><a href="#unpack_opargs-275"><span class="linenos">275</span></a>                <span class="n">op_index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="unpack_opargs-276"><a href="#unpack_opargs-276"><span class="linenos">276</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">i</span>
</span><span id="unpack_opargs-277"><a href="#unpack_opargs-277"><span class="linenos">277</span></a>                <span class="k">continue</span>
</span><span id="unpack_opargs-278"><a href="#unpack_opargs-278"><span class="linenos">278</span></a>            
</span><span id="unpack_opargs-279"><a href="#unpack_opargs-279"><span class="linenos">279</span></a>            <span class="k">if</span> <span class="n">op</span> <span class="o">&gt;=</span> <span class="n">HAVE_ARGUMENT</span><span class="p">:</span>
</span><span id="unpack_opargs-280"><a href="#unpack_opargs-280"><span class="linenos">280</span></a>                <span class="n">ftv_result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ftv</span><span class="p">(</span><span class="n">op</span><span class="p">)</span>
</span><span id="unpack_opargs-281"><a href="#unpack_opargs-281"><span class="linenos">281</span></a>                <span class="k">if</span> <span class="n">ftv_result</span> <span class="ow">is</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="unpack_opargs-282"><a href="#unpack_opargs-282"><span class="linenos">282</span></a>                    <span class="n">real_op_index</span> <span class="o">=</span> <span class="n">op_index</span>
</span><span id="unpack_opargs-283"><a href="#unpack_opargs-283"><span class="linenos">283</span></a>                    <span class="n">real_offset</span> <span class="o">=</span> <span class="n">offset</span>
</span><span id="unpack_opargs-284"><a href="#unpack_opargs-284"><span class="linenos">284</span></a>                <span class="k">elif</span> <span class="n">ftv_result</span> <span class="ow">is</span> <span class="kc">False</span><span class="p">:</span>
</span><span id="unpack_opargs-285"><a href="#unpack_opargs-285"><span class="linenos">285</span></a>                    <span class="n">need_to_clear_real_data</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="unpack_opargs-286"><a href="#unpack_opargs-286"><span class="linenos">286</span></a>
</span><span id="unpack_opargs-287"><a href="#unpack_opargs-287"><span class="linenos">287</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="n">item</span> <span class="o">|</span> <span class="n">extended_arg</span>
</span><span id="unpack_opargs-288"><a href="#unpack_opargs-288"><span class="linenos">288</span></a>                <span class="k">if</span> <span class="n">denormalize_values</span><span class="p">:</span>
</span><span id="unpack_opargs-289"><a href="#unpack_opargs-289"><span class="linenos">289</span></a>                    <span class="n">extended_arg</span> <span class="o">=</span> <span class="p">(</span><span class="n">arg</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="k">if</span> <span class="n">op</span> <span class="o">==</span> <span class="n">EXTENDED_ARG</span> <span class="k">else</span> <span class="mi">0</span>
</span><span id="unpack_opargs-290"><a href="#unpack_opargs-290"><span class="linenos">290</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="unpack_opargs-291"><a href="#unpack_opargs-291"><span class="linenos">291</span></a>                <span class="n">arg</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-292"><a href="#unpack_opargs-292"><span class="linenos">292</span></a>            
</span><span id="unpack_opargs-293"><a href="#unpack_opargs-293"><span class="linenos">293</span></a>            <span class="k">yield</span> <span class="p">(</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span><span class="p">)</span>
</span><span id="unpack_opargs-294"><a href="#unpack_opargs-294"><span class="linenos">294</span></a>            <span class="k">if</span> <span class="n">need_to_clear_real_data</span><span class="p">:</span>
</span><span id="unpack_opargs-295"><a href="#unpack_opargs-295"><span class="linenos">295</span></a>                <span class="n">real_op_index</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-296"><a href="#unpack_opargs-296"><span class="linenos">296</span></a>                <span class="n">real_offset</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="unpack_opargs-297"><a href="#unpack_opargs-297"><span class="linenos">297</span></a>                <span class="n">need_to_clear_real_data</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="find_ops_with_labels">
                            <input id="find_ops_with_labels-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_ops_with_labels</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">]]]</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]]</span>:</span></span>

                <label class="view-source-button" for="find_ops_with_labels-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_ops_with_labels"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_ops_with_labels-299"><a href="#find_ops_with_labels-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">find_ops_with_labels</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">BytecodeSequence</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">],</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]]:</span>
</span><span id="find_ops_with_labels-300"><a href="#find_ops_with_labels-300"><span class="linenos">300</span></a>        <span class="n">labels</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_ops_with_labels-301"><a href="#find_ops_with_labels-301"><span class="linenos">301</span></a>        <span class="n">op_by_label</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">,</span> <span class="nb">int</span><span class="p">]]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="find_ops_with_labels-302"><a href="#find_ops_with_labels-302"><span class="linenos">302</span></a>        <span class="k">for</span> <span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span> <span class="ow">in</span> <span class="n">unpack_opargs</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="find_ops_with_labels-303"><a href="#find_ops_with_labels-303"><span class="linenos">303</span></a>            <span class="k">if</span> <span class="n">arg</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_ops_with_labels-304"><a href="#find_ops_with_labels-304"><span class="linenos">304</span></a>                <span class="k">if</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjrel</span><span class="p">:</span>
</span><span id="find_ops_with_labels-305"><a href="#find_ops_with_labels-305"><span class="linenos">305</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">offset</span> <span class="o">+</span> <span class="mi">2</span> <span class="o">+</span> <span class="n">arg</span>
</span><span id="find_ops_with_labels-306"><a href="#find_ops_with_labels-306"><span class="linenos">306</span></a>                <span class="k">elif</span> <span class="n">op</span> <span class="ow">in</span> <span class="n">hasjabs</span><span class="p">:</span>
</span><span id="find_ops_with_labels-307"><a href="#find_ops_with_labels-307"><span class="linenos">307</span></a>                    <span class="n">label</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="find_ops_with_labels-308"><a href="#find_ops_with_labels-308"><span class="linenos">308</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="find_ops_with_labels-309"><a href="#find_ops_with_labels-309"><span class="linenos">309</span></a>                    <span class="k">continue</span>
</span><span id="find_ops_with_labels-310"><a href="#find_ops_with_labels-310"><span class="linenos">310</span></a>
</span><span id="find_ops_with_labels-311"><a href="#find_ops_with_labels-311"><span class="linenos">311</span></a>                <span class="k">if</span> <span class="n">label</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">op_by_label</span><span class="p">:</span>
</span><span id="find_ops_with_labels-312"><a href="#find_ops_with_labels-312"><span class="linenos">312</span></a>                    <span class="n">labels</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">label</span><span class="p">)</span>
</span><span id="find_ops_with_labels-313"><a href="#find_ops_with_labels-313"><span class="linenos">313</span></a>                    <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_ops_with_labels-314"><a href="#find_ops_with_labels-314"><span class="linenos">314</span></a>                
</span><span id="find_ops_with_labels-315"><a href="#find_ops_with_labels-315"><span class="linenos">315</span></a>                <span class="n">op_by_label</span><span class="p">[</span><span class="n">label</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">op</span><span class="p">,</span> <span class="n">arg</span><span class="p">,</span> <span class="n">op_index</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">real_op_index</span><span class="p">,</span> <span class="n">real_offset</span><span class="p">))</span>
</span><span id="find_ops_with_labels-316"><a href="#find_ops_with_labels-316"><span class="linenos">316</span></a>
</span><span id="find_ops_with_labels-317"><a href="#find_ops_with_labels-317"><span class="linenos">317</span></a>        <span class="k">return</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span>
</span></pre></div>


    

                </section>
                <section id="op_index_to_arg">
                            <input id="op_index_to_arg-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">op_index_to_arg</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="op_index_to_arg-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#op_index_to_arg"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="op_index_to_arg-320"><a href="#op_index_to_arg-320"><span class="linenos">320</span></a>    <span class="k">def</span> <span class="nf">op_index_to_arg</span><span class="p">(</span><span class="n">op_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="op_index_to_arg-321"><a href="#op_index_to_arg-321"><span class="linenos">321</span></a>        <span class="k">return</span> <span class="n">op_index</span> <span class="o">*</span> <span class="mi">2</span>
</span></pre></div>


    

                </section>
                <section id="arg_to_op_index">
                            <input id="arg_to_op_index-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">arg_to_op_index</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">arg</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="arg_to_op_index-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#arg_to_op_index"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="arg_to_op_index-324"><a href="#arg_to_op_index-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">arg_to_op_index</span><span class="p">(</span><span class="n">arg</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="arg_to_op_index-325"><a href="#arg_to_op_index-325"><span class="linenos">325</span></a>        <span class="k">return</span> <span class="n">arg</span> <span class="o">//</span> <span class="mi">2</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>