---
title: bytecode_patcher
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.coro_standard_services<wbr>.loop_yield<wbr>.versions<wbr>.v_0<wbr>.bytecode_patcher    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-bytecode_patcher-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-bytecode_patcher-view-source"><span>View Source</span></label>

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
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">List</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">CodeType</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.python_bytecode_manipulator</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">is_async</span><span class="p">,</span> <span class="n">is_callable</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="k">def</span> <span class="nf">gly_patch</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeType</span><span class="p">:</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>    <span class="c1"># TODO: try to complise strings using _get_code_object() instead of get_code()</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="n">entity_code_type</span><span class="p">:</span> <span class="n">CodeTypeEnum</span> <span class="o">=</span> <span class="n">code_type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="k">if</span> <span class="n">entity_code_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Entity </span><span class="si">{entity}</span><span class="s1"> cann not be patched&#39;</span><span class="p">)</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="n">op_sequence</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_bytecode_sequence</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_code</span><span class="p">)</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="n">op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">op_sequence</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="n">co_consts</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_consts</span><span class="p">)</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="n">first_new_const_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_consts</span><span class="p">)</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="n">co_names</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_names</span><span class="p">)</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="n">first_new_name_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_names</span><span class="p">)</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="n">co_varnames</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>    <span class="n">first_new_varname_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="n">co_nlocals</span> <span class="o">=</span> <span class="n">fn_code</span><span class="o">.</span><span class="n">co_nlocals</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>    <span class="n">co_consts</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="mi">0</span><span class="p">,</span> <span class="p">(</span><span class="s1">&#39;gly&#39;</span><span class="p">,)))</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>    <span class="n">co_names</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="s1">&#39;cengal.parallel_execution.coroutines.coro_standard_services.loop_yield&#39;</span><span class="p">,</span> <span class="s1">&#39;gly&#39;</span><span class="p">))</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="n">co_varnames</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="s1">&#39;gly&#39;</span><span class="p">,</span> <span class="s1">&#39;ly&#39;</span><span class="p">))</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="n">co_nlocals</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>    <span class="n">initialization</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_CONST&#39;</span><span class="p">,</span> <span class="n">first_new_const_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_CONST&#39;</span><span class="p">,</span> <span class="n">first_new_const_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;IMPORT_NAME&#39;</span><span class="p">,</span> <span class="n">first_new_name_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;IMPORT_FROM&#39;</span><span class="p">,</span> <span class="n">first_new_name_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;STORE_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;POP_TOP&#39;</span><span class="p">),</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;CALL_FUNCTION&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;STORE_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="p">]</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="n">initialization_op_sequence</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="n">initialization_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">initialization_op_sequence</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="n">ly_call</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;CALL_FUNCTION&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;POP_TOP&#39;</span><span class="p">),</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="p">]</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    <span class="n">ly_call_op_sequence</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions</span><span class="p">(</span><span class="n">ly_call</span><span class="p">)</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="n">ly_call_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">ly_call_op_sequence</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">initialization_op_sequence</span><span class="p">)</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="c1"># for</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="n">FOR_ITER</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;FOR_ITER&#39;</span><span class="p">)</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>    <span class="n">index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>        <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>            <span class="k">break</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="n">op</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="k">if</span> <span class="n">FOR_ITER</span> <span class="o">==</span> <span class="n">op</span><span class="p">:</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>            <span class="n">place_to_insert</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">2</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">place_to_insert</span><span class="p">,</span> <span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="n">JUMP_ABSOLUTE</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;JUMP_ABSOLUTE&#39;</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>    <span class="n">index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>            <span class="k">break</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>        <span class="n">op</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">get_arg</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="k">if</span> <span class="n">JUMP_ABSOLUTE</span> <span class="o">==</span> <span class="n">op</span><span class="p">:</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>            <span class="n">place_to_insert</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">arg_to_op_index</span><span class="p">(</span><span class="n">arg</span><span class="p">)]</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="n">place_to_insert_op</span><span class="p">,</span> <span class="n">place_to_insert_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place_to_insert</span><span class="p">]</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>            <span class="k">if</span> <span class="n">FOR_ITER</span> <span class="o">==</span> <span class="n">place_to_insert_op</span><span class="p">:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>                <span class="k">continue</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="n">fix_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="n">new_code_type</span> <span class="o">=</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_posonlyargcount</span><span class="p">,</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="n">op_sequence</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(),</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_consts</span><span class="p">),</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_names</span><span class="p">),</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">),</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="p">)</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    <span class="n">set_code</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">new_code_type</span><span class="p">)</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="k">return</span> <span class="n">fn_code</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="k">def</span> <span class="nf">agly_patch</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="c1"># TODO: try to complise strings using _get_code_object() instead of get_code()</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="n">entity_code_type</span><span class="p">:</span> <span class="n">CodeTypeEnum</span> <span class="o">=</span> <span class="n">code_type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="k">if</span> <span class="n">entity_code_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span> <span class="s1">&#39;Entity </span><span class="si">{entity}</span><span class="s1"> cann not be patched&#39;</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>    <span class="k">return</span> <span class="n">fn_code</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a><span class="k">def</span> <span class="nf">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="sd">        @gly_patched</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="sd">        def func():</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">            for i in range(200):</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">                print(i)</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a><span class="sd">                for j in range(100):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="sd">                    print(j)</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="sd">            </span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">            i = 100</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="sd">                print(i)</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a><span class="sd">                i -= 1</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">    Is equivalent to:</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">        def func():</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="sd">            ly = gly()</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a><span class="sd">            for i in range(200):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a><span class="sd">                print(i)</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a><span class="sd">                for j in range(100):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a><span class="sd">                    print(j)</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a><span class="sd">                    ly()</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a><span class="sd">                </span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a><span class="sd">                ly()</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="sd">            </span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="sd">            i = 100</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">                print(i)</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">                i -= 1</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">                ly()</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">    Args:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">        func (Callable): _description_</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a><span class="sd">    Returns:</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">        Callable: _description_</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>    <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">return</span> <span class="n">func</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a><span class="n">glyp</span> <span class="o">=</span> <span class="n">gly_patched</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="n">gp</span> <span class="o">=</span> <span class="n">gly_patched</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="k">def</span> <span class="nf">agly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>    <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>    <span class="k">return</span> <span class="n">func</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="n">aglyp</span> <span class="o">=</span> <span class="n">agly_patched</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="n">agp</span> <span class="o">=</span> <span class="n">agly_patched</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a><span class="k">class</span> <span class="nc">GlyPatchManagerError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    <span class="k">pass</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a><span class="k">class</span> <span class="nc">GlyPatchManager</span><span class="p">:</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>    <span class="n">patched_functions</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="n">call_tree</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="n">func</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">:</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="k">if</span> <span class="n">tree</span><span class="p">:</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>                    <span class="n">agly_patched_tree</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="k">elif</span> <span class="n">is_callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>                    <span class="n">gly_patched_tree</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>                    <span class="k">raise</span> <span class="n">GlyPatchManagerError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Entity </span><span class="si">{</span><span class="n">func</span><span class="si">}</span><span class="s1"> can not be patched: it must be a callable (either async or not)&#39;</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>                    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                <span class="k">elif</span> <span class="n">is_callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                    <span class="k">raise</span> <span class="n">GlyPatchManagerError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Entity </span><span class="si">{</span><span class="n">func</span><span class="si">}</span><span class="s1"> can not be patched: it must be a callable (either async or not)&#39;</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">[</span><span class="n">func</span><span class="p">]</span> <span class="o">=</span> <span class="n">fn_code</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">return</span> <span class="n">func</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>    <span class="k">def</span> <span class="nf">restore</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="k">if</span> <span class="n">func</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="k">if</span> <span class="n">tree</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_unpatch_tree</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>                <span class="n">set_code</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">[</span><span class="n">func</span><span class="p">])</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>        <span class="k">return</span> <span class="n">func</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">_unpatch_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a><span class="k">def</span> <span class="nf">gly_patched_tree</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GlyPatchManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a><span class="k">def</span> <span class="nf">agly_patched_tree</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GlyPatchManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            </section>
                <section id="gly_patch">
                            <input id="gly_patch-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly_patch</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">code</span>:</span></span>

                <label class="view-source-button" for="gly_patch-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gly_patch"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gly_patch-44"><a href="#gly_patch-44"><span class="linenos"> 44</span></a><span class="k">def</span> <span class="nf">gly_patch</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeType</span><span class="p">:</span>
</span><span id="gly_patch-45"><a href="#gly_patch-45"><span class="linenos"> 45</span></a>    <span class="c1"># TODO: try to complise strings using _get_code_object() instead of get_code()</span>
</span><span id="gly_patch-46"><a href="#gly_patch-46"><span class="linenos"> 46</span></a>    <span class="n">entity_code_type</span><span class="p">:</span> <span class="n">CodeTypeEnum</span> <span class="o">=</span> <span class="n">code_type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="gly_patch-47"><a href="#gly_patch-47"><span class="linenos"> 47</span></a>    <span class="k">if</span> <span class="n">entity_code_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="gly_patch-48"><a href="#gly_patch-48"><span class="linenos"> 48</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;Entity </span><span class="si">{entity}</span><span class="s1"> cann not be patched&#39;</span><span class="p">)</span>
</span><span id="gly_patch-49"><a href="#gly_patch-49"><span class="linenos"> 49</span></a>    
</span><span id="gly_patch-50"><a href="#gly_patch-50"><span class="linenos"> 50</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="gly_patch-51"><a href="#gly_patch-51"><span class="linenos"> 51</span></a>    <span class="n">op_sequence</span><span class="p">,</span> <span class="n">labels</span><span class="p">,</span> <span class="n">op_by_label</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_bytecode_sequence</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_code</span><span class="p">)</span>
</span><span id="gly_patch-52"><a href="#gly_patch-52"><span class="linenos"> 52</span></a>    <span class="n">op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">op_sequence</span>
</span><span id="gly_patch-53"><a href="#gly_patch-53"><span class="linenos"> 53</span></a>    <span class="n">co_consts</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_consts</span><span class="p">)</span>
</span><span id="gly_patch-54"><a href="#gly_patch-54"><span class="linenos"> 54</span></a>    <span class="n">first_new_const_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_consts</span><span class="p">)</span>
</span><span id="gly_patch-55"><a href="#gly_patch-55"><span class="linenos"> 55</span></a>    <span class="n">co_names</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_names</span><span class="p">)</span>
</span><span id="gly_patch-56"><a href="#gly_patch-56"><span class="linenos"> 56</span></a>    <span class="n">first_new_name_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_names</span><span class="p">)</span>
</span><span id="gly_patch-57"><a href="#gly_patch-57"><span class="linenos"> 57</span></a>    <span class="n">co_varnames</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">fn_code</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="gly_patch-58"><a href="#gly_patch-58"><span class="linenos"> 58</span></a>    <span class="n">first_new_varname_index</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="gly_patch-59"><a href="#gly_patch-59"><span class="linenos"> 59</span></a>    <span class="n">co_nlocals</span> <span class="o">=</span> <span class="n">fn_code</span><span class="o">.</span><span class="n">co_nlocals</span>
</span><span id="gly_patch-60"><a href="#gly_patch-60"><span class="linenos"> 60</span></a>
</span><span id="gly_patch-61"><a href="#gly_patch-61"><span class="linenos"> 61</span></a>
</span><span id="gly_patch-62"><a href="#gly_patch-62"><span class="linenos"> 62</span></a>    <span class="n">co_consts</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="mi">0</span><span class="p">,</span> <span class="p">(</span><span class="s1">&#39;gly&#39;</span><span class="p">,)))</span>
</span><span id="gly_patch-63"><a href="#gly_patch-63"><span class="linenos"> 63</span></a>    <span class="n">co_names</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="s1">&#39;cengal.parallel_execution.coroutines.coro_standard_services.loop_yield&#39;</span><span class="p">,</span> <span class="s1">&#39;gly&#39;</span><span class="p">))</span>
</span><span id="gly_patch-64"><a href="#gly_patch-64"><span class="linenos"> 64</span></a>    <span class="n">co_varnames</span><span class="o">.</span><span class="n">extend</span><span class="p">((</span><span class="s1">&#39;gly&#39;</span><span class="p">,</span> <span class="s1">&#39;ly&#39;</span><span class="p">))</span>
</span><span id="gly_patch-65"><a href="#gly_patch-65"><span class="linenos"> 65</span></a>    <span class="n">co_nlocals</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">)</span>
</span><span id="gly_patch-66"><a href="#gly_patch-66"><span class="linenos"> 66</span></a>
</span><span id="gly_patch-67"><a href="#gly_patch-67"><span class="linenos"> 67</span></a>    <span class="n">initialization</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="gly_patch-68"><a href="#gly_patch-68"><span class="linenos"> 68</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_CONST&#39;</span><span class="p">,</span> <span class="n">first_new_const_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-69"><a href="#gly_patch-69"><span class="linenos"> 69</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_CONST&#39;</span><span class="p">,</span> <span class="n">first_new_const_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="gly_patch-70"><a href="#gly_patch-70"><span class="linenos"> 70</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;IMPORT_NAME&#39;</span><span class="p">,</span> <span class="n">first_new_name_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-71"><a href="#gly_patch-71"><span class="linenos"> 71</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;IMPORT_FROM&#39;</span><span class="p">,</span> <span class="n">first_new_name_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="gly_patch-72"><a href="#gly_patch-72"><span class="linenos"> 72</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;STORE_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-73"><a href="#gly_patch-73"><span class="linenos"> 73</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;POP_TOP&#39;</span><span class="p">),</span>
</span><span id="gly_patch-74"><a href="#gly_patch-74"><span class="linenos"> 74</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-75"><a href="#gly_patch-75"><span class="linenos"> 75</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;CALL_FUNCTION&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-76"><a href="#gly_patch-76"><span class="linenos"> 76</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;STORE_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="gly_patch-77"><a href="#gly_patch-77"><span class="linenos"> 77</span></a>    <span class="p">]</span>
</span><span id="gly_patch-78"><a href="#gly_patch-78"><span class="linenos"> 78</span></a>    <span class="n">initialization_op_sequence</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span>
</span><span id="gly_patch-79"><a href="#gly_patch-79"><span class="linenos"> 79</span></a>    <span class="n">initialization_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">initialization_op_sequence</span>
</span><span id="gly_patch-80"><a href="#gly_patch-80"><span class="linenos"> 80</span></a>
</span><span id="gly_patch-81"><a href="#gly_patch-81"><span class="linenos"> 81</span></a>    <span class="n">ly_call</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Instruction</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="gly_patch-82"><a href="#gly_patch-82"><span class="linenos"> 82</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;LOAD_FAST&#39;</span><span class="p">,</span> <span class="n">first_new_varname_index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span>
</span><span id="gly_patch-83"><a href="#gly_patch-83"><span class="linenos"> 83</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;CALL_FUNCTION&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
</span><span id="gly_patch-84"><a href="#gly_patch-84"><span class="linenos"> 84</span></a>        <span class="n">mi</span><span class="p">(</span><span class="s1">&#39;POP_TOP&#39;</span><span class="p">),</span>
</span><span id="gly_patch-85"><a href="#gly_patch-85"><span class="linenos"> 85</span></a>    <span class="p">]</span>
</span><span id="gly_patch-86"><a href="#gly_patch-86"><span class="linenos"> 86</span></a>    <span class="n">ly_call_op_sequence</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">OpSequence</span><span class="o">.</span><span class="n">from_instructions</span><span class="p">(</span><span class="n">ly_call</span><span class="p">)</span>
</span><span id="gly_patch-87"><a href="#gly_patch-87"><span class="linenos"> 87</span></a>    <span class="n">ly_call_op_sequence</span><span class="p">:</span> <span class="n">OpSequence</span> <span class="o">=</span> <span class="n">ly_call_op_sequence</span>
</span><span id="gly_patch-88"><a href="#gly_patch-88"><span class="linenos"> 88</span></a>
</span><span id="gly_patch-89"><a href="#gly_patch-89"><span class="linenos"> 89</span></a>    <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">initialization_op_sequence</span><span class="p">)</span>
</span><span id="gly_patch-90"><a href="#gly_patch-90"><span class="linenos"> 90</span></a>
</span><span id="gly_patch-91"><a href="#gly_patch-91"><span class="linenos"> 91</span></a>    <span class="c1"># for</span>
</span><span id="gly_patch-92"><a href="#gly_patch-92"><span class="linenos"> 92</span></a>    <span class="n">FOR_ITER</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;FOR_ITER&#39;</span><span class="p">)</span>
</span><span id="gly_patch-93"><a href="#gly_patch-93"><span class="linenos"> 93</span></a>
</span><span id="gly_patch-94"><a href="#gly_patch-94"><span class="linenos"> 94</span></a>    <span class="n">index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="gly_patch-95"><a href="#gly_patch-95"><span class="linenos"> 95</span></a>    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="gly_patch-96"><a href="#gly_patch-96"><span class="linenos"> 96</span></a>        <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="gly_patch-97"><a href="#gly_patch-97"><span class="linenos"> 97</span></a>        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="gly_patch-98"><a href="#gly_patch-98"><span class="linenos"> 98</span></a>            <span class="k">break</span>
</span><span id="gly_patch-99"><a href="#gly_patch-99"><span class="linenos"> 99</span></a>
</span><span id="gly_patch-100"><a href="#gly_patch-100"><span class="linenos">100</span></a>        <span class="n">op</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="gly_patch-101"><a href="#gly_patch-101"><span class="linenos">101</span></a>        <span class="k">if</span> <span class="n">FOR_ITER</span> <span class="o">==</span> <span class="n">op</span><span class="p">:</span>
</span><span id="gly_patch-102"><a href="#gly_patch-102"><span class="linenos">102</span></a>            <span class="n">place_to_insert</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">2</span>
</span><span id="gly_patch-103"><a href="#gly_patch-103"><span class="linenos">103</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">place_to_insert</span><span class="p">,</span> <span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="gly_patch-104"><a href="#gly_patch-104"><span class="linenos">104</span></a>
</span><span id="gly_patch-105"><a href="#gly_patch-105"><span class="linenos">105</span></a>    <span class="n">JUMP_ABSOLUTE</span> <span class="o">=</span> <span class="n">opcode</span><span class="p">(</span><span class="s1">&#39;JUMP_ABSOLUTE&#39;</span><span class="p">)</span>
</span><span id="gly_patch-106"><a href="#gly_patch-106"><span class="linenos">106</span></a>
</span><span id="gly_patch-107"><a href="#gly_patch-107"><span class="linenos">107</span></a>    <span class="n">index</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">initialization</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
</span><span id="gly_patch-108"><a href="#gly_patch-108"><span class="linenos">108</span></a>    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="gly_patch-109"><a href="#gly_patch-109"><span class="linenos">109</span></a>        <span class="n">index</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="gly_patch-110"><a href="#gly_patch-110"><span class="linenos">110</span></a>        <span class="k">if</span> <span class="n">index</span> <span class="o">&gt;=</span> <span class="nb">len</span><span class="p">(</span><span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">):</span>
</span><span id="gly_patch-111"><a href="#gly_patch-111"><span class="linenos">111</span></a>            <span class="k">break</span>
</span><span id="gly_patch-112"><a href="#gly_patch-112"><span class="linenos">112</span></a>
</span><span id="gly_patch-113"><a href="#gly_patch-113"><span class="linenos">113</span></a>        <span class="n">op</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
</span><span id="gly_patch-114"><a href="#gly_patch-114"><span class="linenos">114</span></a>        <span class="n">arg</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">get_arg</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
</span><span id="gly_patch-115"><a href="#gly_patch-115"><span class="linenos">115</span></a>        <span class="k">if</span> <span class="n">JUMP_ABSOLUTE</span> <span class="o">==</span> <span class="n">op</span><span class="p">:</span>
</span><span id="gly_patch-116"><a href="#gly_patch-116"><span class="linenos">116</span></a>            <span class="n">place_to_insert</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence_offset_map</span><span class="o">.</span><span class="n">new_by_original</span><span class="p">[</span><span class="n">arg_to_op_index</span><span class="p">(</span><span class="n">arg</span><span class="p">)]</span>
</span><span id="gly_patch-117"><a href="#gly_patch-117"><span class="linenos">117</span></a>            <span class="n">place_to_insert_op</span><span class="p">,</span> <span class="n">place_to_insert_arg</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">op_sequence</span><span class="o">.</span><span class="n">op_sequence</span><span class="p">[</span><span class="n">place_to_insert</span><span class="p">]</span>
</span><span id="gly_patch-118"><a href="#gly_patch-118"><span class="linenos">118</span></a>            <span class="k">if</span> <span class="n">FOR_ITER</span> <span class="o">==</span> <span class="n">place_to_insert_op</span><span class="p">:</span>
</span><span id="gly_patch-119"><a href="#gly_patch-119"><span class="linenos">119</span></a>                <span class="k">continue</span>
</span><span id="gly_patch-120"><a href="#gly_patch-120"><span class="linenos">120</span></a>
</span><span id="gly_patch-121"><a href="#gly_patch-121"><span class="linenos">121</span></a>            <span class="n">op_sequence</span><span class="o">.</span><span class="n">insert_op_sequence</span><span class="p">(</span><span class="n">index</span><span class="p">,</span> <span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="gly_patch-122"><a href="#gly_patch-122"><span class="linenos">122</span></a>            <span class="n">index</span> <span class="o">+=</span> <span class="nb">len</span><span class="p">(</span><span class="n">ly_call_op_sequence</span><span class="p">)</span>
</span><span id="gly_patch-123"><a href="#gly_patch-123"><span class="linenos">123</span></a>    
</span><span id="gly_patch-124"><a href="#gly_patch-124"><span class="linenos">124</span></a>    <span class="n">fix_labels</span><span class="p">(</span><span class="n">op_sequence</span><span class="p">,</span> <span class="n">op_by_label</span><span class="p">)</span>
</span><span id="gly_patch-125"><a href="#gly_patch-125"><span class="linenos">125</span></a>
</span><span id="gly_patch-126"><a href="#gly_patch-126"><span class="linenos">126</span></a>    <span class="n">new_code_type</span> <span class="o">=</span> <span class="n">CodeType</span><span class="p">(</span>
</span><span id="gly_patch-127"><a href="#gly_patch-127"><span class="linenos">127</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_argcount</span><span class="p">,</span>
</span><span id="gly_patch-128"><a href="#gly_patch-128"><span class="linenos">128</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_posonlyargcount</span><span class="p">,</span>
</span><span id="gly_patch-129"><a href="#gly_patch-129"><span class="linenos">129</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_kwonlyargcount</span><span class="p">,</span>
</span><span id="gly_patch-130"><a href="#gly_patch-130"><span class="linenos">130</span></a>        <span class="n">co_nlocals</span><span class="p">,</span>
</span><span id="gly_patch-131"><a href="#gly_patch-131"><span class="linenos">131</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_stacksize</span><span class="p">,</span>
</span><span id="gly_patch-132"><a href="#gly_patch-132"><span class="linenos">132</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_flags</span><span class="p">,</span>
</span><span id="gly_patch-133"><a href="#gly_patch-133"><span class="linenos">133</span></a>        <span class="n">op_sequence</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(),</span>
</span><span id="gly_patch-134"><a href="#gly_patch-134"><span class="linenos">134</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_consts</span><span class="p">),</span>
</span><span id="gly_patch-135"><a href="#gly_patch-135"><span class="linenos">135</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_names</span><span class="p">),</span>
</span><span id="gly_patch-136"><a href="#gly_patch-136"><span class="linenos">136</span></a>        <span class="nb">tuple</span><span class="p">(</span><span class="n">co_varnames</span><span class="p">),</span>
</span><span id="gly_patch-137"><a href="#gly_patch-137"><span class="linenos">137</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">,</span>
</span><span id="gly_patch-138"><a href="#gly_patch-138"><span class="linenos">138</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">,</span>
</span><span id="gly_patch-139"><a href="#gly_patch-139"><span class="linenos">139</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="p">,</span>
</span><span id="gly_patch-140"><a href="#gly_patch-140"><span class="linenos">140</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_lnotab</span><span class="p">,</span>
</span><span id="gly_patch-141"><a href="#gly_patch-141"><span class="linenos">141</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_freevars</span><span class="p">,</span>
</span><span id="gly_patch-142"><a href="#gly_patch-142"><span class="linenos">142</span></a>        <span class="n">fn_code</span><span class="o">.</span><span class="n">co_cellvars</span><span class="p">,</span>
</span><span id="gly_patch-143"><a href="#gly_patch-143"><span class="linenos">143</span></a>    <span class="p">)</span>
</span><span id="gly_patch-144"><a href="#gly_patch-144"><span class="linenos">144</span></a>    <span class="n">set_code</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">new_code_type</span><span class="p">)</span>
</span><span id="gly_patch-145"><a href="#gly_patch-145"><span class="linenos">145</span></a>    <span class="k">return</span> <span class="n">fn_code</span>
</span></pre></div>


    

                </section>
                <section id="agly_patch">
                            <input id="agly_patch-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agly_patch</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="agly_patch-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agly_patch"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agly_patch-148"><a href="#agly_patch-148"><span class="linenos">148</span></a><span class="k">def</span> <span class="nf">agly_patch</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="agly_patch-149"><a href="#agly_patch-149"><span class="linenos">149</span></a>    <span class="c1"># TODO: try to complise strings using _get_code_object() instead of get_code()</span>
</span><span id="agly_patch-150"><a href="#agly_patch-150"><span class="linenos">150</span></a>    <span class="n">entity_code_type</span><span class="p">:</span> <span class="n">CodeTypeEnum</span> <span class="o">=</span> <span class="n">code_type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="agly_patch-151"><a href="#agly_patch-151"><span class="linenos">151</span></a>    <span class="k">if</span> <span class="n">entity_code_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="agly_patch-152"><a href="#agly_patch-152"><span class="linenos">152</span></a>        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span> <span class="s1">&#39;Entity </span><span class="si">{entity}</span><span class="s1"> cann not be patched&#39;</span><span class="p">)</span>
</span><span id="agly_patch-153"><a href="#agly_patch-153"><span class="linenos">153</span></a>    
</span><span id="agly_patch-154"><a href="#agly_patch-154"><span class="linenos">154</span></a>    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="agly_patch-155"><a href="#agly_patch-155"><span class="linenos">155</span></a>    <span class="k">return</span> <span class="n">fn_code</span>
</span></pre></div>


    

                </section>
                <section id="gly_patched">
                            <input id="gly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly_patched</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="gly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gly_patched-158"><a href="#gly_patched-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="gly_patched-159"><a href="#gly_patched-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="gly_patched-160"><a href="#gly_patched-160"><span class="linenos">160</span></a><span class="sd">        @gly_patched</span>
</span><span id="gly_patched-161"><a href="#gly_patched-161"><span class="linenos">161</span></a><span class="sd">        def func():</span>
</span><span id="gly_patched-162"><a href="#gly_patched-162"><span class="linenos">162</span></a><span class="sd">            for i in range(200):</span>
</span><span id="gly_patched-163"><a href="#gly_patched-163"><span class="linenos">163</span></a><span class="sd">                print(i)</span>
</span><span id="gly_patched-164"><a href="#gly_patched-164"><span class="linenos">164</span></a><span class="sd">                for j in range(100):</span>
</span><span id="gly_patched-165"><a href="#gly_patched-165"><span class="linenos">165</span></a><span class="sd">                    print(j)</span>
</span><span id="gly_patched-166"><a href="#gly_patched-166"><span class="linenos">166</span></a><span class="sd">            </span>
</span><span id="gly_patched-167"><a href="#gly_patched-167"><span class="linenos">167</span></a><span class="sd">            i = 100</span>
</span><span id="gly_patched-168"><a href="#gly_patched-168"><span class="linenos">168</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="gly_patched-169"><a href="#gly_patched-169"><span class="linenos">169</span></a><span class="sd">                print(i)</span>
</span><span id="gly_patched-170"><a href="#gly_patched-170"><span class="linenos">170</span></a><span class="sd">                i -= 1</span>
</span><span id="gly_patched-171"><a href="#gly_patched-171"><span class="linenos">171</span></a>
</span><span id="gly_patched-172"><a href="#gly_patched-172"><span class="linenos">172</span></a><span class="sd">    Is equivalent to:</span>
</span><span id="gly_patched-173"><a href="#gly_patched-173"><span class="linenos">173</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly</span>
</span><span id="gly_patched-174"><a href="#gly_patched-174"><span class="linenos">174</span></a><span class="sd">        def func():</span>
</span><span id="gly_patched-175"><a href="#gly_patched-175"><span class="linenos">175</span></a><span class="sd">            ly = gly()</span>
</span><span id="gly_patched-176"><a href="#gly_patched-176"><span class="linenos">176</span></a><span class="sd">            for i in range(200):</span>
</span><span id="gly_patched-177"><a href="#gly_patched-177"><span class="linenos">177</span></a><span class="sd">                print(i)</span>
</span><span id="gly_patched-178"><a href="#gly_patched-178"><span class="linenos">178</span></a><span class="sd">                for j in range(100):</span>
</span><span id="gly_patched-179"><a href="#gly_patched-179"><span class="linenos">179</span></a><span class="sd">                    print(j)</span>
</span><span id="gly_patched-180"><a href="#gly_patched-180"><span class="linenos">180</span></a><span class="sd">                    ly()</span>
</span><span id="gly_patched-181"><a href="#gly_patched-181"><span class="linenos">181</span></a><span class="sd">                </span>
</span><span id="gly_patched-182"><a href="#gly_patched-182"><span class="linenos">182</span></a><span class="sd">                ly()</span>
</span><span id="gly_patched-183"><a href="#gly_patched-183"><span class="linenos">183</span></a><span class="sd">            </span>
</span><span id="gly_patched-184"><a href="#gly_patched-184"><span class="linenos">184</span></a><span class="sd">            i = 100</span>
</span><span id="gly_patched-185"><a href="#gly_patched-185"><span class="linenos">185</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="gly_patched-186"><a href="#gly_patched-186"><span class="linenos">186</span></a><span class="sd">                print(i)</span>
</span><span id="gly_patched-187"><a href="#gly_patched-187"><span class="linenos">187</span></a><span class="sd">                i -= 1</span>
</span><span id="gly_patched-188"><a href="#gly_patched-188"><span class="linenos">188</span></a><span class="sd">                ly()</span>
</span><span id="gly_patched-189"><a href="#gly_patched-189"><span class="linenos">189</span></a>
</span><span id="gly_patched-190"><a href="#gly_patched-190"><span class="linenos">190</span></a><span class="sd">    Args:</span>
</span><span id="gly_patched-191"><a href="#gly_patched-191"><span class="linenos">191</span></a><span class="sd">        func (Callable): _description_</span>
</span><span id="gly_patched-192"><a href="#gly_patched-192"><span class="linenos">192</span></a>
</span><span id="gly_patched-193"><a href="#gly_patched-193"><span class="linenos">193</span></a><span class="sd">    Returns:</span>
</span><span id="gly_patched-194"><a href="#gly_patched-194"><span class="linenos">194</span></a><span class="sd">        Callable: _description_</span>
</span><span id="gly_patched-195"><a href="#gly_patched-195"><span class="linenos">195</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="gly_patched-196"><a href="#gly_patched-196"><span class="linenos">196</span></a>    <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="gly_patched-197"><a href="#gly_patched-197"><span class="linenos">197</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    @gly_patched
    def func():
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)</p>

<pre><code>    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
</code></pre>

<p>Is equivalent to:
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    def func():
        ly = gly()
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)
                ly()</p>

<pre><code>        ly()

    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
        ly()
</code></pre>

<p>Args:
    func (Callable): _description_</p>

<p>Returns:
    Callable: _description_</p>
</div>


                </section>
                <section id="glyp">
                            <input id="glyp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">glyp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="glyp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#glyp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="glyp-158"><a href="#glyp-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="glyp-159"><a href="#glyp-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="glyp-160"><a href="#glyp-160"><span class="linenos">160</span></a><span class="sd">        @gly_patched</span>
</span><span id="glyp-161"><a href="#glyp-161"><span class="linenos">161</span></a><span class="sd">        def func():</span>
</span><span id="glyp-162"><a href="#glyp-162"><span class="linenos">162</span></a><span class="sd">            for i in range(200):</span>
</span><span id="glyp-163"><a href="#glyp-163"><span class="linenos">163</span></a><span class="sd">                print(i)</span>
</span><span id="glyp-164"><a href="#glyp-164"><span class="linenos">164</span></a><span class="sd">                for j in range(100):</span>
</span><span id="glyp-165"><a href="#glyp-165"><span class="linenos">165</span></a><span class="sd">                    print(j)</span>
</span><span id="glyp-166"><a href="#glyp-166"><span class="linenos">166</span></a><span class="sd">            </span>
</span><span id="glyp-167"><a href="#glyp-167"><span class="linenos">167</span></a><span class="sd">            i = 100</span>
</span><span id="glyp-168"><a href="#glyp-168"><span class="linenos">168</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="glyp-169"><a href="#glyp-169"><span class="linenos">169</span></a><span class="sd">                print(i)</span>
</span><span id="glyp-170"><a href="#glyp-170"><span class="linenos">170</span></a><span class="sd">                i -= 1</span>
</span><span id="glyp-171"><a href="#glyp-171"><span class="linenos">171</span></a>
</span><span id="glyp-172"><a href="#glyp-172"><span class="linenos">172</span></a><span class="sd">    Is equivalent to:</span>
</span><span id="glyp-173"><a href="#glyp-173"><span class="linenos">173</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly</span>
</span><span id="glyp-174"><a href="#glyp-174"><span class="linenos">174</span></a><span class="sd">        def func():</span>
</span><span id="glyp-175"><a href="#glyp-175"><span class="linenos">175</span></a><span class="sd">            ly = gly()</span>
</span><span id="glyp-176"><a href="#glyp-176"><span class="linenos">176</span></a><span class="sd">            for i in range(200):</span>
</span><span id="glyp-177"><a href="#glyp-177"><span class="linenos">177</span></a><span class="sd">                print(i)</span>
</span><span id="glyp-178"><a href="#glyp-178"><span class="linenos">178</span></a><span class="sd">                for j in range(100):</span>
</span><span id="glyp-179"><a href="#glyp-179"><span class="linenos">179</span></a><span class="sd">                    print(j)</span>
</span><span id="glyp-180"><a href="#glyp-180"><span class="linenos">180</span></a><span class="sd">                    ly()</span>
</span><span id="glyp-181"><a href="#glyp-181"><span class="linenos">181</span></a><span class="sd">                </span>
</span><span id="glyp-182"><a href="#glyp-182"><span class="linenos">182</span></a><span class="sd">                ly()</span>
</span><span id="glyp-183"><a href="#glyp-183"><span class="linenos">183</span></a><span class="sd">            </span>
</span><span id="glyp-184"><a href="#glyp-184"><span class="linenos">184</span></a><span class="sd">            i = 100</span>
</span><span id="glyp-185"><a href="#glyp-185"><span class="linenos">185</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="glyp-186"><a href="#glyp-186"><span class="linenos">186</span></a><span class="sd">                print(i)</span>
</span><span id="glyp-187"><a href="#glyp-187"><span class="linenos">187</span></a><span class="sd">                i -= 1</span>
</span><span id="glyp-188"><a href="#glyp-188"><span class="linenos">188</span></a><span class="sd">                ly()</span>
</span><span id="glyp-189"><a href="#glyp-189"><span class="linenos">189</span></a>
</span><span id="glyp-190"><a href="#glyp-190"><span class="linenos">190</span></a><span class="sd">    Args:</span>
</span><span id="glyp-191"><a href="#glyp-191"><span class="linenos">191</span></a><span class="sd">        func (Callable): _description_</span>
</span><span id="glyp-192"><a href="#glyp-192"><span class="linenos">192</span></a>
</span><span id="glyp-193"><a href="#glyp-193"><span class="linenos">193</span></a><span class="sd">    Returns:</span>
</span><span id="glyp-194"><a href="#glyp-194"><span class="linenos">194</span></a><span class="sd">        Callable: _description_</span>
</span><span id="glyp-195"><a href="#glyp-195"><span class="linenos">195</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="glyp-196"><a href="#glyp-196"><span class="linenos">196</span></a>    <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="glyp-197"><a href="#glyp-197"><span class="linenos">197</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    @gly_patched
    def func():
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)</p>

<pre><code>    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
</code></pre>

<p>Is equivalent to:
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    def func():
        ly = gly()
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)
                ly()</p>

<pre><code>        ly()

    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
        ly()
</code></pre>

<p>Args:
    func (Callable): _description_</p>

<p>Returns:
    Callable: _description_</p>
</div>


                </section>
                <section id="gp">
                            <input id="gp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="gp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gp-158"><a href="#gp-158"><span class="linenos">158</span></a><span class="k">def</span> <span class="nf">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="gp-159"><a href="#gp-159"><span class="linenos">159</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Example:</span>
</span><span id="gp-160"><a href="#gp-160"><span class="linenos">160</span></a><span class="sd">        @gly_patched</span>
</span><span id="gp-161"><a href="#gp-161"><span class="linenos">161</span></a><span class="sd">        def func():</span>
</span><span id="gp-162"><a href="#gp-162"><span class="linenos">162</span></a><span class="sd">            for i in range(200):</span>
</span><span id="gp-163"><a href="#gp-163"><span class="linenos">163</span></a><span class="sd">                print(i)</span>
</span><span id="gp-164"><a href="#gp-164"><span class="linenos">164</span></a><span class="sd">                for j in range(100):</span>
</span><span id="gp-165"><a href="#gp-165"><span class="linenos">165</span></a><span class="sd">                    print(j)</span>
</span><span id="gp-166"><a href="#gp-166"><span class="linenos">166</span></a><span class="sd">            </span>
</span><span id="gp-167"><a href="#gp-167"><span class="linenos">167</span></a><span class="sd">            i = 100</span>
</span><span id="gp-168"><a href="#gp-168"><span class="linenos">168</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="gp-169"><a href="#gp-169"><span class="linenos">169</span></a><span class="sd">                print(i)</span>
</span><span id="gp-170"><a href="#gp-170"><span class="linenos">170</span></a><span class="sd">                i -= 1</span>
</span><span id="gp-171"><a href="#gp-171"><span class="linenos">171</span></a>
</span><span id="gp-172"><a href="#gp-172"><span class="linenos">172</span></a><span class="sd">    Is equivalent to:</span>
</span><span id="gp-173"><a href="#gp-173"><span class="linenos">173</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly</span>
</span><span id="gp-174"><a href="#gp-174"><span class="linenos">174</span></a><span class="sd">        def func():</span>
</span><span id="gp-175"><a href="#gp-175"><span class="linenos">175</span></a><span class="sd">            ly = gly()</span>
</span><span id="gp-176"><a href="#gp-176"><span class="linenos">176</span></a><span class="sd">            for i in range(200):</span>
</span><span id="gp-177"><a href="#gp-177"><span class="linenos">177</span></a><span class="sd">                print(i)</span>
</span><span id="gp-178"><a href="#gp-178"><span class="linenos">178</span></a><span class="sd">                for j in range(100):</span>
</span><span id="gp-179"><a href="#gp-179"><span class="linenos">179</span></a><span class="sd">                    print(j)</span>
</span><span id="gp-180"><a href="#gp-180"><span class="linenos">180</span></a><span class="sd">                    ly()</span>
</span><span id="gp-181"><a href="#gp-181"><span class="linenos">181</span></a><span class="sd">                </span>
</span><span id="gp-182"><a href="#gp-182"><span class="linenos">182</span></a><span class="sd">                ly()</span>
</span><span id="gp-183"><a href="#gp-183"><span class="linenos">183</span></a><span class="sd">            </span>
</span><span id="gp-184"><a href="#gp-184"><span class="linenos">184</span></a><span class="sd">            i = 100</span>
</span><span id="gp-185"><a href="#gp-185"><span class="linenos">185</span></a><span class="sd">            while i &gt; 0:</span>
</span><span id="gp-186"><a href="#gp-186"><span class="linenos">186</span></a><span class="sd">                print(i)</span>
</span><span id="gp-187"><a href="#gp-187"><span class="linenos">187</span></a><span class="sd">                i -= 1</span>
</span><span id="gp-188"><a href="#gp-188"><span class="linenos">188</span></a><span class="sd">                ly()</span>
</span><span id="gp-189"><a href="#gp-189"><span class="linenos">189</span></a>
</span><span id="gp-190"><a href="#gp-190"><span class="linenos">190</span></a><span class="sd">    Args:</span>
</span><span id="gp-191"><a href="#gp-191"><span class="linenos">191</span></a><span class="sd">        func (Callable): _description_</span>
</span><span id="gp-192"><a href="#gp-192"><span class="linenos">192</span></a>
</span><span id="gp-193"><a href="#gp-193"><span class="linenos">193</span></a><span class="sd">    Returns:</span>
</span><span id="gp-194"><a href="#gp-194"><span class="linenos">194</span></a><span class="sd">        Callable: _description_</span>
</span><span id="gp-195"><a href="#gp-195"><span class="linenos">195</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="gp-196"><a href="#gp-196"><span class="linenos">196</span></a>    <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="gp-197"><a href="#gp-197"><span class="linenos">197</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    @gly_patched
    def func():
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)</p>

<pre><code>    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
</code></pre>

<p>Is equivalent to:
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    def func():
        ly = gly()
        for i in range(200):
            print(i)
            for j in range(100):
                print(j)
                ly()</p>

<pre><code>        ly()

    i = 100
    while i &gt; 0:
        print(i)
        i -= 1
        ly()
</code></pre>

<p>Args:
    func (Callable): _description_</p>

<p>Returns:
    Callable: _description_</p>
</div>


                </section>
                <section id="agly_patched">
                            <input id="agly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agly_patched</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="agly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agly_patched-204"><a href="#agly_patched-204"><span class="linenos">204</span></a><span class="k">def</span> <span class="nf">agly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="agly_patched-205"><a href="#agly_patched-205"><span class="linenos">205</span></a>    <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="agly_patched-206"><a href="#agly_patched-206"><span class="linenos">206</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


    

                </section>
                <section id="aglyp">
                            <input id="aglyp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">aglyp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="aglyp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aglyp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aglyp-204"><a href="#aglyp-204"><span class="linenos">204</span></a><span class="k">def</span> <span class="nf">agly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="aglyp-205"><a href="#aglyp-205"><span class="linenos">205</span></a>    <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="aglyp-206"><a href="#aglyp-206"><span class="linenos">206</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


    

                </section>
                <section id="agp">
                            <input id="agp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="agp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agp-204"><a href="#agp-204"><span class="linenos">204</span></a><span class="k">def</span> <span class="nf">agly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="agp-205"><a href="#agp-205"><span class="linenos">205</span></a>    <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="agp-206"><a href="#agp-206"><span class="linenos">206</span></a>    <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


    

                </section>
                <section id="GlyPatchManagerError">
                            <input id="GlyPatchManagerError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">GlyPatchManagerError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="GlyPatchManagerError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GlyPatchManagerError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GlyPatchManagerError-213"><a href="#GlyPatchManagerError-213"><span class="linenos">213</span></a><span class="k">class</span> <span class="nc">GlyPatchManagerError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="GlyPatchManagerError-214"><a href="#GlyPatchManagerError-214"><span class="linenos">214</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="GlyPatchManagerError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="GlyPatchManagerError.with_traceback" class="function">with_traceback</dd>
                <dd id="GlyPatchManagerError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="GlyPatchManager">
                            <input id="GlyPatchManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">GlyPatchManager</span>:

                <label class="view-source-button" for="GlyPatchManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GlyPatchManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GlyPatchManager-217"><a href="#GlyPatchManager-217"><span class="linenos">217</span></a><span class="k">class</span> <span class="nc">GlyPatchManager</span><span class="p">:</span>
</span><span id="GlyPatchManager-218"><a href="#GlyPatchManager-218"><span class="linenos">218</span></a>    <span class="n">patched_functions</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="GlyPatchManager-219"><a href="#GlyPatchManager-219"><span class="linenos">219</span></a>    <span class="n">call_tree</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="GlyPatchManager-220"><a href="#GlyPatchManager-220"><span class="linenos">220</span></a>
</span><span id="GlyPatchManager-221"><a href="#GlyPatchManager-221"><span class="linenos">221</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="GlyPatchManager-222"><a href="#GlyPatchManager-222"><span class="linenos">222</span></a>        <span class="k">if</span> <span class="n">func</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">:</span>
</span><span id="GlyPatchManager-223"><a href="#GlyPatchManager-223"><span class="linenos">223</span></a>            <span class="k">if</span> <span class="n">tree</span><span class="p">:</span>
</span><span id="GlyPatchManager-224"><a href="#GlyPatchManager-224"><span class="linenos">224</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="GlyPatchManager-225"><a href="#GlyPatchManager-225"><span class="linenos">225</span></a>                    <span class="n">agly_patched_tree</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="GlyPatchManager-226"><a href="#GlyPatchManager-226"><span class="linenos">226</span></a>                <span class="k">elif</span> <span class="n">is_callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="GlyPatchManager-227"><a href="#GlyPatchManager-227"><span class="linenos">227</span></a>                    <span class="n">gly_patched_tree</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="GlyPatchManager-228"><a href="#GlyPatchManager-228"><span class="linenos">228</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="GlyPatchManager-229"><a href="#GlyPatchManager-229"><span class="linenos">229</span></a>                    <span class="k">raise</span> <span class="n">GlyPatchManagerError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Entity </span><span class="si">{</span><span class="n">func</span><span class="si">}</span><span class="s1"> can not be patched: it must be a callable (either async or not)&#39;</span><span class="p">)</span>
</span><span id="GlyPatchManager-230"><a href="#GlyPatchManager-230"><span class="linenos">230</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="GlyPatchManager-231"><a href="#GlyPatchManager-231"><span class="linenos">231</span></a>                <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="GlyPatchManager-232"><a href="#GlyPatchManager-232"><span class="linenos">232</span></a>                    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">agly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="GlyPatchManager-233"><a href="#GlyPatchManager-233"><span class="linenos">233</span></a>                <span class="k">elif</span> <span class="n">is_callable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="GlyPatchManager-234"><a href="#GlyPatchManager-234"><span class="linenos">234</span></a>                    <span class="n">fn_code</span> <span class="o">=</span> <span class="n">gly_patch</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="GlyPatchManager-235"><a href="#GlyPatchManager-235"><span class="linenos">235</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="GlyPatchManager-236"><a href="#GlyPatchManager-236"><span class="linenos">236</span></a>                    <span class="k">raise</span> <span class="n">GlyPatchManagerError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Entity </span><span class="si">{</span><span class="n">func</span><span class="si">}</span><span class="s1"> can not be patched: it must be a callable (either async or not)&#39;</span><span class="p">)</span>
</span><span id="GlyPatchManager-237"><a href="#GlyPatchManager-237"><span class="linenos">237</span></a>            
</span><span id="GlyPatchManager-238"><a href="#GlyPatchManager-238"><span class="linenos">238</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">[</span><span class="n">func</span><span class="p">]</span> <span class="o">=</span> <span class="n">fn_code</span>
</span><span id="GlyPatchManager-239"><a href="#GlyPatchManager-239"><span class="linenos">239</span></a>        
</span><span id="GlyPatchManager-240"><a href="#GlyPatchManager-240"><span class="linenos">240</span></a>        <span class="k">return</span> <span class="n">func</span>
</span><span id="GlyPatchManager-241"><a href="#GlyPatchManager-241"><span class="linenos">241</span></a>
</span><span id="GlyPatchManager-242"><a href="#GlyPatchManager-242"><span class="linenos">242</span></a>    <span class="k">def</span> <span class="nf">restore</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="GlyPatchManager-243"><a href="#GlyPatchManager-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="n">func</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">:</span>
</span><span id="GlyPatchManager-244"><a href="#GlyPatchManager-244"><span class="linenos">244</span></a>            <span class="k">if</span> <span class="n">tree</span><span class="p">:</span>
</span><span id="GlyPatchManager-245"><a href="#GlyPatchManager-245"><span class="linenos">245</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_unpatch_tree</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="GlyPatchManager-246"><a href="#GlyPatchManager-246"><span class="linenos">246</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="GlyPatchManager-247"><a href="#GlyPatchManager-247"><span class="linenos">247</span></a>                <span class="n">set_code</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">[</span><span class="n">func</span><span class="p">])</span>
</span><span id="GlyPatchManager-248"><a href="#GlyPatchManager-248"><span class="linenos">248</span></a>
</span><span id="GlyPatchManager-249"><a href="#GlyPatchManager-249"><span class="linenos">249</span></a>        <span class="k">return</span> <span class="n">func</span>
</span><span id="GlyPatchManager-250"><a href="#GlyPatchManager-250"><span class="linenos">250</span></a>    
</span><span id="GlyPatchManager-251"><a href="#GlyPatchManager-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="nf">_unpatch_tree</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="GlyPatchManager-252"><a href="#GlyPatchManager-252"><span class="linenos">252</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="GlyPatchManager.patched_functions" class="classattr">
                                <div class="attr variable">
            <span class="name">patched_functions</span>        =
<span class="default_value">{}</span>

        
    </div>
    <a class="headerlink" href="#GlyPatchManager.patched_functions"></a>
    
    

                            </div>
                            <div id="GlyPatchManager.call_tree" class="classattr">
                                <div class="attr variable">
            <span class="name">call_tree</span>        =
<span class="default_value">{}</span>

        
    </div>
    <a class="headerlink" href="#GlyPatchManager.call_tree"></a>
    
    

                            </div>
                            <div id="GlyPatchManager.restore" class="classattr">
                                        <input id="GlyPatchManager.restore-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">restore</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="GlyPatchManager.restore-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GlyPatchManager.restore"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GlyPatchManager.restore-242"><a href="#GlyPatchManager.restore-242"><span class="linenos">242</span></a>    <span class="k">def</span> <span class="nf">restore</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">tree</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="GlyPatchManager.restore-243"><a href="#GlyPatchManager.restore-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="n">func</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">:</span>
</span><span id="GlyPatchManager.restore-244"><a href="#GlyPatchManager.restore-244"><span class="linenos">244</span></a>            <span class="k">if</span> <span class="n">tree</span><span class="p">:</span>
</span><span id="GlyPatchManager.restore-245"><a href="#GlyPatchManager.restore-245"><span class="linenos">245</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_unpatch_tree</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="GlyPatchManager.restore-246"><a href="#GlyPatchManager.restore-246"><span class="linenos">246</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="GlyPatchManager.restore-247"><a href="#GlyPatchManager.restore-247"><span class="linenos">247</span></a>                <span class="n">set_code</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">patched_functions</span><span class="p">[</span><span class="n">func</span><span class="p">])</span>
</span><span id="GlyPatchManager.restore-248"><a href="#GlyPatchManager.restore-248"><span class="linenos">248</span></a>
</span><span id="GlyPatchManager.restore-249"><a href="#GlyPatchManager.restore-249"><span class="linenos">249</span></a>        <span class="k">return</span> <span class="n">func</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="gly_patched_tree">
                            <input id="gly_patched_tree-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly_patched_tree</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#GlyPatchManager">GlyPatchManager</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="gly_patched_tree-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gly_patched_tree"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gly_patched_tree-255"><a href="#gly_patched_tree-255"><span class="linenos">255</span></a><span class="k">def</span> <span class="nf">gly_patched_tree</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GlyPatchManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="gly_patched_tree-256"><a href="#gly_patched_tree-256"><span class="linenos">256</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                </section>
                <section id="agly_patched_tree">
                            <input id="agly_patched_tree-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agly_patched_tree</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n"><a href="#GlyPatchManager">GlyPatchManager</a></span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="agly_patched_tree-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#agly_patched_tree"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="agly_patched_tree-259"><a href="#agly_patched_tree-259"><span class="linenos">259</span></a><span class="k">def</span> <span class="nf">agly_patched_tree</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">gly_patch_manager</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">GlyPatchManager</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="agly_patched_tree-260"><a href="#agly_patched_tree-260"><span class="linenos">260</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>