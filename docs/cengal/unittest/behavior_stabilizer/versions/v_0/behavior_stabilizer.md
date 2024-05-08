---
title: behavior_stabilizer
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.unittest<wbr>.behavior_stabilizer<wbr>.versions<wbr>.v_0<wbr>.behavior_stabilizer    </h1>

                
                        <input id="mod-behavior_stabilizer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-behavior_stabilizer-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;CallState&#39;</span><span class="p">,</span> <span class="s1">&#39;ResultAlreadyRegisteredError&#39;</span><span class="p">,</span> <span class="s1">&#39;ExceptionAlreadyRegisteredError&#39;</span><span class="p">,</span> <span class="s1">&#39;CallStackIsNotEqualError&#39;</span><span class="p">,</span> 
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>           <span class="s1">&#39;ExpectedTestCaseStateIsNotLoadedError&#39;</span><span class="p">,</span> <span class="s1">&#39;TEST_CASE_STATE&#39;</span><span class="p">,</span> <span class="s1">&#39;get_test_case_state&#39;</span><span class="p">,</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">]</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a><span class="kn">import</span> <span class="nn">datetime</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a><span class="kn">import</span> <span class="nn">inspect</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">import</span> <span class="nn">json</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">import</span> <span class="nn">logging</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">import</span> <span class="nn">os</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">import</span> <span class="nn">traceback</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">import</span> <span class="nn">unittest</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">import</span> <span class="nn">pickle</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">contextmanager</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">FrameType</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">NoReturn</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">cast</span><span class="p">,</span> <span class="n">ContextManager</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">OrderedDict</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ValueHolder</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">intro_func_params_with_values</span><span class="p">,</span> <span class="n">find_current_entity</span><span class="p">,</span> <span class="n">find_entity</span><span class="p">,</span> <span class="n">is_async</span><span class="p">,</span> \
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>    <span class="n">intro_frame_params_with_values</span><span class="p">,</span> <span class="n">entity_class</span><span class="p">,</span> <span class="n">get_exception</span><span class="p">,</span> <span class="n">func_params_with_values</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">cengal.file_system.path_manager</span> <span class="kn">import</span> <span class="n">relative_to_src</span><span class="p">,</span> <span class="n">RelativePath</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span><span class="p">,</span> <span class="n">OrderedDict</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span><span class="p">,</span> <span class="n">update_wrapper</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a><span class="sd">Module Docstring</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="n">VarName</span> <span class="o">=</span> <span class="nb">str</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="n">VarValue</span> <span class="o">=</span> <span class="n">Any</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="n">MeasurementId</span> <span class="o">=</span> <span class="nb">int</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="n">StageId</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="k">def</span> <span class="nf">param</span><span class="p">(</span><span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="sd">    Returns a formatted full name of the parameter: &#39;ClassName__m__MethodName__p__ParameterName&#39;</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="sd">    Returns:</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="sd">    str: furmatted full name of the parameter</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a>    <span class="n">frame</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">FrameType</span><span class="p">,</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span><span class="o">.</span><span class="n">f_back</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a>    <span class="n">real_func</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">FrameType</span><span class="p">,</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">())</span><span class="o">.</span><span class="n">f_back</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">real_func</span><span class="o">.</span><span class="n">co_name</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>    <span class="n">args</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">values</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getargvalues</span><span class="p">(</span><span class="n">frame</span><span class="p">)</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>    <span class="n">parent_obj</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a>    <span class="k">for</span> <span class="n">par_name</span><span class="p">,</span> <span class="n">par_val</span> <span class="ow">in</span> <span class="p">[(</span><span class="n">i</span><span class="p">,</span> <span class="n">values</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">args</span><span class="p">]:</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>        <span class="k">if</span> <span class="s1">&#39;self&#39;</span> <span class="o">==</span> <span class="n">par_name</span><span class="p">:</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>            <span class="n">parent_obj</span> <span class="o">=</span> <span class="n">par_val</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>            <span class="k">break</span>  <span class="c1"># TODO: check if it is needed</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>    
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a>    <span class="n">class_name</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="k">if</span> <span class="n">parent_obj</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>        <span class="n">class_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">parent_obj</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>    
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>    <span class="n">param_full_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">class_name</span><span class="si">}</span><span class="s1">__m__</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">__p__</span><span class="si">{</span><span class="n">param_name</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a>    <span class="k">return</span> <span class="n">param_full_name</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="k">def</span> <span class="nf">param2</span><span class="p">(</span><span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="n">FAKE_RESULTS</span><span class="p">:</span> <span class="s1">&#39;FakeResults&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;FakeResults&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="k">def</span> <span class="nf">get_fake_results</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="s1">&#39;FakeResults&#39;</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">global</span> <span class="n">FAKE_RESULTS</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>    <span class="k">if</span> <span class="n">FAKE_RESULTS</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>        <span class="n">FAKE_RESULTS</span> <span class="o">=</span> <span class="n">FakeResults</span><span class="p">()</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">return</span> <span class="n">FAKE_RESULTS</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="k">class</span> <span class="nc">ParameterIsNotInNotInTheListOfExpectedResultsError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="sd">    Will be raised by FakeResults.check_result() when `param_name not in self.expected_results`</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>    <span class="k">pass</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="k">class</span> <span class="nc">ResultNumberIsNotValidError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">    Will be raised by FakeResults.check_result() when `result_number not in self.expected_results[param_name]`</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>    <span class="k">pass</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a><span class="k">class</span> <span class="nc">FakeResults</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a><span class="sd">    Holds a both an actual and a refference (an expected) results and compares them</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="sd">    Saves a taken results as a refference &#39;expected_results&#39; to a json file on FakeResults.try_to_save_expected_results() if </span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a><span class="sd">    this file was not already loaded by the FakeResults.try_to_load_expected_results() method.</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a><span class="sd">    So if FakeResults.try_to_load_expected_results() will be called before all tests and FakeResults.try_to_save_expected_results()</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a><span class="sd">    will be called after all tests:</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a><span class="sd">        1) At a first iteration it will take all generated results and will save them to the json file as a refference (as an expected_results).</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a><span class="sd">        This step must be made on a developers&#39; machine. Resulting json file must be added to the repository.</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="sd">        2) At all further calls it will find json file exists and will load it&#39;s content as a refference (as an expected_results).</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a><span class="sd">    </span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a><span class="sd">    Can be used as a &#39;with&#39; context manager which will try to load json file at the start and will try to save a refference to the json file</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a><span class="sd">    at the end (if json file wasn&#39;t loaded at the start).</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a><span class="sd">    Raises:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a><span class="sd">        NotImplementedError: _description_</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>    
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">content_full_file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">was_loaded</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span> <span class="o">=</span> <span class="n">content_full_file_name</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span><span class="p">:</span> <span class="s1">&#39;FakeResults&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;FakeResults&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">def</span> <span class="nf">add_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a><span class="sd">        Will add a result to a list of the results for a requested parameter</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a><span class="sd">        For example we have a function:</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a><span class="sd">            def add_int(a: int, b: int) -&gt; int:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a><span class="sd">                return a + b</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a><span class="sd">        </span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a><span class="sd">        Then we can change it in the next way:</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a><span class="sd">            def add_int(a: int, b: int) -&gt; int:</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="sd">                result = a + b</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a><span class="sd">                get_fake_results().add_result(param(&#39;a&#39;), a)</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a><span class="sd">                get_fake_results().add_result(param(&#39;b&#39;), b)</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a><span class="sd">                # get_fake_results().add_result(param(&#39;-&gt;&#39;), result)  # TODO: check if it is needed</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="sd">                return result</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a><span class="sd">        </span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a><span class="sd">        As result we will save all &#39;a&#39; and &#39;b&#39; parameters of an each &#39;add_int()&#39; call to an ordered sequence and will</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a><span class="sd">        be able to compare them with a refference values by the calling FakeResults.check_result(), FakeResults.check_results_range() or FakeResults.check_all_results()</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="sd">        Parameters:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="sd">        param_name (str): your parameter name</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a><span class="sd">        result (Any): current parameters&#39; content</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>        <span class="k">if</span> <span class="n">param_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>            <span class="n">index</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>    
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    <span class="k">def</span> <span class="nf">add_expected_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">expected_result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">        Will add single expected result for the parameter</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">        </span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">        Parameters:</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">        param_name (str): your parameter name</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">        expected_result (Any): expected parameters&#39; content</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="n">expected_result</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">expected_result</span><span class="p">)</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        <span class="k">if</span> <span class="n">param_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">:</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]:</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>            <span class="n">index</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">+</span> <span class="mi">1</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">expected_result</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>    <span class="k">def</span> <span class="nf">register_param_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">expected_results</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a><span class="sd">        Will register a list of expected results for the parameter</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a><span class="sd">        Will add a list of expected results for the parameter</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a><span class="sd">        </span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a><span class="sd">        Parameters:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a><span class="sd">        param_name (str): your parameter name</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a><span class="sd">        expected_results (List[Any]): list of expected parameters&#39; content</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">for</span> <span class="n">expected_result</span> <span class="ow">in</span> <span class="n">expected_results</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">add_expected_result</span><span class="p">(</span><span class="n">param_name</span><span class="p">,</span> <span class="n">expected_result</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    <span class="k">def</span> <span class="nf">register_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">expected_results</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">str</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a><span class="sd">        Will register a dict of expected results for all requested parameters</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a><span class="sd">        Parameters:</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a><span class="sd">        expected_results (Dict[str, Dict[int, str]]): key - parameter name; value.key - index of the expected parameter&#39;s</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a><span class="sd">        content; value.value - expected parameter&#39;s content</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span> <span class="o">=</span> <span class="n">expected_results</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">check_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result_number</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">        Will compare requested parameter&#39;s result with an expected result. if result_number is not None -  will compare</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">        exact items in a sequence instead of comparing all expected results.</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a><span class="sd">        Will return True to an each call until json file will be loaded with a &#39;FakeResults.try_to_load_expected_results()&#39; call.</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a><span class="sd">        Returns:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a><span class="sd">        bool: True if result is equal to an expected result</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">was_loaded</span><span class="p">:</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="k">if</span> <span class="n">param_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">:</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="k">raise</span> <span class="n">ParameterIsNotInNotInTheListOfExpectedResultsError</span><span class="p">(</span><span class="n">param_name</span><span class="p">)</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>        
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">if</span> <span class="n">param_name</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">:</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;ERROR: PARAM NOT IN RESULTS: </span><span class="si">{</span><span class="n">param_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="n">result_number</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            <span class="k">if</span> <span class="n">result_number</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]:</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>                <span class="k">raise</span> <span class="n">ResultNumberIsNotValidError</span><span class="p">((</span><span class="n">param_name</span><span class="p">,</span> <span class="n">result_number</span><span class="p">))</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>            
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>            <span class="k">if</span> <span class="n">result_number</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]:</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;ERROR: PARAM</span><span class="se">\&#39;</span><span class="s1">S RESULT NUMBER </span><span class="si">{</span><span class="n">result_number</span><span class="si">}</span><span class="s1"> NOT IN RESULTS: </span><span class="si">{</span><span class="n">param_name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="k">if</span> <span class="n">result_number</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>            <span class="n">returned_val</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>            <span class="n">expected_val</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">]</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>            <span class="n">returned_val</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">[</span><span class="n">param_name</span><span class="p">][</span><span class="n">result_number</span><span class="p">]</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="n">expected_val</span><span class="p">:</span> <span class="n">Any</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param_name</span><span class="p">][</span><span class="n">result_number</span><span class="p">]</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="k">if</span> <span class="n">returned_val</span> <span class="o">==</span> <span class="n">expected_val</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;ERROR: PARAM IS NOT EQUAL TO EXPECTED: </span><span class="si">{</span><span class="n">param_name</span><span class="si">}</span><span class="se">\n\t</span><span class="s1">RETURNED VAL: </span><span class="si">{</span><span class="n">returned_val</span><span class="si">}</span><span class="se">\n\t</span><span class="s1">EXPECTED VAL: </span><span class="si">{</span><span class="n">expected_val</span><span class="si">}</span><span class="se">\n</span><span class="s1">~~~~~~~~~~~~~~~~~~~~~~~~~&#39;</span><span class="p">)</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>            <span class="c1"># return False  # TODO: check if it is needed</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>    
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">check_results_range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result_number_from</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">result_number_up_to</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a><span class="sd">        Will compare a range of requested parameters&#39; results with an expected results.</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a><span class="sd">        Will return True to an each call until json file will be loaded with a &#39;FakeResults.try_to_load_expected_results()&#39; call.</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a><span class="sd">        Behavior of the &#39;results_number_from&#39; and &#39;results_number_up_to&#39; parameters is the same as in the &#39;range()&#39; call.</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a><span class="sd">        Parameters:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a><span class="sd">        param_name (str): your parameter name</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a><span class="sd">        result_number_from (int): start index of the results range</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a><span class="sd">        result_number_up_to (int): end index of the results range</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a><span class="sd">        Returns:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a><span class="sd">        bool: True if all results in the range are equal to an expected results</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        <span class="k">for</span> <span class="n">result_number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">result_number_from</span><span class="p">,</span> <span class="n">result_number_up_to</span><span class="p">):</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_result</span><span class="p">(</span><span class="n">param_name</span><span class="p">,</span> <span class="n">result_number</span><span class="o">=</span><span class="n">result_number</span><span class="p">):</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="nf">check_current_results</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a><span class="sd">        Will compare all requested parameters&#39; results with an expected results.</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a><span class="sd">        Will return True to an each call until json file will be loaded with a &#39;FakeResults.try_to_load_expected_results()&#39; call.</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="sd">        Returns:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a><span class="sd">        bool: True if all results are equal to an expected results</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="k">for</span> <span class="n">param_name</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_result</span><span class="p">(</span><span class="n">param_name</span><span class="p">):</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">check_all_results</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a><span class="sd">        Will compare all requested parameters&#39; results with an expected results.</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="sd">        Will return True to an each call until json file will be loaded with a &#39;FakeResults.try_to_load_expected_results()&#39; call.</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a><span class="sd">        Returns:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a><span class="sd">        bool: True if all results are equal to an expected results</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>        <span class="k">for</span> <span class="n">param_name</span><span class="p">,</span> <span class="n">_</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">check_result</span><span class="p">(</span><span class="n">param_name</span><span class="p">):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>    <span class="k">def</span> <span class="nf">try_to_load_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a><span class="sd">        Will try to load a json file with a refference results (an expected_results)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="sd">        </span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a><span class="sd">        Parameters:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a><span class="sd">        full_file_name (str): full file name of the json file with a refference results (an expected_results)</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">):</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>            <span class="n">content</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>                <span class="n">content</span> <span class="o">=</span> <span class="n">file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="k">if</span> <span class="n">content</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>                <span class="n">content_str</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>                <span class="n">expected_results</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">content_str</span><span class="p">)</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>                <span class="k">for</span> <span class="n">param</span><span class="p">,</span> <span class="n">values</span> <span class="ow">in</span> <span class="n">expected_results</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>                    <span class="k">if</span> <span class="n">param</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>                    
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>                    <span class="k">for</span> <span class="n">index_str</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">values</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>                        <span class="n">index</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">index_str</span><span class="p">)</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">expected_results</span><span class="p">[</span><span class="n">param</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>                
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">was_loaded</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>    
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">try_to_save_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">full_file_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="sd">        Will try to save a refference results (an expected_results) to a json file. Will not save them if </span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a><span class="sd">        json file was already successfully loaded with a &#39;FakeResults.try_to_load_expected_results()&#39; call.</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a><span class="sd">        Parameters:</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a><span class="sd">        full_file_name (str): full file name of the json file with a refference results (an expected_results)</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">was_loaded</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="k">return</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">)):</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>            <span class="n">content</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">results</span><span class="p">)</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>            <span class="n">content</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">content</span><span class="p">),</span> <span class="n">indent</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>            <span class="n">content_bytes</span> <span class="o">=</span> <span class="n">content</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb+&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>  <span class="c1"># TODO: check if &#39;+&#39; in &#39;wb+&#39; is needed</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>                <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">content_bytes</span><span class="p">)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>    
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a><span class="sd">        Will register current instance to a global &#39;FAKE_RESULTS&#39; variable. Will save a previous value</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">try_to_load_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="k">global</span> <span class="n">FAKE_RESULTS</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span> <span class="o">=</span> <span class="n">FAKE_RESULTS</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>        <span class="n">FAKE_RESULTS</span> <span class="o">=</span> <span class="bp">self</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>    
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">unregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">should_be_saved</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a><span class="sd">        Will restore a previous value of the global &#39;FAKE_RESULTS&#39; variable</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        <span class="k">global</span> <span class="n">FAKE_RESULTS</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="n">FAKE_RESULTS</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        <span class="k">if</span> <span class="n">should_be_saved</span><span class="p">:</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">try_to_save_expected_results</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">):</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unregister</span><span class="p">((</span><span class="n">exc_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_val</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_tb</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a><span class="n">CallState</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s2">&quot;CallState&quot;</span><span class="p">,</span> <span class="s2">&quot;entity params_with_values args kwargs result_holder exception_holder&quot;</span><span class="p">)</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a><span class="k">class</span> <span class="nc">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>    <span class="k">pass</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a><span class="k">class</span> <span class="nc">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>    <span class="k">pass</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a><span class="k">class</span> <span class="nc">CallStackIsNotEqualError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    <span class="k">pass</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a><span class="k">class</span> <span class="nc">ExpectedTestCaseStateIsNotLoadedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>    <span class="k">pass</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a><span class="n">TEST_CASE_STATE</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;TestCaseState&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a><span class="k">def</span> <span class="nf">get_test_case_state</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">:</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>    <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>    <span class="k">if</span> <span class="n">TEST_CASE_STATE</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="n">TestCaseState</span><span class="p">(</span><span class="s1">&#39;Default&#39;</span><span class="p">)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>    
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>    <span class="k">return</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a><span class="k">class</span> <span class="nc">TestCaseState</span><span class="p">:</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">register</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>            <span class="n">parent_entity</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>            <span class="n">parent_class</span> <span class="o">=</span> <span class="n">entity_class</span><span class="p">(</span><span class="n">parent_entity</span><span class="p">)</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>            <span class="n">parent_class_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">parent_class</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">parent_class_name</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>        <span class="p">})</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="p">})</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.pickle&#39;</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.md&#39;</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="n">relative_to_src</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">)</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">)</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;TestCaseState&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="k">if</span> <span class="n">register</span><span class="p">:</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>    <span class="nd">@property</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">current_test_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Hashable</span><span class="p">:</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>    
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>    <span class="nd">@current_test_id</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>    <span class="k">def</span> <span class="nf">current_test_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="k">if</span> <span class="n">value</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>    
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="nd">@property</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="nf">call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>    
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>    <span class="nd">@property</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>    <span class="k">def</span> <span class="nf">expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>    <span class="k">def</span> <span class="nf">is_loaded</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>            <span class="k">raise</span> <span class="n">ExpectedTestCaseStateIsNotLoadedError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected test case state is not loaded: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>    
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">check_current_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Current call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>    
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>    <span class="k">def</span> <span class="nf">check_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: </span><span class="si">{</span><span class="n">item_index</span><span class="si">}</span><span class="se">\n</span><span class="s1">Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>    
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>    <span class="k">def</span> <span class="nf">check_state_range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_start_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">item_end_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="n">call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>        <span class="k">if</span> <span class="n">call_stack_part</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: [</span><span class="si">{</span><span class="n">item_start_index</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="n">item_end_index</span><span class="si">}</span><span class="s1">]</span><span class="se">\n</span><span class="s1">Expected call stack part: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack part: </span><span class="si">{</span><span class="n">call_stack_part</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a>    
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>    <span class="k">def</span> <span class="nf">check_current_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[:</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)]</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>    <span class="k">def</span> <span class="nf">check_whole_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>    <span class="k">def</span> <span class="nf">check_all_tests_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>    <span class="k">def</span> <span class="nf">register_intro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ContextManager</span><span class="p">[</span><span class="n">ValueHolder</span><span class="p">]:</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>        <span class="k">class</span> <span class="nc">RIContextManager</span><span class="p">:</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>            <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">testcasestate</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>            
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>            <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueHolder</span><span class="p">:</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_func_params_with_values</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">((</span><span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>            
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>            <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>                <span class="k">if</span> <span class="n">exc_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">exc_val</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>                <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">)</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos">530</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos">531</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos">532</span></a>        
</span><span id="L-533"><a href="#L-533"><span class="linenos">533</span></a>        <span class="k">return</span> <span class="n">RIContextManager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos">534</span></a>
</span><span id="L-535"><a href="#L-535"><span class="linenos">535</span></a>        <span class="c1"># def context_manager(self: &#39;TestCaseState&#39;):</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos">536</span></a>        <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos">537</span></a>        <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos">538</span></a>        <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos">539</span></a>        <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos">540</span></a>        <span class="c1">#     try:</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos">541</span></a>        <span class="c1">#         yield result_holder</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos">542</span></a>        <span class="c1">#     except:</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos">543</span></a>        <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos">544</span></a>        <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos">545</span></a>        <span class="c1">#             raise</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos">546</span></a>        <span class="c1">#     finally:</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos">547</span></a>        <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos">548</span></a>        <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos">549</span></a>        <span class="c1">#         self.check_current_state_item()</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos">550</span></a>        
</span><span id="L-551"><a href="#L-551"><span class="linenos">551</span></a>        <span class="c1"># return context_manager(self)</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos">552</span></a>
</span><span id="L-553"><a href="#L-553"><span class="linenos">553</span></a>    <span class="c1"># @contextmanager</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos">554</span></a>    <span class="c1"># def register_intro(self, raise_exceptions: Optional[bool] = None) -&gt; ContextManager[ValueHolder]:</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos">555</span></a>    <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos">556</span></a>    <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos">557</span></a>    <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos">558</span></a>    <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos">559</span></a>    <span class="c1">#     try:</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos">560</span></a>    <span class="c1">#         yield result_holder</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos">561</span></a>    <span class="c1">#     except:</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos">562</span></a>    <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos">563</span></a>    <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos">564</span></a>    <span class="c1">#             raise</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos">565</span></a>    <span class="c1">#     finally:</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos">566</span></a>    <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos">567</span></a>    <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos">568</span></a>    <span class="c1">#         self.check_current_state_item()</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos">569</span></a>    
</span><span id="L-570"><a href="#L-570"><span class="linenos">570</span></a>    <span class="n">ri</span> <span class="o">=</span> <span class="n">register_intro</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos">571</span></a>    
</span><span id="L-572"><a href="#L-572"><span class="linenos">572</span></a>    <span class="k">def</span> <span class="nf">register_outro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos">573</span></a>        <span class="n">original_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos">574</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">original_func</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos">575</span></a>            <span class="n">original_func</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">)</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos">576</span></a>
</span><span id="L-577"><a href="#L-577"><span class="linenos">577</span></a>        <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos">578</span></a>            <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos">579</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">awaitable_wrapper</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos">580</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Awaitable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos">581</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos">582</span></a>                        <span class="c1"># code_params_with_values: CodeParamsWithValues = intro_frame_params_with_values(current_entity.cr_frame)</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos">583</span></a>                        <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="nb">dict</span><span class="p">())</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos">584</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos">585</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos">586</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">CodeParamsWithValues</span><span class="p">()</span>
</span><span id="L-587"><a href="#L-587"><span class="linenos">587</span></a>                        <span class="n">result_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos">588</span></a>                        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos">589</span></a>                    
</span><span id="L-590"><a href="#L-590"><span class="linenos">590</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos">591</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos">592</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos">593</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos">594</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos">595</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos">596</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos">597</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos">598</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos">599</span></a>                            <span class="k">raise</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos">600</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos">601</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos">602</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos">603</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos">604</span></a>                
</span><span id="L-605"><a href="#L-605"><span class="linenos">605</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">awaitable_wrapper</span><span class="p">()</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos">606</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos">607</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">async_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos">608</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos">609</span></a>                    <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos">610</span></a>                    <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos">611</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos">612</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos">613</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos">614</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos">615</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos">616</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos">617</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="L-618"><a href="#L-618"><span class="linenos">618</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos">619</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos">620</span></a>                            <span class="k">raise</span>
</span><span id="L-621"><a href="#L-621"><span class="linenos">621</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos">622</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos">623</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos">624</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="L-625"><a href="#L-625"><span class="linenos">625</span></a>                
</span><span id="L-626"><a href="#L-626"><span class="linenos">626</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">async_wrapper</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos">627</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos">628</span></a>            <span class="k">def</span> <span class="nf">sync_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos">629</span></a>                <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos">630</span></a>                <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos">631</span></a>                <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos">632</span></a>                <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos">633</span></a>                <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos">634</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="L-635"><a href="#L-635"><span class="linenos">635</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos">636</span></a>                    <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos">637</span></a>                    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos">638</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos">639</span></a>                    <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos">640</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos">641</span></a>                        <span class="k">raise</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos">642</span></a>                <span class="k">finally</span><span class="p">:</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos">643</span></a>                    <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos">644</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos">645</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos">646</span></a>            
</span><span id="L-647"><a href="#L-647"><span class="linenos">647</span></a>            <span class="n">wrapper</span> <span class="o">=</span> <span class="n">sync_wrapper</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos">648</span></a>        
</span><span id="L-649"><a href="#L-649"><span class="linenos">649</span></a>        <span class="n">original_func_sign</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">Signature</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">original_func</span><span class="p">)</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos">650</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">wrapper</span><span class="p">,</span> <span class="n">original_func</span><span class="p">)</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos">651</span></a>        <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">original_func_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos">652</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos">653</span></a>    
</span><span id="L-654"><a href="#L-654"><span class="linenos">654</span></a>    <span class="n">ro</span> <span class="o">=</span> <span class="n">register_outro</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos">655</span></a>    
</span><span id="L-656"><a href="#L-656"><span class="linenos">656</span></a>    <span class="k">def</span> <span class="nf">register_last_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos">657</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos">658</span></a>        <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos">659</span></a>        <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos">660</span></a>            <span class="k">raise</span> <span class="n">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-661"><a href="#L-661"><span class="linenos">661</span></a>        
</span><span id="L-662"><a href="#L-662"><span class="linenos">662</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos">663</span></a>
</span><span id="L-664"><a href="#L-664"><span class="linenos">664</span></a>    <span class="n">rls</span> <span class="o">=</span> <span class="n">register_last_result</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos">665</span></a>    
</span><span id="L-666"><a href="#L-666"><span class="linenos">666</span></a>    <span class="k">def</span> <span class="nf">register_last_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos">667</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos">668</span></a>        <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos">669</span></a>        <span class="k">if</span> <span class="n">exception_holder</span><span class="p">:</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos">670</span></a>            <span class="k">raise</span> <span class="n">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos">671</span></a>        
</span><span id="L-672"><a href="#L-672"><span class="linenos">672</span></a>        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos">673</span></a>
</span><span id="L-674"><a href="#L-674"><span class="linenos">674</span></a>    <span class="n">rle</span> <span class="o">=</span> <span class="n">register_last_exception</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos">675</span></a>
</span><span id="L-676"><a href="#L-676"><span class="linenos">676</span></a>    <span class="k">def</span> <span class="nf">try_to_load_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos">677</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos">678</span></a><span class="sd">        Will try to load a pickle file with a refference results (an expected_results)</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos">679</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos">680</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">):</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos">681</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos">682</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos">683</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos">684</span></a>    
</span><span id="L-685"><a href="#L-685"><span class="linenos">685</span></a>    <span class="k">def</span> <span class="nf">try_to_save_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos">686</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos">687</span></a><span class="sd">        Will try to save a refference results (an expected_results) to a pickle file. Will not save them if </span>
</span><span id="L-688"><a href="#L-688"><span class="linenos">688</span></a><span class="sd">        pickle file was already successfully loaded with a &#39;FakeResults.try_to_load_expected_call_stack()&#39; call.</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos">689</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos">690</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos">691</span></a>            <span class="k">return</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos">692</span></a>        
</span><span id="L-693"><a href="#L-693"><span class="linenos">693</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)):</span>
</span><span id="L-694"><a href="#L-694"><span class="linenos">694</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos">695</span></a>                <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos">696</span></a>        
</span><span id="L-697"><a href="#L-697"><span class="linenos">697</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)):</span>
</span><span id="L-698"><a href="#L-698"><span class="linenos">698</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos">699</span></a>                <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prepare_readable_content</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">))</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos">700</span></a>    
</span><span id="L-701"><a href="#L-701"><span class="linenos">701</span></a>    <span class="k">def</span> <span class="nf">prepare_readable_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos">702</span></a>        <span class="n">content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos">703</span></a>        <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;# Test Case: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos">704</span></a>        <span class="k">for</span> <span class="n">test_id</span><span class="p">,</span> <span class="n">call_stack</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos">705</span></a>            <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\n</span><span class="s1">## Test ID: </span><span class="si">{</span><span class="n">test_id</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos">706</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">call_state</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">call_stack</span><span class="p">):</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos">707</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\t</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos">708</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">params_with_values</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos">709</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">args: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">args</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos">710</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">kwargs: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">kwargs</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos">711</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span>
</span><span id="L-712"><a href="#L-712"><span class="linenos">712</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">result: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos">713</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos">714</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">exception: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos">715</span></a>        
</span><span id="L-716"><a href="#L-716"><span class="linenos">716</span></a>        <span class="k">return</span> <span class="n">content</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos">717</span></a>    
</span><span id="L-718"><a href="#L-718"><span class="linenos">718</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-719"><a href="#L-719"><span class="linenos">719</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos">720</span></a><span class="sd">        Will register current instance to a global &#39;TEST_CASE_STATE&#39; variable. Will save a previous value</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos">721</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos">722</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">try_to_load_expected_call_stack</span><span class="p">()</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos">723</span></a>
</span><span id="L-724"><a href="#L-724"><span class="linenos">724</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="L-725"><a href="#L-725"><span class="linenos">725</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span> <span class="o">=</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos">726</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos">727</span></a>    
</span><span id="L-728"><a href="#L-728"><span class="linenos">728</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos">729</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="L-730"><a href="#L-730"><span class="linenos">730</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos">731</span></a>
</span><span id="L-732"><a href="#L-732"><span class="linenos">732</span></a>    <span class="k">def</span> <span class="nf">unregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">should_be_saved</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos">733</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos">734</span></a><span class="sd">        Will restore a previous value of the global &#39;TEST_CASE_STATE&#39; variable</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos">735</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos">736</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="L-737"><a href="#L-737"><span class="linenos">737</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos">738</span></a>
</span><span id="L-739"><a href="#L-739"><span class="linenos">739</span></a>        <span class="k">if</span> <span class="n">should_be_saved</span><span class="p">:</span>
</span><span id="L-740"><a href="#L-740"><span class="linenos">740</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">try_to_save_expected_call_stack</span><span class="p">()</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos">741</span></a>
</span><span id="L-742"><a href="#L-742"><span class="linenos">742</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">):</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos">743</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unregister</span><span class="p">((</span><span class="n">exc_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_val</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_tb</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos">744</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-745"><a href="#L-745"><span class="linenos">745</span></a>
</span><span id="L-746"><a href="#L-746"><span class="linenos">746</span></a>
</span><span id="L-747"><a href="#L-747"><span class="linenos">747</span></a>
</span><span id="L-748"><a href="#L-748"><span class="linenos">748</span></a><span class="k">class</span> <span class="nc">StateBase</span><span class="p">:</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos">749</span></a>    <span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">var_name</span><span class="p">:</span> <span class="n">VarName</span><span class="p">,</span> <span class="n">var_value</span><span class="p">:</span> <span class="n">VarValue</span><span class="p">,</span> <span class="n">stage_id</span><span class="p">:</span> <span class="n">StageId</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos">750</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-751"><a href="#L-751"><span class="linenos">751</span></a>    
</span><span id="L-752"><a href="#L-752"><span class="linenos">752</span></a>    <span class="k">def</span> <span class="nf">add_set</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="nb">vars</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">VarName</span><span class="p">,</span> <span class="n">VarValue</span><span class="p">]):</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos">753</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos">754</span></a>    
</span><span id="L-755"><a href="#L-755"><span class="linenos">755</span></a>    <span class="k">def</span> <span class="nf">check_var</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">var_name</span><span class="p">:</span> <span class="n">VarName</span><span class="p">):</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos">756</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos">757</span></a>    
</span><span id="L-758"><a href="#L-758"><span class="linenos">758</span></a>    <span class="k">def</span> <span class="nf">check_var_measurement</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">var_name</span><span class="p">:</span> <span class="n">VarName</span><span class="p">,</span> <span class="n">measurement_id_from</span><span class="p">:</span> <span class="n">MeasurementId</span><span class="p">,</span> <span class="n">measuremente_id_up_to</span><span class="p">:</span> <span class="n">MeasurementId</span><span class="p">):</span>
</span><span id="L-759"><a href="#L-759"><span class="linenos">759</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos">760</span></a>    
</span><span id="L-761"><a href="#L-761"><span class="linenos">761</span></a>    <span class="k">def</span> <span class="nf">check_var_current_state</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">var_name</span><span class="p">:</span> <span class="n">VarName</span><span class="p">):</span>
</span><span id="L-762"><a href="#L-762"><span class="linenos">762</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos">763</span></a>    
</span><span id="L-764"><a href="#L-764"><span class="linenos">764</span></a>    <span class="k">def</span> <span class="nf">check_all</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-765"><a href="#L-765"><span class="linenos">765</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-766"><a href="#L-766"><span class="linenos">766</span></a>    
</span><span id="L-767"><a href="#L-767"><span class="linenos">767</span></a>    <span class="k">def</span> <span class="nf">check_all_current_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos">768</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


            </section>
                <section id="CallState">
                    <div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CallState</span><wbr>(<span class="base">builtins.tuple</span>):

        
    </div>
    <a class="headerlink" href="#CallState"></a>
    
            <div class="docstring"><p>CallState(entity, params_with_values, args, kwargs, result_holder, exception_holder)</p>
</div>


                            <div id="CallState.__init__" class="classattr">
                                <div class="attr function">
            
        <span class="name">CallState</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span>,</span><span class="param">	<span class="n">params_with_values</span>,</span><span class="param">	<span class="n">args</span>,</span><span class="param">	<span class="n">kwargs</span>,</span><span class="param">	<span class="n">result_holder</span>,</span><span class="param">	<span class="n">exception_holder</span></span>)</span>

        
    </div>
    <a class="headerlink" href="#CallState.__init__"></a>
    
            <div class="docstring"><p>Create new instance of CallState(entity, params_with_values, args, kwargs, result_holder, exception_holder)</p>
</div>


                            </div>
                            <div id="CallState.entity" class="classattr">
                                <div class="attr variable">
            <span class="name">entity</span>

        
    </div>
    <a class="headerlink" href="#CallState.entity"></a>
    
            <div class="docstring"><p>Alias for field number 0</p>
</div>


                            </div>
                            <div id="CallState.params_with_values" class="classattr">
                                <div class="attr variable">
            <span class="name">params_with_values</span>

        
    </div>
    <a class="headerlink" href="#CallState.params_with_values"></a>
    
            <div class="docstring"><p>Alias for field number 1</p>
</div>


                            </div>
                            <div id="CallState.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span>

        
    </div>
    <a class="headerlink" href="#CallState.args"></a>
    
            <div class="docstring"><p>Alias for field number 2</p>
</div>


                            </div>
                            <div id="CallState.kwargs" class="classattr">
                                <div class="attr variable">
            <span class="name">kwargs</span>

        
    </div>
    <a class="headerlink" href="#CallState.kwargs"></a>
    
            <div class="docstring"><p>Alias for field number 3</p>
</div>


                            </div>
                            <div id="CallState.result_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">result_holder</span>

        
    </div>
    <a class="headerlink" href="#CallState.result_holder"></a>
    
            <div class="docstring"><p>Alias for field number 4</p>
</div>


                            </div>
                            <div id="CallState.exception_holder" class="classattr">
                                <div class="attr variable">
            <span class="name">exception_holder</span>

        
    </div>
    <a class="headerlink" href="#CallState.exception_holder"></a>
    
            <div class="docstring"><p>Alias for field number 5</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.tuple</dt>
                                <dd id="CallState.index" class="function">index</dd>
                <dd id="CallState.count" class="function">count</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ResultAlreadyRegisteredError">
                            <input id="ResultAlreadyRegisteredError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ResultAlreadyRegisteredError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="ResultAlreadyRegisteredError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ResultAlreadyRegisteredError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ResultAlreadyRegisteredError-388"><a href="#ResultAlreadyRegisteredError-388"><span class="linenos">388</span></a><span class="k">class</span> <span class="nc">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="ResultAlreadyRegisteredError-389"><a href="#ResultAlreadyRegisteredError-389"><span class="linenos">389</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="ResultAlreadyRegisteredError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ResultAlreadyRegisteredError.with_traceback" class="function">with_traceback</dd>
                <dd id="ResultAlreadyRegisteredError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ExceptionAlreadyRegisteredError">
                            <input id="ExceptionAlreadyRegisteredError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExceptionAlreadyRegisteredError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="ExceptionAlreadyRegisteredError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExceptionAlreadyRegisteredError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExceptionAlreadyRegisteredError-392"><a href="#ExceptionAlreadyRegisteredError-392"><span class="linenos">392</span></a><span class="k">class</span> <span class="nc">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="ExceptionAlreadyRegisteredError-393"><a href="#ExceptionAlreadyRegisteredError-393"><span class="linenos">393</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="ExceptionAlreadyRegisteredError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ExceptionAlreadyRegisteredError.with_traceback" class="function">with_traceback</dd>
                <dd id="ExceptionAlreadyRegisteredError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CallStackIsNotEqualError">
                            <input id="CallStackIsNotEqualError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CallStackIsNotEqualError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="CallStackIsNotEqualError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CallStackIsNotEqualError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CallStackIsNotEqualError-396"><a href="#CallStackIsNotEqualError-396"><span class="linenos">396</span></a><span class="k">class</span> <span class="nc">CallStackIsNotEqualError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="CallStackIsNotEqualError-397"><a href="#CallStackIsNotEqualError-397"><span class="linenos">397</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="CallStackIsNotEqualError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="CallStackIsNotEqualError.with_traceback" class="function">with_traceback</dd>
                <dd id="CallStackIsNotEqualError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="ExpectedTestCaseStateIsNotLoadedError">
                            <input id="ExpectedTestCaseStateIsNotLoadedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">ExpectedTestCaseStateIsNotLoadedError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="ExpectedTestCaseStateIsNotLoadedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ExpectedTestCaseStateIsNotLoadedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ExpectedTestCaseStateIsNotLoadedError-400"><a href="#ExpectedTestCaseStateIsNotLoadedError-400"><span class="linenos">400</span></a><span class="k">class</span> <span class="nc">ExpectedTestCaseStateIsNotLoadedError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="ExpectedTestCaseStateIsNotLoadedError-401"><a href="#ExpectedTestCaseStateIsNotLoadedError-401"><span class="linenos">401</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="ExpectedTestCaseStateIsNotLoadedError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="ExpectedTestCaseStateIsNotLoadedError.with_traceback" class="function">with_traceback</dd>
                <dd id="ExpectedTestCaseStateIsNotLoadedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TEST_CASE_STATE">
                    <div class="attr variable">
            <span class="name">TEST_CASE_STATE</span><span class="annotation">: <a href="#TestCaseState">TestCaseState</a></span>        =
<span class="default_value">None</span>

        
    </div>
    <a class="headerlink" href="#TEST_CASE_STATE"></a>
    
    

                </section>
                <section id="get_test_case_state">
                            <input id="get_test_case_state-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_test_case_state</span><span class="signature pdoc-code multiline">(<span class="return-annotation">) -> <span class="n"><a href="#TestCaseState">TestCaseState</a></span>:</span></span>

                <label class="view-source-button" for="get_test_case_state-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_test_case_state"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_test_case_state-407"><a href="#get_test_case_state-407"><span class="linenos">407</span></a><span class="k">def</span> <span class="nf">get_test_case_state</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">:</span>
</span><span id="get_test_case_state-408"><a href="#get_test_case_state-408"><span class="linenos">408</span></a>    <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="get_test_case_state-409"><a href="#get_test_case_state-409"><span class="linenos">409</span></a>    <span class="k">if</span> <span class="n">TEST_CASE_STATE</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_test_case_state-410"><a href="#get_test_case_state-410"><span class="linenos">410</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="n">TestCaseState</span><span class="p">(</span><span class="s1">&#39;Default&#39;</span><span class="p">)</span>
</span><span id="get_test_case_state-411"><a href="#get_test_case_state-411"><span class="linenos">411</span></a>    
</span><span id="get_test_case_state-412"><a href="#get_test_case_state-412"><span class="linenos">412</span></a>    <span class="k">return</span> <span class="n">TEST_CASE_STATE</span>
</span></pre></div>


    

                </section>
                <section id="TestCaseState">
                            <input id="TestCaseState-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TestCaseState</span>:

                <label class="view-source-button" for="TestCaseState-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState-415"><a href="#TestCaseState-415"><span class="linenos">415</span></a><span class="k">class</span> <span class="nc">TestCaseState</span><span class="p">:</span>
</span><span id="TestCaseState-416"><a href="#TestCaseState-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">register</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="TestCaseState-417"><a href="#TestCaseState-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-418"><a href="#TestCaseState-418"><span class="linenos">418</span></a>            <span class="n">parent_entity</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="TestCaseState-419"><a href="#TestCaseState-419"><span class="linenos">419</span></a>            <span class="n">parent_class</span> <span class="o">=</span> <span class="n">entity_class</span><span class="p">(</span><span class="n">parent_entity</span><span class="p">)</span>
</span><span id="TestCaseState-420"><a href="#TestCaseState-420"><span class="linenos">420</span></a>            <span class="n">parent_class_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">parent_class</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="TestCaseState-421"><a href="#TestCaseState-421"><span class="linenos">421</span></a>
</span><span id="TestCaseState-422"><a href="#TestCaseState-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">parent_class_name</span>
</span><span id="TestCaseState-423"><a href="#TestCaseState-423"><span class="linenos">423</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="TestCaseState-424"><a href="#TestCaseState-424"><span class="linenos">424</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState-425"><a href="#TestCaseState-425"><span class="linenos">425</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="TestCaseState-426"><a href="#TestCaseState-426"><span class="linenos">426</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState-427"><a href="#TestCaseState-427"><span class="linenos">427</span></a>        <span class="p">})</span>
</span><span id="TestCaseState-428"><a href="#TestCaseState-428"><span class="linenos">428</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="TestCaseState-429"><a href="#TestCaseState-429"><span class="linenos">429</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState-430"><a href="#TestCaseState-430"><span class="linenos">430</span></a>        <span class="p">})</span>
</span><span id="TestCaseState-431"><a href="#TestCaseState-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TestCaseState-432"><a href="#TestCaseState-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.pickle&#39;</span>
</span><span id="TestCaseState-433"><a href="#TestCaseState-433"><span class="linenos">433</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.md&#39;</span>
</span><span id="TestCaseState-434"><a href="#TestCaseState-434"><span class="linenos">434</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="n">relative_to_src</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="TestCaseState-435"><a href="#TestCaseState-435"><span class="linenos">435</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">)</span>
</span><span id="TestCaseState-436"><a href="#TestCaseState-436"><span class="linenos">436</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">)</span>
</span><span id="TestCaseState-437"><a href="#TestCaseState-437"><span class="linenos">437</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;TestCaseState&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TestCaseState-438"><a href="#TestCaseState-438"><span class="linenos">438</span></a>        <span class="k">if</span> <span class="n">register</span><span class="p">:</span>
</span><span id="TestCaseState-439"><a href="#TestCaseState-439"><span class="linenos">439</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="TestCaseState-440"><a href="#TestCaseState-440"><span class="linenos">440</span></a>
</span><span id="TestCaseState-441"><a href="#TestCaseState-441"><span class="linenos">441</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState-442"><a href="#TestCaseState-442"><span class="linenos">442</span></a>    <span class="k">def</span> <span class="nf">current_test_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Hashable</span><span class="p">:</span>
</span><span id="TestCaseState-443"><a href="#TestCaseState-443"><span class="linenos">443</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span>
</span><span id="TestCaseState-444"><a href="#TestCaseState-444"><span class="linenos">444</span></a>    
</span><span id="TestCaseState-445"><a href="#TestCaseState-445"><span class="linenos">445</span></a>    <span class="nd">@current_test_id</span><span class="o">.</span><span class="n">setter</span>
</span><span id="TestCaseState-446"><a href="#TestCaseState-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">current_test_id</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-447"><a href="#TestCaseState-447"><span class="linenos">447</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="TestCaseState-448"><a href="#TestCaseState-448"><span class="linenos">448</span></a>        <span class="k">if</span> <span class="n">value</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">:</span>
</span><span id="TestCaseState-449"><a href="#TestCaseState-449"><span class="linenos">449</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">[</span><span class="n">value</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState-450"><a href="#TestCaseState-450"><span class="linenos">450</span></a>    
</span><span id="TestCaseState-451"><a href="#TestCaseState-451"><span class="linenos">451</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState-452"><a href="#TestCaseState-452"><span class="linenos">452</span></a>    <span class="k">def</span> <span class="nf">call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="TestCaseState-453"><a href="#TestCaseState-453"><span class="linenos">453</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span><span id="TestCaseState-454"><a href="#TestCaseState-454"><span class="linenos">454</span></a>    
</span><span id="TestCaseState-455"><a href="#TestCaseState-455"><span class="linenos">455</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState-456"><a href="#TestCaseState-456"><span class="linenos">456</span></a>    <span class="k">def</span> <span class="nf">expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="TestCaseState-457"><a href="#TestCaseState-457"><span class="linenos">457</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState-458"><a href="#TestCaseState-458"><span class="linenos">458</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span><span id="TestCaseState-459"><a href="#TestCaseState-459"><span class="linenos">459</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="TestCaseState-460"><a href="#TestCaseState-460"><span class="linenos">460</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState-461"><a href="#TestCaseState-461"><span class="linenos">461</span></a>
</span><span id="TestCaseState-462"><a href="#TestCaseState-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">is_loaded</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TestCaseState-463"><a href="#TestCaseState-463"><span class="linenos">463</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="TestCaseState-464"><a href="#TestCaseState-464"><span class="linenos">464</span></a>            <span class="k">raise</span> <span class="n">ExpectedTestCaseStateIsNotLoadedError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected test case state is not loaded: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-465"><a href="#TestCaseState-465"><span class="linenos">465</span></a>    
</span><span id="TestCaseState-466"><a href="#TestCaseState-466"><span class="linenos">466</span></a>    <span class="k">def</span> <span class="nf">check_current_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-467"><a href="#TestCaseState-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-468"><a href="#TestCaseState-468"><span class="linenos">468</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState-469"><a href="#TestCaseState-469"><span class="linenos">469</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState-470"><a href="#TestCaseState-470"><span class="linenos">470</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="TestCaseState-471"><a href="#TestCaseState-471"><span class="linenos">471</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Current call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-472"><a href="#TestCaseState-472"><span class="linenos">472</span></a>    
</span><span id="TestCaseState-473"><a href="#TestCaseState-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">check_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="TestCaseState-474"><a href="#TestCaseState-474"><span class="linenos">474</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-475"><a href="#TestCaseState-475"><span class="linenos">475</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="TestCaseState-476"><a href="#TestCaseState-476"><span class="linenos">476</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="TestCaseState-477"><a href="#TestCaseState-477"><span class="linenos">477</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="TestCaseState-478"><a href="#TestCaseState-478"><span class="linenos">478</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: </span><span class="si">{</span><span class="n">item_index</span><span class="si">}</span><span class="se">\n</span><span class="s1">Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-479"><a href="#TestCaseState-479"><span class="linenos">479</span></a>    
</span><span id="TestCaseState-480"><a href="#TestCaseState-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">check_state_range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_start_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">item_end_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="TestCaseState-481"><a href="#TestCaseState-481"><span class="linenos">481</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-482"><a href="#TestCaseState-482"><span class="linenos">482</span></a>        <span class="n">call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="TestCaseState-483"><a href="#TestCaseState-483"><span class="linenos">483</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="TestCaseState-484"><a href="#TestCaseState-484"><span class="linenos">484</span></a>        <span class="k">if</span> <span class="n">call_stack_part</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="TestCaseState-485"><a href="#TestCaseState-485"><span class="linenos">485</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: [</span><span class="si">{</span><span class="n">item_start_index</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="n">item_end_index</span><span class="si">}</span><span class="s1">]</span><span class="se">\n</span><span class="s1">Expected call stack part: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack part: </span><span class="si">{</span><span class="n">call_stack_part</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-486"><a href="#TestCaseState-486"><span class="linenos">486</span></a>    
</span><span id="TestCaseState-487"><a href="#TestCaseState-487"><span class="linenos">487</span></a>    <span class="k">def</span> <span class="nf">check_current_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-488"><a href="#TestCaseState-488"><span class="linenos">488</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-489"><a href="#TestCaseState-489"><span class="linenos">489</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[:</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)]</span>
</span><span id="TestCaseState-490"><a href="#TestCaseState-490"><span class="linenos">490</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="TestCaseState-491"><a href="#TestCaseState-491"><span class="linenos">491</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-492"><a href="#TestCaseState-492"><span class="linenos">492</span></a>
</span><span id="TestCaseState-493"><a href="#TestCaseState-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="nf">check_whole_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-494"><a href="#TestCaseState-494"><span class="linenos">494</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-495"><a href="#TestCaseState-495"><span class="linenos">495</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">:</span>
</span><span id="TestCaseState-496"><a href="#TestCaseState-496"><span class="linenos">496</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-497"><a href="#TestCaseState-497"><span class="linenos">497</span></a>
</span><span id="TestCaseState-498"><a href="#TestCaseState-498"><span class="linenos">498</span></a>    <span class="k">def</span> <span class="nf">check_all_tests_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-499"><a href="#TestCaseState-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState-500"><a href="#TestCaseState-500"><span class="linenos">500</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span>
</span><span id="TestCaseState-501"><a href="#TestCaseState-501"><span class="linenos">501</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-502"><a href="#TestCaseState-502"><span class="linenos">502</span></a>
</span><span id="TestCaseState-503"><a href="#TestCaseState-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">register_intro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ContextManager</span><span class="p">[</span><span class="n">ValueHolder</span><span class="p">]:</span>
</span><span id="TestCaseState-504"><a href="#TestCaseState-504"><span class="linenos">504</span></a>        <span class="k">class</span> <span class="nc">RIContextManager</span><span class="p">:</span>
</span><span id="TestCaseState-505"><a href="#TestCaseState-505"><span class="linenos">505</span></a>            <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-506"><a href="#TestCaseState-506"><span class="linenos">506</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">testcasestate</span>
</span><span id="TestCaseState-507"><a href="#TestCaseState-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState-508"><a href="#TestCaseState-508"><span class="linenos">508</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState-509"><a href="#TestCaseState-509"><span class="linenos">509</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-510"><a href="#TestCaseState-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-511"><a href="#TestCaseState-511"><span class="linenos">511</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState-512"><a href="#TestCaseState-512"><span class="linenos">512</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState-513"><a href="#TestCaseState-513"><span class="linenos">513</span></a>            
</span><span id="TestCaseState-514"><a href="#TestCaseState-514"><span class="linenos">514</span></a>            <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueHolder</span><span class="p">:</span>
</span><span id="TestCaseState-515"><a href="#TestCaseState-515"><span class="linenos">515</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState-516"><a href="#TestCaseState-516"><span class="linenos">516</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_func_params_with_values</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState-517"><a href="#TestCaseState-517"><span class="linenos">517</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="TestCaseState-518"><a href="#TestCaseState-518"><span class="linenos">518</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">((</span><span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="TestCaseState-519"><a href="#TestCaseState-519"><span class="linenos">519</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="TestCaseState-520"><a href="#TestCaseState-520"><span class="linenos">520</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState-521"><a href="#TestCaseState-521"><span class="linenos">521</span></a>            
</span><span id="TestCaseState-522"><a href="#TestCaseState-522"><span class="linenos">522</span></a>            <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-523"><a href="#TestCaseState-523"><span class="linenos">523</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState-524"><a href="#TestCaseState-524"><span class="linenos">524</span></a>                <span class="k">if</span> <span class="n">exc_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-525"><a href="#TestCaseState-525"><span class="linenos">525</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">exc_val</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="TestCaseState-526"><a href="#TestCaseState-526"><span class="linenos">526</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState-527"><a href="#TestCaseState-527"><span class="linenos">527</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TestCaseState-528"><a href="#TestCaseState-528"><span class="linenos">528</span></a>
</span><span id="TestCaseState-529"><a href="#TestCaseState-529"><span class="linenos">529</span></a>                <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState-530"><a href="#TestCaseState-530"><span class="linenos">530</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState-531"><a href="#TestCaseState-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState-532"><a href="#TestCaseState-532"><span class="linenos">532</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState-533"><a href="#TestCaseState-533"><span class="linenos">533</span></a>        
</span><span id="TestCaseState-534"><a href="#TestCaseState-534"><span class="linenos">534</span></a>        <span class="k">return</span> <span class="n">RIContextManager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="TestCaseState-535"><a href="#TestCaseState-535"><span class="linenos">535</span></a>
</span><span id="TestCaseState-536"><a href="#TestCaseState-536"><span class="linenos">536</span></a>        <span class="c1"># def context_manager(self: &#39;TestCaseState&#39;):</span>
</span><span id="TestCaseState-537"><a href="#TestCaseState-537"><span class="linenos">537</span></a>        <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="TestCaseState-538"><a href="#TestCaseState-538"><span class="linenos">538</span></a>        <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="TestCaseState-539"><a href="#TestCaseState-539"><span class="linenos">539</span></a>        <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState-540"><a href="#TestCaseState-540"><span class="linenos">540</span></a>        <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState-541"><a href="#TestCaseState-541"><span class="linenos">541</span></a>        <span class="c1">#     try:</span>
</span><span id="TestCaseState-542"><a href="#TestCaseState-542"><span class="linenos">542</span></a>        <span class="c1">#         yield result_holder</span>
</span><span id="TestCaseState-543"><a href="#TestCaseState-543"><span class="linenos">543</span></a>        <span class="c1">#     except:</span>
</span><span id="TestCaseState-544"><a href="#TestCaseState-544"><span class="linenos">544</span></a>        <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="TestCaseState-545"><a href="#TestCaseState-545"><span class="linenos">545</span></a>        <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="TestCaseState-546"><a href="#TestCaseState-546"><span class="linenos">546</span></a>        <span class="c1">#             raise</span>
</span><span id="TestCaseState-547"><a href="#TestCaseState-547"><span class="linenos">547</span></a>        <span class="c1">#     finally:</span>
</span><span id="TestCaseState-548"><a href="#TestCaseState-548"><span class="linenos">548</span></a>        <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="TestCaseState-549"><a href="#TestCaseState-549"><span class="linenos">549</span></a>        <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="TestCaseState-550"><a href="#TestCaseState-550"><span class="linenos">550</span></a>        <span class="c1">#         self.check_current_state_item()</span>
</span><span id="TestCaseState-551"><a href="#TestCaseState-551"><span class="linenos">551</span></a>        
</span><span id="TestCaseState-552"><a href="#TestCaseState-552"><span class="linenos">552</span></a>        <span class="c1"># return context_manager(self)</span>
</span><span id="TestCaseState-553"><a href="#TestCaseState-553"><span class="linenos">553</span></a>
</span><span id="TestCaseState-554"><a href="#TestCaseState-554"><span class="linenos">554</span></a>    <span class="c1"># @contextmanager</span>
</span><span id="TestCaseState-555"><a href="#TestCaseState-555"><span class="linenos">555</span></a>    <span class="c1"># def register_intro(self, raise_exceptions: Optional[bool] = None) -&gt; ContextManager[ValueHolder]:</span>
</span><span id="TestCaseState-556"><a href="#TestCaseState-556"><span class="linenos">556</span></a>    <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="TestCaseState-557"><a href="#TestCaseState-557"><span class="linenos">557</span></a>    <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="TestCaseState-558"><a href="#TestCaseState-558"><span class="linenos">558</span></a>    <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState-559"><a href="#TestCaseState-559"><span class="linenos">559</span></a>    <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState-560"><a href="#TestCaseState-560"><span class="linenos">560</span></a>    <span class="c1">#     try:</span>
</span><span id="TestCaseState-561"><a href="#TestCaseState-561"><span class="linenos">561</span></a>    <span class="c1">#         yield result_holder</span>
</span><span id="TestCaseState-562"><a href="#TestCaseState-562"><span class="linenos">562</span></a>    <span class="c1">#     except:</span>
</span><span id="TestCaseState-563"><a href="#TestCaseState-563"><span class="linenos">563</span></a>    <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="TestCaseState-564"><a href="#TestCaseState-564"><span class="linenos">564</span></a>    <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="TestCaseState-565"><a href="#TestCaseState-565"><span class="linenos">565</span></a>    <span class="c1">#             raise</span>
</span><span id="TestCaseState-566"><a href="#TestCaseState-566"><span class="linenos">566</span></a>    <span class="c1">#     finally:</span>
</span><span id="TestCaseState-567"><a href="#TestCaseState-567"><span class="linenos">567</span></a>    <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="TestCaseState-568"><a href="#TestCaseState-568"><span class="linenos">568</span></a>    <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="TestCaseState-569"><a href="#TestCaseState-569"><span class="linenos">569</span></a>    <span class="c1">#         self.check_current_state_item()</span>
</span><span id="TestCaseState-570"><a href="#TestCaseState-570"><span class="linenos">570</span></a>    
</span><span id="TestCaseState-571"><a href="#TestCaseState-571"><span class="linenos">571</span></a>    <span class="n">ri</span> <span class="o">=</span> <span class="n">register_intro</span>
</span><span id="TestCaseState-572"><a href="#TestCaseState-572"><span class="linenos">572</span></a>    
</span><span id="TestCaseState-573"><a href="#TestCaseState-573"><span class="linenos">573</span></a>    <span class="k">def</span> <span class="nf">register_outro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="TestCaseState-574"><a href="#TestCaseState-574"><span class="linenos">574</span></a>        <span class="n">original_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState-575"><a href="#TestCaseState-575"><span class="linenos">575</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">original_func</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState-576"><a href="#TestCaseState-576"><span class="linenos">576</span></a>            <span class="n">original_func</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">)</span>
</span><span id="TestCaseState-577"><a href="#TestCaseState-577"><span class="linenos">577</span></a>
</span><span id="TestCaseState-578"><a href="#TestCaseState-578"><span class="linenos">578</span></a>        <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState-579"><a href="#TestCaseState-579"><span class="linenos">579</span></a>            <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState-580"><a href="#TestCaseState-580"><span class="linenos">580</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">awaitable_wrapper</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState-581"><a href="#TestCaseState-581"><span class="linenos">581</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Awaitable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState-582"><a href="#TestCaseState-582"><span class="linenos">582</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState-583"><a href="#TestCaseState-583"><span class="linenos">583</span></a>                        <span class="c1"># code_params_with_values: CodeParamsWithValues = intro_frame_params_with_values(current_entity.cr_frame)</span>
</span><span id="TestCaseState-584"><a href="#TestCaseState-584"><span class="linenos">584</span></a>                        <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="nb">dict</span><span class="p">())</span>
</span><span id="TestCaseState-585"><a href="#TestCaseState-585"><span class="linenos">585</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState-586"><a href="#TestCaseState-586"><span class="linenos">586</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState-587"><a href="#TestCaseState-587"><span class="linenos">587</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">CodeParamsWithValues</span><span class="p">()</span>
</span><span id="TestCaseState-588"><a href="#TestCaseState-588"><span class="linenos">588</span></a>                        <span class="n">result_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState-589"><a href="#TestCaseState-589"><span class="linenos">589</span></a>                        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState-590"><a href="#TestCaseState-590"><span class="linenos">590</span></a>                    
</span><span id="TestCaseState-591"><a href="#TestCaseState-591"><span class="linenos">591</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-592"><a href="#TestCaseState-592"><span class="linenos">592</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-593"><a href="#TestCaseState-593"><span class="linenos">593</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState-594"><a href="#TestCaseState-594"><span class="linenos">594</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span>
</span><span id="TestCaseState-595"><a href="#TestCaseState-595"><span class="linenos">595</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState-596"><a href="#TestCaseState-596"><span class="linenos">596</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState-597"><a href="#TestCaseState-597"><span class="linenos">597</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState-598"><a href="#TestCaseState-598"><span class="linenos">598</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState-599"><a href="#TestCaseState-599"><span class="linenos">599</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState-600"><a href="#TestCaseState-600"><span class="linenos">600</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState-601"><a href="#TestCaseState-601"><span class="linenos">601</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState-602"><a href="#TestCaseState-602"><span class="linenos">602</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState-603"><a href="#TestCaseState-603"><span class="linenos">603</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState-604"><a href="#TestCaseState-604"><span class="linenos">604</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState-605"><a href="#TestCaseState-605"><span class="linenos">605</span></a>                
</span><span id="TestCaseState-606"><a href="#TestCaseState-606"><span class="linenos">606</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">awaitable_wrapper</span><span class="p">()</span>
</span><span id="TestCaseState-607"><a href="#TestCaseState-607"><span class="linenos">607</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState-608"><a href="#TestCaseState-608"><span class="linenos">608</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">async_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState-609"><a href="#TestCaseState-609"><span class="linenos">609</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState-610"><a href="#TestCaseState-610"><span class="linenos">610</span></a>                    <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState-611"><a href="#TestCaseState-611"><span class="linenos">611</span></a>                    <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState-612"><a href="#TestCaseState-612"><span class="linenos">612</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-613"><a href="#TestCaseState-613"><span class="linenos">613</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-614"><a href="#TestCaseState-614"><span class="linenos">614</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState-615"><a href="#TestCaseState-615"><span class="linenos">615</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState-616"><a href="#TestCaseState-616"><span class="linenos">616</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState-617"><a href="#TestCaseState-617"><span class="linenos">617</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState-618"><a href="#TestCaseState-618"><span class="linenos">618</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState-619"><a href="#TestCaseState-619"><span class="linenos">619</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState-620"><a href="#TestCaseState-620"><span class="linenos">620</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState-621"><a href="#TestCaseState-621"><span class="linenos">621</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState-622"><a href="#TestCaseState-622"><span class="linenos">622</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState-623"><a href="#TestCaseState-623"><span class="linenos">623</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState-624"><a href="#TestCaseState-624"><span class="linenos">624</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState-625"><a href="#TestCaseState-625"><span class="linenos">625</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState-626"><a href="#TestCaseState-626"><span class="linenos">626</span></a>                
</span><span id="TestCaseState-627"><a href="#TestCaseState-627"><span class="linenos">627</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">async_wrapper</span>
</span><span id="TestCaseState-628"><a href="#TestCaseState-628"><span class="linenos">628</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState-629"><a href="#TestCaseState-629"><span class="linenos">629</span></a>            <span class="k">def</span> <span class="nf">sync_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState-630"><a href="#TestCaseState-630"><span class="linenos">630</span></a>                <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState-631"><a href="#TestCaseState-631"><span class="linenos">631</span></a>                <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState-632"><a href="#TestCaseState-632"><span class="linenos">632</span></a>                <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState-633"><a href="#TestCaseState-633"><span class="linenos">633</span></a>                <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-634"><a href="#TestCaseState-634"><span class="linenos">634</span></a>                <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState-635"><a href="#TestCaseState-635"><span class="linenos">635</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState-636"><a href="#TestCaseState-636"><span class="linenos">636</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState-637"><a href="#TestCaseState-637"><span class="linenos">637</span></a>                    <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState-638"><a href="#TestCaseState-638"><span class="linenos">638</span></a>                    <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState-639"><a href="#TestCaseState-639"><span class="linenos">639</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState-640"><a href="#TestCaseState-640"><span class="linenos">640</span></a>                    <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState-641"><a href="#TestCaseState-641"><span class="linenos">641</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState-642"><a href="#TestCaseState-642"><span class="linenos">642</span></a>                        <span class="k">raise</span>
</span><span id="TestCaseState-643"><a href="#TestCaseState-643"><span class="linenos">643</span></a>                <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState-644"><a href="#TestCaseState-644"><span class="linenos">644</span></a>                    <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState-645"><a href="#TestCaseState-645"><span class="linenos">645</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState-646"><a href="#TestCaseState-646"><span class="linenos">646</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState-647"><a href="#TestCaseState-647"><span class="linenos">647</span></a>            
</span><span id="TestCaseState-648"><a href="#TestCaseState-648"><span class="linenos">648</span></a>            <span class="n">wrapper</span> <span class="o">=</span> <span class="n">sync_wrapper</span>
</span><span id="TestCaseState-649"><a href="#TestCaseState-649"><span class="linenos">649</span></a>        
</span><span id="TestCaseState-650"><a href="#TestCaseState-650"><span class="linenos">650</span></a>        <span class="n">original_func_sign</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">Signature</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState-651"><a href="#TestCaseState-651"><span class="linenos">651</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">wrapper</span><span class="p">,</span> <span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState-652"><a href="#TestCaseState-652"><span class="linenos">652</span></a>        <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">original_func_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="TestCaseState-653"><a href="#TestCaseState-653"><span class="linenos">653</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="TestCaseState-654"><a href="#TestCaseState-654"><span class="linenos">654</span></a>    
</span><span id="TestCaseState-655"><a href="#TestCaseState-655"><span class="linenos">655</span></a>    <span class="n">ro</span> <span class="o">=</span> <span class="n">register_outro</span>
</span><span id="TestCaseState-656"><a href="#TestCaseState-656"><span class="linenos">656</span></a>    
</span><span id="TestCaseState-657"><a href="#TestCaseState-657"><span class="linenos">657</span></a>    <span class="k">def</span> <span class="nf">register_last_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-658"><a href="#TestCaseState-658"><span class="linenos">658</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState-659"><a href="#TestCaseState-659"><span class="linenos">659</span></a>        <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState-660"><a href="#TestCaseState-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="TestCaseState-661"><a href="#TestCaseState-661"><span class="linenos">661</span></a>            <span class="k">raise</span> <span class="n">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-662"><a href="#TestCaseState-662"><span class="linenos">662</span></a>        
</span><span id="TestCaseState-663"><a href="#TestCaseState-663"><span class="linenos">663</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState-664"><a href="#TestCaseState-664"><span class="linenos">664</span></a>
</span><span id="TestCaseState-665"><a href="#TestCaseState-665"><span class="linenos">665</span></a>    <span class="n">rls</span> <span class="o">=</span> <span class="n">register_last_result</span>
</span><span id="TestCaseState-666"><a href="#TestCaseState-666"><span class="linenos">666</span></a>    
</span><span id="TestCaseState-667"><a href="#TestCaseState-667"><span class="linenos">667</span></a>    <span class="k">def</span> <span class="nf">register_last_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-668"><a href="#TestCaseState-668"><span class="linenos">668</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState-669"><a href="#TestCaseState-669"><span class="linenos">669</span></a>        <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState-670"><a href="#TestCaseState-670"><span class="linenos">670</span></a>        <span class="k">if</span> <span class="n">exception_holder</span><span class="p">:</span>
</span><span id="TestCaseState-671"><a href="#TestCaseState-671"><span class="linenos">671</span></a>            <span class="k">raise</span> <span class="n">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState-672"><a href="#TestCaseState-672"><span class="linenos">672</span></a>        
</span><span id="TestCaseState-673"><a href="#TestCaseState-673"><span class="linenos">673</span></a>        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState-674"><a href="#TestCaseState-674"><span class="linenos">674</span></a>
</span><span id="TestCaseState-675"><a href="#TestCaseState-675"><span class="linenos">675</span></a>    <span class="n">rle</span> <span class="o">=</span> <span class="n">register_last_exception</span>
</span><span id="TestCaseState-676"><a href="#TestCaseState-676"><span class="linenos">676</span></a>
</span><span id="TestCaseState-677"><a href="#TestCaseState-677"><span class="linenos">677</span></a>    <span class="k">def</span> <span class="nf">try_to_load_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-678"><a href="#TestCaseState-678"><span class="linenos">678</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState-679"><a href="#TestCaseState-679"><span class="linenos">679</span></a><span class="sd">        Will try to load a pickle file with a refference results (an expected_results)</span>
</span><span id="TestCaseState-680"><a href="#TestCaseState-680"><span class="linenos">680</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState-681"><a href="#TestCaseState-681"><span class="linenos">681</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">):</span>
</span><span id="TestCaseState-682"><a href="#TestCaseState-682"><span class="linenos">682</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState-683"><a href="#TestCaseState-683"><span class="linenos">683</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="TestCaseState-684"><a href="#TestCaseState-684"><span class="linenos">684</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TestCaseState-685"><a href="#TestCaseState-685"><span class="linenos">685</span></a>    
</span><span id="TestCaseState-686"><a href="#TestCaseState-686"><span class="linenos">686</span></a>    <span class="k">def</span> <span class="nf">try_to_save_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState-687"><a href="#TestCaseState-687"><span class="linenos">687</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState-688"><a href="#TestCaseState-688"><span class="linenos">688</span></a><span class="sd">        Will try to save a refference results (an expected_results) to a pickle file. Will not save them if </span>
</span><span id="TestCaseState-689"><a href="#TestCaseState-689"><span class="linenos">689</span></a><span class="sd">        pickle file was already successfully loaded with a &#39;FakeResults.try_to_load_expected_call_stack()&#39; call.</span>
</span><span id="TestCaseState-690"><a href="#TestCaseState-690"><span class="linenos">690</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState-691"><a href="#TestCaseState-691"><span class="linenos">691</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="TestCaseState-692"><a href="#TestCaseState-692"><span class="linenos">692</span></a>            <span class="k">return</span>
</span><span id="TestCaseState-693"><a href="#TestCaseState-693"><span class="linenos">693</span></a>        
</span><span id="TestCaseState-694"><a href="#TestCaseState-694"><span class="linenos">694</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)):</span>
</span><span id="TestCaseState-695"><a href="#TestCaseState-695"><span class="linenos">695</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState-696"><a href="#TestCaseState-696"><span class="linenos">696</span></a>                <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>
</span><span id="TestCaseState-697"><a href="#TestCaseState-697"><span class="linenos">697</span></a>        
</span><span id="TestCaseState-698"><a href="#TestCaseState-698"><span class="linenos">698</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)):</span>
</span><span id="TestCaseState-699"><a href="#TestCaseState-699"><span class="linenos">699</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState-700"><a href="#TestCaseState-700"><span class="linenos">700</span></a>                <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prepare_readable_content</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">))</span>
</span><span id="TestCaseState-701"><a href="#TestCaseState-701"><span class="linenos">701</span></a>    
</span><span id="TestCaseState-702"><a href="#TestCaseState-702"><span class="linenos">702</span></a>    <span class="k">def</span> <span class="nf">prepare_readable_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TestCaseState-703"><a href="#TestCaseState-703"><span class="linenos">703</span></a>        <span class="n">content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="TestCaseState-704"><a href="#TestCaseState-704"><span class="linenos">704</span></a>        <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;# Test Case: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-705"><a href="#TestCaseState-705"><span class="linenos">705</span></a>        <span class="k">for</span> <span class="n">test_id</span><span class="p">,</span> <span class="n">call_stack</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TestCaseState-706"><a href="#TestCaseState-706"><span class="linenos">706</span></a>            <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\n</span><span class="s1">## Test ID: </span><span class="si">{</span><span class="n">test_id</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-707"><a href="#TestCaseState-707"><span class="linenos">707</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">call_state</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">call_stack</span><span class="p">):</span>
</span><span id="TestCaseState-708"><a href="#TestCaseState-708"><span class="linenos">708</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\t</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-709"><a href="#TestCaseState-709"><span class="linenos">709</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">params_with_values</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-710"><a href="#TestCaseState-710"><span class="linenos">710</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">args: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">args</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-711"><a href="#TestCaseState-711"><span class="linenos">711</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">kwargs: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">kwargs</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-712"><a href="#TestCaseState-712"><span class="linenos">712</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span>
</span><span id="TestCaseState-713"><a href="#TestCaseState-713"><span class="linenos">713</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">result: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-714"><a href="#TestCaseState-714"><span class="linenos">714</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span>
</span><span id="TestCaseState-715"><a href="#TestCaseState-715"><span class="linenos">715</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">exception: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState-716"><a href="#TestCaseState-716"><span class="linenos">716</span></a>        
</span><span id="TestCaseState-717"><a href="#TestCaseState-717"><span class="linenos">717</span></a>        <span class="k">return</span> <span class="n">content</span>
</span><span id="TestCaseState-718"><a href="#TestCaseState-718"><span class="linenos">718</span></a>    
</span><span id="TestCaseState-719"><a href="#TestCaseState-719"><span class="linenos">719</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-720"><a href="#TestCaseState-720"><span class="linenos">720</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState-721"><a href="#TestCaseState-721"><span class="linenos">721</span></a><span class="sd">        Will register current instance to a global &#39;TEST_CASE_STATE&#39; variable. Will save a previous value</span>
</span><span id="TestCaseState-722"><a href="#TestCaseState-722"><span class="linenos">722</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState-723"><a href="#TestCaseState-723"><span class="linenos">723</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">try_to_load_expected_call_stack</span><span class="p">()</span>
</span><span id="TestCaseState-724"><a href="#TestCaseState-724"><span class="linenos">724</span></a>
</span><span id="TestCaseState-725"><a href="#TestCaseState-725"><span class="linenos">725</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState-726"><a href="#TestCaseState-726"><span class="linenos">726</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span> <span class="o">=</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState-727"><a href="#TestCaseState-727"><span class="linenos">727</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span>
</span><span id="TestCaseState-728"><a href="#TestCaseState-728"><span class="linenos">728</span></a>    
</span><span id="TestCaseState-729"><a href="#TestCaseState-729"><span class="linenos">729</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState-730"><a href="#TestCaseState-730"><span class="linenos">730</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span><span id="TestCaseState-731"><a href="#TestCaseState-731"><span class="linenos">731</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="TestCaseState-732"><a href="#TestCaseState-732"><span class="linenos">732</span></a>
</span><span id="TestCaseState-733"><a href="#TestCaseState-733"><span class="linenos">733</span></a>    <span class="k">def</span> <span class="nf">unregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">should_be_saved</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="TestCaseState-734"><a href="#TestCaseState-734"><span class="linenos">734</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState-735"><a href="#TestCaseState-735"><span class="linenos">735</span></a><span class="sd">        Will restore a previous value of the global &#39;TEST_CASE_STATE&#39; variable</span>
</span><span id="TestCaseState-736"><a href="#TestCaseState-736"><span class="linenos">736</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState-737"><a href="#TestCaseState-737"><span class="linenos">737</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState-738"><a href="#TestCaseState-738"><span class="linenos">738</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span>
</span><span id="TestCaseState-739"><a href="#TestCaseState-739"><span class="linenos">739</span></a>
</span><span id="TestCaseState-740"><a href="#TestCaseState-740"><span class="linenos">740</span></a>        <span class="k">if</span> <span class="n">should_be_saved</span><span class="p">:</span>
</span><span id="TestCaseState-741"><a href="#TestCaseState-741"><span class="linenos">741</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">try_to_save_expected_call_stack</span><span class="p">()</span>
</span><span id="TestCaseState-742"><a href="#TestCaseState-742"><span class="linenos">742</span></a>
</span><span id="TestCaseState-743"><a href="#TestCaseState-743"><span class="linenos">743</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">):</span>
</span><span id="TestCaseState-744"><a href="#TestCaseState-744"><span class="linenos">744</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">unregister</span><span class="p">((</span><span class="n">exc_type</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_val</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">exc_tb</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">))</span>
</span><span id="TestCaseState-745"><a href="#TestCaseState-745"><span class="linenos">745</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            <div id="TestCaseState.__init__" class="classattr">
                                        <input id="TestCaseState.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TestCaseState</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">register</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">depth</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span>)</span>

                <label class="view-source-button" for="TestCaseState.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.__init__-416"><a href="#TestCaseState.__init__-416"><span class="linenos">416</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">register</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="TestCaseState.__init__-417"><a href="#TestCaseState.__init__-417"><span class="linenos">417</span></a>        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.__init__-418"><a href="#TestCaseState.__init__-418"><span class="linenos">418</span></a>            <span class="n">parent_entity</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-419"><a href="#TestCaseState.__init__-419"><span class="linenos">419</span></a>            <span class="n">parent_class</span> <span class="o">=</span> <span class="n">entity_class</span><span class="p">(</span><span class="n">parent_entity</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-420"><a href="#TestCaseState.__init__-420"><span class="linenos">420</span></a>            <span class="n">parent_class_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">parent_class</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="TestCaseState.__init__-421"><a href="#TestCaseState.__init__-421"><span class="linenos">421</span></a>
</span><span id="TestCaseState.__init__-422"><a href="#TestCaseState.__init__-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">name</span> <span class="ow">or</span> <span class="n">parent_class_name</span>
</span><span id="TestCaseState.__init__-423"><a href="#TestCaseState.__init__-423"><span class="linenos">423</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="n">raise_exceptions</span>
</span><span id="TestCaseState.__init__-424"><a href="#TestCaseState.__init__-424"><span class="linenos">424</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.__init__-425"><a href="#TestCaseState.__init__-425"><span class="linenos">425</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="TestCaseState.__init__-426"><a href="#TestCaseState.__init__-426"><span class="linenos">426</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState.__init__-427"><a href="#TestCaseState.__init__-427"><span class="linenos">427</span></a>        <span class="p">})</span>
</span><span id="TestCaseState.__init__-428"><a href="#TestCaseState.__init__-428"><span class="linenos">428</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span> <span class="n">OrderedDict</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]]</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">({</span>
</span><span id="TestCaseState.__init__-429"><a href="#TestCaseState.__init__-429"><span class="linenos">429</span></a>            <span class="kc">None</span><span class="p">:</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TestCaseState.__init__-430"><a href="#TestCaseState.__init__-430"><span class="linenos">430</span></a>        <span class="p">})</span>
</span><span id="TestCaseState.__init__-431"><a href="#TestCaseState.__init__-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TestCaseState.__init__-432"><a href="#TestCaseState.__init__-432"><span class="linenos">432</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.pickle&#39;</span>
</span><span id="TestCaseState.__init__-433"><a href="#TestCaseState.__init__-433"><span class="linenos">433</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">__test_case_state.md&#39;</span>
</span><span id="TestCaseState.__init__-434"><a href="#TestCaseState.__init__-434"><span class="linenos">434</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">:</span> <span class="n">RelativePath</span> <span class="o">=</span> <span class="n">relative_to_src</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-435"><a href="#TestCaseState.__init__-435"><span class="linenos">435</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_file_name</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-436"><a href="#TestCaseState.__init__-436"><span class="linenos">436</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">content_dir_rel</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_file_name</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-437"><a href="#TestCaseState.__init__-437"><span class="linenos">437</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="s1">&#39;TestCaseState&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TestCaseState.__init__-438"><a href="#TestCaseState.__init__-438"><span class="linenos">438</span></a>        <span class="k">if</span> <span class="n">register</span><span class="p">:</span>
</span><span id="TestCaseState.__init__-439"><a href="#TestCaseState.__init__-439"><span class="linenos">439</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.name" class="classattr">
                                <div class="attr variable">
            <span class="name">name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.name"></a>
    
    

                            </div>
                            <div id="TestCaseState.raise_exceptions" class="classattr">
                                <div class="attr variable">
            <span class="name">raise_exceptions</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.raise_exceptions"></a>
    
    

                            </div>
                            <div id="TestCaseState.call_stack_per_test" class="classattr">
                                <div class="attr variable">
            <span class="name">call_stack_per_test</span><span class="annotation">: &#39;OrderedDict[(Hashable, List[CallState])]&#39;</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.call_stack_per_test"></a>
    
    

                            </div>
                            <div id="TestCaseState.expected_call_stack_per_test" class="classattr">
                                <div class="attr variable">
            <span class="name">expected_call_stack_per_test</span><span class="annotation">: &#39;OrderedDict[(Hashable, List[CallState])]&#39;</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.expected_call_stack_per_test"></a>
    
    

                            </div>
                            <div id="TestCaseState.loaded" class="classattr">
                                <div class="attr variable">
            <span class="name">loaded</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.loaded"></a>
    
    

                            </div>
                            <div id="TestCaseState.content_file_name" class="classattr">
                                <div class="attr variable">
            <span class="name">content_file_name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.content_file_name"></a>
    
    

                            </div>
                            <div id="TestCaseState.readable_content_file_name" class="classattr">
                                <div class="attr variable">
            <span class="name">readable_content_file_name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.readable_content_file_name"></a>
    
    

                            </div>
                            <div id="TestCaseState.content_dir_rel" class="classattr">
                                <div class="attr variable">
            <span class="name">content_dir_rel</span><span class="annotation">: cengal.file_system.path_manager.versions.v_0.path_manager.RelativePath</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.content_dir_rel"></a>
    
    

                            </div>
                            <div id="TestCaseState.content_full_file_name" class="classattr">
                                <div class="attr variable">
            <span class="name">content_full_file_name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.content_full_file_name"></a>
    
    

                            </div>
                            <div id="TestCaseState.readable_content_full_file_name" class="classattr">
                                <div class="attr variable">
            <span class="name">readable_content_full_file_name</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.readable_content_full_file_name"></a>
    
    

                            </div>
                            <div id="TestCaseState.old_global_fake_result" class="classattr">
                                <div class="attr variable">
            <span class="name">old_global_fake_result</span><span class="annotation">: <a href="#TestCaseState">TestCaseState</a></span>

        
    </div>
    <a class="headerlink" href="#TestCaseState.old_global_fake_result"></a>
    
    

                            </div>
                            <div id="TestCaseState.current_test_id" class="classattr">
                                        <input id="TestCaseState.current_test_id-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">current_test_id</span><span class="annotation">: Hashable</span>

                <label class="view-source-button" for="TestCaseState.current_test_id-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.current_test_id"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.current_test_id-441"><a href="#TestCaseState.current_test_id-441"><span class="linenos">441</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState.current_test_id-442"><a href="#TestCaseState.current_test_id-442"><span class="linenos">442</span></a>    <span class="k">def</span> <span class="nf">current_test_id</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Hashable</span><span class="p">:</span>
</span><span id="TestCaseState.current_test_id-443"><a href="#TestCaseState.current_test_id-443"><span class="linenos">443</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_current_test_id</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.call_stack" class="classattr">
                                        <input id="TestCaseState.call_stack-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">call_stack</span><span class="annotation">: List[<a href="#CallState">CallState</a>]</span>

                <label class="view-source-button" for="TestCaseState.call_stack-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.call_stack"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.call_stack-451"><a href="#TestCaseState.call_stack-451"><span class="linenos">451</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState.call_stack-452"><a href="#TestCaseState.call_stack-452"><span class="linenos">452</span></a>    <span class="k">def</span> <span class="nf">call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="TestCaseState.call_stack-453"><a href="#TestCaseState.call_stack-453"><span class="linenos">453</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.expected_call_stack" class="classattr">
                                        <input id="TestCaseState.expected_call_stack-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">expected_call_stack</span><span class="annotation">: List[<a href="#CallState">CallState</a>]</span>

                <label class="view-source-button" for="TestCaseState.expected_call_stack-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.expected_call_stack"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.expected_call_stack-455"><a href="#TestCaseState.expected_call_stack-455"><span class="linenos">455</span></a>    <span class="nd">@property</span>
</span><span id="TestCaseState.expected_call_stack-456"><a href="#TestCaseState.expected_call_stack-456"><span class="linenos">456</span></a>    <span class="k">def</span> <span class="nf">expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]:</span>
</span><span id="TestCaseState.expected_call_stack-457"><a href="#TestCaseState.expected_call_stack-457"><span class="linenos">457</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.expected_call_stack-458"><a href="#TestCaseState.expected_call_stack-458"><span class="linenos">458</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">current_test_id</span><span class="p">]</span>
</span><span id="TestCaseState.expected_call_stack-459"><a href="#TestCaseState.expected_call_stack-459"><span class="linenos">459</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="TestCaseState.expected_call_stack-460"><a href="#TestCaseState.expected_call_stack-460"><span class="linenos">460</span></a>            <span class="k">return</span> <span class="nb">list</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.is_loaded" class="classattr">
                                        <input id="TestCaseState.is_loaded-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_loaded</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.is_loaded-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.is_loaded"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.is_loaded-462"><a href="#TestCaseState.is_loaded-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">is_loaded</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TestCaseState.is_loaded-463"><a href="#TestCaseState.is_loaded-463"><span class="linenos">463</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="TestCaseState.is_loaded-464"><a href="#TestCaseState.is_loaded-464"><span class="linenos">464</span></a>            <span class="k">raise</span> <span class="n">ExpectedTestCaseStateIsNotLoadedError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected test case state is not loaded: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_current_state_item" class="classattr">
                                        <input id="TestCaseState.check_current_state_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_current_state_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_current_state_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_current_state_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_current_state_item-466"><a href="#TestCaseState.check_current_state_item-466"><span class="linenos">466</span></a>    <span class="k">def</span> <span class="nf">check_current_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState.check_current_state_item-467"><a href="#TestCaseState.check_current_state_item-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_current_state_item-468"><a href="#TestCaseState.check_current_state_item-468"><span class="linenos">468</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.check_current_state_item-469"><a href="#TestCaseState.check_current_state_item-469"><span class="linenos">469</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.check_current_state_item-470"><a href="#TestCaseState.check_current_state_item-470"><span class="linenos">470</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="TestCaseState.check_current_state_item-471"><a href="#TestCaseState.check_current_state_item-471"><span class="linenos">471</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Current call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_state_item" class="classattr">
                                        <input id="TestCaseState.check_state_item-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_state_item</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">item_index</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_state_item-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_state_item"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_state_item-473"><a href="#TestCaseState.check_state_item-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">check_state_item</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="TestCaseState.check_state_item-474"><a href="#TestCaseState.check_state_item-474"><span class="linenos">474</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_state_item-475"><a href="#TestCaseState.check_state_item-475"><span class="linenos">475</span></a>        <span class="n">call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="TestCaseState.check_state_item-476"><a href="#TestCaseState.check_state_item-476"><span class="linenos">476</span></a>        <span class="n">expected_call_stack_item</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_index</span><span class="p">]</span>
</span><span id="TestCaseState.check_state_item-477"><a href="#TestCaseState.check_state_item-477"><span class="linenos">477</span></a>        <span class="k">if</span> <span class="n">call_stack_item</span> <span class="o">!=</span> <span class="n">expected_call_stack_item</span><span class="p">:</span>
</span><span id="TestCaseState.check_state_item-478"><a href="#TestCaseState.check_state_item-478"><span class="linenos">478</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: </span><span class="si">{</span><span class="n">item_index</span><span class="si">}</span><span class="se">\n</span><span class="s1">Expected call stack item: </span><span class="si">{</span><span class="n">expected_call_stack_item</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack item: </span><span class="si">{</span><span class="n">call_stack_item</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_state_range" class="classattr">
                                        <input id="TestCaseState.check_state_range-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_state_range</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">item_start_index</span><span class="p">:</span> <span class="nb">int</span>, </span><span class="param"><span class="n">item_end_index</span><span class="p">:</span> <span class="nb">int</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_state_range-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_state_range"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_state_range-480"><a href="#TestCaseState.check_state_range-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">check_state_range</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item_start_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">item_end_index</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
</span><span id="TestCaseState.check_state_range-481"><a href="#TestCaseState.check_state_range-481"><span class="linenos">481</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_state_range-482"><a href="#TestCaseState.check_state_range-482"><span class="linenos">482</span></a>        <span class="n">call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="TestCaseState.check_state_range-483"><a href="#TestCaseState.check_state_range-483"><span class="linenos">483</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[</span><span class="n">item_start_index</span><span class="p">:</span> <span class="n">item_end_index</span><span class="p">]</span>
</span><span id="TestCaseState.check_state_range-484"><a href="#TestCaseState.check_state_range-484"><span class="linenos">484</span></a>        <span class="k">if</span> <span class="n">call_stack_part</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="TestCaseState.check_state_range-485"><a href="#TestCaseState.check_state_range-485"><span class="linenos">485</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Index: [</span><span class="si">{</span><span class="n">item_start_index</span><span class="si">}</span><span class="s1">:</span><span class="si">{</span><span class="n">item_end_index</span><span class="si">}</span><span class="s1">]</span><span class="se">\n</span><span class="s1">Expected call stack part: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack part: </span><span class="si">{</span><span class="n">call_stack_part</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_current_state" class="classattr">
                                        <input id="TestCaseState.check_current_state-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_current_state</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_current_state-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_current_state"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_current_state-487"><a href="#TestCaseState.check_current_state-487"><span class="linenos">487</span></a>    <span class="k">def</span> <span class="nf">check_current_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState.check_current_state-488"><a href="#TestCaseState.check_current_state-488"><span class="linenos">488</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_current_state-489"><a href="#TestCaseState.check_current_state-489"><span class="linenos">489</span></a>        <span class="n">expected_call_stack_part</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">CallState</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">[:</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">)]</span>
</span><span id="TestCaseState.check_current_state-490"><a href="#TestCaseState.check_current_state-490"><span class="linenos">490</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="n">expected_call_stack_part</span><span class="p">:</span>
</span><span id="TestCaseState.check_current_state-491"><a href="#TestCaseState.check_current_state-491"><span class="linenos">491</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="n">expected_call_stack_part</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_whole_state" class="classattr">
                                        <input id="TestCaseState.check_whole_state-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_whole_state</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_whole_state-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_whole_state"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_whole_state-493"><a href="#TestCaseState.check_whole_state-493"><span class="linenos">493</span></a>    <span class="k">def</span> <span class="nf">check_whole_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState.check_whole_state-494"><a href="#TestCaseState.check_whole_state-494"><span class="linenos">494</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_whole_state-495"><a href="#TestCaseState.check_whole_state-495"><span class="linenos">495</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="p">:</span>
</span><span id="TestCaseState.check_whole_state-496"><a href="#TestCaseState.check_whole_state-496"><span class="linenos">496</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stack: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.check_all_tests_state" class="classattr">
                                        <input id="TestCaseState.check_all_tests_state-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">check_all_tests_state</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.check_all_tests_state-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.check_all_tests_state"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.check_all_tests_state-498"><a href="#TestCaseState.check_all_tests_state-498"><span class="linenos">498</span></a>    <span class="k">def</span> <span class="nf">check_all_tests_state</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState.check_all_tests_state-499"><a href="#TestCaseState.check_all_tests_state-499"><span class="linenos">499</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_loaded</span><span class="p">()</span>
</span><span id="TestCaseState.check_all_tests_state-500"><a href="#TestCaseState.check_all_tests_state-500"><span class="linenos">500</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="p">:</span>
</span><span id="TestCaseState.check_all_tests_state-501"><a href="#TestCaseState.check_all_tests_state-501"><span class="linenos">501</span></a>            <span class="k">raise</span> <span class="n">CallStackIsNotEqualError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Expected call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span><span class="si">}</span><span class="se">\n</span><span class="s1">Actual call stacks: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.register_intro" class="classattr">
                                        <input id="TestCaseState.register_intro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_intro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueHolder</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.register_intro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.register_intro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.register_intro-503"><a href="#TestCaseState.register_intro-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">register_intro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ContextManager</span><span class="p">[</span><span class="n">ValueHolder</span><span class="p">]:</span>
</span><span id="TestCaseState.register_intro-504"><a href="#TestCaseState.register_intro-504"><span class="linenos">504</span></a>        <span class="k">class</span> <span class="nc">RIContextManager</span><span class="p">:</span>
</span><span id="TestCaseState.register_intro-505"><a href="#TestCaseState.register_intro-505"><span class="linenos">505</span></a>            <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.register_intro-506"><a href="#TestCaseState.register_intro-506"><span class="linenos">506</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">testcasestate</span>
</span><span id="TestCaseState.register_intro-507"><a href="#TestCaseState.register_intro-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.register_intro-508"><a href="#TestCaseState.register_intro-508"><span class="linenos">508</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.register_intro-509"><a href="#TestCaseState.register_intro-509"><span class="linenos">509</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_intro-510"><a href="#TestCaseState.register_intro-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_intro-511"><a href="#TestCaseState.register_intro-511"><span class="linenos">511</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState.register_intro-512"><a href="#TestCaseState.register_intro-512"><span class="linenos">512</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState.register_intro-513"><a href="#TestCaseState.register_intro-513"><span class="linenos">513</span></a>            
</span><span id="TestCaseState.register_intro-514"><a href="#TestCaseState.register_intro-514"><span class="linenos">514</span></a>            <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueHolder</span><span class="p">:</span>
</span><span id="TestCaseState.register_intro-515"><a href="#TestCaseState.register_intro-515"><span class="linenos">515</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-516"><a href="#TestCaseState.register_intro-516"><span class="linenos">516</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_func_params_with_values</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-517"><a href="#TestCaseState.register_intro-517"><span class="linenos">517</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="TestCaseState.register_intro-518"><a href="#TestCaseState.register_intro-518"><span class="linenos">518</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">((</span><span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="TestCaseState.register_intro-519"><a href="#TestCaseState.register_intro-519"><span class="linenos">519</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-520"><a href="#TestCaseState.register_intro-520"><span class="linenos">520</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.register_intro-521"><a href="#TestCaseState.register_intro-521"><span class="linenos">521</span></a>            
</span><span id="TestCaseState.register_intro-522"><a href="#TestCaseState.register_intro-522"><span class="linenos">522</span></a>            <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.register_intro-523"><a href="#TestCaseState.register_intro-523"><span class="linenos">523</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.register_intro-524"><a href="#TestCaseState.register_intro-524"><span class="linenos">524</span></a>                <span class="k">if</span> <span class="n">exc_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.register_intro-525"><a href="#TestCaseState.register_intro-525"><span class="linenos">525</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">exc_val</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-526"><a href="#TestCaseState.register_intro-526"><span class="linenos">526</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.register_intro-527"><a href="#TestCaseState.register_intro-527"><span class="linenos">527</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TestCaseState.register_intro-528"><a href="#TestCaseState.register_intro-528"><span class="linenos">528</span></a>
</span><span id="TestCaseState.register_intro-529"><a href="#TestCaseState.register_intro-529"><span class="linenos">529</span></a>                <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-530"><a href="#TestCaseState.register_intro-530"><span class="linenos">530</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-531"><a href="#TestCaseState.register_intro-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.register_intro-532"><a href="#TestCaseState.register_intro-532"><span class="linenos">532</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.register_intro-533"><a href="#TestCaseState.register_intro-533"><span class="linenos">533</span></a>        
</span><span id="TestCaseState.register_intro-534"><a href="#TestCaseState.register_intro-534"><span class="linenos">534</span></a>        <span class="k">return</span> <span class="n">RIContextManager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="TestCaseState.register_intro-535"><a href="#TestCaseState.register_intro-535"><span class="linenos">535</span></a>
</span><span id="TestCaseState.register_intro-536"><a href="#TestCaseState.register_intro-536"><span class="linenos">536</span></a>        <span class="c1"># def context_manager(self: &#39;TestCaseState&#39;):</span>
</span><span id="TestCaseState.register_intro-537"><a href="#TestCaseState.register_intro-537"><span class="linenos">537</span></a>        <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="TestCaseState.register_intro-538"><a href="#TestCaseState.register_intro-538"><span class="linenos">538</span></a>        <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="TestCaseState.register_intro-539"><a href="#TestCaseState.register_intro-539"><span class="linenos">539</span></a>        <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState.register_intro-540"><a href="#TestCaseState.register_intro-540"><span class="linenos">540</span></a>        <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState.register_intro-541"><a href="#TestCaseState.register_intro-541"><span class="linenos">541</span></a>        <span class="c1">#     try:</span>
</span><span id="TestCaseState.register_intro-542"><a href="#TestCaseState.register_intro-542"><span class="linenos">542</span></a>        <span class="c1">#         yield result_holder</span>
</span><span id="TestCaseState.register_intro-543"><a href="#TestCaseState.register_intro-543"><span class="linenos">543</span></a>        <span class="c1">#     except:</span>
</span><span id="TestCaseState.register_intro-544"><a href="#TestCaseState.register_intro-544"><span class="linenos">544</span></a>        <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="TestCaseState.register_intro-545"><a href="#TestCaseState.register_intro-545"><span class="linenos">545</span></a>        <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="TestCaseState.register_intro-546"><a href="#TestCaseState.register_intro-546"><span class="linenos">546</span></a>        <span class="c1">#             raise</span>
</span><span id="TestCaseState.register_intro-547"><a href="#TestCaseState.register_intro-547"><span class="linenos">547</span></a>        <span class="c1">#     finally:</span>
</span><span id="TestCaseState.register_intro-548"><a href="#TestCaseState.register_intro-548"><span class="linenos">548</span></a>        <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="TestCaseState.register_intro-549"><a href="#TestCaseState.register_intro-549"><span class="linenos">549</span></a>        <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="TestCaseState.register_intro-550"><a href="#TestCaseState.register_intro-550"><span class="linenos">550</span></a>        <span class="c1">#         self.check_current_state_item()</span>
</span><span id="TestCaseState.register_intro-551"><a href="#TestCaseState.register_intro-551"><span class="linenos">551</span></a>        
</span><span id="TestCaseState.register_intro-552"><a href="#TestCaseState.register_intro-552"><span class="linenos">552</span></a>        <span class="c1"># return context_manager(self)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.ri" class="classattr">
                                        <input id="TestCaseState.ri-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ri</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">AbstractContextManager</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_2</span><span class="o">.</span><span class="n">smart_values</span><span class="o">.</span><span class="n">ValueHolder</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.ri-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.ri"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.ri-503"><a href="#TestCaseState.ri-503"><span class="linenos">503</span></a>    <span class="k">def</span> <span class="nf">register_intro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ContextManager</span><span class="p">[</span><span class="n">ValueHolder</span><span class="p">]:</span>
</span><span id="TestCaseState.ri-504"><a href="#TestCaseState.ri-504"><span class="linenos">504</span></a>        <span class="k">class</span> <span class="nc">RIContextManager</span><span class="p">:</span>
</span><span id="TestCaseState.ri-505"><a href="#TestCaseState.ri-505"><span class="linenos">505</span></a>            <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.ri-506"><a href="#TestCaseState.ri-506"><span class="linenos">506</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="p">:</span> <span class="s1">&#39;TestCaseState&#39;</span> <span class="o">=</span> <span class="n">testcasestate</span>
</span><span id="TestCaseState.ri-507"><a href="#TestCaseState.ri-507"><span class="linenos">507</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.ri-508"><a href="#TestCaseState.ri-508"><span class="linenos">508</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.ri-509"><a href="#TestCaseState.ri-509"><span class="linenos">509</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ri-510"><a href="#TestCaseState.ri-510"><span class="linenos">510</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ri-511"><a href="#TestCaseState.ri-511"><span class="linenos">511</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState.ri-512"><a href="#TestCaseState.ri-512"><span class="linenos">512</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState.ri-513"><a href="#TestCaseState.ri-513"><span class="linenos">513</span></a>            
</span><span id="TestCaseState.ri-514"><a href="#TestCaseState.ri-514"><span class="linenos">514</span></a>            <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ValueHolder</span><span class="p">:</span>
</span><span id="TestCaseState.ri-515"><a href="#TestCaseState.ri-515"><span class="linenos">515</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">find_current_entity</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState.ri-516"><a href="#TestCaseState.ri-516"><span class="linenos">516</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_func_params_with_values</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TestCaseState.ri-517"><a href="#TestCaseState.ri-517"><span class="linenos">517</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="TestCaseState.ri-518"><a href="#TestCaseState.ri-518"><span class="linenos">518</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">((</span><span class="n">arg</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">))</span>
</span><span id="TestCaseState.ri-519"><a href="#TestCaseState.ri-519"><span class="linenos">519</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="o">.</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="TestCaseState.ri-520"><a href="#TestCaseState.ri-520"><span class="linenos">520</span></a>                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.ri-521"><a href="#TestCaseState.ri-521"><span class="linenos">521</span></a>            
</span><span id="TestCaseState.ri-522"><a href="#TestCaseState.ri-522"><span class="linenos">522</span></a>            <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.ri-523"><a href="#TestCaseState.ri-523"><span class="linenos">523</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TestCaseState.ri-524"><a href="#TestCaseState.ri-524"><span class="linenos">524</span></a>                <span class="k">if</span> <span class="n">exc_type</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.ri-525"><a href="#TestCaseState.ri-525"><span class="linenos">525</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">exc_val</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">exc_tb</span><span class="p">)</span>
</span><span id="TestCaseState.ri-526"><a href="#TestCaseState.ri-526"><span class="linenos">526</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.ri-527"><a href="#TestCaseState.ri-527"><span class="linenos">527</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TestCaseState.ri-528"><a href="#TestCaseState.ri-528"><span class="linenos">528</span></a>
</span><span id="TestCaseState.ri-529"><a href="#TestCaseState.ri-529"><span class="linenos">529</span></a>                <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">current_entity</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">code_params_with_values</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">kwargs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_holder</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.ri-530"><a href="#TestCaseState.ri-530"><span class="linenos">530</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.ri-531"><a href="#TestCaseState.ri-531"><span class="linenos">531</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">testcasestate</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.ri-532"><a href="#TestCaseState.ri-532"><span class="linenos">532</span></a>                <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.ri-533"><a href="#TestCaseState.ri-533"><span class="linenos">533</span></a>        
</span><span id="TestCaseState.ri-534"><a href="#TestCaseState.ri-534"><span class="linenos">534</span></a>        <span class="k">return</span> <span class="n">RIContextManager</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="TestCaseState.ri-535"><a href="#TestCaseState.ri-535"><span class="linenos">535</span></a>
</span><span id="TestCaseState.ri-536"><a href="#TestCaseState.ri-536"><span class="linenos">536</span></a>        <span class="c1"># def context_manager(self: &#39;TestCaseState&#39;):</span>
</span><span id="TestCaseState.ri-537"><a href="#TestCaseState.ri-537"><span class="linenos">537</span></a>        <span class="c1">#     current_entity: Callable = find_current_entity(2)</span>
</span><span id="TestCaseState.ri-538"><a href="#TestCaseState.ri-538"><span class="linenos">538</span></a>        <span class="c1">#     code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)</span>
</span><span id="TestCaseState.ri-539"><a href="#TestCaseState.ri-539"><span class="linenos">539</span></a>        <span class="c1">#     result_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState.ri-540"><a href="#TestCaseState.ri-540"><span class="linenos">540</span></a>        <span class="c1">#     exception_holder: ValueHolder = ValueHolder()</span>
</span><span id="TestCaseState.ri-541"><a href="#TestCaseState.ri-541"><span class="linenos">541</span></a>        <span class="c1">#     try:</span>
</span><span id="TestCaseState.ri-542"><a href="#TestCaseState.ri-542"><span class="linenos">542</span></a>        <span class="c1">#         yield result_holder</span>
</span><span id="TestCaseState.ri-543"><a href="#TestCaseState.ri-543"><span class="linenos">543</span></a>        <span class="c1">#     except:</span>
</span><span id="TestCaseState.ri-544"><a href="#TestCaseState.ri-544"><span class="linenos">544</span></a>        <span class="c1">#         exception_holder.value = get_exception()</span>
</span><span id="TestCaseState.ri-545"><a href="#TestCaseState.ri-545"><span class="linenos">545</span></a>        <span class="c1">#         if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):</span>
</span><span id="TestCaseState.ri-546"><a href="#TestCaseState.ri-546"><span class="linenos">546</span></a>        <span class="c1">#             raise</span>
</span><span id="TestCaseState.ri-547"><a href="#TestCaseState.ri-547"><span class="linenos">547</span></a>        <span class="c1">#     finally:</span>
</span><span id="TestCaseState.ri-548"><a href="#TestCaseState.ri-548"><span class="linenos">548</span></a>        <span class="c1">#         current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)</span>
</span><span id="TestCaseState.ri-549"><a href="#TestCaseState.ri-549"><span class="linenos">549</span></a>        <span class="c1">#         self.call_stack.append(current_call_state)</span>
</span><span id="TestCaseState.ri-550"><a href="#TestCaseState.ri-550"><span class="linenos">550</span></a>        <span class="c1">#         self.check_current_state_item()</span>
</span><span id="TestCaseState.ri-551"><a href="#TestCaseState.ri-551"><span class="linenos">551</span></a>        
</span><span id="TestCaseState.ri-552"><a href="#TestCaseState.ri-552"><span class="linenos">552</span></a>        <span class="c1"># return context_manager(self)</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.register_outro" class="classattr">
                                        <input id="TestCaseState.register_outro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_outro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">func</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.register_outro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.register_outro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.register_outro-573"><a href="#TestCaseState.register_outro-573"><span class="linenos">573</span></a>    <span class="k">def</span> <span class="nf">register_outro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-574"><a href="#TestCaseState.register_outro-574"><span class="linenos">574</span></a>        <span class="n">original_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.register_outro-575"><a href="#TestCaseState.register_outro-575"><span class="linenos">575</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">original_func</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-576"><a href="#TestCaseState.register_outro-576"><span class="linenos">576</span></a>            <span class="n">original_func</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-577"><a href="#TestCaseState.register_outro-577"><span class="linenos">577</span></a>
</span><span id="TestCaseState.register_outro-578"><a href="#TestCaseState.register_outro-578"><span class="linenos">578</span></a>        <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-579"><a href="#TestCaseState.register_outro-579"><span class="linenos">579</span></a>            <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-580"><a href="#TestCaseState.register_outro-580"><span class="linenos">580</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">awaitable_wrapper</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-581"><a href="#TestCaseState.register_outro-581"><span class="linenos">581</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Awaitable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.register_outro-582"><a href="#TestCaseState.register_outro-582"><span class="linenos">582</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-583"><a href="#TestCaseState.register_outro-583"><span class="linenos">583</span></a>                        <span class="c1"># code_params_with_values: CodeParamsWithValues = intro_frame_params_with_values(current_entity.cr_frame)</span>
</span><span id="TestCaseState.register_outro-584"><a href="#TestCaseState.register_outro-584"><span class="linenos">584</span></a>                        <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="nb">dict</span><span class="p">())</span>
</span><span id="TestCaseState.register_outro-585"><a href="#TestCaseState.register_outro-585"><span class="linenos">585</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-586"><a href="#TestCaseState.register_outro-586"><span class="linenos">586</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-587"><a href="#TestCaseState.register_outro-587"><span class="linenos">587</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">CodeParamsWithValues</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-588"><a href="#TestCaseState.register_outro-588"><span class="linenos">588</span></a>                        <span class="n">result_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-589"><a href="#TestCaseState.register_outro-589"><span class="linenos">589</span></a>                        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-590"><a href="#TestCaseState.register_outro-590"><span class="linenos">590</span></a>                    
</span><span id="TestCaseState.register_outro-591"><a href="#TestCaseState.register_outro-591"><span class="linenos">591</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-592"><a href="#TestCaseState.register_outro-592"><span class="linenos">592</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-593"><a href="#TestCaseState.register_outro-593"><span class="linenos">593</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-594"><a href="#TestCaseState.register_outro-594"><span class="linenos">594</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span>
</span><span id="TestCaseState.register_outro-595"><a href="#TestCaseState.register_outro-595"><span class="linenos">595</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-596"><a href="#TestCaseState.register_outro-596"><span class="linenos">596</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-597"><a href="#TestCaseState.register_outro-597"><span class="linenos">597</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-598"><a href="#TestCaseState.register_outro-598"><span class="linenos">598</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-599"><a href="#TestCaseState.register_outro-599"><span class="linenos">599</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-600"><a href="#TestCaseState.register_outro-600"><span class="linenos">600</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState.register_outro-601"><a href="#TestCaseState.register_outro-601"><span class="linenos">601</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-602"><a href="#TestCaseState.register_outro-602"><span class="linenos">602</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-603"><a href="#TestCaseState.register_outro-603"><span class="linenos">603</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-604"><a href="#TestCaseState.register_outro-604"><span class="linenos">604</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-605"><a href="#TestCaseState.register_outro-605"><span class="linenos">605</span></a>                
</span><span id="TestCaseState.register_outro-606"><a href="#TestCaseState.register_outro-606"><span class="linenos">606</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">awaitable_wrapper</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-607"><a href="#TestCaseState.register_outro-607"><span class="linenos">607</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-608"><a href="#TestCaseState.register_outro-608"><span class="linenos">608</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">async_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-609"><a href="#TestCaseState.register_outro-609"><span class="linenos">609</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.register_outro-610"><a href="#TestCaseState.register_outro-610"><span class="linenos">610</span></a>                    <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-611"><a href="#TestCaseState.register_outro-611"><span class="linenos">611</span></a>                    <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-612"><a href="#TestCaseState.register_outro-612"><span class="linenos">612</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-613"><a href="#TestCaseState.register_outro-613"><span class="linenos">613</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-614"><a href="#TestCaseState.register_outro-614"><span class="linenos">614</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-615"><a href="#TestCaseState.register_outro-615"><span class="linenos">615</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-616"><a href="#TestCaseState.register_outro-616"><span class="linenos">616</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-617"><a href="#TestCaseState.register_outro-617"><span class="linenos">617</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-618"><a href="#TestCaseState.register_outro-618"><span class="linenos">618</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-619"><a href="#TestCaseState.register_outro-619"><span class="linenos">619</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-620"><a href="#TestCaseState.register_outro-620"><span class="linenos">620</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-621"><a href="#TestCaseState.register_outro-621"><span class="linenos">621</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState.register_outro-622"><a href="#TestCaseState.register_outro-622"><span class="linenos">622</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-623"><a href="#TestCaseState.register_outro-623"><span class="linenos">623</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-624"><a href="#TestCaseState.register_outro-624"><span class="linenos">624</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-625"><a href="#TestCaseState.register_outro-625"><span class="linenos">625</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-626"><a href="#TestCaseState.register_outro-626"><span class="linenos">626</span></a>                
</span><span id="TestCaseState.register_outro-627"><a href="#TestCaseState.register_outro-627"><span class="linenos">627</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">async_wrapper</span>
</span><span id="TestCaseState.register_outro-628"><a href="#TestCaseState.register_outro-628"><span class="linenos">628</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-629"><a href="#TestCaseState.register_outro-629"><span class="linenos">629</span></a>            <span class="k">def</span> <span class="nf">sync_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-630"><a href="#TestCaseState.register_outro-630"><span class="linenos">630</span></a>                <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.register_outro-631"><a href="#TestCaseState.register_outro-631"><span class="linenos">631</span></a>                <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-632"><a href="#TestCaseState.register_outro-632"><span class="linenos">632</span></a>                <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-633"><a href="#TestCaseState.register_outro-633"><span class="linenos">633</span></a>                <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-634"><a href="#TestCaseState.register_outro-634"><span class="linenos">634</span></a>                <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-635"><a href="#TestCaseState.register_outro-635"><span class="linenos">635</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-636"><a href="#TestCaseState.register_outro-636"><span class="linenos">636</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-637"><a href="#TestCaseState.register_outro-637"><span class="linenos">637</span></a>                    <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-638"><a href="#TestCaseState.register_outro-638"><span class="linenos">638</span></a>                    <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.register_outro-639"><a href="#TestCaseState.register_outro-639"><span class="linenos">639</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-640"><a href="#TestCaseState.register_outro-640"><span class="linenos">640</span></a>                    <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-641"><a href="#TestCaseState.register_outro-641"><span class="linenos">641</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.register_outro-642"><a href="#TestCaseState.register_outro-642"><span class="linenos">642</span></a>                        <span class="k">raise</span>
</span><span id="TestCaseState.register_outro-643"><a href="#TestCaseState.register_outro-643"><span class="linenos">643</span></a>                <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.register_outro-644"><a href="#TestCaseState.register_outro-644"><span class="linenos">644</span></a>                    <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-645"><a href="#TestCaseState.register_outro-645"><span class="linenos">645</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-646"><a href="#TestCaseState.register_outro-646"><span class="linenos">646</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.register_outro-647"><a href="#TestCaseState.register_outro-647"><span class="linenos">647</span></a>            
</span><span id="TestCaseState.register_outro-648"><a href="#TestCaseState.register_outro-648"><span class="linenos">648</span></a>            <span class="n">wrapper</span> <span class="o">=</span> <span class="n">sync_wrapper</span>
</span><span id="TestCaseState.register_outro-649"><a href="#TestCaseState.register_outro-649"><span class="linenos">649</span></a>        
</span><span id="TestCaseState.register_outro-650"><a href="#TestCaseState.register_outro-650"><span class="linenos">650</span></a>        <span class="n">original_func_sign</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">Signature</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-651"><a href="#TestCaseState.register_outro-651"><span class="linenos">651</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">wrapper</span><span class="p">,</span> <span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-652"><a href="#TestCaseState.register_outro-652"><span class="linenos">652</span></a>        <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">original_func_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="TestCaseState.register_outro-653"><a href="#TestCaseState.register_outro-653"><span class="linenos">653</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.ro" class="classattr">
                                        <input id="TestCaseState.ro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">func</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bool</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.ro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.ro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.ro-573"><a href="#TestCaseState.ro-573"><span class="linenos">573</span></a>    <span class="k">def</span> <span class="nf">register_outro</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">raise_exceptions</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="TestCaseState.ro-574"><a href="#TestCaseState.ro-574"><span class="linenos">574</span></a>        <span class="n">original_func</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.ro-575"><a href="#TestCaseState.ro-575"><span class="linenos">575</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">original_func</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState.ro-576"><a href="#TestCaseState.ro-576"><span class="linenos">576</span></a>            <span class="n">original_func</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">)</span>
</span><span id="TestCaseState.ro-577"><a href="#TestCaseState.ro-577"><span class="linenos">577</span></a>
</span><span id="TestCaseState.ro-578"><a href="#TestCaseState.ro-578"><span class="linenos">578</span></a>        <span class="k">if</span> <span class="n">is_async</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState.ro-579"><a href="#TestCaseState.ro-579"><span class="linenos">579</span></a>            <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="TestCaseState.ro-580"><a href="#TestCaseState.ro-580"><span class="linenos">580</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">awaitable_wrapper</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.ro-581"><a href="#TestCaseState.ro-581"><span class="linenos">581</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Awaitable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.ro-582"><a href="#TestCaseState.ro-582"><span class="linenos">582</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="s1">&#39;cr_frame&#39;</span><span class="p">):</span>
</span><span id="TestCaseState.ro-583"><a href="#TestCaseState.ro-583"><span class="linenos">583</span></a>                        <span class="c1"># code_params_with_values: CodeParamsWithValues = intro_frame_params_with_values(current_entity.cr_frame)</span>
</span><span id="TestCaseState.ro-584"><a href="#TestCaseState.ro-584"><span class="linenos">584</span></a>                        <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">find_entity</span><span class="p">(</span><span class="n">original_func</span><span class="o">.</span><span class="n">cr_frame</span><span class="p">),</span> <span class="nb">tuple</span><span class="p">(),</span> <span class="nb">dict</span><span class="p">())</span>
</span><span id="TestCaseState.ro-585"><a href="#TestCaseState.ro-585"><span class="linenos">585</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.ro-586"><a href="#TestCaseState.ro-586"><span class="linenos">586</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.ro-587"><a href="#TestCaseState.ro-587"><span class="linenos">587</span></a>                        <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">CodeParamsWithValues</span><span class="p">()</span>
</span><span id="TestCaseState.ro-588"><a href="#TestCaseState.ro-588"><span class="linenos">588</span></a>                        <span class="n">result_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="TestCaseState.ro-589"><a href="#TestCaseState.ro-589"><span class="linenos">589</span></a>                        <span class="n">result_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TestCaseState.ro-590"><a href="#TestCaseState.ro-590"><span class="linenos">590</span></a>                    
</span><span id="TestCaseState.ro-591"><a href="#TestCaseState.ro-591"><span class="linenos">591</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-592"><a href="#TestCaseState.ro-592"><span class="linenos">592</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-593"><a href="#TestCaseState.ro-593"><span class="linenos">593</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.ro-594"><a href="#TestCaseState.ro-594"><span class="linenos">594</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span>
</span><span id="TestCaseState.ro-595"><a href="#TestCaseState.ro-595"><span class="linenos">595</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-596"><a href="#TestCaseState.ro-596"><span class="linenos">596</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-597"><a href="#TestCaseState.ro-597"><span class="linenos">597</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.ro-598"><a href="#TestCaseState.ro-598"><span class="linenos">598</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.ro-599"><a href="#TestCaseState.ro-599"><span class="linenos">599</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.ro-600"><a href="#TestCaseState.ro-600"><span class="linenos">600</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState.ro-601"><a href="#TestCaseState.ro-601"><span class="linenos">601</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.ro-602"><a href="#TestCaseState.ro-602"><span class="linenos">602</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.ro-603"><a href="#TestCaseState.ro-603"><span class="linenos">603</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.ro-604"><a href="#TestCaseState.ro-604"><span class="linenos">604</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.ro-605"><a href="#TestCaseState.ro-605"><span class="linenos">605</span></a>                
</span><span id="TestCaseState.ro-606"><a href="#TestCaseState.ro-606"><span class="linenos">606</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">awaitable_wrapper</span><span class="p">()</span>
</span><span id="TestCaseState.ro-607"><a href="#TestCaseState.ro-607"><span class="linenos">607</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.ro-608"><a href="#TestCaseState.ro-608"><span class="linenos">608</span></a>                <span class="k">async</span> <span class="k">def</span> <span class="nf">async_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.ro-609"><a href="#TestCaseState.ro-609"><span class="linenos">609</span></a>                    <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.ro-610"><a href="#TestCaseState.ro-610"><span class="linenos">610</span></a>                    <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.ro-611"><a href="#TestCaseState.ro-611"><span class="linenos">611</span></a>                    <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.ro-612"><a href="#TestCaseState.ro-612"><span class="linenos">612</span></a>                    <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-613"><a href="#TestCaseState.ro-613"><span class="linenos">613</span></a>                    <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-614"><a href="#TestCaseState.ro-614"><span class="linenos">614</span></a>                    <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.ro-615"><a href="#TestCaseState.ro-615"><span class="linenos">615</span></a>                        <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.ro-616"><a href="#TestCaseState.ro-616"><span class="linenos">616</span></a>                        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-617"><a href="#TestCaseState.ro-617"><span class="linenos">617</span></a>                        <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-618"><a href="#TestCaseState.ro-618"><span class="linenos">618</span></a>                    <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.ro-619"><a href="#TestCaseState.ro-619"><span class="linenos">619</span></a>                        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.ro-620"><a href="#TestCaseState.ro-620"><span class="linenos">620</span></a>                        <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.ro-621"><a href="#TestCaseState.ro-621"><span class="linenos">621</span></a>                            <span class="k">raise</span>
</span><span id="TestCaseState.ro-622"><a href="#TestCaseState.ro-622"><span class="linenos">622</span></a>                    <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.ro-623"><a href="#TestCaseState.ro-623"><span class="linenos">623</span></a>                        <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.ro-624"><a href="#TestCaseState.ro-624"><span class="linenos">624</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.ro-625"><a href="#TestCaseState.ro-625"><span class="linenos">625</span></a>                        <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.ro-626"><a href="#TestCaseState.ro-626"><span class="linenos">626</span></a>                
</span><span id="TestCaseState.ro-627"><a href="#TestCaseState.ro-627"><span class="linenos">627</span></a>                <span class="n">wrapper</span> <span class="o">=</span> <span class="n">async_wrapper</span>
</span><span id="TestCaseState.ro-628"><a href="#TestCaseState.ro-628"><span class="linenos">628</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TestCaseState.ro-629"><a href="#TestCaseState.ro-629"><span class="linenos">629</span></a>            <span class="k">def</span> <span class="nf">sync_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TestCaseState.ro-630"><a href="#TestCaseState.ro-630"><span class="linenos">630</span></a>                <span class="n">current_entity</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="n">func</span>
</span><span id="TestCaseState.ro-631"><a href="#TestCaseState.ro-631"><span class="linenos">631</span></a>                <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span> <span class="o">=</span> <span class="n">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.ro-632"><a href="#TestCaseState.ro-632"><span class="linenos">632</span></a>                <span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">)</span>
</span><span id="TestCaseState.ro-633"><a href="#TestCaseState.ro-633"><span class="linenos">633</span></a>                <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-634"><a href="#TestCaseState.ro-634"><span class="linenos">634</span></a>                <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">()</span>
</span><span id="TestCaseState.ro-635"><a href="#TestCaseState.ro-635"><span class="linenos">635</span></a>                <span class="k">try</span><span class="p">:</span>
</span><span id="TestCaseState.ro-636"><a href="#TestCaseState.ro-636"><span class="linenos">636</span></a>                    <span class="n">result</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TestCaseState.ro-637"><a href="#TestCaseState.ro-637"><span class="linenos">637</span></a>                    <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-638"><a href="#TestCaseState.ro-638"><span class="linenos">638</span></a>                    <span class="k">return</span> <span class="n">result</span>
</span><span id="TestCaseState.ro-639"><a href="#TestCaseState.ro-639"><span class="linenos">639</span></a>                <span class="k">except</span><span class="p">:</span>
</span><span id="TestCaseState.ro-640"><a href="#TestCaseState.ro-640"><span class="linenos">640</span></a>                    <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="TestCaseState.ro-641"><a href="#TestCaseState.ro-641"><span class="linenos">641</span></a>                    <span class="k">if</span> <span class="n">raise_exceptions</span> <span class="ow">or</span> <span class="p">((</span><span class="n">raise_exceptions</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">raise_exceptions</span><span class="p">):</span>
</span><span id="TestCaseState.ro-642"><a href="#TestCaseState.ro-642"><span class="linenos">642</span></a>                        <span class="k">raise</span>
</span><span id="TestCaseState.ro-643"><a href="#TestCaseState.ro-643"><span class="linenos">643</span></a>                <span class="k">finally</span><span class="p">:</span>
</span><span id="TestCaseState.ro-644"><a href="#TestCaseState.ro-644"><span class="linenos">644</span></a>                    <span class="n">current_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="n">CallState</span><span class="p">(</span><span class="n">current_entity</span><span class="p">,</span> <span class="n">code_params_with_values</span><span class="p">,</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span><span class="p">,</span> <span class="n">result_holder</span><span class="p">,</span> <span class="n">exception_holder</span><span class="p">)</span>
</span><span id="TestCaseState.ro-645"><a href="#TestCaseState.ro-645"><span class="linenos">645</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_call_state</span><span class="p">)</span>
</span><span id="TestCaseState.ro-646"><a href="#TestCaseState.ro-646"><span class="linenos">646</span></a>                    <span class="bp">self</span><span class="o">.</span><span class="n">check_current_state_item</span><span class="p">()</span>
</span><span id="TestCaseState.ro-647"><a href="#TestCaseState.ro-647"><span class="linenos">647</span></a>            
</span><span id="TestCaseState.ro-648"><a href="#TestCaseState.ro-648"><span class="linenos">648</span></a>            <span class="n">wrapper</span> <span class="o">=</span> <span class="n">sync_wrapper</span>
</span><span id="TestCaseState.ro-649"><a href="#TestCaseState.ro-649"><span class="linenos">649</span></a>        
</span><span id="TestCaseState.ro-650"><a href="#TestCaseState.ro-650"><span class="linenos">650</span></a>        <span class="n">original_func_sign</span><span class="p">:</span> <span class="n">inspect</span><span class="o">.</span><span class="n">Signature</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">signature</span><span class="p">(</span><span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState.ro-651"><a href="#TestCaseState.ro-651"><span class="linenos">651</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">wrapper</span><span class="p">,</span> <span class="n">original_func</span><span class="p">)</span>
</span><span id="TestCaseState.ro-652"><a href="#TestCaseState.ro-652"><span class="linenos">652</span></a>        <span class="n">wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">original_func_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">original_func_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="TestCaseState.ro-653"><a href="#TestCaseState.ro-653"><span class="linenos">653</span></a>        <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.register_last_result" class="classattr">
                                        <input id="TestCaseState.register_last_result-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_last_result</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result</span><span class="p">:</span> <span class="n">Any</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.register_last_result-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.register_last_result"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.register_last_result-657"><a href="#TestCaseState.register_last_result-657"><span class="linenos">657</span></a>    <span class="k">def</span> <span class="nf">register_last_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.register_last_result-658"><a href="#TestCaseState.register_last_result-658"><span class="linenos">658</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.register_last_result-659"><a href="#TestCaseState.register_last_result-659"><span class="linenos">659</span></a>        <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.register_last_result-660"><a href="#TestCaseState.register_last_result-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="TestCaseState.register_last_result-661"><a href="#TestCaseState.register_last_result-661"><span class="linenos">661</span></a>            <span class="k">raise</span> <span class="n">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState.register_last_result-662"><a href="#TestCaseState.register_last_result-662"><span class="linenos">662</span></a>        
</span><span id="TestCaseState.register_last_result-663"><a href="#TestCaseState.register_last_result-663"><span class="linenos">663</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.rls" class="classattr">
                                        <input id="TestCaseState.rls-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">rls</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result</span><span class="p">:</span> <span class="n">Any</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.rls-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.rls"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.rls-657"><a href="#TestCaseState.rls-657"><span class="linenos">657</span></a>    <span class="k">def</span> <span class="nf">register_last_result</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.rls-658"><a href="#TestCaseState.rls-658"><span class="linenos">658</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.rls-659"><a href="#TestCaseState.rls-659"><span class="linenos">659</span></a>        <span class="n">result_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.rls-660"><a href="#TestCaseState.rls-660"><span class="linenos">660</span></a>        <span class="k">if</span> <span class="n">result_holder</span><span class="p">:</span>
</span><span id="TestCaseState.rls-661"><a href="#TestCaseState.rls-661"><span class="linenos">661</span></a>            <span class="k">raise</span> <span class="n">ResultAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState.rls-662"><a href="#TestCaseState.rls-662"><span class="linenos">662</span></a>        
</span><span id="TestCaseState.rls-663"><a href="#TestCaseState.rls-663"><span class="linenos">663</span></a>        <span class="n">result_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.register_last_exception" class="classattr">
                                        <input id="TestCaseState.register_last_exception-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_last_exception</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result</span><span class="p">:</span> <span class="n">Any</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.register_last_exception-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.register_last_exception"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.register_last_exception-667"><a href="#TestCaseState.register_last_exception-667"><span class="linenos">667</span></a>    <span class="k">def</span> <span class="nf">register_last_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.register_last_exception-668"><a href="#TestCaseState.register_last_exception-668"><span class="linenos">668</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.register_last_exception-669"><a href="#TestCaseState.register_last_exception-669"><span class="linenos">669</span></a>        <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.register_last_exception-670"><a href="#TestCaseState.register_last_exception-670"><span class="linenos">670</span></a>        <span class="k">if</span> <span class="n">exception_holder</span><span class="p">:</span>
</span><span id="TestCaseState.register_last_exception-671"><a href="#TestCaseState.register_last_exception-671"><span class="linenos">671</span></a>            <span class="k">raise</span> <span class="n">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState.register_last_exception-672"><a href="#TestCaseState.register_last_exception-672"><span class="linenos">672</span></a>        
</span><span id="TestCaseState.register_last_exception-673"><a href="#TestCaseState.register_last_exception-673"><span class="linenos">673</span></a>        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.rle" class="classattr">
                                        <input id="TestCaseState.rle-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">rle</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">result</span><span class="p">:</span> <span class="n">Any</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.rle-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.rle"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.rle-667"><a href="#TestCaseState.rle-667"><span class="linenos">667</span></a>    <span class="k">def</span> <span class="nf">register_last_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.rle-668"><a href="#TestCaseState.rle-668"><span class="linenos">668</span></a>        <span class="n">last_call_state</span><span class="p">:</span> <span class="n">CallState</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="TestCaseState.rle-669"><a href="#TestCaseState.rle-669"><span class="linenos">669</span></a>        <span class="n">exception_holder</span><span class="p">:</span> <span class="n">ValueHolder</span> <span class="o">=</span> <span class="n">last_call_state</span><span class="o">.</span><span class="n">result_holder</span>
</span><span id="TestCaseState.rle-670"><a href="#TestCaseState.rle-670"><span class="linenos">670</span></a>        <span class="k">if</span> <span class="n">exception_holder</span><span class="p">:</span>
</span><span id="TestCaseState.rle-671"><a href="#TestCaseState.rle-671"><span class="linenos">671</span></a>            <span class="k">raise</span> <span class="n">ExceptionAlreadyRegisteredError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;For last call state: </span><span class="si">{</span><span class="n">last_call_state</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TestCaseState.rle-672"><a href="#TestCaseState.rle-672"><span class="linenos">672</span></a>        
</span><span id="TestCaseState.rle-673"><a href="#TestCaseState.rle-673"><span class="linenos">673</span></a>        <span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">result</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.try_to_load_expected_call_stack" class="classattr">
                                        <input id="TestCaseState.try_to_load_expected_call_stack-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_to_load_expected_call_stack</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.try_to_load_expected_call_stack-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.try_to_load_expected_call_stack"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.try_to_load_expected_call_stack-677"><a href="#TestCaseState.try_to_load_expected_call_stack-677"><span class="linenos">677</span></a>    <span class="k">def</span> <span class="nf">try_to_load_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-678"><a href="#TestCaseState.try_to_load_expected_call_stack-678"><span class="linenos">678</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-679"><a href="#TestCaseState.try_to_load_expected_call_stack-679"><span class="linenos">679</span></a><span class="sd">        Will try to load a pickle file with a refference results (an expected_results)</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-680"><a href="#TestCaseState.try_to_load_expected_call_stack-680"><span class="linenos">680</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-681"><a href="#TestCaseState.try_to_load_expected_call_stack-681"><span class="linenos">681</span></a>        <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">):</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-682"><a href="#TestCaseState.try_to_load_expected_call_stack-682"><span class="linenos">682</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;rb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-683"><a href="#TestCaseState.try_to_load_expected_call_stack-683"><span class="linenos">683</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">expected_call_stack_per_test</span> <span class="o">=</span> <span class="n">pickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</span><span id="TestCaseState.try_to_load_expected_call_stack-684"><a href="#TestCaseState.try_to_load_expected_call_stack-684"><span class="linenos">684</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


            <div class="docstring"><p>Will try to load a pickle file with a refference results (an expected_results)</p>
</div>


                            </div>
                            <div id="TestCaseState.try_to_save_expected_call_stack" class="classattr">
                                        <input id="TestCaseState.try_to_save_expected_call_stack-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">try_to_save_expected_call_stack</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="kc">None</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.try_to_save_expected_call_stack-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.try_to_save_expected_call_stack"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.try_to_save_expected_call_stack-686"><a href="#TestCaseState.try_to_save_expected_call_stack-686"><span class="linenos">686</span></a>    <span class="k">def</span> <span class="nf">try_to_save_expected_call_stack</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-687"><a href="#TestCaseState.try_to_save_expected_call_stack-687"><span class="linenos">687</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-688"><a href="#TestCaseState.try_to_save_expected_call_stack-688"><span class="linenos">688</span></a><span class="sd">        Will try to save a refference results (an expected_results) to a pickle file. Will not save them if </span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-689"><a href="#TestCaseState.try_to_save_expected_call_stack-689"><span class="linenos">689</span></a><span class="sd">        pickle file was already successfully loaded with a &#39;FakeResults.try_to_load_expected_call_stack()&#39; call.</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-690"><a href="#TestCaseState.try_to_save_expected_call_stack-690"><span class="linenos">690</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-691"><a href="#TestCaseState.try_to_save_expected_call_stack-691"><span class="linenos">691</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">loaded</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-692"><a href="#TestCaseState.try_to_save_expected_call_stack-692"><span class="linenos">692</span></a>            <span class="k">return</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-693"><a href="#TestCaseState.try_to_save_expected_call_stack-693"><span class="linenos">693</span></a>        
</span><span id="TestCaseState.try_to_save_expected_call_stack-694"><a href="#TestCaseState.try_to_save_expected_call_stack-694"><span class="linenos">694</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">)):</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-695"><a href="#TestCaseState.try_to_save_expected_call_stack-695"><span class="linenos">695</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-696"><a href="#TestCaseState.try_to_save_expected_call_stack-696"><span class="linenos">696</span></a>                <span class="n">pickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-697"><a href="#TestCaseState.try_to_save_expected_call_stack-697"><span class="linenos">697</span></a>        
</span><span id="TestCaseState.try_to_save_expected_call_stack-698"><a href="#TestCaseState.try_to_save_expected_call_stack-698"><span class="linenos">698</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)</span> <span class="ow">and</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">)):</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-699"><a href="#TestCaseState.try_to_save_expected_call_stack-699"><span class="linenos">699</span></a>            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">readable_content_full_file_name</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
</span><span id="TestCaseState.try_to_save_expected_call_stack-700"><a href="#TestCaseState.try_to_save_expected_call_stack-700"><span class="linenos">700</span></a>                <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">prepare_readable_content</span><span class="p">()</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s1">&#39;utf-8&#39;</span><span class="p">))</span>
</span></pre></div>


            <div class="docstring"><p>Will try to save a refference results (an expected_results) to a pickle file. Will not save them if 
pickle file was already successfully loaded with a 'FakeResults.try_to_load_expected_call_stack()' call.</p>
</div>


                            </div>
                            <div id="TestCaseState.prepare_readable_content" class="classattr">
                                        <input id="TestCaseState.prepare_readable_content-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">prepare_readable_content</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="TestCaseState.prepare_readable_content-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.prepare_readable_content"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.prepare_readable_content-702"><a href="#TestCaseState.prepare_readable_content-702"><span class="linenos">702</span></a>    <span class="k">def</span> <span class="nf">prepare_readable_content</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TestCaseState.prepare_readable_content-703"><a href="#TestCaseState.prepare_readable_content-703"><span class="linenos">703</span></a>        <span class="n">content</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="TestCaseState.prepare_readable_content-704"><a href="#TestCaseState.prepare_readable_content-704"><span class="linenos">704</span></a>        <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;# Test Case: </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-705"><a href="#TestCaseState.prepare_readable_content-705"><span class="linenos">705</span></a>        <span class="k">for</span> <span class="n">test_id</span><span class="p">,</span> <span class="n">call_stack</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">call_stack_per_test</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TestCaseState.prepare_readable_content-706"><a href="#TestCaseState.prepare_readable_content-706"><span class="linenos">706</span></a>            <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\n</span><span class="s1">## Test ID: </span><span class="si">{</span><span class="n">test_id</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-707"><a href="#TestCaseState.prepare_readable_content-707"><span class="linenos">707</span></a>            <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">call_state</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">call_stack</span><span class="p">):</span>
</span><span id="TestCaseState.prepare_readable_content-708"><a href="#TestCaseState.prepare_readable_content-708"><span class="linenos">708</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\n\t</span><span class="si">{</span><span class="n">index</span><span class="si">}</span><span class="s1">: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">entity</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-709"><a href="#TestCaseState.prepare_readable_content-709"><span class="linenos">709</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">params_with_values</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-710"><a href="#TestCaseState.prepare_readable_content-710"><span class="linenos">710</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">args: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">args</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-711"><a href="#TestCaseState.prepare_readable_content-711"><span class="linenos">711</span></a>                <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">kwargs: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">kwargs</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-712"><a href="#TestCaseState.prepare_readable_content-712"><span class="linenos">712</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="p">:</span>
</span><span id="TestCaseState.prepare_readable_content-713"><a href="#TestCaseState.prepare_readable_content-713"><span class="linenos">713</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">result: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">result_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-714"><a href="#TestCaseState.prepare_readable_content-714"><span class="linenos">714</span></a>                <span class="k">if</span> <span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="p">:</span>
</span><span id="TestCaseState.prepare_readable_content-715"><a href="#TestCaseState.prepare_readable_content-715"><span class="linenos">715</span></a>                    <span class="n">content</span> <span class="o">+=</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="se">\t\t</span><span class="s1">exception: </span><span class="si">{</span><span class="n">call_state</span><span class="o">.</span><span class="n">exception_holder</span><span class="o">.</span><span class="n">value</span><span class="si">}</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TestCaseState.prepare_readable_content-716"><a href="#TestCaseState.prepare_readable_content-716"><span class="linenos">716</span></a>        
</span><span id="TestCaseState.prepare_readable_content-717"><a href="#TestCaseState.prepare_readable_content-717"><span class="linenos">717</span></a>        <span class="k">return</span> <span class="n">content</span>
</span></pre></div>


    

                            </div>
                            <div id="TestCaseState.register" class="classattr">
                                        <input id="TestCaseState.register-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.register-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.register"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.register-719"><a href="#TestCaseState.register-719"><span class="linenos">719</span></a>    <span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TestCaseState.register-720"><a href="#TestCaseState.register-720"><span class="linenos">720</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState.register-721"><a href="#TestCaseState.register-721"><span class="linenos">721</span></a><span class="sd">        Will register current instance to a global &#39;TEST_CASE_STATE&#39; variable. Will save a previous value</span>
</span><span id="TestCaseState.register-722"><a href="#TestCaseState.register-722"><span class="linenos">722</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState.register-723"><a href="#TestCaseState.register-723"><span class="linenos">723</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">try_to_load_expected_call_stack</span><span class="p">()</span>
</span><span id="TestCaseState.register-724"><a href="#TestCaseState.register-724"><span class="linenos">724</span></a>
</span><span id="TestCaseState.register-725"><a href="#TestCaseState.register-725"><span class="linenos">725</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState.register-726"><a href="#TestCaseState.register-726"><span class="linenos">726</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span> <span class="o">=</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState.register-727"><a href="#TestCaseState.register-727"><span class="linenos">727</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span>
</span></pre></div>


            <div class="docstring"><p>Will register current instance to a global 'TEST_CASE_STATE' variable. Will save a previous value</p>
</div>


                            </div>
                            <div id="TestCaseState.unregister" class="classattr">
                                        <input id="TestCaseState.unregister-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">unregister</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">should_be_saved</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TestCaseState.unregister-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TestCaseState.unregister"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TestCaseState.unregister-733"><a href="#TestCaseState.unregister-733"><span class="linenos">733</span></a>    <span class="k">def</span> <span class="nf">unregister</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">should_be_saved</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="TestCaseState.unregister-734"><a href="#TestCaseState.unregister-734"><span class="linenos">734</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="TestCaseState.unregister-735"><a href="#TestCaseState.unregister-735"><span class="linenos">735</span></a><span class="sd">        Will restore a previous value of the global &#39;TEST_CASE_STATE&#39; variable</span>
</span><span id="TestCaseState.unregister-736"><a href="#TestCaseState.unregister-736"><span class="linenos">736</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TestCaseState.unregister-737"><a href="#TestCaseState.unregister-737"><span class="linenos">737</span></a>        <span class="k">global</span> <span class="n">TEST_CASE_STATE</span>
</span><span id="TestCaseState.unregister-738"><a href="#TestCaseState.unregister-738"><span class="linenos">738</span></a>        <span class="n">TEST_CASE_STATE</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">old_global_fake_result</span>
</span><span id="TestCaseState.unregister-739"><a href="#TestCaseState.unregister-739"><span class="linenos">739</span></a>
</span><span id="TestCaseState.unregister-740"><a href="#TestCaseState.unregister-740"><span class="linenos">740</span></a>        <span class="k">if</span> <span class="n">should_be_saved</span><span class="p">:</span>
</span><span id="TestCaseState.unregister-741"><a href="#TestCaseState.unregister-741"><span class="linenos">741</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">try_to_save_expected_call_stack</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Will restore a previous value of the global 'TEST_CASE_STATE' variable</p>
</div>


                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>