---
title: inspect
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.introspection<wbr>.inspect<wbr>.versions<wbr>.v_0<wbr>.inspect    </h1>

                
                        <input id="mod-inspect-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-inspect-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos">  18</span></a><span class="c1"># __all__ = [&#39;frame&#39;, &#39;get_exception&#39;, &#39;get_exception_tripple&#39;, &#39;exception_to_printable_text&#39;, &#39;is_async&#39;, &#39;is_callable&#39;, &#39;func_param_names&#39;, &#39;frame_param_names&#39;, &#39;intro_func_param_names&#39;, &#39;CodeParamsWithValues&#39;, &#39;intro_func_params_with_values&#39;, &#39;intro_func_all_params_with_values&#39;, &#39;intro_func_all_params_with_values_as_ordered_dict&#39;, &#39;code_params_with_values_to_signature_items_gen&#39;, &#39;code_params_with_values_to_signature&#39;]</span>
</span><span id="L-19"><a href="#L-19"><span class="linenos">  19</span></a>
</span><span id="L-20"><a href="#L-20"><span class="linenos">  20</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Generator</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">NamedTuple</span><span class="p">,</span> <span class="n">OrderedDict</span> <span class="k">as</span> <span class="n">OrderedDictType</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">cast</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos">  21</span></a><span class="kn">from</span> <span class="nn">types</span> <span class="kn">import</span> <span class="n">ModuleType</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">,</span> <span class="n">FrameType</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos">  22</span></a><span class="kn">import</span> <span class="nn">traceback</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos">  23</span></a><span class="kn">import</span> <span class="nn">inspect</span>
</span><span id="L-24"><a href="#L-24"><span class="linenos">  24</span></a><span class="kn">from</span> <span class="nn">inspect</span> <span class="kn">import</span> <span class="n">getattr_static</span> <span class="k">as</span> <span class="n">inspect__getattr_static</span>
</span><span id="L-25"><a href="#L-25"><span class="linenos">  25</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos">  26</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.python_bytecode_manipulator</span> <span class="kn">import</span> <span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">code_param_names</span><span class="p">,</span> <span class="n">has_code</span><span class="p">,</span> <span class="n">get_code</span><span class="p">,</span> <span class="n">code_name</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos">  27</span></a><span class="kn">from</span> <span class="nn">cengal.text_processing.brackets_processing</span> <span class="kn">import</span> <span class="n">Bracket</span><span class="p">,</span> <span class="n">BracketPair</span><span class="p">,</span> <span class="n">replace_text_with_brackets</span><span class="p">,</span> <span class="n">find_text_in_brackets</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos">  28</span></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">OrderedDict</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos">  29</span></a><span class="kn">from</span> <span class="nn">importlib</span> <span class="kn">import</span> <span class="n">import_module</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos">  30</span></a>
</span><span id="L-31"><a href="#L-31"><span class="linenos">  31</span></a>
</span><span id="L-32"><a href="#L-32"><span class="linenos">  32</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos">  33</span></a><span class="sd">Module Docstring</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos">  34</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos">  35</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos">  36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos">  37</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos">  38</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos">  39</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos">  40</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos">  41</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos">  42</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos">  43</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos">  44</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos">  45</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos">  46</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos">  47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos">  48</span></a>
</span><span id="L-49"><a href="#L-49"><span class="linenos">  49</span></a><span class="k">class</span> <span class="nc">WrongDepth</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos">  50</span></a>    <span class="k">pass</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos">  51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos">  52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos">  53</span></a><span class="k">class</span> <span class="nc">CanNotRetrieveFrame</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos">  54</span></a>    <span class="k">pass</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos">  55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos">  56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos">  57</span></a><span class="k">def</span> <span class="nf">frame</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">FrameType</span><span class="p">:</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos">  58</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos">  59</span></a><span class="sd">    :param depth: 0 - frame of this function, 1 - frame of the caller function, etc.</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos">  60</span></a><span class="sd">    :return:</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos">  61</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos">  62</span></a>    <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos">  63</span></a>    <span class="k">if</span> <span class="n">depth</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos">  64</span></a>        <span class="k">raise</span> <span class="n">WrongDepth</span><span class="p">(</span><span class="n">depth</span><span class="p">)</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos">  65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos">  66</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">()</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos">  67</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos">  68</span></a>        <span class="k">raise</span> <span class="n">CanNotRetrieveFrame</span><span class="p">()</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos">  69</span></a>
</span><span id="L-70"><a href="#L-70"><span class="linenos">  70</span></a>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">depth</span><span class="p">):</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos">  71</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">f_back</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos">  72</span></a>
</span><span id="L-73"><a href="#L-73"><span class="linenos">  73</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos">  74</span></a>
</span><span id="L-75"><a href="#L-75"><span class="linenos">  75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos">  76</span></a><span class="k">def</span> <span class="nf">get_exception</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="ne">Exception</span><span class="p">:</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos">  77</span></a>    <span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos">  78</span></a>    <span class="k">return</span> <span class="n">ex_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">ex_traceback</span><span class="p">)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos">  79</span></a>
</span><span id="L-80"><a href="#L-80"><span class="linenos">  80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos">  81</span></a><span class="k">def</span> <span class="nf">get_exception_tripple</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos">  82</span></a>    <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos">  83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos">  84</span></a>
</span><span id="L-85"><a href="#L-85"><span class="linenos">  85</span></a><span class="k">def</span> <span class="nf">exception_to_printable_text</span><span class="p">(</span><span class="n">exception</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos">  86</span></a>    <span class="c1"># return &#39;&#39;.join(traceback.format_exception(type(exception), exception, exception.__traceback__))</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos">  87</span></a>    <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">traceback</span><span class="o">.</span><span class="n">TracebackException</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">exception</span><span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">())</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos">  88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos">  89</span></a>
</span><span id="L-90"><a href="#L-90"><span class="linenos">  90</span></a><span class="k">def</span> <span class="nf">is_async</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos">  91</span></a>    <span class="k">return</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isgenerator</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutinefunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isgeneratorfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isasyncgen</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isasyncgenfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos">  92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos">  93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos">  94</span></a><span class="k">def</span> <span class="nf">is_callable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos">  95</span></a>    <span class="k">return</span> <span class="nb">callable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos">  96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos">  97</span></a>
</span><span id="L-98"><a href="#L-98"><span class="linenos">  98</span></a><span class="k">def</span> <span class="nf">func_param_names</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos">  99</span></a>    <span class="k">return</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">get_code</span><span class="p">(</span><span class="n">func</span><span class="p">))</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos"> 100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos"> 101</span></a>
</span><span id="L-102"><a href="#L-102"><span class="linenos"> 102</span></a><span class="k">def</span> <span class="nf">entity_arguments_description</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos"> 103</span></a>    <span class="n">init_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos"> 104</span></a>    <span class="n">cpn</span><span class="p">:</span> <span class="n">CodeParamNames</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">init_code</span><span class="p">)</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos"> 105</span></a>    <span class="n">positional</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">positional</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos"> 106</span></a>    <span class="n">positional_only</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos"> 107</span></a>    <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">keyword_only</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos"> 108</span></a>    <span class="nb">all</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos"> 109</span></a>    <span class="k">return</span> <span class="nb">all</span><span class="p">,</span> <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos"> 110</span></a>
</span><span id="L-111"><a href="#L-111"><span class="linenos"> 111</span></a>
</span><span id="L-112"><a href="#L-112"><span class="linenos"> 112</span></a><span class="k">def</span> <span class="nf">func_code_name</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos"> 113</span></a>    <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos"> 114</span></a>    <span class="k">return</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos"> 115</span></a>
</span><span id="L-116"><a href="#L-116"><span class="linenos"> 116</span></a>
</span><span id="L-117"><a href="#L-117"><span class="linenos"> 117</span></a><span class="k">def</span> <span class="nf">func_name</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos"> 118</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos"> 119</span></a>        <span class="k">return</span> <span class="n">func</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos"> 120</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos"> 121</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos"> 122</span></a>
</span><span id="L-123"><a href="#L-123"><span class="linenos"> 123</span></a>
</span><span id="L-124"><a href="#L-124"><span class="linenos"> 124</span></a><span class="k">def</span> <span class="nf">func_qualname</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos"> 125</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos"> 126</span></a>        <span class="k">return</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos"> 127</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos"> 128</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos"> 129</span></a>
</span><span id="L-130"><a href="#L-130"><span class="linenos"> 130</span></a>
</span><span id="L-131"><a href="#L-131"><span class="linenos"> 131</span></a><span class="k">def</span> <span class="nf">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos"> 132</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos"> 133</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos"> 134</span></a>    
</span><span id="L-135"><a href="#L-135"><span class="linenos"> 135</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos"> 136</span></a>        <span class="k">return</span> <span class="n">code_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos"> 137</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos"> 138</span></a>        <span class="k">return</span> <span class="n">func_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos"> 139</span></a>
</span><span id="L-140"><a href="#L-140"><span class="linenos"> 140</span></a>
</span><span id="L-141"><a href="#L-141"><span class="linenos"> 141</span></a><span class="k">def</span> <span class="nf">entity_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos"> 142</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos"> 143</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos"> 144</span></a>    
</span><span id="L-145"><a href="#L-145"><span class="linenos"> 145</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos"> 146</span></a>        <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&gt;=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos"> 147</span></a>            <span class="k">return</span> <span class="n">code_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos"> 148</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos"> 149</span></a>            <span class="c1"># raise RuntimeError(&#39;CodeType.__qualname__ is available only since Python 3.11&#39;)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos"> 150</span></a>            <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos"> 151</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity_owner_name</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">entity_name</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos"> 152</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos"> 153</span></a>        <span class="k">return</span> <span class="n">func_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos"> 154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos"> 155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos"> 156</span></a><span class="k">def</span> <span class="nf">entity_class</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos"> 157</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos"> 158</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos"> 159</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func</span><span class="p">:</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos"> 160</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos"> 161</span></a>        
</span><span id="L-162"><a href="#L-162"><span class="linenos"> 162</span></a>        <span class="n">func_of_the_bound_method</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos"> 163</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos"> 164</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func_of_the_bound_method</span><span class="p">:</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos"> 165</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos"> 166</span></a>        
</span><span id="L-167"><a href="#L-167"><span class="linenos"> 167</span></a>        <span class="n">func</span> <span class="o">=</span> <span class="n">func_of_the_bound_method</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos"> 168</span></a>    
</span><span id="L-169"><a href="#L-169"><span class="linenos"> 169</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos"> 170</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos"> 171</span></a>            <span class="n">func_class</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">),</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&lt;locals&gt;&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos"> 172</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos"> 173</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos"> 174</span></a>        
</span><span id="L-175"><a href="#L-175"><span class="linenos"> 175</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">func_class</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos"> 176</span></a>            <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos"> 177</span></a>    
</span><span id="L-178"><a href="#L-178"><span class="linenos"> 178</span></a>    <span class="k">return</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="s1">&#39;__objclass__&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos"> 179</span></a>
</span><span id="L-180"><a href="#L-180"><span class="linenos"> 180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos"> 181</span></a><span class="k">def</span> <span class="nf">entity_owner</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos"> 182</span></a>    <span class="n">func_module</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos"> 183</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos"> 184</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos"> 185</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func</span><span class="p">:</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos"> 186</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos"> 187</span></a>        
</span><span id="L-188"><a href="#L-188"><span class="linenos"> 188</span></a>        <span class="n">func_of_the_bound_method</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos"> 189</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos"> 190</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func_of_the_bound_method</span><span class="p">:</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos"> 191</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos"> 192</span></a>        
</span><span id="L-193"><a href="#L-193"><span class="linenos"> 193</span></a>        <span class="n">func</span> <span class="o">=</span> <span class="n">func_of_the_bound_method</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos"> 194</span></a>        
</span><span id="L-195"><a href="#L-195"><span class="linenos"> 195</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos"> 196</span></a>        <span class="n">func_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos"> 197</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos"> 198</span></a>            <span class="n">func_class</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func_module</span><span class="p">,</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&lt;locals&gt;&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos"> 199</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos"> 200</span></a>            <span class="k">return</span> <span class="n">func_module</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos"> 201</span></a>        
</span><span id="L-202"><a href="#L-202"><span class="linenos"> 202</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">func_class</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos"> 203</span></a>            <span class="k">return</span> <span class="n">func_class</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos"> 204</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos"> 205</span></a>            <span class="k">return</span> <span class="n">func_module</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos"> 206</span></a>    
</span><span id="L-207"><a href="#L-207"><span class="linenos"> 207</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos"> 208</span></a>        <span class="k">return</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="s1">&#39;__objclass__&#39;</span><span class="p">)</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos"> 209</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos"> 210</span></a>        <span class="k">if</span> <span class="n">func_module</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos"> 211</span></a>            <span class="n">func_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos"> 212</span></a>        
</span><span id="L-213"><a href="#L-213"><span class="linenos"> 213</span></a>        <span class="k">return</span> <span class="n">func_module</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos"> 214</span></a>
</span><span id="L-215"><a href="#L-215"><span class="linenos"> 215</span></a>
</span><span id="L-216"><a href="#L-216"><span class="linenos"> 216</span></a><span class="n">module_repr_importable_str_bracket_pair</span><span class="p">:</span> <span class="n">BracketPair</span> <span class="o">=</span> <span class="n">BracketPair</span><span class="p">([</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot;&lt;module &#39;&quot;</span><span class="p">)],</span> <span class="p">[</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot;&#39; from &#39;&quot;</span><span class="p">)])</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos"> 217</span></a><span class="n">module_repr_full_file_path_bracket_pair</span><span class="p">:</span> <span class="n">BracketPair</span> <span class="o">=</span> <span class="n">BracketPair</span><span class="p">([</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot;&#39; from &#39;&quot;</span><span class="p">)],</span> <span class="p">[</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot;&#39;&gt;&quot;</span><span class="p">)])</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos"> 218</span></a>
</span><span id="L-219"><a href="#L-219"><span class="linenos"> 219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos"> 220</span></a><span class="k">def</span> <span class="nf">get_module_importable_str_and_path</span><span class="p">(</span><span class="n">module</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos"> 221</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">):</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos"> 222</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Only modules are supported. </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">module</span><span class="p">)</span><span class="si">}</span><span class="s1"> was provided instead&#39;</span><span class="p">)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos"> 223</span></a>    
</span><span id="L-224"><a href="#L-224"><span class="linenos"> 224</span></a>    <span class="n">module_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos"> 225</span></a>    <span class="n">importable_str</span> <span class="o">=</span> <span class="n">module_repr</span><span class="p">[</span><span class="n">find_text_in_brackets</span><span class="p">(</span><span class="n">module_repr</span><span class="p">,</span> <span class="n">module_repr_importable_str_bracket_pair</span><span class="p">)]</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos"> 226</span></a>    <span class="n">full_file_path</span> <span class="o">=</span> <span class="n">module_repr</span><span class="p">[</span><span class="n">find_text_in_brackets</span><span class="p">(</span><span class="n">module_repr</span><span class="p">,</span> <span class="n">module_repr_full_file_path_bracket_pair</span><span class="p">)]</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos"> 227</span></a>    <span class="k">return</span> <span class="n">importable_str</span><span class="p">,</span> <span class="n">full_file_path</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos"> 228</span></a>
</span><span id="L-229"><a href="#L-229"><span class="linenos"> 229</span></a>
</span><span id="L-230"><a href="#L-230"><span class="linenos"> 230</span></a><span class="k">def</span> <span class="nf">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ModuleType</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]]:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos"> 231</span></a>    <span class="n">owning_path</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos"> 232</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos"> 233</span></a>    <span class="n">owner_is_module</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos"> 234</span></a>    <span class="k">while</span> <span class="ow">not</span> <span class="n">owner_is_module</span><span class="p">:</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos"> 235</span></a>        <span class="n">module</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos"> 236</span></a>        <span class="n">owning_path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos"> 237</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">module</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos"> 238</span></a>        <span class="n">owner_is_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos"> 239</span></a>    
</span><span id="L-240"><a href="#L-240"><span class="linenos"> 240</span></a>    <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">module_file_full_path</span> <span class="o">=</span> <span class="n">get_module_importable_str_and_path</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos"> 241</span></a>    <span class="k">return</span> <span class="n">module</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">module_file_full_path</span><span class="p">,</span> <span class="n">owning_path</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos"> 242</span></a>
</span><span id="L-243"><a href="#L-243"><span class="linenos"> 243</span></a>
</span><span id="L-244"><a href="#L-244"><span class="linenos"> 244</span></a><span class="k">def</span> <span class="nf">entity_owning_module_importable_str</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos"> 245</span></a>    <span class="n">_</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos"> 246</span></a>    <span class="k">return</span> <span class="n">module_importable_str</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos"> 247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos"> 248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos"> 249</span></a><span class="k">def</span> <span class="nf">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos"> 250</span></a>    <span class="n">_</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">owning_path</span> <span class="o">=</span> <span class="n">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos"> 251</span></a>    <span class="n">owning_path</span> <span class="o">=</span> <span class="n">owning_path</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos"> 252</span></a>    <span class="n">owning_names_path</span> <span class="o">=</span> <span class="p">[</span><span class="n">entity_name</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span> <span class="k">for</span> <span class="n">owner</span> <span class="ow">in</span> <span class="n">owning_path</span><span class="p">]</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos"> 253</span></a>    <span class="k">return</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos"> 254</span></a>
</span><span id="L-255"><a href="#L-255"><span class="linenos"> 255</span></a>
</span><span id="L-256"><a href="#L-256"><span class="linenos"> 256</span></a><span class="k">def</span> <span class="nf">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">owning_names_path</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos"> 257</span></a>    <span class="n">owner</span> <span class="o">=</span> <span class="n">import_module</span><span class="p">(</span><span class="n">module_importable_str</span><span class="p">)</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos"> 258</span></a>    <span class="k">for</span> <span class="n">owner_name</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">owning_names_path</span><span class="p">):</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos"> 259</span></a>        <span class="n">owner</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">owner_name</span><span class="p">)</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos"> 260</span></a>
</span><span id="L-261"><a href="#L-261"><span class="linenos"> 261</span></a>    <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name</span><span class="p">)</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos"> 262</span></a>
</span><span id="L-263"><a href="#L-263"><span class="linenos"> 263</span></a>
</span><span id="L-264"><a href="#L-264"><span class="linenos"> 264</span></a><span class="n">module_repr_limited_bracket_pair</span><span class="p">:</span> <span class="n">BracketPair</span> <span class="o">=</span> <span class="n">BracketPair</span><span class="p">([</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot; from &#39;&quot;</span><span class="p">)],</span> <span class="p">[</span><span class="n">Bracket</span><span class="p">(</span><span class="s2">&quot;&#39;&gt;&quot;</span><span class="p">)])</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos"> 265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos"> 266</span></a>
</span><span id="L-267"><a href="#L-267"><span class="linenos"> 267</span></a><span class="k">def</span> <span class="nf">normalized_owner_repr</span><span class="p">(</span><span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos"> 268</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos"> 269</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos"> 270</span></a>    
</span><span id="L-271"><a href="#L-271"><span class="linenos"> 271</span></a>    <span class="n">owner_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos"> 272</span></a>    <span class="n">result</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">replace_text_with_brackets</span><span class="p">(</span><span class="n">owner_repr</span><span class="p">,</span> <span class="n">module_repr_limited_bracket_pair</span><span class="p">,</span> <span class="s2">&quot;&gt;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos"> 273</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos"> 274</span></a>
</span><span id="L-275"><a href="#L-275"><span class="linenos"> 275</span></a>
</span><span id="L-276"><a href="#L-276"><span class="linenos"> 276</span></a><span class="k">def</span> <span class="nf">normalized_code_owner_repr</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">,</span> <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos"> 277</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos"> 278</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos"> 279</span></a>    
</span><span id="L-280"><a href="#L-280"><span class="linenos"> 280</span></a>    <span class="n">owner_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos"> 281</span></a>    <span class="n">result</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">replace_text_with_brackets</span><span class="p">(</span><span class="n">owner_repr</span><span class="p">,</span> <span class="n">module_repr_limited_bracket_pair</span><span class="p">,</span> <span class="sa">f</span><span class="s2">&quot; line </span><span class="si">{</span><span class="n">code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="si">}</span><span class="s2">&gt;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos"> 282</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos"> 283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos"> 284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos"> 285</span></a><span class="k">def</span> <span class="nf">entity_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos"> 286</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos"> 287</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos"> 288</span></a>    
</span><span id="L-289"><a href="#L-289"><span class="linenos"> 289</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos"> 290</span></a>        <span class="k">return</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos"> 291</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos"> 292</span></a>        <span class="k">return</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos"> 293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos"> 294</span></a>
</span><span id="L-295"><a href="#L-295"><span class="linenos"> 295</span></a><span class="k">def</span> <span class="nf">owner_name</span><span class="p">(</span><span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos"> 296</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos"> 297</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos"> 298</span></a>    
</span><span id="L-299"><a href="#L-299"><span class="linenos"> 299</span></a>    <span class="k">return</span> <span class="n">owner</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos"> 300</span></a>
</span><span id="L-301"><a href="#L-301"><span class="linenos"> 301</span></a>
</span><span id="L-302"><a href="#L-302"><span class="linenos"> 302</span></a><span class="k">def</span> <span class="nf">entity_owner_name</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos"> 303</span></a>    <span class="k">return</span> <span class="n">owner_name</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos"> 304</span></a>
</span><span id="L-305"><a href="#L-305"><span class="linenos"> 305</span></a>
</span><span id="L-306"><a href="#L-306"><span class="linenos"> 306</span></a><span class="k">def</span> <span class="nf">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">:</span> <span class="n">FrameType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos"> 307</span></a>    <span class="k">return</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span><span class="p">)</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos"> 308</span></a>
</span><span id="L-309"><a href="#L-309"><span class="linenos"> 309</span></a>
</span><span id="L-310"><a href="#L-310"><span class="linenos"> 310</span></a><span class="k">def</span> <span class="nf">intro_func_param_names</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos"> 311</span></a>    <span class="k">return</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos"> 312</span></a>
</span><span id="L-313"><a href="#L-313"><span class="linenos"> 313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos"> 314</span></a><span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">CodeParamNames</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos"> 315</span></a><span class="n">ParamWithValue</span> <span class="o">=</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos"> 316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos"> 317</span></a>
</span><span id="L-318"><a href="#L-318"><span class="linenos"> 318</span></a><span class="k">def</span> <span class="nf">fill_code_params_with_values</span><span class="p">(</span><span class="n">code_params</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos"> 319</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos"> 320</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos"> 321</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos"> 322</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos"> 323</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos"> 324</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos"> 325</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos"> 326</span></a>    
</span><span id="L-327"><a href="#L-327"><span class="linenos"> 327</span></a>    <span class="n">positional_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">args</span><span class="p">[</span><span class="n">index</span><span class="p">])</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">)))</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos"> 328</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos"> 329</span></a>        <span class="n">positional_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">args</span><span class="p">[</span><span class="n">index</span><span class="p">])</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)))</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos"> 330</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos"> 331</span></a>        <span class="n">positional_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos"> 332</span></a>    
</span><span id="L-333"><a href="#L-333"><span class="linenos"> 333</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos"> 334</span></a>        <span class="n">keyword_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">))</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos"> 335</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos"> 336</span></a>        <span class="n">keyword_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos"> 337</span></a>
</span><span id="L-338"><a href="#L-338"><span class="linenos"> 338</span></a>    <span class="n">result_args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">positional_len</span><span class="p">:]</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos"> 339</span></a>    <span class="n">result_kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">key</span><span class="p">:</span> <span class="n">value</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">}</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos"> 340</span></a>    
</span><span id="L-341"><a href="#L-341"><span class="linenos"> 341</span></a>    <span class="k">return</span> <span class="n">CodeParamsWithValues</span><span class="p">(</span><span class="n">positional_values</span><span class="p">,</span> <span class="n">positional_only_values</span><span class="p">,</span> <span class="n">keyword_only_values</span><span class="p">),</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos"> 342</span></a>
</span><span id="L-343"><a href="#L-343"><span class="linenos"> 343</span></a>
</span><span id="L-344"><a href="#L-344"><span class="linenos"> 344</span></a><span class="k">def</span> <span class="nf">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">],</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos"> 345</span></a>    <span class="k">return</span> <span class="n">fill_code_params_with_values</span><span class="p">(</span><span class="n">func_param_names</span><span class="p">(</span><span class="n">func</span><span class="p">),</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos"> 346</span></a>
</span><span id="L-347"><a href="#L-347"><span class="linenos"> 347</span></a>
</span><span id="L-348"><a href="#L-348"><span class="linenos"> 348</span></a><span class="k">def</span> <span class="nf">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamsWithValues</span><span class="p">:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos"> 349</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos"> 350</span></a>    <span class="n">fr_locals</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_locals</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos"> 351</span></a>    <span class="k">return</span> <span class="n">CodeParamsWithValues</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">positional</span><span class="p">)),</span> \
</span><span id="L-352"><a href="#L-352"><span class="linenos"> 352</span></a>        <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">positional_only</span><span class="p">)),</span> \
</span><span id="L-353"><a href="#L-353"><span class="linenos"> 353</span></a>        <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">)))</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos"> 354</span></a>
</span><span id="L-355"><a href="#L-355"><span class="linenos"> 355</span></a>
</span><span id="L-356"><a href="#L-356"><span class="linenos"> 356</span></a><span class="k">def</span> <span class="nf">intro_func_params_with_values</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamsWithValues</span><span class="p">:</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos"> 357</span></a>    <span class="k">return</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos"> 358</span></a>
</span><span id="L-359"><a href="#L-359"><span class="linenos"> 359</span></a>
</span><span id="L-360"><a href="#L-360"><span class="linenos"> 360</span></a><span class="k">def</span> <span class="nf">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ParamWithValue</span><span class="p">]:</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos"> 361</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos"> 362</span></a>    <span class="n">all_params</span> <span class="o">=</span> <span class="n">positional</span> <span class="o">+</span> <span class="n">keyword_only</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos"> 363</span></a>    <span class="n">fr_locals</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_locals</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos"> 364</span></a>    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">all_params</span><span class="p">))</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos"> 365</span></a>
</span><span id="L-366"><a href="#L-366"><span class="linenos"> 366</span></a>
</span><span id="L-367"><a href="#L-367"><span class="linenos"> 367</span></a><span class="k">def</span> <span class="nf">intro_func_all_params_with_values</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ParamWithValue</span><span class="p">]:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos"> 368</span></a>    <span class="k">return</span> <span class="n">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos"> 369</span></a>
</span><span id="L-370"><a href="#L-370"><span class="linenos"> 370</span></a>
</span><span id="L-371"><a href="#L-371"><span class="linenos"> 371</span></a><span class="k">def</span> <span class="nf">intro_frame_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OrderedDictType</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos"> 372</span></a>    <span class="k">return</span> <span class="n">OrderedDict</span><span class="p">(</span><span class="n">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">))</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos"> 373</span></a>
</span><span id="L-374"><a href="#L-374"><span class="linenos"> 374</span></a>
</span><span id="L-375"><a href="#L-375"><span class="linenos"> 375</span></a><span class="k">def</span> <span class="nf">intro_func_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OrderedDictType</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos"> 376</span></a>    <span class="k">return</span> <span class="n">intro_frame_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos"> 377</span></a>
</span><span id="L-378"><a href="#L-378"><span class="linenos"> 378</span></a>
</span><span id="L-379"><a href="#L-379"><span class="linenos"> 379</span></a><span class="k">def</span> <span class="nf">code_params_with_values_to_signature_items_gen</span><span class="p">(</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos"> 380</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params_with_values</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos"> 381</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos"> 382</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos"> 383</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos"> 384</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos"> 385</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos"> 386</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos"> 387</span></a>    
</span><span id="L-388"><a href="#L-388"><span class="linenos"> 388</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos"> 389</span></a>        <span class="n">arg_name</span><span class="p">,</span> <span class="n">arg_value</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos"> 390</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">positional_only_delimiter_place</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">index</span> <span class="o">==</span> <span class="n">positional_only_delimiter_place</span><span class="p">):</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos"> 391</span></a>            <span class="k">yield</span> <span class="s1">&#39;/&#39;</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos"> 392</span></a>        
</span><span id="L-393"><a href="#L-393"><span class="linenos"> 393</span></a>        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos"> 394</span></a>            <span class="k">yield</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">arg_value</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos"> 395</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos"> 396</span></a>            <span class="k">yield</span> <span class="nb">str</span><span class="p">(</span><span class="n">arg_value</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos"> 397</span></a>    
</span><span id="L-398"><a href="#L-398"><span class="linenos"> 398</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos"> 399</span></a>        <span class="k">yield</span> <span class="s1">&#39;*&#39;</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos"> 400</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos"> 401</span></a>            <span class="n">arg_name</span><span class="p">,</span> <span class="n">arg_value</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos"> 402</span></a>            <span class="k">yield</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">arg_value</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos"> 403</span></a>
</span><span id="L-404"><a href="#L-404"><span class="linenos"> 404</span></a>
</span><span id="L-405"><a href="#L-405"><span class="linenos"> 405</span></a><span class="k">def</span> <span class="nf">code_params_to_signature_items_gen</span><span class="p">(</span><span class="n">code_params</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos"> 406</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos"> 407</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos"> 408</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos"> 409</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos"> 410</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos"> 411</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos"> 412</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos"> 413</span></a>    
</span><span id="L-414"><a href="#L-414"><span class="linenos"> 414</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos"> 415</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">positional_only_delimiter_place</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">index</span> <span class="o">==</span> <span class="n">positional_only_delimiter_place</span><span class="p">):</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos"> 416</span></a>            <span class="k">yield</span> <span class="s1">&#39;/&#39;</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos"> 417</span></a>        
</span><span id="L-418"><a href="#L-418"><span class="linenos"> 418</span></a>        <span class="c1"># yield arg[0]</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos"> 419</span></a>        <span class="k">yield</span> <span class="n">arg</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos"> 420</span></a>    
</span><span id="L-421"><a href="#L-421"><span class="linenos"> 421</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos"> 422</span></a>        <span class="k">yield</span> <span class="s1">&#39;*&#39;</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos"> 423</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos"> 424</span></a>            <span class="c1"># yield arg[0]</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos"> 425</span></a>            <span class="k">yield</span> <span class="n">arg</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos"> 426</span></a>
</span><span id="L-427"><a href="#L-427"><span class="linenos"> 427</span></a>
</span><span id="L-428"><a href="#L-428"><span class="linenos"> 428</span></a><span class="k">def</span> <span class="nf">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos"> 429</span></a>    <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos"> 430</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos"> 431</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos"> 432</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos"> 433</span></a>    
</span><span id="L-434"><a href="#L-434"><span class="linenos"> 434</span></a>    <span class="k">return</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">code_params_with_values_to_signature_items_gen</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">))</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos"> 435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos"> 436</span></a>
</span><span id="L-437"><a href="#L-437"><span class="linenos"> 437</span></a><span class="k">def</span> <span class="nf">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos"> 438</span></a>    <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos"> 439</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos"> 440</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos"> 441</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos"> 442</span></a>    
</span><span id="L-443"><a href="#L-443"><span class="linenos"> 443</span></a>    <span class="k">return</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">code_params_to_signature_items_gen</span><span class="p">(</span><span class="n">param_names</span><span class="p">))</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos"> 444</span></a>
</span><span id="L-445"><a href="#L-445"><span class="linenos"> 445</span></a>
</span><span id="L-446"><a href="#L-446"><span class="linenos"> 446</span></a><span class="k">def</span> <span class="nf">entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos"> 447</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos"> 448</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos"> 449</span></a>    
</span><span id="L-450"><a href="#L-450"><span class="linenos"> 450</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos"> 451</span></a>        <span class="n">code</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos"> 452</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos"> 453</span></a>        <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos"> 454</span></a>    
</span><span id="L-455"><a href="#L-455"><span class="linenos"> 455</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos"> 456</span></a>    <span class="n">param_names</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos"> 457</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos"> 458</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos"> 459</span></a>
</span><span id="L-460"><a href="#L-460"><span class="linenos"> 460</span></a>
</span><span id="L-461"><a href="#L-461"><span class="linenos"> 461</span></a><span class="k">def</span> <span class="nf">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos"> 462</span></a>    <span class="k">if</span> <span class="n">has_code</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos"> 463</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos"> 464</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos"> 465</span></a>        
</span><span id="L-466"><a href="#L-466"><span class="linenos"> 466</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos"> 467</span></a>            <span class="n">code</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos"> 468</span></a>            <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos"> 469</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos"> 470</span></a>            <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos"> 471</span></a>            <span class="n">func_name</span> <span class="o">=</span> <span class="n">func_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos"> 472</span></a>        
</span><span id="L-473"><a href="#L-473"><span class="linenos"> 473</span></a>        <span class="n">param_names</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos"> 474</span></a>        <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos"> 475</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos"> 476</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos"> 477</span></a>        <span class="n">entity_type_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos"> 478</span></a>        <span class="n">entity_properties_with_values</span> <span class="o">=</span> <span class="n">entity_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos"> 479</span></a>        <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos"> 480</span></a>            <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos"> 481</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos"> 482</span></a>            <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos"> 483</span></a>        
</span><span id="L-484"><a href="#L-484"><span class="linenos"> 484</span></a>        <span class="n">entity_properties_str</span> <span class="o">=</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">entity_properties_with_values</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos"> 485</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity_type_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">entity_properties_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos"> 486</span></a>
</span><span id="L-487"><a href="#L-487"><span class="linenos"> 487</span></a>
</span><span id="L-488"><a href="#L-488"><span class="linenos"> 488</span></a><span class="k">def</span> <span class="nf">entity_repr_owner_based</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos"> 489</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos"> 490</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos"> 491</span></a>    
</span><span id="L-492"><a href="#L-492"><span class="linenos"> 492</span></a>    <span class="n">owner</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos"> 493</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos"> 494</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner</span><span class="p">)</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos"> 495</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos"> 496</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="L-497"><a href="#L-497"><span class="linenos"> 497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos"> 498</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">):</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos"> 499</span></a>        <span class="n">_entity_repr_limited</span> <span class="o">=</span> <span class="n">entity_repr_limited_try_qualname</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos"> 500</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos"> 501</span></a>        <span class="n">_entity_repr_limited</span> <span class="o">=</span> <span class="n">entity_repr_limited</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos"> 502</span></a>    
</span><span id="L-503"><a href="#L-503"><span class="linenos"> 503</span></a>    <span class="k">if</span> <span class="n">owner_repr</span><span class="p">:</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos"> 504</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">_entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span><span class="w"> </span><span class="n">formatted</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-505"><a href="#L-505"><span class="linenos"> 505</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos"> 506</span></a>        <span class="k">return</span> <span class="n">_entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos"> 507</span></a>
</span><span id="L-508"><a href="#L-508"><span class="linenos"> 508</span></a>
</span><span id="L-509"><a href="#L-509"><span class="linenos"> 509</span></a><span class="k">def</span> <span class="nf">entity_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-510"><a href="#L-510"><span class="linenos"> 510</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos"> 511</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos"> 512</span></a>    
</span><span id="L-513"><a href="#L-513"><span class="linenos"> 513</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos"> 514</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos"> 515</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">module</span><span class="p">)</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos"> 516</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos"> 517</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos"> 518</span></a>    
</span><span id="L-519"><a href="#L-519"><span class="linenos"> 519</span></a>    <span class="k">if</span> <span class="n">owner_repr</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos"> 520</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span><span class="w"> </span><span class="n">formatted</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos"> 521</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos"> 522</span></a>        <span class="k">return</span> <span class="n">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos"> 523</span></a>
</span><span id="L-524"><a href="#L-524"><span class="linenos"> 524</span></a>
</span><span id="L-525"><a href="#L-525"><span class="linenos"> 525</span></a><span class="k">def</span> <span class="nf">entity_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos"> 526</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos"> 527</span></a><span class="sd">    Example:</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos"> 528</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest</span>
</span><span id="L-529"><a href="#L-529"><span class="linenos"> 529</span></a><span class="sd">        from cengal.introspection.inspect import entity_properties</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos"> 530</span></a><span class="sd">        </span>
</span><span id="L-531"><a href="#L-531"><span class="linenos"> 531</span></a><span class="sd">        print(entity_properties(WaitCoroRequest))</span>
</span><span id="L-532"><a href="#L-532"><span class="linenos"> 532</span></a><span class="sd">        &gt;&gt; {&#39;__weakref__&#39;, &#39;put_list&#39;, &#39;fastest&#39;, &#39;atomic&#39;, &#39;list&#39;, &#39;single&#39;, &#39;put_fastest&#39;, &#39;_save&#39;, &#39;put_single&#39;, &#39;put_atomic&#39;}</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos"> 533</span></a>
</span><span id="L-534"><a href="#L-534"><span class="linenos"> 534</span></a>
</span><span id="L-535"><a href="#L-535"><span class="linenos"> 535</span></a><span class="sd">        print(entity_properties(WaitCoroRequest()))</span>
</span><span id="L-536"><a href="#L-536"><span class="linenos"> 536</span></a><span class="sd">        &gt;&gt; {&#39;result_required&#39;, &#39;args&#39;, &#39;tree&#39;, &#39;kill_on_timeout&#39;, &#39;timeout&#39;, &#39;request_type&#39;, &#39;kwargs&#39;, &#39;provide_to_request_handler&#39;}</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos"> 537</span></a>
</span><span id="L-538"><a href="#L-538"><span class="linenos"> 538</span></a>
</span><span id="L-539"><a href="#L-539"><span class="linenos"> 539</span></a><span class="sd">        def my_func(a, b, *, c, d):</span>
</span><span id="L-540"><a href="#L-540"><span class="linenos"> 540</span></a><span class="sd">            return a + b + c + d</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos"> 541</span></a>
</span><span id="L-542"><a href="#L-542"><span class="linenos"> 542</span></a><span class="sd">        my_func.my_property = 2</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos"> 543</span></a>
</span><span id="L-544"><a href="#L-544"><span class="linenos"> 544</span></a><span class="sd">        print(entity_properties(my_func))</span>
</span><span id="L-545"><a href="#L-545"><span class="linenos"> 545</span></a><span class="sd">        &gt;&gt; {&#39;my_property&#39;}</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos"> 546</span></a>
</span><span id="L-547"><a href="#L-547"><span class="linenos"> 547</span></a>
</span><span id="L-548"><a href="#L-548"><span class="linenos"> 548</span></a><span class="sd">    Args:</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos"> 549</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos"> 550</span></a>
</span><span id="L-551"><a href="#L-551"><span class="linenos"> 551</span></a><span class="sd">    Returns:</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos"> 552</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="L-553"><a href="#L-553"><span class="linenos"> 553</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-554"><a href="#L-554"><span class="linenos"> 554</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos"> 555</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-556"><a href="#L-556"><span class="linenos"> 556</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos"> 557</span></a>
</span><span id="L-558"><a href="#L-558"><span class="linenos"> 558</span></a>
</span><span id="L-559"><a href="#L-559"><span class="linenos"> 559</span></a><span class="k">def</span> <span class="nf">entity_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos"> 560</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos"> 561</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">entity_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos"> 562</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos"> 563</span></a>    
</span><span id="L-564"><a href="#L-564"><span class="linenos"> 564</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos"> 565</span></a>
</span><span id="L-566"><a href="#L-566"><span class="linenos"> 566</span></a>
</span><span id="L-567"><a href="#L-567"><span class="linenos"> 567</span></a><span class="k">def</span> <span class="nf">class_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos"> 568</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos"> 569</span></a><span class="sd">    Example:</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos"> 570</span></a>
</span><span id="L-571"><a href="#L-571"><span class="linenos"> 571</span></a><span class="sd">    Args:</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos"> 572</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="L-573"><a href="#L-573"><span class="linenos"> 573</span></a>
</span><span id="L-574"><a href="#L-574"><span class="linenos"> 574</span></a><span class="sd">    Returns:</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos"> 575</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos"> 576</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-577"><a href="#L-577"><span class="linenos"> 577</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos"> 578</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos"> 579</span></a>    <span class="n">mro</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos"> 580</span></a>    <span class="n">base_members</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos"> 581</span></a>    <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="n">mro</span><span class="p">:</span>
</span><span id="L-582"><a href="#L-582"><span class="linenos"> 582</span></a>        <span class="k">if</span> <span class="n">base</span> <span class="ow">is</span> <span class="n">entity</span><span class="p">:</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos"> 583</span></a>            <span class="k">continue</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos"> 584</span></a>        
</span><span id="L-585"><a href="#L-585"><span class="linenos"> 585</span></a>        <span class="n">base_members</span> <span class="o">|=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">base</span><span class="p">))</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos"> 586</span></a>    
</span><span id="L-587"><a href="#L-587"><span class="linenos"> 587</span></a>    <span class="k">return</span> <span class="p">(</span><span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span><span class="p">)</span> <span class="o">-</span> <span class="n">base_members</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos"> 588</span></a>
</span><span id="L-589"><a href="#L-589"><span class="linenos"> 589</span></a>
</span><span id="L-590"><a href="#L-590"><span class="linenos"> 590</span></a><span class="k">def</span> <span class="nf">class_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos"> 591</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-592"><a href="#L-592"><span class="linenos"> 592</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos"> 593</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos"> 594</span></a>    
</span><span id="L-595"><a href="#L-595"><span class="linenos"> 595</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos"> 596</span></a>
</span><span id="L-597"><a href="#L-597"><span class="linenos"> 597</span></a>
</span><span id="L-598"><a href="#L-598"><span class="linenos"> 598</span></a><span class="k">def</span> <span class="nf">class_properties_withot_object</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-599"><a href="#L-599"><span class="linenos"> 599</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos"> 600</span></a><span class="sd">    Example:</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos"> 601</span></a>
</span><span id="L-602"><a href="#L-602"><span class="linenos"> 602</span></a><span class="sd">    Args:</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos"> 603</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos"> 604</span></a>
</span><span id="L-605"><a href="#L-605"><span class="linenos"> 605</span></a><span class="sd">    Returns:</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos"> 606</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="L-607"><a href="#L-607"><span class="linenos"> 607</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-608"><a href="#L-608"><span class="linenos"> 608</span></a>    <span class="n">object_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">object</span><span class="p">))</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos"> 609</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="L-610"><a href="#L-610"><span class="linenos"> 610</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">object_type_items</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos"> 611</span></a>
</span><span id="L-612"><a href="#L-612"><span class="linenos"> 612</span></a>
</span><span id="L-613"><a href="#L-613"><span class="linenos"> 613</span></a><span class="k">def</span> <span class="nf">class_properties_withot_object_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-614"><a href="#L-614"><span class="linenos"> 614</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos"> 615</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties_withot_object</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos"> 616</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos"> 617</span></a>    
</span><span id="L-618"><a href="#L-618"><span class="linenos"> 618</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos"> 619</span></a>
</span><span id="L-620"><a href="#L-620"><span class="linenos"> 620</span></a>
</span><span id="L-621"><a href="#L-621"><span class="linenos"> 621</span></a><span class="k">def</span> <span class="nf">class_properties_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos"> 622</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos"> 623</span></a><span class="sd">    Example:</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos"> 624</span></a>
</span><span id="L-625"><a href="#L-625"><span class="linenos"> 625</span></a><span class="sd">    Args:</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos"> 626</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="L-627"><a href="#L-627"><span class="linenos"> 627</span></a>
</span><span id="L-628"><a href="#L-628"><span class="linenos"> 628</span></a><span class="sd">    Returns:</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos"> 629</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos"> 630</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-631"><a href="#L-631"><span class="linenos"> 631</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="L-632"><a href="#L-632"><span class="linenos"> 632</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos"> 633</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos"> 634</span></a>
</span><span id="L-635"><a href="#L-635"><span class="linenos"> 635</span></a>
</span><span id="L-636"><a href="#L-636"><span class="linenos"> 636</span></a><span class="k">def</span> <span class="nf">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos"> 637</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos"> 638</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="L-639"><a href="#L-639"><span class="linenos"> 639</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos"> 640</span></a>    
</span><span id="L-641"><a href="#L-641"><span class="linenos"> 641</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-642"><a href="#L-642"><span class="linenos"> 642</span></a>
</span><span id="L-643"><a href="#L-643"><span class="linenos"> 643</span></a>
</span><span id="L-644"><a href="#L-644"><span class="linenos"> 644</span></a><span class="k">def</span> <span class="nf">intro_frame_repr_limited</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-645"><a href="#L-645"><span class="linenos"> 645</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span><span class="p">)</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos"> 646</span></a>    <span class="n">params_with_values</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos"> 647</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos"> 648</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos"> 649</span></a>
</span><span id="L-650"><a href="#L-650"><span class="linenos"> 650</span></a>
</span><span id="L-651"><a href="#L-651"><span class="linenos"> 651</span></a><span class="k">def</span> <span class="nf">intro_frame_repr</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos"> 652</span></a>    <span class="n">code</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos"> 653</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos"> 654</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos"> 655</span></a>    <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">module</span><span class="p">)</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos"> 656</span></a>    <span class="n">params_with_values</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos"> 657</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="L-658"><a href="#L-658"><span class="linenos"> 658</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos"> 659</span></a>
</span><span id="L-660"><a href="#L-660"><span class="linenos"> 660</span></a>
</span><span id="L-661"><a href="#L-661"><span class="linenos"> 661</span></a><span class="k">def</span> <span class="nf">intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos"> 662</span></a>    <span class="k">return</span> <span class="n">intro_frame_repr_limited</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos"> 663</span></a>
</span><span id="L-664"><a href="#L-664"><span class="linenos"> 664</span></a>
</span><span id="L-665"><a href="#L-665"><span class="linenos"> 665</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos"> 666</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-667"><a href="#L-667"><span class="linenos"> 667</span></a>
</span><span id="L-668"><a href="#L-668"><span class="linenos"> 668</span></a>
</span><span id="L-669"><a href="#L-669"><span class="linenos"> 669</span></a><span class="n">pifrl</span> <span class="o">=</span> <span class="n">print_intro_func_repr_limited</span>
</span><span id="L-670"><a href="#L-670"><span class="linenos"> 670</span></a>
</span><span id="L-671"><a href="#L-671"><span class="linenos"> 671</span></a>
</span><span id="L-672"><a href="#L-672"><span class="linenos"> 672</span></a><span class="k">def</span> <span class="nf">intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos"> 673</span></a>    <span class="k">return</span> <span class="n">intro_frame_repr</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="L-674"><a href="#L-674"><span class="linenos"> 674</span></a>
</span><span id="L-675"><a href="#L-675"><span class="linenos"> 675</span></a>
</span><span id="L-676"><a href="#L-676"><span class="linenos"> 676</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos"> 677</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos"> 678</span></a>
</span><span id="L-679"><a href="#L-679"><span class="linenos"> 679</span></a>
</span><span id="L-680"><a href="#L-680"><span class="linenos"> 680</span></a><span class="n">pifr</span> <span class="o">=</span> <span class="n">print_intro_func_repr</span>
</span><span id="L-681"><a href="#L-681"><span class="linenos"> 681</span></a>
</span><span id="L-682"><a href="#L-682"><span class="linenos"> 682</span></a>
</span><span id="L-683"><a href="#L-683"><span class="linenos"> 683</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="L-684"><a href="#L-684"><span class="linenos"> 684</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns string with data info: type and value</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos"> 685</span></a>
</span><span id="L-686"><a href="#L-686"><span class="linenos"> 686</span></a><span class="sd">    Args:</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos"> 687</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="L-688"><a href="#L-688"><span class="linenos"> 688</span></a>
</span><span id="L-689"><a href="#L-689"><span class="linenos"> 689</span></a><span class="sd">    Returns:</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos"> 690</span></a><span class="sd">        _type_: _description_</span>
</span><span id="L-691"><a href="#L-691"><span class="linenos"> 691</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-692"><a href="#L-692"><span class="linenos"> 692</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos"> 693</span></a>
</span><span id="L-694"><a href="#L-694"><span class="linenos"> 694</span></a>
</span><span id="L-695"><a href="#L-695"><span class="linenos"> 695</span></a><span class="n">gsodi</span> <span class="o">=</span> <span class="n">get_str_of_data_info</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos"> 696</span></a>
</span><span id="L-697"><a href="#L-697"><span class="linenos"> 697</span></a>
</span><span id="L-698"><a href="#L-698"><span class="linenos"> 698</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos"> 699</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data info: type and value</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos"> 700</span></a>
</span><span id="L-701"><a href="#L-701"><span class="linenos"> 701</span></a><span class="sd">    Args:</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos"> 702</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos"> 703</span></a>
</span><span id="L-704"><a href="#L-704"><span class="linenos"> 704</span></a><span class="sd">    Returns:</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos"> 705</span></a><span class="sd">        _type_: _description_</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos"> 706</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-707"><a href="#L-707"><span class="linenos"> 707</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos"> 708</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos"> 709</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="L-710"><a href="#L-710"><span class="linenos"> 710</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos"> 711</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-712"><a href="#L-712"><span class="linenos"> 712</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="L-713"><a href="#L-713"><span class="linenos"> 713</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="se">\n</span><span class="si">{</span><span class="n">data_str</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos"> 714</span></a>
</span><span id="L-715"><a href="#L-715"><span class="linenos"> 715</span></a>
</span><span id="L-716"><a href="#L-716"><span class="linenos"> 716</span></a><span class="n">gmsodi</span> <span class="o">=</span> <span class="n">get_multistr_of_data_info</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos"> 717</span></a>
</span><span id="L-718"><a href="#L-718"><span class="linenos"> 718</span></a>
</span><span id="L-719"><a href="#L-719"><span class="linenos"> 719</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_value</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos"> 720</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data value</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos"> 721</span></a>
</span><span id="L-722"><a href="#L-722"><span class="linenos"> 722</span></a><span class="sd">    Args:</span>
</span><span id="L-723"><a href="#L-723"><span class="linenos"> 723</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos"> 724</span></a>
</span><span id="L-725"><a href="#L-725"><span class="linenos"> 725</span></a><span class="sd">    Returns:</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos"> 726</span></a><span class="sd">        _type_: _description_</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos"> 727</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="L-728"><a href="#L-728"><span class="linenos"> 728</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos"> 729</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="L-730"><a href="#L-730"><span class="linenos"> 730</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos"> 731</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos"> 732</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos"> 733</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="L-734"><a href="#L-734"><span class="linenos"> 734</span></a>    <span class="k">return</span> <span class="n">data_str</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos"> 735</span></a>
</span><span id="L-736"><a href="#L-736"><span class="linenos"> 736</span></a>
</span><span id="L-737"><a href="#L-737"><span class="linenos"> 737</span></a><span class="n">gmsodv</span> <span class="o">=</span> <span class="n">get_multistr_of_data_value</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos"> 738</span></a>
</span><span id="L-739"><a href="#L-739"><span class="linenos"> 739</span></a>
</span><span id="L-740"><a href="#L-740"><span class="linenos"> 740</span></a><span class="k">def</span> <span class="nf">print_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos"> 741</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Print data info: type and value</span>
</span><span id="L-742"><a href="#L-742"><span class="linenos"> 742</span></a>
</span><span id="L-743"><a href="#L-743"><span class="linenos"> 743</span></a><span class="sd">    Args:</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos"> 744</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="L-745"><a href="#L-745"><span class="linenos"> 745</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-746"><a href="#L-746"><span class="linenos"> 746</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</span><span id="L-747"><a href="#L-747"><span class="linenos"> 747</span></a>
</span><span id="L-748"><a href="#L-748"><span class="linenos"> 748</span></a>
</span><span id="L-749"><a href="#L-749"><span class="linenos"> 749</span></a><span class="n">pdi</span> <span class="o">=</span> <span class="n">print_data_info</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos"> 750</span></a>
</span><span id="L-751"><a href="#L-751"><span class="linenos"> 751</span></a>
</span><span id="L-752"><a href="#L-752"><span class="linenos"> 752</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos"> 753</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;&lt;</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">&gt;&gt; type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos"> 754</span></a>
</span><span id="L-755"><a href="#L-755"><span class="linenos"> 755</span></a>
</span><span id="L-756"><a href="#L-756"><span class="linenos"> 756</span></a><span class="n">gsodin</span> <span class="o">=</span> <span class="n">get_str_of_data_info_named</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos"> 757</span></a>
</span><span id="L-758"><a href="#L-758"><span class="linenos"> 758</span></a>
</span><span id="L-759"><a href="#L-759"><span class="linenos"> 759</span></a><span class="k">def</span> <span class="nf">print_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos"> 760</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">))</span>
</span><span id="L-761"><a href="#L-761"><span class="linenos"> 761</span></a>
</span><span id="L-762"><a href="#L-762"><span class="linenos"> 762</span></a>
</span><span id="L-763"><a href="#L-763"><span class="linenos"> 763</span></a><span class="n">pdin</span> <span class="o">=</span> <span class="n">print_data_info_named</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos"> 764</span></a>
</span><span id="L-765"><a href="#L-765"><span class="linenos"> 765</span></a>
</span><span id="L-766"><a href="#L-766"><span class="linenos"> 766</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos"> 767</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos"> 768</span></a>    <span class="n">data</span> <span class="o">=</span> <span class="n">fr</span><span class="o">.</span><span class="n">f_locals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="L-769"><a href="#L-769"><span class="linenos"> 769</span></a>    <span class="k">return</span> <span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
</span><span id="L-770"><a href="#L-770"><span class="linenos"> 770</span></a>
</span><span id="L-771"><a href="#L-771"><span class="linenos"> 771</span></a>
</span><span id="L-772"><a href="#L-772"><span class="linenos"> 772</span></a><span class="n">gsodibn</span> <span class="o">=</span> <span class="n">get_str_of_data_info_by_name</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos"> 773</span></a>
</span><span id="L-774"><a href="#L-774"><span class="linenos"> 774</span></a>
</span><span id="L-775"><a href="#L-775"><span class="linenos"> 775</span></a><span class="k">def</span> <span class="nf">print_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-776"><a href="#L-776"><span class="linenos"> 776</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span><span id="L-777"><a href="#L-777"><span class="linenos"> 777</span></a>
</span><span id="L-778"><a href="#L-778"><span class="linenos"> 778</span></a>
</span><span id="L-779"><a href="#L-779"><span class="linenos"> 779</span></a><span class="n">pdibn</span> <span class="o">=</span> <span class="n">print_data_info_by_name</span>
</span><span id="L-780"><a href="#L-780"><span class="linenos"> 780</span></a>
</span><span id="L-781"><a href="#L-781"><span class="linenos"> 781</span></a>
</span><span id="L-782"><a href="#L-782"><span class="linenos"> 782</span></a><span class="k">def</span> <span class="nf">is_descriptor</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos"> 783</span></a>    <span class="k">return</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__get__&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__set__&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__delete__&#39;</span><span class="p">)</span>
</span><span id="L-784"><a href="#L-784"><span class="linenos"> 784</span></a>
</span><span id="L-785"><a href="#L-785"><span class="linenos"> 785</span></a>
</span><span id="L-786"><a href="#L-786"><span class="linenos"> 786</span></a><span class="k">def</span> <span class="nf">is_setable_data_descriptor</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos"> 787</span></a>    <span class="k">return</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__get__&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__set__&#39;</span><span class="p">)</span>
</span><span id="L-788"><a href="#L-788"><span class="linenos"> 788</span></a>
</span><span id="L-789"><a href="#L-789"><span class="linenos"> 789</span></a>
</span><span id="L-790"><a href="#L-790"><span class="linenos"> 790</span></a><span class="k">def</span> <span class="nf">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos"> 791</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos"> 792</span></a><span class="sd">        class _foo:</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos"> 793</span></a><span class="sd">        __slots__ = [&#39;foo&#39;, &#39;bar&#39;]</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos"> 794</span></a>
</span><span id="L-795"><a href="#L-795"><span class="linenos"> 795</span></a><span class="sd">        def __init__(self):</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos"> 796</span></a><span class="sd">            self.bar = 2</span>
</span><span id="L-797"><a href="#L-797"><span class="linenos"> 797</span></a>
</span><span id="L-798"><a href="#L-798"><span class="linenos"> 798</span></a><span class="sd">    &#39;foo&#39; - not filled</span>
</span><span id="L-799"><a href="#L-799"><span class="linenos"> 799</span></a><span class="sd">    &#39;bar&#39; - filled</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos"> 800</span></a>
</span><span id="L-801"><a href="#L-801"><span class="linenos"> 801</span></a><span class="sd">    Args:</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos"> 802</span></a><span class="sd">        owning_object (_type_): _description_</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos"> 803</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="L-804"><a href="#L-804"><span class="linenos"> 804</span></a>
</span><span id="L-805"><a href="#L-805"><span class="linenos"> 805</span></a><span class="sd">    Returns:</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos"> 806</span></a><span class="sd">        _type_: _description_</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos"> 807</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="L-808"><a href="#L-808"><span class="linenos"> 808</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos"> 809</span></a>        <span class="n">entity</span><span class="o">.</span><span class="fm">__get__</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos"> 810</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-811"><a href="#L-811"><span class="linenos"> 811</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-812"><a href="#L-812"><span class="linenos"> 812</span></a>    
</span><span id="L-813"><a href="#L-813"><span class="linenos"> 813</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos"> 814</span></a>
</span><span id="L-815"><a href="#L-815"><span class="linenos"> 815</span></a>
</span><span id="L-816"><a href="#L-816"><span class="linenos"> 816</span></a><span class="k">def</span> <span class="nf">filled_slots_names</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos"> 817</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos"> 818</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos"> 819</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-820"><a href="#L-820"><span class="linenos"> 820</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-821"><a href="#L-821"><span class="linenos"> 821</span></a>    
</span><span id="L-822"><a href="#L-822"><span class="linenos"> 822</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-823"><a href="#L-823"><span class="linenos"> 823</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="L-824"><a href="#L-824"><span class="linenos"> 824</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="L-825"><a href="#L-825"><span class="linenos"> 825</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="L-826"><a href="#L-826"><span class="linenos"> 826</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">slot_name</span><span class="p">)</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos"> 827</span></a>    
</span><span id="L-828"><a href="#L-828"><span class="linenos"> 828</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-829"><a href="#L-829"><span class="linenos"> 829</span></a>
</span><span id="L-830"><a href="#L-830"><span class="linenos"> 830</span></a>
</span><span id="L-831"><a href="#L-831"><span class="linenos"> 831</span></a><span class="k">def</span> <span class="nf">filled_slots</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]:</span>
</span><span id="L-832"><a href="#L-832"><span class="linenos"> 832</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos"> 833</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos"> 834</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-835"><a href="#L-835"><span class="linenos"> 835</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-836"><a href="#L-836"><span class="linenos"> 836</span></a>    
</span><span id="L-837"><a href="#L-837"><span class="linenos"> 837</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos"> 838</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="L-839"><a href="#L-839"><span class="linenos"> 839</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="L-840"><a href="#L-840"><span class="linenos"> 840</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="L-841"><a href="#L-841"><span class="linenos"> 841</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">slot</span><span class="p">)</span>
</span><span id="L-842"><a href="#L-842"><span class="linenos"> 842</span></a>    
</span><span id="L-843"><a href="#L-843"><span class="linenos"> 843</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-844"><a href="#L-844"><span class="linenos"> 844</span></a>
</span><span id="L-845"><a href="#L-845"><span class="linenos"> 845</span></a>
</span><span id="L-846"><a href="#L-846"><span class="linenos"> 846</span></a><span class="k">def</span> <span class="nf">filled_slots_with_names</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]:</span>
</span><span id="L-847"><a href="#L-847"><span class="linenos"> 847</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-848"><a href="#L-848"><span class="linenos"> 848</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-849"><a href="#L-849"><span class="linenos"> 849</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-850"><a href="#L-850"><span class="linenos"> 850</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-851"><a href="#L-851"><span class="linenos"> 851</span></a>    
</span><span id="L-852"><a href="#L-852"><span class="linenos"> 852</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-853"><a href="#L-853"><span class="linenos"> 853</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="L-854"><a href="#L-854"><span class="linenos"> 854</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="L-855"><a href="#L-855"><span class="linenos"> 855</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="L-856"><a href="#L-856"><span class="linenos"> 856</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">slot_name</span><span class="p">,</span> <span class="n">slot</span><span class="p">))</span>
</span><span id="L-857"><a href="#L-857"><span class="linenos"> 857</span></a>    
</span><span id="L-858"><a href="#L-858"><span class="linenos"> 858</span></a>    <span class="k">return</span> <span class="n">result</span>
</span><span id="L-859"><a href="#L-859"><span class="linenos"> 859</span></a>
</span><span id="L-860"><a href="#L-860"><span class="linenos"> 860</span></a>
</span><span id="L-861"><a href="#L-861"><span class="linenos"> 861</span></a><span class="k">def</span> <span class="nf">filled_slots_with_names_gen</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-862"><a href="#L-862"><span class="linenos"> 862</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-863"><a href="#L-863"><span class="linenos"> 863</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-864"><a href="#L-864"><span class="linenos"> 864</span></a>        <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="L-865"><a href="#L-865"><span class="linenos"> 865</span></a>            <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect__getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="L-866"><a href="#L-866"><span class="linenos"> 866</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-867"><a href="#L-867"><span class="linenos"> 867</span></a>                <span class="n">slot</span><span class="o">.</span><span class="fm">__get__</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span>
</span><span id="L-868"><a href="#L-868"><span class="linenos"> 868</span></a>                <span class="k">yield</span> <span class="p">(</span><span class="n">slot_name</span><span class="p">,</span> <span class="n">slot</span><span class="p">)</span>
</span><span id="L-869"><a href="#L-869"><span class="linenos"> 869</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-870"><a href="#L-870"><span class="linenos"> 870</span></a>                <span class="k">pass</span>
</span><span id="L-871"><a href="#L-871"><span class="linenos"> 871</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-872"><a href="#L-872"><span class="linenos"> 872</span></a>        <span class="k">pass</span>
</span><span id="L-873"><a href="#L-873"><span class="linenos"> 873</span></a>
</span><span id="L-874"><a href="#L-874"><span class="linenos"> 874</span></a>
</span><span id="L-875"><a href="#L-875"><span class="linenos"> 875</span></a><span class="k">def</span> <span class="nf">filled_slot_names_with_values_gen</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-876"><a href="#L-876"><span class="linenos"> 876</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-877"><a href="#L-877"><span class="linenos"> 877</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="L-878"><a href="#L-878"><span class="linenos"> 878</span></a>        <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="L-879"><a href="#L-879"><span class="linenos"> 879</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-880"><a href="#L-880"><span class="linenos"> 880</span></a>                <span class="k">yield</span> <span class="p">(</span><span class="n">slot_name</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">))</span>
</span><span id="L-881"><a href="#L-881"><span class="linenos"> 881</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-882"><a href="#L-882"><span class="linenos"> 882</span></a>                <span class="k">pass</span>
</span><span id="L-883"><a href="#L-883"><span class="linenos"> 883</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-884"><a href="#L-884"><span class="linenos"> 884</span></a>        <span class="k">pass</span>
</span><span id="L-885"><a href="#L-885"><span class="linenos"> 885</span></a>
</span><span id="L-886"><a href="#L-886"><span class="linenos"> 886</span></a>
</span><span id="L-887"><a href="#L-887"><span class="linenos"> 887</span></a><span class="k">def</span> <span class="nf">current_entity_name</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-888"><a href="#L-888"><span class="linenos"> 888</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-889"><a href="#L-889"><span class="linenos"> 889</span></a>    <span class="k">return</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">fr</span><span class="p">)</span>
</span><span id="L-890"><a href="#L-890"><span class="linenos"> 890</span></a>    <span class="c1"># entity_name = code_name(fr.f_code)</span>
</span><span id="L-891"><a href="#L-891"><span class="linenos"> 891</span></a>    <span class="c1"># # print(dir(fr.f_code))</span>
</span><span id="L-892"><a href="#L-892"><span class="linenos"> 892</span></a>    <span class="c1"># # print(fr.f_code.__class__)</span>
</span><span id="L-893"><a href="#L-893"><span class="linenos"> 893</span></a>    <span class="c1"># # print(dir(fr))</span>
</span><span id="L-894"><a href="#L-894"><span class="linenos"> 894</span></a>    <span class="c1"># # print(fr.__class__)</span>
</span><span id="L-895"><a href="#L-895"><span class="linenos"> 895</span></a>    <span class="c1"># return entity_name</span>
</span><span id="L-896"><a href="#L-896"><span class="linenos"> 896</span></a>
</span><span id="L-897"><a href="#L-897"><span class="linenos"> 897</span></a>
</span><span id="L-898"><a href="#L-898"><span class="linenos"> 898</span></a><span class="n">cen</span> <span class="o">=</span> <span class="n">current_entity_name</span>
</span><span id="L-899"><a href="#L-899"><span class="linenos"> 899</span></a>
</span><span id="L-900"><a href="#L-900"><span class="linenos"> 900</span></a>
</span><span id="L-901"><a href="#L-901"><span class="linenos"> 901</span></a><span class="k">def</span> <span class="nf">current_entity_owner_name</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="L-902"><a href="#L-902"><span class="linenos"> 902</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="L-903"><a href="#L-903"><span class="linenos"> 903</span></a>    <span class="k">return</span> <span class="n">owner_name</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">fr</span><span class="o">.</span><span class="n">f_code</span><span class="p">))</span>
</span><span id="L-904"><a href="#L-904"><span class="linenos"> 904</span></a>
</span><span id="L-905"><a href="#L-905"><span class="linenos"> 905</span></a>
</span><span id="L-906"><a href="#L-906"><span class="linenos"> 906</span></a><span class="c1"># def current_entity_full_name(depth: Optional[int] = 1):</span>
</span><span id="L-907"><a href="#L-907"><span class="linenos"> 907</span></a><span class="c1">#     fr = frame(depth + 1)</span>
</span><span id="L-908"><a href="#L-908"><span class="linenos"> 908</span></a><span class="c1">#     entity_name = code_name(fr.f_code)</span>
</span><span id="L-909"><a href="#L-909"><span class="linenos"> 909</span></a><span class="c1">#     return entity_name</span>
</span><span id="L-910"><a href="#L-910"><span class="linenos"> 910</span></a>
</span><span id="L-911"><a href="#L-911"><span class="linenos"> 911</span></a>
</span><span id="L-912"><a href="#L-912"><span class="linenos"> 912</span></a><span class="c1"># cefn = current_entity_full_name</span>
</span><span id="L-913"><a href="#L-913"><span class="linenos"> 913</span></a>
</span><span id="L-914"><a href="#L-914"><span class="linenos"> 914</span></a>
</span><span id="L-915"><a href="#L-915"><span class="linenos"> 915</span></a><span class="k">def</span> <span class="nf">getattr_ex</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-916"><a href="#L-916"><span class="linenos"> 916</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-917"><a href="#L-917"><span class="linenos"> 917</span></a>        <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">)</span>
</span><span id="L-918"><a href="#L-918"><span class="linenos"> 918</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>  <span class="c1"># See code of the `inspect.getmembers()`</span>
</span><span id="L-919"><a href="#L-919"><span class="linenos"> 919</span></a>        <span class="k">if</span> <span class="n">attr_name</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">:</span>
</span><span id="L-920"><a href="#L-920"><span class="linenos"> 920</span></a>            <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="n">attr_name</span><span class="p">]</span>
</span><span id="L-921"><a href="#L-921"><span class="linenos"> 921</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-922"><a href="#L-922"><span class="linenos"> 922</span></a>            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Attribute &quot;</span><span class="si">{</span><span class="n">attr_name</span><span class="si">}</span><span class="s1">&quot; was not found in the entity &quot;</span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&quot;&#39;</span><span class="p">)</span>
</span><span id="L-923"><a href="#L-923"><span class="linenos"> 923</span></a>
</span><span id="L-924"><a href="#L-924"><span class="linenos"> 924</span></a>
</span><span id="L-925"><a href="#L-925"><span class="linenos"> 925</span></a><span class="k">def</span> <span class="nf">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-926"><a href="#L-926"><span class="linenos"> 926</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-927"><a href="#L-927"><span class="linenos"> 927</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-928"><a href="#L-928"><span class="linenos"> 928</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-929"><a href="#L-929"><span class="linenos"> 929</span></a>    
</span><span id="L-930"><a href="#L-930"><span class="linenos"> 930</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="L-931"><a href="#L-931"><span class="linenos"> 931</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-932"><a href="#L-932"><span class="linenos"> 932</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-933"><a href="#L-933"><span class="linenos"> 933</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-934"><a href="#L-934"><span class="linenos"> 934</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-935"><a href="#L-935"><span class="linenos"> 935</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-936"><a href="#L-936"><span class="linenos"> 936</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-937"><a href="#L-937"><span class="linenos"> 937</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-938"><a href="#L-938"><span class="linenos"> 938</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-939"><a href="#L-939"><span class="linenos"> 939</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-940"><a href="#L-940"><span class="linenos"> 940</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-941"><a href="#L-941"><span class="linenos"> 941</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-942"><a href="#L-942"><span class="linenos"> 942</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-943"><a href="#L-943"><span class="linenos"> 943</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-944"><a href="#L-944"><span class="linenos"> 944</span></a>
</span><span id="L-945"><a href="#L-945"><span class="linenos"> 945</span></a>
</span><span id="L-946"><a href="#L-946"><span class="linenos"> 946</span></a><span class="k">def</span> <span class="nf">get_function_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-947"><a href="#L-947"><span class="linenos"> 947</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-948"><a href="#L-948"><span class="linenos"> 948</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-949"><a href="#L-949"><span class="linenos"> 949</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-950"><a href="#L-950"><span class="linenos"> 950</span></a>    
</span><span id="L-951"><a href="#L-951"><span class="linenos"> 951</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="L-952"><a href="#L-952"><span class="linenos"> 952</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-953"><a href="#L-953"><span class="linenos"> 953</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-954"><a href="#L-954"><span class="linenos"> 954</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-955"><a href="#L-955"><span class="linenos"> 955</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-956"><a href="#L-956"><span class="linenos"> 956</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-957"><a href="#L-957"><span class="linenos"> 957</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-958"><a href="#L-958"><span class="linenos"> 958</span></a>                <span class="k">return</span> <span class="n">possible_entity</span>
</span><span id="L-959"><a href="#L-959"><span class="linenos"> 959</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-960"><a href="#L-960"><span class="linenos"> 960</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-961"><a href="#L-961"><span class="linenos"> 961</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-962"><a href="#L-962"><span class="linenos"> 962</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-963"><a href="#L-963"><span class="linenos"> 963</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-964"><a href="#L-964"><span class="linenos"> 964</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-965"><a href="#L-965"><span class="linenos"> 965</span></a>
</span><span id="L-966"><a href="#L-966"><span class="linenos"> 966</span></a>
</span><span id="L-967"><a href="#L-967"><span class="linenos"> 967</span></a><span class="k">def</span> <span class="nf">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-968"><a href="#L-968"><span class="linenos"> 968</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-969"><a href="#L-969"><span class="linenos"> 969</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-970"><a href="#L-970"><span class="linenos"> 970</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-971"><a href="#L-971"><span class="linenos"> 971</span></a>    
</span><span id="L-972"><a href="#L-972"><span class="linenos"> 972</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="L-973"><a href="#L-973"><span class="linenos"> 973</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-974"><a href="#L-974"><span class="linenos"> 974</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-975"><a href="#L-975"><span class="linenos"> 975</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-976"><a href="#L-976"><span class="linenos"> 976</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-977"><a href="#L-977"><span class="linenos"> 977</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-978"><a href="#L-978"><span class="linenos"> 978</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-979"><a href="#L-979"><span class="linenos"> 979</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-980"><a href="#L-980"><span class="linenos"> 980</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-981"><a href="#L-981"><span class="linenos"> 981</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-982"><a href="#L-982"><span class="linenos"> 982</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-983"><a href="#L-983"><span class="linenos"> 983</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-984"><a href="#L-984"><span class="linenos"> 984</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-985"><a href="#L-985"><span class="linenos"> 985</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-986"><a href="#L-986"><span class="linenos"> 986</span></a>
</span><span id="L-987"><a href="#L-987"><span class="linenos"> 987</span></a>
</span><span id="L-988"><a href="#L-988"><span class="linenos"> 988</span></a><span class="k">def</span> <span class="nf">get_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-989"><a href="#L-989"><span class="linenos"> 989</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-990"><a href="#L-990"><span class="linenos"> 990</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-991"><a href="#L-991"><span class="linenos"> 991</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-992"><a href="#L-992"><span class="linenos"> 992</span></a>    
</span><span id="L-993"><a href="#L-993"><span class="linenos"> 993</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="L-994"><a href="#L-994"><span class="linenos"> 994</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-995"><a href="#L-995"><span class="linenos"> 995</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-996"><a href="#L-996"><span class="linenos"> 996</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-997"><a href="#L-997"><span class="linenos"> 997</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-998"><a href="#L-998"><span class="linenos"> 998</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-999"><a href="#L-999"><span class="linenos"> 999</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1000"><a href="#L-1000"><span class="linenos">1000</span></a>                <span class="k">return</span> <span class="n">possible_entity</span>
</span><span id="L-1001"><a href="#L-1001"><span class="linenos">1001</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1002"><a href="#L-1002"><span class="linenos">1002</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-1003"><a href="#L-1003"><span class="linenos">1003</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-1004"><a href="#L-1004"><span class="linenos">1004</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-1005"><a href="#L-1005"><span class="linenos">1005</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-1006"><a href="#L-1006"><span class="linenos">1006</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-1007"><a href="#L-1007"><span class="linenos">1007</span></a>
</span><span id="L-1008"><a href="#L-1008"><span class="linenos">1008</span></a>
</span><span id="L-1009"><a href="#L-1009"><span class="linenos">1009</span></a><span class="k">def</span> <span class="nf">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1010"><a href="#L-1010"><span class="linenos">1010</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1011"><a href="#L-1011"><span class="linenos">1011</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1012"><a href="#L-1012"><span class="linenos">1012</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-1013"><a href="#L-1013"><span class="linenos">1013</span></a>    
</span><span id="L-1014"><a href="#L-1014"><span class="linenos">1014</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="L-1015"><a href="#L-1015"><span class="linenos">1015</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1016"><a href="#L-1016"><span class="linenos">1016</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1017"><a href="#L-1017"><span class="linenos">1017</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1018"><a href="#L-1018"><span class="linenos">1018</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1019"><a href="#L-1019"><span class="linenos">1019</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1020"><a href="#L-1020"><span class="linenos">1020</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1021"><a href="#L-1021"><span class="linenos">1021</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-1022"><a href="#L-1022"><span class="linenos">1022</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1023"><a href="#L-1023"><span class="linenos">1023</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-1024"><a href="#L-1024"><span class="linenos">1024</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-1025"><a href="#L-1025"><span class="linenos">1025</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-1026"><a href="#L-1026"><span class="linenos">1026</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-1027"><a href="#L-1027"><span class="linenos">1027</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-1028"><a href="#L-1028"><span class="linenos">1028</span></a>
</span><span id="L-1029"><a href="#L-1029"><span class="linenos">1029</span></a>
</span><span id="L-1030"><a href="#L-1030"><span class="linenos">1030</span></a><span class="k">def</span> <span class="nf">get_unbound_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="L-1031"><a href="#L-1031"><span class="linenos">1031</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-1032"><a href="#L-1032"><span class="linenos">1032</span></a>
</span><span id="L-1033"><a href="#L-1033"><span class="linenos">1033</span></a>
</span><span id="L-1034"><a href="#L-1034"><span class="linenos">1034</span></a><span class="k">class</span> <span class="nc">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-1035"><a href="#L-1035"><span class="linenos">1035</span></a>    <span class="k">pass</span>
</span><span id="L-1036"><a href="#L-1036"><span class="linenos">1036</span></a>
</span><span id="L-1037"><a href="#L-1037"><span class="linenos">1037</span></a>
</span><span id="L-1038"><a href="#L-1038"><span class="linenos">1038</span></a><span class="k">class</span> <span class="nc">PossibleOwnerParameterDoesNotMatchError</span><span class="p">(</span><span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">):</span>
</span><span id="L-1039"><a href="#L-1039"><span class="linenos">1039</span></a>    <span class="k">pass</span>
</span><span id="L-1040"><a href="#L-1040"><span class="linenos">1040</span></a>
</span><span id="L-1041"><a href="#L-1041"><span class="linenos">1041</span></a>
</span><span id="L-1042"><a href="#L-1042"><span class="linenos">1042</span></a><span class="k">class</span> <span class="nc">EntityHasNoPositionalParametersError</span><span class="p">(</span><span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">):</span>
</span><span id="L-1043"><a href="#L-1043"><span class="linenos">1043</span></a>    <span class="k">pass</span>
</span><span id="L-1044"><a href="#L-1044"><span class="linenos">1044</span></a>
</span><span id="L-1045"><a href="#L-1045"><span class="linenos">1045</span></a>
</span><span id="L-1046"><a href="#L-1046"><span class="linenos">1046</span></a><span class="k">def</span> <span class="nf">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">return_even_if_not_match</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="L-1047"><a href="#L-1047"><span class="linenos">1047</span></a>    <span class="k">if</span> <span class="n">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1048"><a href="#L-1048"><span class="linenos">1048</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Function has no </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter&#39;</span><span class="p">)</span>
</span><span id="L-1049"><a href="#L-1049"><span class="linenos">1049</span></a>    
</span><span id="L-1050"><a href="#L-1050"><span class="linenos">1050</span></a>    <span class="k">if</span> <span class="n">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1051"><a href="#L-1051"><span class="linenos">1051</span></a>        <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__self__</span>
</span><span id="L-1052"><a href="#L-1052"><span class="linenos">1052</span></a>    <span class="k">elif</span> <span class="n">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1053"><a href="#L-1053"><span class="linenos">1053</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-1054"><a href="#L-1054"><span class="linenos">1054</span></a>            <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1055"><a href="#L-1055"><span class="linenos">1055</span></a>            <span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1056"><a href="#L-1056"><span class="linenos">1056</span></a>            <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">params_with_values</span>
</span><span id="L-1057"><a href="#L-1057"><span class="linenos">1057</span></a>            <span class="k">if</span> <span class="n">positional</span><span class="p">:</span>
</span><span id="L-1058"><a href="#L-1058"><span class="linenos">1058</span></a>                <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-1059"><a href="#L-1059"><span class="linenos">1059</span></a>            <span class="k">elif</span> <span class="n">positional_only</span><span class="p">:</span>
</span><span id="L-1060"><a href="#L-1060"><span class="linenos">1060</span></a>                <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional_only</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-1061"><a href="#L-1061"><span class="linenos">1061</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1062"><a href="#L-1062"><span class="linenos">1062</span></a>                <span class="k">raise</span> <span class="n">EntityHasNoPositionalParametersError</span>
</span><span id="L-1063"><a href="#L-1063"><span class="linenos">1063</span></a>            
</span><span id="L-1064"><a href="#L-1064"><span class="linenos">1064</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1065"><a href="#L-1065"><span class="linenos">1065</span></a>                <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1066"><a href="#L-1066"><span class="linenos">1066</span></a>                <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1067"><a href="#L-1067"><span class="linenos">1067</span></a>                <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1068"><a href="#L-1068"><span class="linenos">1068</span></a>                <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1069"><a href="#L-1069"><span class="linenos">1069</span></a>                    <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="L-1070"><a href="#L-1070"><span class="linenos">1070</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="L-1071"><a href="#L-1071"><span class="linenos">1071</span></a>                    <span class="k">if</span> <span class="n">return_even_if_not_match</span><span class="p">:</span>
</span><span id="L-1072"><a href="#L-1072"><span class="linenos">1072</span></a>                        <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="L-1073"><a href="#L-1073"><span class="linenos">1073</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="L-1074"><a href="#L-1074"><span class="linenos">1074</span></a>                        <span class="k">raise</span> <span class="n">PossibleOwnerParameterDoesNotMatchError</span>
</span><span id="L-1075"><a href="#L-1075"><span class="linenos">1075</span></a>            
</span><span id="L-1076"><a href="#L-1076"><span class="linenos">1076</span></a>            <span class="k">raise</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Can not find an appropriate </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter in </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-1077"><a href="#L-1077"><span class="linenos">1077</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="L-1078"><a href="#L-1078"><span class="linenos">1078</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1"> of type </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="si">}</span><span class="s1"> is not supported&#39;</span><span class="p">)</span>
</span><span id="L-1079"><a href="#L-1079"><span class="linenos">1079</span></a>
</span><span id="L-1080"><a href="#L-1080"><span class="linenos">1080</span></a>
</span><span id="L-1081"><a href="#L-1081"><span class="linenos">1081</span></a><span class="k">def</span> <span class="nf">get_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1082"><a href="#L-1082"><span class="linenos">1082</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;self&#39;</span><span class="p">)</span>
</span><span id="L-1083"><a href="#L-1083"><span class="linenos">1083</span></a>
</span><span id="L-1084"><a href="#L-1084"><span class="linenos">1084</span></a>
</span><span id="L-1085"><a href="#L-1085"><span class="linenos">1085</span></a><span class="k">def</span> <span class="nf">get_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1086"><a href="#L-1086"><span class="linenos">1086</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">)</span>
</span><span id="L-1087"><a href="#L-1087"><span class="linenos">1087</span></a>
</span><span id="L-1088"><a href="#L-1088"><span class="linenos">1088</span></a>
</span><span id="L-1089"><a href="#L-1089"><span class="linenos">1089</span></a><span class="k">def</span> <span class="nf">get_any_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-1090"><a href="#L-1090"><span class="linenos">1090</span></a>    <span class="k">if</span> <span class="n">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1091"><a href="#L-1091"><span class="linenos">1091</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Function has no </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter&#39;</span><span class="p">)</span>
</span><span id="L-1092"><a href="#L-1092"><span class="linenos">1092</span></a>    
</span><span id="L-1093"><a href="#L-1093"><span class="linenos">1093</span></a>    <span class="k">if</span> <span class="n">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1094"><a href="#L-1094"><span class="linenos">1094</span></a>        <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__self__</span>
</span><span id="L-1095"><a href="#L-1095"><span class="linenos">1095</span></a>    <span class="k">elif</span> <span class="n">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1096"><a href="#L-1096"><span class="linenos">1096</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-1097"><a href="#L-1097"><span class="linenos">1097</span></a>            <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1098"><a href="#L-1098"><span class="linenos">1098</span></a>            <span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1099"><a href="#L-1099"><span class="linenos">1099</span></a>            <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">params_with_values</span>
</span><span id="L-1100"><a href="#L-1100"><span class="linenos">1100</span></a>            
</span><span id="L-1101"><a href="#L-1101"><span class="linenos">1101</span></a>            <span class="k">if</span> <span class="n">any_positional</span><span class="p">:</span>
</span><span id="L-1102"><a href="#L-1102"><span class="linenos">1102</span></a>                <span class="n">all_positional</span> <span class="o">=</span> <span class="n">positional</span> <span class="o">+</span> <span class="n">positional_only</span>
</span><span id="L-1103"><a href="#L-1103"><span class="linenos">1103</span></a>                <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">all_positional</span><span class="p">:</span>
</span><span id="L-1104"><a href="#L-1104"><span class="linenos">1104</span></a>                    <span class="n">possible_positional_self_name</span><span class="p">,</span> <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">param</span>
</span><span id="L-1105"><a href="#L-1105"><span class="linenos">1105</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1106"><a href="#L-1106"><span class="linenos">1106</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1107"><a href="#L-1107"><span class="linenos">1107</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1108"><a href="#L-1108"><span class="linenos">1108</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1109"><a href="#L-1109"><span class="linenos">1109</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1110"><a href="#L-1110"><span class="linenos">1110</span></a>                            <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="L-1111"><a href="#L-1111"><span class="linenos">1111</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1112"><a href="#L-1112"><span class="linenos">1112</span></a>                <span class="k">if</span> <span class="n">positional</span><span class="p">:</span>
</span><span id="L-1113"><a href="#L-1113"><span class="linenos">1113</span></a>                    <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-1114"><a href="#L-1114"><span class="linenos">1114</span></a>                <span class="k">elif</span> <span class="n">positional_only</span><span class="p">:</span>
</span><span id="L-1115"><a href="#L-1115"><span class="linenos">1115</span></a>                    <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional_only</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="L-1116"><a href="#L-1116"><span class="linenos">1116</span></a>                
</span><span id="L-1117"><a href="#L-1117"><span class="linenos">1117</span></a>                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1118"><a href="#L-1118"><span class="linenos">1118</span></a>                    <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1119"><a href="#L-1119"><span class="linenos">1119</span></a>                    <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1120"><a href="#L-1120"><span class="linenos">1120</span></a>                    <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1121"><a href="#L-1121"><span class="linenos">1121</span></a>                    <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1122"><a href="#L-1122"><span class="linenos">1122</span></a>                        <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="L-1123"><a href="#L-1123"><span class="linenos">1123</span></a>            
</span><span id="L-1124"><a href="#L-1124"><span class="linenos">1124</span></a>            <span class="k">if</span> <span class="n">any_keyword</span><span class="p">:</span>
</span><span id="L-1125"><a href="#L-1125"><span class="linenos">1125</span></a>                <span class="k">for</span> <span class="n">possible_keyword_self_name</span><span class="p">,</span> <span class="n">possible_keyword_self</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="L-1126"><a href="#L-1126"><span class="linenos">1126</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1127"><a href="#L-1127"><span class="linenos">1127</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1128"><a href="#L-1128"><span class="linenos">1128</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1129"><a href="#L-1129"><span class="linenos">1129</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1130"><a href="#L-1130"><span class="linenos">1130</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1131"><a href="#L-1131"><span class="linenos">1131</span></a>                            <span class="k">return</span> <span class="n">possible_keyword_self</span>
</span><span id="L-1132"><a href="#L-1132"><span class="linenos">1132</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1133"><a href="#L-1133"><span class="linenos">1133</span></a>                <span class="n">keyword_only_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="L-1134"><a href="#L-1134"><span class="linenos">1134</span></a>                <span class="k">if</span> <span class="n">owner_parameter_name</span> <span class="ow">in</span> <span class="n">keyword_only_dict</span><span class="p">:</span>
</span><span id="L-1135"><a href="#L-1135"><span class="linenos">1135</span></a>                    <span class="n">possible_keyword_self</span> <span class="o">=</span> <span class="n">keyword_only_dict</span><span class="p">[</span><span class="n">owner_parameter_name</span><span class="p">]</span>
</span><span id="L-1136"><a href="#L-1136"><span class="linenos">1136</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="L-1137"><a href="#L-1137"><span class="linenos">1137</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1138"><a href="#L-1138"><span class="linenos">1138</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="L-1139"><a href="#L-1139"><span class="linenos">1139</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1140"><a href="#L-1140"><span class="linenos">1140</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1141"><a href="#L-1141"><span class="linenos">1141</span></a>                            <span class="k">return</span> <span class="n">possible_keyword_self</span>
</span><span id="L-1142"><a href="#L-1142"><span class="linenos">1142</span></a>            
</span><span id="L-1143"><a href="#L-1143"><span class="linenos">1143</span></a>            <span class="k">raise</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Can not find </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter in </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-1144"><a href="#L-1144"><span class="linenos">1144</span></a>
</span><span id="L-1145"><a href="#L-1145"><span class="linenos">1145</span></a>
</span><span id="L-1146"><a href="#L-1146"><span class="linenos">1146</span></a><span class="k">def</span> <span class="nf">get_any_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-1147"><a href="#L-1147"><span class="linenos">1147</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;self&#39;</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">)</span>
</span><span id="L-1148"><a href="#L-1148"><span class="linenos">1148</span></a>
</span><span id="L-1149"><a href="#L-1149"><span class="linenos">1149</span></a>
</span><span id="L-1150"><a href="#L-1150"><span class="linenos">1150</span></a><span class="k">def</span> <span class="nf">get_any_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="L-1151"><a href="#L-1151"><span class="linenos">1151</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span> <span class="p">,</span> <span class="n">any_positional</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">)</span>
</span><span id="L-1152"><a href="#L-1152"><span class="linenos">1152</span></a>
</span><span id="L-1153"><a href="#L-1153"><span class="linenos">1153</span></a>
</span><span id="L-1154"><a href="#L-1154"><span class="linenos">1154</span></a><span class="k">def</span> <span class="nf">find_method_in_module_by_code</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeType</span><span class="p">]:</span>
</span><span id="L-1155"><a href="#L-1155"><span class="linenos">1155</span></a>    <span class="k">for</span> <span class="n">entity_name_str</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">module</span><span class="p">):</span>
</span><span id="L-1156"><a href="#L-1156"><span class="linenos">1156</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1157"><a href="#L-1157"><span class="linenos">1157</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1158"><a href="#L-1158"><span class="linenos">1158</span></a>            <span class="n">possible_method</span> <span class="o">=</span> <span class="n">find_method_in_class_by_code</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">)</span>
</span><span id="L-1159"><a href="#L-1159"><span class="linenos">1159</span></a>            <span class="k">if</span> <span class="n">possible_method</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1160"><a href="#L-1160"><span class="linenos">1160</span></a>                <span class="k">return</span> <span class="n">possible_method</span>
</span><span id="L-1161"><a href="#L-1161"><span class="linenos">1161</span></a>    
</span><span id="L-1162"><a href="#L-1162"><span class="linenos">1162</span></a>    <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-1163"><a href="#L-1163"><span class="linenos">1163</span></a>
</span><span id="L-1164"><a href="#L-1164"><span class="linenos">1164</span></a>
</span><span id="L-1165"><a href="#L-1165"><span class="linenos">1165</span></a><span class="k">def</span> <span class="nf">find_method_in_class_by_code</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeType</span><span class="p">]:</span>
</span><span id="L-1166"><a href="#L-1166"><span class="linenos">1166</span></a>    <span class="n">subclassess</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-1167"><a href="#L-1167"><span class="linenos">1167</span></a>    <span class="k">for</span> <span class="n">entity_name_str</span> <span class="ow">in</span> <span class="n">class_properties_including_overrided</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">):</span>
</span><span id="L-1168"><a href="#L-1168"><span class="linenos">1168</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1169"><a href="#L-1169"><span class="linenos">1169</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1170"><a href="#L-1170"><span class="linenos">1170</span></a>            <span class="n">subclassess</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1171"><a href="#L-1171"><span class="linenos">1171</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="L-1172"><a href="#L-1172"><span class="linenos">1172</span></a>            <span class="k">if</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">is</span> <span class="n">code_to_find</span><span class="p">:</span>
</span><span id="L-1173"><a href="#L-1173"><span class="linenos">1173</span></a>                <span class="k">return</span> <span class="n">entity</span>
</span><span id="L-1174"><a href="#L-1174"><span class="linenos">1174</span></a>        
</span><span id="L-1175"><a href="#L-1175"><span class="linenos">1175</span></a>    <span class="k">for</span> <span class="n">subclass</span> <span class="ow">in</span> <span class="n">subclassess</span><span class="p">:</span>
</span><span id="L-1176"><a href="#L-1176"><span class="linenos">1176</span></a>        <span class="n">possible_method</span> <span class="o">=</span> <span class="n">find_method_in_class_by_code</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">)</span>
</span><span id="L-1177"><a href="#L-1177"><span class="linenos">1177</span></a>        <span class="k">if</span> <span class="n">possible_method</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1178"><a href="#L-1178"><span class="linenos">1178</span></a>            <span class="k">return</span> <span class="n">possible_method</span>
</span><span id="L-1179"><a href="#L-1179"><span class="linenos">1179</span></a>    
</span><span id="L-1180"><a href="#L-1180"><span class="linenos">1180</span></a>    <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-1181"><a href="#L-1181"><span class="linenos">1181</span></a>
</span><span id="L-1182"><a href="#L-1182"><span class="linenos">1182</span></a>
</span><span id="L-1183"><a href="#L-1183"><span class="linenos">1183</span></a><span class="k">class</span> <span class="nc">EntityWasNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-1184"><a href="#L-1184"><span class="linenos">1184</span></a>    <span class="k">pass</span>
</span><span id="L-1185"><a href="#L-1185"><span class="linenos">1185</span></a>
</span><span id="L-1186"><a href="#L-1186"><span class="linenos">1186</span></a>
</span><span id="L-1187"><a href="#L-1187"><span class="linenos">1187</span></a><span class="k">def</span> <span class="nf">find_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-1188"><a href="#L-1188"><span class="linenos">1188</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">)):</span>
</span><span id="L-1189"><a href="#L-1189"><span class="linenos">1189</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Only functions, methods, frames and codes are supported. </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="si">}</span><span class="s1"> was provided instead&#39;</span><span class="p">)</span>
</span><span id="L-1190"><a href="#L-1190"><span class="linenos">1190</span></a>    
</span><span id="L-1191"><a href="#L-1191"><span class="linenos">1191</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_function_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1192"><a href="#L-1192"><span class="linenos">1192</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1193"><a href="#L-1193"><span class="linenos">1193</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-1194"><a href="#L-1194"><span class="linenos">1194</span></a>    
</span><span id="L-1195"><a href="#L-1195"><span class="linenos">1195</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1196"><a href="#L-1196"><span class="linenos">1196</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1197"><a href="#L-1197"><span class="linenos">1197</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-1198"><a href="#L-1198"><span class="linenos">1198</span></a>    
</span><span id="L-1199"><a href="#L-1199"><span class="linenos">1199</span></a>    <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1200"><a href="#L-1200"><span class="linenos">1200</span></a>    <span class="n">entity_instance</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-1201"><a href="#L-1201"><span class="linenos">1201</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="L-1202"><a href="#L-1202"><span class="linenos">1202</span></a>        <span class="n">owner</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-1203"><a href="#L-1203"><span class="linenos">1203</span></a>        <span class="n">need_to_try_clr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-1204"><a href="#L-1204"><span class="linenos">1204</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-1205"><a href="#L-1205"><span class="linenos">1205</span></a>            <span class="n">owner</span> <span class="o">=</span> <span class="n">get_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1206"><a href="#L-1206"><span class="linenos">1206</span></a>        <span class="k">except</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">:</span>
</span><span id="L-1207"><a href="#L-1207"><span class="linenos">1207</span></a>            <span class="n">need_to_try_clr</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-1208"><a href="#L-1208"><span class="linenos">1208</span></a>        
</span><span id="L-1209"><a href="#L-1209"><span class="linenos">1209</span></a>        <span class="k">if</span> <span class="n">need_to_try_clr</span><span class="p">:</span>
</span><span id="L-1210"><a href="#L-1210"><span class="linenos">1210</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-1211"><a href="#L-1211"><span class="linenos">1211</span></a>                <span class="n">owner</span> <span class="o">=</span> <span class="n">get_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1212"><a href="#L-1212"><span class="linenos">1212</span></a>            <span class="k">except</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">:</span>
</span><span id="L-1213"><a href="#L-1213"><span class="linenos">1213</span></a>                <span class="k">pass</span>
</span><span id="L-1214"><a href="#L-1214"><span class="linenos">1214</span></a>        
</span><span id="L-1215"><a href="#L-1215"><span class="linenos">1215</span></a>        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="L-1216"><a href="#L-1216"><span class="linenos">1216</span></a>        <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1217"><a href="#L-1217"><span class="linenos">1217</span></a>            <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="L-1218"><a href="#L-1218"><span class="linenos">1218</span></a>            <span class="k">if</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="L-1219"><a href="#L-1219"><span class="linenos">1219</span></a>                <span class="k">return</span> <span class="n">entity_instance</span>
</span><span id="L-1220"><a href="#L-1220"><span class="linenos">1220</span></a>        
</span><span id="L-1221"><a href="#L-1221"><span class="linenos">1221</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity_code</span>
</span><span id="L-1222"><a href="#L-1222"><span class="linenos">1222</span></a>    
</span><span id="L-1223"><a href="#L-1223"><span class="linenos">1223</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="L-1224"><a href="#L-1224"><span class="linenos">1224</span></a>        <span class="n">entity_owner_instance</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="L-1225"><a href="#L-1225"><span class="linenos">1225</span></a>        <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">find_method_in_module_by_code</span><span class="p">(</span><span class="n">entity_owner_instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
</span><span id="L-1226"><a href="#L-1226"><span class="linenos">1226</span></a>        <span class="k">if</span> <span class="n">entity_instance</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1227"><a href="#L-1227"><span class="linenos">1227</span></a>            <span class="k">return</span> <span class="n">entity_instance</span>
</span><span id="L-1228"><a href="#L-1228"><span class="linenos">1228</span></a>    
</span><span id="L-1229"><a href="#L-1229"><span class="linenos">1229</span></a>    <span class="k">raise</span> <span class="n">EntityWasNotFoundError</span>
</span><span id="L-1230"><a href="#L-1230"><span class="linenos">1230</span></a>
</span><span id="L-1231"><a href="#L-1231"><span class="linenos">1231</span></a>
</span><span id="L-1232"><a href="#L-1232"><span class="linenos">1232</span></a><span class="k">def</span> <span class="nf">find_current_entity</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-1233"><a href="#L-1233"><span class="linenos">1233</span></a>    <span class="k">return</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


            </section>
                <section id="WrongDepth">
                            <input id="WrongDepth-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WrongDepth</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="WrongDepth-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WrongDepth"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WrongDepth-50"><a href="#WrongDepth-50"><span class="linenos">50</span></a><span class="k">class</span> <span class="nc">WrongDepth</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="WrongDepth-51"><a href="#WrongDepth-51"><span class="linenos">51</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="WrongDepth.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="WrongDepth.with_traceback" class="function">with_traceback</dd>
                <dd id="WrongDepth.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CanNotRetrieveFrame">
                            <input id="CanNotRetrieveFrame-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CanNotRetrieveFrame</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="CanNotRetrieveFrame-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CanNotRetrieveFrame"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CanNotRetrieveFrame-54"><a href="#CanNotRetrieveFrame-54"><span class="linenos">54</span></a><span class="k">class</span> <span class="nc">CanNotRetrieveFrame</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="CanNotRetrieveFrame-55"><a href="#CanNotRetrieveFrame-55"><span class="linenos">55</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="CanNotRetrieveFrame.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="CanNotRetrieveFrame.with_traceback" class="function">with_traceback</dd>
                <dd id="CanNotRetrieveFrame.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="frame">
                            <input id="frame-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">frame</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">frame</span>:</span></span>

                <label class="view-source-button" for="frame-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#frame"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="frame-58"><a href="#frame-58"><span class="linenos">58</span></a><span class="k">def</span> <span class="nf">frame</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">FrameType</span><span class="p">:</span>
</span><span id="frame-59"><a href="#frame-59"><span class="linenos">59</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="frame-60"><a href="#frame-60"><span class="linenos">60</span></a><span class="sd">    :param depth: 0 - frame of this function, 1 - frame of the caller function, etc.</span>
</span><span id="frame-61"><a href="#frame-61"><span class="linenos">61</span></a><span class="sd">    :return:</span>
</span><span id="frame-62"><a href="#frame-62"><span class="linenos">62</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="frame-63"><a href="#frame-63"><span class="linenos">63</span></a>    <span class="n">depth</span> <span class="o">=</span> <span class="n">depth</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="frame-64"><a href="#frame-64"><span class="linenos">64</span></a>    <span class="k">if</span> <span class="n">depth</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="frame-65"><a href="#frame-65"><span class="linenos">65</span></a>        <span class="k">raise</span> <span class="n">WrongDepth</span><span class="p">(</span><span class="n">depth</span><span class="p">)</span>
</span><span id="frame-66"><a href="#frame-66"><span class="linenos">66</span></a>
</span><span id="frame-67"><a href="#frame-67"><span class="linenos">67</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">currentframe</span><span class="p">()</span>
</span><span id="frame-68"><a href="#frame-68"><span class="linenos">68</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="frame-69"><a href="#frame-69"><span class="linenos">69</span></a>        <span class="k">raise</span> <span class="n">CanNotRetrieveFrame</span><span class="p">()</span>
</span><span id="frame-70"><a href="#frame-70"><span class="linenos">70</span></a>
</span><span id="frame-71"><a href="#frame-71"><span class="linenos">71</span></a>    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">depth</span><span class="p">):</span>
</span><span id="frame-72"><a href="#frame-72"><span class="linenos">72</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="n">result</span><span class="o">.</span><span class="n">f_back</span>
</span><span id="frame-73"><a href="#frame-73"><span class="linenos">73</span></a>
</span><span id="frame-74"><a href="#frame-74"><span class="linenos">74</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>:param depth: 0 - frame of this function, 1 - frame of the caller function, etc.
:return:</p>
</div>


                </section>
                <section id="get_exception">
                            <input id="get_exception-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_exception</span><span class="signature pdoc-code condensed">(<span class="return-annotation">) -> <span class="ne">Exception</span>:</span></span>

                <label class="view-source-button" for="get_exception-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_exception"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_exception-77"><a href="#get_exception-77"><span class="linenos">77</span></a><span class="k">def</span> <span class="nf">get_exception</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="ne">Exception</span><span class="p">:</span>
</span><span id="get_exception-78"><a href="#get_exception-78"><span class="linenos">78</span></a>    <span class="n">ex_type</span><span class="p">,</span> <span class="n">ex_value</span><span class="p">,</span> <span class="n">ex_traceback</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span><span id="get_exception-79"><a href="#get_exception-79"><span class="linenos">79</span></a>    <span class="k">return</span> <span class="n">ex_value</span><span class="o">.</span><span class="n">with_traceback</span><span class="p">(</span><span class="n">ex_traceback</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_exception_tripple">
                            <input id="get_exception_tripple-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_exception_tripple</span><span class="signature pdoc-code condensed">(<span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_exception_tripple-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_exception_tripple"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_exception_tripple-82"><a href="#get_exception_tripple-82"><span class="linenos">82</span></a><span class="k">def</span> <span class="nf">get_exception_tripple</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="ne">Exception</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="get_exception_tripple-83"><a href="#get_exception_tripple-83"><span class="linenos">83</span></a>    <span class="k">return</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="exception_to_printable_text">
                            <input id="exception_to_printable_text-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">exception_to_printable_text</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">exception</span><span class="p">:</span> <span class="ne">Exception</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="exception_to_printable_text-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#exception_to_printable_text"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="exception_to_printable_text-86"><a href="#exception_to_printable_text-86"><span class="linenos">86</span></a><span class="k">def</span> <span class="nf">exception_to_printable_text</span><span class="p">(</span><span class="n">exception</span><span class="p">:</span> <span class="ne">Exception</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="exception_to_printable_text-87"><a href="#exception_to_printable_text-87"><span class="linenos">87</span></a>    <span class="c1"># return &#39;&#39;.join(traceback.format_exception(type(exception), exception, exception.__traceback__))</span>
</span><span id="exception_to_printable_text-88"><a href="#exception_to_printable_text-88"><span class="linenos">88</span></a>    <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">traceback</span><span class="o">.</span><span class="n">TracebackException</span><span class="o">.</span><span class="n">from_exception</span><span class="p">(</span><span class="n">exception</span><span class="p">)</span><span class="o">.</span><span class="n">format</span><span class="p">())</span>
</span></pre></div>


    

                </section>
                <section id="is_async">
                            <input id="is_async-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_async</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="is_async-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_async"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_async-91"><a href="#is_async-91"><span class="linenos">91</span></a><span class="k">def</span> <span class="nf">is_async</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="is_async-92"><a href="#is_async-92"><span class="linenos">92</span></a>    <span class="k">return</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isgenerator</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">iscoroutinefunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isgeneratorfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isasyncgen</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isasyncgenfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isawaitable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="is_callable">
                            <input id="is_callable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_callable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="is_callable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_callable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_callable-95"><a href="#is_callable-95"><span class="linenos">95</span></a><span class="k">def</span> <span class="nf">is_callable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="is_callable-96"><a href="#is_callable-96"><span class="linenos">96</span></a>    <span class="k">return</span> <span class="nb">callable</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="func_param_names">
                            <input id="func_param_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_param_names</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">func</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>:</span></span>

                <label class="view-source-button" for="func_param_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_param_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_param_names-99"><a href="#func_param_names-99"><span class="linenos"> 99</span></a><span class="k">def</span> <span class="nf">func_param_names</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="func_param_names-100"><a href="#func_param_names-100"><span class="linenos">100</span></a>    <span class="k">return</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">get_code</span><span class="p">(</span><span class="n">func</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="entity_arguments_description">
                            <input id="entity_arguments_description-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_arguments_description</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="entity_arguments_description-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_arguments_description"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_arguments_description-103"><a href="#entity_arguments_description-103"><span class="linenos">103</span></a><span class="k">def</span> <span class="nf">entity_arguments_description</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">Sequence</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="entity_arguments_description-104"><a href="#entity_arguments_description-104"><span class="linenos">104</span></a>    <span class="n">init_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_arguments_description-105"><a href="#entity_arguments_description-105"><span class="linenos">105</span></a>    <span class="n">cpn</span><span class="p">:</span> <span class="n">CodeParamNames</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">init_code</span><span class="p">)</span>
</span><span id="entity_arguments_description-106"><a href="#entity_arguments_description-106"><span class="linenos">106</span></a>    <span class="n">positional</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">positional</span>
</span><span id="entity_arguments_description-107"><a href="#entity_arguments_description-107"><span class="linenos">107</span></a>    <span class="n">positional_only</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">positional_only</span>
</span><span id="entity_arguments_description-108"><a href="#entity_arguments_description-108"><span class="linenos">108</span></a>    <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">cpn</span><span class="o">.</span><span class="n">keyword_only</span>
</span><span id="entity_arguments_description-109"><a href="#entity_arguments_description-109"><span class="linenos">109</span></a>    <span class="nb">all</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="entity_arguments_description-110"><a href="#entity_arguments_description-110"><span class="linenos">110</span></a>    <span class="k">return</span> <span class="nb">all</span><span class="p">,</span> <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span>
</span></pre></div>


    

                </section>
                <section id="func_code_name">
                            <input id="func_code_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_code_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="func_code_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_code_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_code_name-113"><a href="#func_code_name-113"><span class="linenos">113</span></a><span class="k">def</span> <span class="nf">func_code_name</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="func_code_name-114"><a href="#func_code_name-114"><span class="linenos">114</span></a>    <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="func_code_name-115"><a href="#func_code_name-115"><span class="linenos">115</span></a>    <span class="k">return</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="func_name">
                            <input id="func_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="func_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_name-118"><a href="#func_name-118"><span class="linenos">118</span></a><span class="k">def</span> <span class="nf">func_name</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="func_name-119"><a href="#func_name-119"><span class="linenos">119</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="func_name-120"><a href="#func_name-120"><span class="linenos">120</span></a>        <span class="k">return</span> <span class="n">func</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="func_name-121"><a href="#func_name-121"><span class="linenos">121</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="func_name-122"><a href="#func_name-122"><span class="linenos">122</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="func_qualname">
                            <input id="func_qualname-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_qualname</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="func_qualname-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_qualname"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_qualname-125"><a href="#func_qualname-125"><span class="linenos">125</span></a><span class="k">def</span> <span class="nf">func_qualname</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="func_qualname-126"><a href="#func_qualname-126"><span class="linenos">126</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="func_qualname-127"><a href="#func_qualname-127"><span class="linenos">127</span></a>        <span class="k">return</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span>
</span><span id="func_qualname-128"><a href="#func_qualname-128"><span class="linenos">128</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="func_qualname-129"><a href="#func_qualname-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="entity_name">
                            <input id="entity_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_name-132"><a href="#entity_name-132"><span class="linenos">132</span></a><span class="k">def</span> <span class="nf">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_name-133"><a href="#entity_name-133"><span class="linenos">133</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_name-134"><a href="#entity_name-134"><span class="linenos">134</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_name-135"><a href="#entity_name-135"><span class="linenos">135</span></a>    
</span><span id="entity_name-136"><a href="#entity_name-136"><span class="linenos">136</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_name-137"><a href="#entity_name-137"><span class="linenos">137</span></a>        <span class="k">return</span> <span class="n">code_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_name-138"><a href="#entity_name-138"><span class="linenos">138</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_name-139"><a href="#entity_name-139"><span class="linenos">139</span></a>        <span class="k">return</span> <span class="n">func_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_qualname">
                            <input id="entity_qualname-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_qualname</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_qualname-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_qualname"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_qualname-142"><a href="#entity_qualname-142"><span class="linenos">142</span></a><span class="k">def</span> <span class="nf">entity_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_qualname-143"><a href="#entity_qualname-143"><span class="linenos">143</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_qualname-144"><a href="#entity_qualname-144"><span class="linenos">144</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_qualname-145"><a href="#entity_qualname-145"><span class="linenos">145</span></a>    
</span><span id="entity_qualname-146"><a href="#entity_qualname-146"><span class="linenos">146</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_qualname-147"><a href="#entity_qualname-147"><span class="linenos">147</span></a>        <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">version_info</span> <span class="o">&gt;=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">11</span><span class="p">):</span>
</span><span id="entity_qualname-148"><a href="#entity_qualname-148"><span class="linenos">148</span></a>            <span class="k">return</span> <span class="n">code_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_qualname-149"><a href="#entity_qualname-149"><span class="linenos">149</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_qualname-150"><a href="#entity_qualname-150"><span class="linenos">150</span></a>            <span class="c1"># raise RuntimeError(&#39;CodeType.__qualname__ is available only since Python 3.11&#39;)</span>
</span><span id="entity_qualname-151"><a href="#entity_qualname-151"><span class="linenos">151</span></a>            <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_qualname-152"><a href="#entity_qualname-152"><span class="linenos">152</span></a>            <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity_owner_name</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">entity_name</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="entity_qualname-153"><a href="#entity_qualname-153"><span class="linenos">153</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_qualname-154"><a href="#entity_qualname-154"><span class="linenos">154</span></a>        <span class="k">return</span> <span class="n">func_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_class">
                            <input id="entity_class-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_class</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="entity_class-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_class"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_class-157"><a href="#entity_class-157"><span class="linenos">157</span></a><span class="k">def</span> <span class="nf">entity_class</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">]:</span>
</span><span id="entity_class-158"><a href="#entity_class-158"><span class="linenos">158</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="entity_class-159"><a href="#entity_class-159"><span class="linenos">159</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="entity_class-160"><a href="#entity_class-160"><span class="linenos">160</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func</span><span class="p">:</span>
</span><span id="entity_class-161"><a href="#entity_class-161"><span class="linenos">161</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_class-162"><a href="#entity_class-162"><span class="linenos">162</span></a>        
</span><span id="entity_class-163"><a href="#entity_class-163"><span class="linenos">163</span></a>        <span class="n">func_of_the_bound_method</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="entity_class-164"><a href="#entity_class-164"><span class="linenos">164</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="entity_class-165"><a href="#entity_class-165"><span class="linenos">165</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func_of_the_bound_method</span><span class="p">:</span>
</span><span id="entity_class-166"><a href="#entity_class-166"><span class="linenos">166</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_class-167"><a href="#entity_class-167"><span class="linenos">167</span></a>        
</span><span id="entity_class-168"><a href="#entity_class-168"><span class="linenos">168</span></a>        <span class="n">func</span> <span class="o">=</span> <span class="n">func_of_the_bound_method</span>
</span><span id="entity_class-169"><a href="#entity_class-169"><span class="linenos">169</span></a>    
</span><span id="entity_class-170"><a href="#entity_class-170"><span class="linenos">170</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="entity_class-171"><a href="#entity_class-171"><span class="linenos">171</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="entity_class-172"><a href="#entity_class-172"><span class="linenos">172</span></a>            <span class="n">func_class</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">),</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&lt;locals&gt;&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="entity_class-173"><a href="#entity_class-173"><span class="linenos">173</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="entity_class-174"><a href="#entity_class-174"><span class="linenos">174</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="entity_class-175"><a href="#entity_class-175"><span class="linenos">175</span></a>        
</span><span id="entity_class-176"><a href="#entity_class-176"><span class="linenos">176</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">func_class</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="entity_class-177"><a href="#entity_class-177"><span class="linenos">177</span></a>            <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_class-178"><a href="#entity_class-178"><span class="linenos">178</span></a>    
</span><span id="entity_class-179"><a href="#entity_class-179"><span class="linenos">179</span></a>    <span class="k">return</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="s1">&#39;__objclass__&#39;</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_owner">
                            <input id="entity_owner-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_owner</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="entity_owner-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_owner"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_owner-182"><a href="#entity_owner-182"><span class="linenos">182</span></a><span class="k">def</span> <span class="nf">entity_owner</span><span class="p">(</span><span class="n">func</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]:</span>
</span><span id="entity_owner-183"><a href="#entity_owner-183"><span class="linenos">183</span></a>    <span class="n">func_module</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="entity_owner-184"><a href="#entity_owner-184"><span class="linenos">184</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="entity_owner-185"><a href="#entity_owner-185"><span class="linenos">185</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="entity_owner-186"><a href="#entity_owner-186"><span class="linenos">186</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func</span><span class="p">:</span>
</span><span id="entity_owner-187"><a href="#entity_owner-187"><span class="linenos">187</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_owner-188"><a href="#entity_owner-188"><span class="linenos">188</span></a>        
</span><span id="entity_owner-189"><a href="#entity_owner-189"><span class="linenos">189</span></a>        <span class="n">func_of_the_bound_method</span> <span class="o">=</span> <span class="n">func</span><span class="o">.</span><span class="vm">__func__</span>
</span><span id="entity_owner-190"><a href="#entity_owner-190"><span class="linenos">190</span></a>        <span class="k">for</span> <span class="n">func_class</span> <span class="ow">in</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__self__</span><span class="o">.</span><span class="vm">__class__</span><span class="p">):</span>
</span><span id="entity_owner-191"><a href="#entity_owner-191"><span class="linenos">191</span></a>            <span class="k">if</span> <span class="n">func_class</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">func</span><span class="o">.</span><span class="vm">__name__</span><span class="p">)</span> <span class="ow">is</span> <span class="n">func_of_the_bound_method</span><span class="p">:</span>
</span><span id="entity_owner-192"><a href="#entity_owner-192"><span class="linenos">192</span></a>                <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_owner-193"><a href="#entity_owner-193"><span class="linenos">193</span></a>        
</span><span id="entity_owner-194"><a href="#entity_owner-194"><span class="linenos">194</span></a>        <span class="n">func</span> <span class="o">=</span> <span class="n">func_of_the_bound_method</span>
</span><span id="entity_owner-195"><a href="#entity_owner-195"><span class="linenos">195</span></a>        
</span><span id="entity_owner-196"><a href="#entity_owner-196"><span class="linenos">196</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="entity_owner-197"><a href="#entity_owner-197"><span class="linenos">197</span></a>        <span class="n">func_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="entity_owner-198"><a href="#entity_owner-198"><span class="linenos">198</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="entity_owner-199"><a href="#entity_owner-199"><span class="linenos">199</span></a>            <span class="n">func_class</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func_module</span><span class="p">,</span> <span class="n">func</span><span class="o">.</span><span class="vm">__qualname__</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;.&lt;locals&gt;&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">rsplit</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="entity_owner-200"><a href="#entity_owner-200"><span class="linenos">200</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="entity_owner-201"><a href="#entity_owner-201"><span class="linenos">201</span></a>            <span class="k">return</span> <span class="n">func_module</span>
</span><span id="entity_owner-202"><a href="#entity_owner-202"><span class="linenos">202</span></a>        
</span><span id="entity_owner-203"><a href="#entity_owner-203"><span class="linenos">203</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">func_class</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="entity_owner-204"><a href="#entity_owner-204"><span class="linenos">204</span></a>            <span class="k">return</span> <span class="n">func_class</span>
</span><span id="entity_owner-205"><a href="#entity_owner-205"><span class="linenos">205</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_owner-206"><a href="#entity_owner-206"><span class="linenos">206</span></a>            <span class="k">return</span> <span class="n">func_module</span>
</span><span id="entity_owner-207"><a href="#entity_owner-207"><span class="linenos">207</span></a>    
</span><span id="entity_owner-208"><a href="#entity_owner-208"><span class="linenos">208</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="entity_owner-209"><a href="#entity_owner-209"><span class="linenos">209</span></a>        <span class="k">return</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="s1">&#39;__objclass__&#39;</span><span class="p">)</span>
</span><span id="entity_owner-210"><a href="#entity_owner-210"><span class="linenos">210</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="entity_owner-211"><a href="#entity_owner-211"><span class="linenos">211</span></a>        <span class="k">if</span> <span class="n">func_module</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="entity_owner-212"><a href="#entity_owner-212"><span class="linenos">212</span></a>            <span class="n">func_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="entity_owner-213"><a href="#entity_owner-213"><span class="linenos">213</span></a>        
</span><span id="entity_owner-214"><a href="#entity_owner-214"><span class="linenos">214</span></a>        <span class="k">return</span> <span class="n">func_module</span>
</span></pre></div>


    

                </section>
                <section id="module_repr_importable_str_bracket_pair">
                    <div class="attr variable">
            <span class="name">module_repr_importable_str_bracket_pair</span><span class="annotation">: cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair</span>        =
<span class="default_value">&lt;cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair object&gt;</span>

        
    </div>
    <a class="headerlink" href="#module_repr_importable_str_bracket_pair"></a>
    
    

                </section>
                <section id="module_repr_full_file_path_bracket_pair">
                    <div class="attr variable">
            <span class="name">module_repr_full_file_path_bracket_pair</span><span class="annotation">: cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair</span>        =
<span class="default_value">&lt;cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair object&gt;</span>

        
    </div>
    <a class="headerlink" href="#module_repr_full_file_path_bracket_pair"></a>
    
    

                </section>
                <section id="get_module_importable_str_and_path">
                            <input id="get_module_importable_str_and_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_module_importable_str_and_path</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">module</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_module_importable_str_and_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_module_importable_str_and_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_module_importable_str_and_path-221"><a href="#get_module_importable_str_and_path-221"><span class="linenos">221</span></a><span class="k">def</span> <span class="nf">get_module_importable_str_and_path</span><span class="p">(</span><span class="n">module</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span>
</span><span id="get_module_importable_str_and_path-222"><a href="#get_module_importable_str_and_path-222"><span class="linenos">222</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">):</span>
</span><span id="get_module_importable_str_and_path-223"><a href="#get_module_importable_str_and_path-223"><span class="linenos">223</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Only modules are supported. </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">module</span><span class="p">)</span><span class="si">}</span><span class="s1"> was provided instead&#39;</span><span class="p">)</span>
</span><span id="get_module_importable_str_and_path-224"><a href="#get_module_importable_str_and_path-224"><span class="linenos">224</span></a>    
</span><span id="get_module_importable_str_and_path-225"><a href="#get_module_importable_str_and_path-225"><span class="linenos">225</span></a>    <span class="n">module_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="get_module_importable_str_and_path-226"><a href="#get_module_importable_str_and_path-226"><span class="linenos">226</span></a>    <span class="n">importable_str</span> <span class="o">=</span> <span class="n">module_repr</span><span class="p">[</span><span class="n">find_text_in_brackets</span><span class="p">(</span><span class="n">module_repr</span><span class="p">,</span> <span class="n">module_repr_importable_str_bracket_pair</span><span class="p">)]</span>
</span><span id="get_module_importable_str_and_path-227"><a href="#get_module_importable_str_and_path-227"><span class="linenos">227</span></a>    <span class="n">full_file_path</span> <span class="o">=</span> <span class="n">module_repr</span><span class="p">[</span><span class="n">find_text_in_brackets</span><span class="p">(</span><span class="n">module_repr</span><span class="p">,</span> <span class="n">module_repr_full_file_path_bracket_pair</span><span class="p">)]</span>
</span><span id="get_module_importable_str_and_path-228"><a href="#get_module_importable_str_and_path-228"><span class="linenos">228</span></a>    <span class="k">return</span> <span class="n">importable_str</span><span class="p">,</span> <span class="n">full_file_path</span>
</span></pre></div>


    

                </section>
                <section id="entity_owning_module_info_and_owning_path">
                            <input id="entity_owning_module_info_and_owning_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_owning_module_info_and_owning_path</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">module</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">module</span><span class="p">]]]</span>:</span></span>

                <label class="view-source-button" for="entity_owning_module_info_and_owning_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_owning_module_info_and_owning_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_owning_module_info_and_owning_path-231"><a href="#entity_owning_module_info_and_owning_path-231"><span class="linenos">231</span></a><span class="k">def</span> <span class="nf">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ModuleType</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]]:</span>
</span><span id="entity_owning_module_info_and_owning_path-232"><a href="#entity_owning_module_info_and_owning_path-232"><span class="linenos">232</span></a>    <span class="n">owning_path</span><span class="p">:</span> <span class="n">List</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="entity_owning_module_info_and_owning_path-233"><a href="#entity_owning_module_info_and_owning_path-233"><span class="linenos">233</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="entity_owning_module_info_and_owning_path-234"><a href="#entity_owning_module_info_and_owning_path-234"><span class="linenos">234</span></a>    <span class="n">owner_is_module</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="entity_owning_module_info_and_owning_path-235"><a href="#entity_owning_module_info_and_owning_path-235"><span class="linenos">235</span></a>    <span class="k">while</span> <span class="ow">not</span> <span class="n">owner_is_module</span><span class="p">:</span>
</span><span id="entity_owning_module_info_and_owning_path-236"><a href="#entity_owning_module_info_and_owning_path-236"><span class="linenos">236</span></a>        <span class="n">module</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_owning_module_info_and_owning_path-237"><a href="#entity_owning_module_info_and_owning_path-237"><span class="linenos">237</span></a>        <span class="n">owning_path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="entity_owning_module_info_and_owning_path-238"><a href="#entity_owning_module_info_and_owning_path-238"><span class="linenos">238</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">module</span>
</span><span id="entity_owning_module_info_and_owning_path-239"><a href="#entity_owning_module_info_and_owning_path-239"><span class="linenos">239</span></a>        <span class="n">owner_is_module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="entity_owning_module_info_and_owning_path-240"><a href="#entity_owning_module_info_and_owning_path-240"><span class="linenos">240</span></a>    
</span><span id="entity_owning_module_info_and_owning_path-241"><a href="#entity_owning_module_info_and_owning_path-241"><span class="linenos">241</span></a>    <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">module_file_full_path</span> <span class="o">=</span> <span class="n">get_module_importable_str_and_path</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="entity_owning_module_info_and_owning_path-242"><a href="#entity_owning_module_info_and_owning_path-242"><span class="linenos">242</span></a>    <span class="k">return</span> <span class="n">module</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">module_file_full_path</span><span class="p">,</span> <span class="n">owning_path</span>
</span></pre></div>


    

                </section>
                <section id="entity_owning_module_importable_str">
                            <input id="entity_owning_module_importable_str-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_owning_module_importable_str</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="entity_owning_module_importable_str-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_owning_module_importable_str"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_owning_module_importable_str-245"><a href="#entity_owning_module_importable_str-245"><span class="linenos">245</span></a><span class="k">def</span> <span class="nf">entity_owning_module_importable_str</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="entity_owning_module_importable_str-246"><a href="#entity_owning_module_importable_str-246"><span class="linenos">246</span></a>    <span class="n">_</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_owning_module_importable_str-247"><a href="#entity_owning_module_importable_str-247"><span class="linenos">247</span></a>    <span class="k">return</span> <span class="n">module_importable_str</span>
</span></pre></div>


    

                </section>
                <section id="entity_module_importable_str_and_owning_names_path">
                            <input id="entity_module_importable_str_and_owning_names_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_module_importable_str_and_owning_names_path</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="entity_module_importable_str_and_owning_names_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_module_importable_str_and_owning_names_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_module_importable_str_and_owning_names_path-250"><a href="#entity_module_importable_str_and_owning_names_path-250"><span class="linenos">250</span></a><span class="k">def</span> <span class="nf">entity_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="entity_module_importable_str_and_owning_names_path-251"><a href="#entity_module_importable_str_and_owning_names_path-251"><span class="linenos">251</span></a>    <span class="n">_</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">owning_path</span> <span class="o">=</span> <span class="n">entity_owning_module_info_and_owning_path</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_module_importable_str_and_owning_names_path-252"><a href="#entity_module_importable_str_and_owning_names_path-252"><span class="linenos">252</span></a>    <span class="n">owning_path</span> <span class="o">=</span> <span class="n">owning_path</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
</span><span id="entity_module_importable_str_and_owning_names_path-253"><a href="#entity_module_importable_str_and_owning_names_path-253"><span class="linenos">253</span></a>    <span class="n">owning_names_path</span> <span class="o">=</span> <span class="p">[</span><span class="n">entity_name</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span> <span class="k">for</span> <span class="n">owner</span> <span class="ow">in</span> <span class="n">owning_path</span><span class="p">]</span>
</span><span id="entity_module_importable_str_and_owning_names_path-254"><a href="#entity_module_importable_str_and_owning_names_path-254"><span class="linenos">254</span></a>    <span class="k">return</span> <span class="n">module_importable_str</span><span class="p">,</span> <span class="n">owning_names_path</span>
</span></pre></div>


    

                </section>
                <section id="entity_by_name_module_importable_str_and_owning_names_path">
                            <input id="entity_by_name_module_importable_str_and_owning_names_path-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_by_name_module_importable_str_and_owning_names_path</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">module_importable_str</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">owning_names_path</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="entity_by_name_module_importable_str_and_owning_names_path-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_by_name_module_importable_str_and_owning_names_path"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_by_name_module_importable_str_and_owning_names_path-257"><a href="#entity_by_name_module_importable_str_and_owning_names_path-257"><span class="linenos">257</span></a><span class="k">def</span> <span class="nf">entity_by_name_module_importable_str_and_owning_names_path</span><span class="p">(</span><span class="n">entity_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">module_importable_str</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">owning_names_path</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="entity_by_name_module_importable_str_and_owning_names_path-258"><a href="#entity_by_name_module_importable_str_and_owning_names_path-258"><span class="linenos">258</span></a>    <span class="n">owner</span> <span class="o">=</span> <span class="n">import_module</span><span class="p">(</span><span class="n">module_importable_str</span><span class="p">)</span>
</span><span id="entity_by_name_module_importable_str_and_owning_names_path-259"><a href="#entity_by_name_module_importable_str_and_owning_names_path-259"><span class="linenos">259</span></a>    <span class="k">for</span> <span class="n">owner_name</span> <span class="ow">in</span> <span class="nb">reversed</span><span class="p">(</span><span class="n">owning_names_path</span><span class="p">):</span>
</span><span id="entity_by_name_module_importable_str_and_owning_names_path-260"><a href="#entity_by_name_module_importable_str_and_owning_names_path-260"><span class="linenos">260</span></a>        <span class="n">owner</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">owner_name</span><span class="p">)</span>
</span><span id="entity_by_name_module_importable_str_and_owning_names_path-261"><a href="#entity_by_name_module_importable_str_and_owning_names_path-261"><span class="linenos">261</span></a>
</span><span id="entity_by_name_module_importable_str_and_owning_names_path-262"><a href="#entity_by_name_module_importable_str_and_owning_names_path-262"><span class="linenos">262</span></a>    <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="module_repr_limited_bracket_pair">
                    <div class="attr variable">
            <span class="name">module_repr_limited_bracket_pair</span><span class="annotation">: cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair</span>        =
<span class="default_value">&lt;cengal.text_processing.brackets_processing.versions.v_0.brackets.BracketPair object&gt;</span>

        
    </div>
    <a class="headerlink" href="#module_repr_limited_bracket_pair"></a>
    
    

                </section>
                <section id="normalized_owner_repr">
                            <input id="normalized_owner_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">normalized_owner_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owner</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="normalized_owner_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#normalized_owner_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="normalized_owner_repr-268"><a href="#normalized_owner_repr-268"><span class="linenos">268</span></a><span class="k">def</span> <span class="nf">normalized_owner_repr</span><span class="p">(</span><span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="normalized_owner_repr-269"><a href="#normalized_owner_repr-269"><span class="linenos">269</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="normalized_owner_repr-270"><a href="#normalized_owner_repr-270"><span class="linenos">270</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="normalized_owner_repr-271"><a href="#normalized_owner_repr-271"><span class="linenos">271</span></a>    
</span><span id="normalized_owner_repr-272"><a href="#normalized_owner_repr-272"><span class="linenos">272</span></a>    <span class="n">owner_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="normalized_owner_repr-273"><a href="#normalized_owner_repr-273"><span class="linenos">273</span></a>    <span class="n">result</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">replace_text_with_brackets</span><span class="p">(</span><span class="n">owner_repr</span><span class="p">,</span> <span class="n">module_repr_limited_bracket_pair</span><span class="p">,</span> <span class="s2">&quot;&gt;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="normalized_owner_repr-274"><a href="#normalized_owner_repr-274"><span class="linenos">274</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="normalized_code_owner_repr">
                            <input id="normalized_code_owner_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">normalized_code_owner_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">code</span><span class="p">:</span> <span class="n">code</span>, </span><span class="param"><span class="n">owner</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="normalized_code_owner_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#normalized_code_owner_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="normalized_code_owner_repr-277"><a href="#normalized_code_owner_repr-277"><span class="linenos">277</span></a><span class="k">def</span> <span class="nf">normalized_code_owner_repr</span><span class="p">(</span><span class="n">code</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">,</span> <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="normalized_code_owner_repr-278"><a href="#normalized_code_owner_repr-278"><span class="linenos">278</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="normalized_code_owner_repr-279"><a href="#normalized_code_owner_repr-279"><span class="linenos">279</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="normalized_code_owner_repr-280"><a href="#normalized_code_owner_repr-280"><span class="linenos">280</span></a>    
</span><span id="normalized_code_owner_repr-281"><a href="#normalized_code_owner_repr-281"><span class="linenos">281</span></a>    <span class="n">owner_repr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="normalized_code_owner_repr-282"><a href="#normalized_code_owner_repr-282"><span class="linenos">282</span></a>    <span class="n">result</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">replace_text_with_brackets</span><span class="p">(</span><span class="n">owner_repr</span><span class="p">,</span> <span class="n">module_repr_limited_bracket_pair</span><span class="p">,</span> <span class="sa">f</span><span class="s2">&quot; line </span><span class="si">{</span><span class="n">code</span><span class="o">.</span><span class="n">co_firstlineno</span><span class="si">}</span><span class="s2">&gt;&quot;</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="normalized_code_owner_repr-283"><a href="#normalized_code_owner_repr-283"><span class="linenos">283</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="entity_owner_repr">
                            <input id="entity_owner_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_owner_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_owner_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_owner_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_owner_repr-286"><a href="#entity_owner_repr-286"><span class="linenos">286</span></a><span class="k">def</span> <span class="nf">entity_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_owner_repr-287"><a href="#entity_owner_repr-287"><span class="linenos">287</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_owner_repr-288"><a href="#entity_owner_repr-288"><span class="linenos">288</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_owner_repr-289"><a href="#entity_owner_repr-289"><span class="linenos">289</span></a>    
</span><span id="entity_owner_repr-290"><a href="#entity_owner_repr-290"><span class="linenos">290</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_owner_repr-291"><a href="#entity_owner_repr-291"><span class="linenos">291</span></a>        <span class="k">return</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="entity_owner_repr-292"><a href="#entity_owner_repr-292"><span class="linenos">292</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_owner_repr-293"><a href="#entity_owner_repr-293"><span class="linenos">293</span></a>        <span class="k">return</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="owner_name">
                            <input id="owner_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">owner_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owner</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Type</span><span class="p">,</span> <span class="n">module</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="owner_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#owner_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="owner_name-296"><a href="#owner_name-296"><span class="linenos">296</span></a><span class="k">def</span> <span class="nf">owner_name</span><span class="p">(</span><span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]])</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="owner_name-297"><a href="#owner_name-297"><span class="linenos">297</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="owner_name-298"><a href="#owner_name-298"><span class="linenos">298</span></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">()</span>
</span><span id="owner_name-299"><a href="#owner_name-299"><span class="linenos">299</span></a>    
</span><span id="owner_name-300"><a href="#owner_name-300"><span class="linenos">300</span></a>    <span class="k">return</span> <span class="n">owner</span><span class="o">.</span><span class="vm">__name__</span>
</span></pre></div>


    

                </section>
                <section id="entity_owner_name">
                            <input id="entity_owner_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_owner_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_owner_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_owner_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_owner_name-303"><a href="#entity_owner_name-303"><span class="linenos">303</span></a><span class="k">def</span> <span class="nf">entity_owner_name</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_owner_name-304"><a href="#entity_owner_name-304"><span class="linenos">304</span></a>    <span class="k">return</span> <span class="n">owner_name</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="frame_param_names">
                            <input id="frame_param_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">frame_param_names</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">frame_instance</span><span class="p">:</span> <span class="n">frame</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>:</span></span>

                <label class="view-source-button" for="frame_param_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#frame_param_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="frame_param_names-307"><a href="#frame_param_names-307"><span class="linenos">307</span></a><span class="k">def</span> <span class="nf">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">:</span> <span class="n">FrameType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="frame_param_names-308"><a href="#frame_param_names-308"><span class="linenos">308</span></a>    <span class="k">return</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_param_names">
                            <input id="intro_func_param_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_param_names</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>:</span></span>

                <label class="view-source-button" for="intro_func_param_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_param_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_param_names-311"><a href="#intro_func_param_names-311"><span class="linenos">311</span></a><span class="k">def</span> <span class="nf">intro_func_param_names</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamNames</span><span class="p">:</span>
</span><span id="intro_func_param_names-312"><a href="#intro_func_param_names-312"><span class="linenos">312</span></a>    <span class="k">return</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="CodeParamsWithValues">
                    <div class="attr variable">
            <span class="name">CodeParamsWithValues</span>        =
<input id="CodeParamsWithValues-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="CodeParamsWithValues-view-value"></label><span class="default_value">&lt;class &#39;cengal.code_flow_control.python_bytecode_manipulator.versions.v_0.python_bytecode_manipulator.CodeParamNames&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#CodeParamsWithValues"></a>
    
    

                </section>
                <section id="ParamWithValue">
                    <div class="attr variable">
            <span class="name">ParamWithValue</span>        =
<span class="default_value">typing.Tuple[str, typing.Any]</span>

        
    </div>
    <a class="headerlink" href="#ParamWithValue"></a>
    
    

                </section>
                <section id="fill_code_params_with_values">
                            <input id="fill_code_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">fill_code_params_with_values</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code_params</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>,</span><span class="param">	<span class="n">args</span>,</span><span class="param">	<span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="fill_code_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#fill_code_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="fill_code_params_with_values-319"><a href="#fill_code_params_with_values-319"><span class="linenos">319</span></a><span class="k">def</span> <span class="nf">fill_code_params_with_values</span><span class="p">(</span><span class="n">code_params</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="fill_code_params_with_values-320"><a href="#fill_code_params_with_values-320"><span class="linenos">320</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params</span>
</span><span id="fill_code_params_with_values-321"><a href="#fill_code_params_with_values-321"><span class="linenos">321</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="fill_code_params_with_values-322"><a href="#fill_code_params_with_values-322"><span class="linenos">322</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="fill_code_params_with_values-323"><a href="#fill_code_params_with_values-323"><span class="linenos">323</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="fill_code_params_with_values-324"><a href="#fill_code_params_with_values-324"><span class="linenos">324</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="fill_code_params_with_values-325"><a href="#fill_code_params_with_values-325"><span class="linenos">325</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="fill_code_params_with_values-326"><a href="#fill_code_params_with_values-326"><span class="linenos">326</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="fill_code_params_with_values-327"><a href="#fill_code_params_with_values-327"><span class="linenos">327</span></a>    
</span><span id="fill_code_params_with_values-328"><a href="#fill_code_params_with_values-328"><span class="linenos">328</span></a>    <span class="n">positional_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">args</span><span class="p">[</span><span class="n">index</span><span class="p">])</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">)))</span>
</span><span id="fill_code_params_with_values-329"><a href="#fill_code_params_with_values-329"><span class="linenos">329</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="fill_code_params_with_values-330"><a href="#fill_code_params_with_values-330"><span class="linenos">330</span></a>        <span class="n">positional_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">args</span><span class="p">[</span><span class="n">index</span><span class="p">])</span> <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)))</span>
</span><span id="fill_code_params_with_values-331"><a href="#fill_code_params_with_values-331"><span class="linenos">331</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="fill_code_params_with_values-332"><a href="#fill_code_params_with_values-332"><span class="linenos">332</span></a>        <span class="n">positional_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="fill_code_params_with_values-333"><a href="#fill_code_params_with_values-333"><span class="linenos">333</span></a>    
</span><span id="fill_code_params_with_values-334"><a href="#fill_code_params_with_values-334"><span class="linenos">334</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="fill_code_params_with_values-335"><a href="#fill_code_params_with_values-335"><span class="linenos">335</span></a>        <span class="n">keyword_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">))</span>
</span><span id="fill_code_params_with_values-336"><a href="#fill_code_params_with_values-336"><span class="linenos">336</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="fill_code_params_with_values-337"><a href="#fill_code_params_with_values-337"><span class="linenos">337</span></a>        <span class="n">keyword_only_values</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">()</span>
</span><span id="fill_code_params_with_values-338"><a href="#fill_code_params_with_values-338"><span class="linenos">338</span></a>
</span><span id="fill_code_params_with_values-339"><a href="#fill_code_params_with_values-339"><span class="linenos">339</span></a>    <span class="n">result_args</span><span class="p">:</span> <span class="n">Tuple</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="n">positional_len</span><span class="p">:]</span>
</span><span id="fill_code_params_with_values-340"><a href="#fill_code_params_with_values-340"><span class="linenos">340</span></a>    <span class="n">result_kwargs</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">key</span><span class="p">:</span> <span class="n">value</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">}</span>
</span><span id="fill_code_params_with_values-341"><a href="#fill_code_params_with_values-341"><span class="linenos">341</span></a>    
</span><span id="fill_code_params_with_values-342"><a href="#fill_code_params_with_values-342"><span class="linenos">342</span></a>    <span class="k">return</span> <span class="n">CodeParamsWithValues</span><span class="p">(</span><span class="n">positional_values</span><span class="p">,</span> <span class="n">positional_only_values</span><span class="p">,</span> <span class="n">keyword_only_values</span><span class="p">),</span> <span class="n">result_args</span><span class="p">,</span> <span class="n">result_kwargs</span>
</span></pre></div>


    

                </section>
                <section id="func_params_with_values">
                            <input id="func_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">func_params_with_values</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">func</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Awaitable</span><span class="p">]</span>,</span><span class="param">	<span class="n">args</span>,</span><span class="param">	<span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="func_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#func_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="func_params_with_values-345"><a href="#func_params_with_values-345"><span class="linenos">345</span></a><span class="k">def</span> <span class="nf">func_params_with_values</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">],</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="func_params_with_values-346"><a href="#func_params_with_values-346"><span class="linenos">346</span></a>    <span class="k">return</span> <span class="n">fill_code_params_with_values</span><span class="p">(</span><span class="n">func_param_names</span><span class="p">(</span><span class="n">func</span><span class="p">),</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="intro_frame_params_with_values">
                            <input id="intro_frame_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_frame_params_with_values</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">frame_instance</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>:</span></span>

                <label class="view-source-button" for="intro_frame_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_frame_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_frame_params_with_values-349"><a href="#intro_frame_params_with_values-349"><span class="linenos">349</span></a><span class="k">def</span> <span class="nf">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamsWithValues</span><span class="p">:</span>
</span><span id="intro_frame_params_with_values-350"><a href="#intro_frame_params_with_values-350"><span class="linenos">350</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="intro_frame_params_with_values-351"><a href="#intro_frame_params_with_values-351"><span class="linenos">351</span></a>    <span class="n">fr_locals</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_locals</span>
</span><span id="intro_frame_params_with_values-352"><a href="#intro_frame_params_with_values-352"><span class="linenos">352</span></a>    <span class="k">return</span> <span class="n">CodeParamsWithValues</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">positional</span><span class="p">)),</span> \
</span><span id="intro_frame_params_with_values-353"><a href="#intro_frame_params_with_values-353"><span class="linenos">353</span></a>        <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">positional_only</span><span class="p">)),</span> \
</span><span id="intro_frame_params_with_values-354"><a href="#intro_frame_params_with_values-354"><span class="linenos">354</span></a>        <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">)))</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_params_with_values">
                            <input id="intro_func_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_params_with_values</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>:</span></span>

                <label class="view-source-button" for="intro_func_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_params_with_values-357"><a href="#intro_func_params_with_values-357"><span class="linenos">357</span></a><span class="k">def</span> <span class="nf">intro_func_params_with_values</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">CodeParamsWithValues</span><span class="p">:</span>
</span><span id="intro_func_params_with_values-358"><a href="#intro_func_params_with_values-358"><span class="linenos">358</span></a>    <span class="k">return</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="intro_frame_all_params_with_values">
                            <input id="intro_frame_all_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_frame_all_params_with_values</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">frame_instance</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="intro_frame_all_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_frame_all_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_frame_all_params_with_values-361"><a href="#intro_frame_all_params_with_values-361"><span class="linenos">361</span></a><span class="k">def</span> <span class="nf">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ParamWithValue</span><span class="p">]:</span>
</span><span id="intro_frame_all_params_with_values-362"><a href="#intro_frame_all_params_with_values-362"><span class="linenos">362</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">_</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">frame_param_names</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="intro_frame_all_params_with_values-363"><a href="#intro_frame_all_params_with_values-363"><span class="linenos">363</span></a>    <span class="n">all_params</span> <span class="o">=</span> <span class="n">positional</span> <span class="o">+</span> <span class="n">keyword_only</span>
</span><span id="intro_frame_all_params_with_values-364"><a href="#intro_frame_all_params_with_values-364"><span class="linenos">364</span></a>    <span class="n">fr_locals</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_locals</span>
</span><span id="intro_frame_all_params_with_values-365"><a href="#intro_frame_all_params_with_values-365"><span class="linenos">365</span></a>    <span class="k">return</span> <span class="nb">tuple</span><span class="p">(((</span><span class="n">arg</span><span class="p">,</span> <span class="n">fr_locals</span><span class="p">[</span><span class="n">arg</span><span class="p">])</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">all_params</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_all_params_with_values">
                            <input id="intro_func_all_params_with_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_all_params_with_values</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="intro_func_all_params_with_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_all_params_with_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_all_params_with_values-368"><a href="#intro_func_all_params_with_values-368"><span class="linenos">368</span></a><span class="k">def</span> <span class="nf">intro_func_all_params_with_values</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">ParamWithValue</span><span class="p">]:</span>
</span><span id="intro_func_all_params_with_values-369"><a href="#intro_func_all_params_with_values-369"><span class="linenos">369</span></a>    <span class="k">return</span> <span class="n">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="intro_frame_all_params_with_values_as_ordered_dict">
                            <input id="intro_frame_all_params_with_values_as_ordered_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_frame_all_params_with_values_as_ordered_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">frame_instance</span></span><span class="return-annotation">) -> <span class="n">OrderedDict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="intro_frame_all_params_with_values_as_ordered_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_frame_all_params_with_values_as_ordered_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_frame_all_params_with_values_as_ordered_dict-372"><a href="#intro_frame_all_params_with_values_as_ordered_dict-372"><span class="linenos">372</span></a><span class="k">def</span> <span class="nf">intro_frame_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OrderedDictType</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="intro_frame_all_params_with_values_as_ordered_dict-373"><a href="#intro_frame_all_params_with_values_as_ordered_dict-373"><span class="linenos">373</span></a>    <span class="k">return</span> <span class="n">OrderedDict</span><span class="p">(</span><span class="n">intro_frame_all_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_all_params_with_values_as_ordered_dict">
                            <input id="intro_func_all_params_with_values_as_ordered_dict-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_all_params_with_values_as_ordered_dict</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">OrderedDict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="intro_func_all_params_with_values_as_ordered_dict-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_all_params_with_values_as_ordered_dict"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_all_params_with_values_as_ordered_dict-376"><a href="#intro_func_all_params_with_values_as_ordered_dict-376"><span class="linenos">376</span></a><span class="k">def</span> <span class="nf">intro_func_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">OrderedDictType</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="intro_func_all_params_with_values_as_ordered_dict-377"><a href="#intro_func_all_params_with_values_as_ordered_dict-377"><span class="linenos">377</span></a>    <span class="k">return</span> <span class="n">intro_frame_all_params_with_values_as_ordered_dict</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="code_params_with_values_to_signature_items_gen">
                            <input id="code_params_with_values_to_signature_items_gen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_params_with_values_to_signature_items_gen</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>,</span><span class="param">	<span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="code_params_with_values_to_signature_items_gen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_params_with_values_to_signature_items_gen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_params_with_values_to_signature_items_gen-380"><a href="#code_params_with_values_to_signature_items_gen-380"><span class="linenos">380</span></a><span class="k">def</span> <span class="nf">code_params_with_values_to_signature_items_gen</span><span class="p">(</span><span class="n">code_params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="code_params_with_values_to_signature_items_gen-381"><a href="#code_params_with_values_to_signature_items_gen-381"><span class="linenos">381</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params_with_values</span>
</span><span id="code_params_with_values_to_signature_items_gen-382"><a href="#code_params_with_values_to_signature_items_gen-382"><span class="linenos">382</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="code_params_with_values_to_signature_items_gen-383"><a href="#code_params_with_values_to_signature_items_gen-383"><span class="linenos">383</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="code_params_with_values_to_signature_items_gen-384"><a href="#code_params_with_values_to_signature_items_gen-384"><span class="linenos">384</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="code_params_with_values_to_signature_items_gen-385"><a href="#code_params_with_values_to_signature_items_gen-385"><span class="linenos">385</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="code_params_with_values_to_signature_items_gen-386"><a href="#code_params_with_values_to_signature_items_gen-386"><span class="linenos">386</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature_items_gen-387"><a href="#code_params_with_values_to_signature_items_gen-387"><span class="linenos">387</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="code_params_with_values_to_signature_items_gen-388"><a href="#code_params_with_values_to_signature_items_gen-388"><span class="linenos">388</span></a>    
</span><span id="code_params_with_values_to_signature_items_gen-389"><a href="#code_params_with_values_to_signature_items_gen-389"><span class="linenos">389</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="code_params_with_values_to_signature_items_gen-390"><a href="#code_params_with_values_to_signature_items_gen-390"><span class="linenos">390</span></a>        <span class="n">arg_name</span><span class="p">,</span> <span class="n">arg_value</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="code_params_with_values_to_signature_items_gen-391"><a href="#code_params_with_values_to_signature_items_gen-391"><span class="linenos">391</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">positional_only_delimiter_place</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">index</span> <span class="o">==</span> <span class="n">positional_only_delimiter_place</span><span class="p">):</span>
</span><span id="code_params_with_values_to_signature_items_gen-392"><a href="#code_params_with_values_to_signature_items_gen-392"><span class="linenos">392</span></a>            <span class="k">yield</span> <span class="s1">&#39;/&#39;</span>
</span><span id="code_params_with_values_to_signature_items_gen-393"><a href="#code_params_with_values_to_signature_items_gen-393"><span class="linenos">393</span></a>        
</span><span id="code_params_with_values_to_signature_items_gen-394"><a href="#code_params_with_values_to_signature_items_gen-394"><span class="linenos">394</span></a>        <span class="k">if</span> <span class="n">verbose</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature_items_gen-395"><a href="#code_params_with_values_to_signature_items_gen-395"><span class="linenos">395</span></a>            <span class="k">yield</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">arg_value</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="code_params_with_values_to_signature_items_gen-396"><a href="#code_params_with_values_to_signature_items_gen-396"><span class="linenos">396</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature_items_gen-397"><a href="#code_params_with_values_to_signature_items_gen-397"><span class="linenos">397</span></a>            <span class="k">yield</span> <span class="nb">str</span><span class="p">(</span><span class="n">arg_value</span><span class="p">)</span>
</span><span id="code_params_with_values_to_signature_items_gen-398"><a href="#code_params_with_values_to_signature_items_gen-398"><span class="linenos">398</span></a>    
</span><span id="code_params_with_values_to_signature_items_gen-399"><a href="#code_params_with_values_to_signature_items_gen-399"><span class="linenos">399</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature_items_gen-400"><a href="#code_params_with_values_to_signature_items_gen-400"><span class="linenos">400</span></a>        <span class="k">yield</span> <span class="s1">&#39;*&#39;</span>
</span><span id="code_params_with_values_to_signature_items_gen-401"><a href="#code_params_with_values_to_signature_items_gen-401"><span class="linenos">401</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature_items_gen-402"><a href="#code_params_with_values_to_signature_items_gen-402"><span class="linenos">402</span></a>            <span class="n">arg_name</span><span class="p">,</span> <span class="n">arg_value</span> <span class="o">=</span> <span class="n">arg</span>
</span><span id="code_params_with_values_to_signature_items_gen-403"><a href="#code_params_with_values_to_signature_items_gen-403"><span class="linenos">403</span></a>            <span class="k">yield</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">arg_name</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">arg_value</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


    

                </section>
                <section id="code_params_to_signature_items_gen">
                            <input id="code_params_to_signature_items_gen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_params_to_signature_items_gen</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">code_params</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span></span><span class="return-annotation">) -> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="code_params_to_signature_items_gen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_params_to_signature_items_gen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_params_to_signature_items_gen-406"><a href="#code_params_to_signature_items_gen-406"><span class="linenos">406</span></a><span class="k">def</span> <span class="nf">code_params_to_signature_items_gen</span><span class="p">(</span><span class="n">code_params</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="kc">None</span><span class="p">,</span> <span class="kc">None</span><span class="p">]:</span>
</span><span id="code_params_to_signature_items_gen-407"><a href="#code_params_to_signature_items_gen-407"><span class="linenos">407</span></a>    <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">code_params</span>
</span><span id="code_params_to_signature_items_gen-408"><a href="#code_params_to_signature_items_gen-408"><span class="linenos">408</span></a>    <span class="n">positional_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional</span><span class="p">)</span>
</span><span id="code_params_to_signature_items_gen-409"><a href="#code_params_to_signature_items_gen-409"><span class="linenos">409</span></a>    <span class="n">positional_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">positional_only</span><span class="p">)</span>
</span><span id="code_params_to_signature_items_gen-410"><a href="#code_params_to_signature_items_gen-410"><span class="linenos">410</span></a>    <span class="n">keyword_only_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="code_params_to_signature_items_gen-411"><a href="#code_params_to_signature_items_gen-411"><span class="linenos">411</span></a>    <span class="n">positional_only_delimiter_place</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="code_params_to_signature_items_gen-412"><a href="#code_params_to_signature_items_gen-412"><span class="linenos">412</span></a>    <span class="k">if</span> <span class="n">positional_only_len</span><span class="p">:</span>
</span><span id="code_params_to_signature_items_gen-413"><a href="#code_params_to_signature_items_gen-413"><span class="linenos">413</span></a>        <span class="n">positional_only_delimiter_place</span> <span class="o">=</span> <span class="n">positional_only_len</span>
</span><span id="code_params_to_signature_items_gen-414"><a href="#code_params_to_signature_items_gen-414"><span class="linenos">414</span></a>    
</span><span id="code_params_to_signature_items_gen-415"><a href="#code_params_to_signature_items_gen-415"><span class="linenos">415</span></a>    <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">arg</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">positional</span><span class="p">):</span>
</span><span id="code_params_to_signature_items_gen-416"><a href="#code_params_to_signature_items_gen-416"><span class="linenos">416</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">positional_only_delimiter_place</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">index</span> <span class="o">==</span> <span class="n">positional_only_delimiter_place</span><span class="p">):</span>
</span><span id="code_params_to_signature_items_gen-417"><a href="#code_params_to_signature_items_gen-417"><span class="linenos">417</span></a>            <span class="k">yield</span> <span class="s1">&#39;/&#39;</span>
</span><span id="code_params_to_signature_items_gen-418"><a href="#code_params_to_signature_items_gen-418"><span class="linenos">418</span></a>        
</span><span id="code_params_to_signature_items_gen-419"><a href="#code_params_to_signature_items_gen-419"><span class="linenos">419</span></a>        <span class="c1"># yield arg[0]</span>
</span><span id="code_params_to_signature_items_gen-420"><a href="#code_params_to_signature_items_gen-420"><span class="linenos">420</span></a>        <span class="k">yield</span> <span class="n">arg</span>
</span><span id="code_params_to_signature_items_gen-421"><a href="#code_params_to_signature_items_gen-421"><span class="linenos">421</span></a>    
</span><span id="code_params_to_signature_items_gen-422"><a href="#code_params_to_signature_items_gen-422"><span class="linenos">422</span></a>    <span class="k">if</span> <span class="n">keyword_only_len</span><span class="p">:</span>
</span><span id="code_params_to_signature_items_gen-423"><a href="#code_params_to_signature_items_gen-423"><span class="linenos">423</span></a>        <span class="k">yield</span> <span class="s1">&#39;*&#39;</span>
</span><span id="code_params_to_signature_items_gen-424"><a href="#code_params_to_signature_items_gen-424"><span class="linenos">424</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="code_params_to_signature_items_gen-425"><a href="#code_params_to_signature_items_gen-425"><span class="linenos">425</span></a>            <span class="c1"># yield arg[0]</span>
</span><span id="code_params_to_signature_items_gen-426"><a href="#code_params_to_signature_items_gen-426"><span class="linenos">426</span></a>            <span class="k">yield</span> <span class="n">arg</span>
</span></pre></div>


    

                </section>
                <section id="code_params_with_values_to_signature">
                            <input id="code_params_with_values_to_signature-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_params_with_values_to_signature</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">params_with_values</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>,</span><span class="param">	<span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>,</span><span class="param">	<span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="code_params_with_values_to_signature-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_params_with_values_to_signature"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_params_with_values_to_signature-429"><a href="#code_params_with_values_to_signature-429"><span class="linenos">429</span></a><span class="k">def</span> <span class="nf">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature-430"><a href="#code_params_with_values_to_signature-430"><span class="linenos">430</span></a>    <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature-431"><a href="#code_params_with_values_to_signature-431"><span class="linenos">431</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="code_params_with_values_to_signature-432"><a href="#code_params_with_values_to_signature-432"><span class="linenos">432</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="code_params_with_values_to_signature-433"><a href="#code_params_with_values_to_signature-433"><span class="linenos">433</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="code_params_with_values_to_signature-434"><a href="#code_params_with_values_to_signature-434"><span class="linenos">434</span></a>    
</span><span id="code_params_with_values_to_signature-435"><a href="#code_params_with_values_to_signature-435"><span class="linenos">435</span></a>    <span class="k">return</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">code_params_with_values_to_signature_items_gen</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="code_params_to_signature">
                            <input id="code_params_to_signature-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">code_params_to_signature</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">param_names</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">python_bytecode_manipulator</span><span class="o">.</span><span class="n">CodeParamNames</span>,</span><span class="param">	<span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="code_params_to_signature-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#code_params_to_signature"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="code_params_to_signature-438"><a href="#code_params_to_signature-438"><span class="linenos">438</span></a><span class="k">def</span> <span class="nf">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">:</span> <span class="n">CodeParamNames</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="code_params_to_signature-439"><a href="#code_params_to_signature-439"><span class="linenos">439</span></a>    <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="code_params_to_signature-440"><a href="#code_params_to_signature-440"><span class="linenos">440</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="code_params_to_signature-441"><a href="#code_params_to_signature-441"><span class="linenos">441</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="code_params_to_signature-442"><a href="#code_params_to_signature-442"><span class="linenos">442</span></a>        <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="code_params_to_signature-443"><a href="#code_params_to_signature-443"><span class="linenos">443</span></a>    
</span><span id="code_params_to_signature-444"><a href="#code_params_to_signature-444"><span class="linenos">444</span></a>    <span class="k">return</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">code_params_to_signature_items_gen</span><span class="p">(</span><span class="n">param_names</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="entity_repr_limited">
                            <input id="entity_repr_limited-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_repr_limited</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_repr_limited-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_repr_limited"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_repr_limited-447"><a href="#entity_repr_limited-447"><span class="linenos">447</span></a><span class="k">def</span> <span class="nf">entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="entity_repr_limited-448"><a href="#entity_repr_limited-448"><span class="linenos">448</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_repr_limited-449"><a href="#entity_repr_limited-449"><span class="linenos">449</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_repr_limited-450"><a href="#entity_repr_limited-450"><span class="linenos">450</span></a>    
</span><span id="entity_repr_limited-451"><a href="#entity_repr_limited-451"><span class="linenos">451</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_repr_limited-452"><a href="#entity_repr_limited-452"><span class="linenos">452</span></a>        <span class="n">code</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="entity_repr_limited-453"><a href="#entity_repr_limited-453"><span class="linenos">453</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_limited-454"><a href="#entity_repr_limited-454"><span class="linenos">454</span></a>        <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr_limited-455"><a href="#entity_repr_limited-455"><span class="linenos">455</span></a>    
</span><span id="entity_repr_limited-456"><a href="#entity_repr_limited-456"><span class="linenos">456</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="entity_repr_limited-457"><a href="#entity_repr_limited-457"><span class="linenos">457</span></a>    <span class="n">param_names</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="entity_repr_limited-458"><a href="#entity_repr_limited-458"><span class="linenos">458</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="entity_repr_limited-459"><a href="#entity_repr_limited-459"><span class="linenos">459</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span></pre></div>


    

                </section>
                <section id="entity_repr_limited_try_qualname">
                            <input id="entity_repr_limited_try_qualname-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_repr_limited_try_qualname</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_repr_limited_try_qualname-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_repr_limited_try_qualname"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_repr_limited_try_qualname-462"><a href="#entity_repr_limited_try_qualname-462"><span class="linenos">462</span></a><span class="k">def</span> <span class="nf">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="entity_repr_limited_try_qualname-463"><a href="#entity_repr_limited_try_qualname-463"><span class="linenos">463</span></a>    <span class="k">if</span> <span class="n">has_code</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_repr_limited_try_qualname-464"><a href="#entity_repr_limited_try_qualname-464"><span class="linenos">464</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_repr_limited_try_qualname-465"><a href="#entity_repr_limited_try_qualname-465"><span class="linenos">465</span></a>            <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_repr_limited_try_qualname-466"><a href="#entity_repr_limited_try_qualname-466"><span class="linenos">466</span></a>        
</span><span id="entity_repr_limited_try_qualname-467"><a href="#entity_repr_limited_try_qualname-467"><span class="linenos">467</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_repr_limited_try_qualname-468"><a href="#entity_repr_limited_try_qualname-468"><span class="linenos">468</span></a>            <span class="n">code</span> <span class="o">=</span> <span class="n">entity</span>
</span><span id="entity_repr_limited_try_qualname-469"><a href="#entity_repr_limited_try_qualname-469"><span class="linenos">469</span></a>            <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-470"><a href="#entity_repr_limited_try_qualname-470"><span class="linenos">470</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_limited_try_qualname-471"><a href="#entity_repr_limited_try_qualname-471"><span class="linenos">471</span></a>            <span class="n">code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-472"><a href="#entity_repr_limited_try_qualname-472"><span class="linenos">472</span></a>            <span class="n">func_name</span> <span class="o">=</span> <span class="n">func_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-473"><a href="#entity_repr_limited_try_qualname-473"><span class="linenos">473</span></a>        
</span><span id="entity_repr_limited_try_qualname-474"><a href="#entity_repr_limited_try_qualname-474"><span class="linenos">474</span></a>        <span class="n">param_names</span> <span class="o">=</span> <span class="n">code_param_names</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-475"><a href="#entity_repr_limited_try_qualname-475"><span class="linenos">475</span></a>        <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_to_signature</span><span class="p">(</span><span class="n">param_names</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-476"><a href="#entity_repr_limited_try_qualname-476"><span class="linenos">476</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span><span id="entity_repr_limited_try_qualname-477"><a href="#entity_repr_limited_try_qualname-477"><span class="linenos">477</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_limited_try_qualname-478"><a href="#entity_repr_limited_try_qualname-478"><span class="linenos">478</span></a>        <span class="n">entity_type_name</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="o">.</span><span class="vm">__name__</span>
</span><span id="entity_repr_limited_try_qualname-479"><a href="#entity_repr_limited_try_qualname-479"><span class="linenos">479</span></a>        <span class="n">entity_properties_with_values</span> <span class="o">=</span> <span class="n">entity_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr_limited_try_qualname-480"><a href="#entity_repr_limited_try_qualname-480"><span class="linenos">480</span></a>        <span class="k">if</span> <span class="n">formatted</span><span class="p">:</span>
</span><span id="entity_repr_limited_try_qualname-481"><a href="#entity_repr_limited_try_qualname-481"><span class="linenos">481</span></a>            <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;,</span><span class="se">\n\t</span><span class="s1">&#39;</span>
</span><span id="entity_repr_limited_try_qualname-482"><a href="#entity_repr_limited_try_qualname-482"><span class="linenos">482</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_limited_try_qualname-483"><a href="#entity_repr_limited_try_qualname-483"><span class="linenos">483</span></a>            <span class="n">delimiter</span> <span class="o">=</span> <span class="s1">&#39;, &#39;</span>
</span><span id="entity_repr_limited_try_qualname-484"><a href="#entity_repr_limited_try_qualname-484"><span class="linenos">484</span></a>        
</span><span id="entity_repr_limited_try_qualname-485"><a href="#entity_repr_limited_try_qualname-485"><span class="linenos">485</span></a>        <span class="n">entity_properties_str</span> <span class="o">=</span> <span class="n">delimiter</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">=</span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">entity_properties_with_values</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>
</span><span id="entity_repr_limited_try_qualname-486"><a href="#entity_repr_limited_try_qualname-486"><span class="linenos">486</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity_type_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">entity_properties_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span></pre></div>


    

                </section>
                <section id="entity_repr_owner_based">
                            <input id="entity_repr_owner_based-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_repr_owner_based</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_repr_owner_based-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_repr_owner_based"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_repr_owner_based-489"><a href="#entity_repr_owner_based-489"><span class="linenos">489</span></a><span class="k">def</span> <span class="nf">entity_repr_owner_based</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="entity_repr_owner_based-490"><a href="#entity_repr_owner_based-490"><span class="linenos">490</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_repr_owner_based-491"><a href="#entity_repr_owner_based-491"><span class="linenos">491</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_repr_owner_based-492"><a href="#entity_repr_owner_based-492"><span class="linenos">492</span></a>    
</span><span id="entity_repr_owner_based-493"><a href="#entity_repr_owner_based-493"><span class="linenos">493</span></a>    <span class="n">owner</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr_owner_based-494"><a href="#entity_repr_owner_based-494"><span class="linenos">494</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_repr_owner_based-495"><a href="#entity_repr_owner_based-495"><span class="linenos">495</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner</span><span class="p">)</span>
</span><span id="entity_repr_owner_based-496"><a href="#entity_repr_owner_based-496"><span class="linenos">496</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_owner_based-497"><a href="#entity_repr_owner_based-497"><span class="linenos">497</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">owner</span><span class="p">)</span>
</span><span id="entity_repr_owner_based-498"><a href="#entity_repr_owner_based-498"><span class="linenos">498</span></a>
</span><span id="entity_repr_owner_based-499"><a href="#entity_repr_owner_based-499"><span class="linenos">499</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">):</span>
</span><span id="entity_repr_owner_based-500"><a href="#entity_repr_owner_based-500"><span class="linenos">500</span></a>        <span class="n">_entity_repr_limited</span> <span class="o">=</span> <span class="n">entity_repr_limited_try_qualname</span>
</span><span id="entity_repr_owner_based-501"><a href="#entity_repr_owner_based-501"><span class="linenos">501</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_owner_based-502"><a href="#entity_repr_owner_based-502"><span class="linenos">502</span></a>        <span class="n">_entity_repr_limited</span> <span class="o">=</span> <span class="n">entity_repr_limited</span>
</span><span id="entity_repr_owner_based-503"><a href="#entity_repr_owner_based-503"><span class="linenos">503</span></a>    
</span><span id="entity_repr_owner_based-504"><a href="#entity_repr_owner_based-504"><span class="linenos">504</span></a>    <span class="k">if</span> <span class="n">owner_repr</span><span class="p">:</span>
</span><span id="entity_repr_owner_based-505"><a href="#entity_repr_owner_based-505"><span class="linenos">505</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">_entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span><span class="w"> </span><span class="n">formatted</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="entity_repr_owner_based-506"><a href="#entity_repr_owner_based-506"><span class="linenos">506</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr_owner_based-507"><a href="#entity_repr_owner_based-507"><span class="linenos">507</span></a>        <span class="k">return</span> <span class="n">_entity_repr_limited</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_repr">
                            <input id="entity_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_repr-510"><a href="#entity_repr-510"><span class="linenos">510</span></a><span class="k">def</span> <span class="nf">entity_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="entity_repr-511"><a href="#entity_repr-511"><span class="linenos">511</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="entity_repr-512"><a href="#entity_repr-512"><span class="linenos">512</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="entity_repr-513"><a href="#entity_repr-513"><span class="linenos">513</span></a>    
</span><span id="entity_repr-514"><a href="#entity_repr-514"><span class="linenos">514</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_repr-515"><a href="#entity_repr-515"><span class="linenos">515</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="entity_repr-516"><a href="#entity_repr-516"><span class="linenos">516</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">module</span><span class="p">)</span>
</span><span id="entity_repr-517"><a href="#entity_repr-517"><span class="linenos">517</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr-518"><a href="#entity_repr-518"><span class="linenos">518</span></a>        <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_owner_repr</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
</span><span id="entity_repr-519"><a href="#entity_repr-519"><span class="linenos">519</span></a>    
</span><span id="entity_repr-520"><a href="#entity_repr-520"><span class="linenos">520</span></a>    <span class="k">if</span> <span class="n">owner_repr</span><span class="p">:</span>
</span><span id="entity_repr-521"><a href="#entity_repr-521"><span class="linenos">521</span></a>        <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span><span class="w"> </span><span class="n">formatted</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span>
</span><span id="entity_repr-522"><a href="#entity_repr-522"><span class="linenos">522</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_repr-523"><a href="#entity_repr-523"><span class="linenos">523</span></a>        <span class="k">return</span> <span class="n">entity_repr_limited_try_qualname</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">formatted</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_properties">
                            <input id="entity_properties-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_properties</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="entity_properties-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_properties"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_properties-526"><a href="#entity_properties-526"><span class="linenos">526</span></a><span class="k">def</span> <span class="nf">entity_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="entity_properties-527"><a href="#entity_properties-527"><span class="linenos">527</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="entity_properties-528"><a href="#entity_properties-528"><span class="linenos">528</span></a><span class="sd">    Example:</span>
</span><span id="entity_properties-529"><a href="#entity_properties-529"><span class="linenos">529</span></a><span class="sd">        from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest</span>
</span><span id="entity_properties-530"><a href="#entity_properties-530"><span class="linenos">530</span></a><span class="sd">        from cengal.introspection.inspect import entity_properties</span>
</span><span id="entity_properties-531"><a href="#entity_properties-531"><span class="linenos">531</span></a><span class="sd">        </span>
</span><span id="entity_properties-532"><a href="#entity_properties-532"><span class="linenos">532</span></a><span class="sd">        print(entity_properties(WaitCoroRequest))</span>
</span><span id="entity_properties-533"><a href="#entity_properties-533"><span class="linenos">533</span></a><span class="sd">        &gt;&gt; {&#39;__weakref__&#39;, &#39;put_list&#39;, &#39;fastest&#39;, &#39;atomic&#39;, &#39;list&#39;, &#39;single&#39;, &#39;put_fastest&#39;, &#39;_save&#39;, &#39;put_single&#39;, &#39;put_atomic&#39;}</span>
</span><span id="entity_properties-534"><a href="#entity_properties-534"><span class="linenos">534</span></a>
</span><span id="entity_properties-535"><a href="#entity_properties-535"><span class="linenos">535</span></a>
</span><span id="entity_properties-536"><a href="#entity_properties-536"><span class="linenos">536</span></a><span class="sd">        print(entity_properties(WaitCoroRequest()))</span>
</span><span id="entity_properties-537"><a href="#entity_properties-537"><span class="linenos">537</span></a><span class="sd">        &gt;&gt; {&#39;result_required&#39;, &#39;args&#39;, &#39;tree&#39;, &#39;kill_on_timeout&#39;, &#39;timeout&#39;, &#39;request_type&#39;, &#39;kwargs&#39;, &#39;provide_to_request_handler&#39;}</span>
</span><span id="entity_properties-538"><a href="#entity_properties-538"><span class="linenos">538</span></a>
</span><span id="entity_properties-539"><a href="#entity_properties-539"><span class="linenos">539</span></a>
</span><span id="entity_properties-540"><a href="#entity_properties-540"><span class="linenos">540</span></a><span class="sd">        def my_func(a, b, *, c, d):</span>
</span><span id="entity_properties-541"><a href="#entity_properties-541"><span class="linenos">541</span></a><span class="sd">            return a + b + c + d</span>
</span><span id="entity_properties-542"><a href="#entity_properties-542"><span class="linenos">542</span></a>
</span><span id="entity_properties-543"><a href="#entity_properties-543"><span class="linenos">543</span></a><span class="sd">        my_func.my_property = 2</span>
</span><span id="entity_properties-544"><a href="#entity_properties-544"><span class="linenos">544</span></a>
</span><span id="entity_properties-545"><a href="#entity_properties-545"><span class="linenos">545</span></a><span class="sd">        print(entity_properties(my_func))</span>
</span><span id="entity_properties-546"><a href="#entity_properties-546"><span class="linenos">546</span></a><span class="sd">        &gt;&gt; {&#39;my_property&#39;}</span>
</span><span id="entity_properties-547"><a href="#entity_properties-547"><span class="linenos">547</span></a>
</span><span id="entity_properties-548"><a href="#entity_properties-548"><span class="linenos">548</span></a>
</span><span id="entity_properties-549"><a href="#entity_properties-549"><span class="linenos">549</span></a><span class="sd">    Args:</span>
</span><span id="entity_properties-550"><a href="#entity_properties-550"><span class="linenos">550</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="entity_properties-551"><a href="#entity_properties-551"><span class="linenos">551</span></a>
</span><span id="entity_properties-552"><a href="#entity_properties-552"><span class="linenos">552</span></a><span class="sd">    Returns:</span>
</span><span id="entity_properties-553"><a href="#entity_properties-553"><span class="linenos">553</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="entity_properties-554"><a href="#entity_properties-554"><span class="linenos">554</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="entity_properties-555"><a href="#entity_properties-555"><span class="linenos">555</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="entity_properties-556"><a href="#entity_properties-556"><span class="linenos">556</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="entity_properties-557"><a href="#entity_properties-557"><span class="linenos">557</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span>
</span></pre></div>


            <div class="docstring"><p>Example:
    from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest
    from cengal.introspection.inspect import entity_properties</p>

<pre><code>print(entity_properties(WaitCoroRequest))
&gt;&gt; {'__weakref__', 'put_list', 'fastest', 'atomic', 'list', 'single', 'put_fastest', '_save', 'put_single', 'put_atomic'}


print(entity_properties(WaitCoroRequest()))
&gt;&gt; {'result_required', 'args', 'tree', 'kill_on_timeout', 'timeout', 'request_type', 'kwargs', 'provide_to_request_handler'}


def my_func(a, b, *, c, d):
    return a + b + c + d

my_func.my_property = 2

print(entity_properties(my_func))
&gt;&gt; {'my_property'}
</code></pre>

<p>Args:
    entity (_type_): _description_</p>

<p>Returns:
    Set[str]: _description_</p>
</div>


                </section>
                <section id="entity_properties_values">
                            <input id="entity_properties_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_properties_values</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="entity_properties_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_properties_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_properties_values-560"><a href="#entity_properties_values-560"><span class="linenos">560</span></a><span class="k">def</span> <span class="nf">entity_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="entity_properties_values-561"><a href="#entity_properties_values-561"><span class="linenos">561</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="entity_properties_values-562"><a href="#entity_properties_values-562"><span class="linenos">562</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">entity_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="entity_properties_values-563"><a href="#entity_properties_values-563"><span class="linenos">563</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="entity_properties_values-564"><a href="#entity_properties_values-564"><span class="linenos">564</span></a>    
</span><span id="entity_properties_values-565"><a href="#entity_properties_values-565"><span class="linenos">565</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="class_properties">
                            <input id="class_properties-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span></span><span class="return-annotation">) -> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties-568"><a href="#class_properties-568"><span class="linenos">568</span></a><span class="k">def</span> <span class="nf">class_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="class_properties-569"><a href="#class_properties-569"><span class="linenos">569</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="class_properties-570"><a href="#class_properties-570"><span class="linenos">570</span></a><span class="sd">    Example:</span>
</span><span id="class_properties-571"><a href="#class_properties-571"><span class="linenos">571</span></a>
</span><span id="class_properties-572"><a href="#class_properties-572"><span class="linenos">572</span></a><span class="sd">    Args:</span>
</span><span id="class_properties-573"><a href="#class_properties-573"><span class="linenos">573</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="class_properties-574"><a href="#class_properties-574"><span class="linenos">574</span></a>
</span><span id="class_properties-575"><a href="#class_properties-575"><span class="linenos">575</span></a><span class="sd">    Returns:</span>
</span><span id="class_properties-576"><a href="#class_properties-576"><span class="linenos">576</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="class_properties-577"><a href="#class_properties-577"><span class="linenos">577</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="class_properties-578"><a href="#class_properties-578"><span class="linenos">578</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="class_properties-579"><a href="#class_properties-579"><span class="linenos">579</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="class_properties-580"><a href="#class_properties-580"><span class="linenos">580</span></a>    <span class="n">mro</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmro</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="class_properties-581"><a href="#class_properties-581"><span class="linenos">581</span></a>    <span class="n">base_members</span><span class="p">:</span> <span class="n">Set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="class_properties-582"><a href="#class_properties-582"><span class="linenos">582</span></a>    <span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="n">mro</span><span class="p">:</span>
</span><span id="class_properties-583"><a href="#class_properties-583"><span class="linenos">583</span></a>        <span class="k">if</span> <span class="n">base</span> <span class="ow">is</span> <span class="n">entity</span><span class="p">:</span>
</span><span id="class_properties-584"><a href="#class_properties-584"><span class="linenos">584</span></a>            <span class="k">continue</span>
</span><span id="class_properties-585"><a href="#class_properties-585"><span class="linenos">585</span></a>        
</span><span id="class_properties-586"><a href="#class_properties-586"><span class="linenos">586</span></a>        <span class="n">base_members</span> <span class="o">|=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">base</span><span class="p">))</span>
</span><span id="class_properties-587"><a href="#class_properties-587"><span class="linenos">587</span></a>    
</span><span id="class_properties-588"><a href="#class_properties-588"><span class="linenos">588</span></a>    <span class="k">return</span> <span class="p">(</span><span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span><span class="p">)</span> <span class="o">-</span> <span class="n">base_members</span>
</span></pre></div>


            <div class="docstring"><p>Example:</p>

<p>Args:
    entity (_type_): _description_</p>

<p>Returns:
    Set[str]: _description_</p>
</div>


                </section>
                <section id="class_properties_values">
                            <input id="class_properties_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties_values</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties_values-591"><a href="#class_properties_values-591"><span class="linenos">591</span></a><span class="k">def</span> <span class="nf">class_properties_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="class_properties_values-592"><a href="#class_properties_values-592"><span class="linenos">592</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="class_properties_values-593"><a href="#class_properties_values-593"><span class="linenos">593</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="class_properties_values-594"><a href="#class_properties_values-594"><span class="linenos">594</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="class_properties_values-595"><a href="#class_properties_values-595"><span class="linenos">595</span></a>    
</span><span id="class_properties_values-596"><a href="#class_properties_values-596"><span class="linenos">596</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="class_properties_withot_object">
                            <input id="class_properties_withot_object-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties_withot_object</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span></span><span class="return-annotation">) -> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties_withot_object-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties_withot_object"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties_withot_object-599"><a href="#class_properties_withot_object-599"><span class="linenos">599</span></a><span class="k">def</span> <span class="nf">class_properties_withot_object</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="class_properties_withot_object-600"><a href="#class_properties_withot_object-600"><span class="linenos">600</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="class_properties_withot_object-601"><a href="#class_properties_withot_object-601"><span class="linenos">601</span></a><span class="sd">    Example:</span>
</span><span id="class_properties_withot_object-602"><a href="#class_properties_withot_object-602"><span class="linenos">602</span></a>
</span><span id="class_properties_withot_object-603"><a href="#class_properties_withot_object-603"><span class="linenos">603</span></a><span class="sd">    Args:</span>
</span><span id="class_properties_withot_object-604"><a href="#class_properties_withot_object-604"><span class="linenos">604</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="class_properties_withot_object-605"><a href="#class_properties_withot_object-605"><span class="linenos">605</span></a>
</span><span id="class_properties_withot_object-606"><a href="#class_properties_withot_object-606"><span class="linenos">606</span></a><span class="sd">    Returns:</span>
</span><span id="class_properties_withot_object-607"><a href="#class_properties_withot_object-607"><span class="linenos">607</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="class_properties_withot_object-608"><a href="#class_properties_withot_object-608"><span class="linenos">608</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="class_properties_withot_object-609"><a href="#class_properties_withot_object-609"><span class="linenos">609</span></a>    <span class="n">object_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">object</span><span class="p">))</span>
</span><span id="class_properties_withot_object-610"><a href="#class_properties_withot_object-610"><span class="linenos">610</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="n">entity</span><span class="p">))</span>
</span><span id="class_properties_withot_object-611"><a href="#class_properties_withot_object-611"><span class="linenos">611</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">object_type_items</span>
</span></pre></div>


            <div class="docstring"><p>Example:</p>

<p>Args:
    entity (_type_): _description_</p>

<p>Returns:
    Set[str]: _description_</p>
</div>


                </section>
                <section id="class_properties_withot_object_values">
                            <input id="class_properties_withot_object_values-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties_withot_object_values</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties_withot_object_values-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties_withot_object_values"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties_withot_object_values-614"><a href="#class_properties_withot_object_values-614"><span class="linenos">614</span></a><span class="k">def</span> <span class="nf">class_properties_withot_object_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="class_properties_withot_object_values-615"><a href="#class_properties_withot_object_values-615"><span class="linenos">615</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="class_properties_withot_object_values-616"><a href="#class_properties_withot_object_values-616"><span class="linenos">616</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties_withot_object</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="class_properties_withot_object_values-617"><a href="#class_properties_withot_object_values-617"><span class="linenos">617</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="class_properties_withot_object_values-618"><a href="#class_properties_withot_object_values-618"><span class="linenos">618</span></a>    
</span><span id="class_properties_withot_object_values-619"><a href="#class_properties_withot_object_values-619"><span class="linenos">619</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="class_properties_including_overrided">
                            <input id="class_properties_including_overrided-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties_including_overrided</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Type</span></span><span class="return-annotation">) -> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties_including_overrided-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties_including_overrided"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties_including_overrided-622"><a href="#class_properties_including_overrided-622"><span class="linenos">622</span></a><span class="k">def</span> <span class="nf">class_properties_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Type</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
</span><span id="class_properties_including_overrided-623"><a href="#class_properties_including_overrided-623"><span class="linenos">623</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="class_properties_including_overrided-624"><a href="#class_properties_including_overrided-624"><span class="linenos">624</span></a><span class="sd">    Example:</span>
</span><span id="class_properties_including_overrided-625"><a href="#class_properties_including_overrided-625"><span class="linenos">625</span></a>
</span><span id="class_properties_including_overrided-626"><a href="#class_properties_including_overrided-626"><span class="linenos">626</span></a><span class="sd">    Args:</span>
</span><span id="class_properties_including_overrided-627"><a href="#class_properties_including_overrided-627"><span class="linenos">627</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="class_properties_including_overrided-628"><a href="#class_properties_including_overrided-628"><span class="linenos">628</span></a>
</span><span id="class_properties_including_overrided-629"><a href="#class_properties_including_overrided-629"><span class="linenos">629</span></a><span class="sd">    Returns:</span>
</span><span id="class_properties_including_overrided-630"><a href="#class_properties_including_overrided-630"><span class="linenos">630</span></a><span class="sd">        Set[str]: _description_</span>
</span><span id="class_properties_including_overrided-631"><a href="#class_properties_including_overrided-631"><span class="linenos">631</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="class_properties_including_overrided-632"><a href="#class_properties_including_overrided-632"><span class="linenos">632</span></a>    <span class="n">entity_type_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">dir</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)))</span>
</span><span id="class_properties_including_overrided-633"><a href="#class_properties_including_overrided-633"><span class="linenos">633</span></a>    <span class="n">entity_items</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>
</span><span id="class_properties_including_overrided-634"><a href="#class_properties_including_overrided-634"><span class="linenos">634</span></a>    <span class="k">return</span> <span class="n">entity_items</span> <span class="o">-</span> <span class="n">entity_type_items</span>
</span></pre></div>


            <div class="docstring"><p>Example:</p>

<p>Args:
    entity (_type_): _description_</p>

<p>Returns:
    Set[str]: _description_</p>
</div>


                </section>
                <section id="class_properties_values_including_overrided">
                            <input id="class_properties_values_including_overrided-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">class_properties_values_including_overrided</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="class_properties_values_including_overrided-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#class_properties_values_including_overrided"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="class_properties_values_including_overrided-637"><a href="#class_properties_values_including_overrided-637"><span class="linenos">637</span></a><span class="k">def</span> <span class="nf">class_properties_values_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="class_properties_values_including_overrided-638"><a href="#class_properties_values_including_overrided-638"><span class="linenos">638</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="class_properties_values_including_overrided-639"><a href="#class_properties_values_including_overrided-639"><span class="linenos">639</span></a>    <span class="k">for</span> <span class="n">property_name</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">class_properties_including_overrided</span><span class="p">(</span><span class="n">entity</span><span class="p">)):</span>
</span><span id="class_properties_values_including_overrided-640"><a href="#class_properties_values_including_overrided-640"><span class="linenos">640</span></a>        <span class="n">result</span><span class="p">[</span><span class="n">property_name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">property_name</span><span class="p">)</span>
</span><span id="class_properties_values_including_overrided-641"><a href="#class_properties_values_including_overrided-641"><span class="linenos">641</span></a>    
</span><span id="class_properties_values_including_overrided-642"><a href="#class_properties_values_including_overrided-642"><span class="linenos">642</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="intro_frame_repr_limited">
                            <input id="intro_frame_repr_limited-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_frame_repr_limited</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">frame_instance</span>, </span><span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="intro_frame_repr_limited-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_frame_repr_limited"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_frame_repr_limited-645"><a href="#intro_frame_repr_limited-645"><span class="linenos">645</span></a><span class="k">def</span> <span class="nf">intro_frame_repr_limited</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="intro_frame_repr_limited-646"><a href="#intro_frame_repr_limited-646"><span class="linenos">646</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span><span class="p">)</span>
</span><span id="intro_frame_repr_limited-647"><a href="#intro_frame_repr_limited-647"><span class="linenos">647</span></a>    <span class="n">params_with_values</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="intro_frame_repr_limited-648"><a href="#intro_frame_repr_limited-648"><span class="linenos">648</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="intro_frame_repr_limited-649"><a href="#intro_frame_repr_limited-649"><span class="linenos">649</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span></pre></div>


    

                </section>
                <section id="intro_frame_repr">
                            <input id="intro_frame_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_frame_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">frame_instance</span>, </span><span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="intro_frame_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_frame_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_frame_repr-652"><a href="#intro_frame_repr-652"><span class="linenos">652</span></a><span class="k">def</span> <span class="nf">intro_frame_repr</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">,</span> <span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="intro_frame_repr-653"><a href="#intro_frame_repr-653"><span class="linenos">653</span></a>    <span class="n">code</span> <span class="o">=</span> <span class="n">frame_instance</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="intro_frame_repr-654"><a href="#intro_frame_repr-654"><span class="linenos">654</span></a>    <span class="n">func_name</span> <span class="o">=</span> <span class="n">code_name</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="intro_frame_repr-655"><a href="#intro_frame_repr-655"><span class="linenos">655</span></a>    <span class="n">module</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getmodule</span><span class="p">(</span><span class="n">code</span><span class="p">)</span>
</span><span id="intro_frame_repr-656"><a href="#intro_frame_repr-656"><span class="linenos">656</span></a>    <span class="n">owner_repr</span> <span class="o">=</span> <span class="n">normalized_code_owner_repr</span><span class="p">(</span><span class="n">code</span><span class="p">,</span> <span class="n">module</span><span class="p">)</span>
</span><span id="intro_frame_repr-657"><a href="#intro_frame_repr-657"><span class="linenos">657</span></a>    <span class="n">params_with_values</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">frame_instance</span><span class="p">)</span>
</span><span id="intro_frame_repr-658"><a href="#intro_frame_repr-658"><span class="linenos">658</span></a>    <span class="n">function_params_str</span> <span class="o">=</span> <span class="n">code_params_with_values_to_signature</span><span class="p">(</span><span class="n">params_with_values</span><span class="p">,</span> <span class="n">verbose</span><span class="p">)</span>
</span><span id="intro_frame_repr-659"><a href="#intro_frame_repr-659"><span class="linenos">659</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">owner_repr</span><span class="si">}</span><span class="s1">.</span><span class="si">{</span><span class="n">func_name</span><span class="si">}</span><span class="s1">(</span><span class="si">{</span><span class="n">function_params_str</span><span class="si">}</span><span class="s1">)&#39;</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_repr_limited">
                            <input id="intro_func_repr_limited-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_repr_limited</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="intro_func_repr_limited-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_repr_limited"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_repr_limited-662"><a href="#intro_func_repr_limited-662"><span class="linenos">662</span></a><span class="k">def</span> <span class="nf">intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="intro_func_repr_limited-663"><a href="#intro_func_repr_limited-663"><span class="linenos">663</span></a>    <span class="k">return</span> <span class="n">intro_frame_repr_limited</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">verbose</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="print_intro_func_repr_limited">
                            <input id="print_intro_func_repr_limited-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">print_intro_func_repr_limited</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="print_intro_func_repr_limited-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#print_intro_func_repr_limited"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="print_intro_func_repr_limited-666"><a href="#print_intro_func_repr_limited-666"><span class="linenos">666</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="print_intro_func_repr_limited-667"><a href="#print_intro_func_repr_limited-667"><span class="linenos">667</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="pifrl">
                            <input id="pifrl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">pifrl</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="pifrl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#pifrl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="pifrl-666"><a href="#pifrl-666"><span class="linenos">666</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="pifrl-667"><a href="#pifrl-667"><span class="linenos">667</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr_limited</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="intro_func_repr">
                            <input id="intro_func_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">intro_func_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="intro_func_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#intro_func_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="intro_func_repr-673"><a href="#intro_func_repr-673"><span class="linenos">673</span></a><span class="k">def</span> <span class="nf">intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="intro_func_repr-674"><a href="#intro_func_repr-674"><span class="linenos">674</span></a>    <span class="k">return</span> <span class="n">intro_frame_repr</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">),</span> <span class="n">verbose</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="print_intro_func_repr">
                            <input id="print_intro_func_repr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">print_intro_func_repr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="print_intro_func_repr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#print_intro_func_repr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="print_intro_func_repr-677"><a href="#print_intro_func_repr-677"><span class="linenos">677</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="print_intro_func_repr-678"><a href="#print_intro_func_repr-678"><span class="linenos">678</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="pifr">
                            <input id="pifr-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">pifr</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="pifr-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#pifr"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="pifr-677"><a href="#pifr-677"><span class="linenos">677</span></a><span class="k">def</span> <span class="nf">print_intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="pifr-678"><a href="#pifr-678"><span class="linenos">678</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">intro_func_repr</span><span class="p">(</span><span class="n">verbose</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="get_str_of_data_info">
                            <input id="get_str_of_data_info-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_str_of_data_info</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_str_of_data_info-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_str_of_data_info"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_str_of_data_info-684"><a href="#get_str_of_data_info-684"><span class="linenos">684</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="get_str_of_data_info-685"><a href="#get_str_of_data_info-685"><span class="linenos">685</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns string with data info: type and value</span>
</span><span id="get_str_of_data_info-686"><a href="#get_str_of_data_info-686"><span class="linenos">686</span></a>
</span><span id="get_str_of_data_info-687"><a href="#get_str_of_data_info-687"><span class="linenos">687</span></a><span class="sd">    Args:</span>
</span><span id="get_str_of_data_info-688"><a href="#get_str_of_data_info-688"><span class="linenos">688</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="get_str_of_data_info-689"><a href="#get_str_of_data_info-689"><span class="linenos">689</span></a>
</span><span id="get_str_of_data_info-690"><a href="#get_str_of_data_info-690"><span class="linenos">690</span></a><span class="sd">    Returns:</span>
</span><span id="get_str_of_data_info-691"><a href="#get_str_of_data_info-691"><span class="linenos">691</span></a><span class="sd">        _type_: _description_</span>
</span><span id="get_str_of_data_info-692"><a href="#get_str_of_data_info-692"><span class="linenos">692</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="get_str_of_data_info-693"><a href="#get_str_of_data_info-693"><span class="linenos">693</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


            <div class="docstring"><p>Returns string with data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="gsodi">
                            <input id="gsodi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gsodi</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="gsodi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gsodi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gsodi-684"><a href="#gsodi-684"><span class="linenos">684</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="gsodi-685"><a href="#gsodi-685"><span class="linenos">685</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns string with data info: type and value</span>
</span><span id="gsodi-686"><a href="#gsodi-686"><span class="linenos">686</span></a>
</span><span id="gsodi-687"><a href="#gsodi-687"><span class="linenos">687</span></a><span class="sd">    Args:</span>
</span><span id="gsodi-688"><a href="#gsodi-688"><span class="linenos">688</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="gsodi-689"><a href="#gsodi-689"><span class="linenos">689</span></a>
</span><span id="gsodi-690"><a href="#gsodi-690"><span class="linenos">690</span></a><span class="sd">    Returns:</span>
</span><span id="gsodi-691"><a href="#gsodi-691"><span class="linenos">691</span></a><span class="sd">        _type_: _description_</span>
</span><span id="gsodi-692"><a href="#gsodi-692"><span class="linenos">692</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="gsodi-693"><a href="#gsodi-693"><span class="linenos">693</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


            <div class="docstring"><p>Returns string with data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="get_multistr_of_data_info">
                            <input id="get_multistr_of_data_info-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_multistr_of_data_info</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">data</span>,</span><span class="param">	<span class="n">shift_num</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_multistr_of_data_info-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_multistr_of_data_info"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_multistr_of_data_info-699"><a href="#get_multistr_of_data_info-699"><span class="linenos">699</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="get_multistr_of_data_info-700"><a href="#get_multistr_of_data_info-700"><span class="linenos">700</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data info: type and value</span>
</span><span id="get_multistr_of_data_info-701"><a href="#get_multistr_of_data_info-701"><span class="linenos">701</span></a>
</span><span id="get_multistr_of_data_info-702"><a href="#get_multistr_of_data_info-702"><span class="linenos">702</span></a><span class="sd">    Args:</span>
</span><span id="get_multistr_of_data_info-703"><a href="#get_multistr_of_data_info-703"><span class="linenos">703</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="get_multistr_of_data_info-704"><a href="#get_multistr_of_data_info-704"><span class="linenos">704</span></a>
</span><span id="get_multistr_of_data_info-705"><a href="#get_multistr_of_data_info-705"><span class="linenos">705</span></a><span class="sd">    Returns:</span>
</span><span id="get_multistr_of_data_info-706"><a href="#get_multistr_of_data_info-706"><span class="linenos">706</span></a><span class="sd">        _type_: _description_</span>
</span><span id="get_multistr_of_data_info-707"><a href="#get_multistr_of_data_info-707"><span class="linenos">707</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="get_multistr_of_data_info-708"><a href="#get_multistr_of_data_info-708"><span class="linenos">708</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="get_multistr_of_data_info-709"><a href="#get_multistr_of_data_info-709"><span class="linenos">709</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="get_multistr_of_data_info-710"><a href="#get_multistr_of_data_info-710"><span class="linenos">710</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="get_multistr_of_data_info-711"><a href="#get_multistr_of_data_info-711"><span class="linenos">711</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="get_multistr_of_data_info-712"><a href="#get_multistr_of_data_info-712"><span class="linenos">712</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="get_multistr_of_data_info-713"><a href="#get_multistr_of_data_info-713"><span class="linenos">713</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="get_multistr_of_data_info-714"><a href="#get_multistr_of_data_info-714"><span class="linenos">714</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="se">\n</span><span class="si">{</span><span class="n">data_str</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


            <div class="docstring"><p>Returns multiline string with data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="gmsodi">
                            <input id="gmsodi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gmsodi</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">data</span>,</span><span class="param">	<span class="n">shift_num</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="gmsodi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gmsodi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gmsodi-699"><a href="#gmsodi-699"><span class="linenos">699</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="gmsodi-700"><a href="#gmsodi-700"><span class="linenos">700</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data info: type and value</span>
</span><span id="gmsodi-701"><a href="#gmsodi-701"><span class="linenos">701</span></a>
</span><span id="gmsodi-702"><a href="#gmsodi-702"><span class="linenos">702</span></a><span class="sd">    Args:</span>
</span><span id="gmsodi-703"><a href="#gmsodi-703"><span class="linenos">703</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="gmsodi-704"><a href="#gmsodi-704"><span class="linenos">704</span></a>
</span><span id="gmsodi-705"><a href="#gmsodi-705"><span class="linenos">705</span></a><span class="sd">    Returns:</span>
</span><span id="gmsodi-706"><a href="#gmsodi-706"><span class="linenos">706</span></a><span class="sd">        _type_: _description_</span>
</span><span id="gmsodi-707"><a href="#gmsodi-707"><span class="linenos">707</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="gmsodi-708"><a href="#gmsodi-708"><span class="linenos">708</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="gmsodi-709"><a href="#gmsodi-709"><span class="linenos">709</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="gmsodi-710"><a href="#gmsodi-710"><span class="linenos">710</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="gmsodi-711"><a href="#gmsodi-711"><span class="linenos">711</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="gmsodi-712"><a href="#gmsodi-712"><span class="linenos">712</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="gmsodi-713"><a href="#gmsodi-713"><span class="linenos">713</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="gmsodi-714"><a href="#gmsodi-714"><span class="linenos">714</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="se">\n</span><span class="si">{</span><span class="n">data_str</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


            <div class="docstring"><p>Returns multiline string with data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="get_multistr_of_data_value">
                            <input id="get_multistr_of_data_value-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_multistr_of_data_value</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">data</span>,</span><span class="param">	<span class="n">shift_num</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_multistr_of_data_value-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_multistr_of_data_value"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_multistr_of_data_value-720"><a href="#get_multistr_of_data_value-720"><span class="linenos">720</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_value</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="get_multistr_of_data_value-721"><a href="#get_multistr_of_data_value-721"><span class="linenos">721</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data value</span>
</span><span id="get_multistr_of_data_value-722"><a href="#get_multistr_of_data_value-722"><span class="linenos">722</span></a>
</span><span id="get_multistr_of_data_value-723"><a href="#get_multistr_of_data_value-723"><span class="linenos">723</span></a><span class="sd">    Args:</span>
</span><span id="get_multistr_of_data_value-724"><a href="#get_multistr_of_data_value-724"><span class="linenos">724</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="get_multistr_of_data_value-725"><a href="#get_multistr_of_data_value-725"><span class="linenos">725</span></a>
</span><span id="get_multistr_of_data_value-726"><a href="#get_multistr_of_data_value-726"><span class="linenos">726</span></a><span class="sd">    Returns:</span>
</span><span id="get_multistr_of_data_value-727"><a href="#get_multistr_of_data_value-727"><span class="linenos">727</span></a><span class="sd">        _type_: _description_</span>
</span><span id="get_multistr_of_data_value-728"><a href="#get_multistr_of_data_value-728"><span class="linenos">728</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="get_multistr_of_data_value-729"><a href="#get_multistr_of_data_value-729"><span class="linenos">729</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="get_multistr_of_data_value-730"><a href="#get_multistr_of_data_value-730"><span class="linenos">730</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="get_multistr_of_data_value-731"><a href="#get_multistr_of_data_value-731"><span class="linenos">731</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="get_multistr_of_data_value-732"><a href="#get_multistr_of_data_value-732"><span class="linenos">732</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="get_multistr_of_data_value-733"><a href="#get_multistr_of_data_value-733"><span class="linenos">733</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="get_multistr_of_data_value-734"><a href="#get_multistr_of_data_value-734"><span class="linenos">734</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="get_multistr_of_data_value-735"><a href="#get_multistr_of_data_value-735"><span class="linenos">735</span></a>    <span class="k">return</span> <span class="n">data_str</span>
</span></pre></div>


            <div class="docstring"><p>Returns multiline string with data value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="gmsodv">
                            <input id="gmsodv-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gmsodv</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">data</span>,</span><span class="param">	<span class="n">shift_num</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="gmsodv-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gmsodv"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gmsodv-720"><a href="#gmsodv-720"><span class="linenos">720</span></a><span class="k">def</span> <span class="nf">get_multistr_of_data_value</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">shift_num</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">shift_char</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\t</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="gmsodv-721"><a href="#gmsodv-721"><span class="linenos">721</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Returns multiline string with data value</span>
</span><span id="gmsodv-722"><a href="#gmsodv-722"><span class="linenos">722</span></a>
</span><span id="gmsodv-723"><a href="#gmsodv-723"><span class="linenos">723</span></a><span class="sd">    Args:</span>
</span><span id="gmsodv-724"><a href="#gmsodv-724"><span class="linenos">724</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="gmsodv-725"><a href="#gmsodv-725"><span class="linenos">725</span></a>
</span><span id="gmsodv-726"><a href="#gmsodv-726"><span class="linenos">726</span></a><span class="sd">    Returns:</span>
</span><span id="gmsodv-727"><a href="#gmsodv-727"><span class="linenos">727</span></a><span class="sd">        _type_: _description_</span>
</span><span id="gmsodv-728"><a href="#gmsodv-728"><span class="linenos">728</span></a><span class="sd">    &quot;&quot;&quot;</span>
</span><span id="gmsodv-729"><a href="#gmsodv-729"><span class="linenos">729</span></a>    <span class="n">shift_num</span> <span class="o">=</span> <span class="n">shift_num</span> <span class="ow">or</span> <span class="mi">0</span>
</span><span id="gmsodv-730"><a href="#gmsodv-730"><span class="linenos">730</span></a>    <span class="n">shift_str</span> <span class="o">=</span> <span class="n">shift_char</span> <span class="o">*</span> <span class="n">shift_num</span>
</span><span id="gmsodv-731"><a href="#gmsodv-731"><span class="linenos">731</span></a>    <span class="kn">from</span> <span class="nn">pprint</span> <span class="kn">import</span> <span class="n">pformat</span>
</span><span id="gmsodv-732"><a href="#gmsodv-732"><span class="linenos">732</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="n">pformat</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="gmsodv-733"><a href="#gmsodv-733"><span class="linenos">733</span></a>    <span class="n">data_str_lines</span> <span class="o">=</span> <span class="n">data_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="gmsodv-734"><a href="#gmsodv-734"><span class="linenos">734</span></a>    <span class="n">data_str</span> <span class="o">=</span> <span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">shift_str</span><span class="si">}{</span><span class="n">line</span><span class="si">}</span><span class="s1">&#39;</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">data_str_lines</span><span class="p">])</span>
</span><span id="gmsodv-735"><a href="#gmsodv-735"><span class="linenos">735</span></a>    <span class="k">return</span> <span class="n">data_str</span>
</span></pre></div>


            <div class="docstring"><p>Returns multiline string with data value</p>

<p>Args:
    data (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="print_data_info">
                            <input id="print_data_info-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">print_data_info</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="print_data_info-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#print_data_info"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="print_data_info-741"><a href="#print_data_info-741"><span class="linenos">741</span></a><span class="k">def</span> <span class="nf">print_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="print_data_info-742"><a href="#print_data_info-742"><span class="linenos">742</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Print data info: type and value</span>
</span><span id="print_data_info-743"><a href="#print_data_info-743"><span class="linenos">743</span></a>
</span><span id="print_data_info-744"><a href="#print_data_info-744"><span class="linenos">744</span></a><span class="sd">    Args:</span>
</span><span id="print_data_info-745"><a href="#print_data_info-745"><span class="linenos">745</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="print_data_info-746"><a href="#print_data_info-746"><span class="linenos">746</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="print_data_info-747"><a href="#print_data_info-747"><span class="linenos">747</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</span></pre></div>


            <div class="docstring"><p>Print data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>
</div>


                </section>
                <section id="pdi">
                            <input id="pdi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">pdi</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="pdi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#pdi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="pdi-741"><a href="#pdi-741"><span class="linenos">741</span></a><span class="k">def</span> <span class="nf">print_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
</span><span id="pdi-742"><a href="#pdi-742"><span class="linenos">742</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Print data info: type and value</span>
</span><span id="pdi-743"><a href="#pdi-743"><span class="linenos">743</span></a>
</span><span id="pdi-744"><a href="#pdi-744"><span class="linenos">744</span></a><span class="sd">    Args:</span>
</span><span id="pdi-745"><a href="#pdi-745"><span class="linenos">745</span></a><span class="sd">        data (_type_): _description_</span>
</span><span id="pdi-746"><a href="#pdi-746"><span class="linenos">746</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="pdi-747"><a href="#pdi-747"><span class="linenos">747</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
</span></pre></div>


            <div class="docstring"><p>Print data info: type and value</p>

<p>Args:
    data (_type_): _description_</p>
</div>


                </section>
                <section id="get_str_of_data_info_named">
                            <input id="get_str_of_data_info_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_str_of_data_info_named</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_str_of_data_info_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_str_of_data_info_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_str_of_data_info_named-753"><a href="#get_str_of_data_info_named-753"><span class="linenos">753</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="get_str_of_data_info_named-754"><a href="#get_str_of_data_info_named-754"><span class="linenos">754</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;&lt;</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">&gt;&gt; type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


    

                </section>
                <section id="gsodin">
                            <input id="gsodin-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gsodin</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="gsodin-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gsodin"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gsodin-753"><a href="#gsodin-753"><span class="linenos">753</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="gsodin-754"><a href="#gsodin-754"><span class="linenos">754</span></a>    <span class="k">return</span> <span class="sa">f</span><span class="s1">&#39;&lt;&lt;</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s1">&gt;&gt; type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="si">}</span><span class="s1">; value: </span><span class="si">{</span><span class="n">data</span><span class="si">}</span><span class="s1">&#39;</span>
</span></pre></div>


    

                </section>
                <section id="print_data_info_named">
                            <input id="print_data_info_named-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">print_data_info_named</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="print_data_info_named-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#print_data_info_named"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="print_data_info_named-760"><a href="#print_data_info_named-760"><span class="linenos">760</span></a><span class="k">def</span> <span class="nf">print_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="print_data_info_named-761"><a href="#print_data_info_named-761"><span class="linenos">761</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="pdin">
                            <input id="pdin-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">pdin</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="pdin-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#pdin"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="pdin-760"><a href="#pdin-760"><span class="linenos">760</span></a><span class="k">def</span> <span class="nf">print_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="pdin-761"><a href="#pdin-761"><span class="linenos">761</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="get_str_of_data_info_by_name">
                            <input id="get_str_of_data_info_by_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_str_of_data_info_by_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_str_of_data_info_by_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_str_of_data_info_by_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_str_of_data_info_by_name-767"><a href="#get_str_of_data_info_by_name-767"><span class="linenos">767</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="get_str_of_data_info_by_name-768"><a href="#get_str_of_data_info_by_name-768"><span class="linenos">768</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="get_str_of_data_info_by_name-769"><a href="#get_str_of_data_info_by_name-769"><span class="linenos">769</span></a>    <span class="n">data</span> <span class="o">=</span> <span class="n">fr</span><span class="o">.</span><span class="n">f_locals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="get_str_of_data_info_by_name-770"><a href="#get_str_of_data_info_by_name-770"><span class="linenos">770</span></a>    <span class="k">return</span> <span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="gsodibn">
                            <input id="gsodibn-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gsodibn</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="gsodibn-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#gsodibn"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="gsodibn-767"><a href="#gsodibn-767"><span class="linenos">767</span></a><span class="k">def</span> <span class="nf">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="gsodibn-768"><a href="#gsodibn-768"><span class="linenos">768</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="gsodibn-769"><a href="#gsodibn-769"><span class="linenos">769</span></a>    <span class="n">data</span> <span class="o">=</span> <span class="n">fr</span><span class="o">.</span><span class="n">f_locals</span><span class="p">[</span><span class="n">name</span><span class="p">]</span>
</span><span id="gsodibn-770"><a href="#gsodibn-770"><span class="linenos">770</span></a>    <span class="k">return</span> <span class="n">get_str_of_data_info_named</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="print_data_info_by_name">
                            <input id="print_data_info_by_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">print_data_info_by_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="print_data_info_by_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#print_data_info_by_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="print_data_info_by_name-776"><a href="#print_data_info_by_name-776"><span class="linenos">776</span></a><span class="k">def</span> <span class="nf">print_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="print_data_info_by_name-777"><a href="#print_data_info_by_name-777"><span class="linenos">777</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="pdibn">
                            <input id="pdibn-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">pdibn</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">name</span>, </span><span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="pdibn-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#pdibn"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="pdibn-776"><a href="#pdibn-776"><span class="linenos">776</span></a><span class="k">def</span> <span class="nf">print_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="pdibn-777"><a href="#pdibn-777"><span class="linenos">777</span></a>    <span class="nb">print</span><span class="p">(</span><span class="n">get_str_of_data_info_by_name</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="is_descriptor">
                            <input id="is_descriptor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_descriptor</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_descriptor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_descriptor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_descriptor-783"><a href="#is_descriptor-783"><span class="linenos">783</span></a><span class="k">def</span> <span class="nf">is_descriptor</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="is_descriptor-784"><a href="#is_descriptor-784"><span class="linenos">784</span></a>    <span class="k">return</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__get__&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__set__&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__delete__&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="is_setable_data_descriptor">
                            <input id="is_setable_data_descriptor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_setable_data_descriptor</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="is_setable_data_descriptor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_setable_data_descriptor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_setable_data_descriptor-787"><a href="#is_setable_data_descriptor-787"><span class="linenos">787</span></a><span class="k">def</span> <span class="nf">is_setable_data_descriptor</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="is_setable_data_descriptor-788"><a href="#is_setable_data_descriptor-788"><span class="linenos">788</span></a>    <span class="k">return</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__get__&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;__set__&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="is_filled_descriptor">
                            <input id="is_filled_descriptor-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">is_filled_descriptor</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span>, </span><span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="is_filled_descriptor-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#is_filled_descriptor"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="is_filled_descriptor-791"><a href="#is_filled_descriptor-791"><span class="linenos">791</span></a><span class="k">def</span> <span class="nf">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="is_filled_descriptor-792"><a href="#is_filled_descriptor-792"><span class="linenos">792</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;</span>
</span><span id="is_filled_descriptor-793"><a href="#is_filled_descriptor-793"><span class="linenos">793</span></a><span class="sd">        class _foo:</span>
</span><span id="is_filled_descriptor-794"><a href="#is_filled_descriptor-794"><span class="linenos">794</span></a><span class="sd">        __slots__ = [&#39;foo&#39;, &#39;bar&#39;]</span>
</span><span id="is_filled_descriptor-795"><a href="#is_filled_descriptor-795"><span class="linenos">795</span></a>
</span><span id="is_filled_descriptor-796"><a href="#is_filled_descriptor-796"><span class="linenos">796</span></a><span class="sd">        def __init__(self):</span>
</span><span id="is_filled_descriptor-797"><a href="#is_filled_descriptor-797"><span class="linenos">797</span></a><span class="sd">            self.bar = 2</span>
</span><span id="is_filled_descriptor-798"><a href="#is_filled_descriptor-798"><span class="linenos">798</span></a>
</span><span id="is_filled_descriptor-799"><a href="#is_filled_descriptor-799"><span class="linenos">799</span></a><span class="sd">    &#39;foo&#39; - not filled</span>
</span><span id="is_filled_descriptor-800"><a href="#is_filled_descriptor-800"><span class="linenos">800</span></a><span class="sd">    &#39;bar&#39; - filled</span>
</span><span id="is_filled_descriptor-801"><a href="#is_filled_descriptor-801"><span class="linenos">801</span></a>
</span><span id="is_filled_descriptor-802"><a href="#is_filled_descriptor-802"><span class="linenos">802</span></a><span class="sd">    Args:</span>
</span><span id="is_filled_descriptor-803"><a href="#is_filled_descriptor-803"><span class="linenos">803</span></a><span class="sd">        owning_object (_type_): _description_</span>
</span><span id="is_filled_descriptor-804"><a href="#is_filled_descriptor-804"><span class="linenos">804</span></a><span class="sd">        entity (_type_): _description_</span>
</span><span id="is_filled_descriptor-805"><a href="#is_filled_descriptor-805"><span class="linenos">805</span></a>
</span><span id="is_filled_descriptor-806"><a href="#is_filled_descriptor-806"><span class="linenos">806</span></a><span class="sd">    Returns:</span>
</span><span id="is_filled_descriptor-807"><a href="#is_filled_descriptor-807"><span class="linenos">807</span></a><span class="sd">        _type_: _description_</span>
</span><span id="is_filled_descriptor-808"><a href="#is_filled_descriptor-808"><span class="linenos">808</span></a><span class="sd">    &quot;&quot;&quot;</span>    
</span><span id="is_filled_descriptor-809"><a href="#is_filled_descriptor-809"><span class="linenos">809</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="is_filled_descriptor-810"><a href="#is_filled_descriptor-810"><span class="linenos">810</span></a>        <span class="n">entity</span><span class="o">.</span><span class="fm">__get__</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span>
</span><span id="is_filled_descriptor-811"><a href="#is_filled_descriptor-811"><span class="linenos">811</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="is_filled_descriptor-812"><a href="#is_filled_descriptor-812"><span class="linenos">812</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="is_filled_descriptor-813"><a href="#is_filled_descriptor-813"><span class="linenos">813</span></a>    
</span><span id="is_filled_descriptor-814"><a href="#is_filled_descriptor-814"><span class="linenos">814</span></a>    <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


            <div class="docstring"><p>class _foo:
    __slots__ = ['foo', 'bar']</p>

<pre><code>def __init__(self):
    self.bar = 2
</code></pre>

<p>'foo' - not filled
'bar' - filled</p>

<p>Args:
    owning_object (_type_): _description_
    entity (_type_): _description_</p>

<p>Returns:
    _type_: _description_</p>
</div>


                </section>
                <section id="filled_slots_names">
                            <input id="filled_slots_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">filled_slots_names</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="filled_slots_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#filled_slots_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="filled_slots_names-817"><a href="#filled_slots_names-817"><span class="linenos">817</span></a><span class="k">def</span> <span class="nf">filled_slots_names</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="nb">str</span><span class="p">]]:</span>
</span><span id="filled_slots_names-818"><a href="#filled_slots_names-818"><span class="linenos">818</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slots_names-819"><a href="#filled_slots_names-819"><span class="linenos">819</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="filled_slots_names-820"><a href="#filled_slots_names-820"><span class="linenos">820</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slots_names-821"><a href="#filled_slots_names-821"><span class="linenos">821</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="filled_slots_names-822"><a href="#filled_slots_names-822"><span class="linenos">822</span></a>    
</span><span id="filled_slots_names-823"><a href="#filled_slots_names-823"><span class="linenos">823</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="filled_slots_names-824"><a href="#filled_slots_names-824"><span class="linenos">824</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="filled_slots_names-825"><a href="#filled_slots_names-825"><span class="linenos">825</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="filled_slots_names-826"><a href="#filled_slots_names-826"><span class="linenos">826</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="filled_slots_names-827"><a href="#filled_slots_names-827"><span class="linenos">827</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">slot_name</span><span class="p">)</span>
</span><span id="filled_slots_names-828"><a href="#filled_slots_names-828"><span class="linenos">828</span></a>    
</span><span id="filled_slots_names-829"><a href="#filled_slots_names-829"><span class="linenos">829</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="filled_slots">
                            <input id="filled_slots-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">filled_slots</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="filled_slots-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#filled_slots"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="filled_slots-832"><a href="#filled_slots-832"><span class="linenos">832</span></a><span class="k">def</span> <span class="nf">filled_slots</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Any</span><span class="p">]]:</span>
</span><span id="filled_slots-833"><a href="#filled_slots-833"><span class="linenos">833</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slots-834"><a href="#filled_slots-834"><span class="linenos">834</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="filled_slots-835"><a href="#filled_slots-835"><span class="linenos">835</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slots-836"><a href="#filled_slots-836"><span class="linenos">836</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="filled_slots-837"><a href="#filled_slots-837"><span class="linenos">837</span></a>    
</span><span id="filled_slots-838"><a href="#filled_slots-838"><span class="linenos">838</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="filled_slots-839"><a href="#filled_slots-839"><span class="linenos">839</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="filled_slots-840"><a href="#filled_slots-840"><span class="linenos">840</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="filled_slots-841"><a href="#filled_slots-841"><span class="linenos">841</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="filled_slots-842"><a href="#filled_slots-842"><span class="linenos">842</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">slot</span><span class="p">)</span>
</span><span id="filled_slots-843"><a href="#filled_slots-843"><span class="linenos">843</span></a>    
</span><span id="filled_slots-844"><a href="#filled_slots-844"><span class="linenos">844</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="filled_slots_with_names">
                            <input id="filled_slots_with_names-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">filled_slots_with_names</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]],</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="filled_slots_with_names-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#filled_slots_with_names"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="filled_slots_with_names-847"><a href="#filled_slots_with_names-847"><span class="linenos">847</span></a><span class="k">def</span> <span class="nf">filled_slots_with_names</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]]]:</span>
</span><span id="filled_slots_with_names-848"><a href="#filled_slots_with_names-848"><span class="linenos">848</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slots_with_names-849"><a href="#filled_slots_with_names-849"><span class="linenos">849</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="filled_slots_with_names-850"><a href="#filled_slots_with_names-850"><span class="linenos">850</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slots_with_names-851"><a href="#filled_slots_with_names-851"><span class="linenos">851</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="filled_slots_with_names-852"><a href="#filled_slots_with_names-852"><span class="linenos">852</span></a>    
</span><span id="filled_slots_with_names-853"><a href="#filled_slots_with_names-853"><span class="linenos">853</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="filled_slots_with_names-854"><a href="#filled_slots_with_names-854"><span class="linenos">854</span></a>    <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="filled_slots_with_names-855"><a href="#filled_slots_with_names-855"><span class="linenos">855</span></a>        <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect</span><span class="o">.</span><span class="n">getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="filled_slots_with_names-856"><a href="#filled_slots_with_names-856"><span class="linenos">856</span></a>        <span class="k">if</span> <span class="n">is_filled_descriptor</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot</span><span class="p">):</span>
</span><span id="filled_slots_with_names-857"><a href="#filled_slots_with_names-857"><span class="linenos">857</span></a>            <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">slot_name</span><span class="p">,</span> <span class="n">slot</span><span class="p">))</span>
</span><span id="filled_slots_with_names-858"><a href="#filled_slots_with_names-858"><span class="linenos">858</span></a>    
</span><span id="filled_slots_with_names-859"><a href="#filled_slots_with_names-859"><span class="linenos">859</span></a>    <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


    

                </section>
                <section id="filled_slots_with_names_gen">
                            <input id="filled_slots_with_names_gen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">filled_slots_with_names_gen</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span></span><span class="return-annotation">) -> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="filled_slots_with_names_gen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#filled_slots_with_names_gen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="filled_slots_with_names_gen-862"><a href="#filled_slots_with_names_gen-862"><span class="linenos">862</span></a><span class="k">def</span> <span class="nf">filled_slots_with_names_gen</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="filled_slots_with_names_gen-863"><a href="#filled_slots_with_names_gen-863"><span class="linenos">863</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slots_with_names_gen-864"><a href="#filled_slots_with_names_gen-864"><span class="linenos">864</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="filled_slots_with_names_gen-865"><a href="#filled_slots_with_names_gen-865"><span class="linenos">865</span></a>        <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="filled_slots_with_names_gen-866"><a href="#filled_slots_with_names_gen-866"><span class="linenos">866</span></a>            <span class="n">slot</span> <span class="o">=</span> <span class="n">inspect__getattr_static</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">)</span>
</span><span id="filled_slots_with_names_gen-867"><a href="#filled_slots_with_names_gen-867"><span class="linenos">867</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slots_with_names_gen-868"><a href="#filled_slots_with_names_gen-868"><span class="linenos">868</span></a>                <span class="n">slot</span><span class="o">.</span><span class="fm">__get__</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span>
</span><span id="filled_slots_with_names_gen-869"><a href="#filled_slots_with_names_gen-869"><span class="linenos">869</span></a>                <span class="k">yield</span> <span class="p">(</span><span class="n">slot_name</span><span class="p">,</span> <span class="n">slot</span><span class="p">)</span>
</span><span id="filled_slots_with_names_gen-870"><a href="#filled_slots_with_names_gen-870"><span class="linenos">870</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slots_with_names_gen-871"><a href="#filled_slots_with_names_gen-871"><span class="linenos">871</span></a>                <span class="k">pass</span>
</span><span id="filled_slots_with_names_gen-872"><a href="#filled_slots_with_names_gen-872"><span class="linenos">872</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slots_with_names_gen-873"><a href="#filled_slots_with_names_gen-873"><span class="linenos">873</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="filled_slot_names_with_values_gen">
                            <input id="filled_slot_names_with_values_gen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">filled_slot_names_with_values_gen</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">owning_object</span></span><span class="return-annotation">) -> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="filled_slot_names_with_values_gen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#filled_slot_names_with_values_gen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="filled_slot_names_with_values_gen-876"><a href="#filled_slot_names_with_values_gen-876"><span class="linenos">876</span></a><span class="k">def</span> <span class="nf">filled_slot_names_with_values_gen</span><span class="p">(</span><span class="n">owning_object</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Generator</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="filled_slot_names_with_values_gen-877"><a href="#filled_slot_names_with_values_gen-877"><span class="linenos">877</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slot_names_with_values_gen-878"><a href="#filled_slot_names_with_values_gen-878"><span class="linenos">878</span></a>        <span class="n">slots_names</span> <span class="o">=</span> <span class="n">owning_object</span><span class="o">.</span><span class="vm">__slots__</span>
</span><span id="filled_slot_names_with_values_gen-879"><a href="#filled_slot_names_with_values_gen-879"><span class="linenos">879</span></a>        <span class="k">for</span> <span class="n">slot_name</span> <span class="ow">in</span> <span class="n">slots_names</span><span class="p">:</span>
</span><span id="filled_slot_names_with_values_gen-880"><a href="#filled_slot_names_with_values_gen-880"><span class="linenos">880</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="filled_slot_names_with_values_gen-881"><a href="#filled_slot_names_with_values_gen-881"><span class="linenos">881</span></a>                <span class="k">yield</span> <span class="p">(</span><span class="n">slot_name</span><span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">owning_object</span><span class="p">,</span> <span class="n">slot_name</span><span class="p">))</span>
</span><span id="filled_slot_names_with_values_gen-882"><a href="#filled_slot_names_with_values_gen-882"><span class="linenos">882</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slot_names_with_values_gen-883"><a href="#filled_slot_names_with_values_gen-883"><span class="linenos">883</span></a>                <span class="k">pass</span>
</span><span id="filled_slot_names_with_values_gen-884"><a href="#filled_slot_names_with_values_gen-884"><span class="linenos">884</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="filled_slot_names_with_values_gen-885"><a href="#filled_slot_names_with_values_gen-885"><span class="linenos">885</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                </section>
                <section id="current_entity_name">
                            <input id="current_entity_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">current_entity_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="current_entity_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#current_entity_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="current_entity_name-888"><a href="#current_entity_name-888"><span class="linenos">888</span></a><span class="k">def</span> <span class="nf">current_entity_name</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="current_entity_name-889"><a href="#current_entity_name-889"><span class="linenos">889</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="current_entity_name-890"><a href="#current_entity_name-890"><span class="linenos">890</span></a>    <span class="k">return</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">fr</span><span class="p">)</span>
</span><span id="current_entity_name-891"><a href="#current_entity_name-891"><span class="linenos">891</span></a>    <span class="c1"># entity_name = code_name(fr.f_code)</span>
</span><span id="current_entity_name-892"><a href="#current_entity_name-892"><span class="linenos">892</span></a>    <span class="c1"># # print(dir(fr.f_code))</span>
</span><span id="current_entity_name-893"><a href="#current_entity_name-893"><span class="linenos">893</span></a>    <span class="c1"># # print(fr.f_code.__class__)</span>
</span><span id="current_entity_name-894"><a href="#current_entity_name-894"><span class="linenos">894</span></a>    <span class="c1"># # print(dir(fr))</span>
</span><span id="current_entity_name-895"><a href="#current_entity_name-895"><span class="linenos">895</span></a>    <span class="c1"># # print(fr.__class__)</span>
</span><span id="current_entity_name-896"><a href="#current_entity_name-896"><span class="linenos">896</span></a>    <span class="c1"># return entity_name</span>
</span></pre></div>


    

                </section>
                <section id="cen">
                            <input id="cen-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cen</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cen-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cen"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cen-888"><a href="#cen-888"><span class="linenos">888</span></a><span class="k">def</span> <span class="nf">current_entity_name</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="cen-889"><a href="#cen-889"><span class="linenos">889</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="cen-890"><a href="#cen-890"><span class="linenos">890</span></a>    <span class="k">return</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">fr</span><span class="p">)</span>
</span><span id="cen-891"><a href="#cen-891"><span class="linenos">891</span></a>    <span class="c1"># entity_name = code_name(fr.f_code)</span>
</span><span id="cen-892"><a href="#cen-892"><span class="linenos">892</span></a>    <span class="c1"># # print(dir(fr.f_code))</span>
</span><span id="cen-893"><a href="#cen-893"><span class="linenos">893</span></a>    <span class="c1"># # print(fr.f_code.__class__)</span>
</span><span id="cen-894"><a href="#cen-894"><span class="linenos">894</span></a>    <span class="c1"># # print(dir(fr))</span>
</span><span id="cen-895"><a href="#cen-895"><span class="linenos">895</span></a>    <span class="c1"># # print(fr.__class__)</span>
</span><span id="cen-896"><a href="#cen-896"><span class="linenos">896</span></a>    <span class="c1"># return entity_name</span>
</span></pre></div>


    

                </section>
                <section id="current_entity_owner_name">
                            <input id="current_entity_owner_name-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">current_entity_owner_name</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="current_entity_owner_name-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#current_entity_owner_name"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="current_entity_owner_name-902"><a href="#current_entity_owner_name-902"><span class="linenos">902</span></a><span class="k">def</span> <span class="nf">current_entity_owner_name</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">):</span>
</span><span id="current_entity_owner_name-903"><a href="#current_entity_owner_name-903"><span class="linenos">903</span></a>    <span class="n">fr</span> <span class="o">=</span> <span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
</span><span id="current_entity_owner_name-904"><a href="#current_entity_owner_name-904"><span class="linenos">904</span></a>    <span class="k">return</span> <span class="n">owner_name</span><span class="p">(</span><span class="n">entity_owner</span><span class="p">(</span><span class="n">fr</span><span class="o">.</span><span class="n">f_code</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="getattr_ex">
                            <input id="getattr_ex-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">getattr_ex</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">attr_name</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="getattr_ex-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#getattr_ex"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="getattr_ex-916"><a href="#getattr_ex-916"><span class="linenos">916</span></a><span class="k">def</span> <span class="nf">getattr_ex</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="getattr_ex-917"><a href="#getattr_ex-917"><span class="linenos">917</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="getattr_ex-918"><a href="#getattr_ex-918"><span class="linenos">918</span></a>        <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">)</span>
</span><span id="getattr_ex-919"><a href="#getattr_ex-919"><span class="linenos">919</span></a>    <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>  <span class="c1"># See code of the `inspect.getmembers()`</span>
</span><span id="getattr_ex-920"><a href="#getattr_ex-920"><span class="linenos">920</span></a>        <span class="k">if</span> <span class="n">attr_name</span> <span class="ow">in</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">:</span>
</span><span id="getattr_ex-921"><a href="#getattr_ex-921"><span class="linenos">921</span></a>            <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__dict__</span><span class="p">[</span><span class="n">attr_name</span><span class="p">]</span>
</span><span id="getattr_ex-922"><a href="#getattr_ex-922"><span class="linenos">922</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="getattr_ex-923"><a href="#getattr_ex-923"><span class="linenos">923</span></a>            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Attribute &quot;</span><span class="si">{</span><span class="n">attr_name</span><span class="si">}</span><span class="s1">&quot; was not found in the entity &quot;</span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&quot;&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="entity_is_function">
                            <input id="entity_is_function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_is_function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="entity_is_function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_is_function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_is_function-926"><a href="#entity_is_function-926"><span class="linenos">926</span></a><span class="k">def</span> <span class="nf">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="entity_is_function-927"><a href="#entity_is_function-927"><span class="linenos">927</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_function-928"><a href="#entity_is_function-928"><span class="linenos">928</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="entity_is_function-929"><a href="#entity_is_function-929"><span class="linenos">929</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_function-930"><a href="#entity_is_function-930"><span class="linenos">930</span></a>    
</span><span id="entity_is_function-931"><a href="#entity_is_function-931"><span class="linenos">931</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="entity_is_function-932"><a href="#entity_is_function-932"><span class="linenos">932</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_function-933"><a href="#entity_is_function-933"><span class="linenos">933</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="entity_is_function-934"><a href="#entity_is_function-934"><span class="linenos">934</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="entity_is_function-935"><a href="#entity_is_function-935"><span class="linenos">935</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="entity_is_function-936"><a href="#entity_is_function-936"><span class="linenos">936</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_function-937"><a href="#entity_is_function-937"><span class="linenos">937</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="entity_is_function-938"><a href="#entity_is_function-938"><span class="linenos">938</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="entity_is_function-939"><a href="#entity_is_function-939"><span class="linenos">939</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_function-940"><a href="#entity_is_function-940"><span class="linenos">940</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_function-941"><a href="#entity_is_function-941"><span class="linenos">941</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_function-942"><a href="#entity_is_function-942"><span class="linenos">942</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_function-943"><a href="#entity_is_function-943"><span class="linenos">943</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_function-944"><a href="#entity_is_function-944"><span class="linenos">944</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="get_function_by_entity">
                            <input id="get_function_by_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_function_by_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_function_by_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_function_by_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_function_by_entity-947"><a href="#get_function_by_entity-947"><span class="linenos">947</span></a><span class="k">def</span> <span class="nf">get_function_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="get_function_by_entity-948"><a href="#get_function_by_entity-948"><span class="linenos">948</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_function_by_entity-949"><a href="#get_function_by_entity-949"><span class="linenos">949</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_function_by_entity-950"><a href="#get_function_by_entity-950"><span class="linenos">950</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_function_by_entity-951"><a href="#get_function_by_entity-951"><span class="linenos">951</span></a>    
</span><span id="get_function_by_entity-952"><a href="#get_function_by_entity-952"><span class="linenos">952</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="get_function_by_entity-953"><a href="#get_function_by_entity-953"><span class="linenos">953</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_function_by_entity-954"><a href="#get_function_by_entity-954"><span class="linenos">954</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_function_by_entity-955"><a href="#get_function_by_entity-955"><span class="linenos">955</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_function_by_entity-956"><a href="#get_function_by_entity-956"><span class="linenos">956</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_function_by_entity-957"><a href="#get_function_by_entity-957"><span class="linenos">957</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_function_by_entity-958"><a href="#get_function_by_entity-958"><span class="linenos">958</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_function_by_entity-959"><a href="#get_function_by_entity-959"><span class="linenos">959</span></a>                <span class="k">return</span> <span class="n">possible_entity</span>
</span><span id="get_function_by_entity-960"><a href="#get_function_by_entity-960"><span class="linenos">960</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="get_function_by_entity-961"><a href="#get_function_by_entity-961"><span class="linenos">961</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_function_by_entity-962"><a href="#get_function_by_entity-962"><span class="linenos">962</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="get_function_by_entity-963"><a href="#get_function_by_entity-963"><span class="linenos">963</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_function_by_entity-964"><a href="#get_function_by_entity-964"><span class="linenos">964</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="get_function_by_entity-965"><a href="#get_function_by_entity-965"><span class="linenos">965</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="entity_is_method">
                            <input id="entity_is_method-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_is_method</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="entity_is_method-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_is_method"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_is_method-968"><a href="#entity_is_method-968"><span class="linenos">968</span></a><span class="k">def</span> <span class="nf">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="entity_is_method-969"><a href="#entity_is_method-969"><span class="linenos">969</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_method-970"><a href="#entity_is_method-970"><span class="linenos">970</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="entity_is_method-971"><a href="#entity_is_method-971"><span class="linenos">971</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_method-972"><a href="#entity_is_method-972"><span class="linenos">972</span></a>    
</span><span id="entity_is_method-973"><a href="#entity_is_method-973"><span class="linenos">973</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="entity_is_method-974"><a href="#entity_is_method-974"><span class="linenos">974</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_method-975"><a href="#entity_is_method-975"><span class="linenos">975</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="entity_is_method-976"><a href="#entity_is_method-976"><span class="linenos">976</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="entity_is_method-977"><a href="#entity_is_method-977"><span class="linenos">977</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="entity_is_method-978"><a href="#entity_is_method-978"><span class="linenos">978</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_method-979"><a href="#entity_is_method-979"><span class="linenos">979</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="entity_is_method-980"><a href="#entity_is_method-980"><span class="linenos">980</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="entity_is_method-981"><a href="#entity_is_method-981"><span class="linenos">981</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_method-982"><a href="#entity_is_method-982"><span class="linenos">982</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_method-983"><a href="#entity_is_method-983"><span class="linenos">983</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_method-984"><a href="#entity_is_method-984"><span class="linenos">984</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_method-985"><a href="#entity_is_method-985"><span class="linenos">985</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_method-986"><a href="#entity_is_method-986"><span class="linenos">986</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="get_method_by_entity">
                            <input id="get_method_by_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_method_by_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_method_by_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_method_by_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_method_by_entity-989"><a href="#get_method_by_entity-989"><span class="linenos"> 989</span></a><span class="k">def</span> <span class="nf">get_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="get_method_by_entity-990"><a href="#get_method_by_entity-990"><span class="linenos"> 990</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_method_by_entity-991"><a href="#get_method_by_entity-991"><span class="linenos"> 991</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="get_method_by_entity-992"><a href="#get_method_by_entity-992"><span class="linenos"> 992</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_method_by_entity-993"><a href="#get_method_by_entity-993"><span class="linenos"> 993</span></a>    
</span><span id="get_method_by_entity-994"><a href="#get_method_by_entity-994"><span class="linenos"> 994</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="get_method_by_entity-995"><a href="#get_method_by_entity-995"><span class="linenos"> 995</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_method_by_entity-996"><a href="#get_method_by_entity-996"><span class="linenos"> 996</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_method_by_entity-997"><a href="#get_method_by_entity-997"><span class="linenos"> 997</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_method_by_entity-998"><a href="#get_method_by_entity-998"><span class="linenos"> 998</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_method_by_entity-999"><a href="#get_method_by_entity-999"><span class="linenos"> 999</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_method_by_entity-1000"><a href="#get_method_by_entity-1000"><span class="linenos">1000</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_method_by_entity-1001"><a href="#get_method_by_entity-1001"><span class="linenos">1001</span></a>                <span class="k">return</span> <span class="n">possible_entity</span>
</span><span id="get_method_by_entity-1002"><a href="#get_method_by_entity-1002"><span class="linenos">1002</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="get_method_by_entity-1003"><a href="#get_method_by_entity-1003"><span class="linenos">1003</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_method_by_entity-1004"><a href="#get_method_by_entity-1004"><span class="linenos">1004</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="get_method_by_entity-1005"><a href="#get_method_by_entity-1005"><span class="linenos">1005</span></a>            <span class="k">return</span> <span class="kc">None</span>
</span><span id="get_method_by_entity-1006"><a href="#get_method_by_entity-1006"><span class="linenos">1006</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="get_method_by_entity-1007"><a href="#get_method_by_entity-1007"><span class="linenos">1007</span></a>        <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="entity_is_unbound_method">
                            <input id="entity_is_unbound_method-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">entity_is_unbound_method</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="entity_is_unbound_method-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#entity_is_unbound_method"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="entity_is_unbound_method-1010"><a href="#entity_is_unbound_method-1010"><span class="linenos">1010</span></a><span class="k">def</span> <span class="nf">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="entity_is_unbound_method-1011"><a href="#entity_is_unbound_method-1011"><span class="linenos">1011</span></a>    <span class="n">owner</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">,</span> <span class="n">ModuleType</span><span class="p">]]</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_unbound_method-1012"><a href="#entity_is_unbound_method-1012"><span class="linenos">1012</span></a>    <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="entity_is_unbound_method-1013"><a href="#entity_is_unbound_method-1013"><span class="linenos">1013</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_unbound_method-1014"><a href="#entity_is_unbound_method-1014"><span class="linenos">1014</span></a>    
</span><span id="entity_is_unbound_method-1015"><a href="#entity_is_unbound_method-1015"><span class="linenos">1015</span></a>    <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismodule</span><span class="p">(</span><span class="n">owner</span><span class="p">):</span>
</span><span id="entity_is_unbound_method-1016"><a href="#entity_is_unbound_method-1016"><span class="linenos">1016</span></a>        <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_unbound_method-1017"><a href="#entity_is_unbound_method-1017"><span class="linenos">1017</span></a>        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="entity_is_unbound_method-1018"><a href="#entity_is_unbound_method-1018"><span class="linenos">1018</span></a>            <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="entity_is_unbound_method-1019"><a href="#entity_is_unbound_method-1019"><span class="linenos">1019</span></a>            <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="entity_is_unbound_method-1020"><a href="#entity_is_unbound_method-1020"><span class="linenos">1020</span></a>            <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="entity_is_unbound_method-1021"><a href="#entity_is_unbound_method-1021"><span class="linenos">1021</span></a>            <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="entity_is_unbound_method-1022"><a href="#entity_is_unbound_method-1022"><span class="linenos">1022</span></a>                <span class="k">return</span> <span class="kc">False</span>
</span><span id="entity_is_unbound_method-1023"><a href="#entity_is_unbound_method-1023"><span class="linenos">1023</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_unbound_method-1024"><a href="#entity_is_unbound_method-1024"><span class="linenos">1024</span></a>                <span class="k">return</span> <span class="kc">True</span>
</span><span id="entity_is_unbound_method-1025"><a href="#entity_is_unbound_method-1025"><span class="linenos">1025</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_unbound_method-1026"><a href="#entity_is_unbound_method-1026"><span class="linenos">1026</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="entity_is_unbound_method-1027"><a href="#entity_is_unbound_method-1027"><span class="linenos">1027</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="entity_is_unbound_method-1028"><a href="#entity_is_unbound_method-1028"><span class="linenos">1028</span></a>        <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                </section>
                <section id="get_unbound_method_by_entity">
                            <input id="get_unbound_method_by_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_unbound_method_by_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="get_unbound_method_by_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_unbound_method_by_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_unbound_method_by_entity-1031"><a href="#get_unbound_method_by_entity-1031"><span class="linenos">1031</span></a><span class="k">def</span> <span class="nf">get_unbound_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]:</span>
</span><span id="get_unbound_method_by_entity-1032"><a href="#get_unbound_method_by_entity-1032"><span class="linenos">1032</span></a>    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="AnAppropriateOwnerParameterWasNotFoundError">
                            <input id="AnAppropriateOwnerParameterWasNotFoundError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">AnAppropriateOwnerParameterWasNotFoundError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="AnAppropriateOwnerParameterWasNotFoundError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#AnAppropriateOwnerParameterWasNotFoundError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="AnAppropriateOwnerParameterWasNotFoundError-1035"><a href="#AnAppropriateOwnerParameterWasNotFoundError-1035"><span class="linenos">1035</span></a><span class="k">class</span> <span class="nc">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="AnAppropriateOwnerParameterWasNotFoundError-1036"><a href="#AnAppropriateOwnerParameterWasNotFoundError-1036"><span class="linenos">1036</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="AnAppropriateOwnerParameterWasNotFoundError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="AnAppropriateOwnerParameterWasNotFoundError.with_traceback" class="function">with_traceback</dd>
                <dd id="AnAppropriateOwnerParameterWasNotFoundError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="PossibleOwnerParameterDoesNotMatchError">
                            <input id="PossibleOwnerParameterDoesNotMatchError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">PossibleOwnerParameterDoesNotMatchError</span><wbr>(<span class="base"><a href="#AnAppropriateOwnerParameterWasNotFoundError">AnAppropriateOwnerParameterWasNotFoundError</a></span>):

                <label class="view-source-button" for="PossibleOwnerParameterDoesNotMatchError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#PossibleOwnerParameterDoesNotMatchError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="PossibleOwnerParameterDoesNotMatchError-1039"><a href="#PossibleOwnerParameterDoesNotMatchError-1039"><span class="linenos">1039</span></a><span class="k">class</span> <span class="nc">PossibleOwnerParameterDoesNotMatchError</span><span class="p">(</span><span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">):</span>
</span><span id="PossibleOwnerParameterDoesNotMatchError-1040"><a href="#PossibleOwnerParameterDoesNotMatchError-1040"><span class="linenos">1040</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="PossibleOwnerParameterDoesNotMatchError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="PossibleOwnerParameterDoesNotMatchError.with_traceback" class="function">with_traceback</dd>
                <dd id="PossibleOwnerParameterDoesNotMatchError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EntityHasNoPositionalParametersError">
                            <input id="EntityHasNoPositionalParametersError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EntityHasNoPositionalParametersError</span><wbr>(<span class="base"><a href="#AnAppropriateOwnerParameterWasNotFoundError">AnAppropriateOwnerParameterWasNotFoundError</a></span>):

                <label class="view-source-button" for="EntityHasNoPositionalParametersError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityHasNoPositionalParametersError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityHasNoPositionalParametersError-1043"><a href="#EntityHasNoPositionalParametersError-1043"><span class="linenos">1043</span></a><span class="k">class</span> <span class="nc">EntityHasNoPositionalParametersError</span><span class="p">(</span><span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">):</span>
</span><span id="EntityHasNoPositionalParametersError-1044"><a href="#EntityHasNoPositionalParametersError-1044"><span class="linenos">1044</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="EntityHasNoPositionalParametersError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EntityHasNoPositionalParametersError.with_traceback" class="function">with_traceback</dd>
                <dd id="EntityHasNoPositionalParametersError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="get_owner_parameter">
                            <input id="get_owner_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_owner_parameter</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span>,</span><span class="param">	<span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">return_even_if_not_match</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_owner_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_owner_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_owner_parameter-1047"><a href="#get_owner_parameter-1047"><span class="linenos">1047</span></a><span class="k">def</span> <span class="nf">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">return_even_if_not_match</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
</span><span id="get_owner_parameter-1048"><a href="#get_owner_parameter-1048"><span class="linenos">1048</span></a>    <span class="k">if</span> <span class="n">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_owner_parameter-1049"><a href="#get_owner_parameter-1049"><span class="linenos">1049</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Function has no </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter&#39;</span><span class="p">)</span>
</span><span id="get_owner_parameter-1050"><a href="#get_owner_parameter-1050"><span class="linenos">1050</span></a>    
</span><span id="get_owner_parameter-1051"><a href="#get_owner_parameter-1051"><span class="linenos">1051</span></a>    <span class="k">if</span> <span class="n">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_owner_parameter-1052"><a href="#get_owner_parameter-1052"><span class="linenos">1052</span></a>        <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__self__</span>
</span><span id="get_owner_parameter-1053"><a href="#get_owner_parameter-1053"><span class="linenos">1053</span></a>    <span class="k">elif</span> <span class="n">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_owner_parameter-1054"><a href="#get_owner_parameter-1054"><span class="linenos">1054</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="get_owner_parameter-1055"><a href="#get_owner_parameter-1055"><span class="linenos">1055</span></a>            <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_owner_parameter-1056"><a href="#get_owner_parameter-1056"><span class="linenos">1056</span></a>            <span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_owner_parameter-1057"><a href="#get_owner_parameter-1057"><span class="linenos">1057</span></a>            <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">params_with_values</span>
</span><span id="get_owner_parameter-1058"><a href="#get_owner_parameter-1058"><span class="linenos">1058</span></a>            <span class="k">if</span> <span class="n">positional</span><span class="p">:</span>
</span><span id="get_owner_parameter-1059"><a href="#get_owner_parameter-1059"><span class="linenos">1059</span></a>                <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="get_owner_parameter-1060"><a href="#get_owner_parameter-1060"><span class="linenos">1060</span></a>            <span class="k">elif</span> <span class="n">positional_only</span><span class="p">:</span>
</span><span id="get_owner_parameter-1061"><a href="#get_owner_parameter-1061"><span class="linenos">1061</span></a>                <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional_only</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="get_owner_parameter-1062"><a href="#get_owner_parameter-1062"><span class="linenos">1062</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="get_owner_parameter-1063"><a href="#get_owner_parameter-1063"><span class="linenos">1063</span></a>                <span class="k">raise</span> <span class="n">EntityHasNoPositionalParametersError</span>
</span><span id="get_owner_parameter-1064"><a href="#get_owner_parameter-1064"><span class="linenos">1064</span></a>            
</span><span id="get_owner_parameter-1065"><a href="#get_owner_parameter-1065"><span class="linenos">1065</span></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_owner_parameter-1066"><a href="#get_owner_parameter-1066"><span class="linenos">1066</span></a>                <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_owner_parameter-1067"><a href="#get_owner_parameter-1067"><span class="linenos">1067</span></a>                <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_owner_parameter-1068"><a href="#get_owner_parameter-1068"><span class="linenos">1068</span></a>                <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_owner_parameter-1069"><a href="#get_owner_parameter-1069"><span class="linenos">1069</span></a>                <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_owner_parameter-1070"><a href="#get_owner_parameter-1070"><span class="linenos">1070</span></a>                    <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="get_owner_parameter-1071"><a href="#get_owner_parameter-1071"><span class="linenos">1071</span></a>                <span class="k">else</span><span class="p">:</span>
</span><span id="get_owner_parameter-1072"><a href="#get_owner_parameter-1072"><span class="linenos">1072</span></a>                    <span class="k">if</span> <span class="n">return_even_if_not_match</span><span class="p">:</span>
</span><span id="get_owner_parameter-1073"><a href="#get_owner_parameter-1073"><span class="linenos">1073</span></a>                        <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="get_owner_parameter-1074"><a href="#get_owner_parameter-1074"><span class="linenos">1074</span></a>                    <span class="k">else</span><span class="p">:</span>
</span><span id="get_owner_parameter-1075"><a href="#get_owner_parameter-1075"><span class="linenos">1075</span></a>                        <span class="k">raise</span> <span class="n">PossibleOwnerParameterDoesNotMatchError</span>
</span><span id="get_owner_parameter-1076"><a href="#get_owner_parameter-1076"><span class="linenos">1076</span></a>            
</span><span id="get_owner_parameter-1077"><a href="#get_owner_parameter-1077"><span class="linenos">1077</span></a>            <span class="k">raise</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Can not find an appropriate </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter in </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="get_owner_parameter-1078"><a href="#get_owner_parameter-1078"><span class="linenos">1078</span></a>    <span class="k">else</span><span class="p">:</span>
</span><span id="get_owner_parameter-1079"><a href="#get_owner_parameter-1079"><span class="linenos">1079</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1"> of type </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="si">}</span><span class="s1"> is not supported&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_self_parameter">
                            <input id="get_self_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_self_parameter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_self_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_self_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_self_parameter-1082"><a href="#get_self_parameter-1082"><span class="linenos">1082</span></a><span class="k">def</span> <span class="nf">get_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_self_parameter-1083"><a href="#get_self_parameter-1083"><span class="linenos">1083</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;self&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_cls_parameter">
                            <input id="get_cls_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_cls_parameter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_cls_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_cls_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_cls_parameter-1086"><a href="#get_cls_parameter-1086"><span class="linenos">1086</span></a><span class="k">def</span> <span class="nf">get_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_cls_parameter-1087"><a href="#get_cls_parameter-1087"><span class="linenos">1087</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_any_owner_parameter">
                            <input id="get_any_owner_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_any_owner_parameter</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">entity</span>,</span><span class="param">	<span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span>,</span><span class="param">	<span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>,</span><span class="param">	<span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_any_owner_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_any_owner_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_any_owner_parameter-1090"><a href="#get_any_owner_parameter-1090"><span class="linenos">1090</span></a><span class="k">def</span> <span class="nf">get_any_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">owner_parameter_name</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1091"><a href="#get_any_owner_parameter-1091"><span class="linenos">1091</span></a>    <span class="k">if</span> <span class="n">entity_is_function</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1092"><a href="#get_any_owner_parameter-1092"><span class="linenos">1092</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Function has no </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter&#39;</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1093"><a href="#get_any_owner_parameter-1093"><span class="linenos">1093</span></a>    
</span><span id="get_any_owner_parameter-1094"><a href="#get_any_owner_parameter-1094"><span class="linenos">1094</span></a>    <span class="k">if</span> <span class="n">entity_is_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1095"><a href="#get_any_owner_parameter-1095"><span class="linenos">1095</span></a>        <span class="k">return</span> <span class="n">entity</span><span class="o">.</span><span class="vm">__self__</span>
</span><span id="get_any_owner_parameter-1096"><a href="#get_any_owner_parameter-1096"><span class="linenos">1096</span></a>    <span class="k">elif</span> <span class="n">entity_is_unbound_method</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1097"><a href="#get_any_owner_parameter-1097"><span class="linenos">1097</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1098"><a href="#get_any_owner_parameter-1098"><span class="linenos">1098</span></a>            <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1099"><a href="#get_any_owner_parameter-1099"><span class="linenos">1099</span></a>            <span class="n">params_with_values</span><span class="p">:</span> <span class="n">CodeParamsWithValues</span> <span class="o">=</span> <span class="n">intro_frame_params_with_values</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1100"><a href="#get_any_owner_parameter-1100"><span class="linenos">1100</span></a>            <span class="n">positional</span><span class="p">,</span> <span class="n">positional_only</span><span class="p">,</span> <span class="n">keyword_only</span> <span class="o">=</span> <span class="n">params_with_values</span>
</span><span id="get_any_owner_parameter-1101"><a href="#get_any_owner_parameter-1101"><span class="linenos">1101</span></a>            
</span><span id="get_any_owner_parameter-1102"><a href="#get_any_owner_parameter-1102"><span class="linenos">1102</span></a>            <span class="k">if</span> <span class="n">any_positional</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1103"><a href="#get_any_owner_parameter-1103"><span class="linenos">1103</span></a>                <span class="n">all_positional</span> <span class="o">=</span> <span class="n">positional</span> <span class="o">+</span> <span class="n">positional_only</span>
</span><span id="get_any_owner_parameter-1104"><a href="#get_any_owner_parameter-1104"><span class="linenos">1104</span></a>                <span class="k">for</span> <span class="n">param</span> <span class="ow">in</span> <span class="n">all_positional</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1105"><a href="#get_any_owner_parameter-1105"><span class="linenos">1105</span></a>                    <span class="n">possible_positional_self_name</span><span class="p">,</span> <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">param</span>
</span><span id="get_any_owner_parameter-1106"><a href="#get_any_owner_parameter-1106"><span class="linenos">1106</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1107"><a href="#get_any_owner_parameter-1107"><span class="linenos">1107</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1108"><a href="#get_any_owner_parameter-1108"><span class="linenos">1108</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1109"><a href="#get_any_owner_parameter-1109"><span class="linenos">1109</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1110"><a href="#get_any_owner_parameter-1110"><span class="linenos">1110</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1111"><a href="#get_any_owner_parameter-1111"><span class="linenos">1111</span></a>                            <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="get_any_owner_parameter-1112"><a href="#get_any_owner_parameter-1112"><span class="linenos">1112</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1113"><a href="#get_any_owner_parameter-1113"><span class="linenos">1113</span></a>                <span class="k">if</span> <span class="n">positional</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1114"><a href="#get_any_owner_parameter-1114"><span class="linenos">1114</span></a>                    <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="get_any_owner_parameter-1115"><a href="#get_any_owner_parameter-1115"><span class="linenos">1115</span></a>                <span class="k">elif</span> <span class="n">positional_only</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1116"><a href="#get_any_owner_parameter-1116"><span class="linenos">1116</span></a>                    <span class="n">possible_positional_self</span> <span class="o">=</span> <span class="n">positional_only</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span>
</span><span id="get_any_owner_parameter-1117"><a href="#get_any_owner_parameter-1117"><span class="linenos">1117</span></a>                
</span><span id="get_any_owner_parameter-1118"><a href="#get_any_owner_parameter-1118"><span class="linenos">1118</span></a>                <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1119"><a href="#get_any_owner_parameter-1119"><span class="linenos">1119</span></a>                    <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_positional_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1120"><a href="#get_any_owner_parameter-1120"><span class="linenos">1120</span></a>                    <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1121"><a href="#get_any_owner_parameter-1121"><span class="linenos">1121</span></a>                    <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1122"><a href="#get_any_owner_parameter-1122"><span class="linenos">1122</span></a>                    <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1123"><a href="#get_any_owner_parameter-1123"><span class="linenos">1123</span></a>                        <span class="k">return</span> <span class="n">possible_positional_self</span>
</span><span id="get_any_owner_parameter-1124"><a href="#get_any_owner_parameter-1124"><span class="linenos">1124</span></a>            
</span><span id="get_any_owner_parameter-1125"><a href="#get_any_owner_parameter-1125"><span class="linenos">1125</span></a>            <span class="k">if</span> <span class="n">any_keyword</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1126"><a href="#get_any_owner_parameter-1126"><span class="linenos">1126</span></a>                <span class="k">for</span> <span class="n">possible_keyword_self_name</span><span class="p">,</span> <span class="n">possible_keyword_self</span> <span class="ow">in</span> <span class="n">keyword_only</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1127"><a href="#get_any_owner_parameter-1127"><span class="linenos">1127</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1128"><a href="#get_any_owner_parameter-1128"><span class="linenos">1128</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1129"><a href="#get_any_owner_parameter-1129"><span class="linenos">1129</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1130"><a href="#get_any_owner_parameter-1130"><span class="linenos">1130</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1131"><a href="#get_any_owner_parameter-1131"><span class="linenos">1131</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1132"><a href="#get_any_owner_parameter-1132"><span class="linenos">1132</span></a>                            <span class="k">return</span> <span class="n">possible_keyword_self</span>
</span><span id="get_any_owner_parameter-1133"><a href="#get_any_owner_parameter-1133"><span class="linenos">1133</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1134"><a href="#get_any_owner_parameter-1134"><span class="linenos">1134</span></a>                <span class="n">keyword_only_dict</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">keyword_only</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1135"><a href="#get_any_owner_parameter-1135"><span class="linenos">1135</span></a>                <span class="k">if</span> <span class="n">owner_parameter_name</span> <span class="ow">in</span> <span class="n">keyword_only_dict</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1136"><a href="#get_any_owner_parameter-1136"><span class="linenos">1136</span></a>                    <span class="n">possible_keyword_self</span> <span class="o">=</span> <span class="n">keyword_only_dict</span><span class="p">[</span><span class="n">owner_parameter_name</span><span class="p">]</span>
</span><span id="get_any_owner_parameter-1137"><a href="#get_any_owner_parameter-1137"><span class="linenos">1137</span></a>                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">):</span>
</span><span id="get_any_owner_parameter-1138"><a href="#get_any_owner_parameter-1138"><span class="linenos">1138</span></a>                        <span class="n">possible_entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">possible_keyword_self</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1139"><a href="#get_any_owner_parameter-1139"><span class="linenos">1139</span></a>                        <span class="n">possible_entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">possible_entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1140"><a href="#get_any_owner_parameter-1140"><span class="linenos">1140</span></a>                        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="get_any_owner_parameter-1141"><a href="#get_any_owner_parameter-1141"><span class="linenos">1141</span></a>                        <span class="k">if</span> <span class="n">possible_entity_code</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="get_any_owner_parameter-1142"><a href="#get_any_owner_parameter-1142"><span class="linenos">1142</span></a>                            <span class="k">return</span> <span class="n">possible_keyword_self</span>
</span><span id="get_any_owner_parameter-1143"><a href="#get_any_owner_parameter-1143"><span class="linenos">1143</span></a>            
</span><span id="get_any_owner_parameter-1144"><a href="#get_any_owner_parameter-1144"><span class="linenos">1144</span></a>            <span class="k">raise</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Can not find </span><span class="si">{</span><span class="n">owner_parameter_name</span><span class="si">}</span><span class="s1"> parameter in </span><span class="si">{</span><span class="n">entity</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_any_self_parameter">
                            <input id="get_any_self_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_any_self_parameter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>, </span><span class="param"><span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_any_self_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_any_self_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_any_self_parameter-1147"><a href="#get_any_self_parameter-1147"><span class="linenos">1147</span></a><span class="k">def</span> <span class="nf">get_any_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="get_any_self_parameter-1148"><a href="#get_any_self_parameter-1148"><span class="linenos">1148</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;self&#39;</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="get_any_cls_parameter">
                            <input id="get_any_cls_parameter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">get_any_cls_parameter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span>, </span><span class="param"><span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>, </span><span class="param"><span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="get_any_cls_parameter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#get_any_cls_parameter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="get_any_cls_parameter-1151"><a href="#get_any_cls_parameter-1151"><span class="linenos">1151</span></a><span class="k">def</span> <span class="nf">get_any_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">any_positional</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">):</span>
</span><span id="get_any_cls_parameter-1152"><a href="#get_any_cls_parameter-1152"><span class="linenos">1152</span></a>    <span class="k">return</span> <span class="n">get_owner_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="s1">&#39;cls&#39;</span> <span class="p">,</span> <span class="n">any_positional</span><span class="p">,</span> <span class="n">any_keyword</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="find_method_in_module_by_code">
                            <input id="find_method_in_module_by_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_method_in_module_by_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">module</span>, </span><span class="param"><span class="n">code_to_find</span><span class="p">:</span> <span class="n">code</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">code</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="find_method_in_module_by_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_method_in_module_by_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_method_in_module_by_code-1155"><a href="#find_method_in_module_by_code-1155"><span class="linenos">1155</span></a><span class="k">def</span> <span class="nf">find_method_in_module_by_code</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeType</span><span class="p">]:</span>
</span><span id="find_method_in_module_by_code-1156"><a href="#find_method_in_module_by_code-1156"><span class="linenos">1156</span></a>    <span class="k">for</span> <span class="n">entity_name_str</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">module</span><span class="p">):</span>
</span><span id="find_method_in_module_by_code-1157"><a href="#find_method_in_module_by_code-1157"><span class="linenos">1157</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="find_method_in_module_by_code-1158"><a href="#find_method_in_module_by_code-1158"><span class="linenos">1158</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="find_method_in_module_by_code-1159"><a href="#find_method_in_module_by_code-1159"><span class="linenos">1159</span></a>            <span class="n">possible_method</span> <span class="o">=</span> <span class="n">find_method_in_class_by_code</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">)</span>
</span><span id="find_method_in_module_by_code-1160"><a href="#find_method_in_module_by_code-1160"><span class="linenos">1160</span></a>            <span class="k">if</span> <span class="n">possible_method</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_method_in_module_by_code-1161"><a href="#find_method_in_module_by_code-1161"><span class="linenos">1161</span></a>                <span class="k">return</span> <span class="n">possible_method</span>
</span><span id="find_method_in_module_by_code-1162"><a href="#find_method_in_module_by_code-1162"><span class="linenos">1162</span></a>    
</span><span id="find_method_in_module_by_code-1163"><a href="#find_method_in_module_by_code-1163"><span class="linenos">1163</span></a>    <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="find_method_in_class_by_code">
                            <input id="find_method_in_class_by_code-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_method_in_class_by_code</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">class_to_search_in</span>, </span><span class="param"><span class="n">code_to_find</span><span class="p">:</span> <span class="n">code</span></span><span class="return-annotation">) -> <span class="n">Union</span><span class="p">[</span><span class="n">code</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="find_method_in_class_by_code-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_method_in_class_by_code"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_method_in_class_by_code-1166"><a href="#find_method_in_class_by_code-1166"><span class="linenos">1166</span></a><span class="k">def</span> <span class="nf">find_method_in_class_by_code</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">:</span> <span class="n">CodeType</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CodeType</span><span class="p">]:</span>
</span><span id="find_method_in_class_by_code-1167"><a href="#find_method_in_class_by_code-1167"><span class="linenos">1167</span></a>    <span class="n">subclassess</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="find_method_in_class_by_code-1168"><a href="#find_method_in_class_by_code-1168"><span class="linenos">1168</span></a>    <span class="k">for</span> <span class="n">entity_name_str</span> <span class="ow">in</span> <span class="n">class_properties_including_overrided</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">):</span>
</span><span id="find_method_in_class_by_code-1169"><a href="#find_method_in_class_by_code-1169"><span class="linenos">1169</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">class_to_search_in</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="find_method_in_class_by_code-1170"><a href="#find_method_in_class_by_code-1170"><span class="linenos">1170</span></a>        <span class="k">if</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isclass</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="find_method_in_class_by_code-1171"><a href="#find_method_in_class_by_code-1171"><span class="linenos">1171</span></a>            <span class="n">subclassess</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_method_in_class_by_code-1172"><a href="#find_method_in_class_by_code-1172"><span class="linenos">1172</span></a>        <span class="k">elif</span> <span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">entity</span><span class="p">):</span>
</span><span id="find_method_in_class_by_code-1173"><a href="#find_method_in_class_by_code-1173"><span class="linenos">1173</span></a>            <span class="k">if</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">is</span> <span class="n">code_to_find</span><span class="p">:</span>
</span><span id="find_method_in_class_by_code-1174"><a href="#find_method_in_class_by_code-1174"><span class="linenos">1174</span></a>                <span class="k">return</span> <span class="n">entity</span>
</span><span id="find_method_in_class_by_code-1175"><a href="#find_method_in_class_by_code-1175"><span class="linenos">1175</span></a>        
</span><span id="find_method_in_class_by_code-1176"><a href="#find_method_in_class_by_code-1176"><span class="linenos">1176</span></a>    <span class="k">for</span> <span class="n">subclass</span> <span class="ow">in</span> <span class="n">subclassess</span><span class="p">:</span>
</span><span id="find_method_in_class_by_code-1177"><a href="#find_method_in_class_by_code-1177"><span class="linenos">1177</span></a>        <span class="n">possible_method</span> <span class="o">=</span> <span class="n">find_method_in_class_by_code</span><span class="p">(</span><span class="n">subclass</span><span class="p">,</span> <span class="n">code_to_find</span><span class="p">)</span>
</span><span id="find_method_in_class_by_code-1178"><a href="#find_method_in_class_by_code-1178"><span class="linenos">1178</span></a>        <span class="k">if</span> <span class="n">possible_method</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_method_in_class_by_code-1179"><a href="#find_method_in_class_by_code-1179"><span class="linenos">1179</span></a>            <span class="k">return</span> <span class="n">possible_method</span>
</span><span id="find_method_in_class_by_code-1180"><a href="#find_method_in_class_by_code-1180"><span class="linenos">1180</span></a>    
</span><span id="find_method_in_class_by_code-1181"><a href="#find_method_in_class_by_code-1181"><span class="linenos">1181</span></a>    <span class="k">return</span> <span class="kc">None</span>
</span></pre></div>


    

                </section>
                <section id="EntityWasNotFoundError">
                            <input id="EntityWasNotFoundError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EntityWasNotFoundError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="EntityWasNotFoundError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EntityWasNotFoundError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EntityWasNotFoundError-1184"><a href="#EntityWasNotFoundError-1184"><span class="linenos">1184</span></a><span class="k">class</span> <span class="nc">EntityWasNotFoundError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="EntityWasNotFoundError-1185"><a href="#EntityWasNotFoundError-1185"><span class="linenos">1185</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="EntityWasNotFoundError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EntityWasNotFoundError.with_traceback" class="function">with_traceback</dd>
                <dd id="EntityWasNotFoundError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="find_entity">
                            <input id="find_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">entity</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">,</span> <span class="n">frame</span><span class="p">,</span> <span class="n">code</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="find_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_entity-1188"><a href="#find_entity-1188"><span class="linenos">1188</span></a><span class="k">def</span> <span class="nf">find_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Callable</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="find_entity-1189"><a href="#find_entity-1189"><span class="linenos">1189</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">inspect</span><span class="o">.</span><span class="n">isfunction</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="n">inspect</span><span class="o">.</span><span class="n">ismethod</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">)</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">)):</span>
</span><span id="find_entity-1190"><a href="#find_entity-1190"><span class="linenos">1190</span></a>        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Only functions, methods, frames and codes are supported. </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span><span class="si">}</span><span class="s1"> was provided instead&#39;</span><span class="p">)</span>
</span><span id="find_entity-1191"><a href="#find_entity-1191"><span class="linenos">1191</span></a>    
</span><span id="find_entity-1192"><a href="#find_entity-1192"><span class="linenos">1192</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_function_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1193"><a href="#find_entity-1193"><span class="linenos">1193</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_entity-1194"><a href="#find_entity-1194"><span class="linenos">1194</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="find_entity-1195"><a href="#find_entity-1195"><span class="linenos">1195</span></a>    
</span><span id="find_entity-1196"><a href="#find_entity-1196"><span class="linenos">1196</span></a>    <span class="n">result</span> <span class="o">=</span> <span class="n">get_method_by_entity</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1197"><a href="#find_entity-1197"><span class="linenos">1197</span></a>    <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_entity-1198"><a href="#find_entity-1198"><span class="linenos">1198</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="find_entity-1199"><a href="#find_entity-1199"><span class="linenos">1199</span></a>    
</span><span id="find_entity-1200"><a href="#find_entity-1200"><span class="linenos">1200</span></a>    <span class="n">entity_name_str</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">entity_name</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1201"><a href="#find_entity-1201"><span class="linenos">1201</span></a>    <span class="n">entity_instance</span><span class="p">:</span> <span class="n">Callable</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_entity-1202"><a href="#find_entity-1202"><span class="linenos">1202</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">FrameType</span><span class="p">):</span>
</span><span id="find_entity-1203"><a href="#find_entity-1203"><span class="linenos">1203</span></a>        <span class="n">owner</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="find_entity-1204"><a href="#find_entity-1204"><span class="linenos">1204</span></a>        <span class="n">need_to_try_clr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="find_entity-1205"><a href="#find_entity-1205"><span class="linenos">1205</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="find_entity-1206"><a href="#find_entity-1206"><span class="linenos">1206</span></a>            <span class="n">owner</span> <span class="o">=</span> <span class="n">get_self_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1207"><a href="#find_entity-1207"><span class="linenos">1207</span></a>        <span class="k">except</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">:</span>
</span><span id="find_entity-1208"><a href="#find_entity-1208"><span class="linenos">1208</span></a>            <span class="n">need_to_try_clr</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="find_entity-1209"><a href="#find_entity-1209"><span class="linenos">1209</span></a>        
</span><span id="find_entity-1210"><a href="#find_entity-1210"><span class="linenos">1210</span></a>        <span class="k">if</span> <span class="n">need_to_try_clr</span><span class="p">:</span>
</span><span id="find_entity-1211"><a href="#find_entity-1211"><span class="linenos">1211</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="find_entity-1212"><a href="#find_entity-1212"><span class="linenos">1212</span></a>                <span class="n">owner</span> <span class="o">=</span> <span class="n">get_cls_parameter</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1213"><a href="#find_entity-1213"><span class="linenos">1213</span></a>            <span class="k">except</span> <span class="n">AnAppropriateOwnerParameterWasNotFoundError</span><span class="p">:</span>
</span><span id="find_entity-1214"><a href="#find_entity-1214"><span class="linenos">1214</span></a>                <span class="k">pass</span>
</span><span id="find_entity-1215"><a href="#find_entity-1215"><span class="linenos">1215</span></a>        
</span><span id="find_entity-1216"><a href="#find_entity-1216"><span class="linenos">1216</span></a>        <span class="n">entity_code</span> <span class="o">=</span> <span class="n">entity</span><span class="o">.</span><span class="n">f_code</span>
</span><span id="find_entity-1217"><a href="#find_entity-1217"><span class="linenos">1217</span></a>        <span class="k">if</span> <span class="n">owner</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_entity-1218"><a href="#find_entity-1218"><span class="linenos">1218</span></a>            <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">getattr_ex</span><span class="p">(</span><span class="n">owner</span><span class="p">,</span> <span class="n">entity_name_str</span><span class="p">)</span>
</span><span id="find_entity-1219"><a href="#find_entity-1219"><span class="linenos">1219</span></a>            <span class="k">if</span> <span class="n">get_code</span><span class="p">(</span><span class="n">entity_instance</span><span class="p">)</span> <span class="ow">is</span> <span class="n">entity_code</span><span class="p">:</span>
</span><span id="find_entity-1220"><a href="#find_entity-1220"><span class="linenos">1220</span></a>                <span class="k">return</span> <span class="n">entity_instance</span>
</span><span id="find_entity-1221"><a href="#find_entity-1221"><span class="linenos">1221</span></a>        
</span><span id="find_entity-1222"><a href="#find_entity-1222"><span class="linenos">1222</span></a>        <span class="n">entity</span> <span class="o">=</span> <span class="n">entity_code</span>
</span><span id="find_entity-1223"><a href="#find_entity-1223"><span class="linenos">1223</span></a>    
</span><span id="find_entity-1224"><a href="#find_entity-1224"><span class="linenos">1224</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">entity</span><span class="p">,</span> <span class="n">CodeType</span><span class="p">):</span>
</span><span id="find_entity-1225"><a href="#find_entity-1225"><span class="linenos">1225</span></a>        <span class="n">entity_owner_instance</span> <span class="o">=</span> <span class="n">entity_owner</span><span class="p">(</span><span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1226"><a href="#find_entity-1226"><span class="linenos">1226</span></a>        <span class="n">entity_instance</span> <span class="o">=</span> <span class="n">find_method_in_module_by_code</span><span class="p">(</span><span class="n">entity_owner_instance</span><span class="p">,</span> <span class="n">entity</span><span class="p">)</span>
</span><span id="find_entity-1227"><a href="#find_entity-1227"><span class="linenos">1227</span></a>        <span class="k">if</span> <span class="n">entity_instance</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="find_entity-1228"><a href="#find_entity-1228"><span class="linenos">1228</span></a>            <span class="k">return</span> <span class="n">entity_instance</span>
</span><span id="find_entity-1229"><a href="#find_entity-1229"><span class="linenos">1229</span></a>    
</span><span id="find_entity-1230"><a href="#find_entity-1230"><span class="linenos">1230</span></a>    <span class="k">raise</span> <span class="n">EntityWasNotFoundError</span>
</span></pre></div>


    

                </section>
                <section id="find_current_entity">
                            <input id="find_current_entity-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">find_current_entity</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">depth</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="find_current_entity-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#find_current_entity"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="find_current_entity-1233"><a href="#find_current_entity-1233"><span class="linenos">1233</span></a><span class="k">def</span> <span class="nf">find_current_entity</span><span class="p">(</span><span class="n">depth</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="find_current_entity-1234"><a href="#find_current_entity-1234"><span class="linenos">1234</span></a>    <span class="k">return</span> <span class="n">find_entity</span><span class="p">(</span><span class="n">frame</span><span class="p">(</span><span class="n">depth</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>