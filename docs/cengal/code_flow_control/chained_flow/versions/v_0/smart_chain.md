---
title: smart_chain
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.chained_flow<wbr>.versions<wbr>.v_0<wbr>.smart_chain    </h1>

                
                        <input id="mod-smart_chain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-smart_chain-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos"> 18</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a><span class="kn">import</span> <span class="nn">copy</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a><span class="kn">import</span> <span class="nn">traceback</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">contextmanager</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">from</span> <span class="nn">cengal.data_generation.id_generator</span> <span class="kn">import</span> <span class="n">IDGenerator</span><span class="p">,</span> <span class="n">GeneratorType</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions.v_0.result_types</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="sd">Module Docstring</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">IsOK_BlockFailed</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="k">class</span> <span class="nc">IsOK_Closed</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="sd">    is_ok considers it ordinary external exception</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">):</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_Closed</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;Content Holder is closed. &#39;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>                                          <span class="s1">&#39;Content Holder ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>                                          <span class="s1">&#39;Content Holder Info: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>                                          <span class="s1">&#39;Block ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>                                          <span class="s1">&#39;Block Info </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_id</span><span class="p">),</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_info</span><span class="p">),</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_id</span><span class="p">),</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_info</span><span class="p">)))</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="k">class</span> <span class="nc">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="k">class</span> <span class="nc">CriteriaType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="c1"># class CriteriaType():  # much more efficient than Enum inheritance</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>    <span class="n">needed</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># only set of this blocks is needed (should be already successfully done)</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a>    <span class="n">optional</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># all blocks are needed except of this set of blocks</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="nb">any</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># any result will fit criteria</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="n">forbidden</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># set of this blocks should be already failed</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="n">not_successful</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># set of this blocks should not be successfully done (also may not start) at the check time</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="k">class</span> <span class="nc">IgnoreBlockResultCriteriaType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="n">do_not_ignore</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="n">ignore_if_failed</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>    <span class="n">ignore_if_successful</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="k">class</span> <span class="nc">IsOK_HistoryExport</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">history</span><span class="p">,</span> <span class="n">process_error_result</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_HistoryExport</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="o">=</span> <span class="n">history</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_error_result</span> <span class="o">=</span> <span class="n">process_error_result</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="k">class</span> <span class="nc">IsOK_IntenalResult</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">str_data</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">str_data</span> <span class="o">=</span> <span class="n">str_data</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">str_data</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="k">class</span> <span class="nc">IsOK_IntenalResultType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="c1"># class CriteriaType():  # much more efficient than Enum inheritance</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>    <span class="n">built_in_exception__is_ok_block_failed</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>    <span class="n">built_in_exception__bad_history_import</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="n">external_exception</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>    <span class="n">block_did_not_returned_an_answer</span> <span class="o">=</span> <span class="mi">3</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="k">class</span> <span class="nc">IsOK_ContextHolder</span><span class="p">:</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context_holder_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">global_block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>                 <span class="n">raise_exceptions</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">save_debug_trace</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">closeable</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">        :param context_holder_id:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">        :param context_holder_info:</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="sd">        :param global_block_results_criteria: will be set to ResultType(CriteriaType.optional, set()) if None;</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="sd">            in this case all blocks are required.</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a><span class="sd">        :param raise_exceptions:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="sd">        :param save_debug_trace:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="sd">        :param closeable:</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">        :return:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>        <span class="c1"># Use only ResultType(CriteriaType.optional, ...) or ResultType(CriteriaType.needed, set()).</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="c1"># Other will be ignored here.</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>        <span class="c1"># You may use global_block_results_criteria=ResultType(CriteriaType.optional, set()) to create criteria</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="c1"># &quot;no fails in any block&quot;</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_id</span> <span class="o">=</span> <span class="n">context_holder_id</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_info</span> <span class="o">=</span> <span class="n">context_holder_info</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_reserve_block_id_generator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">(</span><span class="n">GeneratorType</span><span class="o">.</span><span class="n">guid_string</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="n">global_block_results_criteria</span> <span class="o">=</span> <span class="n">global_block_results_criteria</span> <span class="ow">or</span> <span class="n">ResultType</span><span class="p">(</span><span class="n">CriteriaType</span><span class="o">.</span><span class="n">optional</span><span class="p">,</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="k">if</span> <span class="n">global_block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">global_block_results_criteria</span><span class="p">)</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_raise_exceptions</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_save_debug_trace</span> <span class="o">=</span> <span class="n">save_debug_trace</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closeable</span> <span class="o">=</span> <span class="n">closeable</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_all_made_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    <span class="c1"># def _push_criteria(self, set_of_needed_blocks=None, set_of_optional_blocks=None):</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">_push_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">):</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>        <span class="c1"># Do not use!</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">_pop_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>        <span class="c1"># Do not use!</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="c1"># May raise exception if len(self.criteria_list)==0, but this is OK.</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="k">def</span> <span class="nf">read_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>        <span class="n">criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>            <span class="n">criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>        <span class="k">return</span> <span class="n">criteria</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>    <span class="k">def</span> <span class="nf">_push_block_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="k">def</span> <span class="nf">_pop_block_info</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">push_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="p">)</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">def</span> <span class="nf">push_result_c</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="c1"># &quot;class&quot; version: to use when result = ResultExistence()</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="k">def</span> <span class="nf">read_block_result_link</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>        <span class="c1"># result is NOT protected from changing!</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>        <span class="c1"># result = self._blocks_library[block_id][3]</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>    <span class="k">def</span> <span class="nf">read_block_result_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="k">def</span> <span class="nf">read_block_result_deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    <span class="k">def</span> <span class="nf">_save_block_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="c1"># ignore_block_result_criteria = ignore_block_result_criteria or IgnoreBlockResultCriteriaType.do_not_ignore</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="k">if</span> <span class="p">((</span><span class="n">IgnoreBlockResultCriteriaType</span><span class="o">.</span><span class="n">ignore_if_failed</span> <span class="o">==</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="ow">and</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>                <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span> \
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>                <span class="ow">or</span> <span class="p">((</span><span class="n">IgnoreBlockResultCriteriaType</span><span class="o">.</span><span class="n">ignore_if_successful</span> <span class="o">==</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="ow">and</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>            <span class="k">return</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="n">import_depth</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="n">full_block_info</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span><span class="p">,</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>                           <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">,</span> <span class="n">import_depth</span><span class="p">)</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">full_block_info</span><span class="p">)</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">full_block_info</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_all_made_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">:</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>            <span class="n">current_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_criteria</span><span class="p">()</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>            <span class="k">if</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">needed</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="p">):</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">optional</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span> <span class="o">-</span> <span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">any</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">forbidden</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span><span class="p">):</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">not_successful</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>    <span class="nd">@staticmethod</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="k">def</span> <span class="nf">_block_list_to_str</span><span class="p">(</span><span class="n">block_list</span><span class="p">):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>        <span class="n">blocks_str</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s1">&#39;(index(</span><span class="si">{}</span><span class="s1">), depth(</span><span class="si">{}</span><span class="s1">), ID(</span><span class="si">{}</span><span class="s1">), INFO(</span><span class="si">{}</span><span class="s1">), RESULT(</span><span class="si">{}</span><span class="s1">))&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">4</span><span class="p">]),</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>                                                          <span class="s1">&#39;(</span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">1</span><span class="p">])))</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>                                <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="n">block_list</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="k">return</span> <span class="n">blocks_str</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>    <span class="k">def</span> <span class="nf">_block_str_to_context_holder_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">blocks_str</span><span class="p">):</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="s1">&#39;{{{{CONTEXT_HOLDER_ID(</span><span class="si">{}</span><span class="s1">): CONTEXT_HOLDER_INFO(</span><span class="si">{}</span><span class="s1">)}}:[</span><span class="se">\n</span><span class="si">{}</span><span class="se">\n</span><span class="s1">]}}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_info</span><span class="p">,</span> <span class="n">blocks_str</span><span class="p">)</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">:</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>        <span class="n">bad_blocks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">()</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>        <span class="n">full_history_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_list_to_str</span><span class="p">(</span><span class="n">bad_blocks</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_str_to_context_holder_str</span><span class="p">(</span><span class="n">full_history_str</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>    <span class="k">def</span> <span class="nf">raise_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">())</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">raise_full_history</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>    <span class="k">def</span> <span class="nf">process_history_import</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">his_ex</span><span class="p">):</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="n">history</span> <span class="o">=</span> <span class="n">his_ex</span><span class="o">.</span><span class="n">history</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="n">history</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="n">full_block_info</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span><span class="o">.</span><span class="n">get_new_ID</span><span class="p">(),</span> <span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                               <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">full_block_info</span><span class="p">)</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>    <span class="k">def</span> <span class="nf">_reopen</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="n">full_history_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_list_to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_str_to_context_holder_str</span><span class="p">(</span><span class="n">full_history_str</span><span class="p">)</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>        <span class="k">return</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a><span class="nd">@contextmanager</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a><span class="k">def</span> <span class="nf">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>    <span class="k">if</span> <span class="n">block_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="n">new_id</span> <span class="o">=</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_reserve_block_id_generator</span><span class="p">()</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="p">(</span><span class="n">new_id</span><span class="p">,</span> <span class="n">new_id</span><span class="p">)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>    <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_closeable</span> <span class="ow">and</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_closed</span><span class="p">:</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="k">raise</span> <span class="n">IsOK_Closed</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_block_info</span><span class="p">(</span><span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">)</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_criteria</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    <span class="n">need_to_save_block_result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>        <span class="k">yield</span> <span class="n">context_holder</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>    <span class="k">except</span> <span class="n">IsOK_BlockFailed</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>        <span class="n">result_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>        <span class="k">if</span> <span class="n">exc</span><span class="o">.</span><span class="n">args</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>            <span class="n">result_info</span> <span class="o">=</span> <span class="n">exc</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">built_in_exception__is_ok_block_failed</span><span class="p">,</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                <span class="s1">&#39;ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: IsOK_BlockFailed (</span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">result_info</span><span class="p">),</span> <span class="n">result_info</span><span class="p">))</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>    <span class="k">except</span> <span class="n">IsOK_HistoryExport</span> <span class="k">as</span> <span class="n">export</span><span class="p">:</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">process_history_import</span><span class="p">(</span><span class="n">export</span><span class="p">)</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>        <span class="k">if</span> <span class="n">export</span><span class="o">.</span><span class="n">process_error_result</span><span class="p">:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>                    <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">built_in_exception__bad_history_import</span><span class="p">,</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                    <span class="s1">&#39;ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>        <span class="n">exc</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>        <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_obj</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exc</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        <span class="n">tb_full_file_name</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">exc_tb</span><span class="o">.</span><span class="n">tb_frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="n">tb_line_number</span> <span class="o">=</span> <span class="n">exc_tb</span><span class="o">.</span><span class="n">tb_lineno</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="n">tb_function_name</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="n">tb_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        <span class="n">tb_list</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">extract_tb</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tb_list</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>            <span class="n">actual_tb</span> <span class="o">=</span> <span class="n">tb_list</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">,</span> <span class="n">tb_text</span> <span class="o">=</span> <span class="n">actual_tb</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">exc</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>        <span class="n">error_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">str</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>        <span class="c1"># print(&#39;+++&#39;, error_str)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="n">formatted_traceback</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_exception</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">exception</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">exception</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">formatted_traceback</span><span class="p">,)</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="n">trace_str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_debug_trace</span><span class="p">:</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>            <span class="n">result_string</span> <span class="o">=</span> <span class="s1">&#39;ISOK INTERNAL RESULT. CODE EXCEPTION &quot;</span><span class="si">{}</span><span class="s1">&quot; AT &quot;</span><span class="si">{}</span><span class="s1">&quot;:</span><span class="si">{}</span><span class="s1"> in </span><span class="si">{}</span><span class="s1"> WITH TRACE: </span><span class="se">\n</span><span class="s1">&#39;</span> \
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>                            <span class="s1">&#39;</span><span class="si">{}</span><span class="se">\n</span><span class="s1">&#39;</span> \
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>                            <span class="s1">&#39;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~&#39;</span> \
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>                            <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">error_str</span><span class="p">,</span> <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">,</span> <span class="n">trace_str</span><span class="p">)</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            <span class="n">result_string</span> <span class="o">=</span> <span class="s1">&#39;ISOK INTERNAL RESULT. CODE EXCEPTION &quot;</span><span class="si">{}</span><span class="s1">&quot; AT &quot;</span><span class="si">{}</span><span class="s1">&quot;:</span><span class="si">{}</span><span class="s1"> in </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>                    <span class="n">error_str</span><span class="p">,</span> <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">)</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>                <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">external_exception</span><span class="p">,</span> <span class="n">result_string</span><span class="p">,</span> <span class="n">exc</span><span class="p">))</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="c1"># print(result_string)</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="c1"># _is_ok_reader_runner__context_holder.push_result(False, sys.exc_info()[1])</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_raise_exceptions</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="n">need_to_save_block_result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_block_result</span><span class="p">()</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">raise_bad_blocks</span><span class="p">()</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>            <span class="c1"># raise</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>            <span class="c1"># _is_ok_reader_runner__context_holder.push_result(True)</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>                    <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">block_did_not_returned_an_answer</span><span class="p">,</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>                    <span class="s1">&#39;ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="k">if</span> <span class="n">need_to_save_block_result</span><span class="p">:</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_block_result</span><span class="p">(</span><span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_criteria</span><span class="p">()</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_block_info</span><span class="p">()</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a><span class="k">def</span> <span class="nf">is_ok__function</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="sd">    Parameters: is_ok__context_holder= (required)</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a><span class="sd">        , is_ok__block_id= (required)</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a><span class="sd">        , is_ok__block_info= (optional)</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a><span class="sd">        , is_ok__block_results_criteria= (optional)</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="sd">        , is_ok__ignore_block_result_criteria= (optional).</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a><span class="sd">    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a><span class="sd">    :param target_function: function</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a><span class="sd">    :return:</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_id&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="n">block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_info&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="n">block_info</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_info&#39;</span><span class="p">]</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_info&#39;</span><span class="p">]</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>            <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> \
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>                <span class="n">context</span><span class="p">:</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a><span class="k">class</span> <span class="nc">_IsOkRunner</span><span class="p">:</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">ignore_block_result_criteria</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>    <span class="k">def</span> <span class="fm">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="n">target_functor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__current_globals</span><span class="p">:</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>            <span class="n">target_functor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__current_globals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_functor</span><span class="p">)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_info</span><span class="p">,</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>                       <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_results_criteria</span><span class="p">,</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>                       <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>                <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>                <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>            <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a><span class="k">class</span> <span class="nc">IsOkRunner</span><span class="p">:</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>                             <span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a><span class="k">class</span> <span class="nc">_IsOkCallRunner</span><span class="p">:</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">ignore_block_result_criteria</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">target_functor</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_functor</span><span class="p">)</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_info</span><span class="p">,</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__block_results_criteria</span><span class="p">,</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner__ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a><span class="k">class</span> <span class="nc">IsOkCallRunner</span><span class="p">:</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkCallRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>                                 <span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a><span class="k">def</span> <span class="nf">is_ok__function__simple</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a><span class="sd">    Parameters: is_ok__context_holder= (required)</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a><span class="sd">        , is_ok__block_id= (optional) (default value == str(target_function))</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a><span class="sd">        , is_ok__block_results_criteria= (optional)</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a><span class="sd">        , is_ok__ignore_block_result_criteria= (optional).</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a><span class="sd">    Parameters passed to the target_function: .</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a><span class="sd">    :param target_function: function</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a><span class="sd">    :return:</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>        <span class="c1"># block_id = &#39;__UNNAMED_FUNCTION_SIMPLE_BLOCK__&#39;</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_function</span><span class="p">)</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_id&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>        <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>            <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>            <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>                <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>                <span class="n">context</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a><span class="k">class</span> <span class="nc">_IsOkRunnerSimple</span><span class="p">:</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">ignore_block_result_criteria</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>    <span class="k">def</span> <span class="fm">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>        <span class="n">target_functor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__current_globals</span><span class="p">:</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>            <span class="n">target_functor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__current_globals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>        <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_functor</span><span class="p">)</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>            <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span><span class="p">,</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                       <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span><span class="p">,</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>                       <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>                    <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                    <span class="n">is_good_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span><span class="p">(</span><span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>                    <span class="n">context</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="n">is_good_result</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>            <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>        <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a><span class="k">class</span> <span class="nc">IsOkUniRunner</span><span class="p">:</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunner</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunnerSimple</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                                   <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">)</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a><span class="k">class</span> <span class="nc">_IsOkCallRunnerSimple</span><span class="p">:</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">ignore_block_result_criteria</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">target_functor</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span> <span class="ow">or</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_functor</span><span class="p">)</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span><span class="p">,</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span><span class="p">,</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>            <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>                <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>                <span class="n">is_good_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span><span class="p">(</span><span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>                <span class="n">context</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="n">is_good_result</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a><span class="k">class</span> <span class="nc">IsOkUniCallRunner</span><span class="p">:</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunner</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunnerSimple</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>                                   <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">)</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a><span class="k">class</span> <span class="nc">_IsOkValRunner</span><span class="p">:</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">reaction_to_the_result</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">ignore_block_result_criteria</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__reaction_to_the_result</span> <span class="o">=</span> <span class="n">reaction_to_the_result</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">functor_result</span><span class="p">):</span>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">functor_result</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_id</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_info</span><span class="p">,</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__block_results_criteria</span><span class="p">,</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>                   <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>            <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>                <span class="n">is_good_result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__function_result_criteria</span><span class="p">(</span><span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__reaction_to_the_result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>                    <span class="n">verdict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_runner_simple__reaction_to_the_result</span><span class="p">(</span><span class="n">is_good_result</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>                    <span class="n">target_function_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">target_function_result</span><span class="p">,</span> <span class="n">verdict</span><span class="p">)</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a>                <span class="n">context</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="n">is_good_result</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a>        <span class="k">return</span> <span class="n">functor_result</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a><span class="k">class</span> <span class="nc">IsOkValRunner</span><span class="p">:</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">reaction_to_the_result</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reaction_to_the_result</span> <span class="o">=</span> <span class="n">reaction_to_the_result</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkValRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>                                <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>                                <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">reaction_to_the_result</span><span class="p">)</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a><span class="nd">@contextmanager</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos">713</span></a><span class="k">def</span> <span class="nf">is_ok_reader</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos">714</span></a>    <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos">715</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_criteria</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="L-716"><a href="#L-716"><span class="linenos">716</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos">717</span></a>        <span class="k">yield</span> <span class="n">context_holder</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos">718</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="L-719"><a href="#L-719"><span class="linenos">719</span></a>        <span class="k">raise</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos">720</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos">721</span></a>        <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos">722</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_criteria</span><span class="p">()</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos">723</span></a>        <span class="k">if</span> <span class="n">close</span><span class="p">:</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos">724</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span><span id="L-725"><a href="#L-725"><span class="linenos">725</span></a>
</span><span id="L-726"><a href="#L-726"><span class="linenos">726</span></a>
</span><span id="L-727"><a href="#L-727"><span class="linenos">727</span></a><span class="k">def</span> <span class="nf">is_ok_reader__function</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="L-728"><a href="#L-728"><span class="linenos">728</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos">729</span></a><span class="sd">    Parameters: is_ok__context_holder= (required), is_ok__block_results_criteria= (optional), is_ok__close= (optional).</span>
</span><span id="L-730"><a href="#L-730"><span class="linenos">730</span></a><span class="sd">    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos">731</span></a><span class="sd">    :param target_function: function</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos">732</span></a><span class="sd">    :return:</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos">733</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos">734</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos">735</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos">736</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-737"><a href="#L-737"><span class="linenos">737</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos">738</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos">739</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-740"><a href="#L-740"><span class="linenos">740</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos">741</span></a>
</span><span id="L-742"><a href="#L-742"><span class="linenos">742</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos">743</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos">744</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-745"><a href="#L-745"><span class="linenos">745</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="L-746"><a href="#L-746"><span class="linenos">746</span></a>
</span><span id="L-747"><a href="#L-747"><span class="linenos">747</span></a>        <span class="n">close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-748"><a href="#L-748"><span class="linenos">748</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__close&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos">749</span></a>            <span class="n">close</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__close&#39;</span><span class="p">]</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos">750</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__close&#39;</span><span class="p">]</span>
</span><span id="L-751"><a href="#L-751"><span class="linenos">751</span></a>
</span><span id="L-752"><a href="#L-752"><span class="linenos">752</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos">753</span></a>        <span class="k">with</span> <span class="n">is_ok_reader</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos">754</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-755"><a href="#L-755"><span class="linenos">755</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos">756</span></a>
</span><span id="L-757"><a href="#L-757"><span class="linenos">757</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-758"><a href="#L-758"><span class="linenos">758</span></a>
</span><span id="L-759"><a href="#L-759"><span class="linenos">759</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos">760</span></a>
</span><span id="L-761"><a href="#L-761"><span class="linenos">761</span></a>
</span><span id="L-762"><a href="#L-762"><span class="linenos">762</span></a><span class="k">class</span> <span class="nc">_IsOkReaderRunner</span><span class="p">:</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos">763</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos">764</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-765"><a href="#L-765"><span class="linenos">765</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-766"><a href="#L-766"><span class="linenos">766</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos">767</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__close</span> <span class="o">=</span> <span class="n">close</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos">768</span></a>
</span><span id="L-769"><a href="#L-769"><span class="linenos">769</span></a>    <span class="k">def</span> <span class="fm">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos">770</span></a>        <span class="n">target_functor</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-771"><a href="#L-771"><span class="linenos">771</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__current_globals</span><span class="p">:</span>
</span><span id="L-772"><a href="#L-772"><span class="linenos">772</span></a>            <span class="n">target_functor</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__current_globals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos">773</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-774"><a href="#L-774"><span class="linenos">774</span></a>            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos">775</span></a>
</span><span id="L-776"><a href="#L-776"><span class="linenos">776</span></a>        <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-777"><a href="#L-777"><span class="linenos">777</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos">778</span></a>            <span class="k">with</span> <span class="n">is_ok_reader</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__context_holder</span><span class="p">,</span>
</span><span id="L-779"><a href="#L-779"><span class="linenos">779</span></a>                              <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__block_results_criteria</span><span class="p">,</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos">780</span></a>                              <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__close</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-781"><a href="#L-781"><span class="linenos">781</span></a>                <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-782"><a href="#L-782"><span class="linenos">782</span></a>                <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos">783</span></a>
</span><span id="L-784"><a href="#L-784"><span class="linenos">784</span></a>            <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-785"><a href="#L-785"><span class="linenos">785</span></a>
</span><span id="L-786"><a href="#L-786"><span class="linenos">786</span></a>        <span class="k">return</span> <span class="n">new_target_function</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos">787</span></a>
</span><span id="L-788"><a href="#L-788"><span class="linenos">788</span></a>
</span><span id="L-789"><a href="#L-789"><span class="linenos">789</span></a><span class="k">class</span> <span class="nc">IsOkReaderRunner</span><span class="p">:</span>
</span><span id="L-790"><a href="#L-790"><span class="linenos">790</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos">791</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos">792</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos">793</span></a>
</span><span id="L-794"><a href="#L-794"><span class="linenos">794</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-795"><a href="#L-795"><span class="linenos">795</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkReaderRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos">796</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-797"><a href="#L-797"><span class="linenos">797</span></a>
</span><span id="L-798"><a href="#L-798"><span class="linenos">798</span></a>
</span><span id="L-799"><a href="#L-799"><span class="linenos">799</span></a><span class="k">class</span> <span class="nc">_IsOkReaderCallRunner</span><span class="p">:</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos">800</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-801"><a href="#L-801"><span class="linenos">801</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos">802</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__block_results_criteria</span> <span class="o">=</span> <span class="n">block_results_criteria</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos">803</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__close</span> <span class="o">=</span> <span class="n">close</span>
</span><span id="L-804"><a href="#L-804"><span class="linenos">804</span></a>
</span><span id="L-805"><a href="#L-805"><span class="linenos">805</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">target_functor</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos">806</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos">807</span></a>        <span class="k">with</span> <span class="n">is_ok_reader</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__context_holder</span><span class="p">,</span>
</span><span id="L-808"><a href="#L-808"><span class="linenos">808</span></a>                          <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__block_results_criteria</span><span class="p">,</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos">809</span></a>                          <span class="bp">self</span><span class="o">.</span><span class="n">_is_ok_reader_runner__close</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos">810</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="L-811"><a href="#L-811"><span class="linenos">811</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_functor</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-812"><a href="#L-812"><span class="linenos">812</span></a>
</span><span id="L-813"><a href="#L-813"><span class="linenos">813</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos">814</span></a>
</span><span id="L-815"><a href="#L-815"><span class="linenos">815</span></a>
</span><span id="L-816"><a href="#L-816"><span class="linenos">816</span></a><span class="k">class</span> <span class="nc">IsOkReaderCallRunner</span><span class="p">:</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos">817</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos">818</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos">819</span></a>
</span><span id="L-820"><a href="#L-820"><span class="linenos">820</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="L-821"><a href="#L-821"><span class="linenos">821</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkReaderCallRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos">822</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            </section>
                <section id="IsOK_BlockFailed">
                            <input id="IsOK_BlockFailed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_BlockFailed</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="IsOK_BlockFailed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_BlockFailed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_BlockFailed-45"><a href="#IsOK_BlockFailed-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">IsOK_BlockFailed</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="IsOK_BlockFailed.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="IsOK_BlockFailed.with_traceback" class="function">with_traceback</dd>
                <dd id="IsOK_BlockFailed.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IsOK_Closed">
                            <input id="IsOK_Closed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_Closed</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="IsOK_Closed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_Closed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_Closed-48"><a href="#IsOK_Closed-48"><span class="linenos">48</span></a><span class="k">class</span> <span class="nc">IsOK_Closed</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="IsOK_Closed-49"><a href="#IsOK_Closed-49"><span class="linenos">49</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IsOK_Closed-50"><a href="#IsOK_Closed-50"><span class="linenos">50</span></a><span class="sd">    is_ok considers it ordinary external exception</span>
</span><span id="IsOK_Closed-51"><a href="#IsOK_Closed-51"><span class="linenos">51</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="IsOK_Closed-52"><a href="#IsOK_Closed-52"><span class="linenos">52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">):</span>
</span><span id="IsOK_Closed-53"><a href="#IsOK_Closed-53"><span class="linenos">53</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_Closed</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;Content Holder is closed. &#39;</span>
</span><span id="IsOK_Closed-54"><a href="#IsOK_Closed-54"><span class="linenos">54</span></a>                                          <span class="s1">&#39;Content Holder ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed-55"><a href="#IsOK_Closed-55"><span class="linenos">55</span></a>                                          <span class="s1">&#39;Content Holder Info: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed-56"><a href="#IsOK_Closed-56"><span class="linenos">56</span></a>                                          <span class="s1">&#39;Block ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed-57"><a href="#IsOK_Closed-57"><span class="linenos">57</span></a>                                          <span class="s1">&#39;Block Info </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_id</span><span class="p">),</span>
</span><span id="IsOK_Closed-58"><a href="#IsOK_Closed-58"><span class="linenos">58</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_info</span><span class="p">),</span>
</span><span id="IsOK_Closed-59"><a href="#IsOK_Closed-59"><span class="linenos">59</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_id</span><span class="p">),</span>
</span><span id="IsOK_Closed-60"><a href="#IsOK_Closed-60"><span class="linenos">60</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_info</span><span class="p">)))</span>
</span><span id="IsOK_Closed-61"><a href="#IsOK_Closed-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOK_Closed-62"><a href="#IsOK_Closed-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="IsOK_Closed-63"><a href="#IsOK_Closed-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span></pre></div>


            <div class="docstring"><p>is_ok considers it ordinary external exception</p>
</div>


                            <div id="IsOK_Closed.__init__" class="classattr">
                                        <input id="IsOK_Closed.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOK_Closed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">context_holder</span>, </span><span class="param"><span class="n">block_id</span>, </span><span class="param"><span class="n">block_info</span></span>)</span>

                <label class="view-source-button" for="IsOK_Closed.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_Closed.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_Closed.__init__-52"><a href="#IsOK_Closed.__init__-52"><span class="linenos">52</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">):</span>
</span><span id="IsOK_Closed.__init__-53"><a href="#IsOK_Closed.__init__-53"><span class="linenos">53</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_Closed</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;Content Holder is closed. &#39;</span>
</span><span id="IsOK_Closed.__init__-54"><a href="#IsOK_Closed.__init__-54"><span class="linenos">54</span></a>                                          <span class="s1">&#39;Content Holder ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed.__init__-55"><a href="#IsOK_Closed.__init__-55"><span class="linenos">55</span></a>                                          <span class="s1">&#39;Content Holder Info: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed.__init__-56"><a href="#IsOK_Closed.__init__-56"><span class="linenos">56</span></a>                                          <span class="s1">&#39;Block ID: </span><span class="si">{}</span><span class="s1">; &#39;</span>
</span><span id="IsOK_Closed.__init__-57"><a href="#IsOK_Closed.__init__-57"><span class="linenos">57</span></a>                                          <span class="s1">&#39;Block Info </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_id</span><span class="p">),</span>
</span><span id="IsOK_Closed.__init__-58"><a href="#IsOK_Closed.__init__-58"><span class="linenos">58</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">context_holder</span><span class="o">.</span><span class="n">_context_holder_info</span><span class="p">),</span>
</span><span id="IsOK_Closed.__init__-59"><a href="#IsOK_Closed.__init__-59"><span class="linenos">59</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_id</span><span class="p">),</span>
</span><span id="IsOK_Closed.__init__-60"><a href="#IsOK_Closed.__init__-60"><span class="linenos">60</span></a>                                                                 <span class="nb">str</span><span class="p">(</span><span class="n">block_info</span><span class="p">)))</span>
</span><span id="IsOK_Closed.__init__-61"><a href="#IsOK_Closed.__init__-61"><span class="linenos">61</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOK_Closed.__init__-62"><a href="#IsOK_Closed.__init__-62"><span class="linenos">62</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="IsOK_Closed.__init__-63"><a href="#IsOK_Closed.__init__-63"><span class="linenos">63</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_Closed.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOK_Closed.context_holder"></a>
    
    

                            </div>
                            <div id="IsOK_Closed.block_id" class="classattr">
                                <div class="attr variable">
            <span class="name">block_id</span>

        
    </div>
    <a class="headerlink" href="#IsOK_Closed.block_id"></a>
    
    

                            </div>
                            <div id="IsOK_Closed.block_info" class="classattr">
                                <div class="attr variable">
            <span class="name">block_info</span>

        
    </div>
    <a class="headerlink" href="#IsOK_Closed.block_info"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.BaseException</dt>
                                <dd id="IsOK_Closed.with_traceback" class="function">with_traceback</dd>
                <dd id="IsOK_Closed.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IsOKForFunction_ParameterNeeded">
                            <input id="IsOKForFunction_ParameterNeeded-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOKForFunction_ParameterNeeded</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="IsOKForFunction_ParameterNeeded-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOKForFunction_ParameterNeeded"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOKForFunction_ParameterNeeded-66"><a href="#IsOKForFunction_ParameterNeeded-66"><span class="linenos">66</span></a><span class="k">class</span> <span class="nc">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span> <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="IsOKForFunction_ParameterNeeded.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="IsOKForFunction_ParameterNeeded.with_traceback" class="function">with_traceback</dd>
                <dd id="IsOKForFunction_ParameterNeeded.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CriteriaType">
                            <input id="CriteriaType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CriteriaType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="CriteriaType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CriteriaType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CriteriaType-69"><a href="#CriteriaType-69"><span class="linenos">69</span></a><span class="k">class</span> <span class="nc">CriteriaType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="CriteriaType-70"><a href="#CriteriaType-70"><span class="linenos">70</span></a><span class="c1"># class CriteriaType():  # much more efficient than Enum inheritance</span>
</span><span id="CriteriaType-71"><a href="#CriteriaType-71"><span class="linenos">71</span></a>    <span class="n">needed</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># only set of this blocks is needed (should be already successfully done)</span>
</span><span id="CriteriaType-72"><a href="#CriteriaType-72"><span class="linenos">72</span></a>    <span class="n">optional</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># all blocks are needed except of this set of blocks</span>
</span><span id="CriteriaType-73"><a href="#CriteriaType-73"><span class="linenos">73</span></a>    <span class="nb">any</span> <span class="o">=</span> <span class="mi">2</span>  <span class="c1"># any result will fit criteria</span>
</span><span id="CriteriaType-74"><a href="#CriteriaType-74"><span class="linenos">74</span></a>    <span class="n">forbidden</span> <span class="o">=</span> <span class="mi">3</span>  <span class="c1"># set of this blocks should be already failed</span>
</span><span id="CriteriaType-75"><a href="#CriteriaType-75"><span class="linenos">75</span></a>    <span class="n">not_successful</span> <span class="o">=</span> <span class="mi">4</span>  <span class="c1"># set of this blocks should not be successfully done (also may not start) at the check time</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="CriteriaType.needed" class="classattr">
                                <div class="attr variable">
            <span class="name">needed</span>        =
<span class="default_value">&lt;<a href="#CriteriaType.needed">CriteriaType.needed</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#CriteriaType.needed"></a>
    
    

                            </div>
                            <div id="CriteriaType.optional" class="classattr">
                                <div class="attr variable">
            <span class="name">optional</span>        =
<span class="default_value">&lt;<a href="#CriteriaType.optional">CriteriaType.optional</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#CriteriaType.optional"></a>
    
    

                            </div>
                            <div id="CriteriaType.any" class="classattr">
                                <div class="attr variable">
            <span class="name">any</span>        =
<span class="default_value">&lt;<a href="#CriteriaType.any">CriteriaType.any</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#CriteriaType.any"></a>
    
    

                            </div>
                            <div id="CriteriaType.forbidden" class="classattr">
                                <div class="attr variable">
            <span class="name">forbidden</span>        =
<span class="default_value">&lt;<a href="#CriteriaType.forbidden">CriteriaType.forbidden</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#CriteriaType.forbidden"></a>
    
    

                            </div>
                            <div id="CriteriaType.not_successful" class="classattr">
                                <div class="attr variable">
            <span class="name">not_successful</span>        =
<span class="default_value">&lt;<a href="#CriteriaType.not_successful">CriteriaType.not_successful</a>: 4&gt;</span>

        
    </div>
    <a class="headerlink" href="#CriteriaType.not_successful"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="CriteriaType.name" class="variable">name</dd>
                <dd id="CriteriaType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IgnoreBlockResultCriteriaType">
                            <input id="IgnoreBlockResultCriteriaType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IgnoreBlockResultCriteriaType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="IgnoreBlockResultCriteriaType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IgnoreBlockResultCriteriaType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IgnoreBlockResultCriteriaType-78"><a href="#IgnoreBlockResultCriteriaType-78"><span class="linenos">78</span></a><span class="k">class</span> <span class="nc">IgnoreBlockResultCriteriaType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="IgnoreBlockResultCriteriaType-79"><a href="#IgnoreBlockResultCriteriaType-79"><span class="linenos">79</span></a>    <span class="n">do_not_ignore</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="IgnoreBlockResultCriteriaType-80"><a href="#IgnoreBlockResultCriteriaType-80"><span class="linenos">80</span></a>    <span class="n">ignore_if_failed</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="IgnoreBlockResultCriteriaType-81"><a href="#IgnoreBlockResultCriteriaType-81"><span class="linenos">81</span></a>    <span class="n">ignore_if_successful</span> <span class="o">=</span> <span class="mi">2</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="IgnoreBlockResultCriteriaType.do_not_ignore" class="classattr">
                                <div class="attr variable">
            <span class="name">do_not_ignore</span>        =
<span class="default_value">&lt;<a href="#IgnoreBlockResultCriteriaType.do_not_ignore">IgnoreBlockResultCriteriaType.do_not_ignore</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#IgnoreBlockResultCriteriaType.do_not_ignore"></a>
    
    

                            </div>
                            <div id="IgnoreBlockResultCriteriaType.ignore_if_failed" class="classattr">
                                <div class="attr variable">
            <span class="name">ignore_if_failed</span>        =
<span class="default_value">&lt;<a href="#IgnoreBlockResultCriteriaType.ignore_if_failed">IgnoreBlockResultCriteriaType.ignore_if_failed</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#IgnoreBlockResultCriteriaType.ignore_if_failed"></a>
    
    

                            </div>
                            <div id="IgnoreBlockResultCriteriaType.ignore_if_successful" class="classattr">
                                <div class="attr variable">
            <span class="name">ignore_if_successful</span>        =
<span class="default_value">&lt;<a href="#IgnoreBlockResultCriteriaType.ignore_if_successful">IgnoreBlockResultCriteriaType.ignore_if_successful</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#IgnoreBlockResultCriteriaType.ignore_if_successful"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="IgnoreBlockResultCriteriaType.name" class="variable">name</dd>
                <dd id="IgnoreBlockResultCriteriaType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IsOK_HistoryExport">
                            <input id="IsOK_HistoryExport-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_HistoryExport</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="IsOK_HistoryExport-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_HistoryExport"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_HistoryExport-84"><a href="#IsOK_HistoryExport-84"><span class="linenos">84</span></a><span class="k">class</span> <span class="nc">IsOK_HistoryExport</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="IsOK_HistoryExport-85"><a href="#IsOK_HistoryExport-85"><span class="linenos">85</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">history</span><span class="p">,</span> <span class="n">process_error_result</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IsOK_HistoryExport-86"><a href="#IsOK_HistoryExport-86"><span class="linenos">86</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_HistoryExport</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="IsOK_HistoryExport-87"><a href="#IsOK_HistoryExport-87"><span class="linenos">87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="o">=</span> <span class="n">history</span>
</span><span id="IsOK_HistoryExport-88"><a href="#IsOK_HistoryExport-88"><span class="linenos">88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_error_result</span> <span class="o">=</span> <span class="n">process_error_result</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div id="IsOK_HistoryExport.__init__" class="classattr">
                                        <input id="IsOK_HistoryExport.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOK_HistoryExport</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">history</span>, </span><span class="param"><span class="n">process_error_result</span><span class="o">=</span><span class="kc">True</span></span>)</span>

                <label class="view-source-button" for="IsOK_HistoryExport.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_HistoryExport.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_HistoryExport.__init__-85"><a href="#IsOK_HistoryExport.__init__-85"><span class="linenos">85</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">history</span><span class="p">,</span> <span class="n">process_error_result</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IsOK_HistoryExport.__init__-86"><a href="#IsOK_HistoryExport.__init__-86"><span class="linenos">86</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">IsOK_HistoryExport</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="s1">&#39;&#39;</span><span class="p">)</span>
</span><span id="IsOK_HistoryExport.__init__-87"><a href="#IsOK_HistoryExport.__init__-87"><span class="linenos">87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">history</span> <span class="o">=</span> <span class="n">history</span>
</span><span id="IsOK_HistoryExport.__init__-88"><a href="#IsOK_HistoryExport.__init__-88"><span class="linenos">88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">process_error_result</span> <span class="o">=</span> <span class="n">process_error_result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_HistoryExport.history" class="classattr">
                                <div class="attr variable">
            <span class="name">history</span>

        
    </div>
    <a class="headerlink" href="#IsOK_HistoryExport.history"></a>
    
    

                            </div>
                            <div id="IsOK_HistoryExport.process_error_result" class="classattr">
                                <div class="attr variable">
            <span class="name">process_error_result</span>

        
    </div>
    <a class="headerlink" href="#IsOK_HistoryExport.process_error_result"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.BaseException</dt>
                                <dd id="IsOK_HistoryExport.with_traceback" class="function">with_traceback</dd>
                <dd id="IsOK_HistoryExport.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IsOK_IntenalResult">
                            <input id="IsOK_IntenalResult-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_IntenalResult</span>:

                <label class="view-source-button" for="IsOK_IntenalResult-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_IntenalResult"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_IntenalResult-91"><a href="#IsOK_IntenalResult-91"><span class="linenos">91</span></a><span class="k">class</span> <span class="nc">IsOK_IntenalResult</span><span class="p">:</span>
</span><span id="IsOK_IntenalResult-92"><a href="#IsOK_IntenalResult-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">str_data</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="IsOK_IntenalResult-93"><a href="#IsOK_IntenalResult-93"><span class="linenos">93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="IsOK_IntenalResult-94"><a href="#IsOK_IntenalResult-94"><span class="linenos">94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">str_data</span> <span class="o">=</span> <span class="n">str_data</span>
</span><span id="IsOK_IntenalResult-95"><a href="#IsOK_IntenalResult-95"><span class="linenos">95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span>
</span><span id="IsOK_IntenalResult-96"><a href="#IsOK_IntenalResult-96"><span class="linenos">96</span></a>
</span><span id="IsOK_IntenalResult-97"><a href="#IsOK_IntenalResult-97"><span class="linenos">97</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_IntenalResult-98"><a href="#IsOK_IntenalResult-98"><span class="linenos">98</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">str_data</span>
</span></pre></div>


    

                            <div id="IsOK_IntenalResult.__init__" class="classattr">
                                        <input id="IsOK_IntenalResult.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOK_IntenalResult</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">type_id</span>, </span><span class="param"><span class="n">str_data</span>, </span><span class="param"><span class="n">data</span></span>)</span>

                <label class="view-source-button" for="IsOK_IntenalResult.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_IntenalResult.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_IntenalResult.__init__-92"><a href="#IsOK_IntenalResult.__init__-92"><span class="linenos">92</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">type_id</span><span class="p">,</span> <span class="n">str_data</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="IsOK_IntenalResult.__init__-93"><a href="#IsOK_IntenalResult.__init__-93"><span class="linenos">93</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">type_id</span> <span class="o">=</span> <span class="n">type_id</span>
</span><span id="IsOK_IntenalResult.__init__-94"><a href="#IsOK_IntenalResult.__init__-94"><span class="linenos">94</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">str_data</span> <span class="o">=</span> <span class="n">str_data</span>
</span><span id="IsOK_IntenalResult.__init__-95"><a href="#IsOK_IntenalResult.__init__-95"><span class="linenos">95</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">data</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_IntenalResult.type_id" class="classattr">
                                <div class="attr variable">
            <span class="name">type_id</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResult.type_id"></a>
    
    

                            </div>
                            <div id="IsOK_IntenalResult.str_data" class="classattr">
                                <div class="attr variable">
            <span class="name">str_data</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResult.str_data"></a>
    
    

                            </div>
                            <div id="IsOK_IntenalResult.data" class="classattr">
                                <div class="attr variable">
            <span class="name">data</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResult.data"></a>
    
    

                            </div>
                </section>
                <section id="IsOK_IntenalResultType">
                            <input id="IsOK_IntenalResultType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_IntenalResultType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="IsOK_IntenalResultType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_IntenalResultType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_IntenalResultType-101"><a href="#IsOK_IntenalResultType-101"><span class="linenos">101</span></a><span class="k">class</span> <span class="nc">IsOK_IntenalResultType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="IsOK_IntenalResultType-102"><a href="#IsOK_IntenalResultType-102"><span class="linenos">102</span></a><span class="c1"># class CriteriaType():  # much more efficient than Enum inheritance</span>
</span><span id="IsOK_IntenalResultType-103"><a href="#IsOK_IntenalResultType-103"><span class="linenos">103</span></a>    <span class="n">built_in_exception__is_ok_block_failed</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="IsOK_IntenalResultType-104"><a href="#IsOK_IntenalResultType-104"><span class="linenos">104</span></a>    <span class="n">built_in_exception__bad_history_import</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="IsOK_IntenalResultType-105"><a href="#IsOK_IntenalResultType-105"><span class="linenos">105</span></a>    <span class="n">external_exception</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="IsOK_IntenalResultType-106"><a href="#IsOK_IntenalResultType-106"><span class="linenos">106</span></a>    <span class="n">block_did_not_returned_an_answer</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="IsOK_IntenalResultType.built_in_exception__is_ok_block_failed" class="classattr">
                                <div class="attr variable">
            <span class="name">built_in_exception__is_ok_block_failed</span>        =
<span class="default_value">&lt;<a href="#IsOK_IntenalResultType.built_in_exception__is_ok_block_failed">IsOK_IntenalResultType.built_in_exception__is_ok_block_failed</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResultType.built_in_exception__is_ok_block_failed"></a>
    
    

                            </div>
                            <div id="IsOK_IntenalResultType.built_in_exception__bad_history_import" class="classattr">
                                <div class="attr variable">
            <span class="name">built_in_exception__bad_history_import</span>        =
<span class="default_value">&lt;<a href="#IsOK_IntenalResultType.built_in_exception__bad_history_import">IsOK_IntenalResultType.built_in_exception__bad_history_import</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResultType.built_in_exception__bad_history_import"></a>
    
    

                            </div>
                            <div id="IsOK_IntenalResultType.external_exception" class="classattr">
                                <div class="attr variable">
            <span class="name">external_exception</span>        =
<span class="default_value">&lt;<a href="#IsOK_IntenalResultType.external_exception">IsOK_IntenalResultType.external_exception</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResultType.external_exception"></a>
    
    

                            </div>
                            <div id="IsOK_IntenalResultType.block_did_not_returned_an_answer" class="classattr">
                                <div class="attr variable">
            <span class="name">block_did_not_returned_an_answer</span>        =
<span class="default_value">&lt;<a href="#IsOK_IntenalResultType.block_did_not_returned_an_answer">IsOK_IntenalResultType.block_did_not_returned_an_answer</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#IsOK_IntenalResultType.block_did_not_returned_an_answer"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="IsOK_IntenalResultType.name" class="variable">name</dd>
                <dd id="IsOK_IntenalResultType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IsOK_ContextHolder">
                            <input id="IsOK_ContextHolder-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOK_ContextHolder</span>:

                <label class="view-source-button" for="IsOK_ContextHolder-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder-109"><a href="#IsOK_ContextHolder-109"><span class="linenos">109</span></a><span class="k">class</span> <span class="nc">IsOK_ContextHolder</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-110"><a href="#IsOK_ContextHolder-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context_holder_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">global_block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOK_ContextHolder-111"><a href="#IsOK_ContextHolder-111"><span class="linenos">111</span></a>                 <span class="n">raise_exceptions</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">save_debug_trace</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">closeable</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-112"><a href="#IsOK_ContextHolder-112"><span class="linenos">112</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IsOK_ContextHolder-113"><a href="#IsOK_ContextHolder-113"><span class="linenos">113</span></a>
</span><span id="IsOK_ContextHolder-114"><a href="#IsOK_ContextHolder-114"><span class="linenos">114</span></a><span class="sd">        :param context_holder_id:</span>
</span><span id="IsOK_ContextHolder-115"><a href="#IsOK_ContextHolder-115"><span class="linenos">115</span></a><span class="sd">        :param context_holder_info:</span>
</span><span id="IsOK_ContextHolder-116"><a href="#IsOK_ContextHolder-116"><span class="linenos">116</span></a><span class="sd">        :param global_block_results_criteria: will be set to ResultType(CriteriaType.optional, set()) if None;</span>
</span><span id="IsOK_ContextHolder-117"><a href="#IsOK_ContextHolder-117"><span class="linenos">117</span></a><span class="sd">            in this case all blocks are required.</span>
</span><span id="IsOK_ContextHolder-118"><a href="#IsOK_ContextHolder-118"><span class="linenos">118</span></a><span class="sd">        :param raise_exceptions:</span>
</span><span id="IsOK_ContextHolder-119"><a href="#IsOK_ContextHolder-119"><span class="linenos">119</span></a><span class="sd">        :param save_debug_trace:</span>
</span><span id="IsOK_ContextHolder-120"><a href="#IsOK_ContextHolder-120"><span class="linenos">120</span></a><span class="sd">        :param closeable:</span>
</span><span id="IsOK_ContextHolder-121"><a href="#IsOK_ContextHolder-121"><span class="linenos">121</span></a><span class="sd">        :return:</span>
</span><span id="IsOK_ContextHolder-122"><a href="#IsOK_ContextHolder-122"><span class="linenos">122</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IsOK_ContextHolder-123"><a href="#IsOK_ContextHolder-123"><span class="linenos">123</span></a>        <span class="c1"># Use only ResultType(CriteriaType.optional, ...) or ResultType(CriteriaType.needed, set()).</span>
</span><span id="IsOK_ContextHolder-124"><a href="#IsOK_ContextHolder-124"><span class="linenos">124</span></a>        <span class="c1"># Other will be ignored here.</span>
</span><span id="IsOK_ContextHolder-125"><a href="#IsOK_ContextHolder-125"><span class="linenos">125</span></a>        <span class="c1"># You may use global_block_results_criteria=ResultType(CriteriaType.optional, set()) to create criteria</span>
</span><span id="IsOK_ContextHolder-126"><a href="#IsOK_ContextHolder-126"><span class="linenos">126</span></a>        <span class="c1"># &quot;no fails in any block&quot;</span>
</span><span id="IsOK_ContextHolder-127"><a href="#IsOK_ContextHolder-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_id</span> <span class="o">=</span> <span class="n">context_holder_id</span>
</span><span id="IsOK_ContextHolder-128"><a href="#IsOK_ContextHolder-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_info</span> <span class="o">=</span> <span class="n">context_holder_info</span>
</span><span id="IsOK_ContextHolder-129"><a href="#IsOK_ContextHolder-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-130"><a href="#IsOK_ContextHolder-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_reserve_block_id_generator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">(</span><span class="n">GeneratorType</span><span class="o">.</span><span class="n">guid_string</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-131"><a href="#IsOK_ContextHolder-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-132"><a href="#IsOK_ContextHolder-132"><span class="linenos">132</span></a>        <span class="n">global_block_results_criteria</span> <span class="o">=</span> <span class="n">global_block_results_criteria</span> <span class="ow">or</span> <span class="n">ResultType</span><span class="p">(</span><span class="n">CriteriaType</span><span class="o">.</span><span class="n">optional</span><span class="p">,</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="IsOK_ContextHolder-133"><a href="#IsOK_ContextHolder-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="n">global_block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-134"><a href="#IsOK_ContextHolder-134"><span class="linenos">134</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">global_block_results_criteria</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-135"><a href="#IsOK_ContextHolder-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_raise_exceptions</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="IsOK_ContextHolder-136"><a href="#IsOK_ContextHolder-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_save_debug_trace</span> <span class="o">=</span> <span class="n">save_debug_trace</span>
</span><span id="IsOK_ContextHolder-137"><a href="#IsOK_ContextHolder-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closeable</span> <span class="o">=</span> <span class="n">closeable</span>
</span><span id="IsOK_ContextHolder-138"><a href="#IsOK_ContextHolder-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-139"><a href="#IsOK_ContextHolder-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-140"><a href="#IsOK_ContextHolder-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_all_made_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-141"><a href="#IsOK_ContextHolder-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-142"><a href="#IsOK_ContextHolder-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-143"><a href="#IsOK_ContextHolder-143"><span class="linenos">143</span></a>
</span><span id="IsOK_ContextHolder-144"><a href="#IsOK_ContextHolder-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-145"><a href="#IsOK_ContextHolder-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-146"><a href="#IsOK_ContextHolder-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-147"><a href="#IsOK_ContextHolder-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-148"><a href="#IsOK_ContextHolder-148"><span class="linenos">148</span></a>
</span><span id="IsOK_ContextHolder-149"><a href="#IsOK_ContextHolder-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-150"><a href="#IsOK_ContextHolder-150"><span class="linenos">150</span></a>
</span><span id="IsOK_ContextHolder-151"><a href="#IsOK_ContextHolder-151"><span class="linenos">151</span></a>    <span class="c1"># def _push_criteria(self, set_of_needed_blocks=None, set_of_optional_blocks=None):</span>
</span><span id="IsOK_ContextHolder-152"><a href="#IsOK_ContextHolder-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">_push_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-153"><a href="#IsOK_ContextHolder-153"><span class="linenos">153</span></a>        <span class="c1"># Do not use!</span>
</span><span id="IsOK_ContextHolder-154"><a href="#IsOK_ContextHolder-154"><span class="linenos">154</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-155"><a href="#IsOK_ContextHolder-155"><span class="linenos">155</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-156"><a href="#IsOK_ContextHolder-156"><span class="linenos">156</span></a>
</span><span id="IsOK_ContextHolder-157"><a href="#IsOK_ContextHolder-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">_pop_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-158"><a href="#IsOK_ContextHolder-158"><span class="linenos">158</span></a>        <span class="c1"># Do not use!</span>
</span><span id="IsOK_ContextHolder-159"><a href="#IsOK_ContextHolder-159"><span class="linenos">159</span></a>        <span class="c1"># May raise exception if len(self.criteria_list)==0, but this is OK.</span>
</span><span id="IsOK_ContextHolder-160"><a href="#IsOK_ContextHolder-160"><span class="linenos">160</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-161"><a href="#IsOK_ContextHolder-161"><span class="linenos">161</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-162"><a href="#IsOK_ContextHolder-162"><span class="linenos">162</span></a>
</span><span id="IsOK_ContextHolder-163"><a href="#IsOK_ContextHolder-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">read_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-164"><a href="#IsOK_ContextHolder-164"><span class="linenos">164</span></a>        <span class="n">criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-165"><a href="#IsOK_ContextHolder-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-166"><a href="#IsOK_ContextHolder-166"><span class="linenos">166</span></a>            <span class="n">criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder-167"><a href="#IsOK_ContextHolder-167"><span class="linenos">167</span></a>        <span class="k">return</span> <span class="n">criteria</span>
</span><span id="IsOK_ContextHolder-168"><a href="#IsOK_ContextHolder-168"><span class="linenos">168</span></a>
</span><span id="IsOK_ContextHolder-169"><a href="#IsOK_ContextHolder-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">_push_block_info</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-170"><a href="#IsOK_ContextHolder-170"><span class="linenos">170</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="n">block_id</span>
</span><span id="IsOK_ContextHolder-171"><a href="#IsOK_ContextHolder-171"><span class="linenos">171</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="n">block_info</span>
</span><span id="IsOK_ContextHolder-172"><a href="#IsOK_ContextHolder-172"><span class="linenos">172</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-173"><a href="#IsOK_ContextHolder-173"><span class="linenos">173</span></a>
</span><span id="IsOK_ContextHolder-174"><a href="#IsOK_ContextHolder-174"><span class="linenos">174</span></a>    <span class="k">def</span> <span class="nf">_pop_block_info</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-175"><a href="#IsOK_ContextHolder-175"><span class="linenos">175</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-176"><a href="#IsOK_ContextHolder-176"><span class="linenos">176</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-177"><a href="#IsOK_ContextHolder-177"><span class="linenos">177</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder-178"><a href="#IsOK_ContextHolder-178"><span class="linenos">178</span></a>
</span><span id="IsOK_ContextHolder-179"><a href="#IsOK_ContextHolder-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">push_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-180"><a href="#IsOK_ContextHolder-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-181"><a href="#IsOK_ContextHolder-181"><span class="linenos">181</span></a>
</span><span id="IsOK_ContextHolder-182"><a href="#IsOK_ContextHolder-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">push_result_c</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-183"><a href="#IsOK_ContextHolder-183"><span class="linenos">183</span></a>        <span class="c1"># &quot;class&quot; version: to use when result = ResultExistence()</span>
</span><span id="IsOK_ContextHolder-184"><a href="#IsOK_ContextHolder-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-185"><a href="#IsOK_ContextHolder-185"><span class="linenos">185</span></a>
</span><span id="IsOK_ContextHolder-186"><a href="#IsOK_ContextHolder-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">read_block_result_link</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-187"><a href="#IsOK_ContextHolder-187"><span class="linenos">187</span></a>        <span class="c1"># result is NOT protected from changing!</span>
</span><span id="IsOK_ContextHolder-188"><a href="#IsOK_ContextHolder-188"><span class="linenos">188</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder-189"><a href="#IsOK_ContextHolder-189"><span class="linenos">189</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="IsOK_ContextHolder-190"><a href="#IsOK_ContextHolder-190"><span class="linenos">190</span></a>        <span class="c1"># result = self._blocks_library[block_id][3]</span>
</span><span id="IsOK_ContextHolder-191"><a href="#IsOK_ContextHolder-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="IsOK_ContextHolder-192"><a href="#IsOK_ContextHolder-192"><span class="linenos">192</span></a>
</span><span id="IsOK_ContextHolder-193"><a href="#IsOK_ContextHolder-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">read_block_result_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-194"><a href="#IsOK_ContextHolder-194"><span class="linenos">194</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder-195"><a href="#IsOK_ContextHolder-195"><span class="linenos">195</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="IsOK_ContextHolder-196"><a href="#IsOK_ContextHolder-196"><span class="linenos">196</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="IsOK_ContextHolder-197"><a href="#IsOK_ContextHolder-197"><span class="linenos">197</span></a>
</span><span id="IsOK_ContextHolder-198"><a href="#IsOK_ContextHolder-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="nf">read_block_result_deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-199"><a href="#IsOK_ContextHolder-199"><span class="linenos">199</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder-200"><a href="#IsOK_ContextHolder-200"><span class="linenos">200</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="IsOK_ContextHolder-201"><a href="#IsOK_ContextHolder-201"><span class="linenos">201</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="IsOK_ContextHolder-202"><a href="#IsOK_ContextHolder-202"><span class="linenos">202</span></a>
</span><span id="IsOK_ContextHolder-203"><a href="#IsOK_ContextHolder-203"><span class="linenos">203</span></a>    <span class="k">def</span> <span class="nf">_save_block_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-204"><a href="#IsOK_ContextHolder-204"><span class="linenos">204</span></a>        <span class="c1"># ignore_block_result_criteria = ignore_block_result_criteria or IgnoreBlockResultCriteriaType.do_not_ignore</span>
</span><span id="IsOK_ContextHolder-205"><a href="#IsOK_ContextHolder-205"><span class="linenos">205</span></a>        <span class="k">if</span> <span class="p">((</span><span class="n">IgnoreBlockResultCriteriaType</span><span class="o">.</span><span class="n">ignore_if_failed</span> <span class="o">==</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="ow">and</span>
</span><span id="IsOK_ContextHolder-206"><a href="#IsOK_ContextHolder-206"><span class="linenos">206</span></a>                <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span> \
</span><span id="IsOK_ContextHolder-207"><a href="#IsOK_ContextHolder-207"><span class="linenos">207</span></a>                <span class="ow">or</span> <span class="p">((</span><span class="n">IgnoreBlockResultCriteriaType</span><span class="o">.</span><span class="n">ignore_if_successful</span> <span class="o">==</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="ow">and</span>
</span><span id="IsOK_ContextHolder-208"><a href="#IsOK_ContextHolder-208"><span class="linenos">208</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
</span><span id="IsOK_ContextHolder-209"><a href="#IsOK_ContextHolder-209"><span class="linenos">209</span></a>            <span class="k">return</span>
</span><span id="IsOK_ContextHolder-210"><a href="#IsOK_ContextHolder-210"><span class="linenos">210</span></a>
</span><span id="IsOK_ContextHolder-211"><a href="#IsOK_ContextHolder-211"><span class="linenos">211</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-212"><a href="#IsOK_ContextHolder-212"><span class="linenos">212</span></a>        <span class="n">import_depth</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="IsOK_ContextHolder-213"><a href="#IsOK_ContextHolder-213"><span class="linenos">213</span></a>        <span class="n">full_block_info</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span><span class="p">,</span>
</span><span id="IsOK_ContextHolder-214"><a href="#IsOK_ContextHolder-214"><span class="linenos">214</span></a>                           <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">,</span> <span class="n">import_depth</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-215"><a href="#IsOK_ContextHolder-215"><span class="linenos">215</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">full_block_info</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-216"><a href="#IsOK_ContextHolder-216"><span class="linenos">216</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">]</span> <span class="o">=</span> <span class="n">full_block_info</span>
</span><span id="IsOK_ContextHolder-217"><a href="#IsOK_ContextHolder-217"><span class="linenos">217</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_all_made_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-218"><a href="#IsOK_ContextHolder-218"><span class="linenos">218</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="IsOK_ContextHolder-219"><a href="#IsOK_ContextHolder-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-220"><a href="#IsOK_ContextHolder-220"><span class="linenos">220</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-221"><a href="#IsOK_ContextHolder-221"><span class="linenos">221</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-222"><a href="#IsOK_ContextHolder-222"><span class="linenos">222</span></a>
</span><span id="IsOK_ContextHolder-223"><a href="#IsOK_ContextHolder-223"><span class="linenos">223</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-224"><a href="#IsOK_ContextHolder-224"><span class="linenos">224</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-225"><a href="#IsOK_ContextHolder-225"><span class="linenos">225</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="o">.</span><span class="n">get</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-226"><a href="#IsOK_ContextHolder-226"><span class="linenos">226</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-227"><a href="#IsOK_ContextHolder-227"><span class="linenos">227</span></a>            <span class="n">current_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_criteria</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-228"><a href="#IsOK_ContextHolder-228"><span class="linenos">228</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="IsOK_ContextHolder-229"><a href="#IsOK_ContextHolder-229"><span class="linenos">229</span></a>            <span class="k">if</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">needed</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-230"><a href="#IsOK_ContextHolder-230"><span class="linenos">230</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-231"><a href="#IsOK_ContextHolder-231"><span class="linenos">231</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-232"><a href="#IsOK_ContextHolder-232"><span class="linenos">232</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">optional</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-233"><a href="#IsOK_ContextHolder-233"><span class="linenos">233</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span> <span class="o">-</span> <span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-234"><a href="#IsOK_ContextHolder-234"><span class="linenos">234</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-235"><a href="#IsOK_ContextHolder-235"><span class="linenos">235</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">any</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-236"><a href="#IsOK_ContextHolder-236"><span class="linenos">236</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="IsOK_ContextHolder-237"><a href="#IsOK_ContextHolder-237"><span class="linenos">237</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">forbidden</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-238"><a href="#IsOK_ContextHolder-238"><span class="linenos">238</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-239"><a href="#IsOK_ContextHolder-239"><span class="linenos">239</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-240"><a href="#IsOK_ContextHolder-240"><span class="linenos">240</span></a>            <span class="k">elif</span> <span class="n">CriteriaType</span><span class="o">.</span><span class="n">not_successful</span> <span class="o">==</span> <span class="n">current_criteria</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-241"><a href="#IsOK_ContextHolder-241"><span class="linenos">241</span></a>                <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">current_criteria</span><span class="o">.</span><span class="n">result</span> <span class="o">&amp;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-242"><a href="#IsOK_ContextHolder-242"><span class="linenos">242</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-243"><a href="#IsOK_ContextHolder-243"><span class="linenos">243</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-244"><a href="#IsOK_ContextHolder-244"><span class="linenos">244</span></a>            <span class="k">return</span> <span class="n">result</span>
</span><span id="IsOK_ContextHolder-245"><a href="#IsOK_ContextHolder-245"><span class="linenos">245</span></a>
</span><span id="IsOK_ContextHolder-246"><a href="#IsOK_ContextHolder-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-247"><a href="#IsOK_ContextHolder-247"><span class="linenos">247</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__bool__</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-248"><a href="#IsOK_ContextHolder-248"><span class="linenos">248</span></a>
</span><span id="IsOK_ContextHolder-249"><a href="#IsOK_ContextHolder-249"><span class="linenos">249</span></a>    <span class="nd">@staticmethod</span>
</span><span id="IsOK_ContextHolder-250"><a href="#IsOK_ContextHolder-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="nf">_block_list_to_str</span><span class="p">(</span><span class="n">block_list</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-251"><a href="#IsOK_ContextHolder-251"><span class="linenos">251</span></a>        <span class="n">blocks_str</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s1">&#39;(index(</span><span class="si">{}</span><span class="s1">), depth(</span><span class="si">{}</span><span class="s1">), ID(</span><span class="si">{}</span><span class="s1">), INFO(</span><span class="si">{}</span><span class="s1">), RESULT(</span><span class="si">{}</span><span class="s1">))&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
</span><span id="IsOK_ContextHolder-252"><a href="#IsOK_ContextHolder-252"><span class="linenos">252</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">4</span><span class="p">]),</span>
</span><span id="IsOK_ContextHolder-253"><a href="#IsOK_ContextHolder-253"><span class="linenos">253</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
</span><span id="IsOK_ContextHolder-254"><a href="#IsOK_ContextHolder-254"><span class="linenos">254</span></a>                                                                                              <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span>
</span><span id="IsOK_ContextHolder-255"><a href="#IsOK_ContextHolder-255"><span class="linenos">255</span></a>                                                          <span class="s1">&#39;(</span><span class="si">{}</span><span class="s1">, </span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">str</span><span class="p">(</span><span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">1</span><span class="p">])))</span>
</span><span id="IsOK_ContextHolder-256"><a href="#IsOK_ContextHolder-256"><span class="linenos">256</span></a>                                <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="n">block_list</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-257"><a href="#IsOK_ContextHolder-257"><span class="linenos">257</span></a>        <span class="k">return</span> <span class="n">blocks_str</span>
</span><span id="IsOK_ContextHolder-258"><a href="#IsOK_ContextHolder-258"><span class="linenos">258</span></a>
</span><span id="IsOK_ContextHolder-259"><a href="#IsOK_ContextHolder-259"><span class="linenos">259</span></a>    <span class="k">def</span> <span class="nf">_block_str_to_context_holder_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">blocks_str</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-260"><a href="#IsOK_ContextHolder-260"><span class="linenos">260</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="s1">&#39;{{{{CONTEXT_HOLDER_ID(</span><span class="si">{}</span><span class="s1">): CONTEXT_HOLDER_INFO(</span><span class="si">{}</span><span class="s1">)}}:[</span><span class="se">\n</span><span class="si">{}</span><span class="se">\n</span><span class="s1">]}}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
</span><span id="IsOK_ContextHolder-261"><a href="#IsOK_ContextHolder-261"><span class="linenos">261</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_id</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_info</span><span class="p">,</span> <span class="n">blocks_str</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-262"><a href="#IsOK_ContextHolder-262"><span class="linenos">262</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="IsOK_ContextHolder-263"><a href="#IsOK_ContextHolder-263"><span class="linenos">263</span></a>
</span><span id="IsOK_ContextHolder-264"><a href="#IsOK_ContextHolder-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-265"><a href="#IsOK_ContextHolder-265"><span class="linenos">265</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-266"><a href="#IsOK_ContextHolder-266"><span class="linenos">266</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-267"><a href="#IsOK_ContextHolder-267"><span class="linenos">267</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="IsOK_ContextHolder-268"><a href="#IsOK_ContextHolder-268"><span class="linenos">268</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-269"><a href="#IsOK_ContextHolder-269"><span class="linenos">269</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="IsOK_ContextHolder-270"><a href="#IsOK_ContextHolder-270"><span class="linenos">270</span></a>
</span><span id="IsOK_ContextHolder-271"><a href="#IsOK_ContextHolder-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-272"><a href="#IsOK_ContextHolder-272"><span class="linenos">272</span></a>        <span class="n">bad_blocks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder-273"><a href="#IsOK_ContextHolder-273"><span class="linenos">273</span></a>        <span class="n">full_history_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_list_to_str</span><span class="p">(</span><span class="n">bad_blocks</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-274"><a href="#IsOK_ContextHolder-274"><span class="linenos">274</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_str_to_context_holder_str</span><span class="p">(</span><span class="n">full_history_str</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-275"><a href="#IsOK_ContextHolder-275"><span class="linenos">275</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="IsOK_ContextHolder-276"><a href="#IsOK_ContextHolder-276"><span class="linenos">276</span></a>
</span><span id="IsOK_ContextHolder-277"><a href="#IsOK_ContextHolder-277"><span class="linenos">277</span></a>    <span class="k">def</span> <span class="nf">raise_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-278"><a href="#IsOK_ContextHolder-278"><span class="linenos">278</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">())</span>
</span><span id="IsOK_ContextHolder-279"><a href="#IsOK_ContextHolder-279"><span class="linenos">279</span></a>
</span><span id="IsOK_ContextHolder-280"><a href="#IsOK_ContextHolder-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">raise_full_history</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-281"><a href="#IsOK_ContextHolder-281"><span class="linenos">281</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-282"><a href="#IsOK_ContextHolder-282"><span class="linenos">282</span></a>
</span><span id="IsOK_ContextHolder-283"><a href="#IsOK_ContextHolder-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="nf">process_history_import</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">his_ex</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-284"><a href="#IsOK_ContextHolder-284"><span class="linenos">284</span></a>        <span class="n">history</span> <span class="o">=</span> <span class="n">his_ex</span><span class="o">.</span><span class="n">history</span>
</span><span id="IsOK_ContextHolder-285"><a href="#IsOK_ContextHolder-285"><span class="linenos">285</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="n">history</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder-286"><a href="#IsOK_ContextHolder-286"><span class="linenos">286</span></a>            <span class="n">full_block_info</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span><span class="o">.</span><span class="n">get_new_ID</span><span class="p">(),</span> <span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="IsOK_ContextHolder-287"><a href="#IsOK_ContextHolder-287"><span class="linenos">287</span></a>                               <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-288"><a href="#IsOK_ContextHolder-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">full_block_info</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-289"><a href="#IsOK_ContextHolder-289"><span class="linenos">289</span></a>
</span><span id="IsOK_ContextHolder-290"><a href="#IsOK_ContextHolder-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-291"><a href="#IsOK_ContextHolder-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="IsOK_ContextHolder-292"><a href="#IsOK_ContextHolder-292"><span class="linenos">292</span></a>
</span><span id="IsOK_ContextHolder-293"><a href="#IsOK_ContextHolder-293"><span class="linenos">293</span></a>    <span class="k">def</span> <span class="nf">_reopen</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-294"><a href="#IsOK_ContextHolder-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder-295"><a href="#IsOK_ContextHolder-295"><span class="linenos">295</span></a>
</span><span id="IsOK_ContextHolder-296"><a href="#IsOK_ContextHolder-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-297"><a href="#IsOK_ContextHolder-297"><span class="linenos">297</span></a>        <span class="n">full_history_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_list_to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-298"><a href="#IsOK_ContextHolder-298"><span class="linenos">298</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_str_to_context_holder_str</span><span class="p">(</span><span class="n">full_history_str</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-299"><a href="#IsOK_ContextHolder-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span><span id="IsOK_ContextHolder-300"><a href="#IsOK_ContextHolder-300"><span class="linenos">300</span></a>
</span><span id="IsOK_ContextHolder-301"><a href="#IsOK_ContextHolder-301"><span class="linenos">301</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-302"><a href="#IsOK_ContextHolder-302"><span class="linenos">302</span></a>        <span class="k">return</span> <span class="n">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder-303"><a href="#IsOK_ContextHolder-303"><span class="linenos">303</span></a>
</span><span id="IsOK_ContextHolder-304"><a href="#IsOK_ContextHolder-304"><span class="linenos">304</span></a>    <span class="k">def</span> <span class="nf">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder-305"><a href="#IsOK_ContextHolder-305"><span class="linenos">305</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="IsOK_ContextHolder.__init__" class="classattr">
                                        <input id="IsOK_ContextHolder.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOK_ContextHolder</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context_holder_id</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">context_holder_info</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">global_block_results_criteria</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">save_debug_trace</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">closeable</span><span class="o">=</span><span class="kc">True</span></span>)</span>

                <label class="view-source-button" for="IsOK_ContextHolder.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.__init__-110"><a href="#IsOK_ContextHolder.__init__-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">context_holder_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">global_block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOK_ContextHolder.__init__-111"><a href="#IsOK_ContextHolder.__init__-111"><span class="linenos">111</span></a>                 <span class="n">raise_exceptions</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">save_debug_trace</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">closeable</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.__init__-112"><a href="#IsOK_ContextHolder.__init__-112"><span class="linenos">112</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="IsOK_ContextHolder.__init__-113"><a href="#IsOK_ContextHolder.__init__-113"><span class="linenos">113</span></a>
</span><span id="IsOK_ContextHolder.__init__-114"><a href="#IsOK_ContextHolder.__init__-114"><span class="linenos">114</span></a><span class="sd">        :param context_holder_id:</span>
</span><span id="IsOK_ContextHolder.__init__-115"><a href="#IsOK_ContextHolder.__init__-115"><span class="linenos">115</span></a><span class="sd">        :param context_holder_info:</span>
</span><span id="IsOK_ContextHolder.__init__-116"><a href="#IsOK_ContextHolder.__init__-116"><span class="linenos">116</span></a><span class="sd">        :param global_block_results_criteria: will be set to ResultType(CriteriaType.optional, set()) if None;</span>
</span><span id="IsOK_ContextHolder.__init__-117"><a href="#IsOK_ContextHolder.__init__-117"><span class="linenos">117</span></a><span class="sd">            in this case all blocks are required.</span>
</span><span id="IsOK_ContextHolder.__init__-118"><a href="#IsOK_ContextHolder.__init__-118"><span class="linenos">118</span></a><span class="sd">        :param raise_exceptions:</span>
</span><span id="IsOK_ContextHolder.__init__-119"><a href="#IsOK_ContextHolder.__init__-119"><span class="linenos">119</span></a><span class="sd">        :param save_debug_trace:</span>
</span><span id="IsOK_ContextHolder.__init__-120"><a href="#IsOK_ContextHolder.__init__-120"><span class="linenos">120</span></a><span class="sd">        :param closeable:</span>
</span><span id="IsOK_ContextHolder.__init__-121"><a href="#IsOK_ContextHolder.__init__-121"><span class="linenos">121</span></a><span class="sd">        :return:</span>
</span><span id="IsOK_ContextHolder.__init__-122"><a href="#IsOK_ContextHolder.__init__-122"><span class="linenos">122</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="IsOK_ContextHolder.__init__-123"><a href="#IsOK_ContextHolder.__init__-123"><span class="linenos">123</span></a>        <span class="c1"># Use only ResultType(CriteriaType.optional, ...) or ResultType(CriteriaType.needed, set()).</span>
</span><span id="IsOK_ContextHolder.__init__-124"><a href="#IsOK_ContextHolder.__init__-124"><span class="linenos">124</span></a>        <span class="c1"># Other will be ignored here.</span>
</span><span id="IsOK_ContextHolder.__init__-125"><a href="#IsOK_ContextHolder.__init__-125"><span class="linenos">125</span></a>        <span class="c1"># You may use global_block_results_criteria=ResultType(CriteriaType.optional, set()) to create criteria</span>
</span><span id="IsOK_ContextHolder.__init__-126"><a href="#IsOK_ContextHolder.__init__-126"><span class="linenos">126</span></a>        <span class="c1"># &quot;no fails in any block&quot;</span>
</span><span id="IsOK_ContextHolder.__init__-127"><a href="#IsOK_ContextHolder.__init__-127"><span class="linenos">127</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_id</span> <span class="o">=</span> <span class="n">context_holder_id</span>
</span><span id="IsOK_ContextHolder.__init__-128"><a href="#IsOK_ContextHolder.__init__-128"><span class="linenos">128</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_context_holder_info</span> <span class="o">=</span> <span class="n">context_holder_info</span>
</span><span id="IsOK_ContextHolder.__init__-129"><a href="#IsOK_ContextHolder.__init__-129"><span class="linenos">129</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-130"><a href="#IsOK_ContextHolder.__init__-130"><span class="linenos">130</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_reserve_block_id_generator</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">(</span><span class="n">GeneratorType</span><span class="o">.</span><span class="n">guid_string</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.__init__-131"><a href="#IsOK_ContextHolder.__init__-131"><span class="linenos">131</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-132"><a href="#IsOK_ContextHolder.__init__-132"><span class="linenos">132</span></a>        <span class="n">global_block_results_criteria</span> <span class="o">=</span> <span class="n">global_block_results_criteria</span> <span class="ow">or</span> <span class="n">ResultType</span><span class="p">(</span><span class="n">CriteriaType</span><span class="o">.</span><span class="n">optional</span><span class="p">,</span> <span class="nb">set</span><span class="p">())</span>
</span><span id="IsOK_ContextHolder.__init__-133"><a href="#IsOK_ContextHolder.__init__-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="n">global_block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder.__init__-134"><a href="#IsOK_ContextHolder.__init__-134"><span class="linenos">134</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">global_block_results_criteria</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.__init__-135"><a href="#IsOK_ContextHolder.__init__-135"><span class="linenos">135</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_raise_exceptions</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="IsOK_ContextHolder.__init__-136"><a href="#IsOK_ContextHolder.__init__-136"><span class="linenos">136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_save_debug_trace</span> <span class="o">=</span> <span class="n">save_debug_trace</span>
</span><span id="IsOK_ContextHolder.__init__-137"><a href="#IsOK_ContextHolder.__init__-137"><span class="linenos">137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closeable</span> <span class="o">=</span> <span class="n">closeable</span>
</span><span id="IsOK_ContextHolder.__init__-138"><a href="#IsOK_ContextHolder.__init__-138"><span class="linenos">138</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-139"><a href="#IsOK_ContextHolder.__init__-139"><span class="linenos">139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-140"><a href="#IsOK_ContextHolder.__init__-140"><span class="linenos">140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_all_made_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-141"><a href="#IsOK_ContextHolder.__init__-141"><span class="linenos">141</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_good_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-142"><a href="#IsOK_ContextHolder.__init__-142"><span class="linenos">142</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bad_blocks</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.__init__-143"><a href="#IsOK_ContextHolder.__init__-143"><span class="linenos">143</span></a>
</span><span id="IsOK_ContextHolder.__init__-144"><a href="#IsOK_ContextHolder.__init__-144"><span class="linenos">144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder.__init__-145"><a href="#IsOK_ContextHolder.__init__-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder.__init__-146"><a href="#IsOK_ContextHolder.__init__-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder.__init__-147"><a href="#IsOK_ContextHolder.__init__-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="IsOK_ContextHolder.__init__-148"><a href="#IsOK_ContextHolder.__init__-148"><span class="linenos">148</span></a>
</span><span id="IsOK_ContextHolder.__init__-149"><a href="#IsOK_ContextHolder.__init__-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bool_result</span> <span class="o">=</span> <span class="n">ResultCache</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>:param context_holder_id:
:param context_holder_info:
:param global_block_results_criteria: will be set to ResultType(<a href="#CriteriaType.optional">CriteriaType.optional</a>, set()) if None;
    in this case all blocks are required.
:param raise_exceptions:
:param save_debug_trace:
:param closeable:
:return:</p>
</div>


                            </div>
                            <div id="IsOK_ContextHolder.read_criteria" class="classattr">
                                        <input id="IsOK_ContextHolder.read_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.read_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.read_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.read_criteria-163"><a href="#IsOK_ContextHolder.read_criteria-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">read_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.read_criteria-164"><a href="#IsOK_ContextHolder.read_criteria-164"><span class="linenos">164</span></a>        <span class="n">criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="IsOK_ContextHolder.read_criteria-165"><a href="#IsOK_ContextHolder.read_criteria-165"><span class="linenos">165</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder.read_criteria-166"><a href="#IsOK_ContextHolder.read_criteria-166"><span class="linenos">166</span></a>            <span class="n">criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_criteria_list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder.read_criteria-167"><a href="#IsOK_ContextHolder.read_criteria-167"><span class="linenos">167</span></a>        <span class="k">return</span> <span class="n">criteria</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.push_result" class="classattr">
                                        <input id="IsOK_ContextHolder.push_result-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">push_result</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">bool_result</span>, </span><span class="param"><span class="n">info_or_data</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.push_result-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.push_result"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.push_result-179"><a href="#IsOK_ContextHolder.push_result-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">push_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.push_result-180"><a href="#IsOK_ContextHolder.push_result-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">bool_result</span><span class="p">,</span> <span class="n">info_or_data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.push_result_c" class="classattr">
                                        <input id="IsOK_ContextHolder.push_result_c-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">push_result_c</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.push_result_c-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.push_result_c"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.push_result_c-182"><a href="#IsOK_ContextHolder.push_result_c-182"><span class="linenos">182</span></a>    <span class="k">def</span> <span class="nf">push_result_c</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.push_result_c-183"><a href="#IsOK_ContextHolder.push_result_c-183"><span class="linenos">183</span></a>        <span class="c1"># &quot;class&quot; version: to use when result = ResultExistence()</span>
</span><span id="IsOK_ContextHolder.push_result_c-184"><a href="#IsOK_ContextHolder.push_result_c-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="o">=</span> <span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">existence</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">result</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.read_block_result_link" class="classattr">
                                        <input id="IsOK_ContextHolder.read_block_result_link-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_block_result_link</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">block_id</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.read_block_result_link-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.read_block_result_link"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.read_block_result_link-186"><a href="#IsOK_ContextHolder.read_block_result_link-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">read_block_result_link</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.read_block_result_link-187"><a href="#IsOK_ContextHolder.read_block_result_link-187"><span class="linenos">187</span></a>        <span class="c1"># result is NOT protected from changing!</span>
</span><span id="IsOK_ContextHolder.read_block_result_link-188"><a href="#IsOK_ContextHolder.read_block_result_link-188"><span class="linenos">188</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder.read_block_result_link-189"><a href="#IsOK_ContextHolder.read_block_result_link-189"><span class="linenos">189</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
</span><span id="IsOK_ContextHolder.read_block_result_link-190"><a href="#IsOK_ContextHolder.read_block_result_link-190"><span class="linenos">190</span></a>        <span class="c1"># result = self._blocks_library[block_id][3]</span>
</span><span id="IsOK_ContextHolder.read_block_result_link-191"><a href="#IsOK_ContextHolder.read_block_result_link-191"><span class="linenos">191</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.read_block_result_copy" class="classattr">
                                        <input id="IsOK_ContextHolder.read_block_result_copy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_block_result_copy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">block_id</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.read_block_result_copy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.read_block_result_copy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.read_block_result_copy-193"><a href="#IsOK_ContextHolder.read_block_result_copy-193"><span class="linenos">193</span></a>    <span class="k">def</span> <span class="nf">read_block_result_copy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.read_block_result_copy-194"><a href="#IsOK_ContextHolder.read_block_result_copy-194"><span class="linenos">194</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder.read_block_result_copy-195"><a href="#IsOK_ContextHolder.read_block_result_copy-195"><span class="linenos">195</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="IsOK_ContextHolder.read_block_result_copy-196"><a href="#IsOK_ContextHolder.read_block_result_copy-196"><span class="linenos">196</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.read_block_result_deepcopy" class="classattr">
                                        <input id="IsOK_ContextHolder.read_block_result_deepcopy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">read_block_result_deepcopy</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">block_id</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.read_block_result_deepcopy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.read_block_result_deepcopy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.read_block_result_deepcopy-198"><a href="#IsOK_ContextHolder.read_block_result_deepcopy-198"><span class="linenos">198</span></a>    <span class="k">def</span> <span class="nf">read_block_result_deepcopy</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.read_block_result_deepcopy-199"><a href="#IsOK_ContextHolder.read_block_result_deepcopy-199"><span class="linenos">199</span></a>        <span class="n">original_result_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_blocks_library</span><span class="p">[</span><span class="n">block_id</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
</span><span id="IsOK_ContextHolder.read_block_result_deepcopy-200"><a href="#IsOK_ContextHolder.read_block_result_deepcopy-200"><span class="linenos">200</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">ResultExistence</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">copy</span><span class="o">.</span><span class="n">deepcopy</span><span class="p">(</span><span class="n">original_result_data</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span>
</span><span id="IsOK_ContextHolder.read_block_result_deepcopy-201"><a href="#IsOK_ContextHolder.read_block_result_deepcopy-201"><span class="linenos">201</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.get_bad_blocks" class="classattr">
                                        <input id="IsOK_ContextHolder.get_bad_blocks-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_bad_blocks</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.get_bad_blocks-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.get_bad_blocks"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.get_bad_blocks-264"><a href="#IsOK_ContextHolder.get_bad_blocks-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks-265"><a href="#IsOK_ContextHolder.get_bad_blocks-265"><span class="linenos">265</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks-266"><a href="#IsOK_ContextHolder.get_bad_blocks-266"><span class="linenos">266</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks-267"><a href="#IsOK_ContextHolder.get_bad_blocks-267"><span class="linenos">267</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]:</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks-268"><a href="#IsOK_ContextHolder.get_bad_blocks-268"><span class="linenos">268</span></a>                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks-269"><a href="#IsOK_ContextHolder.get_bad_blocks-269"><span class="linenos">269</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.get_bad_blocks_str" class="classattr">
                                        <input id="IsOK_ContextHolder.get_bad_blocks_str-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_bad_blocks_str</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.get_bad_blocks_str-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.get_bad_blocks_str"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.get_bad_blocks_str-271"><a href="#IsOK_ContextHolder.get_bad_blocks_str-271"><span class="linenos">271</span></a>    <span class="k">def</span> <span class="nf">get_bad_blocks_str</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks_str-272"><a href="#IsOK_ContextHolder.get_bad_blocks_str-272"><span class="linenos">272</span></a>        <span class="n">bad_blocks</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">()</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks_str-273"><a href="#IsOK_ContextHolder.get_bad_blocks_str-273"><span class="linenos">273</span></a>        <span class="n">full_history_str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_list_to_str</span><span class="p">(</span><span class="n">bad_blocks</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks_str-274"><a href="#IsOK_ContextHolder.get_bad_blocks_str-274"><span class="linenos">274</span></a>        <span class="n">full_string</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_block_str_to_context_holder_str</span><span class="p">(</span><span class="n">full_history_str</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.get_bad_blocks_str-275"><a href="#IsOK_ContextHolder.get_bad_blocks_str-275"><span class="linenos">275</span></a>        <span class="k">return</span> <span class="n">full_string</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.raise_bad_blocks" class="classattr">
                                        <input id="IsOK_ContextHolder.raise_bad_blocks-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">raise_bad_blocks</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.raise_bad_blocks-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.raise_bad_blocks"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.raise_bad_blocks-277"><a href="#IsOK_ContextHolder.raise_bad_blocks-277"><span class="linenos">277</span></a>    <span class="k">def</span> <span class="nf">raise_bad_blocks</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.raise_bad_blocks-278"><a href="#IsOK_ContextHolder.raise_bad_blocks-278"><span class="linenos">278</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_bad_blocks</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.raise_full_history" class="classattr">
                                        <input id="IsOK_ContextHolder.raise_full_history-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">raise_full_history</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.raise_full_history-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.raise_full_history"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.raise_full_history-280"><a href="#IsOK_ContextHolder.raise_full_history-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">raise_full_history</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.raise_full_history-281"><a href="#IsOK_ContextHolder.raise_full_history-281"><span class="linenos">281</span></a>        <span class="k">raise</span> <span class="n">IsOK_HistoryExport</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.process_history_import" class="classattr">
                                        <input id="IsOK_ContextHolder.process_history_import-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">process_history_import</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">his_ex</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.process_history_import-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.process_history_import"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.process_history_import-283"><a href="#IsOK_ContextHolder.process_history_import-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="nf">process_history_import</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">his_ex</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.process_history_import-284"><a href="#IsOK_ContextHolder.process_history_import-284"><span class="linenos">284</span></a>        <span class="n">history</span> <span class="o">=</span> <span class="n">his_ex</span><span class="o">.</span><span class="n">history</span>
</span><span id="IsOK_ContextHolder.process_history_import-285"><a href="#IsOK_ContextHolder.process_history_import-285"><span class="linenos">285</span></a>        <span class="k">for</span> <span class="n">block</span> <span class="ow">in</span> <span class="n">history</span><span class="p">:</span>
</span><span id="IsOK_ContextHolder.process_history_import-286"><a href="#IsOK_ContextHolder.process_history_import-286"><span class="linenos">286</span></a>            <span class="n">full_block_info</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_internal_blocks_index</span><span class="o">.</span><span class="n">get_new_ID</span><span class="p">(),</span> <span class="n">block</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span>
</span><span id="IsOK_ContextHolder.process_history_import-287"><a href="#IsOK_ContextHolder.process_history_import-287"><span class="linenos">287</span></a>                               <span class="n">block</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span> <span class="n">block</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="IsOK_ContextHolder.process_history_import-288"><a href="#IsOK_ContextHolder.process_history_import-288"><span class="linenos">288</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_full_history</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">full_block_info</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.close" class="classattr">
                                        <input id="IsOK_ContextHolder.close-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">close</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.close-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.close"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.close-290"><a href="#IsOK_ContextHolder.close-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.close-291"><a href="#IsOK_ContextHolder.close-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_closed</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOK_ContextHolder.is_ok" class="classattr">
                                        <input id="IsOK_ContextHolder.is_ok-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_ok</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOK_ContextHolder.is_ok-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOK_ContextHolder.is_ok"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOK_ContextHolder.is_ok-304"><a href="#IsOK_ContextHolder.is_ok-304"><span class="linenos">304</span></a>    <span class="k">def</span> <span class="nf">is_ok</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="IsOK_ContextHolder.is_ok-305"><a href="#IsOK_ContextHolder.is_ok-305"><span class="linenos">305</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="is_ok">
                            <input id="is_ok-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@contextmanager</div>

        <span class="def">def</span>
        <span class="name">is_ok</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context_holder</span>,</span><span class="param">	<span class="n">block_id</span>,</span><span class="param">	<span class="n">block_info</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_ok-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_ok"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_ok-308"><a href="#is_ok-308"><span class="linenos">308</span></a><span class="nd">@contextmanager</span>
</span><span id="is_ok-309"><a href="#is_ok-309"><span class="linenos">309</span></a><span class="k">def</span> <span class="nf">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="is_ok-310"><a href="#is_ok-310"><span class="linenos">310</span></a>    <span class="k">if</span> <span class="n">block_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok-311"><a href="#is_ok-311"><span class="linenos">311</span></a>        <span class="n">new_id</span> <span class="o">=</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_reserve_block_id_generator</span><span class="p">()</span>
</span><span id="is_ok-312"><a href="#is_ok-312"><span class="linenos">312</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="p">(</span><span class="n">new_id</span><span class="p">,</span> <span class="n">new_id</span><span class="p">)</span>
</span><span id="is_ok-313"><a href="#is_ok-313"><span class="linenos">313</span></a>
</span><span id="is_ok-314"><a href="#is_ok-314"><span class="linenos">314</span></a>    <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_closeable</span> <span class="ow">and</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_closed</span><span class="p">:</span>
</span><span id="is_ok-315"><a href="#is_ok-315"><span class="linenos">315</span></a>        <span class="k">raise</span> <span class="n">IsOK_Closed</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">)</span>
</span><span id="is_ok-316"><a href="#is_ok-316"><span class="linenos">316</span></a>
</span><span id="is_ok-317"><a href="#is_ok-317"><span class="linenos">317</span></a>    <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_block_info</span><span class="p">(</span><span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">)</span>
</span><span id="is_ok-318"><a href="#is_ok-318"><span class="linenos">318</span></a>    <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok-319"><a href="#is_ok-319"><span class="linenos">319</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_criteria</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="is_ok-320"><a href="#is_ok-320"><span class="linenos">320</span></a>    <span class="n">need_to_save_block_result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="is_ok-321"><a href="#is_ok-321"><span class="linenos">321</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="is_ok-322"><a href="#is_ok-322"><span class="linenos">322</span></a>        <span class="k">yield</span> <span class="n">context_holder</span>
</span><span id="is_ok-323"><a href="#is_ok-323"><span class="linenos">323</span></a>    <span class="k">except</span> <span class="n">IsOK_BlockFailed</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
</span><span id="is_ok-324"><a href="#is_ok-324"><span class="linenos">324</span></a>        <span class="n">result_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok-325"><a href="#is_ok-325"><span class="linenos">325</span></a>        <span class="k">if</span> <span class="n">exc</span><span class="o">.</span><span class="n">args</span><span class="p">:</span>
</span><span id="is_ok-326"><a href="#is_ok-326"><span class="linenos">326</span></a>            <span class="n">result_info</span> <span class="o">=</span> <span class="n">exc</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</span><span id="is_ok-327"><a href="#is_ok-327"><span class="linenos">327</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="is_ok-328"><a href="#is_ok-328"><span class="linenos">328</span></a>                <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">built_in_exception__is_ok_block_failed</span><span class="p">,</span>
</span><span id="is_ok-329"><a href="#is_ok-329"><span class="linenos">329</span></a>                <span class="s1">&#39;ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: IsOK_BlockFailed (</span><span class="si">{}</span><span class="s1">)&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">result_info</span><span class="p">),</span> <span class="n">result_info</span><span class="p">))</span>
</span><span id="is_ok-330"><a href="#is_ok-330"><span class="linenos">330</span></a>    <span class="k">except</span> <span class="n">IsOK_HistoryExport</span> <span class="k">as</span> <span class="n">export</span><span class="p">:</span>
</span><span id="is_ok-331"><a href="#is_ok-331"><span class="linenos">331</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">process_history_import</span><span class="p">(</span><span class="n">export</span><span class="p">)</span>
</span><span id="is_ok-332"><a href="#is_ok-332"><span class="linenos">332</span></a>        <span class="k">if</span> <span class="n">export</span><span class="o">.</span><span class="n">process_error_result</span><span class="p">:</span>
</span><span id="is_ok-333"><a href="#is_ok-333"><span class="linenos">333</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="is_ok-334"><a href="#is_ok-334"><span class="linenos">334</span></a>                    <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">built_in_exception__bad_history_import</span><span class="p">,</span>
</span><span id="is_ok-335"><a href="#is_ok-335"><span class="linenos">335</span></a>                    <span class="s1">&#39;ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="is_ok-336"><a href="#is_ok-336"><span class="linenos">336</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="is_ok-337"><a href="#is_ok-337"><span class="linenos">337</span></a>        <span class="n">exc</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span><span id="is_ok-338"><a href="#is_ok-338"><span class="linenos">338</span></a>        <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_obj</span><span class="p">,</span> <span class="n">exc_tb</span> <span class="o">=</span> <span class="n">exc</span>
</span><span id="is_ok-339"><a href="#is_ok-339"><span class="linenos">339</span></a>        <span class="n">tb_full_file_name</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">exc_tb</span><span class="o">.</span><span class="n">tb_frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_filename</span><span class="p">)[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="is_ok-340"><a href="#is_ok-340"><span class="linenos">340</span></a>        <span class="n">tb_line_number</span> <span class="o">=</span> <span class="n">exc_tb</span><span class="o">.</span><span class="n">tb_lineno</span>
</span><span id="is_ok-341"><a href="#is_ok-341"><span class="linenos">341</span></a>        <span class="n">tb_function_name</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="is_ok-342"><a href="#is_ok-342"><span class="linenos">342</span></a>        <span class="n">tb_text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="is_ok-343"><a href="#is_ok-343"><span class="linenos">343</span></a>
</span><span id="is_ok-344"><a href="#is_ok-344"><span class="linenos">344</span></a>        <span class="n">tb_list</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">extract_tb</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
</span><span id="is_ok-345"><a href="#is_ok-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tb_list</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">2</span><span class="p">:</span>
</span><span id="is_ok-346"><a href="#is_ok-346"><span class="linenos">346</span></a>            <span class="n">actual_tb</span> <span class="o">=</span> <span class="n">tb_list</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</span><span id="is_ok-347"><a href="#is_ok-347"><span class="linenos">347</span></a>            <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">,</span> <span class="n">tb_text</span> <span class="o">=</span> <span class="n">actual_tb</span>
</span><span id="is_ok-348"><a href="#is_ok-348"><span class="linenos">348</span></a>
</span><span id="is_ok-349"><a href="#is_ok-349"><span class="linenos">349</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">exc</span>
</span><span id="is_ok-350"><a href="#is_ok-350"><span class="linenos">350</span></a>        <span class="n">error_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="nb">str</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
</span><span id="is_ok-351"><a href="#is_ok-351"><span class="linenos">351</span></a>        <span class="c1"># print(&#39;+++&#39;, error_str)</span>
</span><span id="is_ok-352"><a href="#is_ok-352"><span class="linenos">352</span></a>        <span class="n">formatted_traceback</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_exception</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">exception</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">exception</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="is_ok-353"><a href="#is_ok-353"><span class="linenos">353</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="n">exception</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">formatted_traceback</span><span class="p">,)</span>
</span><span id="is_ok-354"><a href="#is_ok-354"><span class="linenos">354</span></a>        <span class="n">trace_str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">exception</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>
</span><span id="is_ok-355"><a href="#is_ok-355"><span class="linenos">355</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_debug_trace</span><span class="p">:</span>
</span><span id="is_ok-356"><a href="#is_ok-356"><span class="linenos">356</span></a>            <span class="n">result_string</span> <span class="o">=</span> <span class="s1">&#39;ISOK INTERNAL RESULT. CODE EXCEPTION &quot;</span><span class="si">{}</span><span class="s1">&quot; AT &quot;</span><span class="si">{}</span><span class="s1">&quot;:</span><span class="si">{}</span><span class="s1"> in </span><span class="si">{}</span><span class="s1"> WITH TRACE: </span><span class="se">\n</span><span class="s1">&#39;</span> \
</span><span id="is_ok-357"><a href="#is_ok-357"><span class="linenos">357</span></a>                            <span class="s1">&#39;</span><span class="si">{}</span><span class="se">\n</span><span class="s1">&#39;</span> \
</span><span id="is_ok-358"><a href="#is_ok-358"><span class="linenos">358</span></a>                            <span class="s1">&#39;~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~&#39;</span> \
</span><span id="is_ok-359"><a href="#is_ok-359"><span class="linenos">359</span></a>                            <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">error_str</span><span class="p">,</span> <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">,</span> <span class="n">trace_str</span><span class="p">)</span>
</span><span id="is_ok-360"><a href="#is_ok-360"><span class="linenos">360</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok-361"><a href="#is_ok-361"><span class="linenos">361</span></a>            <span class="n">result_string</span> <span class="o">=</span> <span class="s1">&#39;ISOK INTERNAL RESULT. CODE EXCEPTION &quot;</span><span class="si">{}</span><span class="s1">&quot; AT &quot;</span><span class="si">{}</span><span class="s1">&quot;:</span><span class="si">{}</span><span class="s1"> in </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
</span><span id="is_ok-362"><a href="#is_ok-362"><span class="linenos">362</span></a>                    <span class="n">error_str</span><span class="p">,</span> <span class="n">tb_full_file_name</span><span class="p">,</span> <span class="n">tb_line_number</span><span class="p">,</span> <span class="n">tb_function_name</span><span class="p">)</span>
</span><span id="is_ok-363"><a href="#is_ok-363"><span class="linenos">363</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="is_ok-364"><a href="#is_ok-364"><span class="linenos">364</span></a>                <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">external_exception</span><span class="p">,</span> <span class="n">result_string</span><span class="p">,</span> <span class="n">exc</span><span class="p">))</span>
</span><span id="is_ok-365"><a href="#is_ok-365"><span class="linenos">365</span></a>        <span class="c1"># print(result_string)</span>
</span><span id="is_ok-366"><a href="#is_ok-366"><span class="linenos">366</span></a>        <span class="c1"># _is_ok_reader_runner__context_holder.push_result(False, sys.exc_info()[1])</span>
</span><span id="is_ok-367"><a href="#is_ok-367"><span class="linenos">367</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_raise_exceptions</span><span class="p">:</span>
</span><span id="is_ok-368"><a href="#is_ok-368"><span class="linenos">368</span></a>            <span class="n">need_to_save_block_result</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="is_ok-369"><a href="#is_ok-369"><span class="linenos">369</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_block_result</span><span class="p">()</span>
</span><span id="is_ok-370"><a href="#is_ok-370"><span class="linenos">370</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">raise_bad_blocks</span><span class="p">()</span>
</span><span id="is_ok-371"><a href="#is_ok-371"><span class="linenos">371</span></a>            <span class="c1"># raise</span>
</span><span id="is_ok-372"><a href="#is_ok-372"><span class="linenos">372</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok-373"><a href="#is_ok-373"><span class="linenos">373</span></a>        <span class="k">if</span> <span class="n">context_holder</span><span class="o">.</span><span class="n">_current_block_result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok-374"><a href="#is_ok-374"><span class="linenos">374</span></a>            <span class="c1"># _is_ok_reader_runner__context_holder.push_result(True)</span>
</span><span id="is_ok-375"><a href="#is_ok-375"><span class="linenos">375</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">False</span><span class="p">,</span> <span class="n">IsOK_IntenalResult</span><span class="p">(</span>
</span><span id="is_ok-376"><a href="#is_ok-376"><span class="linenos">376</span></a>                    <span class="n">IsOK_IntenalResultType</span><span class="o">.</span><span class="n">block_did_not_returned_an_answer</span><span class="p">,</span>
</span><span id="is_ok-377"><a href="#is_ok-377"><span class="linenos">377</span></a>                    <span class="s1">&#39;ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="is_ok-378"><a href="#is_ok-378"><span class="linenos">378</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="is_ok-379"><a href="#is_ok-379"><span class="linenos">379</span></a>        <span class="k">if</span> <span class="n">need_to_save_block_result</span><span class="p">:</span>
</span><span id="is_ok-380"><a href="#is_ok-380"><span class="linenos">380</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_save_block_result</span><span class="p">(</span><span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="is_ok-381"><a href="#is_ok-381"><span class="linenos">381</span></a>        <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok-382"><a href="#is_ok-382"><span class="linenos">382</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_criteria</span><span class="p">()</span>
</span><span id="is_ok-383"><a href="#is_ok-383"><span class="linenos">383</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_block_info</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="is_ok__function">
                            <input id="is_ok__function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_ok__function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">target_function</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_ok__function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_ok__function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_ok__function-386"><a href="#is_ok__function-386"><span class="linenos">386</span></a><span class="k">def</span> <span class="nf">is_ok__function</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="is_ok__function-387"><a href="#is_ok__function-387"><span class="linenos">387</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="is_ok__function-388"><a href="#is_ok__function-388"><span class="linenos">388</span></a><span class="sd">    Parameters: is_ok__context_holder= (required)</span>
</span><span id="is_ok__function-389"><a href="#is_ok__function-389"><span class="linenos">389</span></a><span class="sd">        , is_ok__block_id= (required)</span>
</span><span id="is_ok__function-390"><a href="#is_ok__function-390"><span class="linenos">390</span></a><span class="sd">        , is_ok__block_info= (optional)</span>
</span><span id="is_ok__function-391"><a href="#is_ok__function-391"><span class="linenos">391</span></a><span class="sd">        , is_ok__block_results_criteria= (optional)</span>
</span><span id="is_ok__function-392"><a href="#is_ok__function-392"><span class="linenos">392</span></a><span class="sd">        , is_ok__ignore_block_result_criteria= (optional).</span>
</span><span id="is_ok__function-393"><a href="#is_ok__function-393"><span class="linenos">393</span></a><span class="sd">    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).</span>
</span><span id="is_ok__function-394"><a href="#is_ok__function-394"><span class="linenos">394</span></a><span class="sd">    :param target_function: function</span>
</span><span id="is_ok__function-395"><a href="#is_ok__function-395"><span class="linenos">395</span></a><span class="sd">    :return:</span>
</span><span id="is_ok__function-396"><a href="#is_ok__function-396"><span class="linenos">396</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="is_ok__function-397"><a href="#is_ok__function-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="is_ok__function-398"><a href="#is_ok__function-398"><span class="linenos">398</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-399"><a href="#is_ok__function-399"><span class="linenos">399</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function-400"><a href="#is_ok__function-400"><span class="linenos">400</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-401"><a href="#is_ok__function-401"><span class="linenos">401</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-402"><a href="#is_ok__function-402"><span class="linenos">402</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok__function-403"><a href="#is_ok__function-403"><span class="linenos">403</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="is_ok__function-404"><a href="#is_ok__function-404"><span class="linenos">404</span></a>
</span><span id="is_ok__function-405"><a href="#is_ok__function-405"><span class="linenos">405</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-406"><a href="#is_ok__function-406"><span class="linenos">406</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_id&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function-407"><a href="#is_ok__function-407"><span class="linenos">407</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-408"><a href="#is_ok__function-408"><span class="linenos">408</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-409"><a href="#is_ok__function-409"><span class="linenos">409</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok__function-410"><a href="#is_ok__function-410"><span class="linenos">410</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">)</span>
</span><span id="is_ok__function-411"><a href="#is_ok__function-411"><span class="linenos">411</span></a>
</span><span id="is_ok__function-412"><a href="#is_ok__function-412"><span class="linenos">412</span></a>        <span class="n">block_info</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-413"><a href="#is_ok__function-413"><span class="linenos">413</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_info&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function-414"><a href="#is_ok__function-414"><span class="linenos">414</span></a>            <span class="n">block_info</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_info&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-415"><a href="#is_ok__function-415"><span class="linenos">415</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_info&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-416"><a href="#is_ok__function-416"><span class="linenos">416</span></a>
</span><span id="is_ok__function-417"><a href="#is_ok__function-417"><span class="linenos">417</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-418"><a href="#is_ok__function-418"><span class="linenos">418</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function-419"><a href="#is_ok__function-419"><span class="linenos">419</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-420"><a href="#is_ok__function-420"><span class="linenos">420</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-421"><a href="#is_ok__function-421"><span class="linenos">421</span></a>
</span><span id="is_ok__function-422"><a href="#is_ok__function-422"><span class="linenos">422</span></a>        <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-423"><a href="#is_ok__function-423"><span class="linenos">423</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function-424"><a href="#is_ok__function-424"><span class="linenos">424</span></a>            <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-425"><a href="#is_ok__function-425"><span class="linenos">425</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function-426"><a href="#is_ok__function-426"><span class="linenos">426</span></a>
</span><span id="is_ok__function-427"><a href="#is_ok__function-427"><span class="linenos">427</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function-428"><a href="#is_ok__function-428"><span class="linenos">428</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> \
</span><span id="is_ok__function-429"><a href="#is_ok__function-429"><span class="linenos">429</span></a>                <span class="n">context</span><span class="p">:</span>
</span><span id="is_ok__function-430"><a href="#is_ok__function-430"><span class="linenos">430</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="is_ok__function-431"><a href="#is_ok__function-431"><span class="linenos">431</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="is_ok__function-432"><a href="#is_ok__function-432"><span class="linenos">432</span></a>
</span><span id="is_ok__function-433"><a href="#is_ok__function-433"><span class="linenos">433</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="is_ok__function-434"><a href="#is_ok__function-434"><span class="linenos">434</span></a>
</span><span id="is_ok__function-435"><a href="#is_ok__function-435"><span class="linenos">435</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span></pre></div>


            <div class="docstring"><p>Parameters: is_ok__context_holder= (required)
    , is_ok__block_id= (required)
    , is_ok__block_info= (optional)
    , is_ok__block_results_criteria= (optional)
    , is_ok__ignore_block_result_criteria= (optional).
Parameters passed to the target_function: is_ok__context_holder (after local block configuration).
:param target_function: function
:return:</p>
</div>


                </section>
                <section id="IsOkRunner">
                            <input id="IsOkRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkRunner</span>:

                <label class="view-source-button" for="IsOkRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkRunner-469"><a href="#IsOkRunner-469"><span class="linenos">469</span></a><span class="k">class</span> <span class="nc">IsOkRunner</span><span class="p">:</span>
</span><span id="IsOkRunner-470"><a href="#IsOkRunner-470"><span class="linenos">470</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkRunner-471"><a href="#IsOkRunner-471"><span class="linenos">471</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkRunner-472"><a href="#IsOkRunner-472"><span class="linenos">472</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkRunner-473"><a href="#IsOkRunner-473"><span class="linenos">473</span></a>
</span><span id="IsOkRunner-474"><a href="#IsOkRunner-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOkRunner-475"><a href="#IsOkRunner-475"><span class="linenos">475</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkRunner-476"><a href="#IsOkRunner-476"><span class="linenos">476</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span>
</span><span id="IsOkRunner-477"><a href="#IsOkRunner-477"><span class="linenos">477</span></a>                             <span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="IsOkRunner-478"><a href="#IsOkRunner-478"><span class="linenos">478</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkRunner.__init__" class="classattr">
                                        <input id="IsOkRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkRunner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">current_globals</span>, </span><span class="param"><span class="n">context_holder</span></span>)</span>

                <label class="view-source-button" for="IsOkRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkRunner.__init__-470"><a href="#IsOkRunner.__init__-470"><span class="linenos">470</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkRunner.__init__-471"><a href="#IsOkRunner.__init__-471"><span class="linenos">471</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkRunner.__init__-472"><a href="#IsOkRunner.__init__-472"><span class="linenos">472</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkRunner.current_globals" class="classattr">
                                <div class="attr variable">
            <span class="name">current_globals</span>

        
    </div>
    <a class="headerlink" href="#IsOkRunner.current_globals"></a>
    
    

                            </div>
                            <div id="IsOkRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkRunner.context_holder"></a>
    
    

                            </div>
                </section>
                <section id="IsOkCallRunner">
                            <input id="IsOkCallRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkCallRunner</span>:

                <label class="view-source-button" for="IsOkCallRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkCallRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkCallRunner-502"><a href="#IsOkCallRunner-502"><span class="linenos">502</span></a><span class="k">class</span> <span class="nc">IsOkCallRunner</span><span class="p">:</span>
</span><span id="IsOkCallRunner-503"><a href="#IsOkCallRunner-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkCallRunner-504"><a href="#IsOkCallRunner-504"><span class="linenos">504</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkCallRunner-505"><a href="#IsOkCallRunner-505"><span class="linenos">505</span></a>
</span><span id="IsOkCallRunner-506"><a href="#IsOkCallRunner-506"><span class="linenos">506</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOkCallRunner-507"><a href="#IsOkCallRunner-507"><span class="linenos">507</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkCallRunner-508"><a href="#IsOkCallRunner-508"><span class="linenos">508</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkCallRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span>
</span><span id="IsOkCallRunner-509"><a href="#IsOkCallRunner-509"><span class="linenos">509</span></a>                                 <span class="n">ignore_block_result_criteria</span><span class="p">)</span>
</span><span id="IsOkCallRunner-510"><a href="#IsOkCallRunner-510"><span class="linenos">510</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkCallRunner.__init__" class="classattr">
                                        <input id="IsOkCallRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkCallRunner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">context_holder</span></span>)</span>

                <label class="view-source-button" for="IsOkCallRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkCallRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkCallRunner.__init__-503"><a href="#IsOkCallRunner.__init__-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkCallRunner.__init__-504"><a href="#IsOkCallRunner.__init__-504"><span class="linenos">504</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkCallRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkCallRunner.context_holder"></a>
    
    

                            </div>
                </section>
                <section id="is_ok__function__simple">
                            <input id="is_ok__function__simple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_ok__function__simple</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">target_function</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_ok__function__simple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_ok__function__simple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_ok__function__simple-513"><a href="#is_ok__function__simple-513"><span class="linenos">513</span></a><span class="k">def</span> <span class="nf">is_ok__function__simple</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="is_ok__function__simple-514"><a href="#is_ok__function__simple-514"><span class="linenos">514</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="is_ok__function__simple-515"><a href="#is_ok__function__simple-515"><span class="linenos">515</span></a><span class="sd">    Parameters: is_ok__context_holder= (required)</span>
</span><span id="is_ok__function__simple-516"><a href="#is_ok__function__simple-516"><span class="linenos">516</span></a><span class="sd">        , is_ok__block_id= (optional) (default value == str(target_function))</span>
</span><span id="is_ok__function__simple-517"><a href="#is_ok__function__simple-517"><span class="linenos">517</span></a><span class="sd">        , is_ok__block_results_criteria= (optional)</span>
</span><span id="is_ok__function__simple-518"><a href="#is_ok__function__simple-518"><span class="linenos">518</span></a><span class="sd">        , is_ok__ignore_block_result_criteria= (optional).</span>
</span><span id="is_ok__function__simple-519"><a href="#is_ok__function__simple-519"><span class="linenos">519</span></a><span class="sd">    Parameters passed to the target_function: .</span>
</span><span id="is_ok__function__simple-520"><a href="#is_ok__function__simple-520"><span class="linenos">520</span></a><span class="sd">    :param target_function: function</span>
</span><span id="is_ok__function__simple-521"><a href="#is_ok__function__simple-521"><span class="linenos">521</span></a><span class="sd">    :return:</span>
</span><span id="is_ok__function__simple-522"><a href="#is_ok__function__simple-522"><span class="linenos">522</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="is_ok__function__simple-523"><a href="#is_ok__function__simple-523"><span class="linenos">523</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="is_ok__function__simple-524"><a href="#is_ok__function__simple-524"><span class="linenos">524</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function__simple-525"><a href="#is_ok__function__simple-525"><span class="linenos">525</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function__simple-526"><a href="#is_ok__function__simple-526"><span class="linenos">526</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-527"><a href="#is_ok__function__simple-527"><span class="linenos">527</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-528"><a href="#is_ok__function__simple-528"><span class="linenos">528</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok__function__simple-529"><a href="#is_ok__function__simple-529"><span class="linenos">529</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="is_ok__function__simple-530"><a href="#is_ok__function__simple-530"><span class="linenos">530</span></a>
</span><span id="is_ok__function__simple-531"><a href="#is_ok__function__simple-531"><span class="linenos">531</span></a>        <span class="c1"># block_id = &#39;__UNNAMED_FUNCTION_SIMPLE_BLOCK__&#39;</span>
</span><span id="is_ok__function__simple-532"><a href="#is_ok__function__simple-532"><span class="linenos">532</span></a>        <span class="n">block_id</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">target_function</span><span class="p">)</span>
</span><span id="is_ok__function__simple-533"><a href="#is_ok__function__simple-533"><span class="linenos">533</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_id&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function__simple-534"><a href="#is_ok__function__simple-534"><span class="linenos">534</span></a>            <span class="n">block_id</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-535"><a href="#is_ok__function__simple-535"><span class="linenos">535</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_id&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-536"><a href="#is_ok__function__simple-536"><span class="linenos">536</span></a>
</span><span id="is_ok__function__simple-537"><a href="#is_ok__function__simple-537"><span class="linenos">537</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function__simple-538"><a href="#is_ok__function__simple-538"><span class="linenos">538</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function__simple-539"><a href="#is_ok__function__simple-539"><span class="linenos">539</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-540"><a href="#is_ok__function__simple-540"><span class="linenos">540</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-541"><a href="#is_ok__function__simple-541"><span class="linenos">541</span></a>
</span><span id="is_ok__function__simple-542"><a href="#is_ok__function__simple-542"><span class="linenos">542</span></a>        <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function__simple-543"><a href="#is_ok__function__simple-543"><span class="linenos">543</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok__function__simple-544"><a href="#is_ok__function__simple-544"><span class="linenos">544</span></a>            <span class="n">ignore_block_result_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-545"><a href="#is_ok__function__simple-545"><span class="linenos">545</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__ignore_block_result_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok__function__simple-546"><a href="#is_ok__function__simple-546"><span class="linenos">546</span></a>
</span><span id="is_ok__function__simple-547"><a href="#is_ok__function__simple-547"><span class="linenos">547</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok__function__simple-548"><a href="#is_ok__function__simple-548"><span class="linenos">548</span></a>        <span class="k">with</span> <span class="n">is_ok</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="is_ok__function__simple-549"><a href="#is_ok__function__simple-549"><span class="linenos">549</span></a>            <span class="k">if</span> <span class="n">context</span><span class="p">:</span>
</span><span id="is_ok__function__simple-550"><a href="#is_ok__function__simple-550"><span class="linenos">550</span></a>                <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="is_ok__function__simple-551"><a href="#is_ok__function__simple-551"><span class="linenos">551</span></a>                <span class="n">context</span><span class="o">.</span><span class="n">push_result</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="n">target_function_result</span><span class="p">)</span>
</span><span id="is_ok__function__simple-552"><a href="#is_ok__function__simple-552"><span class="linenos">552</span></a>
</span><span id="is_ok__function__simple-553"><a href="#is_ok__function__simple-553"><span class="linenos">553</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="is_ok__function__simple-554"><a href="#is_ok__function__simple-554"><span class="linenos">554</span></a>
</span><span id="is_ok__function__simple-555"><a href="#is_ok__function__simple-555"><span class="linenos">555</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span></pre></div>


            <div class="docstring"><p>Parameters: is_ok__context_holder= (required)
    , is_ok__block_id= (optional) (default value == str(target_function))
    , is_ok__block_results_criteria= (optional)
    , is_ok__ignore_block_result_criteria= (optional).
Parameters passed to the target_function: .
:param target_function: function
:return:</p>
</div>


                </section>
                <section id="IsOkUniRunner">
                            <input id="IsOkUniRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkUniRunner</span>:

                <label class="view-source-button" for="IsOkUniRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniRunner-592"><a href="#IsOkUniRunner-592"><span class="linenos">592</span></a><span class="k">class</span> <span class="nc">IsOkUniRunner</span><span class="p">:</span>
</span><span id="IsOkUniRunner-593"><a href="#IsOkUniRunner-593"><span class="linenos">593</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniRunner-594"><a href="#IsOkUniRunner-594"><span class="linenos">594</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkUniRunner-595"><a href="#IsOkUniRunner-595"><span class="linenos">595</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkUniRunner-596"><a href="#IsOkUniRunner-596"><span class="linenos">596</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="IsOkUniRunner-597"><a href="#IsOkUniRunner-597"><span class="linenos">597</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkUniRunner-598"><a href="#IsOkUniRunner-598"><span class="linenos">598</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniRunner-599"><a href="#IsOkUniRunner-599"><span class="linenos">599</span></a>
</span><span id="IsOkUniRunner-600"><a href="#IsOkUniRunner-600"><span class="linenos">600</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunner</span>
</span><span id="IsOkUniRunner-601"><a href="#IsOkUniRunner-601"><span class="linenos">601</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="IsOkUniRunner-602"><a href="#IsOkUniRunner-602"><span class="linenos">602</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunnerSimple</span>
</span><span id="IsOkUniRunner-603"><a href="#IsOkUniRunner-603"><span class="linenos">603</span></a>
</span><span id="IsOkUniRunner-604"><a href="#IsOkUniRunner-604"><span class="linenos">604</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkUniRunner-605"><a href="#IsOkUniRunner-605"><span class="linenos">605</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="IsOkUniRunner-606"><a href="#IsOkUniRunner-606"><span class="linenos">606</span></a>
</span><span id="IsOkUniRunner-607"><a href="#IsOkUniRunner-607"><span class="linenos">607</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkUniRunner-608"><a href="#IsOkUniRunner-608"><span class="linenos">608</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniRunner-609"><a href="#IsOkUniRunner-609"><span class="linenos">609</span></a>
</span><span id="IsOkUniRunner-610"><a href="#IsOkUniRunner-610"><span class="linenos">610</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOkUniRunner-611"><a href="#IsOkUniRunner-611"><span class="linenos">611</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniRunner-612"><a href="#IsOkUniRunner-612"><span class="linenos">612</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="IsOkUniRunner-613"><a href="#IsOkUniRunner-613"><span class="linenos">613</span></a>                                   <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">)</span>
</span><span id="IsOkUniRunner-614"><a href="#IsOkUniRunner-614"><span class="linenos">614</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkUniRunner.__init__" class="classattr">
                                        <input id="IsOkUniRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkUniRunner</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">current_globals</span>,</span><span class="param">	<span class="n">context_holder</span>,</span><span class="param">	<span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span>,</span><span class="param">	<span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="IsOkUniRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniRunner.__init__-593"><a href="#IsOkUniRunner.__init__-593"><span class="linenos">593</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniRunner.__init__-594"><a href="#IsOkUniRunner.__init__-594"><span class="linenos">594</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkUniRunner.__init__-595"><a href="#IsOkUniRunner.__init__-595"><span class="linenos">595</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkUniRunner.__init__-596"><a href="#IsOkUniRunner.__init__-596"><span class="linenos">596</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="IsOkUniRunner.__init__-597"><a href="#IsOkUniRunner.__init__-597"><span class="linenos">597</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkUniRunner.__init__-598"><a href="#IsOkUniRunner.__init__-598"><span class="linenos">598</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniRunner.__init__-599"><a href="#IsOkUniRunner.__init__-599"><span class="linenos">599</span></a>
</span><span id="IsOkUniRunner.__init__-600"><a href="#IsOkUniRunner.__init__-600"><span class="linenos">600</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunner</span>
</span><span id="IsOkUniRunner.__init__-601"><a href="#IsOkUniRunner.__init__-601"><span class="linenos">601</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="IsOkUniRunner.__init__-602"><a href="#IsOkUniRunner.__init__-602"><span class="linenos">602</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkRunnerSimple</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkUniRunner.current_globals" class="classattr">
                                <div class="attr variable">
            <span class="name">current_globals</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.current_globals"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.context_holder"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.simple_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">simple_mode</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.simple_mode"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.default_function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">default_function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.default_function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.runner_class" class="classattr">
                                <div class="attr variable">
            <span class="name">runner_class</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniRunner.runner_class"></a>
    
    

                            </div>
                            <div id="IsOkUniRunner.set_function_result_criteria" class="classattr">
                                        <input id="IsOkUniRunner.set_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result_criteria_computer</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkUniRunner.set_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniRunner.set_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniRunner.set_function_result_criteria-604"><a href="#IsOkUniRunner.set_function_result_criteria-604"><span class="linenos">604</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkUniRunner.set_function_result_criteria-605"><a href="#IsOkUniRunner.set_function_result_criteria-605"><span class="linenos">605</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkUniRunner.reset_function_result_criteria" class="classattr">
                                        <input id="IsOkUniRunner.reset_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">reset_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkUniRunner.reset_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniRunner.reset_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniRunner.reset_function_result_criteria-607"><a href="#IsOkUniRunner.reset_function_result_criteria-607"><span class="linenos">607</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkUniRunner.reset_function_result_criteria-608"><a href="#IsOkUniRunner.reset_function_result_criteria-608"><span class="linenos">608</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="IsOkUniCallRunner">
                            <input id="IsOkUniCallRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkUniCallRunner</span>:

                <label class="view-source-button" for="IsOkUniCallRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniCallRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniCallRunner-641"><a href="#IsOkUniCallRunner-641"><span class="linenos">641</span></a><span class="k">class</span> <span class="nc">IsOkUniCallRunner</span><span class="p">:</span>
</span><span id="IsOkUniCallRunner-642"><a href="#IsOkUniCallRunner-642"><span class="linenos">642</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner-643"><a href="#IsOkUniCallRunner-643"><span class="linenos">643</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkUniCallRunner-644"><a href="#IsOkUniCallRunner-644"><span class="linenos">644</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="IsOkUniCallRunner-645"><a href="#IsOkUniCallRunner-645"><span class="linenos">645</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkUniCallRunner-646"><a href="#IsOkUniCallRunner-646"><span class="linenos">646</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniCallRunner-647"><a href="#IsOkUniCallRunner-647"><span class="linenos">647</span></a>
</span><span id="IsOkUniCallRunner-648"><a href="#IsOkUniCallRunner-648"><span class="linenos">648</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunner</span>
</span><span id="IsOkUniCallRunner-649"><a href="#IsOkUniCallRunner-649"><span class="linenos">649</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="IsOkUniCallRunner-650"><a href="#IsOkUniCallRunner-650"><span class="linenos">650</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunnerSimple</span>
</span><span id="IsOkUniCallRunner-651"><a href="#IsOkUniCallRunner-651"><span class="linenos">651</span></a>
</span><span id="IsOkUniCallRunner-652"><a href="#IsOkUniCallRunner-652"><span class="linenos">652</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner-653"><a href="#IsOkUniCallRunner-653"><span class="linenos">653</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="IsOkUniCallRunner-654"><a href="#IsOkUniCallRunner-654"><span class="linenos">654</span></a>
</span><span id="IsOkUniCallRunner-655"><a href="#IsOkUniCallRunner-655"><span class="linenos">655</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner-656"><a href="#IsOkUniCallRunner-656"><span class="linenos">656</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniCallRunner-657"><a href="#IsOkUniCallRunner-657"><span class="linenos">657</span></a>
</span><span id="IsOkUniCallRunner-658"><a href="#IsOkUniCallRunner-658"><span class="linenos">658</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOkUniCallRunner-659"><a href="#IsOkUniCallRunner-659"><span class="linenos">659</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner-660"><a href="#IsOkUniCallRunner-660"><span class="linenos">660</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="IsOkUniCallRunner-661"><a href="#IsOkUniCallRunner-661"><span class="linenos">661</span></a>                                   <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">)</span>
</span><span id="IsOkUniCallRunner-662"><a href="#IsOkUniCallRunner-662"><span class="linenos">662</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkUniCallRunner.__init__" class="classattr">
                                        <input id="IsOkUniCallRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkUniCallRunner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">context_holder</span>, </span><span class="param"><span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span>, </span><span class="param"><span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="IsOkUniCallRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniCallRunner.__init__-642"><a href="#IsOkUniCallRunner.__init__-642"><span class="linenos">642</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">simple_mode</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner.__init__-643"><a href="#IsOkUniCallRunner.__init__-643"><span class="linenos">643</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkUniCallRunner.__init__-644"><a href="#IsOkUniCallRunner.__init__-644"><span class="linenos">644</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span> <span class="o">=</span> <span class="n">simple_mode</span>
</span><span id="IsOkUniCallRunner.__init__-645"><a href="#IsOkUniCallRunner.__init__-645"><span class="linenos">645</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkUniCallRunner.__init__-646"><a href="#IsOkUniCallRunner.__init__-646"><span class="linenos">646</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkUniCallRunner.__init__-647"><a href="#IsOkUniCallRunner.__init__-647"><span class="linenos">647</span></a>
</span><span id="IsOkUniCallRunner.__init__-648"><a href="#IsOkUniCallRunner.__init__-648"><span class="linenos">648</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunner</span>
</span><span id="IsOkUniCallRunner.__init__-649"><a href="#IsOkUniCallRunner.__init__-649"><span class="linenos">649</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">simple_mode</span><span class="p">:</span>
</span><span id="IsOkUniCallRunner.__init__-650"><a href="#IsOkUniCallRunner.__init__-650"><span class="linenos">650</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">runner_class</span> <span class="o">=</span> <span class="n">_IsOkCallRunnerSimple</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkUniCallRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.context_holder"></a>
    
    

                            </div>
                            <div id="IsOkUniCallRunner.simple_mode" class="classattr">
                                <div class="attr variable">
            <span class="name">simple_mode</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.simple_mode"></a>
    
    

                            </div>
                            <div id="IsOkUniCallRunner.default_function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">default_function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.default_function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkUniCallRunner.function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkUniCallRunner.runner_class" class="classattr">
                                <div class="attr variable">
            <span class="name">runner_class</span>

        
    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.runner_class"></a>
    
    

                            </div>
                            <div id="IsOkUniCallRunner.set_function_result_criteria" class="classattr">
                                        <input id="IsOkUniCallRunner.set_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result_criteria_computer</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkUniCallRunner.set_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.set_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniCallRunner.set_function_result_criteria-652"><a href="#IsOkUniCallRunner.set_function_result_criteria-652"><span class="linenos">652</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner.set_function_result_criteria-653"><a href="#IsOkUniCallRunner.set_function_result_criteria-653"><span class="linenos">653</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkUniCallRunner.reset_function_result_criteria" class="classattr">
                                        <input id="IsOkUniCallRunner.reset_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">reset_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkUniCallRunner.reset_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkUniCallRunner.reset_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkUniCallRunner.reset_function_result_criteria-655"><a href="#IsOkUniCallRunner.reset_function_result_criteria-655"><span class="linenos">655</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkUniCallRunner.reset_function_result_criteria-656"><a href="#IsOkUniCallRunner.reset_function_result_criteria-656"><span class="linenos">656</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="IsOkValRunner">
                            <input id="IsOkValRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkValRunner</span>:

                <label class="view-source-button" for="IsOkValRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkValRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkValRunner-692"><a href="#IsOkValRunner-692"><span class="linenos">692</span></a><span class="k">class</span> <span class="nc">IsOkValRunner</span><span class="p">:</span>
</span><span id="IsOkValRunner-693"><a href="#IsOkValRunner-693"><span class="linenos">693</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">reaction_to_the_result</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkValRunner-694"><a href="#IsOkValRunner-694"><span class="linenos">694</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkValRunner-695"><a href="#IsOkValRunner-695"><span class="linenos">695</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkValRunner-696"><a href="#IsOkValRunner-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkValRunner-697"><a href="#IsOkValRunner-697"><span class="linenos">697</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reaction_to_the_result</span> <span class="o">=</span> <span class="n">reaction_to_the_result</span>
</span><span id="IsOkValRunner-698"><a href="#IsOkValRunner-698"><span class="linenos">698</span></a>
</span><span id="IsOkValRunner-699"><a href="#IsOkValRunner-699"><span class="linenos">699</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkValRunner-700"><a href="#IsOkValRunner-700"><span class="linenos">700</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span><span id="IsOkValRunner-701"><a href="#IsOkValRunner-701"><span class="linenos">701</span></a>
</span><span id="IsOkValRunner-702"><a href="#IsOkValRunner-702"><span class="linenos">702</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkValRunner-703"><a href="#IsOkValRunner-703"><span class="linenos">703</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkValRunner-704"><a href="#IsOkValRunner-704"><span class="linenos">704</span></a>
</span><span id="IsOkValRunner-705"><a href="#IsOkValRunner-705"><span class="linenos">705</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_id</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_info</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span>
</span><span id="IsOkValRunner-706"><a href="#IsOkValRunner-706"><span class="linenos">706</span></a>                 <span class="n">ignore_block_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkValRunner-707"><a href="#IsOkValRunner-707"><span class="linenos">707</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkValRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_id</span><span class="p">,</span> <span class="n">block_info</span><span class="p">,</span>
</span><span id="IsOkValRunner-708"><a href="#IsOkValRunner-708"><span class="linenos">708</span></a>                                <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">ignore_block_result_criteria</span><span class="p">,</span>
</span><span id="IsOkValRunner-709"><a href="#IsOkValRunner-709"><span class="linenos">709</span></a>                                <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">reaction_to_the_result</span><span class="p">)</span>
</span><span id="IsOkValRunner-710"><a href="#IsOkValRunner-710"><span class="linenos">710</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkValRunner.__init__" class="classattr">
                                        <input id="IsOkValRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkValRunner</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">context_holder</span>,</span><span class="param">	<span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">reaction_to_the_result</span><span class="o">=</span><span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="IsOkValRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkValRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkValRunner.__init__-693"><a href="#IsOkValRunner.__init__-693"><span class="linenos">693</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">,</span> <span class="n">function_result_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">reaction_to_the_result</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="IsOkValRunner.__init__-694"><a href="#IsOkValRunner.__init__-694"><span class="linenos">694</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkValRunner.__init__-695"><a href="#IsOkValRunner.__init__-695"><span class="linenos">695</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span> <span class="o">=</span> <span class="n">function_result_criteria</span> <span class="ow">or</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="IsOkValRunner.__init__-696"><a href="#IsOkValRunner.__init__-696"><span class="linenos">696</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span><span id="IsOkValRunner.__init__-697"><a href="#IsOkValRunner.__init__-697"><span class="linenos">697</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">reaction_to_the_result</span> <span class="o">=</span> <span class="n">reaction_to_the_result</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkValRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkValRunner.context_holder"></a>
    
    

                            </div>
                            <div id="IsOkValRunner.default_function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">default_function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkValRunner.default_function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkValRunner.function_result_criteria" class="classattr">
                                <div class="attr variable">
            <span class="name">function_result_criteria</span>

        
    </div>
    <a class="headerlink" href="#IsOkValRunner.function_result_criteria"></a>
    
    

                            </div>
                            <div id="IsOkValRunner.reaction_to_the_result" class="classattr">
                                <div class="attr variable">
            <span class="name">reaction_to_the_result</span>

        
    </div>
    <a class="headerlink" href="#IsOkValRunner.reaction_to_the_result"></a>
    
    

                            </div>
                            <div id="IsOkValRunner.set_function_result_criteria" class="classattr">
                                        <input id="IsOkValRunner.set_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result_criteria_computer</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkValRunner.set_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkValRunner.set_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkValRunner.set_function_result_criteria-699"><a href="#IsOkValRunner.set_function_result_criteria-699"><span class="linenos">699</span></a>    <span class="k">def</span> <span class="nf">set_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result_criteria_computer</span><span class="p">):</span>
</span><span id="IsOkValRunner.set_function_result_criteria-700"><a href="#IsOkValRunner.set_function_result_criteria-700"><span class="linenos">700</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="n">result_criteria_computer</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkValRunner.reset_function_result_criteria" class="classattr">
                                        <input id="IsOkValRunner.reset_function_result_criteria-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">reset_function_result_criteria</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="IsOkValRunner.reset_function_result_criteria-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkValRunner.reset_function_result_criteria"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkValRunner.reset_function_result_criteria-702"><a href="#IsOkValRunner.reset_function_result_criteria-702"><span class="linenos">702</span></a>    <span class="k">def</span> <span class="nf">reset_function_result_criteria</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="IsOkValRunner.reset_function_result_criteria-703"><a href="#IsOkValRunner.reset_function_result_criteria-703"><span class="linenos">703</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">function_result_criteria</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_function_result_criteria</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="is_ok_reader">
                            <input id="is_ok_reader-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@contextmanager</div>

        <span class="def">def</span>
        <span class="name">is_ok_reader</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">context_holder</span>, </span><span class="param"><span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span>, </span><span class="param"><span class="n">close</span><span class="o">=</span><span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_ok_reader-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_ok_reader"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_ok_reader-713"><a href="#is_ok_reader-713"><span class="linenos">713</span></a><span class="nd">@contextmanager</span>
</span><span id="is_ok_reader-714"><a href="#is_ok_reader-714"><span class="linenos">714</span></a><span class="k">def</span> <span class="nf">is_ok_reader</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="is_ok_reader-715"><a href="#is_ok_reader-715"><span class="linenos">715</span></a>    <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok_reader-716"><a href="#is_ok_reader-716"><span class="linenos">716</span></a>        <span class="n">context_holder</span><span class="o">.</span><span class="n">_push_criteria</span><span class="p">(</span><span class="n">block_results_criteria</span><span class="p">)</span>
</span><span id="is_ok_reader-717"><a href="#is_ok_reader-717"><span class="linenos">717</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="is_ok_reader-718"><a href="#is_ok_reader-718"><span class="linenos">718</span></a>        <span class="k">yield</span> <span class="n">context_holder</span>
</span><span id="is_ok_reader-719"><a href="#is_ok_reader-719"><span class="linenos">719</span></a>    <span class="k">except</span><span class="p">:</span>
</span><span id="is_ok_reader-720"><a href="#is_ok_reader-720"><span class="linenos">720</span></a>        <span class="k">raise</span>
</span><span id="is_ok_reader-721"><a href="#is_ok_reader-721"><span class="linenos">721</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="is_ok_reader-722"><a href="#is_ok_reader-722"><span class="linenos">722</span></a>        <span class="k">if</span> <span class="n">block_results_criteria</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="is_ok_reader-723"><a href="#is_ok_reader-723"><span class="linenos">723</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">_pop_criteria</span><span class="p">()</span>
</span><span id="is_ok_reader-724"><a href="#is_ok_reader-724"><span class="linenos">724</span></a>        <span class="k">if</span> <span class="n">close</span><span class="p">:</span>
</span><span id="is_ok_reader-725"><a href="#is_ok_reader-725"><span class="linenos">725</span></a>            <span class="n">context_holder</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="is_ok_reader__function">
                            <input id="is_ok_reader__function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_ok_reader__function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">target_function</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_ok_reader__function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_ok_reader__function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_ok_reader__function-728"><a href="#is_ok_reader__function-728"><span class="linenos">728</span></a><span class="k">def</span> <span class="nf">is_ok_reader__function</span><span class="p">(</span><span class="n">target_function</span><span class="p">):</span>
</span><span id="is_ok_reader__function-729"><a href="#is_ok_reader__function-729"><span class="linenos">729</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="is_ok_reader__function-730"><a href="#is_ok_reader__function-730"><span class="linenos">730</span></a><span class="sd">    Parameters: is_ok__context_holder= (required), is_ok__block_results_criteria= (optional), is_ok__close= (optional).</span>
</span><span id="is_ok_reader__function-731"><a href="#is_ok_reader__function-731"><span class="linenos">731</span></a><span class="sd">    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).</span>
</span><span id="is_ok_reader__function-732"><a href="#is_ok_reader__function-732"><span class="linenos">732</span></a><span class="sd">    :param target_function: function</span>
</span><span id="is_ok_reader__function-733"><a href="#is_ok_reader__function-733"><span class="linenos">733</span></a><span class="sd">    :return:</span>
</span><span id="is_ok_reader__function-734"><a href="#is_ok_reader__function-734"><span class="linenos">734</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="is_ok_reader__function-735"><a href="#is_ok_reader__function-735"><span class="linenos">735</span></a>    <span class="k">def</span> <span class="nf">new_target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="is_ok_reader__function-736"><a href="#is_ok_reader__function-736"><span class="linenos">736</span></a>        <span class="n">context_holder</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok_reader__function-737"><a href="#is_ok_reader__function-737"><span class="linenos">737</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__context_holder&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok_reader__function-738"><a href="#is_ok_reader__function-738"><span class="linenos">738</span></a>            <span class="n">context_holder</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-739"><a href="#is_ok_reader__function-739"><span class="linenos">739</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-740"><a href="#is_ok_reader__function-740"><span class="linenos">740</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="is_ok_reader__function-741"><a href="#is_ok_reader__function-741"><span class="linenos">741</span></a>            <span class="k">raise</span> <span class="n">IsOKForFunction_ParameterNeeded</span><span class="p">(</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">)</span>
</span><span id="is_ok_reader__function-742"><a href="#is_ok_reader__function-742"><span class="linenos">742</span></a>
</span><span id="is_ok_reader__function-743"><a href="#is_ok_reader__function-743"><span class="linenos">743</span></a>        <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok_reader__function-744"><a href="#is_ok_reader__function-744"><span class="linenos">744</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__block_results_criteria&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok_reader__function-745"><a href="#is_ok_reader__function-745"><span class="linenos">745</span></a>            <span class="n">block_results_criteria</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-746"><a href="#is_ok_reader__function-746"><span class="linenos">746</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__block_results_criteria&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-747"><a href="#is_ok_reader__function-747"><span class="linenos">747</span></a>
</span><span id="is_ok_reader__function-748"><a href="#is_ok_reader__function-748"><span class="linenos">748</span></a>        <span class="n">close</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok_reader__function-749"><a href="#is_ok_reader__function-749"><span class="linenos">749</span></a>        <span class="k">if</span> <span class="s1">&#39;is_ok__close&#39;</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="p">:</span>
</span><span id="is_ok_reader__function-750"><a href="#is_ok_reader__function-750"><span class="linenos">750</span></a>            <span class="n">close</span> <span class="o">=</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__close&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-751"><a href="#is_ok_reader__function-751"><span class="linenos">751</span></a>            <span class="k">del</span> <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__close&#39;</span><span class="p">]</span>
</span><span id="is_ok_reader__function-752"><a href="#is_ok_reader__function-752"><span class="linenos">752</span></a>
</span><span id="is_ok_reader__function-753"><a href="#is_ok_reader__function-753"><span class="linenos">753</span></a>        <span class="n">target_function_result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="is_ok_reader__function-754"><a href="#is_ok_reader__function-754"><span class="linenos">754</span></a>        <span class="k">with</span> <span class="n">is_ok_reader</span><span class="p">(</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span> <span class="k">as</span> <span class="n">context</span><span class="p">:</span>
</span><span id="is_ok_reader__function-755"><a href="#is_ok_reader__function-755"><span class="linenos">755</span></a>            <span class="n">kwargs</span><span class="p">[</span><span class="s1">&#39;is_ok__context_holder&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">context</span>
</span><span id="is_ok_reader__function-756"><a href="#is_ok_reader__function-756"><span class="linenos">756</span></a>            <span class="n">target_function_result</span> <span class="o">=</span> <span class="n">target_function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="is_ok_reader__function-757"><a href="#is_ok_reader__function-757"><span class="linenos">757</span></a>
</span><span id="is_ok_reader__function-758"><a href="#is_ok_reader__function-758"><span class="linenos">758</span></a>        <span class="k">return</span> <span class="n">target_function_result</span>
</span><span id="is_ok_reader__function-759"><a href="#is_ok_reader__function-759"><span class="linenos">759</span></a>
</span><span id="is_ok_reader__function-760"><a href="#is_ok_reader__function-760"><span class="linenos">760</span></a>    <span class="k">return</span> <span class="n">new_target_function</span>
</span></pre></div>


            <div class="docstring"><p>Parameters: is_ok__context_holder= (required), is_ok__block_results_criteria= (optional), is_ok__close= (optional).
Parameters passed to the target_function: is_ok__context_holder (after local block configuration).
:param target_function: function
:return:</p>
</div>


                </section>
                <section id="IsOkReaderRunner">
                            <input id="IsOkReaderRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkReaderRunner</span>:

                <label class="view-source-button" for="IsOkReaderRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkReaderRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkReaderRunner-790"><a href="#IsOkReaderRunner-790"><span class="linenos">790</span></a><span class="k">class</span> <span class="nc">IsOkReaderRunner</span><span class="p">:</span>
</span><span id="IsOkReaderRunner-791"><a href="#IsOkReaderRunner-791"><span class="linenos">791</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkReaderRunner-792"><a href="#IsOkReaderRunner-792"><span class="linenos">792</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkReaderRunner-793"><a href="#IsOkReaderRunner-793"><span class="linenos">793</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkReaderRunner-794"><a href="#IsOkReaderRunner-794"><span class="linenos">794</span></a>
</span><span id="IsOkReaderRunner-795"><a href="#IsOkReaderRunner-795"><span class="linenos">795</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="IsOkReaderRunner-796"><a href="#IsOkReaderRunner-796"><span class="linenos">796</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkReaderRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span>
</span><span id="IsOkReaderRunner-797"><a href="#IsOkReaderRunner-797"><span class="linenos">797</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkReaderRunner.__init__" class="classattr">
                                        <input id="IsOkReaderRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkReaderRunner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">current_globals</span>, </span><span class="param"><span class="n">context_holder</span></span>)</span>

                <label class="view-source-button" for="IsOkReaderRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkReaderRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkReaderRunner.__init__-791"><a href="#IsOkReaderRunner.__init__-791"><span class="linenos">791</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">current_globals</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkReaderRunner.__init__-792"><a href="#IsOkReaderRunner.__init__-792"><span class="linenos">792</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_globals</span> <span class="o">=</span> <span class="n">current_globals</span>
</span><span id="IsOkReaderRunner.__init__-793"><a href="#IsOkReaderRunner.__init__-793"><span class="linenos">793</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkReaderRunner.current_globals" class="classattr">
                                <div class="attr variable">
            <span class="name">current_globals</span>

        
    </div>
    <a class="headerlink" href="#IsOkReaderRunner.current_globals"></a>
    
    

                            </div>
                            <div id="IsOkReaderRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkReaderRunner.context_holder"></a>
    
    

                            </div>
                </section>
                <section id="IsOkReaderCallRunner">
                            <input id="IsOkReaderCallRunner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IsOkReaderCallRunner</span>:

                <label class="view-source-button" for="IsOkReaderCallRunner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkReaderCallRunner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkReaderCallRunner-817"><a href="#IsOkReaderCallRunner-817"><span class="linenos">817</span></a><span class="k">class</span> <span class="nc">IsOkReaderCallRunner</span><span class="p">:</span>
</span><span id="IsOkReaderCallRunner-818"><a href="#IsOkReaderCallRunner-818"><span class="linenos">818</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkReaderCallRunner-819"><a href="#IsOkReaderCallRunner-819"><span class="linenos">819</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span><span id="IsOkReaderCallRunner-820"><a href="#IsOkReaderCallRunner-820"><span class="linenos">820</span></a>
</span><span id="IsOkReaderCallRunner-821"><a href="#IsOkReaderCallRunner-821"><span class="linenos">821</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">close</span><span class="o">=</span><span class="kc">False</span><span class="p">):</span>
</span><span id="IsOkReaderCallRunner-822"><a href="#IsOkReaderCallRunner-822"><span class="linenos">822</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">_IsOkReaderCallRunner</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span><span class="p">,</span> <span class="n">block_results_criteria</span><span class="p">,</span> <span class="n">close</span><span class="p">)</span>
</span><span id="IsOkReaderCallRunner-823"><a href="#IsOkReaderCallRunner-823"><span class="linenos">823</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                            <div id="IsOkReaderCallRunner.__init__" class="classattr">
                                        <input id="IsOkReaderCallRunner.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">IsOkReaderCallRunner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">context_holder</span></span>)</span>

                <label class="view-source-button" for="IsOkReaderCallRunner.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IsOkReaderCallRunner.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IsOkReaderCallRunner.__init__-818"><a href="#IsOkReaderCallRunner.__init__-818"><span class="linenos">818</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">context_holder</span><span class="p">):</span>
</span><span id="IsOkReaderCallRunner.__init__-819"><a href="#IsOkReaderCallRunner.__init__-819"><span class="linenos">819</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">context_holder</span> <span class="o">=</span> <span class="n">context_holder</span>
</span></pre></div>


    

                            </div>
                            <div id="IsOkReaderCallRunner.context_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">context_holder</span>

        
    </div>
    <a class="headerlink" href="#IsOkReaderCallRunner.context_holder"></a>
    
    

                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>