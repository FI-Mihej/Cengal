---
title: text_translator
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.text_processing<wbr>.text_translator<wbr>.versions<wbr>.v_1<wbr>.text_translator    </h1>

                
                        <input id="mod-text_translator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-text_translator-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TextTranslationDictionary&#39;</span><span class="p">,</span> <span class="s1">&#39;TextEntityId&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslationLanguageId&#39;</span><span class="p">,</span> 
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>           <span class="s1">&#39;TextTranslatorError&#39;</span><span class="p">,</span> <span class="s1">&#39;TextTranslator&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslationLanguageMapper&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslationLanguageChooser&#39;</span><span class="p">,</span> 
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>           <span class="s1">&#39;TextTranslationReapplier&#39;</span><span class="p">,</span> <span class="s1">&#39;CoroPriority&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslationWorker&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslatableText&#39;</span><span class="p">,</span> <span class="s1">&#39;tt&#39;</span><span class="p">,</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>           <span class="s1">&#39;TranslateMe&#39;</span><span class="p">,</span> <span class="s1">&#39;TMe&#39;</span><span class="p">,</span> <span class="s1">&#39;tme&#39;</span><span class="p">,</span> <span class="s1">&#39;TranslatableTextElement&#39;</span><span class="p">,</span> <span class="s1">&#39;TTE&#39;</span><span class="p">]</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a><span class="kn">from</span> <span class="nn">collections.abc</span> <span class="kn">import</span> <span class="n">Mapping</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">TypeVar</span><span class="p">,</span> <span class="n">Generic</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.serialization</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.call_history_reapplier</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.sleep</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.wait_coro</span> <span class="kn">import</span> <span class="n">WaitCoroRequest</span><span class="p">,</span> <span class="n">CoroutineNotFoundError</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">is_callable</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a><span class="kn">from</span> <span class="nn">uuid</span> <span class="kn">import</span> <span class="n">uuid4</span>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a><span class="kn">import</span> <span class="nn">sys</span>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>
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
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.0&quot;</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a><span class="n">TranslationLanguageId</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="n">TextEntityId</span> <span class="o">=</span> <span class="n">Hashable</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a><span class="n">TextTranslationDictionary</span> <span class="o">=</span> <span class="n">Dict</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a><span class="sd">&#39;&#39;&#39;</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="sd">In Python:</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="sd">text_translation_dictionary = {</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="sd">    &#39;{str}&#39;: {</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="sd">        &#39;default&#39;: {  // Can be empty. &quot;Variants&quot; field must not be empty in this case.</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a><span class="sd">            &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="sd">            &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="sd">            ...</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="sd">        },</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="sd">        &#39;variants&#39;: {  // Can be empty. &quot;Default&quot; field must not be empty in this case.</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="sd">            &#39;{TextEntityId}&#39;: {</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="sd">                &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="sd">                &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="sd">                ...</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="sd">            },</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="sd">            &#39;{TextEntityId}&#39;: {</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a><span class="sd">                &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a><span class="sd">                &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="sd">                ...</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="sd">            },</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="sd">            ...</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="sd">        }</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="sd">    }</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="sd">}</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="sd">In JSON:</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="sd">{</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="sd">    &#39;type&#39;: &#39;Cengal.TextTranslationDictionary&#39;,</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="sd">    &#39;version&#39;: &#39;1.0.0&#39;</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="sd">    &#39;text_translation_list&#39;: [</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="sd">        {</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a><span class="sd">            &#39;text&#39;: &#39;{str}&#39;,</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="sd">            &#39;translations&#39;: {</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="sd">                &#39;default&#39;: {  // Can be empty. &quot;Variants&quot; field must not be empty in this case.</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="sd">                    &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="sd">                    &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="sd">                    ...</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="sd">                },</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="sd">                &#39;variants&#39;: {  // Can be empty. &quot;Default&quot; field must not be empty in this case.</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a><span class="sd">                    &#39;{TextEntityId}&#39;: {</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a><span class="sd">                        &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="sd">                        &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="sd">                        ...</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="sd">                    },</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="sd">                    &#39;{TextEntityId}&#39;: {</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a><span class="sd">                        &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a><span class="sd">                        &#39;{TranslationLanguageId}&#39;: &#39;{str}&#39;,</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="sd">                        ...</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a><span class="sd">                    },</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a><span class="sd">                    ...</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a><span class="sd">                }</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a><span class="sd">            }</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a><span class="sd">        }</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a><span class="sd">    ]</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a><span class="sd">}</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a><span class="sd">&#39;&#39;&#39;</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a><span class="n">TranslationLangToLangMap</span> <span class="o">=</span> <span class="n">Dict</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">,</span> <span class="n">TranslationLanguageId</span><span class="p">]</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a><span class="n">TranslationWorker</span> <span class="o">=</span> <span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="kc">None</span><span class="p">]</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a><span class="k">class</span> <span class="nc">TextTranslatorError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>    <span class="k">pass</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a><span class="k">class</span> <span class="nc">TextTranslator</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="nd">@classmethod</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">encoding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>        <span class="n">serializer</span> <span class="o">=</span> <span class="n">best_serializer_for_standard_data</span><span class="p">((</span><span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">),</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>                                <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_large</span><span class="p">,</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>                                <span class="mf">0.1</span><span class="p">)</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>        <span class="n">encoding</span> <span class="o">=</span> <span class="n">encoding</span> <span class="ow">or</span> <span class="s1">&#39;utf-8&#39;</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_data</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>            <span class="n">json_data</span> <span class="o">=</span> <span class="n">json_data</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">)</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>        <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_data</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">,</span> <span class="n">Mapping</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: root must be a dict&#39;</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>        <span class="k">if</span> <span class="s1">&#39;Cengal.TextTranslationDictionary&#39;</span> <span class="o">!=</span> <span class="n">decoded_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;type&#39;</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: lack of &quot;type&quot; field or a &quot;type&quot; field value mismatch&#39;</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>            <span class="n">text_translation_dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>            <span class="n">text_translation_list</span> <span class="o">=</span> <span class="n">decoded_data</span><span class="p">[</span><span class="s1">&#39;text_translation_list&#39;</span><span class="p">]</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">text_translation_list</span><span class="p">:</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>                <span class="n">text_translation_dictionary</span><span class="p">[</span><span class="n">item</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s1">&#39;translations&#39;</span><span class="p">]</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">text_translation_dictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">)</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="k">except</span> <span class="p">(</span><span class="ne">KeyError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">):</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data or other parsing error&#39;</span><span class="p">)</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dictionary</span> <span class="o">=</span> <span class="n">dictionary</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">decoded_data</span> <span class="o">=</span> <span class="n">decoded_data</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>            <span class="n">translations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dictionary</span><span class="p">[</span><span class="n">text</span><span class="p">]</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>                <span class="n">variant</span> <span class="o">=</span> <span class="n">translations</span><span class="p">[</span><span class="s1">&#39;default&#39;</span><span class="p">]</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>                <span class="n">variant</span> <span class="o">=</span> <span class="n">translations</span><span class="p">[</span><span class="s1">&#39;variants&#39;</span><span class="p">][</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>            <span class="k">return</span> <span class="n">variant</span><span class="p">[</span><span class="n">language</span><span class="p">]</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>            <span class="k">return</span> <span class="n">text</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a><span class="k">class</span> <span class="nc">TranslationLanguageMapper</span><span class="p">:</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span><span class="p">,</span> <span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span> <span class="o">=</span> <span class="n">lang_2_lang</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span> <span class="o">=</span> <span class="n">default_lang</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_2_lang</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lang</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_lang</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a><span class="k">class</span> <span class="nc">TranslationLanguageChooser</span><span class="p">:</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> 
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>                 <span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span><span class="p">,</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>                 <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span> <span class="o">=</span> <span class="n">translation_language_mapper</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">coro_scheduler</span> <span class="ow">or</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid4</span><span class="p">())</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>    
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a>    <span class="nd">@property</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a>    <span class="k">def</span> <span class="nf">lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>    
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>    <span class="nd">@lang</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="k">def</span> <span class="nf">lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span> <span class="o">=</span> <span class="n">language</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_mapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">)</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>        
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>        <span class="c1"># def raise_translation_language_changed_event(</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="c1">#     interface: Interface,</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>        <span class="c1">#     translation_language_changed_event: str,</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="c1">#     lang: TranslationLanguageId,</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>        <span class="c1">#     end_lang: TranslationLanguageId</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>        <span class="c1">#     ):</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="c1">#     with log_uncatched_exception():</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="c1">#         print(&#39;raise_translation_language_changed_event - raising event...&#39;)</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="c1">#         print(interface, translation_language_changed_event, lang, end_lang)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="c1">#         interface(Sleep, 1.0)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="c1">#         interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="c1">#         interface(Sleep, 1.0)</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="c1">#         print(&#39;raise_translation_language_changed_event - done&#39;)</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>        <span class="c1"># try_put_coro_to(get_interface_and_loop_with_explicit_loop(self.coro_scheduler), raise_translation_language_changed_event, </span>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>        <span class="c1">#         self.translation_language_changed_event, self._lang, self._end_lang)</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a>        <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">),</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">)</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>    <span class="c1"># @staticmethod</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>    <span class="c1"># def raise_translation_language_changed_event(</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>    <span class="c1">#     interface: Interface,</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>    <span class="c1">#     translation_language_changed_event: str,</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>    <span class="c1">#     lang: TranslationLanguageId,</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>    <span class="c1">#     end_lang: TranslationLanguageId</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>    <span class="c1">#     ):</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>    <span class="c1">#     print(&#39;raise_translation_language_changed_event - raising event...&#39;)</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>    <span class="c1">#     print(interface, translation_language_changed_event, lang, end_lang)</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>    <span class="c1">#     interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>    <span class="c1">#     print(&#39;raise_translation_language_changed_event - done&#39;)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>    
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>    <span class="k">def</span> <span class="nf">set_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslationLanguageChooser&#39;</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a><span class="w">        </span><span class="sd">&#39;&#39;&#39;</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a><span class="sd">        For usage with ArgsManager like</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a><span class="sd">                am = ArgsManager(</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a><span class="sd">                    EArgs(text_translator=TranslationLanguageChooser(</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a><span class="sd">                        TextTranslator.from_json(TEXT_DICTIONARY), </span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a><span class="sd">                        TranslationLanguageMapper(TRANSLATION_LANGUAGE_MAP, &#39;en&#39;)).set_lang(&#39;ru&#39;))</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a><span class="sd">                )</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a><span class="sd">        &#39;&#39;&#39;</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang</span> <span class="o">=</span> <span class="n">language</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>    
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>    <span class="nd">@property</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>    <span class="k">def</span> <span class="nf">end_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>    
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>    <span class="nd">@end_lang</span><span class="o">.</span><span class="n">setter</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>    <span class="k">def</span> <span class="nf">end_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="k">pass</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>    
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a><span class="k">class</span> <span class="nc">TextTranslationReapplier</span><span class="p">(</span><span class="n">CallHistoryReapplier</span><span class="p">):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="o">=</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">):</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>    
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>    <span class="k">def</span> <span class="nf">_translate_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">):</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="k">return</span> <span class="n">value</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>    
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>    <span class="k">def</span> <span class="nf">call_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">TranslationWorker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>            <span class="n">new_args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">))</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="n">new_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>            <span class="n">new_kwargs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>        
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="n">text_template</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="k">if</span> <span class="n">new_kwargs</span><span class="p">:</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;There are tt items in kwargs, however text_template is None&#39;</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">new_args</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="n">text_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">new_args</span><span class="p">,</span> <span class="o">**</span><span class="n">new_kwargs</span><span class="p">)</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="n">translation_worker</span><span class="p">(</span><span class="n">translated_text</span><span class="p">)</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">args_to_key_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="k">return</span> <span class="p">((</span><span class="n">entity_id</span><span class="p">,</span> <span class="nb">id</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">field</span><span class="p">),</span> <span class="p">(</span><span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">))</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>    
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>    <span class="k">def</span> <span class="nf">key_value_to_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>        <span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span> <span class="o">=</span> <span class="n">key</span>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">([</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">]</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>        <span class="k">return</span> <span class="n">new_args</span><span class="p">,</span> <span class="n">kwargs</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a><span class="k">class</span> <span class="nc">TranslatableText</span><span class="p">:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">],</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">text</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">formatter</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_awaitable</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>    
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="k">if</span> <span class="n">is_callable</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">):</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">()</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>    
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>            <span class="k">return</span> <span class="n">text</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>    
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a><span class="n">tt</span> <span class="o">=</span> <span class="n">TranslatableText</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a><span class="k">class</span> <span class="nc">TranslateMe</span><span class="p">:</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]]</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_contains_translatable_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_contains_translatable_text</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>    
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>    <span class="k">def</span> <span class="nf">to_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">arg</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text_translator</span><span class="p">(</span><span class="n">language</span><span class="p">,</span> <span class="n">arg</span><span class="p">(),</span> <span class="n">arg</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">else</span> <span class="n">arg</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">])</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>    <span class="k">def</span> <span class="nf">tte</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslateMe&#39;</span><span class="p">:</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span> <span class="o">=</span> <span class="n">tte</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>    
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span><span class="o">.</span><span class="n">translate_me</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a><span class="n">TMe</span> <span class="o">=</span> <span class="n">TranslateMe</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a><span class="n">tme</span> <span class="o">=</span> <span class="n">TranslateMe</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="n">T</span> <span class="o">=</span> <span class="n">TypeVar</span><span class="p">(</span><span class="s1">&#39;T&#39;</span><span class="p">)</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a><span class="k">class</span> <span class="nc">TranslatableTextElement</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">T</span><span class="p">]):</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">text_translator</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>    
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_element</span><span class="p">:</span> <span class="n">T</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">set_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_element</span><span class="p">:</span> <span class="n">T</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">TranslateMe</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">T</span><span class="p">:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>    <span class="k">def</span> <span class="nf">translate_me</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">translate_me</span><span class="p">:</span> <span class="n">TranslateMe</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>        <span class="k">return</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">end_lang</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>    <span class="k">def</span> <span class="nf">start_translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>        <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_reapplier</span><span class="p">)</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>    
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>        <span class="n">waiting_set</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="p">{</span><span class="n">i</span><span class="o">.</span><span class="n">coro_id</span><span class="p">}</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="c1"># await i(WaitCoroRequest().list(waiting_set))  # TODO: Not Implemented currently</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">waiting_set</span><span class="p">:</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>                <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">WaitCoroRequest</span><span class="p">()</span><span class="o">.</span><span class="n">single</span><span class="p">(</span><span class="n">coro_id</span><span class="p">))</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>            <span class="k">except</span> <span class="n">CoroutineNotFoundError</span><span class="p">:</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>                <span class="k">pass</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>        
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="n">waiting_set</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>        
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="k">return</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>        
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        <span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">)()</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="k">for</span> <span class="n">lang</span><span class="p">,</span> <span class="n">end_lang</span> <span class="ow">in</span> <span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>            <span class="k">for</span> <span class="n">text_element</span><span class="p">,</span> <span class="n">translate_me</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>                <span class="n">text_element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="n">end_lang</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>    <span class="k">def</span> <span class="nf">register_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">remove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aremove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>    
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>    <span class="k">def</span> <span class="nf">on_lang_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]):</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>        <span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">start_translation_reapplier</span><span class="p">)</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="n">TTE</span> <span class="o">=</span> <span class="n">TranslatableTextElement</span>
</span></pre></div>


            </section>
                <section id="TextTranslationDictionary">
                    <div class="attr variable">
            <span class="name">TextTranslationDictionary</span>        =
<span class="default_value">typing.Dict</span>

        
    </div>
    <a class="headerlink" href="#TextTranslationDictionary"></a>
    
            <div class="docstring"><p>In Python:
text_translation_dictionary = {
    '{str}': {
        'default': {  // Can be empty. "Variants" field must not be empty in this case.
            '{TranslationLanguageId}': '{str}',
            '{TranslationLanguageId}': '{str}',
            ...
        },
        'variants': {  // Can be empty. "Default" field must not be empty in this case.
            '{TextEntityId}': {
                '{TranslationLanguageId}': '{str}',
                '{TranslationLanguageId}': '{str}',
                ...
            },
            '{TextEntityId}': {
                '{TranslationLanguageId}': '{str}',
                '{TranslationLanguageId}': '{str}',
                ...
            },
            ...
        }
    }
}</p>

<p>In JSON:
{
    'type': 'Cengal.TextTranslationDictionary',
    'version': '1.0.0'
    'text_translation_list': [
        {
            'text': '{str}',
            'translations': {
                'default': {  // Can be empty. "Variants" field must not be empty in this case.
                    '{TranslationLanguageId}': '{str}',
                    '{TranslationLanguageId}': '{str}',
                    ...
                },
                'variants': {  // Can be empty. "Default" field must not be empty in this case.
                    '{TextEntityId}': {
                        '{TranslationLanguageId}': '{str}',
                        '{TranslationLanguageId}': '{str}',
                        ...
                    },
                    '{TextEntityId}': {
                        '{TranslationLanguageId}': '{str}',
                        '{TranslationLanguageId}': '{str}',
                        ...
                    },
                    ...
                }
            }
        }
    ]
}</p>
</div>


                </section>
                <section id="TextEntityId">
                    <div class="attr variable">
            <span class="name">TextEntityId</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#TextEntityId"></a>
    
    

                </section>
                <section id="TranslationLanguageId">
                    <div class="attr variable">
            <span class="name">TranslationLanguageId</span>        =
<span class="default_value">typing.Hashable</span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageId"></a>
    
    

                </section>
                <section id="TextTranslatorError">
                            <input id="TextTranslatorError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TextTranslatorError</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="TextTranslatorError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslatorError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslatorError-120"><a href="#TextTranslatorError-120"><span class="linenos">120</span></a><span class="k">class</span> <span class="nc">TextTranslatorError</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="TextTranslatorError-121"><a href="#TextTranslatorError-121"><span class="linenos">121</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="TextTranslatorError.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="TextTranslatorError.with_traceback" class="function">with_traceback</dd>
                <dd id="TextTranslatorError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TextTranslator">
                            <input id="TextTranslator-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TextTranslator</span>:

                <label class="view-source-button" for="TextTranslator-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslator"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslator-123"><a href="#TextTranslator-123"><span class="linenos">123</span></a><span class="k">class</span> <span class="nc">TextTranslator</span><span class="p">:</span>
</span><span id="TextTranslator-124"><a href="#TextTranslator-124"><span class="linenos">124</span></a>    <span class="nd">@classmethod</span>
</span><span id="TextTranslator-125"><a href="#TextTranslator-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">encoding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TextTranslator-126"><a href="#TextTranslator-126"><span class="linenos">126</span></a>        <span class="n">serializer</span> <span class="o">=</span> <span class="n">best_serializer_for_standard_data</span><span class="p">((</span><span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="TextTranslator-127"><a href="#TextTranslator-127"><span class="linenos">127</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="TextTranslator-128"><a href="#TextTranslator-128"><span class="linenos">128</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="TextTranslator-129"><a href="#TextTranslator-129"><span class="linenos">129</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="TextTranslator-130"><a href="#TextTranslator-130"><span class="linenos">130</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">),</span>
</span><span id="TextTranslator-131"><a href="#TextTranslator-131"><span class="linenos">131</span></a>                                <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_large</span><span class="p">,</span>
</span><span id="TextTranslator-132"><a href="#TextTranslator-132"><span class="linenos">132</span></a>                                <span class="mf">0.1</span><span class="p">)</span>
</span><span id="TextTranslator-133"><a href="#TextTranslator-133"><span class="linenos">133</span></a>        <span class="n">encoding</span> <span class="o">=</span> <span class="n">encoding</span> <span class="ow">or</span> <span class="s1">&#39;utf-8&#39;</span>
</span><span id="TextTranslator-134"><a href="#TextTranslator-134"><span class="linenos">134</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_data</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="TextTranslator-135"><a href="#TextTranslator-135"><span class="linenos">135</span></a>            <span class="n">json_data</span> <span class="o">=</span> <span class="n">json_data</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">)</span>
</span><span id="TextTranslator-136"><a href="#TextTranslator-136"><span class="linenos">136</span></a>        <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_data</span><span class="p">)</span>
</span><span id="TextTranslator-137"><a href="#TextTranslator-137"><span class="linenos">137</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">,</span> <span class="n">Mapping</span><span class="p">):</span>
</span><span id="TextTranslator-138"><a href="#TextTranslator-138"><span class="linenos">138</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: root must be a dict&#39;</span><span class="p">)</span>
</span><span id="TextTranslator-139"><a href="#TextTranslator-139"><span class="linenos">139</span></a>        <span class="k">if</span> <span class="s1">&#39;Cengal.TextTranslationDictionary&#39;</span> <span class="o">!=</span> <span class="n">decoded_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;type&#39;</span><span class="p">):</span>
</span><span id="TextTranslator-140"><a href="#TextTranslator-140"><span class="linenos">140</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: lack of &quot;type&quot; field or a &quot;type&quot; field value mismatch&#39;</span><span class="p">)</span>
</span><span id="TextTranslator-141"><a href="#TextTranslator-141"><span class="linenos">141</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TextTranslator-142"><a href="#TextTranslator-142"><span class="linenos">142</span></a>            <span class="n">text_translation_dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TextTranslator-143"><a href="#TextTranslator-143"><span class="linenos">143</span></a>            <span class="n">text_translation_list</span> <span class="o">=</span> <span class="n">decoded_data</span><span class="p">[</span><span class="s1">&#39;text_translation_list&#39;</span><span class="p">]</span>
</span><span id="TextTranslator-144"><a href="#TextTranslator-144"><span class="linenos">144</span></a>            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">text_translation_list</span><span class="p">:</span>
</span><span id="TextTranslator-145"><a href="#TextTranslator-145"><span class="linenos">145</span></a>                <span class="n">text_translation_dictionary</span><span class="p">[</span><span class="n">item</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s1">&#39;translations&#39;</span><span class="p">]</span>
</span><span id="TextTranslator-146"><a href="#TextTranslator-146"><span class="linenos">146</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">text_translation_dictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">)</span>
</span><span id="TextTranslator-147"><a href="#TextTranslator-147"><span class="linenos">147</span></a>        <span class="k">except</span> <span class="p">(</span><span class="ne">KeyError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">):</span>
</span><span id="TextTranslator-148"><a href="#TextTranslator-148"><span class="linenos">148</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data or other parsing error&#39;</span><span class="p">)</span>
</span><span id="TextTranslator-149"><a href="#TextTranslator-149"><span class="linenos">149</span></a>    
</span><span id="TextTranslator-150"><a href="#TextTranslator-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TextTranslator-151"><a href="#TextTranslator-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dictionary</span> <span class="o">=</span> <span class="n">dictionary</span>
</span><span id="TextTranslator-152"><a href="#TextTranslator-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">decoded_data</span> <span class="o">=</span> <span class="n">decoded_data</span>
</span><span id="TextTranslator-153"><a href="#TextTranslator-153"><span class="linenos">153</span></a>    
</span><span id="TextTranslator-154"><a href="#TextTranslator-154"><span class="linenos">154</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TextTranslator-155"><a href="#TextTranslator-155"><span class="linenos">155</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TextTranslator-156"><a href="#TextTranslator-156"><span class="linenos">156</span></a>            <span class="n">translations</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dictionary</span><span class="p">[</span><span class="n">text</span><span class="p">]</span>
</span><span id="TextTranslator-157"><a href="#TextTranslator-157"><span class="linenos">157</span></a>            <span class="k">if</span> <span class="n">entity_id</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TextTranslator-158"><a href="#TextTranslator-158"><span class="linenos">158</span></a>                <span class="n">variant</span> <span class="o">=</span> <span class="n">translations</span><span class="p">[</span><span class="s1">&#39;default&#39;</span><span class="p">]</span>
</span><span id="TextTranslator-159"><a href="#TextTranslator-159"><span class="linenos">159</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TextTranslator-160"><a href="#TextTranslator-160"><span class="linenos">160</span></a>                <span class="n">variant</span> <span class="o">=</span> <span class="n">translations</span><span class="p">[</span><span class="s1">&#39;variants&#39;</span><span class="p">][</span><span class="n">entity_id</span><span class="p">]</span>
</span><span id="TextTranslator-161"><a href="#TextTranslator-161"><span class="linenos">161</span></a>            <span class="k">return</span> <span class="n">variant</span><span class="p">[</span><span class="n">language</span><span class="p">]</span>
</span><span id="TextTranslator-162"><a href="#TextTranslator-162"><span class="linenos">162</span></a>        <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
</span><span id="TextTranslator-163"><a href="#TextTranslator-163"><span class="linenos">163</span></a>            <span class="k">return</span> <span class="n">text</span>
</span></pre></div>


    

                            <div id="TextTranslator.__init__" class="classattr">
                                        <input id="TextTranslator.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TextTranslator</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">dictionary</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span>,</span><span class="param">	<span class="n">decoded_data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="TextTranslator.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslator.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslator.__init__-150"><a href="#TextTranslator.__init__-150"><span class="linenos">150</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Dict</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TextTranslator.__init__-151"><a href="#TextTranslator.__init__-151"><span class="linenos">151</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">dictionary</span> <span class="o">=</span> <span class="n">dictionary</span>
</span><span id="TextTranslator.__init__-152"><a href="#TextTranslator.__init__-152"><span class="linenos">152</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">decoded_data</span> <span class="o">=</span> <span class="n">decoded_data</span>
</span></pre></div>


    

                            </div>
                            <div id="TextTranslator.from_json" class="classattr">
                                        <input id="TextTranslator.from_json-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@classmethod</div>

        <span class="def">def</span>
        <span class="name">from_json</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">cls</span>,</span><span class="param">	<span class="n">json_data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span>,</span><span class="param">	<span class="n">encoding</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TextTranslator.from_json-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslator.from_json"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslator.from_json-124"><a href="#TextTranslator.from_json-124"><span class="linenos">124</span></a>    <span class="nd">@classmethod</span>
</span><span id="TextTranslator.from_json-125"><a href="#TextTranslator.from_json-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">from_json</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">json_data</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">bytes</span><span class="p">,</span> <span class="nb">str</span><span class="p">],</span> <span class="n">encoding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TextTranslator.from_json-126"><a href="#TextTranslator.from_json-126"><span class="linenos">126</span></a>        <span class="n">serializer</span> <span class="o">=</span> <span class="n">best_serializer_for_standard_data</span><span class="p">((</span><span class="n">DataFormats</span><span class="o">.</span><span class="n">json</span><span class="p">,</span>
</span><span id="TextTranslator.from_json-127"><a href="#TextTranslator.from_json-127"><span class="linenos">127</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_str_as_str</span><span class="p">,</span>
</span><span id="TextTranslator.from_json-128"><a href="#TextTranslator.from_json-128"><span class="linenos">128</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">decode_list_as_list</span><span class="p">,</span>
</span><span id="TextTranslator.from_json-129"><a href="#TextTranslator.from_json-129"><span class="linenos">129</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">superficial</span><span class="p">,</span>
</span><span id="TextTranslator.from_json-130"><a href="#TextTranslator.from_json-130"><span class="linenos">130</span></a>                                 <span class="n">Tags</span><span class="o">.</span><span class="n">current_platform</span><span class="p">),</span>
</span><span id="TextTranslator.from_json-131"><a href="#TextTranslator.from_json-131"><span class="linenos">131</span></a>                                <span class="n">TestDataType</span><span class="o">.</span><span class="n">deep_large</span><span class="p">,</span>
</span><span id="TextTranslator.from_json-132"><a href="#TextTranslator.from_json-132"><span class="linenos">132</span></a>                                <span class="mf">0.1</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-133"><a href="#TextTranslator.from_json-133"><span class="linenos">133</span></a>        <span class="n">encoding</span> <span class="o">=</span> <span class="n">encoding</span> <span class="ow">or</span> <span class="s1">&#39;utf-8&#39;</span>
</span><span id="TextTranslator.from_json-134"><a href="#TextTranslator.from_json-134"><span class="linenos">134</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">json_data</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">):</span>
</span><span id="TextTranslator.from_json-135"><a href="#TextTranslator.from_json-135"><span class="linenos">135</span></a>            <span class="n">json_data</span> <span class="o">=</span> <span class="n">json_data</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">encoding</span><span class="o">=</span><span class="n">encoding</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-136"><a href="#TextTranslator.from_json-136"><span class="linenos">136</span></a>        <span class="n">decoded_data</span><span class="p">:</span> <span class="n">Dict</span> <span class="o">=</span> <span class="n">serializer</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">json_data</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-137"><a href="#TextTranslator.from_json-137"><span class="linenos">137</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">decoded_data</span><span class="p">,</span> <span class="n">Mapping</span><span class="p">):</span>
</span><span id="TextTranslator.from_json-138"><a href="#TextTranslator.from_json-138"><span class="linenos">138</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: root must be a dict&#39;</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-139"><a href="#TextTranslator.from_json-139"><span class="linenos">139</span></a>        <span class="k">if</span> <span class="s1">&#39;Cengal.TextTranslationDictionary&#39;</span> <span class="o">!=</span> <span class="n">decoded_data</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">&#39;type&#39;</span><span class="p">):</span>
</span><span id="TextTranslator.from_json-140"><a href="#TextTranslator.from_json-140"><span class="linenos">140</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data: lack of &quot;type&quot; field or a &quot;type&quot; field value mismatch&#39;</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-141"><a href="#TextTranslator.from_json-141"><span class="linenos">141</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TextTranslator.from_json-142"><a href="#TextTranslator.from_json-142"><span class="linenos">142</span></a>            <span class="n">text_translation_dictionary</span><span class="p">:</span> <span class="n">TextTranslationDictionary</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TextTranslator.from_json-143"><a href="#TextTranslator.from_json-143"><span class="linenos">143</span></a>            <span class="n">text_translation_list</span> <span class="o">=</span> <span class="n">decoded_data</span><span class="p">[</span><span class="s1">&#39;text_translation_list&#39;</span><span class="p">]</span>
</span><span id="TextTranslator.from_json-144"><a href="#TextTranslator.from_json-144"><span class="linenos">144</span></a>            <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">text_translation_list</span><span class="p">:</span>
</span><span id="TextTranslator.from_json-145"><a href="#TextTranslator.from_json-145"><span class="linenos">145</span></a>                <span class="n">text_translation_dictionary</span><span class="p">[</span><span class="n">item</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="n">item</span><span class="p">[</span><span class="s1">&#39;translations&#39;</span><span class="p">]</span>
</span><span id="TextTranslator.from_json-146"><a href="#TextTranslator.from_json-146"><span class="linenos">146</span></a>            <span class="k">return</span> <span class="bp">cls</span><span class="p">(</span><span class="n">text_translation_dictionary</span><span class="p">,</span> <span class="n">decoded_data</span><span class="p">)</span>
</span><span id="TextTranslator.from_json-147"><a href="#TextTranslator.from_json-147"><span class="linenos">147</span></a>        <span class="k">except</span> <span class="p">(</span><span class="ne">KeyError</span><span class="p">,</span> <span class="ne">TypeError</span><span class="p">):</span>
</span><span id="TextTranslator.from_json-148"><a href="#TextTranslator.from_json-148"><span class="linenos">148</span></a>            <span class="k">raise</span> <span class="n">TextTranslatorError</span><span class="p">(</span><span class="s1">&#39;Wrong json data or other parsing error&#39;</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TextTranslator.dictionary" class="classattr">
                                <div class="attr variable">
            <span class="name">dictionary</span>

        
    </div>
    <a class="headerlink" href="#TextTranslator.dictionary"></a>
    
    

                            </div>
                            <div id="TextTranslator.decoded_data" class="classattr">
                                <div class="attr variable">
            <span class="name">decoded_data</span>

        
    </div>
    <a class="headerlink" href="#TextTranslator.decoded_data"></a>
    
    

                            </div>
                </section>
                <section id="TranslationLanguageMapper">
                            <input id="TranslationLanguageMapper-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TranslationLanguageMapper</span>:

                <label class="view-source-button" for="TranslationLanguageMapper-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageMapper"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageMapper-166"><a href="#TranslationLanguageMapper-166"><span class="linenos">166</span></a><span class="k">class</span> <span class="nc">TranslationLanguageMapper</span><span class="p">:</span>
</span><span id="TranslationLanguageMapper-167"><a href="#TranslationLanguageMapper-167"><span class="linenos">167</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span><span class="p">,</span> <span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="TranslationLanguageMapper-168"><a href="#TranslationLanguageMapper-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span> <span class="o">=</span> <span class="n">lang_2_lang</span>
</span><span id="TranslationLanguageMapper-169"><a href="#TranslationLanguageMapper-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span> <span class="o">=</span> <span class="n">default_lang</span>
</span><span id="TranslationLanguageMapper-170"><a href="#TranslationLanguageMapper-170"><span class="linenos">170</span></a>    
</span><span id="TranslationLanguageMapper-171"><a href="#TranslationLanguageMapper-171"><span class="linenos">171</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="TranslationLanguageMapper-172"><a href="#TranslationLanguageMapper-172"><span class="linenos">172</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_2_lang</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">lang</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">default_lang</span>
</span></pre></div>


    

                            <div id="TranslationLanguageMapper.__init__" class="classattr">
                                        <input id="TranslationLanguageMapper.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TranslationLanguageMapper</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Dict</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span><span class="p">]</span>,</span><span class="param">	<span class="n">default_lang</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span>)</span>

                <label class="view-source-button" for="TranslationLanguageMapper.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageMapper.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageMapper.__init__-167"><a href="#TranslationLanguageMapper.__init__-167"><span class="linenos">167</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span><span class="p">,</span> <span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="TranslationLanguageMapper.__init__-168"><a href="#TranslationLanguageMapper.__init__-168"><span class="linenos">168</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_2_lang</span><span class="p">:</span> <span class="n">TranslationLangToLangMap</span> <span class="o">=</span> <span class="n">lang_2_lang</span>
</span><span id="TranslationLanguageMapper.__init__-169"><a href="#TranslationLanguageMapper.__init__-169"><span class="linenos">169</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">default_lang</span><span class="p">:</span> <span class="n">TranslationLanguageId</span> <span class="o">=</span> <span class="n">default_lang</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslationLanguageMapper.lang_2_lang" class="classattr">
                                <div class="attr variable">
            <span class="name">lang_2_lang</span><span class="annotation">: Dict[Hashable, Hashable]</span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageMapper.lang_2_lang"></a>
    
    

                            </div>
                            <div id="TranslationLanguageMapper.default_lang" class="classattr">
                                <div class="attr variable">
            <span class="name">default_lang</span><span class="annotation">: Hashable</span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageMapper.default_lang"></a>
    
    

                            </div>
                </section>
                <section id="TranslationLanguageChooser">
                            <input id="TranslationLanguageChooser-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TranslationLanguageChooser</span>:

                <label class="view-source-button" for="TranslationLanguageChooser-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageChooser"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageChooser-175"><a href="#TranslationLanguageChooser-175"><span class="linenos">175</span></a><span class="k">class</span> <span class="nc">TranslationLanguageChooser</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser-176"><a href="#TranslationLanguageChooser-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> 
</span><span id="TranslationLanguageChooser-177"><a href="#TranslationLanguageChooser-177"><span class="linenos">177</span></a>                 <span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span><span class="p">,</span>
</span><span id="TranslationLanguageChooser-178"><a href="#TranslationLanguageChooser-178"><span class="linenos">178</span></a>                 <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TranslationLanguageChooser-179"><a href="#TranslationLanguageChooser-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TranslationLanguageChooser-180"><a href="#TranslationLanguageChooser-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TranslationLanguageChooser-181"><a href="#TranslationLanguageChooser-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="TranslationLanguageChooser-182"><a href="#TranslationLanguageChooser-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span> <span class="o">=</span> <span class="n">translation_language_mapper</span>
</span><span id="TranslationLanguageChooser-183"><a href="#TranslationLanguageChooser-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">coro_scheduler</span> <span class="ow">or</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="TranslationLanguageChooser-184"><a href="#TranslationLanguageChooser-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid4</span><span class="p">())</span>
</span><span id="TranslationLanguageChooser-185"><a href="#TranslationLanguageChooser-185"><span class="linenos">185</span></a>    
</span><span id="TranslationLanguageChooser-186"><a href="#TranslationLanguageChooser-186"><span class="linenos">186</span></a>    <span class="nd">@property</span>
</span><span id="TranslationLanguageChooser-187"><a href="#TranslationLanguageChooser-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser-188"><a href="#TranslationLanguageChooser-188"><span class="linenos">188</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span>
</span><span id="TranslationLanguageChooser-189"><a href="#TranslationLanguageChooser-189"><span class="linenos">189</span></a>    
</span><span id="TranslationLanguageChooser-190"><a href="#TranslationLanguageChooser-190"><span class="linenos">190</span></a>    <span class="nd">@lang</span><span class="o">.</span><span class="n">setter</span>
</span><span id="TranslationLanguageChooser-191"><a href="#TranslationLanguageChooser-191"><span class="linenos">191</span></a>    <span class="k">def</span> <span class="nf">lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="TranslationLanguageChooser-192"><a href="#TranslationLanguageChooser-192"><span class="linenos">192</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span> <span class="o">=</span> <span class="n">language</span>
</span><span id="TranslationLanguageChooser-193"><a href="#TranslationLanguageChooser-193"><span class="linenos">193</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_mapper</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">)</span>
</span><span id="TranslationLanguageChooser-194"><a href="#TranslationLanguageChooser-194"><span class="linenos">194</span></a>        
</span><span id="TranslationLanguageChooser-195"><a href="#TranslationLanguageChooser-195"><span class="linenos">195</span></a>        <span class="c1"># def raise_translation_language_changed_event(</span>
</span><span id="TranslationLanguageChooser-196"><a href="#TranslationLanguageChooser-196"><span class="linenos">196</span></a>        <span class="c1">#     interface: Interface,</span>
</span><span id="TranslationLanguageChooser-197"><a href="#TranslationLanguageChooser-197"><span class="linenos">197</span></a>        <span class="c1">#     translation_language_changed_event: str,</span>
</span><span id="TranslationLanguageChooser-198"><a href="#TranslationLanguageChooser-198"><span class="linenos">198</span></a>        <span class="c1">#     lang: TranslationLanguageId,</span>
</span><span id="TranslationLanguageChooser-199"><a href="#TranslationLanguageChooser-199"><span class="linenos">199</span></a>        <span class="c1">#     end_lang: TranslationLanguageId</span>
</span><span id="TranslationLanguageChooser-200"><a href="#TranslationLanguageChooser-200"><span class="linenos">200</span></a>        <span class="c1">#     ):</span>
</span><span id="TranslationLanguageChooser-201"><a href="#TranslationLanguageChooser-201"><span class="linenos">201</span></a>        <span class="c1">#     with log_uncatched_exception():</span>
</span><span id="TranslationLanguageChooser-202"><a href="#TranslationLanguageChooser-202"><span class="linenos">202</span></a>        <span class="c1">#         print(&#39;raise_translation_language_changed_event - raising event...&#39;)</span>
</span><span id="TranslationLanguageChooser-203"><a href="#TranslationLanguageChooser-203"><span class="linenos">203</span></a>        <span class="c1">#         print(interface, translation_language_changed_event, lang, end_lang)</span>
</span><span id="TranslationLanguageChooser-204"><a href="#TranslationLanguageChooser-204"><span class="linenos">204</span></a>        <span class="c1">#         interface(Sleep, 1.0)</span>
</span><span id="TranslationLanguageChooser-205"><a href="#TranslationLanguageChooser-205"><span class="linenos">205</span></a>        <span class="c1">#         interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))</span>
</span><span id="TranslationLanguageChooser-206"><a href="#TranslationLanguageChooser-206"><span class="linenos">206</span></a>        <span class="c1">#         interface(Sleep, 1.0)</span>
</span><span id="TranslationLanguageChooser-207"><a href="#TranslationLanguageChooser-207"><span class="linenos">207</span></a>        <span class="c1">#         print(&#39;raise_translation_language_changed_event - done&#39;)</span>
</span><span id="TranslationLanguageChooser-208"><a href="#TranslationLanguageChooser-208"><span class="linenos">208</span></a>        
</span><span id="TranslationLanguageChooser-209"><a href="#TranslationLanguageChooser-209"><span class="linenos">209</span></a>        <span class="c1"># try_put_coro_to(get_interface_and_loop_with_explicit_loop(self.coro_scheduler), raise_translation_language_changed_event, </span>
</span><span id="TranslationLanguageChooser-210"><a href="#TranslationLanguageChooser-210"><span class="linenos">210</span></a>        <span class="c1">#         self.translation_language_changed_event, self._lang, self._end_lang)</span>
</span><span id="TranslationLanguageChooser-211"><a href="#TranslationLanguageChooser-211"><span class="linenos">211</span></a>        <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">),</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">high</span><span class="p">)</span>
</span><span id="TranslationLanguageChooser-212"><a href="#TranslationLanguageChooser-212"><span class="linenos">212</span></a>    
</span><span id="TranslationLanguageChooser-213"><a href="#TranslationLanguageChooser-213"><span class="linenos">213</span></a>    <span class="c1"># @staticmethod</span>
</span><span id="TranslationLanguageChooser-214"><a href="#TranslationLanguageChooser-214"><span class="linenos">214</span></a>    <span class="c1"># def raise_translation_language_changed_event(</span>
</span><span id="TranslationLanguageChooser-215"><a href="#TranslationLanguageChooser-215"><span class="linenos">215</span></a>    <span class="c1">#     interface: Interface,</span>
</span><span id="TranslationLanguageChooser-216"><a href="#TranslationLanguageChooser-216"><span class="linenos">216</span></a>    <span class="c1">#     translation_language_changed_event: str,</span>
</span><span id="TranslationLanguageChooser-217"><a href="#TranslationLanguageChooser-217"><span class="linenos">217</span></a>    <span class="c1">#     lang: TranslationLanguageId,</span>
</span><span id="TranslationLanguageChooser-218"><a href="#TranslationLanguageChooser-218"><span class="linenos">218</span></a>    <span class="c1">#     end_lang: TranslationLanguageId</span>
</span><span id="TranslationLanguageChooser-219"><a href="#TranslationLanguageChooser-219"><span class="linenos">219</span></a>    <span class="c1">#     ):</span>
</span><span id="TranslationLanguageChooser-220"><a href="#TranslationLanguageChooser-220"><span class="linenos">220</span></a>    <span class="c1">#     print(&#39;raise_translation_language_changed_event - raising event...&#39;)</span>
</span><span id="TranslationLanguageChooser-221"><a href="#TranslationLanguageChooser-221"><span class="linenos">221</span></a>    <span class="c1">#     print(interface, translation_language_changed_event, lang, end_lang)</span>
</span><span id="TranslationLanguageChooser-222"><a href="#TranslationLanguageChooser-222"><span class="linenos">222</span></a>    <span class="c1">#     interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))</span>
</span><span id="TranslationLanguageChooser-223"><a href="#TranslationLanguageChooser-223"><span class="linenos">223</span></a>    <span class="c1">#     print(&#39;raise_translation_language_changed_event - done&#39;)</span>
</span><span id="TranslationLanguageChooser-224"><a href="#TranslationLanguageChooser-224"><span class="linenos">224</span></a>    
</span><span id="TranslationLanguageChooser-225"><a href="#TranslationLanguageChooser-225"><span class="linenos">225</span></a>    <span class="k">def</span> <span class="nf">set_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslationLanguageChooser&#39;</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser-226"><a href="#TranslationLanguageChooser-226"><span class="linenos">226</span></a><span class="w">        </span><span class="sd">&#39;&#39;&#39;</span>
</span><span id="TranslationLanguageChooser-227"><a href="#TranslationLanguageChooser-227"><span class="linenos">227</span></a><span class="sd">        For usage with ArgsManager like</span>
</span><span id="TranslationLanguageChooser-228"><a href="#TranslationLanguageChooser-228"><span class="linenos">228</span></a><span class="sd">                am = ArgsManager(</span>
</span><span id="TranslationLanguageChooser-229"><a href="#TranslationLanguageChooser-229"><span class="linenos">229</span></a><span class="sd">                    EArgs(text_translator=TranslationLanguageChooser(</span>
</span><span id="TranslationLanguageChooser-230"><a href="#TranslationLanguageChooser-230"><span class="linenos">230</span></a><span class="sd">                        TextTranslator.from_json(TEXT_DICTIONARY), </span>
</span><span id="TranslationLanguageChooser-231"><a href="#TranslationLanguageChooser-231"><span class="linenos">231</span></a><span class="sd">                        TranslationLanguageMapper(TRANSLATION_LANGUAGE_MAP, &#39;en&#39;)).set_lang(&#39;ru&#39;))</span>
</span><span id="TranslationLanguageChooser-232"><a href="#TranslationLanguageChooser-232"><span class="linenos">232</span></a><span class="sd">                )</span>
</span><span id="TranslationLanguageChooser-233"><a href="#TranslationLanguageChooser-233"><span class="linenos">233</span></a>
</span><span id="TranslationLanguageChooser-234"><a href="#TranslationLanguageChooser-234"><span class="linenos">234</span></a><span class="sd">        &#39;&#39;&#39;</span>
</span><span id="TranslationLanguageChooser-235"><a href="#TranslationLanguageChooser-235"><span class="linenos">235</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang</span> <span class="o">=</span> <span class="n">language</span>
</span><span id="TranslationLanguageChooser-236"><a href="#TranslationLanguageChooser-236"><span class="linenos">236</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="TranslationLanguageChooser-237"><a href="#TranslationLanguageChooser-237"><span class="linenos">237</span></a>    
</span><span id="TranslationLanguageChooser-238"><a href="#TranslationLanguageChooser-238"><span class="linenos">238</span></a>    <span class="nd">@property</span>
</span><span id="TranslationLanguageChooser-239"><a href="#TranslationLanguageChooser-239"><span class="linenos">239</span></a>    <span class="k">def</span> <span class="nf">end_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser-240"><a href="#TranslationLanguageChooser-240"><span class="linenos">240</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span>
</span><span id="TranslationLanguageChooser-241"><a href="#TranslationLanguageChooser-241"><span class="linenos">241</span></a>    
</span><span id="TranslationLanguageChooser-242"><a href="#TranslationLanguageChooser-242"><span class="linenos">242</span></a>    <span class="nd">@end_lang</span><span class="o">.</span><span class="n">setter</span>
</span><span id="TranslationLanguageChooser-243"><a href="#TranslationLanguageChooser-243"><span class="linenos">243</span></a>    <span class="k">def</span> <span class="nf">end_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">):</span>
</span><span id="TranslationLanguageChooser-244"><a href="#TranslationLanguageChooser-244"><span class="linenos">244</span></a>        <span class="k">pass</span>
</span><span id="TranslationLanguageChooser-245"><a href="#TranslationLanguageChooser-245"><span class="linenos">245</span></a>    
</span><span id="TranslationLanguageChooser-246"><a href="#TranslationLanguageChooser-246"><span class="linenos">246</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser-247"><a href="#TranslationLanguageChooser-247"><span class="linenos">247</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">,</span> <span class="n">text</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="TranslationLanguageChooser.__init__" class="classattr">
                                        <input id="TranslationLanguageChooser.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TranslationLanguageChooser</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">text_translator</span><span class="p">:</span> <span class="n"><a href="#TextTranslator">TextTranslator</a></span>,</span><span class="param">	<span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n"><a href="#TranslationLanguageMapper">TranslationLanguageMapper</a></span>,</span><span class="param">	<span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerGreenlet</span><span class="p">,</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">CoroSchedulerAwaitable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="TranslationLanguageChooser.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageChooser.__init__-176"><a href="#TranslationLanguageChooser.__init__-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> 
</span><span id="TranslationLanguageChooser.__init__-177"><a href="#TranslationLanguageChooser.__init__-177"><span class="linenos">177</span></a>                 <span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span><span class="p">,</span>
</span><span id="TranslationLanguageChooser.__init__-178"><a href="#TranslationLanguageChooser.__init__-178"><span class="linenos">178</span></a>                 <span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CoroSchedulerType</span><span class="p">]</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
</span><span id="TranslationLanguageChooser.__init__-179"><a href="#TranslationLanguageChooser.__init__-179"><span class="linenos">179</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TranslationLanguageChooser.__init__-180"><a href="#TranslationLanguageChooser.__init__-180"><span class="linenos">180</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TranslationLanguageId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TranslationLanguageChooser.__init__-181"><a href="#TranslationLanguageChooser.__init__-181"><span class="linenos">181</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="TranslationLanguageChooser.__init__-182"><a href="#TranslationLanguageChooser.__init__-182"><span class="linenos">182</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_mapper</span><span class="p">:</span> <span class="n">TranslationLanguageMapper</span> <span class="o">=</span> <span class="n">translation_language_mapper</span>
</span><span id="TranslationLanguageChooser.__init__-183"><a href="#TranslationLanguageChooser.__init__-183"><span class="linenos">183</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">coro_scheduler</span> <span class="ow">or</span> <span class="n">CoroScheduler</span><span class="o">.</span><span class="n">current_loop</span><span class="p">()</span>
</span><span id="TranslationLanguageChooser.__init__-184"><a href="#TranslationLanguageChooser.__init__-184"><span class="linenos">184</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">uuid4</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslationLanguageChooser.text_translator" class="classattr">
                                <div class="attr variable">
            <span class="name">text_translator</span><span class="annotation">: <a href="#TextTranslator">TextTranslator</a></span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.text_translator"></a>
    
    

                            </div>
                            <div id="TranslationLanguageChooser.translation_language_mapper" class="classattr">
                                <div class="attr variable">
            <span class="name">translation_language_mapper</span><span class="annotation">: <a href="#TranslationLanguageMapper">TranslationLanguageMapper</a></span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.translation_language_mapper"></a>
    
    

                            </div>
                            <div id="TranslationLanguageChooser.coro_scheduler" class="classattr">
                                <div class="attr variable">
            <span class="name">coro_scheduler</span><span class="annotation">: Union[cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.CoroSchedulerGreenlet, cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler.CoroSchedulerAwaitable]</span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.coro_scheduler"></a>
    
    

                            </div>
                            <div id="TranslationLanguageChooser.translation_language_changed_event" class="classattr">
                                <div class="attr variable">
            <span class="name">translation_language_changed_event</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.translation_language_changed_event"></a>
    
    

                            </div>
                            <div id="TranslationLanguageChooser.lang" class="classattr">
                                        <input id="TranslationLanguageChooser.lang-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">lang</span><span class="annotation">: Hashable</span>

                <label class="view-source-button" for="TranslationLanguageChooser.lang-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.lang"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageChooser.lang-186"><a href="#TranslationLanguageChooser.lang-186"><span class="linenos">186</span></a>    <span class="nd">@property</span>
</span><span id="TranslationLanguageChooser.lang-187"><a href="#TranslationLanguageChooser.lang-187"><span class="linenos">187</span></a>    <span class="k">def</span> <span class="nf">lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser.lang-188"><a href="#TranslationLanguageChooser.lang-188"><span class="linenos">188</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_lang</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslationLanguageChooser.set_lang" class="classattr">
                                        <input id="TranslationLanguageChooser.set_lang-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_lang</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">language</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="n"><a href="#TranslationLanguageChooser">TranslationLanguageChooser</a></span>:</span></span>

                <label class="view-source-button" for="TranslationLanguageChooser.set_lang-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.set_lang"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageChooser.set_lang-225"><a href="#TranslationLanguageChooser.set_lang-225"><span class="linenos">225</span></a>    <span class="k">def</span> <span class="nf">set_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslationLanguageChooser&#39;</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser.set_lang-226"><a href="#TranslationLanguageChooser.set_lang-226"><span class="linenos">226</span></a><span class="w">        </span><span class="sd">&#39;&#39;&#39;</span>
</span><span id="TranslationLanguageChooser.set_lang-227"><a href="#TranslationLanguageChooser.set_lang-227"><span class="linenos">227</span></a><span class="sd">        For usage with ArgsManager like</span>
</span><span id="TranslationLanguageChooser.set_lang-228"><a href="#TranslationLanguageChooser.set_lang-228"><span class="linenos">228</span></a><span class="sd">                am = ArgsManager(</span>
</span><span id="TranslationLanguageChooser.set_lang-229"><a href="#TranslationLanguageChooser.set_lang-229"><span class="linenos">229</span></a><span class="sd">                    EArgs(text_translator=TranslationLanguageChooser(</span>
</span><span id="TranslationLanguageChooser.set_lang-230"><a href="#TranslationLanguageChooser.set_lang-230"><span class="linenos">230</span></a><span class="sd">                        TextTranslator.from_json(TEXT_DICTIONARY), </span>
</span><span id="TranslationLanguageChooser.set_lang-231"><a href="#TranslationLanguageChooser.set_lang-231"><span class="linenos">231</span></a><span class="sd">                        TranslationLanguageMapper(TRANSLATION_LANGUAGE_MAP, &#39;en&#39;)).set_lang(&#39;ru&#39;))</span>
</span><span id="TranslationLanguageChooser.set_lang-232"><a href="#TranslationLanguageChooser.set_lang-232"><span class="linenos">232</span></a><span class="sd">                )</span>
</span><span id="TranslationLanguageChooser.set_lang-233"><a href="#TranslationLanguageChooser.set_lang-233"><span class="linenos">233</span></a>
</span><span id="TranslationLanguageChooser.set_lang-234"><a href="#TranslationLanguageChooser.set_lang-234"><span class="linenos">234</span></a><span class="sd">        &#39;&#39;&#39;</span>
</span><span id="TranslationLanguageChooser.set_lang-235"><a href="#TranslationLanguageChooser.set_lang-235"><span class="linenos">235</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang</span> <span class="o">=</span> <span class="n">language</span>
</span><span id="TranslationLanguageChooser.set_lang-236"><a href="#TranslationLanguageChooser.set_lang-236"><span class="linenos">236</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


            <div class="docstring"><p>For usage with ArgsManager like
        am = ArgsManager(
            EArgs(text_translator=TranslationLanguageChooser(
                <a href="#TextTranslator.from_json">TextTranslator.from_json</a>(TEXT_DICTIONARY), 
                TranslationLanguageMapper(TRANSLATION_LANGUAGE_MAP, 'en')).set_lang('ru'))
        )</p>
</div>


                            </div>
                            <div id="TranslationLanguageChooser.end_lang" class="classattr">
                                        <input id="TranslationLanguageChooser.end_lang-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr variable">
            <span class="name">end_lang</span><span class="annotation">: Hashable</span>

                <label class="view-source-button" for="TranslationLanguageChooser.end_lang-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslationLanguageChooser.end_lang"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslationLanguageChooser.end_lang-238"><a href="#TranslationLanguageChooser.end_lang-238"><span class="linenos">238</span></a>    <span class="nd">@property</span>
</span><span id="TranslationLanguageChooser.end_lang-239"><a href="#TranslationLanguageChooser.end_lang-239"><span class="linenos">239</span></a>    <span class="k">def</span> <span class="nf">end_lang</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TranslationLanguageId</span><span class="p">:</span>
</span><span id="TranslationLanguageChooser.end_lang-240"><a href="#TranslationLanguageChooser.end_lang-240"><span class="linenos">240</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_end_lang</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TextTranslationReapplier">
                            <input id="TextTranslationReapplier-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TextTranslationReapplier</span><wbr>(<span class="base">cengal.code_flow_control.call_history_reapplier.versions.v_0.call_history_reapplier.CallHistoryReapplier</span>):

                <label class="view-source-button" for="TextTranslationReapplier-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslationReapplier"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslationReapplier-250"><a href="#TextTranslationReapplier-250"><span class="linenos">250</span></a><span class="k">class</span> <span class="nc">TextTranslationReapplier</span><span class="p">(</span><span class="n">CallHistoryReapplier</span><span class="p">):</span>
</span><span id="TextTranslationReapplier-251"><a href="#TextTranslationReapplier-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="o">=</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">):</span>
</span><span id="TextTranslationReapplier-252"><a href="#TextTranslationReapplier-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="TextTranslationReapplier-253"><a href="#TextTranslationReapplier-253"><span class="linenos">253</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-254"><a href="#TextTranslationReapplier-254"><span class="linenos">254</span></a>    
</span><span id="TextTranslationReapplier-255"><a href="#TextTranslationReapplier-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">_translate_needed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-256"><a href="#TextTranslationReapplier-256"><span class="linenos">256</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">):</span>
</span><span id="TextTranslationReapplier-257"><a href="#TextTranslationReapplier-257"><span class="linenos">257</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">(</span><span class="n">value</span><span class="o">.</span><span class="n">text</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-258"><a href="#TextTranslationReapplier-258"><span class="linenos">258</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-259"><a href="#TextTranslationReapplier-259"><span class="linenos">259</span></a>            <span class="k">return</span> <span class="n">value</span>
</span><span id="TextTranslationReapplier-260"><a href="#TextTranslationReapplier-260"><span class="linenos">260</span></a>    
</span><span id="TextTranslationReapplier-261"><a href="#TextTranslationReapplier-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">call_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">TranslationWorker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TextTranslationReapplier-262"><a href="#TextTranslationReapplier-262"><span class="linenos">262</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TextTranslationReapplier-263"><a href="#TextTranslationReapplier-263"><span class="linenos">263</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-264"><a href="#TextTranslationReapplier-264"><span class="linenos">264</span></a>            <span class="n">new_args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">))</span>
</span><span id="TextTranslationReapplier-265"><a href="#TextTranslationReapplier-265"><span class="linenos">265</span></a>        
</span><span id="TextTranslationReapplier-266"><a href="#TextTranslationReapplier-266"><span class="linenos">266</span></a>        <span class="n">new_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TextTranslationReapplier-267"><a href="#TextTranslationReapplier-267"><span class="linenos">267</span></a>        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TextTranslationReapplier-268"><a href="#TextTranslationReapplier-268"><span class="linenos">268</span></a>            <span class="n">new_kwargs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-269"><a href="#TextTranslationReapplier-269"><span class="linenos">269</span></a>        
</span><span id="TextTranslationReapplier-270"><a href="#TextTranslationReapplier-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">text_template</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-271"><a href="#TextTranslationReapplier-271"><span class="linenos">271</span></a>            <span class="k">if</span> <span class="n">new_kwargs</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-272"><a href="#TextTranslationReapplier-272"><span class="linenos">272</span></a>                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;There are tt items in kwargs, however text_template is None&#39;</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-273"><a href="#TextTranslationReapplier-273"><span class="linenos">273</span></a>
</span><span id="TextTranslationReapplier-274"><a href="#TextTranslationReapplier-274"><span class="linenos">274</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">new_args</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-275"><a href="#TextTranslationReapplier-275"><span class="linenos">275</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TextTranslationReapplier-276"><a href="#TextTranslationReapplier-276"><span class="linenos">276</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="n">text_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">new_args</span><span class="p">,</span> <span class="o">**</span><span class="n">new_kwargs</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-277"><a href="#TextTranslationReapplier-277"><span class="linenos">277</span></a>        
</span><span id="TextTranslationReapplier-278"><a href="#TextTranslationReapplier-278"><span class="linenos">278</span></a>        <span class="n">translation_worker</span><span class="p">(</span><span class="n">translated_text</span><span class="p">)</span>
</span><span id="TextTranslationReapplier-279"><a href="#TextTranslationReapplier-279"><span class="linenos">279</span></a>    
</span><span id="TextTranslationReapplier-280"><a href="#TextTranslationReapplier-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">args_to_key_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="TextTranslationReapplier-281"><a href="#TextTranslationReapplier-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="p">((</span><span class="n">entity_id</span><span class="p">,</span> <span class="nb">id</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">field</span><span class="p">),</span> <span class="p">(</span><span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">))</span>
</span><span id="TextTranslationReapplier-282"><a href="#TextTranslationReapplier-282"><span class="linenos">282</span></a>    
</span><span id="TextTranslationReapplier-283"><a href="#TextTranslationReapplier-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="nf">key_value_to_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="TextTranslationReapplier-284"><a href="#TextTranslationReapplier-284"><span class="linenos">284</span></a>        <span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span> <span class="o">=</span> <span class="n">key</span>
</span><span id="TextTranslationReapplier-285"><a href="#TextTranslationReapplier-285"><span class="linenos">285</span></a>        <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="TextTranslationReapplier-286"><a href="#TextTranslationReapplier-286"><span class="linenos">286</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">([</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">]</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>
</span><span id="TextTranslationReapplier-287"><a href="#TextTranslationReapplier-287"><span class="linenos">287</span></a>        <span class="k">return</span> <span class="n">new_args</span><span class="p">,</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            <div id="TextTranslationReapplier.__init__" class="classattr">
                                        <input id="TextTranslationReapplier.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TextTranslationReapplier</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">text_translator</span><span class="p">:</span> <span class="n"><a href="#TranslationLanguageChooser">TranslationLanguageChooser</a></span>,</span><span class="param">	<span class="n">priority</span><span class="p">:</span> <span class="n"><a href="#CoroPriority">CoroPriority</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#CoroPriority.low">CoroPriority.low</a></span><span class="p">:</span> <span class="mi">2</span><span class="o">&gt;</span></span>)</span>

                <label class="view-source-button" for="TextTranslationReapplier.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslationReapplier.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslationReapplier.__init__-251"><a href="#TextTranslationReapplier.__init__-251"><span class="linenos">251</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">,</span> <span class="n">priority</span><span class="p">:</span> <span class="n">CoroPriority</span><span class="o">=</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">low</span><span class="p">):</span>
</span><span id="TextTranslationReapplier.__init__-252"><a href="#TextTranslationReapplier.__init__-252"><span class="linenos">252</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span> <span class="o">=</span> <span class="n">text_translator</span>
</span><span id="TextTranslationReapplier.__init__-253"><a href="#TextTranslationReapplier.__init__-253"><span class="linenos">253</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">priority</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TextTranslationReapplier.text_translator" class="classattr">
                                <div class="attr variable">
            <span class="name">text_translator</span>

        
    </div>
    <a class="headerlink" href="#TextTranslationReapplier.text_translator"></a>
    
    

                            </div>
                            <div id="TextTranslationReapplier.call_impl" class="classattr">
                                        <input id="TextTranslationReapplier.call_impl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">call_impl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">field</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">translation_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">[[</span><span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">text_template</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TextTranslationReapplier.call_impl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslationReapplier.call_impl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslationReapplier.call_impl-261"><a href="#TextTranslationReapplier.call_impl-261"><span class="linenos">261</span></a>    <span class="k">def</span> <span class="nf">call_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">TranslationWorker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="TextTranslationReapplier.call_impl-262"><a href="#TextTranslationReapplier.call_impl-262"><span class="linenos">262</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TextTranslationReapplier.call_impl-263"><a href="#TextTranslationReapplier.call_impl-263"><span class="linenos">263</span></a>        <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="n">args</span><span class="p">:</span>
</span><span id="TextTranslationReapplier.call_impl-264"><a href="#TextTranslationReapplier.call_impl-264"><span class="linenos">264</span></a>            <span class="n">new_args</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">))</span>
</span><span id="TextTranslationReapplier.call_impl-265"><a href="#TextTranslationReapplier.call_impl-265"><span class="linenos">265</span></a>        
</span><span id="TextTranslationReapplier.call_impl-266"><a href="#TextTranslationReapplier.call_impl-266"><span class="linenos">266</span></a>        <span class="n">new_kwargs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TextTranslationReapplier.call_impl-267"><a href="#TextTranslationReapplier.call_impl-267"><span class="linenos">267</span></a>        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">kwargs</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TextTranslationReapplier.call_impl-268"><a href="#TextTranslationReapplier.call_impl-268"><span class="linenos">268</span></a>            <span class="n">new_kwargs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_translate_needed</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">)</span>
</span><span id="TextTranslationReapplier.call_impl-269"><a href="#TextTranslationReapplier.call_impl-269"><span class="linenos">269</span></a>        
</span><span id="TextTranslationReapplier.call_impl-270"><a href="#TextTranslationReapplier.call_impl-270"><span class="linenos">270</span></a>        <span class="k">if</span> <span class="n">text_template</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TextTranslationReapplier.call_impl-271"><a href="#TextTranslationReapplier.call_impl-271"><span class="linenos">271</span></a>            <span class="k">if</span> <span class="n">new_kwargs</span><span class="p">:</span>
</span><span id="TextTranslationReapplier.call_impl-272"><a href="#TextTranslationReapplier.call_impl-272"><span class="linenos">272</span></a>                <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">&#39;There are tt items in kwargs, however text_template is None&#39;</span><span class="p">)</span>
</span><span id="TextTranslationReapplier.call_impl-273"><a href="#TextTranslationReapplier.call_impl-273"><span class="linenos">273</span></a>
</span><span id="TextTranslationReapplier.call_impl-274"><a href="#TextTranslationReapplier.call_impl-274"><span class="linenos">274</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">new_args</span><span class="p">)</span>
</span><span id="TextTranslationReapplier.call_impl-275"><a href="#TextTranslationReapplier.call_impl-275"><span class="linenos">275</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TextTranslationReapplier.call_impl-276"><a href="#TextTranslationReapplier.call_impl-276"><span class="linenos">276</span></a>            <span class="n">translated_text</span> <span class="o">=</span> <span class="n">text_template</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="o">*</span><span class="n">new_args</span><span class="p">,</span> <span class="o">**</span><span class="n">new_kwargs</span><span class="p">)</span>
</span><span id="TextTranslationReapplier.call_impl-277"><a href="#TextTranslationReapplier.call_impl-277"><span class="linenos">277</span></a>        
</span><span id="TextTranslationReapplier.call_impl-278"><a href="#TextTranslationReapplier.call_impl-278"><span class="linenos">278</span></a>        <span class="n">translation_worker</span><span class="p">(</span><span class="n">translated_text</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TextTranslationReapplier.args_to_key_value" class="classattr">
                                        <input id="TextTranslationReapplier.args_to_key_value-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">args_to_key_value</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="n">obj</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span>,</span><span class="param">	<span class="n">field</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>,</span><span class="param">	<span class="n">translation_worker</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span>,</span><span class="param">	<span class="n">text_template</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TextTranslationReapplier.args_to_key_value-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslationReapplier.args_to_key_value"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslationReapplier.args_to_key_value-280"><a href="#TextTranslationReapplier.args_to_key_value-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">args_to_key_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">],</span> <span class="n">obj</span><span class="p">:</span> <span class="n">Any</span><span class="p">,</span> <span class="n">field</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">text_template</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
</span><span id="TextTranslationReapplier.args_to_key_value-281"><a href="#TextTranslationReapplier.args_to_key_value-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="p">((</span><span class="n">entity_id</span><span class="p">,</span> <span class="nb">id</span><span class="p">(</span><span class="n">obj</span><span class="p">),</span> <span class="n">field</span><span class="p">),</span> <span class="p">(</span><span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TextTranslationReapplier.key_value_to_args" class="classattr">
                                        <input id="TextTranslationReapplier.key_value_to_args-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">key_value_to_args</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">key</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>, </span><span class="param"><span class="n">value</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Any</span></span><span class="return-annotation">) -> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TextTranslationReapplier.key_value_to_args-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TextTranslationReapplier.key_value_to_args"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TextTranslationReapplier.key_value_to_args-283"><a href="#TextTranslationReapplier.key_value_to_args-283"><span class="linenos">283</span></a>    <span class="k">def</span> <span class="nf">key_value_to_args</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Tuple</span><span class="p">,</span> <span class="n">Dict</span><span class="p">]:</span>
</span><span id="TextTranslationReapplier.key_value_to_args-284"><a href="#TextTranslationReapplier.key_value_to_args-284"><span class="linenos">284</span></a>        <span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span> <span class="o">=</span> <span class="n">key</span>
</span><span id="TextTranslationReapplier.key_value_to_args-285"><a href="#TextTranslationReapplier.key_value_to_args-285"><span class="linenos">285</span></a>        <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">kwargs</span> <span class="o">=</span> <span class="n">value</span>
</span><span id="TextTranslationReapplier.key_value_to_args-286"><a href="#TextTranslationReapplier.key_value_to_args-286"><span class="linenos">286</span></a>        <span class="n">new_args</span> <span class="o">=</span> <span class="nb">tuple</span><span class="p">([</span><span class="n">entity_id</span><span class="p">,</span> <span class="n">obj</span><span class="p">,</span> <span class="n">field</span><span class="p">,</span> <span class="n">translation_worker</span><span class="p">,</span> <span class="n">text_template</span><span class="p">]</span> <span class="o">+</span> <span class="nb">list</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>
</span><span id="TextTranslationReapplier.key_value_to_args-287"><a href="#TextTranslationReapplier.key_value_to_args-287"><span class="linenos">287</span></a>        <span class="k">return</span> <span class="n">new_args</span><span class="p">,</span> <span class="n">kwargs</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.code_flow_control.call_history_reapplier.versions.v_0.call_history_reapplier.CallHistoryReapplier</dt>
                                <dd id="TextTranslationReapplier.history" class="variable">history</dd>
                <dd id="TextTranslationReapplier.priority" class="variable">priority</dd>
                <dd id="TextTranslationReapplier.reapply" class="function">reapply</dd>
                <dd id="TextTranslationReapplier.destroy" class="function">destroy</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CoroPriority">
                            <input id="CoroPriority-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroPriority</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="CoroPriority-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroPriority"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroPriority-59"><a href="#CoroPriority-59"><span class="linenos">59</span></a><span class="k">class</span> <span class="nc">CoroPriority</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="CoroPriority-60"><a href="#CoroPriority-60"><span class="linenos">60</span></a>    <span class="n">high</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="CoroPriority-61"><a href="#CoroPriority-61"><span class="linenos">61</span></a>    <span class="n">normal</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="CoroPriority-62"><a href="#CoroPriority-62"><span class="linenos">62</span></a>    <span class="n">low</span> <span class="o">=</span> <span class="mi">2</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="CoroPriority.high" class="classattr">
                                <div class="attr variable">
            <span class="name">high</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.high">CoroPriority.high</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.high"></a>
    
    

                            </div>
                            <div id="CoroPriority.normal" class="classattr">
                                <div class="attr variable">
            <span class="name">normal</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.normal">CoroPriority.normal</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.normal"></a>
    
    

                            </div>
                            <div id="CoroPriority.low" class="classattr">
                                <div class="attr variable">
            <span class="name">low</span>        =
<span class="default_value">&lt;<a href="#CoroPriority.low">CoroPriority.low</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#CoroPriority.low"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="CoroPriority.name" class="variable">name</dd>
                <dd id="CoroPriority.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TranslationWorker">
                    <div class="attr variable">
            <span class="name">TranslationWorker</span>        =
<span class="default_value">typing.Callable[[str], NoneType]</span>

        
    </div>
    <a class="headerlink" href="#TranslationWorker"></a>
    
    

                </section>
                <section id="TranslatableText">
                            <input id="TranslatableText-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TranslatableText</span>:

                <label class="view-source-button" for="TranslatableText-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableText"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableText-290"><a href="#TranslatableText-290"><span class="linenos">290</span></a><span class="k">class</span> <span class="nc">TranslatableText</span><span class="p">:</span>
</span><span id="TranslatableText-291"><a href="#TranslatableText-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">],</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableText-292"><a href="#TranslatableText-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">text</span>
</span><span id="TranslatableText-293"><a href="#TranslatableText-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="TranslatableText-294"><a href="#TranslatableText-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">formatter</span>
</span><span id="TranslatableText-295"><a href="#TranslatableText-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_awaitable</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TranslatableText-296"><a href="#TranslatableText-296"><span class="linenos">296</span></a>    
</span><span id="TranslatableText-297"><a href="#TranslatableText-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TranslatableText-298"><a href="#TranslatableText-298"><span class="linenos">298</span></a>        <span class="k">if</span> <span class="n">is_callable</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">):</span>
</span><span id="TranslatableText-299"><a href="#TranslatableText-299"><span class="linenos">299</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">()</span>
</span><span id="TranslatableText-300"><a href="#TranslatableText-300"><span class="linenos">300</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TranslatableText-301"><a href="#TranslatableText-301"><span class="linenos">301</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">text</span>
</span><span id="TranslatableText-302"><a href="#TranslatableText-302"><span class="linenos">302</span></a>    
</span><span id="TranslatableText-303"><a href="#TranslatableText-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslatableText-304"><a href="#TranslatableText-304"><span class="linenos">304</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableText-305"><a href="#TranslatableText-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">text</span>
</span><span id="TranslatableText-306"><a href="#TranslatableText-306"><span class="linenos">306</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TranslatableText-307"><a href="#TranslatableText-307"><span class="linenos">307</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</span><span id="TranslatableText-308"><a href="#TranslatableText-308"><span class="linenos">308</span></a>    
</span><span id="TranslatableText-309"><a href="#TranslatableText-309"><span class="linenos">309</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslatableText-310"><a href="#TranslatableText-310"><span class="linenos">310</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="TranslatableText.__init__" class="classattr">
                                        <input id="TranslatableText.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TranslatableText</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">text</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">]</span>,</span><span class="param">	<span class="n">entity_id</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">formatter</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n">typing</span><span class="o">.</span><span class="n">Callable</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="TranslatableText.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableText.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableText.__init__-291"><a href="#TranslatableText.__init__-291"><span class="linenos">291</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Callable</span><span class="p">],</span> <span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableText.__init__-292"><a href="#TranslatableText.__init__-292"><span class="linenos">292</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">text</span>
</span><span id="TranslatableText.__init__-293"><a href="#TranslatableText.__init__-293"><span class="linenos">293</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">entity_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">TextEntityId</span><span class="p">]</span> <span class="o">=</span> <span class="n">entity_id</span>
</span><span id="TranslatableText.__init__-294"><a href="#TranslatableText.__init__-294"><span class="linenos">294</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="n">formatter</span>
</span><span id="TranslatableText.__init__-295"><a href="#TranslatableText.__init__-295"><span class="linenos">295</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">is_awaitable</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableText.text" class="classattr">
                                <div class="attr variable">
            <span class="name">text</span><span class="annotation">: str</span>

        
    </div>
    <a class="headerlink" href="#TranslatableText.text"></a>
    
    

                            </div>
                            <div id="TranslatableText.entity_id" class="classattr">
                                <div class="attr variable">
            <span class="name">entity_id</span><span class="annotation">: Union[Hashable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#TranslatableText.entity_id"></a>
    
    

                            </div>
                            <div id="TranslatableText.formatter" class="classattr">
                                <div class="attr variable">
            <span class="name">formatter</span><span class="annotation">: Union[Callable, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#TranslatableText.formatter"></a>
    
    

                            </div>
                            <div id="TranslatableText.is_awaitable" class="classattr">
                                <div class="attr variable">
            <span class="name">is_awaitable</span><span class="annotation">: bool</span>

        
    </div>
    <a class="headerlink" href="#TranslatableText.is_awaitable"></a>
    
    

                            </div>
                            <div id="TranslatableText.format" class="classattr">
                                        <input id="TranslatableText.format-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">format</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">text</span><span class="p">:</span> <span class="nb">str</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="TranslatableText.format-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableText.format"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableText.format-303"><a href="#TranslatableText.format-303"><span class="linenos">303</span></a>    <span class="k">def</span> <span class="nf">format</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslatableText.format-304"><a href="#TranslatableText.format-304"><span class="linenos">304</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableText.format-305"><a href="#TranslatableText.format-305"><span class="linenos">305</span></a>            <span class="k">return</span> <span class="n">text</span>
</span><span id="TranslatableText.format-306"><a href="#TranslatableText.format-306"><span class="linenos">306</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TranslatableText.format-307"><a href="#TranslatableText.format-307"><span class="linenos">307</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">formatter</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="tt">
                    <div class="attr variable">
            <span class="name">tt</span>        =
<span class="default_value">&lt;class &#39;<a href="#TranslatableText">TranslatableText</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#tt"></a>
    
    

                </section>
                <section id="TranslateMe">
                            <input id="TranslateMe-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TranslateMe</span>:

                <label class="view-source-button" for="TranslateMe-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslateMe"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslateMe-316"><a href="#TranslateMe-316"><span class="linenos">316</span></a><span class="k">class</span> <span class="nc">TranslateMe</span><span class="p">:</span>
</span><span id="TranslateMe-317"><a href="#TranslateMe-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslateMe-318"><a href="#TranslateMe-318"><span class="linenos">318</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]]</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="TranslateMe-319"><a href="#TranslateMe-319"><span class="linenos">319</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_contains_translatable_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</span><span id="TranslateMe-320"><a href="#TranslateMe-320"><span class="linenos">320</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TranslateMe-321"><a href="#TranslateMe-321"><span class="linenos">321</span></a>    
</span><span id="TranslateMe-322"><a href="#TranslateMe-322"><span class="linenos">322</span></a>    <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TranslateMe-323"><a href="#TranslateMe-323"><span class="linenos">323</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_contains_translatable_text</span>
</span><span id="TranslateMe-324"><a href="#TranslateMe-324"><span class="linenos">324</span></a>    
</span><span id="TranslateMe-325"><a href="#TranslateMe-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="nf">to_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslateMe-326"><a href="#TranslateMe-326"><span class="linenos">326</span></a>        <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">arg</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text_translator</span><span class="p">(</span><span class="n">language</span><span class="p">,</span> <span class="n">arg</span><span class="p">(),</span> <span class="n">arg</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">else</span> <span class="n">arg</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">])</span>
</span><span id="TranslateMe-327"><a href="#TranslateMe-327"><span class="linenos">327</span></a>
</span><span id="TranslateMe-328"><a href="#TranslateMe-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">tte</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslateMe&#39;</span><span class="p">:</span>
</span><span id="TranslateMe-329"><a href="#TranslateMe-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span> <span class="o">=</span> <span class="n">tte</span>
</span><span id="TranslateMe-330"><a href="#TranslateMe-330"><span class="linenos">330</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span><span id="TranslateMe-331"><a href="#TranslateMe-331"><span class="linenos">331</span></a>    
</span><span id="TranslateMe-332"><a href="#TranslateMe-332"><span class="linenos">332</span></a>    <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslateMe-333"><a href="#TranslateMe-333"><span class="linenos">333</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span><span class="o">.</span><span class="n">translate_me</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            <div id="TranslateMe.__init__" class="classattr">
                                        <input id="TranslateMe.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TranslateMe</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span></span>)</span>

                <label class="view-source-button" for="TranslateMe.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslateMe.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslateMe.__init__-317"><a href="#TranslateMe.__init__-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslateMe.__init__-318"><a href="#TranslateMe.__init__-318"><span class="linenos">318</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]]</span> <span class="o">=</span> <span class="n">args</span>
</span><span id="TranslateMe.__init__-319"><a href="#TranslateMe.__init__-319"><span class="linenos">319</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_contains_translatable_text</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="nb">any</span><span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">)</span>
</span><span id="TranslateMe.__init__-320"><a href="#TranslateMe.__init__-320"><span class="linenos">320</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslateMe.args" class="classattr">
                                <div class="attr variable">
            <span class="name">args</span><span class="annotation">: Tuple[Union[str, <a href="#TranslatableText">TranslatableText</a>]]</span>

        
    </div>
    <a class="headerlink" href="#TranslateMe.args"></a>
    
    

                            </div>
                            <div id="TranslateMe.to_str" class="classattr">
                                        <input id="TranslateMe.to_str-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">to_str</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">text_translator</span><span class="p">:</span> <span class="n"><a href="#TextTranslator">TextTranslator</a></span>,</span><span class="param">	<span class="n">language</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="TranslateMe.to_str-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslateMe.to_str"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslateMe.to_str-325"><a href="#TranslateMe.to_str-325"><span class="linenos">325</span></a>    <span class="k">def</span> <span class="nf">to_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span><span class="p">,</span> <span class="n">language</span><span class="p">:</span> <span class="n">TranslationLanguageId</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslateMe.to_str-326"><a href="#TranslateMe.to_str-326"><span class="linenos">326</span></a>        <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="n">arg</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">text_translator</span><span class="p">(</span><span class="n">language</span><span class="p">,</span> <span class="n">arg</span><span class="p">(),</span> <span class="n">arg</span><span class="o">.</span><span class="n">entity_id</span><span class="p">))</span> <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">arg</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">)</span> <span class="k">else</span> <span class="n">arg</span> <span class="k">for</span> <span class="n">arg</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">])</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslateMe.tte" class="classattr">
                                        <input id="TranslateMe.tte-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">tte</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">tte</span><span class="p">:</span> <span class="n"><a href="#TranslatableTextElement">TranslatableTextElement</a></span></span><span class="return-annotation">) -> <span class="n"><a href="#TranslateMe">TranslateMe</a></span>:</span></span>

                <label class="view-source-button" for="TranslateMe.tte-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslateMe.tte"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslateMe.tte-328"><a href="#TranslateMe.tte-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">tte</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tte</span><span class="p">:</span> <span class="s1">&#39;TranslatableTextElement&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="s1">&#39;TranslateMe&#39;</span><span class="p">:</span>
</span><span id="TranslateMe.tte-329"><a href="#TranslateMe.tte-329"><span class="linenos">329</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_tte</span> <span class="o">=</span> <span class="n">tte</span>
</span><span id="TranslateMe.tte-330"><a href="#TranslateMe.tte-330"><span class="linenos">330</span></a>        <span class="k">return</span> <span class="bp">self</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TMe">
                    <div class="attr variable">
            <span class="name">TMe</span>        =
<span class="default_value">&lt;class &#39;<a href="#TranslateMe">TranslateMe</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#TMe"></a>
    
    

                </section>
                <section id="tme">
                    <div class="attr variable">
            <span class="name">tme</span>        =
<span class="default_value">&lt;class &#39;<a href="#TranslateMe">TranslateMe</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#tme"></a>
    
    

                </section>
                <section id="TranslatableTextElement">
                            <input id="TranslatableTextElement-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TranslatableTextElement</span><wbr>(<span class="base">typing.Generic[~T]</span>):

                <label class="view-source-button" for="TranslatableTextElement-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement-343"><a href="#TranslatableTextElement-343"><span class="linenos">343</span></a><span class="k">class</span> <span class="nc">TranslatableTextElement</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">T</span><span class="p">]):</span>
</span><span id="TranslatableTextElement-344"><a href="#TranslatableTextElement-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableTextElement-345"><a href="#TranslatableTextElement-345"><span class="linenos">345</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span>
</span><span id="TranslatableTextElement-346"><a href="#TranslatableTextElement-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">text_translator</span>
</span><span id="TranslatableTextElement-347"><a href="#TranslatableTextElement-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TranslatableTextElement-348"><a href="#TranslatableTextElement-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TranslatableTextElement-349"><a href="#TranslatableTextElement-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TranslatableTextElement-350"><a href="#TranslatableTextElement-350"><span class="linenos">350</span></a>    
</span><span id="TranslatableTextElement-351"><a href="#TranslatableTextElement-351"><span class="linenos">351</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_element</span><span class="p">:</span> <span class="n">T</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="TranslatableTextElement-352"><a href="#TranslatableTextElement-352"><span class="linenos">352</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="TranslatableTextElement-353"><a href="#TranslatableTextElement-353"><span class="linenos">353</span></a>
</span><span id="TranslatableTextElement-354"><a href="#TranslatableTextElement-354"><span class="linenos">354</span></a>    <span class="k">def</span> <span class="nf">set_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_element</span><span class="p">:</span> <span class="n">T</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">TranslateMe</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">T</span><span class="p">:</span>
</span><span id="TranslatableTextElement-355"><a href="#TranslatableTextElement-355"><span class="linenos">355</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span><span id="TranslatableTextElement-356"><a href="#TranslatableTextElement-356"><span class="linenos">356</span></a>    
</span><span id="TranslatableTextElement-357"><a href="#TranslatableTextElement-357"><span class="linenos">357</span></a>    <span class="k">def</span> <span class="nf">translate_me</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">translate_me</span><span class="p">:</span> <span class="n">TranslateMe</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslatableTextElement-358"><a href="#TranslatableTextElement-358"><span class="linenos">358</span></a>        <span class="k">return</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">end_lang</span><span class="p">)</span>
</span><span id="TranslatableTextElement-359"><a href="#TranslatableTextElement-359"><span class="linenos">359</span></a>
</span><span id="TranslatableTextElement-360"><a href="#TranslatableTextElement-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="nf">start_translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="TranslatableTextElement-361"><a href="#TranslatableTextElement-361"><span class="linenos">361</span></a>        <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_reapplier</span><span class="p">)</span>
</span><span id="TranslatableTextElement-362"><a href="#TranslatableTextElement-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span><span id="TranslatableTextElement-363"><a href="#TranslatableTextElement-363"><span class="linenos">363</span></a>    
</span><span id="TranslatableTextElement-364"><a href="#TranslatableTextElement-364"><span class="linenos">364</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="TranslatableTextElement-365"><a href="#TranslatableTextElement-365"><span class="linenos">365</span></a>        <span class="n">waiting_set</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="p">{</span><span class="n">i</span><span class="o">.</span><span class="n">coro_id</span><span class="p">}</span>
</span><span id="TranslatableTextElement-366"><a href="#TranslatableTextElement-366"><span class="linenos">366</span></a>        <span class="c1"># await i(WaitCoroRequest().list(waiting_set))  # TODO: Not Implemented currently</span>
</span><span id="TranslatableTextElement-367"><a href="#TranslatableTextElement-367"><span class="linenos">367</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">waiting_set</span><span class="p">:</span>
</span><span id="TranslatableTextElement-368"><a href="#TranslatableTextElement-368"><span class="linenos">368</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TranslatableTextElement-369"><a href="#TranslatableTextElement-369"><span class="linenos">369</span></a>                <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">WaitCoroRequest</span><span class="p">()</span><span class="o">.</span><span class="n">single</span><span class="p">(</span><span class="n">coro_id</span><span class="p">))</span>
</span><span id="TranslatableTextElement-370"><a href="#TranslatableTextElement-370"><span class="linenos">370</span></a>            <span class="k">except</span> <span class="n">CoroutineNotFoundError</span><span class="p">:</span>
</span><span id="TranslatableTextElement-371"><a href="#TranslatableTextElement-371"><span class="linenos">371</span></a>                <span class="k">pass</span>
</span><span id="TranslatableTextElement-372"><a href="#TranslatableTextElement-372"><span class="linenos">372</span></a>        
</span><span id="TranslatableTextElement-373"><a href="#TranslatableTextElement-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="n">waiting_set</span>
</span><span id="TranslatableTextElement-374"><a href="#TranslatableTextElement-374"><span class="linenos">374</span></a>        
</span><span id="TranslatableTextElement-375"><a href="#TranslatableTextElement-375"><span class="linenos">375</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="TranslatableTextElement-376"><a href="#TranslatableTextElement-376"><span class="linenos">376</span></a>            <span class="k">return</span>
</span><span id="TranslatableTextElement-377"><a href="#TranslatableTextElement-377"><span class="linenos">377</span></a>        
</span><span id="TranslatableTextElement-378"><a href="#TranslatableTextElement-378"><span class="linenos">378</span></a>        <span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span>
</span><span id="TranslatableTextElement-379"><a href="#TranslatableTextElement-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">)()</span>
</span><span id="TranslatableTextElement-380"><a href="#TranslatableTextElement-380"><span class="linenos">380</span></a>        <span class="k">for</span> <span class="n">lang</span><span class="p">,</span> <span class="n">end_lang</span> <span class="ow">in</span> <span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="TranslatableTextElement-381"><a href="#TranslatableTextElement-381"><span class="linenos">381</span></a>            <span class="k">for</span> <span class="n">text_element</span><span class="p">,</span> <span class="n">translate_me</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TranslatableTextElement-382"><a href="#TranslatableTextElement-382"><span class="linenos">382</span></a>                <span class="n">text_element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="n">end_lang</span><span class="p">)</span>
</span><span id="TranslatableTextElement-383"><a href="#TranslatableTextElement-383"><span class="linenos">383</span></a>
</span><span id="TranslatableTextElement-384"><a href="#TranslatableTextElement-384"><span class="linenos">384</span></a>    <span class="k">def</span> <span class="nf">register_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement-385"><a href="#TranslatableTextElement-385"><span class="linenos">385</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement-386"><a href="#TranslatableTextElement-386"><span class="linenos">386</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="TranslatableTextElement-387"><a href="#TranslatableTextElement-387"><span class="linenos">387</span></a>
</span><span id="TranslatableTextElement-388"><a href="#TranslatableTextElement-388"><span class="linenos">388</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement-389"><a href="#TranslatableTextElement-389"><span class="linenos">389</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement-390"><a href="#TranslatableTextElement-390"><span class="linenos">390</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="TranslatableTextElement-391"><a href="#TranslatableTextElement-391"><span class="linenos">391</span></a>
</span><span id="TranslatableTextElement-392"><a href="#TranslatableTextElement-392"><span class="linenos">392</span></a>    <span class="k">def</span> <span class="nf">remove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement-393"><a href="#TranslatableTextElement-393"><span class="linenos">393</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement-394"><a href="#TranslatableTextElement-394"><span class="linenos">394</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="TranslatableTextElement-395"><a href="#TranslatableTextElement-395"><span class="linenos">395</span></a>
</span><span id="TranslatableTextElement-396"><a href="#TranslatableTextElement-396"><span class="linenos">396</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aremove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement-397"><a href="#TranslatableTextElement-397"><span class="linenos">397</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement-398"><a href="#TranslatableTextElement-398"><span class="linenos">398</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span><span id="TranslatableTextElement-399"><a href="#TranslatableTextElement-399"><span class="linenos">399</span></a>    
</span><span id="TranslatableTextElement-400"><a href="#TranslatableTextElement-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">on_lang_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]):</span>
</span><span id="TranslatableTextElement-401"><a href="#TranslatableTextElement-401"><span class="linenos">401</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TranslatableTextElement-402"><a href="#TranslatableTextElement-402"><span class="linenos">402</span></a>        <span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">start_translation_reapplier</span><span class="p">)</span>
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


                            <div id="TranslatableTextElement.__init__" class="classattr">
                                        <input id="TranslatableTextElement.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TranslatableTextElement</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n"><a href="#TranslationLanguageChooser">TranslationLanguageChooser</a></span></span>)</span>

                <label class="view-source-button" for="TranslatableTextElement.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.__init__-344"><a href="#TranslatableTextElement.__init__-344"><span class="linenos">344</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TranslatableTextElement.__init__-345"><a href="#TranslatableTextElement.__init__-345"><span class="linenos">345</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="p">:</span> <span class="n">TranslationLanguageChooser</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span>
</span><span id="TranslatableTextElement.__init__-346"><a href="#TranslatableTextElement.__init__-346"><span class="linenos">346</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">:</span> <span class="n">TextTranslator</span> <span class="o">=</span> <span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">text_translator</span>
</span><span id="TranslatableTextElement.__init__-347"><a href="#TranslatableTextElement.__init__-347"><span class="linenos">347</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">T</span><span class="p">,</span> <span class="n">TranslatableText</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="TranslatableTextElement.__init__-348"><a href="#TranslatableTextElement.__init__-348"><span class="linenos">348</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="TranslatableTextElement.__init__-349"><a href="#TranslatableTextElement.__init__-349"><span class="linenos">349</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.text_translation_language_chooser" class="classattr">
                                <div class="attr variable">
            <span class="name">text_translation_language_chooser</span><span class="annotation">: <a href="#TranslationLanguageChooser">TranslationLanguageChooser</a></span>

        
    </div>
    <a class="headerlink" href="#TranslatableTextElement.text_translation_language_chooser"></a>
    
    

                            </div>
                            <div id="TranslatableTextElement.text_translator" class="classattr">
                                <div class="attr variable">
            <span class="name">text_translator</span><span class="annotation">: <a href="#TextTranslator">TextTranslator</a></span>

        
    </div>
    <a class="headerlink" href="#TranslatableTextElement.text_translator"></a>
    
    

                            </div>
                            <div id="TranslatableTextElement.elements_and_their_translatable_text" class="classattr">
                                <div class="attr variable">
            <span class="name">elements_and_their_translatable_text</span><span class="annotation">: Dict[~T, <a href="#TranslatableText">TranslatableText</a>]</span>

        
    </div>
    <a class="headerlink" href="#TranslatableTextElement.elements_and_their_translatable_text"></a>
    
    

                            </div>
                            <div id="TranslatableTextElement.current_translation_reapplier_coros_ids" class="classattr">
                                <div class="attr variable">
            <span class="name">current_translation_reapplier_coros_ids</span><span class="annotation">: Set[int]</span>

        
    </div>
    <a class="headerlink" href="#TranslatableTextElement.current_translation_reapplier_coros_ids"></a>
    
    

                            </div>
                            <div id="TranslatableTextElement.lang_changing_queue" class="classattr">
                                <div class="attr variable">
            <span class="name">lang_changing_queue</span><span class="annotation">: List[Tuple[str, str]]</span>

        
    </div>
    <a class="headerlink" href="#TranslatableTextElement.lang_changing_queue"></a>
    
    

                            </div>
                            <div id="TranslatableTextElement.set_text" class="classattr">
                                        <input id="TranslatableTextElement.set_text-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">set_text</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">text_element</span><span class="p">:</span> <span class="o">~</span><span class="n">T</span>,</span><span class="param">	<span class="n">text</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Union</span><span class="p">[</span><span class="n"><a href="#TranslateMe">TranslateMe</a></span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="o">~</span><span class="n">T</span>:</span></span>

                <label class="view-source-button" for="TranslatableTextElement.set_text-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.set_text"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.set_text-354"><a href="#TranslatableTextElement.set_text-354"><span class="linenos">354</span></a>    <span class="k">def</span> <span class="nf">set_text</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text_element</span><span class="p">:</span> <span class="n">T</span><span class="p">,</span> <span class="n">text</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">TranslateMe</span><span class="p">,</span> <span class="nb">str</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="n">T</span><span class="p">:</span>
</span><span id="TranslatableTextElement.set_text-355"><a href="#TranslatableTextElement.set_text-355"><span class="linenos">355</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.translate_me" class="classattr">
                                        <input id="TranslatableTextElement.translate_me-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">translate_me</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">translate_me</span><span class="p">:</span> <span class="n"><a href="#TranslateMe">TranslateMe</a></span></span><span class="return-annotation">) -> <span class="nb">str</span>:</span></span>

                <label class="view-source-button" for="TranslatableTextElement.translate_me-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.translate_me"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.translate_me-357"><a href="#TranslatableTextElement.translate_me-357"><span class="linenos">357</span></a>    <span class="k">def</span> <span class="nf">translate_me</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">translate_me</span><span class="p">:</span> <span class="n">TranslateMe</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translate_me-358"><a href="#TranslatableTextElement.translate_me-358"><span class="linenos">358</span></a>        <span class="k">return</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">end_lang</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.start_translation_reapplier" class="classattr">
                                        <input id="TranslatableTextElement.start_translation_reapplier-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_translation_reapplier</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.start_translation_reapplier-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.start_translation_reapplier"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.start_translation_reapplier-360"><a href="#TranslatableTextElement.start_translation_reapplier-360"><span class="linenos">360</span></a>    <span class="k">def</span> <span class="nf">start_translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="TranslatableTextElement.start_translation_reapplier-361"><a href="#TranslatableTextElement.start_translation_reapplier-361"><span class="linenos">361</span></a>        <span class="n">coro_id</span><span class="p">:</span> <span class="n">CoroID</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">translation_reapplier</span><span class="p">)</span>
</span><span id="TranslatableTextElement.start_translation_reapplier-362"><a href="#TranslatableTextElement.start_translation_reapplier-362"><span class="linenos">362</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">coro_id</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.translation_reapplier" class="classattr">
                                        <input id="TranslatableTextElement.translation_reapplier-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">translation_reapplier</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.translation_reapplier-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.translation_reapplier"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.translation_reapplier-364"><a href="#TranslatableTextElement.translation_reapplier-364"><span class="linenos">364</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">translation_reapplier</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="TranslatableTextElement.translation_reapplier-365"><a href="#TranslatableTextElement.translation_reapplier-365"><span class="linenos">365</span></a>        <span class="n">waiting_set</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">CoroID</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="p">{</span><span class="n">i</span><span class="o">.</span><span class="n">coro_id</span><span class="p">}</span>
</span><span id="TranslatableTextElement.translation_reapplier-366"><a href="#TranslatableTextElement.translation_reapplier-366"><span class="linenos">366</span></a>        <span class="c1"># await i(WaitCoroRequest().list(waiting_set))  # TODO: Not Implemented currently</span>
</span><span id="TranslatableTextElement.translation_reapplier-367"><a href="#TranslatableTextElement.translation_reapplier-367"><span class="linenos">367</span></a>        <span class="k">for</span> <span class="n">coro_id</span> <span class="ow">in</span> <span class="n">waiting_set</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translation_reapplier-368"><a href="#TranslatableTextElement.translation_reapplier-368"><span class="linenos">368</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translation_reapplier-369"><a href="#TranslatableTextElement.translation_reapplier-369"><span class="linenos">369</span></a>                <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">WaitCoroRequest</span><span class="p">()</span><span class="o">.</span><span class="n">single</span><span class="p">(</span><span class="n">coro_id</span><span class="p">))</span>
</span><span id="TranslatableTextElement.translation_reapplier-370"><a href="#TranslatableTextElement.translation_reapplier-370"><span class="linenos">370</span></a>            <span class="k">except</span> <span class="n">CoroutineNotFoundError</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translation_reapplier-371"><a href="#TranslatableTextElement.translation_reapplier-371"><span class="linenos">371</span></a>                <span class="k">pass</span>
</span><span id="TranslatableTextElement.translation_reapplier-372"><a href="#TranslatableTextElement.translation_reapplier-372"><span class="linenos">372</span></a>        
</span><span id="TranslatableTextElement.translation_reapplier-373"><a href="#TranslatableTextElement.translation_reapplier-373"><span class="linenos">373</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">current_translation_reapplier_coros_ids</span> <span class="o">-</span> <span class="n">waiting_set</span>
</span><span id="TranslatableTextElement.translation_reapplier-374"><a href="#TranslatableTextElement.translation_reapplier-374"><span class="linenos">374</span></a>        
</span><span id="TranslatableTextElement.translation_reapplier-375"><a href="#TranslatableTextElement.translation_reapplier-375"><span class="linenos">375</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translation_reapplier-376"><a href="#TranslatableTextElement.translation_reapplier-376"><span class="linenos">376</span></a>            <span class="k">return</span>
</span><span id="TranslatableTextElement.translation_reapplier-377"><a href="#TranslatableTextElement.translation_reapplier-377"><span class="linenos">377</span></a>        
</span><span id="TranslatableTextElement.translation_reapplier-378"><a href="#TranslatableTextElement.translation_reapplier-378"><span class="linenos">378</span></a>        <span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span>
</span><span id="TranslatableTextElement.translation_reapplier-379"><a href="#TranslatableTextElement.translation_reapplier-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="p">)()</span>
</span><span id="TranslatableTextElement.translation_reapplier-380"><a href="#TranslatableTextElement.translation_reapplier-380"><span class="linenos">380</span></a>        <span class="k">for</span> <span class="n">lang</span><span class="p">,</span> <span class="n">end_lang</span> <span class="ow">in</span> <span class="n">lang_changing_queue</span><span class="p">:</span>
</span><span id="TranslatableTextElement.translation_reapplier-381"><a href="#TranslatableTextElement.translation_reapplier-381"><span class="linenos">381</span></a>            <span class="k">for</span> <span class="n">text_element</span><span class="p">,</span> <span class="n">translate_me</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">elements_and_their_translatable_text</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="TranslatableTextElement.translation_reapplier-382"><a href="#TranslatableTextElement.translation_reapplier-382"><span class="linenos">382</span></a>                <span class="n">text_element</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="n">translate_me</span><span class="o">.</span><span class="n">to_str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translator</span><span class="p">,</span> <span class="n">end_lang</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.register_on_lang_changed_handler" class="classattr">
                                        <input id="TranslatableTextElement.register_on_lang_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">register_on_lang_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.register_on_lang_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.register_on_lang_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.register_on_lang_changed_handler-384"><a href="#TranslatableTextElement.register_on_lang_changed_handler-384"><span class="linenos">384</span></a>    <span class="k">def</span> <span class="nf">register_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement.register_on_lang_changed_handler-385"><a href="#TranslatableTextElement.register_on_lang_changed_handler-385"><span class="linenos">385</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement.register_on_lang_changed_handler-386"><a href="#TranslatableTextElement.register_on_lang_changed_handler-386"><span class="linenos">386</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.aregister_on_lang_changed_handler" class="classattr">
                                        <input id="TranslatableTextElement.aregister_on_lang_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aregister_on_lang_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.aregister_on_lang_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.aregister_on_lang_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.aregister_on_lang_changed_handler-388"><a href="#TranslatableTextElement.aregister_on_lang_changed_handler-388"><span class="linenos">388</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aregister_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement.aregister_on_lang_changed_handler-389"><a href="#TranslatableTextElement.aregister_on_lang_changed_handler-389"><span class="linenos">389</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement.aregister_on_lang_changed_handler-390"><a href="#TranslatableTextElement.aregister_on_lang_changed_handler-390"><span class="linenos">390</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">register_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.remove_on_lang_changed_handler" class="classattr">
                                        <input id="TranslatableTextElement.remove_on_lang_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">remove_on_lang_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.remove_on_lang_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.remove_on_lang_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.remove_on_lang_changed_handler-392"><a href="#TranslatableTextElement.remove_on_lang_changed_handler-392"><span class="linenos">392</span></a>    <span class="k">def</span> <span class="nf">remove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement.remove_on_lang_changed_handler-393"><a href="#TranslatableTextElement.remove_on_lang_changed_handler-393"><span class="linenos">393</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement.remove_on_lang_changed_handler-394"><a href="#TranslatableTextElement.remove_on_lang_changed_handler-394"><span class="linenos">394</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.aremove_on_lang_changed_handler" class="classattr">
                                        <input id="TranslatableTextElement.aremove_on_lang_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aremove_on_lang_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.aremove_on_lang_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.aremove_on_lang_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.aremove_on_lang_changed_handler-396"><a href="#TranslatableTextElement.aremove_on_lang_changed_handler-396"><span class="linenos">396</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aremove_on_lang_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TranslatableTextElement.aremove_on_lang_changed_handler-397"><a href="#TranslatableTextElement.aremove_on_lang_changed_handler-397"><span class="linenos">397</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="TranslatableTextElement.aremove_on_lang_changed_handler-398"><a href="#TranslatableTextElement.aremove_on_lang_changed_handler-398"><span class="linenos">398</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">remove_handler</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">text_translation_language_chooser</span><span class="o">.</span><span class="n">translation_language_changed_event</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">on_lang_changed</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="TranslatableTextElement.on_lang_changed" class="classattr">
                                        <input id="TranslatableTextElement.on_lang_changed-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">on_lang_changed</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">event</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Hashable</span>, </span><span class="param"><span class="n">data</span><span class="p">:</span> <span class="n">typing</span><span class="o">.</span><span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TranslatableTextElement.on_lang_changed-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TranslatableTextElement.on_lang_changed"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TranslatableTextElement.on_lang_changed-400"><a href="#TranslatableTextElement.on_lang_changed-400"><span class="linenos">400</span></a>    <span class="k">def</span> <span class="nf">on_lang_changed</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="n">Tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]):</span>
</span><span id="TranslatableTextElement.on_lang_changed-401"><a href="#TranslatableTextElement.on_lang_changed-401"><span class="linenos">401</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">lang_changing_queue</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TranslatableTextElement.on_lang_changed-402"><a href="#TranslatableTextElement.on_lang_changed-402"><span class="linenos">402</span></a>        <span class="n">put_coro</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">start_translation_reapplier</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TTE">
                    <div class="attr variable">
            <span class="name">TTE</span>        =
<input id="TTE-view-value" class="view-value-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
            <label class="view-value-button pdoc-button" for="TTE-view-value"></label><span class="default_value">&lt;class &#39;<a href="#TranslatableTextElement">TranslatableTextElement</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#TTE"></a>
    
    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>