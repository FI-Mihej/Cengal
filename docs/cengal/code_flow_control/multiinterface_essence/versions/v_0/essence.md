---
title: essence
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.code_flow_control<wbr>.multiinterface_essence<wbr>.versions<wbr>.v_0<wbr>.essence    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-essence-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-essence-view-source"><span>View Source</span></label>

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
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.3.3&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a><span class="kn">from</span> <span class="nn">inspect</span> <span class="kn">import</span> <span class="n">isclass</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a><span class="kn">from</span> <span class="nn">cengal.introspection.inspect</span> <span class="kn">import</span> <span class="n">get_exception</span>
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.args_manager</span> <span class="kn">import</span> <span class="n">EntityArgsHolder</span>
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">NoReturn</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Dict</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">TypeVar</span><span class="p">,</span> <span class="n">Generic</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">Sequence</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a><span class="c1"># from enum import Enum</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a><span class="k">class</span> <span class="nc">EssenceModelException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="k">pass</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a><span class="k">class</span> <span class="nc">IncompatibleEssenceModelError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="c1"># Must be raised by constructor of EssenceInterface class if incompatible essence_model was given</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="k">pass</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a><span class="k">class</span> <span class="nc">UnsuitableEssenceInterfaceError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="k">pass</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="k">class</span> <span class="nc">EssenceInterfaceIsNotApplicableError</span><span class="p">(</span><span class="n">UnsuitableEssenceInterfaceError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>    <span class="c1"># Must be raised by EssenceModel.__call__ when requested EssenceInterface is not active (applicable)</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>    <span class="k">pass</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="k">class</span> <span class="nc">EssenceInterfaceIsNotRegisteredError</span><span class="p">(</span><span class="n">UnsuitableEssenceInterfaceError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a>    <span class="c1"># Must be raised by EssenceModel.__call__ when requested EssenceInterface is not registered</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>    <span class="k">pass</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="k">class</span> <span class="nc">EssenceModelCanNotInjectSelfError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Must be raised by EssenceModel.emi_inject_model when an object of a class A(EssenceModel) tries</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="sd">    to inject class A - type(self)</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="sd">    This behavior is restricted since it may lead to: </span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="sd">        - endless recursion</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="sd">        - interface collisions when high order model will include several instances of the same interface class&quot;&quot;&quot;</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a>    <span class="k">pass</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="k">class</span> <span class="nc">EssenceModelCanNotBeInjectedError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a>    <span class="c1"># Must be raised by EssenceModel.emi_inject_model if injectable model can not be injected (incompatible)</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a>    <span class="k">pass</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="k">class</span> <span class="nc">EssenceModelIsNotInjectedError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a>    <span class="c1"># Must be raised by EssenceModel.emi_injected_model if not injected model was requested</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a>    <span class="k">pass</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="k">class</span> <span class="nc">IncompatibleHighOrderEssenceModelError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a>    <span class="c1"># Must be raised by EssenceModel.emu_behave_as_unknown_model method if incompatible on attempt to inject it to</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a>    <span class="c1"># incompatible high order model</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>    <span class="k">pass</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a><span class="k">class</span> <span class="nc">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span><span class="p">(</span><span class="ne">NotImplementedError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a>    <span class="k">pass</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="k">class</span> <span class="nc">EssenceModelInheritanceAbstract</span><span class="p">:</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">failed_worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>    <span class="k">def</span> <span class="nf">_em_check_applicability_of_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a><span class="k">class</span> <span class="nc">EssenceModelInjectionAbstract</span><span class="p">:</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a>    <span class="k">def</span> <span class="nf">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a><span class="k">class</span> <span class="nc">EssenceModelUnknownInjectionAbstract</span><span class="p">:</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>    
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    <span class="k">def</span> <span class="nf">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>    <span class="k">def</span> <span class="nf">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a>    
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>    <span class="k">def</span> <span class="nf">_emu_notify_unknown_models_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a><span class="k">class</span> <span class="nc">EssenceModel</span><span class="p">(</span><span class="n">EssenceModelInheritanceAbstract</span><span class="p">,</span> <span class="n">EssenceModelInjectionAbstract</span><span class="p">,</span> <span class="n">EssenceModelUnknownInjectionAbstract</span><span class="p">):</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Must contain related data in a consistent state.</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a><span class="sd">    </span>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="sd">    In order to do this, you must reload `em_on_model_updated()` and `emi_on_injected_model_updated()` methods.</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="sd">    Your interfaces can provide some appropriate information though an additional `parameters of em_on_model_updated()`</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a><span class="sd">    and `emi_on_injected_model_updated()` methods.</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a><span class="sd">    </span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a><span class="sd">    Do not forget to:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a><span class="sd">      - run `self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)` at</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a><span class="sd">          the end of your `em_on_model_updated()`</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a><span class="sd">      - run `self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)` at</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a><span class="sd">          the end of your `emi_on_injected_model_updated()`&quot;&quot;&quot;</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>    <span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="c1"># emu_compatible_high_order_essence_model_class: Optional[Type[&#39;EssenceModel&#39;]] = None</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>    <span class="n">emu_compatible_high_order_essence_model_classes</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_raise_on_uninjectable_model</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_raise_on_incompatible_high_order_model</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Should be called in order to get needed model interface&quot;&quot;&quot;</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>            <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>                <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>                <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>                    <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>                    <span class="k">break</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>            <span class="k">if</span> <span class="n">injected_model_interface</span><span class="p">:</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>                <span class="k">return</span> <span class="n">injected_model_interface</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotApplicableError</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotRegisteredError</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">failed_worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>        <span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">em_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a>        <span class="k">except</span> <span class="p">(</span><span class="n">EssenceInterfaceIsNotApplicableError</span><span class="p">,</span> <span class="n">EssenceInterfaceIsNotRegisteredError</span><span class="p">)</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>        <span class="k">if</span> <span class="n">interface</span><span class="p">:</span>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>            <span class="k">return</span> <span class="n">worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="k">if</span> <span class="n">failed_worker</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>                <span class="k">return</span> <span class="n">failed_worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">exception</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>    
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>        <span class="n">has_own_interface</span> <span class="o">=</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> \
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>                            <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>        <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_has_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span> <span class="ow">or</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>                <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>                <span class="k">break</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>        <span class="k">return</span> <span class="n">has_own_interface</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_interface</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a>        <span class="n">own_interface_active</span> <span class="o">=</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>        <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>                <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>                <span class="k">break</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>        <span class="k">return</span> <span class="n">own_interface_active</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_active_interface</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>        <span class="n">own_active_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>        <span class="n">injected_models_active_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>            <span class="n">injected_models_active_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_active_interfaces</span><span class="p">())</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>        <span class="k">return</span> <span class="n">own_active_interfaces</span> <span class="o">|</span> <span class="n">injected_models_active_interfaces</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        <span class="n">own_all_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="n">injected_models_all_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>            <span class="n">injected_models_all_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_all_interfaces</span><span class="p">())</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>        <span class="k">return</span> <span class="n">own_all_interfaces</span> <span class="o">|</span> <span class="n">injected_models_all_interfaces</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">_em_check_applicability_of_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>        <span class="n">new_interfaces</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>        <span class="n">new_possible_interfaces</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>        <span class="k">for</span> <span class="n">interface_class</span><span class="p">,</span> <span class="n">interface</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>                <span class="n">new_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>                <span class="n">new_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>        <span class="k">for</span> <span class="n">interface_class</span><span class="p">,</span> <span class="n">interface</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>                <span class="n">new_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>                <span class="n">new_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span> <span class="o">=</span> <span class="n">new_interfaces</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span> <span class="o">=</span> <span class="n">new_possible_interfaces</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Must be run by EssenceInterface (by running EssenceInterface.notify_model_about_change method) after changing</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a><span class="sd">          model&#39;s data. It is enough to run in once per a method - at the end of the method work.</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a><span class="sd">        In &#39;super&#39; in method of inherit class should be run at the end of the method&quot;&quot;&quot;</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">interface_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">):</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="n">interface_class</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>        <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Will be called after high order model successfully registered this mode&quot;&quot;&quot;</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="n">high_order_model</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>        <span class="c1"># Will be called before high order model actually unregistered this mode</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>        <span class="c1"># Should use &#39;EssenceModel&#39; instead of Type[&#39;EssenceModel&#39;] since we should use result of fully constructed</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a>        <span class="c1">#   essence_model with all needed interfaces - result of an appropriate factory work</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>        <span class="n">essence_model_class</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">essence_model</span><span class="p">)</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">essence_model</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">):</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>            <span class="k">raise</span> <span class="n">EssenceModelCanNotInjectSelfError</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>        
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>        <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a>            <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a>            <span class="k">if</span> <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)):</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>                <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_raise_on_incompatible_high_order_model</span><span class="p">:</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>                    <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>        <span class="n">injected</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>        <span class="k">if</span> <span class="n">injectable_model</span><span class="p">:</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a>            <span class="n">essence_model</span><span class="o">.</span><span class="n">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a>            <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a>                <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_behave_as_unknown_model</span><span class="p">()</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a>            
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>            <span class="n">injected</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_raise_on_uninjectable_model</span><span class="p">:</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>                <span class="k">raise</span> <span class="n">EssenceModelCanNotBeInjectedError</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>            
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="n">injected</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a>        <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">)</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">:</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>            <span class="k">raise</span> <span class="n">EssenceModelIsNotInjectedError</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="c1"># In &#39;super&#39; in method of inherit class should be run at the end of the method</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="c1"># With deep injection it will be like (model_3, model_2, model_1, interface_1, arg_1, arg_2, arg_3)</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="c1">#   where `interface_1` is an interface of the `model_1`</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">essence_model_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>    <span class="k">def</span> <span class="nf">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span><span class="p">):</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>            <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>            <span class="n">high_order_model</span><span class="o">.</span><span class="n">emi_on_injected_model_updated</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>        <span class="n">injected_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="n">injected_model</span><span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        <span class="n">injected_model</span><span class="o">.</span><span class="n">emi_on_unregistering_from_high_order_model</span><span class="p">()</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in order to make this model compatible with more than one high order models</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a><span class="sd">        Args:</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a><span class="sd">            high_order_model_class (Type[): [description]</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a><span class="sd">        Returns:</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a><span class="sd">            bool: [description]</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>        <span class="c1"># return high_order_model_class == self.emu_compatible_high_order_essence_model_class</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="k">return</span> <span class="n">high_order_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_compatible_high_order_essence_model_classes</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>        <span class="c1"># Should be called by a high order model for an unknown injected model</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="c1"># if type(self.__emi_high_order_model) != self.emu_compatible_high_order_essence_model_class:</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="p">):</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>            <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="o">.</span><span class="n">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">emu_on_behave_as_unknown_model</span><span class="p">()</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="k">pass</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>    <span class="k">def</span> <span class="nf">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">requester</span><span class="p">]]</span> <span class="o">=</span> <span class="n">requester</span>
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="nf">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>        <span class="n">model_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">requester</span><span class="p">)</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="n">model_type</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">:</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">[</span><span class="n">model_type</span><span class="p">]</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>    <span class="k">def</span> <span class="nf">_emu_notify_unknown_models_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="k">for</span> <span class="n">umodel</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>            <span class="n">unknown_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">umodel</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>            <span class="n">unknown_model</span><span class="o">.</span><span class="n">emu_on_model_changed_callback</span><span class="p">()</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="k">raise</span> <span class="n">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a><span class="n">Model</span> <span class="o">=</span> <span class="n">TypeVar</span><span class="p">(</span><span class="s1">&#39;Model&#39;</span><span class="p">,</span> <span class="n">bound</span><span class="o">=</span><span class="n">EssenceModel</span><span class="p">)</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a><span class="k">class</span> <span class="nc">EssenceInterface</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">Model</span><span class="p">]):</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>    <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]</span> <span class="o">=</span> <span class="n">EssenceModel</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">__init_subclass__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__init_subclass__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>        <span class="bp">cls</span><span class="o">.</span><span class="n">essence_model_class</span> <span class="o">=</span> <span class="n">EssenceModel</span> <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">essence_model_class</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">em</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__check_essence_mode_type</span><span class="p">()</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>    <span class="k">def</span> <span class="nf">__check_essence_mode_type</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">essence_model_class</span><span class="p">):</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>            <span class="k">raise</span> <span class="n">IncompatibleEssenceModelError</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>    <span class="k">def</span> <span class="nf">applicable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>    <span class="k">def</span> <span class="nf">_applicable_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">applicable</span><span class="p">()</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span><span class="p">:</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>            <span class="k">for</span> <span class="n">handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="p">:</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>                <span class="n">handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a>        
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>    
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>    <span class="k">def</span> <span class="nf">add_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>    
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>    <span class="k">def</span> <span class="nf">discard_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>    <span class="k">def</span> <span class="nf">notify_model_about_change</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="c1"># Must be run by EssenceInterface&#39;s methods if and after changing model&#39;s data. It is enough to run in once per</span>
</span><span id="L-481"><a href="#L-481"><span class="linenos">481</span></a>        <span class="c1">#   a method - at the end of the method work.</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos">482</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="o">.</span><span class="n">em_on_model_updated</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-483"><a href="#L-483"><span class="linenos">483</span></a>
</span><span id="L-484"><a href="#L-484"><span class="linenos">484</span></a>
</span><span id="L-485"><a href="#L-485"><span class="linenos">485</span></a><span class="k">def</span> <span class="nf">essence_model_changer</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos">486</span></a>    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="n">EssenceInterface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos">487</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos">488</span></a>            <span class="n">func</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos">489</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos">490</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">notify_model_about_change</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos">491</span></a>
</span><span id="L-492"><a href="#L-492"><span class="linenos">492</span></a>    <span class="k">return</span> <span class="n">wrapper</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos">493</span></a>
</span><span id="L-494"><a href="#L-494"><span class="linenos">494</span></a>
</span><span id="L-495"><a href="#L-495"><span class="linenos">495</span></a><span class="n">em_changer</span> <span class="o">=</span> <span class="n">essence_model_changer</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos">496</span></a>
</span><span id="L-497"><a href="#L-497"><span class="linenos">497</span></a>
</span><span id="L-498"><a href="#L-498"><span class="linenos">498</span></a><span class="k">class</span> <span class="nc">EssenceModelFactoryExample</span><span class="p">:</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos">499</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-500"><a href="#L-500"><span class="linenos">500</span></a>        <span class="n">model</span><span class="p">:</span> <span class="n">EssenceModel</span> <span class="o">=</span> <span class="n">EssenceModel</span><span class="p">()</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos">501</span></a>        <span class="n">model</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="n">EssenceInterface</span><span class="p">)</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos">502</span></a>        <span class="k">return</span> <span class="n">model</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos">503</span></a>
</span><span id="L-504"><a href="#L-504"><span class="linenos">504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos">505</span></a><span class="k">def</span> <span class="nf">simple_essence_model_factory</span><span class="p">(</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos">506</span></a>        <span class="n">model</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceModel</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">],</span> 
</span><span id="L-507"><a href="#L-507"><span class="linenos">507</span></a>        <span class="n">interfaces</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos">508</span></a>                <span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> 
</span><span id="L-509"><a href="#L-509"><span class="linenos">509</span></a>                <span class="n">EntityArgsHolder</span><span class="p">,</span> 
</span><span id="L-510"><a href="#L-510"><span class="linenos">510</span></a>                <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">]]</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos">511</span></a>            <span class="p">]</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos">512</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EssenceModel</span><span class="p">:</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos">513</span></a>    <span class="n">model_instance</span><span class="p">:</span> <span class="n">EssenceModel</span> <span class="o">=</span> <span class="n">model</span><span class="p">()</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos">514</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="nb">type</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">)):</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos">515</span></a>        <span class="n">interfaces</span> <span class="o">=</span> <span class="p">(</span><span class="n">interfaces</span><span class="p">,)</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos">516</span></a>    
</span><span id="L-517"><a href="#L-517"><span class="linenos">517</span></a>    <span class="k">for</span> <span class="n">interface</span> <span class="ow">in</span> <span class="n">interfaces</span><span class="p">:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos">518</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos">519</span></a>            <span class="k">if</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">):</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos">520</span></a>                <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos">521</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">):</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos">522</span></a>            <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="o">*</span><span class="n">interface</span><span class="o">.</span><span class="n">entity_args_kwargs</span><span class="p">())</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos">523</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos">524</span></a>            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong interface type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-525"><a href="#L-525"><span class="linenos">525</span></a>
</span><span id="L-526"><a href="#L-526"><span class="linenos">526</span></a>    <span class="k">return</span> <span class="n">model_instance</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos">527</span></a>
</span><span id="L-528"><a href="#L-528"><span class="linenos">528</span></a>
</span><span id="L-529"><a href="#L-529"><span class="linenos">529</span></a><span class="n">simple_em_factory</span> <span class="o">=</span> <span class="n">simple_essence_model_factory</span>
</span></pre></div>


            </section>
                <section id="EssenceModelException">
                            <input id="EssenceModelException-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelException</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="EssenceModelException-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelException"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelException-45"><a href="#EssenceModelException-45"><span class="linenos">45</span></a><span class="k">class</span> <span class="nc">EssenceModelException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="EssenceModelException-46"><a href="#EssenceModelException-46"><span class="linenos">46</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="EssenceModelException.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceModelException.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceModelException.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IncompatibleEssenceModelError">
                            <input id="IncompatibleEssenceModelError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IncompatibleEssenceModelError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="IncompatibleEssenceModelError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IncompatibleEssenceModelError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IncompatibleEssenceModelError-49"><a href="#IncompatibleEssenceModelError-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">IncompatibleEssenceModelError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="IncompatibleEssenceModelError-50"><a href="#IncompatibleEssenceModelError-50"><span class="linenos">50</span></a>    <span class="c1"># Must be raised by constructor of EssenceInterface class if incompatible essence_model was given</span>
</span><span id="IncompatibleEssenceModelError-51"><a href="#IncompatibleEssenceModelError-51"><span class="linenos">51</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="IncompatibleEssenceModelError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="IncompatibleEssenceModelError.with_traceback" class="function">with_traceback</dd>
                <dd id="IncompatibleEssenceModelError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UnsuitableEssenceInterfaceError">
                            <input id="UnsuitableEssenceInterfaceError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnsuitableEssenceInterfaceError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="UnsuitableEssenceInterfaceError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnsuitableEssenceInterfaceError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnsuitableEssenceInterfaceError-54"><a href="#UnsuitableEssenceInterfaceError-54"><span class="linenos">54</span></a><span class="k">class</span> <span class="nc">UnsuitableEssenceInterfaceError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="UnsuitableEssenceInterfaceError-55"><a href="#UnsuitableEssenceInterfaceError-55"><span class="linenos">55</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="UnsuitableEssenceInterfaceError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnsuitableEssenceInterfaceError.with_traceback" class="function">with_traceback</dd>
                <dd id="UnsuitableEssenceInterfaceError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceInterfaceIsNotApplicableError">
                            <input id="EssenceInterfaceIsNotApplicableError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceInterfaceIsNotApplicableError</span><wbr>(<span class="base"><a href="#UnsuitableEssenceInterfaceError">UnsuitableEssenceInterfaceError</a></span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="EssenceInterfaceIsNotApplicableError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterfaceIsNotApplicableError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterfaceIsNotApplicableError-58"><a href="#EssenceInterfaceIsNotApplicableError-58"><span class="linenos">58</span></a><span class="k">class</span> <span class="nc">EssenceInterfaceIsNotApplicableError</span><span class="p">(</span><span class="n">UnsuitableEssenceInterfaceError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="EssenceInterfaceIsNotApplicableError-59"><a href="#EssenceInterfaceIsNotApplicableError-59"><span class="linenos">59</span></a>    <span class="c1"># Must be raised by EssenceModel.__call__ when requested EssenceInterface is not active (applicable)</span>
</span><span id="EssenceInterfaceIsNotApplicableError-60"><a href="#EssenceInterfaceIsNotApplicableError-60"><span class="linenos">60</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="EssenceInterfaceIsNotApplicableError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceInterfaceIsNotApplicableError.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceInterfaceIsNotApplicableError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceInterfaceIsNotRegisteredError">
                            <input id="EssenceInterfaceIsNotRegisteredError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceInterfaceIsNotRegisteredError</span><wbr>(<span class="base"><a href="#UnsuitableEssenceInterfaceError">UnsuitableEssenceInterfaceError</a></span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="EssenceInterfaceIsNotRegisteredError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterfaceIsNotRegisteredError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterfaceIsNotRegisteredError-63"><a href="#EssenceInterfaceIsNotRegisteredError-63"><span class="linenos">63</span></a><span class="k">class</span> <span class="nc">EssenceInterfaceIsNotRegisteredError</span><span class="p">(</span><span class="n">UnsuitableEssenceInterfaceError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="EssenceInterfaceIsNotRegisteredError-64"><a href="#EssenceInterfaceIsNotRegisteredError-64"><span class="linenos">64</span></a>    <span class="c1"># Must be raised by EssenceModel.__call__ when requested EssenceInterface is not registered</span>
</span><span id="EssenceInterfaceIsNotRegisteredError-65"><a href="#EssenceInterfaceIsNotRegisteredError-65"><span class="linenos">65</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="EssenceInterfaceIsNotRegisteredError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceInterfaceIsNotRegisteredError.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceInterfaceIsNotRegisteredError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceModelCanNotInjectSelfError">
                            <input id="EssenceModelCanNotInjectSelfError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelCanNotInjectSelfError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="EssenceModelCanNotInjectSelfError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelCanNotInjectSelfError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelCanNotInjectSelfError-68"><a href="#EssenceModelCanNotInjectSelfError-68"><span class="linenos">68</span></a><span class="k">class</span> <span class="nc">EssenceModelCanNotInjectSelfError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="EssenceModelCanNotInjectSelfError-69"><a href="#EssenceModelCanNotInjectSelfError-69"><span class="linenos">69</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Must be raised by EssenceModel.emi_inject_model when an object of a class A(EssenceModel) tries</span>
</span><span id="EssenceModelCanNotInjectSelfError-70"><a href="#EssenceModelCanNotInjectSelfError-70"><span class="linenos">70</span></a><span class="sd">    to inject class A - type(self)</span>
</span><span id="EssenceModelCanNotInjectSelfError-71"><a href="#EssenceModelCanNotInjectSelfError-71"><span class="linenos">71</span></a>
</span><span id="EssenceModelCanNotInjectSelfError-72"><a href="#EssenceModelCanNotInjectSelfError-72"><span class="linenos">72</span></a><span class="sd">    This behavior is restricted since it may lead to: </span>
</span><span id="EssenceModelCanNotInjectSelfError-73"><a href="#EssenceModelCanNotInjectSelfError-73"><span class="linenos">73</span></a><span class="sd">        - endless recursion</span>
</span><span id="EssenceModelCanNotInjectSelfError-74"><a href="#EssenceModelCanNotInjectSelfError-74"><span class="linenos">74</span></a><span class="sd">        - interface collisions when high order model will include several instances of the same interface class&quot;&quot;&quot;</span>
</span><span id="EssenceModelCanNotInjectSelfError-75"><a href="#EssenceModelCanNotInjectSelfError-75"><span class="linenos">75</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Must be raised by <a href="#EssenceModel.emi_inject_model">EssenceModel.emi_inject_model</a> when an object of a class A(EssenceModel) tries
to inject class A - type(self)</p>

<p>This behavior is restricted since it may lead to: 
    - endless recursion
    - interface collisions when high order model will include several instances of the same interface class</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="EssenceModelCanNotInjectSelfError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceModelCanNotInjectSelfError.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceModelCanNotInjectSelfError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceModelCanNotBeInjectedError">
                            <input id="EssenceModelCanNotBeInjectedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelCanNotBeInjectedError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="EssenceModelCanNotBeInjectedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelCanNotBeInjectedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelCanNotBeInjectedError-78"><a href="#EssenceModelCanNotBeInjectedError-78"><span class="linenos">78</span></a><span class="k">class</span> <span class="nc">EssenceModelCanNotBeInjectedError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="EssenceModelCanNotBeInjectedError-79"><a href="#EssenceModelCanNotBeInjectedError-79"><span class="linenos">79</span></a>    <span class="c1"># Must be raised by EssenceModel.emi_inject_model if injectable model can not be injected (incompatible)</span>
</span><span id="EssenceModelCanNotBeInjectedError-80"><a href="#EssenceModelCanNotBeInjectedError-80"><span class="linenos">80</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="EssenceModelCanNotBeInjectedError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceModelCanNotBeInjectedError.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceModelCanNotBeInjectedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceModelIsNotInjectedError">
                            <input id="EssenceModelIsNotInjectedError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelIsNotInjectedError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="EssenceModelIsNotInjectedError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelIsNotInjectedError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelIsNotInjectedError-83"><a href="#EssenceModelIsNotInjectedError-83"><span class="linenos">83</span></a><span class="k">class</span> <span class="nc">EssenceModelIsNotInjectedError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="EssenceModelIsNotInjectedError-84"><a href="#EssenceModelIsNotInjectedError-84"><span class="linenos">84</span></a>    <span class="c1"># Must be raised by EssenceModel.emi_injected_model if not injected model was requested</span>
</span><span id="EssenceModelIsNotInjectedError-85"><a href="#EssenceModelIsNotInjectedError-85"><span class="linenos">85</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="EssenceModelIsNotInjectedError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="EssenceModelIsNotInjectedError.with_traceback" class="function">with_traceback</dd>
                <dd id="EssenceModelIsNotInjectedError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="IncompatibleHighOrderEssenceModelError">
                            <input id="IncompatibleHighOrderEssenceModelError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">IncompatibleHighOrderEssenceModelError</span><wbr>(<span class="base">builtins.RuntimeError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="IncompatibleHighOrderEssenceModelError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#IncompatibleHighOrderEssenceModelError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="IncompatibleHighOrderEssenceModelError-88"><a href="#IncompatibleHighOrderEssenceModelError-88"><span class="linenos">88</span></a><span class="k">class</span> <span class="nc">IncompatibleHighOrderEssenceModelError</span><span class="p">(</span><span class="ne">RuntimeError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="IncompatibleHighOrderEssenceModelError-89"><a href="#IncompatibleHighOrderEssenceModelError-89"><span class="linenos">89</span></a>    <span class="c1"># Must be raised by EssenceModel.emu_behave_as_unknown_model method if incompatible on attempt to inject it to</span>
</span><span id="IncompatibleHighOrderEssenceModelError-90"><a href="#IncompatibleHighOrderEssenceModelError-90"><span class="linenos">90</span></a>    <span class="c1"># incompatible high order model</span>
</span><span id="IncompatibleHighOrderEssenceModelError-91"><a href="#IncompatibleHighOrderEssenceModelError-91"><span class="linenos">91</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Unspecified run-time error.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.RuntimeError</dt>
                                <dd id="IncompatibleHighOrderEssenceModelError.__init__" class="function">RuntimeError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="IncompatibleHighOrderEssenceModelError.with_traceback" class="function">with_traceback</dd>
                <dd id="IncompatibleHighOrderEssenceModelError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError">
                            <input id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span><wbr>(<span class="base">builtins.NotImplementedError</span>, <span class="base"><a href="#EssenceModelException">EssenceModelException</a></span>):

                <label class="view-source-button" for="UnknownEssenceModeBehaviorWasNotImplementedProperlyError-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#UnknownEssenceModeBehaviorWasNotImplementedProperlyError"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError-94"><a href="#UnknownEssenceModeBehaviorWasNotImplementedProperlyError-94"><span class="linenos">94</span></a><span class="k">class</span> <span class="nc">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span><span class="p">(</span><span class="ne">NotImplementedError</span><span class="p">,</span> <span class="n">EssenceModelException</span><span class="p">):</span>
</span><span id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError-95"><a href="#UnknownEssenceModeBehaviorWasNotImplementedProperlyError-95"><span class="linenos">95</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Method or function hasn't been implemented yet.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.NotImplementedError</dt>
                                <dd id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError.__init__" class="function">NotImplementedError</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError.with_traceback" class="function">with_traceback</dd>
                <dd id="UnknownEssenceModeBehaviorWasNotImplementedProperlyError.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="EssenceModelInheritanceAbstract">
                            <input id="EssenceModelInheritanceAbstract-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelInheritanceAbstract</span>:

                <label class="view-source-button" for="EssenceModelInheritanceAbstract-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract-98"><a href="#EssenceModelInheritanceAbstract-98"><span class="linenos"> 98</span></a><span class="k">class</span> <span class="nc">EssenceModelInheritanceAbstract</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-99"><a href="#EssenceModelInheritanceAbstract-99"><span class="linenos"> 99</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">failed_worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-100"><a href="#EssenceModelInheritanceAbstract-100"><span class="linenos">100</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-101"><a href="#EssenceModelInheritanceAbstract-101"><span class="linenos">101</span></a>
</span><span id="EssenceModelInheritanceAbstract-102"><a href="#EssenceModelInheritanceAbstract-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-103"><a href="#EssenceModelInheritanceAbstract-103"><span class="linenos">103</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-104"><a href="#EssenceModelInheritanceAbstract-104"><span class="linenos">104</span></a>
</span><span id="EssenceModelInheritanceAbstract-105"><a href="#EssenceModelInheritanceAbstract-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-106"><a href="#EssenceModelInheritanceAbstract-106"><span class="linenos">106</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-107"><a href="#EssenceModelInheritanceAbstract-107"><span class="linenos">107</span></a>
</span><span id="EssenceModelInheritanceAbstract-108"><a href="#EssenceModelInheritanceAbstract-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-109"><a href="#EssenceModelInheritanceAbstract-109"><span class="linenos">109</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-110"><a href="#EssenceModelInheritanceAbstract-110"><span class="linenos">110</span></a>
</span><span id="EssenceModelInheritanceAbstract-111"><a href="#EssenceModelInheritanceAbstract-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModelInheritanceAbstract-112"><a href="#EssenceModelInheritanceAbstract-112"><span class="linenos">112</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-113"><a href="#EssenceModelInheritanceAbstract-113"><span class="linenos">113</span></a>
</span><span id="EssenceModelInheritanceAbstract-114"><a href="#EssenceModelInheritanceAbstract-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModelInheritanceAbstract-115"><a href="#EssenceModelInheritanceAbstract-115"><span class="linenos">115</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-116"><a href="#EssenceModelInheritanceAbstract-116"><span class="linenos">116</span></a>
</span><span id="EssenceModelInheritanceAbstract-117"><a href="#EssenceModelInheritanceAbstract-117"><span class="linenos">117</span></a>    <span class="k">def</span> <span class="nf">_em_check_applicability_of_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-118"><a href="#EssenceModelInheritanceAbstract-118"><span class="linenos">118</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-119"><a href="#EssenceModelInheritanceAbstract-119"><span class="linenos">119</span></a>
</span><span id="EssenceModelInheritanceAbstract-120"><a href="#EssenceModelInheritanceAbstract-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelInheritanceAbstract-121"><a href="#EssenceModelInheritanceAbstract-121"><span class="linenos">121</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-122"><a href="#EssenceModelInheritanceAbstract-122"><span class="linenos">122</span></a>
</span><span id="EssenceModelInheritanceAbstract-123"><a href="#EssenceModelInheritanceAbstract-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-124"><a href="#EssenceModelInheritanceAbstract-124"><span class="linenos">124</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInheritanceAbstract-125"><a href="#EssenceModelInheritanceAbstract-125"><span class="linenos">125</span></a>
</span><span id="EssenceModelInheritanceAbstract-126"><a href="#EssenceModelInheritanceAbstract-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract-127"><a href="#EssenceModelInheritanceAbstract-127"><span class="linenos">127</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="EssenceModelInheritanceAbstract.em_interface" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n"><a href="#EssenceInterface">EssenceInterface</a></span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_interface-102"><a href="#EssenceModelInheritanceAbstract.em_interface-102"><span class="linenos">102</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract.em_interface-103"><a href="#EssenceModelInheritanceAbstract.em_interface-103"><span class="linenos">103</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_has_interface" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_has_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_has_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_has_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_has_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_has_interface-105"><a href="#EssenceModelInheritanceAbstract.em_has_interface-105"><span class="linenos">105</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract.em_has_interface-106"><a href="#EssenceModelInheritanceAbstract.em_has_interface-106"><span class="linenos">106</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_interface_active" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_interface_active-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_interface_active</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_interface_active-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_interface_active"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_interface_active-108"><a href="#EssenceModelInheritanceAbstract.em_interface_active-108"><span class="linenos">108</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract.em_interface_active-109"><a href="#EssenceModelInheritanceAbstract.em_interface_active-109"><span class="linenos">109</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_active_interfaces" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_active_interfaces-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_active_interfaces</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">set</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_active_interfaces-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_active_interfaces"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_active_interfaces-111"><a href="#EssenceModelInheritanceAbstract.em_active_interfaces-111"><span class="linenos">111</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModelInheritanceAbstract.em_active_interfaces-112"><a href="#EssenceModelInheritanceAbstract.em_active_interfaces-112"><span class="linenos">112</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_all_interfaces" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_all_interfaces-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_all_interfaces</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">set</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_all_interfaces-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_all_interfaces"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_all_interfaces-114"><a href="#EssenceModelInheritanceAbstract.em_all_interfaces-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModelInheritanceAbstract.em_all_interfaces-115"><a href="#EssenceModelInheritanceAbstract.em_all_interfaces-115"><span class="linenos">115</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_on_model_updated" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_on_model_updated-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_on_model_updated</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_on_model_updated-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_on_model_updated"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_on_model_updated-120"><a href="#EssenceModelInheritanceAbstract.em_on_model_updated-120"><span class="linenos">120</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelInheritanceAbstract.em_on_model_updated-121"><a href="#EssenceModelInheritanceAbstract.em_on_model_updated-121"><span class="linenos">121</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_add_interface" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_add_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_add_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_add_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_add_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_add_interface-123"><a href="#EssenceModelInheritanceAbstract.em_add_interface-123"><span class="linenos">123</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract.em_add_interface-124"><a href="#EssenceModelInheritanceAbstract.em_add_interface-124"><span class="linenos">124</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInheritanceAbstract.em_remove_interface" class="classattr">
                                        <input id="EssenceModelInheritanceAbstract.em_remove_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_remove_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInheritanceAbstract.em_remove_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInheritanceAbstract.em_remove_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInheritanceAbstract.em_remove_interface-126"><a href="#EssenceModelInheritanceAbstract.em_remove_interface-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInheritanceAbstract.em_remove_interface-127"><a href="#EssenceModelInheritanceAbstract.em_remove_interface-127"><span class="linenos">127</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="EssenceModelInjectionAbstract">
                            <input id="EssenceModelInjectionAbstract-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelInjectionAbstract</span>:

                <label class="view-source-button" for="EssenceModelInjectionAbstract-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract-130"><a href="#EssenceModelInjectionAbstract-130"><span class="linenos">130</span></a><span class="k">class</span> <span class="nc">EssenceModelInjectionAbstract</span><span class="p">:</span>
</span><span id="EssenceModelInjectionAbstract-131"><a href="#EssenceModelInjectionAbstract-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract-132"><a href="#EssenceModelInjectionAbstract-132"><span class="linenos">132</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-133"><a href="#EssenceModelInjectionAbstract-133"><span class="linenos">133</span></a>
</span><span id="EssenceModelInjectionAbstract-134"><a href="#EssenceModelInjectionAbstract-134"><span class="linenos">134</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract-135"><a href="#EssenceModelInjectionAbstract-135"><span class="linenos">135</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-136"><a href="#EssenceModelInjectionAbstract-136"><span class="linenos">136</span></a>
</span><span id="EssenceModelInjectionAbstract-137"><a href="#EssenceModelInjectionAbstract-137"><span class="linenos">137</span></a>    <span class="k">def</span> <span class="nf">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract-138"><a href="#EssenceModelInjectionAbstract-138"><span class="linenos">138</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-139"><a href="#EssenceModelInjectionAbstract-139"><span class="linenos">139</span></a>
</span><span id="EssenceModelInjectionAbstract-140"><a href="#EssenceModelInjectionAbstract-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInjectionAbstract-141"><a href="#EssenceModelInjectionAbstract-141"><span class="linenos">141</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-142"><a href="#EssenceModelInjectionAbstract-142"><span class="linenos">142</span></a>
</span><span id="EssenceModelInjectionAbstract-143"><a href="#EssenceModelInjectionAbstract-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract-144"><a href="#EssenceModelInjectionAbstract-144"><span class="linenos">144</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-145"><a href="#EssenceModelInjectionAbstract-145"><span class="linenos">145</span></a>
</span><span id="EssenceModelInjectionAbstract-146"><a href="#EssenceModelInjectionAbstract-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="EssenceModelInjectionAbstract-147"><a href="#EssenceModelInjectionAbstract-147"><span class="linenos">147</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-148"><a href="#EssenceModelInjectionAbstract-148"><span class="linenos">148</span></a>
</span><span id="EssenceModelInjectionAbstract-149"><a href="#EssenceModelInjectionAbstract-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span>
</span><span id="EssenceModelInjectionAbstract-150"><a href="#EssenceModelInjectionAbstract-150"><span class="linenos">150</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract-151"><a href="#EssenceModelInjectionAbstract-151"><span class="linenos">151</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelInjectionAbstract-152"><a href="#EssenceModelInjectionAbstract-152"><span class="linenos">152</span></a>
</span><span id="EssenceModelInjectionAbstract-153"><a href="#EssenceModelInjectionAbstract-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="EssenceModelInjectionAbstract-154"><a href="#EssenceModelInjectionAbstract-154"><span class="linenos">154</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_registered_in_high_order_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">high_order_model</span><span class="p">:</span> <span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-131"><a href="#EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-132"><a href="#EssenceModelInjectionAbstract.emi_on_registered_in_high_order_model-132"><span class="linenos">132</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_unregistering_from_high_order_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-134"><a href="#EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-134"><span class="linenos">134</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-135"><a href="#EssenceModelInjectionAbstract.emi_on_unregistering_from_high_order_model-135"><span class="linenos">135</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_inject_model" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_inject_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_inject_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model</span><span class="p">:</span> <span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_inject_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_inject_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_inject_model-140"><a href="#EssenceModelInjectionAbstract.emi_inject_model-140"><span class="linenos">140</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelInjectionAbstract.emi_inject_model-141"><a href="#EssenceModelInjectionAbstract.emi_inject_model-141"><span class="linenos">141</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_injected_models" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_injected_models-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_injected_models</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_injected_models-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_injected_models"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_injected_models-143"><a href="#EssenceModelInjectionAbstract.emi_injected_models-143"><span class="linenos">143</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract.emi_injected_models-144"><a href="#EssenceModelInjectionAbstract.emi_injected_models-144"><span class="linenos">144</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_injected_model" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_injected_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_injected_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_injected_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_injected_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_injected_model-146"><a href="#EssenceModelInjectionAbstract.emi_injected_model-146"><span class="linenos">146</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="EssenceModelInjectionAbstract.emi_injected_model-147"><a href="#EssenceModelInjectionAbstract.emi_injected_model-147"><span class="linenos">147</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_on_injected_model_updated" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_on_injected_model_updated-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_injected_model_updated</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_on_injected_model_updated-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_on_injected_model_updated"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_on_injected_model_updated-149"><a href="#EssenceModelInjectionAbstract.emi_on_injected_model_updated-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span>
</span><span id="EssenceModelInjectionAbstract.emi_on_injected_model_updated-150"><a href="#EssenceModelInjectionAbstract.emi_on_injected_model_updated-150"><span class="linenos">150</span></a>            <span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelInjectionAbstract.emi_on_injected_model_updated-151"><a href="#EssenceModelInjectionAbstract.emi_on_injected_model_updated-151"><span class="linenos">151</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelInjectionAbstract.emi_remove_injected_model" class="classattr">
                                        <input id="EssenceModelInjectionAbstract.emi_remove_injected_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_remove_injected_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelInjectionAbstract.emi_remove_injected_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelInjectionAbstract.emi_remove_injected_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelInjectionAbstract.emi_remove_injected_model-153"><a href="#EssenceModelInjectionAbstract.emi_remove_injected_model-153"><span class="linenos">153</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">]):</span>
</span><span id="EssenceModelInjectionAbstract.emi_remove_injected_model-154"><a href="#EssenceModelInjectionAbstract.emi_remove_injected_model-154"><span class="linenos">154</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="EssenceModelUnknownInjectionAbstract">
                            <input id="EssenceModelUnknownInjectionAbstract-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelUnknownInjectionAbstract</span>:

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract-157"><a href="#EssenceModelUnknownInjectionAbstract-157"><span class="linenos">157</span></a><span class="k">class</span> <span class="nc">EssenceModelUnknownInjectionAbstract</span><span class="p">:</span>
</span><span id="EssenceModelUnknownInjectionAbstract-158"><a href="#EssenceModelUnknownInjectionAbstract-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelUnknownInjectionAbstract-159"><a href="#EssenceModelUnknownInjectionAbstract-159"><span class="linenos">159</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-160"><a href="#EssenceModelUnknownInjectionAbstract-160"><span class="linenos">160</span></a>    
</span><span id="EssenceModelUnknownInjectionAbstract-161"><a href="#EssenceModelUnknownInjectionAbstract-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-162"><a href="#EssenceModelUnknownInjectionAbstract-162"><span class="linenos">162</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-163"><a href="#EssenceModelUnknownInjectionAbstract-163"><span class="linenos">163</span></a>
</span><span id="EssenceModelUnknownInjectionAbstract-164"><a href="#EssenceModelUnknownInjectionAbstract-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-165"><a href="#EssenceModelUnknownInjectionAbstract-165"><span class="linenos">165</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-166"><a href="#EssenceModelUnknownInjectionAbstract-166"><span class="linenos">166</span></a>
</span><span id="EssenceModelUnknownInjectionAbstract-167"><a href="#EssenceModelUnknownInjectionAbstract-167"><span class="linenos">167</span></a>    <span class="k">def</span> <span class="nf">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-168"><a href="#EssenceModelUnknownInjectionAbstract-168"><span class="linenos">168</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-169"><a href="#EssenceModelUnknownInjectionAbstract-169"><span class="linenos">169</span></a>
</span><span id="EssenceModelUnknownInjectionAbstract-170"><a href="#EssenceModelUnknownInjectionAbstract-170"><span class="linenos">170</span></a>    <span class="k">def</span> <span class="nf">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-171"><a href="#EssenceModelUnknownInjectionAbstract-171"><span class="linenos">171</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-172"><a href="#EssenceModelUnknownInjectionAbstract-172"><span class="linenos">172</span></a>    
</span><span id="EssenceModelUnknownInjectionAbstract-173"><a href="#EssenceModelUnknownInjectionAbstract-173"><span class="linenos">173</span></a>    <span class="k">def</span> <span class="nf">_emu_notify_unknown_models_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-174"><a href="#EssenceModelUnknownInjectionAbstract-174"><span class="linenos">174</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-175"><a href="#EssenceModelUnknownInjectionAbstract-175"><span class="linenos">175</span></a>
</span><span id="EssenceModelUnknownInjectionAbstract-176"><a href="#EssenceModelUnknownInjectionAbstract-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-177"><a href="#EssenceModelUnknownInjectionAbstract-177"><span class="linenos">177</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span><span id="EssenceModelUnknownInjectionAbstract-178"><a href="#EssenceModelUnknownInjectionAbstract-178"><span class="linenos">178</span></a>
</span><span id="EssenceModelUnknownInjectionAbstract-179"><a href="#EssenceModelUnknownInjectionAbstract-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract-180"><a href="#EssenceModelUnknownInjectionAbstract-180"><span class="linenos">180</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            <div id="EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model" class="classattr">
                                        <input id="EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_is_compatible_high_order_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">high_order_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-158"><a href="#EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-158"><span class="linenos">158</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-159"><a href="#EssenceModelUnknownInjectionAbstract.emu_is_compatible_high_order_model-159"><span class="linenos">159</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model" class="classattr">
                                        <input id="EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_behave_as_unknown_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-161"><a href="#EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-161"><span class="linenos">161</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-162"><a href="#EssenceModelUnknownInjectionAbstract.emu_behave_as_unknown_model-162"><span class="linenos">162</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model" class="classattr">
                                        <input id="EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_on_behave_as_unknown_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-164"><a href="#EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-164"><span class="linenos">164</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-165"><a href="#EssenceModelUnknownInjectionAbstract.emu_on_behave_as_unknown_model-165"><span class="linenos">165</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback" class="classattr">
                                        <input id="EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_on_model_changed_callback</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-176"><a href="#EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-176"><span class="linenos">176</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-177"><a href="#EssenceModelUnknownInjectionAbstract.emu_on_model_changed_callback-177"><span class="linenos">177</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior" class="classattr">
                                        <input id="EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_is_in_unknown_model_behavior</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-179"><a href="#EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-179"><span class="linenos">179</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-180"><a href="#EssenceModelUnknownInjectionAbstract.emu_is_in_unknown_model_behavior-180"><span class="linenos">180</span></a>        <span class="k">raise</span> <span class="ne">NotImplementedError</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="EssenceModel">
                            <input id="EssenceModel-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModel</span><wbr>(<span class="base"><a href="#EssenceModelInheritanceAbstract">EssenceModelInheritanceAbstract</a></span>, <span class="base"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span>, <span class="base"><a href="#EssenceModelUnknownInjectionAbstract">EssenceModelUnknownInjectionAbstract</a></span>):

                <label class="view-source-button" for="EssenceModel-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel-183"><a href="#EssenceModel-183"><span class="linenos">183</span></a><span class="k">class</span> <span class="nc">EssenceModel</span><span class="p">(</span><span class="n">EssenceModelInheritanceAbstract</span><span class="p">,</span> <span class="n">EssenceModelInjectionAbstract</span><span class="p">,</span> <span class="n">EssenceModelUnknownInjectionAbstract</span><span class="p">):</span>
</span><span id="EssenceModel-184"><a href="#EssenceModel-184"><span class="linenos">184</span></a><span class="w">    </span><span class="sd">&quot;&quot;&quot;Must contain related data in a consistent state.</span>
</span><span id="EssenceModel-185"><a href="#EssenceModel-185"><span class="linenos">185</span></a><span class="sd">    </span>
</span><span id="EssenceModel-186"><a href="#EssenceModel-186"><span class="linenos">186</span></a><span class="sd">    In order to do this, you must reload `em_on_model_updated()` and `emi_on_injected_model_updated()` methods.</span>
</span><span id="EssenceModel-187"><a href="#EssenceModel-187"><span class="linenos">187</span></a><span class="sd">    Your interfaces can provide some appropriate information though an additional `parameters of em_on_model_updated()`</span>
</span><span id="EssenceModel-188"><a href="#EssenceModel-188"><span class="linenos">188</span></a><span class="sd">    and `emi_on_injected_model_updated()` methods.</span>
</span><span id="EssenceModel-189"><a href="#EssenceModel-189"><span class="linenos">189</span></a><span class="sd">    </span>
</span><span id="EssenceModel-190"><a href="#EssenceModel-190"><span class="linenos">190</span></a><span class="sd">    Do not forget to:</span>
</span><span id="EssenceModel-191"><a href="#EssenceModel-191"><span class="linenos">191</span></a><span class="sd">      - run `self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)` at</span>
</span><span id="EssenceModel-192"><a href="#EssenceModel-192"><span class="linenos">192</span></a><span class="sd">          the end of your `em_on_model_updated()`</span>
</span><span id="EssenceModel-193"><a href="#EssenceModel-193"><span class="linenos">193</span></a><span class="sd">      - run `self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)` at</span>
</span><span id="EssenceModel-194"><a href="#EssenceModel-194"><span class="linenos">194</span></a><span class="sd">          the end of your `emi_on_injected_model_updated()`&quot;&quot;&quot;</span>
</span><span id="EssenceModel-195"><a href="#EssenceModel-195"><span class="linenos">195</span></a>
</span><span id="EssenceModel-196"><a href="#EssenceModel-196"><span class="linenos">196</span></a>    <span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel-197"><a href="#EssenceModel-197"><span class="linenos">197</span></a>    <span class="c1"># emu_compatible_high_order_essence_model_class: Optional[Type[&#39;EssenceModel&#39;]] = None</span>
</span><span id="EssenceModel-198"><a href="#EssenceModel-198"><span class="linenos">198</span></a>    <span class="n">emu_compatible_high_order_essence_model_classes</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel-199"><a href="#EssenceModel-199"><span class="linenos">199</span></a>
</span><span id="EssenceModel-200"><a href="#EssenceModel-200"><span class="linenos">200</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-201"><a href="#EssenceModel-201"><span class="linenos">201</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-202"><a href="#EssenceModel-202"><span class="linenos">202</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-203"><a href="#EssenceModel-203"><span class="linenos">203</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-204"><a href="#EssenceModel-204"><span class="linenos">204</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_raise_on_uninjectable_model</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-205"><a href="#EssenceModel-205"><span class="linenos">205</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel-206"><a href="#EssenceModel-206"><span class="linenos">206</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-207"><a href="#EssenceModel-207"><span class="linenos">207</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_raise_on_incompatible_high_order_model</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-208"><a href="#EssenceModel-208"><span class="linenos">208</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">:</span> <span class="n">Dict</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-209"><a href="#EssenceModel-209"><span class="linenos">209</span></a>
</span><span id="EssenceModel-210"><a href="#EssenceModel-210"><span class="linenos">210</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="EssenceModel-211"><a href="#EssenceModel-211"><span class="linenos">211</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Should be called in order to get needed model interface&quot;&quot;&quot;</span>
</span><span id="EssenceModel-212"><a href="#EssenceModel-212"><span class="linenos">212</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel-213"><a href="#EssenceModel-213"><span class="linenos">213</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel-214"><a href="#EssenceModel-214"><span class="linenos">214</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-215"><a href="#EssenceModel-215"><span class="linenos">215</span></a>            <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel-216"><a href="#EssenceModel-216"><span class="linenos">216</span></a>            <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-217"><a href="#EssenceModel-217"><span class="linenos">217</span></a>                <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel-218"><a href="#EssenceModel-218"><span class="linenos">218</span></a>                <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel-219"><a href="#EssenceModel-219"><span class="linenos">219</span></a>                    <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span>
</span><span id="EssenceModel-220"><a href="#EssenceModel-220"><span class="linenos">220</span></a>                    <span class="k">break</span>
</span><span id="EssenceModel-221"><a href="#EssenceModel-221"><span class="linenos">221</span></a>            <span class="k">if</span> <span class="n">injected_model_interface</span><span class="p">:</span>
</span><span id="EssenceModel-222"><a href="#EssenceModel-222"><span class="linenos">222</span></a>                <span class="k">return</span> <span class="n">injected_model_interface</span>
</span><span id="EssenceModel-223"><a href="#EssenceModel-223"><span class="linenos">223</span></a>            <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel-224"><a href="#EssenceModel-224"><span class="linenos">224</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotApplicableError</span>
</span><span id="EssenceModel-225"><a href="#EssenceModel-225"><span class="linenos">225</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-226"><a href="#EssenceModel-226"><span class="linenos">226</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotRegisteredError</span>
</span><span id="EssenceModel-227"><a href="#EssenceModel-227"><span class="linenos">227</span></a>
</span><span id="EssenceModel-228"><a href="#EssenceModel-228"><span class="linenos">228</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="n">worker</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">failed_worker</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="EssenceModel-229"><a href="#EssenceModel-229"><span class="linenos">229</span></a>        <span class="n">interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel-230"><a href="#EssenceModel-230"><span class="linenos">230</span></a>        <span class="n">exception</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel-231"><a href="#EssenceModel-231"><span class="linenos">231</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="EssenceModel-232"><a href="#EssenceModel-232"><span class="linenos">232</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">em_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span>
</span><span id="EssenceModel-233"><a href="#EssenceModel-233"><span class="linenos">233</span></a>        <span class="k">except</span> <span class="p">(</span><span class="n">EssenceInterfaceIsNotApplicableError</span><span class="p">,</span> <span class="n">EssenceInterfaceIsNotRegisteredError</span><span class="p">)</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>
</span><span id="EssenceModel-234"><a href="#EssenceModel-234"><span class="linenos">234</span></a>            <span class="n">exception</span> <span class="o">=</span> <span class="n">get_exception</span><span class="p">()</span>
</span><span id="EssenceModel-235"><a href="#EssenceModel-235"><span class="linenos">235</span></a>        
</span><span id="EssenceModel-236"><a href="#EssenceModel-236"><span class="linenos">236</span></a>        <span class="k">if</span> <span class="n">interface</span><span class="p">:</span>
</span><span id="EssenceModel-237"><a href="#EssenceModel-237"><span class="linenos">237</span></a>            <span class="k">return</span> <span class="n">worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-238"><a href="#EssenceModel-238"><span class="linenos">238</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-239"><a href="#EssenceModel-239"><span class="linenos">239</span></a>            <span class="k">if</span> <span class="n">failed_worker</span><span class="p">:</span>
</span><span id="EssenceModel-240"><a href="#EssenceModel-240"><span class="linenos">240</span></a>                <span class="k">return</span> <span class="n">failed_worker</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">exception</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-241"><a href="#EssenceModel-241"><span class="linenos">241</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-242"><a href="#EssenceModel-242"><span class="linenos">242</span></a>                <span class="k">return</span> <span class="kc">None</span>
</span><span id="EssenceModel-243"><a href="#EssenceModel-243"><span class="linenos">243</span></a>    
</span><span id="EssenceModel-244"><a href="#EssenceModel-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel-245"><a href="#EssenceModel-245"><span class="linenos">245</span></a>        <span class="n">has_own_interface</span> <span class="o">=</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> \
</span><span id="EssenceModel-246"><a href="#EssenceModel-246"><span class="linenos">246</span></a>                            <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel-247"><a href="#EssenceModel-247"><span class="linenos">247</span></a>        <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-248"><a href="#EssenceModel-248"><span class="linenos">248</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-249"><a href="#EssenceModel-249"><span class="linenos">249</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel-250"><a href="#EssenceModel-250"><span class="linenos">250</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_has_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span> <span class="ow">or</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel-251"><a href="#EssenceModel-251"><span class="linenos">251</span></a>                <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-252"><a href="#EssenceModel-252"><span class="linenos">252</span></a>                <span class="k">break</span>
</span><span id="EssenceModel-253"><a href="#EssenceModel-253"><span class="linenos">253</span></a>        <span class="k">return</span> <span class="n">has_own_interface</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_interface</span>
</span><span id="EssenceModel-254"><a href="#EssenceModel-254"><span class="linenos">254</span></a>
</span><span id="EssenceModel-255"><a href="#EssenceModel-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel-256"><a href="#EssenceModel-256"><span class="linenos">256</span></a>        <span class="n">own_interface_active</span> <span class="o">=</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span>
</span><span id="EssenceModel-257"><a href="#EssenceModel-257"><span class="linenos">257</span></a>        <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-258"><a href="#EssenceModel-258"><span class="linenos">258</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-259"><a href="#EssenceModel-259"><span class="linenos">259</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel-260"><a href="#EssenceModel-260"><span class="linenos">260</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel-261"><a href="#EssenceModel-261"><span class="linenos">261</span></a>                <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-262"><a href="#EssenceModel-262"><span class="linenos">262</span></a>                <span class="k">break</span>
</span><span id="EssenceModel-263"><a href="#EssenceModel-263"><span class="linenos">263</span></a>        <span class="k">return</span> <span class="n">own_interface_active</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_active_interface</span>
</span><span id="EssenceModel-264"><a href="#EssenceModel-264"><span class="linenos">264</span></a>
</span><span id="EssenceModel-265"><a href="#EssenceModel-265"><span class="linenos">265</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModel-266"><a href="#EssenceModel-266"><span class="linenos">266</span></a>        <span class="n">own_active_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel-267"><a href="#EssenceModel-267"><span class="linenos">267</span></a>        <span class="n">injected_models_active_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel-268"><a href="#EssenceModel-268"><span class="linenos">268</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-269"><a href="#EssenceModel-269"><span class="linenos">269</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel-270"><a href="#EssenceModel-270"><span class="linenos">270</span></a>            <span class="n">injected_models_active_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_active_interfaces</span><span class="p">())</span>
</span><span id="EssenceModel-271"><a href="#EssenceModel-271"><span class="linenos">271</span></a>        <span class="k">return</span> <span class="n">own_active_interfaces</span> <span class="o">|</span> <span class="n">injected_models_active_interfaces</span>
</span><span id="EssenceModel-272"><a href="#EssenceModel-272"><span class="linenos">272</span></a>
</span><span id="EssenceModel-273"><a href="#EssenceModel-273"><span class="linenos">273</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModel-274"><a href="#EssenceModel-274"><span class="linenos">274</span></a>        <span class="n">own_all_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel-275"><a href="#EssenceModel-275"><span class="linenos">275</span></a>        <span class="n">injected_models_all_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel-276"><a href="#EssenceModel-276"><span class="linenos">276</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-277"><a href="#EssenceModel-277"><span class="linenos">277</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel-278"><a href="#EssenceModel-278"><span class="linenos">278</span></a>            <span class="n">injected_models_all_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_all_interfaces</span><span class="p">())</span>
</span><span id="EssenceModel-279"><a href="#EssenceModel-279"><span class="linenos">279</span></a>        <span class="k">return</span> <span class="n">own_all_interfaces</span> <span class="o">|</span> <span class="n">injected_models_all_interfaces</span>
</span><span id="EssenceModel-280"><a href="#EssenceModel-280"><span class="linenos">280</span></a>
</span><span id="EssenceModel-281"><a href="#EssenceModel-281"><span class="linenos">281</span></a>    <span class="k">def</span> <span class="nf">_em_check_applicability_of_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="EssenceModel-282"><a href="#EssenceModel-282"><span class="linenos">282</span></a>        <span class="n">new_interfaces</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-283"><a href="#EssenceModel-283"><span class="linenos">283</span></a>        <span class="n">new_possible_interfaces</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
</span><span id="EssenceModel-284"><a href="#EssenceModel-284"><span class="linenos">284</span></a>
</span><span id="EssenceModel-285"><a href="#EssenceModel-285"><span class="linenos">285</span></a>        <span class="k">for</span> <span class="n">interface_class</span><span class="p">,</span> <span class="n">interface</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-286"><a href="#EssenceModel-286"><span class="linenos">286</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="EssenceModel-287"><a href="#EssenceModel-287"><span class="linenos">287</span></a>                <span class="n">new_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-288"><a href="#EssenceModel-288"><span class="linenos">288</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-289"><a href="#EssenceModel-289"><span class="linenos">289</span></a>                <span class="n">new_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-290"><a href="#EssenceModel-290"><span class="linenos">290</span></a>
</span><span id="EssenceModel-291"><a href="#EssenceModel-291"><span class="linenos">291</span></a>        <span class="k">for</span> <span class="n">interface_class</span><span class="p">,</span> <span class="n">interface</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel-292"><a href="#EssenceModel-292"><span class="linenos">292</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="EssenceModel-293"><a href="#EssenceModel-293"><span class="linenos">293</span></a>                <span class="n">new_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-294"><a href="#EssenceModel-294"><span class="linenos">294</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-295"><a href="#EssenceModel-295"><span class="linenos">295</span></a>                <span class="n">new_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-296"><a href="#EssenceModel-296"><span class="linenos">296</span></a>
</span><span id="EssenceModel-297"><a href="#EssenceModel-297"><span class="linenos">297</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span> <span class="o">=</span> <span class="n">new_interfaces</span>
</span><span id="EssenceModel-298"><a href="#EssenceModel-298"><span class="linenos">298</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span> <span class="o">=</span> <span class="n">new_possible_interfaces</span>
</span><span id="EssenceModel-299"><a href="#EssenceModel-299"><span class="linenos">299</span></a>
</span><span id="EssenceModel-300"><a href="#EssenceModel-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel-301"><a href="#EssenceModel-301"><span class="linenos">301</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Must be run by EssenceInterface (by running EssenceInterface.notify_model_about_change method) after changing</span>
</span><span id="EssenceModel-302"><a href="#EssenceModel-302"><span class="linenos">302</span></a><span class="sd">          model&#39;s data. It is enough to run in once per a method - at the end of the method work.</span>
</span><span id="EssenceModel-303"><a href="#EssenceModel-303"><span class="linenos">303</span></a><span class="sd">        In &#39;super&#39; in method of inherit class should be run at the end of the method&quot;&quot;&quot;</span>
</span><span id="EssenceModel-304"><a href="#EssenceModel-304"><span class="linenos">304</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="EssenceModel-305"><a href="#EssenceModel-305"><span class="linenos">305</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="EssenceModel-306"><a href="#EssenceModel-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">interface_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-307"><a href="#EssenceModel-307"><span class="linenos">307</span></a>
</span><span id="EssenceModel-308"><a href="#EssenceModel-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel-309"><a href="#EssenceModel-309"><span class="linenos">309</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">):</span>
</span><span id="EssenceModel-310"><a href="#EssenceModel-310"><span class="linenos">310</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="EssenceModel-311"><a href="#EssenceModel-311"><span class="linenos">311</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-312"><a href="#EssenceModel-312"><span class="linenos">312</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="n">interface_class</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-313"><a href="#EssenceModel-313"><span class="linenos">313</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="EssenceModel-314"><a href="#EssenceModel-314"><span class="linenos">314</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-315"><a href="#EssenceModel-315"><span class="linenos">315</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-316"><a href="#EssenceModel-316"><span class="linenos">316</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel-317"><a href="#EssenceModel-317"><span class="linenos">317</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceModel-318"><a href="#EssenceModel-318"><span class="linenos">318</span></a>
</span><span id="EssenceModel-319"><a href="#EssenceModel-319"><span class="linenos">319</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel-320"><a href="#EssenceModel-320"><span class="linenos">320</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel-321"><a href="#EssenceModel-321"><span class="linenos">321</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel-322"><a href="#EssenceModel-322"><span class="linenos">322</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceModel-323"><a href="#EssenceModel-323"><span class="linenos">323</span></a>        <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel-324"><a href="#EssenceModel-324"><span class="linenos">324</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel-325"><a href="#EssenceModel-325"><span class="linenos">325</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceModel-326"><a href="#EssenceModel-326"><span class="linenos">326</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-327"><a href="#EssenceModel-327"><span class="linenos">327</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="EssenceModel-328"><a href="#EssenceModel-328"><span class="linenos">328</span></a>
</span><span id="EssenceModel-329"><a href="#EssenceModel-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="EssenceModel-330"><a href="#EssenceModel-330"><span class="linenos">330</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Will be called after high order model successfully registered this mode&quot;&quot;&quot;</span>
</span><span id="EssenceModel-331"><a href="#EssenceModel-331"><span class="linenos">331</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="n">high_order_model</span>
</span><span id="EssenceModel-332"><a href="#EssenceModel-332"><span class="linenos">332</span></a>
</span><span id="EssenceModel-333"><a href="#EssenceModel-333"><span class="linenos">333</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-334"><a href="#EssenceModel-334"><span class="linenos">334</span></a>        <span class="c1"># Will be called before high order model actually unregistered this mode</span>
</span><span id="EssenceModel-335"><a href="#EssenceModel-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel-336"><a href="#EssenceModel-336"><span class="linenos">336</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-337"><a href="#EssenceModel-337"><span class="linenos">337</span></a>
</span><span id="EssenceModel-338"><a href="#EssenceModel-338"><span class="linenos">338</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="EssenceModel-339"><a href="#EssenceModel-339"><span class="linenos">339</span></a>        <span class="c1"># Should use &#39;EssenceModel&#39; instead of Type[&#39;EssenceModel&#39;] since we should use result of fully constructed</span>
</span><span id="EssenceModel-340"><a href="#EssenceModel-340"><span class="linenos">340</span></a>        <span class="c1">#   essence_model with all needed interfaces - result of an appropriate factory work</span>
</span><span id="EssenceModel-341"><a href="#EssenceModel-341"><span class="linenos">341</span></a>        <span class="n">essence_model_class</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">essence_model</span><span class="p">)</span>
</span><span id="EssenceModel-342"><a href="#EssenceModel-342"><span class="linenos">342</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">essence_model</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">):</span>
</span><span id="EssenceModel-343"><a href="#EssenceModel-343"><span class="linenos">343</span></a>            <span class="k">raise</span> <span class="n">EssenceModelCanNotInjectSelfError</span>
</span><span id="EssenceModel-344"><a href="#EssenceModel-344"><span class="linenos">344</span></a>        
</span><span id="EssenceModel-345"><a href="#EssenceModel-345"><span class="linenos">345</span></a>        <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-346"><a href="#EssenceModel-346"><span class="linenos">346</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="EssenceModel-347"><a href="#EssenceModel-347"><span class="linenos">347</span></a>            <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-348"><a href="#EssenceModel-348"><span class="linenos">348</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-349"><a href="#EssenceModel-349"><span class="linenos">349</span></a>            <span class="k">if</span> <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)):</span>
</span><span id="EssenceModel-350"><a href="#EssenceModel-350"><span class="linenos">350</span></a>                <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-351"><a href="#EssenceModel-351"><span class="linenos">351</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-352"><a href="#EssenceModel-352"><span class="linenos">352</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_raise_on_incompatible_high_order_model</span><span class="p">:</span>
</span><span id="EssenceModel-353"><a href="#EssenceModel-353"><span class="linenos">353</span></a>                    <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="EssenceModel-354"><a href="#EssenceModel-354"><span class="linenos">354</span></a>        
</span><span id="EssenceModel-355"><a href="#EssenceModel-355"><span class="linenos">355</span></a>        <span class="n">injected</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel-356"><a href="#EssenceModel-356"><span class="linenos">356</span></a>        <span class="k">if</span> <span class="n">injectable_model</span><span class="p">:</span>
</span><span id="EssenceModel-357"><a href="#EssenceModel-357"><span class="linenos">357</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceModel-358"><a href="#EssenceModel-358"><span class="linenos">358</span></a>            <span class="n">essence_model</span><span class="o">.</span><span class="n">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="EssenceModel-359"><a href="#EssenceModel-359"><span class="linenos">359</span></a>            <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="EssenceModel-360"><a href="#EssenceModel-360"><span class="linenos">360</span></a>                <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_behave_as_unknown_model</span><span class="p">()</span>
</span><span id="EssenceModel-361"><a href="#EssenceModel-361"><span class="linenos">361</span></a>            
</span><span id="EssenceModel-362"><a href="#EssenceModel-362"><span class="linenos">362</span></a>            <span class="n">injected</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-363"><a href="#EssenceModel-363"><span class="linenos">363</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-364"><a href="#EssenceModel-364"><span class="linenos">364</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_raise_on_uninjectable_model</span><span class="p">:</span>
</span><span id="EssenceModel-365"><a href="#EssenceModel-365"><span class="linenos">365</span></a>                <span class="k">raise</span> <span class="n">EssenceModelCanNotBeInjectedError</span>
</span><span id="EssenceModel-366"><a href="#EssenceModel-366"><span class="linenos">366</span></a>            
</span><span id="EssenceModel-367"><a href="#EssenceModel-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="n">injected</span>
</span><span id="EssenceModel-368"><a href="#EssenceModel-368"><span class="linenos">368</span></a>
</span><span id="EssenceModel-369"><a href="#EssenceModel-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-370"><a href="#EssenceModel-370"><span class="linenos">370</span></a>        <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">)</span>
</span><span id="EssenceModel-371"><a href="#EssenceModel-371"><span class="linenos">371</span></a>
</span><span id="EssenceModel-372"><a href="#EssenceModel-372"><span class="linenos">372</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="EssenceModel-373"><a href="#EssenceModel-373"><span class="linenos">373</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">:</span>
</span><span id="EssenceModel-374"><a href="#EssenceModel-374"><span class="linenos">374</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="EssenceModel-375"><a href="#EssenceModel-375"><span class="linenos">375</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel-376"><a href="#EssenceModel-376"><span class="linenos">376</span></a>            <span class="k">raise</span> <span class="n">EssenceModelIsNotInjectedError</span>
</span><span id="EssenceModel-377"><a href="#EssenceModel-377"><span class="linenos">377</span></a>
</span><span id="EssenceModel-378"><a href="#EssenceModel-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel-379"><a href="#EssenceModel-379"><span class="linenos">379</span></a>        <span class="c1"># In &#39;super&#39; in method of inherit class should be run at the end of the method</span>
</span><span id="EssenceModel-380"><a href="#EssenceModel-380"><span class="linenos">380</span></a>        <span class="c1"># With deep injection it will be like (model_3, model_2, model_1, interface_1, arg_1, arg_2, arg_3)</span>
</span><span id="EssenceModel-381"><a href="#EssenceModel-381"><span class="linenos">381</span></a>        <span class="c1">#   where `interface_1` is an interface of the `model_1`</span>
</span><span id="EssenceModel-382"><a href="#EssenceModel-382"><span class="linenos">382</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="EssenceModel-383"><a href="#EssenceModel-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="EssenceModel-384"><a href="#EssenceModel-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">essence_model_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-385"><a href="#EssenceModel-385"><span class="linenos">385</span></a>
</span><span id="EssenceModel-386"><a href="#EssenceModel-386"><span class="linenos">386</span></a>    <span class="k">def</span> <span class="nf">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel-387"><a href="#EssenceModel-387"><span class="linenos">387</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span><span class="p">):</span>
</span><span id="EssenceModel-388"><a href="#EssenceModel-388"><span class="linenos">388</span></a>            <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span>
</span><span id="EssenceModel-389"><a href="#EssenceModel-389"><span class="linenos">389</span></a>            <span class="n">high_order_model</span><span class="o">.</span><span class="n">emi_on_injected_model_updated</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel-390"><a href="#EssenceModel-390"><span class="linenos">390</span></a>
</span><span id="EssenceModel-391"><a href="#EssenceModel-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="EssenceModel-392"><a href="#EssenceModel-392"><span class="linenos">392</span></a>        <span class="n">injected_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="EssenceModel-393"><a href="#EssenceModel-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="n">injected_model</span><span class="p">)</span>
</span><span id="EssenceModel-394"><a href="#EssenceModel-394"><span class="linenos">394</span></a>        <span class="n">injected_model</span><span class="o">.</span><span class="n">emi_on_unregistering_from_high_order_model</span><span class="p">()</span>
</span><span id="EssenceModel-395"><a href="#EssenceModel-395"><span class="linenos">395</span></a>        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="EssenceModel-396"><a href="#EssenceModel-396"><span class="linenos">396</span></a>
</span><span id="EssenceModel-397"><a href="#EssenceModel-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel-398"><a href="#EssenceModel-398"><span class="linenos">398</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in order to make this model compatible with more than one high order models</span>
</span><span id="EssenceModel-399"><a href="#EssenceModel-399"><span class="linenos">399</span></a>
</span><span id="EssenceModel-400"><a href="#EssenceModel-400"><span class="linenos">400</span></a><span class="sd">        Args:</span>
</span><span id="EssenceModel-401"><a href="#EssenceModel-401"><span class="linenos">401</span></a><span class="sd">            high_order_model_class (Type[): [description]</span>
</span><span id="EssenceModel-402"><a href="#EssenceModel-402"><span class="linenos">402</span></a>
</span><span id="EssenceModel-403"><a href="#EssenceModel-403"><span class="linenos">403</span></a><span class="sd">        Returns:</span>
</span><span id="EssenceModel-404"><a href="#EssenceModel-404"><span class="linenos">404</span></a><span class="sd">            bool: [description]</span>
</span><span id="EssenceModel-405"><a href="#EssenceModel-405"><span class="linenos">405</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="EssenceModel-406"><a href="#EssenceModel-406"><span class="linenos">406</span></a>        <span class="c1"># return high_order_model_class == self.emu_compatible_high_order_essence_model_class</span>
</span><span id="EssenceModel-407"><a href="#EssenceModel-407"><span class="linenos">407</span></a>        <span class="k">return</span> <span class="n">high_order_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_compatible_high_order_essence_model_classes</span>
</span><span id="EssenceModel-408"><a href="#EssenceModel-408"><span class="linenos">408</span></a>
</span><span id="EssenceModel-409"><a href="#EssenceModel-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-410"><a href="#EssenceModel-410"><span class="linenos">410</span></a>        <span class="c1"># Should be called by a high order model for an unknown injected model</span>
</span><span id="EssenceModel-411"><a href="#EssenceModel-411"><span class="linenos">411</span></a>        <span class="c1"># if type(self.__emi_high_order_model) != self.emu_compatible_high_order_essence_model_class:</span>
</span><span id="EssenceModel-412"><a href="#EssenceModel-412"><span class="linenos">412</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="p">):</span>
</span><span id="EssenceModel-413"><a href="#EssenceModel-413"><span class="linenos">413</span></a>            <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="EssenceModel-414"><a href="#EssenceModel-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="o">.</span><span class="n">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="EssenceModel-415"><a href="#EssenceModel-415"><span class="linenos">415</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel-416"><a href="#EssenceModel-416"><span class="linenos">416</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">emu_on_behave_as_unknown_model</span><span class="p">()</span>
</span><span id="EssenceModel-417"><a href="#EssenceModel-417"><span class="linenos">417</span></a>
</span><span id="EssenceModel-418"><a href="#EssenceModel-418"><span class="linenos">418</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-419"><a href="#EssenceModel-419"><span class="linenos">419</span></a>        <span class="k">pass</span>
</span><span id="EssenceModel-420"><a href="#EssenceModel-420"><span class="linenos">420</span></a>
</span><span id="EssenceModel-421"><a href="#EssenceModel-421"><span class="linenos">421</span></a>    <span class="k">def</span> <span class="nf">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModel-422"><a href="#EssenceModel-422"><span class="linenos">422</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n">requester</span><span class="p">]]</span> <span class="o">=</span> <span class="n">requester</span>
</span><span id="EssenceModel-423"><a href="#EssenceModel-423"><span class="linenos">423</span></a>
</span><span id="EssenceModel-424"><a href="#EssenceModel-424"><span class="linenos">424</span></a>    <span class="k">def</span> <span class="nf">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">requester</span><span class="p">:</span> <span class="s1">&#39;EssenceModelUnknownInjectionAbstract&#39;</span><span class="p">):</span>
</span><span id="EssenceModel-425"><a href="#EssenceModel-425"><span class="linenos">425</span></a>        <span class="n">model_type</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">requester</span><span class="p">)</span>
</span><span id="EssenceModel-426"><a href="#EssenceModel-426"><span class="linenos">426</span></a>        <span class="k">if</span> <span class="n">model_type</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">:</span>
</span><span id="EssenceModel-427"><a href="#EssenceModel-427"><span class="linenos">427</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="p">[</span><span class="n">model_type</span><span class="p">]</span>
</span><span id="EssenceModel-428"><a href="#EssenceModel-428"><span class="linenos">428</span></a>
</span><span id="EssenceModel-429"><a href="#EssenceModel-429"><span class="linenos">429</span></a>    <span class="k">def</span> <span class="nf">_emu_notify_unknown_models_about_self_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel-430"><a href="#EssenceModel-430"><span class="linenos">430</span></a>        <span class="k">for</span> <span class="n">umodel</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_unknown_injected_models</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
</span><span id="EssenceModel-431"><a href="#EssenceModel-431"><span class="linenos">431</span></a>            <span class="n">unknown_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">umodel</span>
</span><span id="EssenceModel-432"><a href="#EssenceModel-432"><span class="linenos">432</span></a>            <span class="n">unknown_model</span><span class="o">.</span><span class="n">emu_on_model_changed_callback</span><span class="p">()</span>
</span><span id="EssenceModel-433"><a href="#EssenceModel-433"><span class="linenos">433</span></a>
</span><span id="EssenceModel-434"><a href="#EssenceModel-434"><span class="linenos">434</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-435"><a href="#EssenceModel-435"><span class="linenos">435</span></a>        <span class="k">raise</span> <span class="n">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span>
</span><span id="EssenceModel-436"><a href="#EssenceModel-436"><span class="linenos">436</span></a>
</span><span id="EssenceModel-437"><a href="#EssenceModel-437"><span class="linenos">437</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel-438"><a href="#EssenceModel-438"><span class="linenos">438</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span>
</span></pre></div>


            <div class="docstring"><p>Must contain related data in a consistent state.</p>

<p>In order to do this, you must reload <code><a href="#EssenceModel.em_on_model_updated">em_on_model_updated()</a></code> and <code><a href="#EssenceModel.emi_on_injected_model_updated">emi_on_injected_model_updated()</a></code> methods.
Your interfaces can provide some appropriate information though an additional <code>parameters of em_on_model_updated()</code>
and <code><a href="#EssenceModel.emi_on_injected_model_updated">emi_on_injected_model_updated()</a></code> methods.</p>

<p>Do not forget to:</p>

<ul>
<li>run <code>self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)</code> at
the end of your <code><a href="#EssenceModel.em_on_model_updated">em_on_model_updated()</a></code></li>
<li>run <code>self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)</code> at
the end of your <code><a href="#EssenceModel.emi_on_injected_model_updated">emi_on_injected_model_updated()</a></code></li>
</ul>
</div>


                            <div id="EssenceModel.emi_compatible_injectable_essence_model_classes" class="classattr">
                                <div class="attr variable">
            <span class="name">emi_compatible_injectable_essence_model_classes</span><span class="annotation">: set[type[<a href="#EssenceModel">EssenceModel</a>]]</span>        =
<span class="default_value">set()</span>

        
    </div>
    <a class="headerlink" href="#EssenceModel.emi_compatible_injectable_essence_model_classes"></a>
    
    

                            </div>
                            <div id="EssenceModel.emu_compatible_high_order_essence_model_classes" class="classattr">
                                <div class="attr variable">
            <span class="name">emu_compatible_high_order_essence_model_classes</span><span class="annotation">: set[type[<a href="#EssenceModel">EssenceModel</a>]]</span>        =
<span class="default_value">set()</span>

        
    </div>
    <a class="headerlink" href="#EssenceModel.emu_compatible_high_order_essence_model_classes"></a>
    
    

                            </div>
                            <div id="EssenceModel.em_interface" class="classattr">
                                        <input id="EssenceModel.em_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n"><a href="#EssenceInterface">EssenceInterface</a></span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_interface-210"><a href="#EssenceModel.em_interface-210"><span class="linenos">210</span></a>    <span class="k">def</span> <span class="nf">em_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="s1">&#39;EssenceInterface&#39;</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-211"><a href="#EssenceModel.em_interface-211"><span class="linenos">211</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Should be called in order to get needed model interface&quot;&quot;&quot;</span>
</span><span id="EssenceModel.em_interface-212"><a href="#EssenceModel.em_interface-212"><span class="linenos">212</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-213"><a href="#EssenceModel.em_interface-213"><span class="linenos">213</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel.em_interface-214"><a href="#EssenceModel.em_interface-214"><span class="linenos">214</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-215"><a href="#EssenceModel.em_interface-215"><span class="linenos">215</span></a>            <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel.em_interface-216"><a href="#EssenceModel.em_interface-216"><span class="linenos">216</span></a>            <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel.em_interface-217"><a href="#EssenceModel.em_interface-217"><span class="linenos">217</span></a>                <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel.em_interface-218"><a href="#EssenceModel.em_interface-218"><span class="linenos">218</span></a>                <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel.em_interface-219"><a href="#EssenceModel.em_interface-219"><span class="linenos">219</span></a>                    <span class="n">injected_model_interface</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span>
</span><span id="EssenceModel.em_interface-220"><a href="#EssenceModel.em_interface-220"><span class="linenos">220</span></a>                    <span class="k">break</span>
</span><span id="EssenceModel.em_interface-221"><a href="#EssenceModel.em_interface-221"><span class="linenos">221</span></a>            <span class="k">if</span> <span class="n">injected_model_interface</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-222"><a href="#EssenceModel.em_interface-222"><span class="linenos">222</span></a>                <span class="k">return</span> <span class="n">injected_model_interface</span>
</span><span id="EssenceModel.em_interface-223"><a href="#EssenceModel.em_interface-223"><span class="linenos">223</span></a>            <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-224"><a href="#EssenceModel.em_interface-224"><span class="linenos">224</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotApplicableError</span>
</span><span id="EssenceModel.em_interface-225"><a href="#EssenceModel.em_interface-225"><span class="linenos">225</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface-226"><a href="#EssenceModel.em_interface-226"><span class="linenos">226</span></a>                <span class="k">raise</span> <span class="n">EssenceInterfaceIsNotRegisteredError</span>
</span></pre></div>


            <div class="docstring"><p>Should be called in order to get needed model interface</p>
</div>


                            </div>
                            <div id="EssenceModel.em_has_interface" class="classattr">
                                        <input id="EssenceModel.em_has_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_has_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_has_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_has_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_has_interface-244"><a href="#EssenceModel.em_has_interface-244"><span class="linenos">244</span></a>    <span class="k">def</span> <span class="nf">em_has_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel.em_has_interface-245"><a href="#EssenceModel.em_has_interface-245"><span class="linenos">245</span></a>        <span class="n">has_own_interface</span> <span class="o">=</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> \
</span><span id="EssenceModel.em_has_interface-246"><a href="#EssenceModel.em_has_interface-246"><span class="linenos">246</span></a>                            <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel.em_has_interface-247"><a href="#EssenceModel.em_has_interface-247"><span class="linenos">247</span></a>        <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel.em_has_interface-248"><a href="#EssenceModel.em_has_interface-248"><span class="linenos">248</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel.em_has_interface-249"><a href="#EssenceModel.em_has_interface-249"><span class="linenos">249</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel.em_has_interface-250"><a href="#EssenceModel.em_has_interface-250"><span class="linenos">250</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_has_interface</span><span class="p">(</span><span class="n">interface_class</span><span class="p">)</span> <span class="ow">or</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel.em_has_interface-251"><a href="#EssenceModel.em_has_interface-251"><span class="linenos">251</span></a>                <span class="n">one_of_injected_models_has_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.em_has_interface-252"><a href="#EssenceModel.em_has_interface-252"><span class="linenos">252</span></a>                <span class="k">break</span>
</span><span id="EssenceModel.em_has_interface-253"><a href="#EssenceModel.em_has_interface-253"><span class="linenos">253</span></a>        <span class="k">return</span> <span class="n">has_own_interface</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_interface</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.em_interface_active" class="classattr">
                                        <input id="EssenceModel.em_interface_active-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_interface_active</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_interface_active-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_interface_active"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_interface_active-255"><a href="#EssenceModel.em_interface_active-255"><span class="linenos">255</span></a>    <span class="k">def</span> <span class="nf">em_interface_active</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel.em_interface_active-256"><a href="#EssenceModel.em_interface_active-256"><span class="linenos">256</span></a>        <span class="n">own_interface_active</span> <span class="o">=</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span>
</span><span id="EssenceModel.em_interface_active-257"><a href="#EssenceModel.em_interface_active-257"><span class="linenos">257</span></a>        <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel.em_interface_active-258"><a href="#EssenceModel.em_interface_active-258"><span class="linenos">258</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel.em_interface_active-259"><a href="#EssenceModel.em_interface_active-259"><span class="linenos">259</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel.em_interface_active-260"><a href="#EssenceModel.em_interface_active-260"><span class="linenos">260</span></a>            <span class="k">if</span> <span class="n">model</span><span class="o">.</span><span class="n">em_interface_active</span><span class="p">(</span><span class="n">interface_class</span><span class="p">):</span>
</span><span id="EssenceModel.em_interface_active-261"><a href="#EssenceModel.em_interface_active-261"><span class="linenos">261</span></a>                <span class="n">one_of_injected_models_has_active_interface</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.em_interface_active-262"><a href="#EssenceModel.em_interface_active-262"><span class="linenos">262</span></a>                <span class="k">break</span>
</span><span id="EssenceModel.em_interface_active-263"><a href="#EssenceModel.em_interface_active-263"><span class="linenos">263</span></a>        <span class="k">return</span> <span class="n">own_interface_active</span> <span class="ow">or</span> <span class="n">one_of_injected_models_has_active_interface</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.em_active_interfaces" class="classattr">
                                        <input id="EssenceModel.em_active_interfaces-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_active_interfaces</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">set</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_active_interfaces-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_active_interfaces"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_active_interfaces-265"><a href="#EssenceModel.em_active_interfaces-265"><span class="linenos">265</span></a>    <span class="k">def</span> <span class="nf">em_active_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModel.em_active_interfaces-266"><a href="#EssenceModel.em_active_interfaces-266"><span class="linenos">266</span></a>        <span class="n">own_active_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel.em_active_interfaces-267"><a href="#EssenceModel.em_active_interfaces-267"><span class="linenos">267</span></a>        <span class="n">injected_models_active_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel.em_active_interfaces-268"><a href="#EssenceModel.em_active_interfaces-268"><span class="linenos">268</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel.em_active_interfaces-269"><a href="#EssenceModel.em_active_interfaces-269"><span class="linenos">269</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel.em_active_interfaces-270"><a href="#EssenceModel.em_active_interfaces-270"><span class="linenos">270</span></a>            <span class="n">injected_models_active_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_active_interfaces</span><span class="p">())</span>
</span><span id="EssenceModel.em_active_interfaces-271"><a href="#EssenceModel.em_active_interfaces-271"><span class="linenos">271</span></a>        <span class="k">return</span> <span class="n">own_active_interfaces</span> <span class="o">|</span> <span class="n">injected_models_active_interfaces</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.em_all_interfaces" class="classattr">
                                        <input id="EssenceModel.em_all_interfaces-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_all_interfaces</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">set</span><span class="p">[</span><span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]]</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_all_interfaces-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_all_interfaces"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_all_interfaces-273"><a href="#EssenceModel.em_all_interfaces-273"><span class="linenos">273</span></a>    <span class="k">def</span> <span class="nf">em_all_interfaces</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]:</span>
</span><span id="EssenceModel.em_all_interfaces-274"><a href="#EssenceModel.em_all_interfaces-274"><span class="linenos">274</span></a>        <span class="n">own_all_interfaces</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="o">|</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">)</span>
</span><span id="EssenceModel.em_all_interfaces-275"><a href="#EssenceModel.em_all_interfaces-275"><span class="linenos">275</span></a>        <span class="n">injected_models_all_interfaces</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">]]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceModel.em_all_interfaces-276"><a href="#EssenceModel.em_all_interfaces-276"><span class="linenos">276</span></a>        <span class="k">for</span> <span class="n">injected_model_class</span><span class="p">,</span> <span class="n">injected_model</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
</span><span id="EssenceModel.em_all_interfaces-277"><a href="#EssenceModel.em_all_interfaces-277"><span class="linenos">277</span></a>            <span class="n">model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="n">injected_model</span>
</span><span id="EssenceModel.em_all_interfaces-278"><a href="#EssenceModel.em_all_interfaces-278"><span class="linenos">278</span></a>            <span class="n">injected_models_all_interfaces</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">em_all_interfaces</span><span class="p">())</span>
</span><span id="EssenceModel.em_all_interfaces-279"><a href="#EssenceModel.em_all_interfaces-279"><span class="linenos">279</span></a>        <span class="k">return</span> <span class="n">own_all_interfaces</span> <span class="o">|</span> <span class="n">injected_models_all_interfaces</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.em_on_model_updated" class="classattr">
                                        <input id="EssenceModel.em_on_model_updated-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_on_model_updated</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.em_on_model_updated-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_on_model_updated"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_on_model_updated-300"><a href="#EssenceModel.em_on_model_updated-300"><span class="linenos">300</span></a>    <span class="k">def</span> <span class="nf">em_on_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel.em_on_model_updated-301"><a href="#EssenceModel.em_on_model_updated-301"><span class="linenos">301</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Must be run by EssenceInterface (by running EssenceInterface.notify_model_about_change method) after changing</span>
</span><span id="EssenceModel.em_on_model_updated-302"><a href="#EssenceModel.em_on_model_updated-302"><span class="linenos">302</span></a><span class="sd">          model&#39;s data. It is enough to run in once per a method - at the end of the method work.</span>
</span><span id="EssenceModel.em_on_model_updated-303"><a href="#EssenceModel.em_on_model_updated-303"><span class="linenos">303</span></a><span class="sd">        In &#39;super&#39; in method of inherit class should be run at the end of the method&quot;&quot;&quot;</span>
</span><span id="EssenceModel.em_on_model_updated-304"><a href="#EssenceModel.em_on_model_updated-304"><span class="linenos">304</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="EssenceModel.em_on_model_updated-305"><a href="#EssenceModel.em_on_model_updated-305"><span class="linenos">305</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="EssenceModel.em_on_model_updated-306"><a href="#EssenceModel.em_on_model_updated-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">interface_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Must be run by EssenceInterface (by running <a href="#EssenceInterface.notify_model_about_change">EssenceInterface.notify_model_about_change</a> method) after changing
  model's data. It is enough to run in once per a method - at the end of the method work.
In 'super' in method of inherit class should be run at the end of the method</p>
</div>


                            </div>
                            <div id="EssenceModel.em_add_interface" class="classattr">
                                        <input id="EssenceModel.em_add_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_add_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_add_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_add_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_add_interface-308"><a href="#EssenceModel.em_add_interface-308"><span class="linenos">308</span></a>    <span class="k">def</span> <span class="nf">em_add_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel.em_add_interface-309"><a href="#EssenceModel.em_add_interface-309"><span class="linenos">309</span></a>        <span class="k">if</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">):</span>
</span><span id="EssenceModel.em_add_interface-310"><a href="#EssenceModel.em_add_interface-310"><span class="linenos">310</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="EssenceModel.em_add_interface-311"><a href="#EssenceModel.em_add_interface-311"><span class="linenos">311</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.em_add_interface-312"><a href="#EssenceModel.em_add_interface-312"><span class="linenos">312</span></a>            <span class="n">interface</span> <span class="o">=</span> <span class="n">interface_class</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceModel.em_add_interface-313"><a href="#EssenceModel.em_add_interface-313"><span class="linenos">313</span></a>            <span class="k">if</span> <span class="n">interface</span><span class="o">.</span><span class="n">_applicable_impl</span><span class="p">():</span>
</span><span id="EssenceModel.em_add_interface-314"><a href="#EssenceModel.em_add_interface-314"><span class="linenos">314</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel.em_add_interface-315"><a href="#EssenceModel.em_add_interface-315"><span class="linenos">315</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.em_add_interface-316"><a href="#EssenceModel.em_add_interface-316"><span class="linenos">316</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="EssenceModel.em_add_interface-317"><a href="#EssenceModel.em_add_interface-317"><span class="linenos">317</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.em_remove_interface" class="classattr">
                                        <input id="EssenceModel.em_remove_interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_remove_interface</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">interface_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.em_remove_interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.em_remove_interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.em_remove_interface-319"><a href="#EssenceModel.em_remove_interface-319"><span class="linenos">319</span></a>    <span class="k">def</span> <span class="nf">em_remove_interface</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">interface_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceInterface&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel.em_remove_interface-320"><a href="#EssenceModel.em_remove_interface-320"><span class="linenos">320</span></a>        <span class="k">if</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel.em_remove_interface-321"><a href="#EssenceModel.em_remove_interface-321"><span class="linenos">321</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel.em_remove_interface-322"><a href="#EssenceModel.em_remove_interface-322"><span class="linenos">322</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceModel.em_remove_interface-323"><a href="#EssenceModel.em_remove_interface-323"><span class="linenos">323</span></a>        <span class="k">elif</span> <span class="n">interface_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">:</span>
</span><span id="EssenceModel.em_remove_interface-324"><a href="#EssenceModel.em_remove_interface-324"><span class="linenos">324</span></a>            <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__em_possible_interfaces</span><span class="p">[</span><span class="n">interface_class</span><span class="p">]</span>
</span><span id="EssenceModel.em_remove_interface-325"><a href="#EssenceModel.em_remove_interface-325"><span class="linenos">325</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceModel.em_remove_interface-326"><a href="#EssenceModel.em_remove_interface-326"><span class="linenos">326</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.em_remove_interface-327"><a href="#EssenceModel.em_remove_interface-327"><span class="linenos">327</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_on_registered_in_high_order_model" class="classattr">
                                        <input id="EssenceModel.emi_on_registered_in_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_registered_in_high_order_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">high_order_model</span><span class="p">:</span> <span class="n"><a href="#EssenceModel">EssenceModel</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_on_registered_in_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_on_registered_in_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_on_registered_in_high_order_model-329"><a href="#EssenceModel.emi_on_registered_in_high_order_model-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="EssenceModel.emi_on_registered_in_high_order_model-330"><a href="#EssenceModel.emi_on_registered_in_high_order_model-330"><span class="linenos">330</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Will be called after high order model successfully registered this mode&quot;&quot;&quot;</span>
</span><span id="EssenceModel.emi_on_registered_in_high_order_model-331"><a href="#EssenceModel.emi_on_registered_in_high_order_model-331"><span class="linenos">331</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="n">high_order_model</span>
</span></pre></div>


            <div class="docstring"><p>Will be called after high order model successfully registered this mode</p>
</div>


                            </div>
                            <div id="EssenceModel.emi_on_unregistering_from_high_order_model" class="classattr">
                                        <input id="EssenceModel.emi_on_unregistering_from_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_unregistering_from_high_order_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_on_unregistering_from_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_on_unregistering_from_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_on_unregistering_from_high_order_model-333"><a href="#EssenceModel.emi_on_unregistering_from_high_order_model-333"><span class="linenos">333</span></a>    <span class="k">def</span> <span class="nf">emi_on_unregistering_from_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emi_on_unregistering_from_high_order_model-334"><a href="#EssenceModel.emi_on_unregistering_from_high_order_model-334"><span class="linenos">334</span></a>        <span class="c1"># Will be called before high order model actually unregistered this mode</span>
</span><span id="EssenceModel.emi_on_unregistering_from_high_order_model-335"><a href="#EssenceModel.emi_on_unregistering_from_high_order_model-335"><span class="linenos">335</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceModel.emi_on_unregistering_from_high_order_model-336"><a href="#EssenceModel.emi_on_unregistering_from_high_order_model-336"><span class="linenos">336</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_inject_model" class="classattr">
                                        <input id="EssenceModel.emi_inject_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_inject_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model</span><span class="p">:</span> <span class="n"><a href="#EssenceModel">EssenceModel</a></span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_inject_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_inject_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_inject_model-338"><a href="#EssenceModel.emi_inject_model-338"><span class="linenos">338</span></a>    <span class="k">def</span> <span class="nf">emi_inject_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span><span class="p">):</span>
</span><span id="EssenceModel.emi_inject_model-339"><a href="#EssenceModel.emi_inject_model-339"><span class="linenos">339</span></a>        <span class="c1"># Should use &#39;EssenceModel&#39; instead of Type[&#39;EssenceModel&#39;] since we should use result of fully constructed</span>
</span><span id="EssenceModel.emi_inject_model-340"><a href="#EssenceModel.emi_inject_model-340"><span class="linenos">340</span></a>        <span class="c1">#   essence_model with all needed interfaces - result of an appropriate factory work</span>
</span><span id="EssenceModel.emi_inject_model-341"><a href="#EssenceModel.emi_inject_model-341"><span class="linenos">341</span></a>        <span class="n">essence_model_class</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">essence_model</span><span class="p">)</span>
</span><span id="EssenceModel.emi_inject_model-342"><a href="#EssenceModel.emi_inject_model-342"><span class="linenos">342</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">essence_model</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span> <span class="ow">or</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">):</span>
</span><span id="EssenceModel.emi_inject_model-343"><a href="#EssenceModel.emi_inject_model-343"><span class="linenos">343</span></a>            <span class="k">raise</span> <span class="n">EssenceModelCanNotInjectSelfError</span>
</span><span id="EssenceModel.emi_inject_model-344"><a href="#EssenceModel.emi_inject_model-344"><span class="linenos">344</span></a>        
</span><span id="EssenceModel.emi_inject_model-345"><a href="#EssenceModel.emi_inject_model-345"><span class="linenos">345</span></a>        <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel.emi_inject_model-346"><a href="#EssenceModel.emi_inject_model-346"><span class="linenos">346</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-347"><a href="#EssenceModel.emi_inject_model-347"><span class="linenos">347</span></a>            <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.emi_inject_model-348"><a href="#EssenceModel.emi_inject_model-348"><span class="linenos">348</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-349"><a href="#EssenceModel.emi_inject_model-349"><span class="linenos">349</span></a>            <span class="k">if</span> <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">)):</span>
</span><span id="EssenceModel.emi_inject_model-350"><a href="#EssenceModel.emi_inject_model-350"><span class="linenos">350</span></a>                <span class="n">injectable_model</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.emi_inject_model-351"><a href="#EssenceModel.emi_inject_model-351"><span class="linenos">351</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-352"><a href="#EssenceModel.emi_inject_model-352"><span class="linenos">352</span></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_raise_on_incompatible_high_order_model</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-353"><a href="#EssenceModel.emi_inject_model-353"><span class="linenos">353</span></a>                    <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="EssenceModel.emi_inject_model-354"><a href="#EssenceModel.emi_inject_model-354"><span class="linenos">354</span></a>        
</span><span id="EssenceModel.emi_inject_model-355"><a href="#EssenceModel.emi_inject_model-355"><span class="linenos">355</span></a>        <span class="n">injected</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="EssenceModel.emi_inject_model-356"><a href="#EssenceModel.emi_inject_model-356"><span class="linenos">356</span></a>        <span class="k">if</span> <span class="n">injectable_model</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-357"><a href="#EssenceModel.emi_inject_model-357"><span class="linenos">357</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceModel.emi_inject_model-358"><a href="#EssenceModel.emi_inject_model-358"><span class="linenos">358</span></a>            <span class="n">essence_model</span><span class="o">.</span><span class="n">emi_on_registered_in_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="EssenceModel.emi_inject_model-359"><a href="#EssenceModel.emi_inject_model-359"><span class="linenos">359</span></a>            <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emi_compatible_injectable_essence_model_classes</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-360"><a href="#EssenceModel.emi_inject_model-360"><span class="linenos">360</span></a>                <span class="n">essence_model</span><span class="o">.</span><span class="n">emu_behave_as_unknown_model</span><span class="p">()</span>
</span><span id="EssenceModel.emi_inject_model-361"><a href="#EssenceModel.emi_inject_model-361"><span class="linenos">361</span></a>            
</span><span id="EssenceModel.emi_inject_model-362"><a href="#EssenceModel.emi_inject_model-362"><span class="linenos">362</span></a>            <span class="n">injected</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.emi_inject_model-363"><a href="#EssenceModel.emi_inject_model-363"><span class="linenos">363</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-364"><a href="#EssenceModel.emi_inject_model-364"><span class="linenos">364</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_raise_on_uninjectable_model</span><span class="p">:</span>
</span><span id="EssenceModel.emi_inject_model-365"><a href="#EssenceModel.emi_inject_model-365"><span class="linenos">365</span></a>                <span class="k">raise</span> <span class="n">EssenceModelCanNotBeInjectedError</span>
</span><span id="EssenceModel.emi_inject_model-366"><a href="#EssenceModel.emi_inject_model-366"><span class="linenos">366</span></a>            
</span><span id="EssenceModel.emi_inject_model-367"><a href="#EssenceModel.emi_inject_model-367"><span class="linenos">367</span></a>        <span class="k">return</span> <span class="n">injected</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_injected_models" class="classattr">
                                        <input id="EssenceModel.emi_injected_models-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_injected_models</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_injected_models-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_injected_models"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_injected_models-369"><a href="#EssenceModel.emi_injected_models-369"><span class="linenos">369</span></a>    <span class="k">def</span> <span class="nf">emi_injected_models</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emi_injected_models-370"><a href="#EssenceModel.emi_injected_models-370"><span class="linenos">370</span></a>        <span class="k">return</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_injected_model" class="classattr">
                                        <input id="EssenceModel.emi_injected_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_injected_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModel">EssenceModel</a></span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_injected_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_injected_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_injected_model-372"><a href="#EssenceModel.emi_injected_model-372"><span class="linenos">372</span></a>    <span class="k">def</span> <span class="nf">emi_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="EssenceModel.emi_injected_model-373"><a href="#EssenceModel.emi_injected_model-373"><span class="linenos">373</span></a>        <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">:</span>
</span><span id="EssenceModel.emi_injected_model-374"><a href="#EssenceModel.emi_injected_model-374"><span class="linenos">374</span></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="EssenceModel.emi_injected_model-375"><a href="#EssenceModel.emi_injected_model-375"><span class="linenos">375</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="EssenceModel.emi_injected_model-376"><a href="#EssenceModel.emi_injected_model-376"><span class="linenos">376</span></a>            <span class="k">raise</span> <span class="n">EssenceModelIsNotInjectedError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_on_injected_model_updated" class="classattr">
                                        <input id="EssenceModel.emi_on_injected_model_updated-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_on_injected_model_updated</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModel">EssenceModel</a></span><span class="p">]</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_on_injected_model_updated-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_on_injected_model_updated"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_on_injected_model_updated-378"><a href="#EssenceModel.emi_on_injected_model_updated-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="nf">emi_on_injected_model_updated</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">],</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-379"><a href="#EssenceModel.emi_on_injected_model_updated-379"><span class="linenos">379</span></a>        <span class="c1"># In &#39;super&#39; in method of inherit class should be run at the end of the method</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-380"><a href="#EssenceModel.emi_on_injected_model_updated-380"><span class="linenos">380</span></a>        <span class="c1"># With deep injection it will be like (model_3, model_2, model_1, interface_1, arg_1, arg_2, arg_3)</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-381"><a href="#EssenceModel.emi_on_injected_model_updated-381"><span class="linenos">381</span></a>        <span class="c1">#   where `interface_1` is an interface of the `model_1`</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-382"><a href="#EssenceModel.emi_on_injected_model_updated-382"><span class="linenos">382</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_em_check_applicability_of_interfaces</span><span class="p">()</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-383"><a href="#EssenceModel.emi_on_injected_model_updated-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_notify_unknown_models_about_self_update</span><span class="p">()</span>
</span><span id="EssenceModel.emi_on_injected_model_updated-384"><a href="#EssenceModel.emi_on_injected_model_updated-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emi_notify_high_order_model_about_self_update</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="n">essence_model_class</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emi_remove_injected_model" class="classattr">
                                        <input id="EssenceModel.emi_remove_injected_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emi_remove_injected_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">essence_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModel">EssenceModel</a></span><span class="p">]</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emi_remove_injected_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emi_remove_injected_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emi_remove_injected_model-391"><a href="#EssenceModel.emi_remove_injected_model-391"><span class="linenos">391</span></a>    <span class="k">def</span> <span class="nf">emi_remove_injected_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModel&#39;</span><span class="p">]):</span>
</span><span id="EssenceModel.emi_remove_injected_model-392"><a href="#EssenceModel.emi_remove_injected_model-392"><span class="linenos">392</span></a>        <span class="n">injected_model</span><span class="p">:</span> <span class="s1">&#39;EssenceModel&#39;</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span><span id="EssenceModel.emi_remove_injected_model-393"><a href="#EssenceModel.emi_remove_injected_model-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_emu_deregister_on_model_changed_callback</span><span class="p">(</span><span class="n">injected_model</span><span class="p">)</span>
</span><span id="EssenceModel.emi_remove_injected_model-394"><a href="#EssenceModel.emi_remove_injected_model-394"><span class="linenos">394</span></a>        <span class="n">injected_model</span><span class="o">.</span><span class="n">emi_on_unregistering_from_high_order_model</span><span class="p">()</span>
</span><span id="EssenceModel.emi_remove_injected_model-395"><a href="#EssenceModel.emi_remove_injected_model-395"><span class="linenos">395</span></a>        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emi_injected_models</span><span class="p">[</span><span class="n">essence_model_class</span><span class="p">]</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emu_is_compatible_high_order_model" class="classattr">
                                        <input id="EssenceModel.emu_is_compatible_high_order_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_is_compatible_high_order_model</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">high_order_model_class</span><span class="p">:</span> <span class="nb">type</span><span class="p">[</span><span class="n"><a href="#EssenceModelInjectionAbstract">EssenceModelInjectionAbstract</a></span><span class="p">]</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceModel.emu_is_compatible_high_order_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emu_is_compatible_high_order_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emu_is_compatible_high_order_model-397"><a href="#EssenceModel.emu_is_compatible_high_order_model-397"><span class="linenos">397</span></a>    <span class="k">def</span> <span class="nf">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">high_order_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="s1">&#39;EssenceModelInjectionAbstract&#39;</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-398"><a href="#EssenceModel.emu_is_compatible_high_order_model-398"><span class="linenos">398</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Might be overloaded in order to make this model compatible with more than one high order models</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-399"><a href="#EssenceModel.emu_is_compatible_high_order_model-399"><span class="linenos">399</span></a>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-400"><a href="#EssenceModel.emu_is_compatible_high_order_model-400"><span class="linenos">400</span></a><span class="sd">        Args:</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-401"><a href="#EssenceModel.emu_is_compatible_high_order_model-401"><span class="linenos">401</span></a><span class="sd">            high_order_model_class (Type[): [description]</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-402"><a href="#EssenceModel.emu_is_compatible_high_order_model-402"><span class="linenos">402</span></a>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-403"><a href="#EssenceModel.emu_is_compatible_high_order_model-403"><span class="linenos">403</span></a><span class="sd">        Returns:</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-404"><a href="#EssenceModel.emu_is_compatible_high_order_model-404"><span class="linenos">404</span></a><span class="sd">            bool: [description]</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-405"><a href="#EssenceModel.emu_is_compatible_high_order_model-405"><span class="linenos">405</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-406"><a href="#EssenceModel.emu_is_compatible_high_order_model-406"><span class="linenos">406</span></a>        <span class="c1"># return high_order_model_class == self.emu_compatible_high_order_essence_model_class</span>
</span><span id="EssenceModel.emu_is_compatible_high_order_model-407"><a href="#EssenceModel.emu_is_compatible_high_order_model-407"><span class="linenos">407</span></a>        <span class="k">return</span> <span class="n">high_order_model_class</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_compatible_high_order_essence_model_classes</span>
</span></pre></div>


            <div class="docstring"><p>Might be overloaded in order to make this model compatible with more than one high order models</p>

<p>Args:
    high_order_model_class (Type[): [description]</p>

<p>Returns:
    bool: [description]</p>
</div>


                            </div>
                            <div id="EssenceModel.emu_behave_as_unknown_model" class="classattr">
                                        <input id="EssenceModel.emu_behave_as_unknown_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_behave_as_unknown_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emu_behave_as_unknown_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emu_behave_as_unknown_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emu_behave_as_unknown_model-409"><a href="#EssenceModel.emu_behave_as_unknown_model-409"><span class="linenos">409</span></a>    <span class="k">def</span> <span class="nf">emu_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-410"><a href="#EssenceModel.emu_behave_as_unknown_model-410"><span class="linenos">410</span></a>        <span class="c1"># Should be called by a high order model for an unknown injected model</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-411"><a href="#EssenceModel.emu_behave_as_unknown_model-411"><span class="linenos">411</span></a>        <span class="c1"># if type(self.__emi_high_order_model) != self.emu_compatible_high_order_essence_model_class:</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-412"><a href="#EssenceModel.emu_behave_as_unknown_model-412"><span class="linenos">412</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">emu_is_compatible_high_order_model</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="p">):</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-413"><a href="#EssenceModel.emu_behave_as_unknown_model-413"><span class="linenos">413</span></a>            <span class="k">raise</span> <span class="n">IncompatibleHighOrderEssenceModelError</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-414"><a href="#EssenceModel.emu_behave_as_unknown_model-414"><span class="linenos">414</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emi_high_order_model</span><span class="o">.</span><span class="n">_emu_register_on_model_changed_callback</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-415"><a href="#EssenceModel.emu_behave_as_unknown_model-415"><span class="linenos">415</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="EssenceModel.emu_behave_as_unknown_model-416"><a href="#EssenceModel.emu_behave_as_unknown_model-416"><span class="linenos">416</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">emu_on_behave_as_unknown_model</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emu_on_behave_as_unknown_model" class="classattr">
                                        <input id="EssenceModel.emu_on_behave_as_unknown_model-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_on_behave_as_unknown_model</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emu_on_behave_as_unknown_model-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emu_on_behave_as_unknown_model"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emu_on_behave_as_unknown_model-418"><a href="#EssenceModel.emu_on_behave_as_unknown_model-418"><span class="linenos">418</span></a>    <span class="k">def</span> <span class="nf">emu_on_behave_as_unknown_model</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emu_on_behave_as_unknown_model-419"><a href="#EssenceModel.emu_on_behave_as_unknown_model-419"><span class="linenos">419</span></a>        <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emu_on_model_changed_callback" class="classattr">
                                        <input id="EssenceModel.emu_on_model_changed_callback-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_on_model_changed_callback</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emu_on_model_changed_callback-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emu_on_model_changed_callback"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emu_on_model_changed_callback-434"><a href="#EssenceModel.emu_on_model_changed_callback-434"><span class="linenos">434</span></a>    <span class="k">def</span> <span class="nf">emu_on_model_changed_callback</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emu_on_model_changed_callback-435"><a href="#EssenceModel.emu_on_model_changed_callback-435"><span class="linenos">435</span></a>        <span class="k">raise</span> <span class="n">UnknownEssenceModeBehaviorWasNotImplementedProperlyError</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceModel.emu_is_in_unknown_model_behavior" class="classattr">
                                        <input id="EssenceModel.emu_is_in_unknown_model_behavior-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">emu_is_in_unknown_model_behavior</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceModel.emu_is_in_unknown_model_behavior-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModel.emu_is_in_unknown_model_behavior"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModel.emu_is_in_unknown_model_behavior-437"><a href="#EssenceModel.emu_is_in_unknown_model_behavior-437"><span class="linenos">437</span></a>    <span class="k">def</span> <span class="nf">emu_is_in_unknown_model_behavior</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceModel.emu_is_in_unknown_model_behavior-438"><a href="#EssenceModel.emu_is_in_unknown_model_behavior-438"><span class="linenos">438</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">__emu_in_unknown_model_behavior</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="EssenceInterface">
                            <input id="EssenceInterface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceInterface</span><wbr>(<span class="base">typing.Generic[~Model]</span>):

                <label class="view-source-button" for="EssenceInterface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface-444"><a href="#EssenceInterface-444"><span class="linenos">444</span></a><span class="k">class</span> <span class="nc">EssenceInterface</span><span class="p">(</span><span class="n">Generic</span><span class="p">[</span><span class="n">Model</span><span class="p">]):</span>
</span><span id="EssenceInterface-445"><a href="#EssenceInterface-445"><span class="linenos">445</span></a>    <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]</span> <span class="o">=</span> <span class="n">EssenceModel</span>
</span><span id="EssenceInterface-446"><a href="#EssenceInterface-446"><span class="linenos">446</span></a>
</span><span id="EssenceInterface-447"><a href="#EssenceInterface-447"><span class="linenos">447</span></a>    <span class="k">def</span> <span class="nf">__init_subclass__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="n">essence_model_class</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">Model</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceInterface-448"><a href="#EssenceInterface-448"><span class="linenos">448</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__init_subclass__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="EssenceInterface-449"><a href="#EssenceInterface-449"><span class="linenos">449</span></a>        <span class="bp">cls</span><span class="o">.</span><span class="n">essence_model_class</span> <span class="o">=</span> <span class="n">EssenceModel</span> <span class="k">if</span> <span class="n">essence_model_class</span> <span class="ow">is</span> <span class="kc">None</span> <span class="k">else</span> <span class="n">essence_model_class</span>
</span><span id="EssenceInterface-450"><a href="#EssenceInterface-450"><span class="linenos">450</span></a>
</span><span id="EssenceInterface-451"><a href="#EssenceInterface-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceInterface-452"><a href="#EssenceInterface-452"><span class="linenos">452</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceInterface-453"><a href="#EssenceInterface-453"><span class="linenos">453</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">em</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceInterface-454"><a href="#EssenceInterface-454"><span class="linenos">454</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceInterface-455"><a href="#EssenceInterface-455"><span class="linenos">455</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceInterface-456"><a href="#EssenceInterface-456"><span class="linenos">456</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__check_essence_mode_type</span><span class="p">()</span>
</span><span id="EssenceInterface-457"><a href="#EssenceInterface-457"><span class="linenos">457</span></a>
</span><span id="EssenceInterface-458"><a href="#EssenceInterface-458"><span class="linenos">458</span></a>    <span class="k">def</span> <span class="nf">__check_essence_mode_type</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="EssenceInterface-459"><a href="#EssenceInterface-459"><span class="linenos">459</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">essence_model_class</span><span class="p">):</span>
</span><span id="EssenceInterface-460"><a href="#EssenceInterface-460"><span class="linenos">460</span></a>            <span class="k">raise</span> <span class="n">IncompatibleEssenceModelError</span>
</span><span id="EssenceInterface-461"><a href="#EssenceInterface-461"><span class="linenos">461</span></a>
</span><span id="EssenceInterface-462"><a href="#EssenceInterface-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">applicable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceInterface-463"><a href="#EssenceInterface-463"><span class="linenos">463</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="EssenceInterface-464"><a href="#EssenceInterface-464"><span class="linenos">464</span></a>
</span><span id="EssenceInterface-465"><a href="#EssenceInterface-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">_applicable_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceInterface-466"><a href="#EssenceInterface-466"><span class="linenos">466</span></a>        <span class="n">result</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">applicable</span><span class="p">()</span>
</span><span id="EssenceInterface-467"><a href="#EssenceInterface-467"><span class="linenos">467</span></a>        <span class="k">if</span> <span class="n">result</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span><span class="p">:</span>
</span><span id="EssenceInterface-468"><a href="#EssenceInterface-468"><span class="linenos">468</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="EssenceInterface-469"><a href="#EssenceInterface-469"><span class="linenos">469</span></a>            <span class="k">for</span> <span class="n">handler</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="p">:</span>
</span><span id="EssenceInterface-470"><a href="#EssenceInterface-470"><span class="linenos">470</span></a>                <span class="n">handler</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="EssenceInterface-471"><a href="#EssenceInterface-471"><span class="linenos">471</span></a>        
</span><span id="EssenceInterface-472"><a href="#EssenceInterface-472"><span class="linenos">472</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="EssenceInterface-473"><a href="#EssenceInterface-473"><span class="linenos">473</span></a>    
</span><span id="EssenceInterface-474"><a href="#EssenceInterface-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">add_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="EssenceInterface-475"><a href="#EssenceInterface-475"><span class="linenos">475</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="EssenceInterface-476"><a href="#EssenceInterface-476"><span class="linenos">476</span></a>    
</span><span id="EssenceInterface-477"><a href="#EssenceInterface-477"><span class="linenos">477</span></a>    <span class="k">def</span> <span class="nf">discard_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="EssenceInterface-478"><a href="#EssenceInterface-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span><span id="EssenceInterface-479"><a href="#EssenceInterface-479"><span class="linenos">479</span></a>
</span><span id="EssenceInterface-480"><a href="#EssenceInterface-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">notify_model_about_change</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceInterface-481"><a href="#EssenceInterface-481"><span class="linenos">481</span></a>        <span class="c1"># Must be run by EssenceInterface&#39;s methods if and after changing model&#39;s data. It is enough to run in once per</span>
</span><span id="EssenceInterface-482"><a href="#EssenceInterface-482"><span class="linenos">482</span></a>        <span class="c1">#   a method - at the end of the method work.</span>
</span><span id="EssenceInterface-483"><a href="#EssenceInterface-483"><span class="linenos">483</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="o">.</span><span class="n">em_on_model_updated</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
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


                            <div id="EssenceInterface.__init__" class="classattr">
                                        <input id="EssenceInterface.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">EssenceInterface</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">essence_model</span><span class="p">:</span> <span class="o">~</span><span class="n">Model</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="EssenceInterface.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface.__init__-451"><a href="#EssenceInterface.__init__-451"><span class="linenos">451</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceInterface.__init__-452"><a href="#EssenceInterface.__init__-452"><span class="linenos">452</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceInterface.__init__-453"><a href="#EssenceInterface.__init__-453"><span class="linenos">453</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">em</span><span class="p">:</span> <span class="n">Model</span> <span class="o">=</span> <span class="n">essence_model</span>
</span><span id="EssenceInterface.__init__-454"><a href="#EssenceInterface.__init__-454"><span class="linenos">454</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="p">:</span> <span class="n">Set</span><span class="p">[</span><span class="n">Callable</span><span class="p">]</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
</span><span id="EssenceInterface.__init__-455"><a href="#EssenceInterface.__init__-455"><span class="linenos">455</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_applicability_state</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="EssenceInterface.__init__-456"><a href="#EssenceInterface.__init__-456"><span class="linenos">456</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">__check_essence_mode_type</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceInterface.essence_model_class" class="classattr">
                                <div class="attr variable">
            <span class="name">essence_model_class</span><span class="annotation">: Type[~Model]</span>        =
<span class="default_value">&lt;class &#39;<a href="#EssenceModel">EssenceModel</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#EssenceInterface.essence_model_class"></a>
    
    

                            </div>
                            <div id="EssenceInterface.essence_model" class="classattr">
                                <div class="attr variable">
            <span class="name">essence_model</span><span class="annotation">: ~Model</span>

        
    </div>
    <a class="headerlink" href="#EssenceInterface.essence_model"></a>
    
    

                            </div>
                            <div id="EssenceInterface.em" class="classattr">
                                <div class="attr variable">
            <span class="name">em</span><span class="annotation">: ~Model</span>

        
    </div>
    <a class="headerlink" href="#EssenceInterface.em"></a>
    
    

                            </div>
                            <div id="EssenceInterface.applicable" class="classattr">
                                        <input id="EssenceInterface.applicable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">applicable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="EssenceInterface.applicable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface.applicable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface.applicable-462"><a href="#EssenceInterface.applicable-462"><span class="linenos">462</span></a>    <span class="k">def</span> <span class="nf">applicable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="EssenceInterface.applicable-463"><a href="#EssenceInterface.applicable-463"><span class="linenos">463</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceInterface.add_on_applicability_changed_handler" class="classattr">
                                        <input id="EssenceInterface.add_on_applicability_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">add_on_applicability_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceInterface.add_on_applicability_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface.add_on_applicability_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface.add_on_applicability_changed_handler-474"><a href="#EssenceInterface.add_on_applicability_changed_handler-474"><span class="linenos">474</span></a>    <span class="k">def</span> <span class="nf">add_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="EssenceInterface.add_on_applicability_changed_handler-475"><a href="#EssenceInterface.add_on_applicability_changed_handler-475"><span class="linenos">475</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceInterface.discard_on_applicability_changed_handler" class="classattr">
                                        <input id="EssenceInterface.discard_on_applicability_changed_handler-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">discard_on_applicability_changed_handler</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceInterface.discard_on_applicability_changed_handler-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface.discard_on_applicability_changed_handler"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface.discard_on_applicability_changed_handler-477"><a href="#EssenceInterface.discard_on_applicability_changed_handler-477"><span class="linenos">477</span></a>    <span class="k">def</span> <span class="nf">discard_on_applicability_changed_handler</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handler</span><span class="p">:</span> <span class="n">Callable</span><span class="p">):</span>
</span><span id="EssenceInterface.discard_on_applicability_changed_handler-478"><a href="#EssenceInterface.discard_on_applicability_changed_handler-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_on_applicability_changed_handlers</span><span class="o">.</span><span class="n">discard</span><span class="p">(</span><span class="n">handler</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="EssenceInterface.notify_model_about_change" class="classattr">
                                        <input id="EssenceInterface.notify_model_about_change-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">notify_model_about_change</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="EssenceInterface.notify_model_about_change-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceInterface.notify_model_about_change"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceInterface.notify_model_about_change-480"><a href="#EssenceInterface.notify_model_about_change-480"><span class="linenos">480</span></a>    <span class="k">def</span> <span class="nf">notify_model_about_change</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceInterface.notify_model_about_change-481"><a href="#EssenceInterface.notify_model_about_change-481"><span class="linenos">481</span></a>        <span class="c1"># Must be run by EssenceInterface&#39;s methods if and after changing model&#39;s data. It is enough to run in once per</span>
</span><span id="EssenceInterface.notify_model_about_change-482"><a href="#EssenceInterface.notify_model_about_change-482"><span class="linenos">482</span></a>        <span class="c1">#   a method - at the end of the method work.</span>
</span><span id="EssenceInterface.notify_model_about_change-483"><a href="#EssenceInterface.notify_model_about_change-483"><span class="linenos">483</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">essence_model</span><span class="o">.</span><span class="n">em_on_model_updated</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="essence_model_changer">
                            <input id="essence_model_changer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">essence_model_changer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="essence_model_changer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#essence_model_changer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="essence_model_changer-486"><a href="#essence_model_changer-486"><span class="linenos">486</span></a><span class="k">def</span> <span class="nf">essence_model_changer</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="essence_model_changer-487"><a href="#essence_model_changer-487"><span class="linenos">487</span></a>    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="n">EssenceInterface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="essence_model_changer-488"><a href="#essence_model_changer-488"><span class="linenos">488</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="essence_model_changer-489"><a href="#essence_model_changer-489"><span class="linenos">489</span></a>            <span class="n">func</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="essence_model_changer-490"><a href="#essence_model_changer-490"><span class="linenos">490</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="essence_model_changer-491"><a href="#essence_model_changer-491"><span class="linenos">491</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">notify_model_about_change</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="essence_model_changer-492"><a href="#essence_model_changer-492"><span class="linenos">492</span></a>
</span><span id="essence_model_changer-493"><a href="#essence_model_changer-493"><span class="linenos">493</span></a>    <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


    

                </section>
                <section id="em_changer">
                            <input id="em_changer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">em_changer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">func</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="em_changer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#em_changer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="em_changer-486"><a href="#em_changer-486"><span class="linenos">486</span></a><span class="k">def</span> <span class="nf">essence_model_changer</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
</span><span id="em_changer-487"><a href="#em_changer-487"><span class="linenos">487</span></a>    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="bp">self</span><span class="p">:</span> <span class="n">EssenceInterface</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="em_changer-488"><a href="#em_changer-488"><span class="linenos">488</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="em_changer-489"><a href="#em_changer-489"><span class="linenos">489</span></a>            <span class="n">func</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="em_changer-490"><a href="#em_changer-490"><span class="linenos">490</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="em_changer-491"><a href="#em_changer-491"><span class="linenos">491</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">notify_model_about_change</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="em_changer-492"><a href="#em_changer-492"><span class="linenos">492</span></a>
</span><span id="em_changer-493"><a href="#em_changer-493"><span class="linenos">493</span></a>    <span class="k">return</span> <span class="n">wrapper</span>
</span></pre></div>


    

                </section>
                <section id="EssenceModelFactoryExample">
                            <input id="EssenceModelFactoryExample-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">EssenceModelFactoryExample</span>:

                <label class="view-source-button" for="EssenceModelFactoryExample-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#EssenceModelFactoryExample"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="EssenceModelFactoryExample-499"><a href="#EssenceModelFactoryExample-499"><span class="linenos">499</span></a><span class="k">class</span> <span class="nc">EssenceModelFactoryExample</span><span class="p">:</span>
</span><span id="EssenceModelFactoryExample-500"><a href="#EssenceModelFactoryExample-500"><span class="linenos">500</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="EssenceModelFactoryExample-501"><a href="#EssenceModelFactoryExample-501"><span class="linenos">501</span></a>        <span class="n">model</span><span class="p">:</span> <span class="n">EssenceModel</span> <span class="o">=</span> <span class="n">EssenceModel</span><span class="p">()</span>
</span><span id="EssenceModelFactoryExample-502"><a href="#EssenceModelFactoryExample-502"><span class="linenos">502</span></a>        <span class="n">model</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="n">EssenceInterface</span><span class="p">)</span>
</span><span id="EssenceModelFactoryExample-503"><a href="#EssenceModelFactoryExample-503"><span class="linenos">503</span></a>        <span class="k">return</span> <span class="n">model</span>
</span></pre></div>


    

                </section>
                <section id="simple_essence_model_factory">
                            <input id="simple_essence_model_factory-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">simple_essence_model_factory</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">model</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceModel">EssenceModel</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">]</span>,</span><span class="param">	<span class="n">interfaces</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">]]]</span></span><span class="return-annotation">) -> <span class="n"><a href="#EssenceModel">EssenceModel</a></span>:</span></span>

                <label class="view-source-button" for="simple_essence_model_factory-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#simple_essence_model_factory"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="simple_essence_model_factory-506"><a href="#simple_essence_model_factory-506"><span class="linenos">506</span></a><span class="k">def</span> <span class="nf">simple_essence_model_factory</span><span class="p">(</span>
</span><span id="simple_essence_model_factory-507"><a href="#simple_essence_model_factory-507"><span class="linenos">507</span></a>        <span class="n">model</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceModel</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">],</span> 
</span><span id="simple_essence_model_factory-508"><a href="#simple_essence_model_factory-508"><span class="linenos">508</span></a>        <span class="n">interfaces</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
</span><span id="simple_essence_model_factory-509"><a href="#simple_essence_model_factory-509"><span class="linenos">509</span></a>                <span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> 
</span><span id="simple_essence_model_factory-510"><a href="#simple_essence_model_factory-510"><span class="linenos">510</span></a>                <span class="n">EntityArgsHolder</span><span class="p">,</span> 
</span><span id="simple_essence_model_factory-511"><a href="#simple_essence_model_factory-511"><span class="linenos">511</span></a>                <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">]]</span>
</span><span id="simple_essence_model_factory-512"><a href="#simple_essence_model_factory-512"><span class="linenos">512</span></a>            <span class="p">]</span>
</span><span id="simple_essence_model_factory-513"><a href="#simple_essence_model_factory-513"><span class="linenos">513</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EssenceModel</span><span class="p">:</span>
</span><span id="simple_essence_model_factory-514"><a href="#simple_essence_model_factory-514"><span class="linenos">514</span></a>    <span class="n">model_instance</span><span class="p">:</span> <span class="n">EssenceModel</span> <span class="o">=</span> <span class="n">model</span><span class="p">()</span>
</span><span id="simple_essence_model_factory-515"><a href="#simple_essence_model_factory-515"><span class="linenos">515</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="nb">type</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">)):</span>
</span><span id="simple_essence_model_factory-516"><a href="#simple_essence_model_factory-516"><span class="linenos">516</span></a>        <span class="n">interfaces</span> <span class="o">=</span> <span class="p">(</span><span class="n">interfaces</span><span class="p">,)</span>
</span><span id="simple_essence_model_factory-517"><a href="#simple_essence_model_factory-517"><span class="linenos">517</span></a>    
</span><span id="simple_essence_model_factory-518"><a href="#simple_essence_model_factory-518"><span class="linenos">518</span></a>    <span class="k">for</span> <span class="n">interface</span> <span class="ow">in</span> <span class="n">interfaces</span><span class="p">:</span>
</span><span id="simple_essence_model_factory-519"><a href="#simple_essence_model_factory-519"><span class="linenos">519</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="simple_essence_model_factory-520"><a href="#simple_essence_model_factory-520"><span class="linenos">520</span></a>            <span class="k">if</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">):</span>
</span><span id="simple_essence_model_factory-521"><a href="#simple_essence_model_factory-521"><span class="linenos">521</span></a>                <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span>
</span><span id="simple_essence_model_factory-522"><a href="#simple_essence_model_factory-522"><span class="linenos">522</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">):</span>
</span><span id="simple_essence_model_factory-523"><a href="#simple_essence_model_factory-523"><span class="linenos">523</span></a>            <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="o">*</span><span class="n">interface</span><span class="o">.</span><span class="n">entity_args_kwargs</span><span class="p">())</span>
</span><span id="simple_essence_model_factory-524"><a href="#simple_essence_model_factory-524"><span class="linenos">524</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="simple_essence_model_factory-525"><a href="#simple_essence_model_factory-525"><span class="linenos">525</span></a>            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong interface type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="simple_essence_model_factory-526"><a href="#simple_essence_model_factory-526"><span class="linenos">526</span></a>
</span><span id="simple_essence_model_factory-527"><a href="#simple_essence_model_factory-527"><span class="linenos">527</span></a>    <span class="k">return</span> <span class="n">model_instance</span>
</span></pre></div>


    

                </section>
                <section id="simple_em_factory">
                            <input id="simple_em_factory-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">simple_em_factory</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">model</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceModel">EssenceModel</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">]</span>,</span><span class="param">	<span class="n">interfaces</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">,</span> <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n"><a href="#EssenceInterface">EssenceInterface</a></span><span class="p">],</span> <span class="n">cengal</span><span class="o">.</span><span class="n">code_flow_control</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">args_manager</span><span class="o">.</span><span class="n">EntityArgsHolder</span><span class="p">]]]</span></span><span class="return-annotation">) -> <span class="n"><a href="#EssenceModel">EssenceModel</a></span>:</span></span>

                <label class="view-source-button" for="simple_em_factory-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#simple_em_factory"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="simple_em_factory-506"><a href="#simple_em_factory-506"><span class="linenos">506</span></a><span class="k">def</span> <span class="nf">simple_essence_model_factory</span><span class="p">(</span>
</span><span id="simple_em_factory-507"><a href="#simple_em_factory-507"><span class="linenos">507</span></a>        <span class="n">model</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceModel</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">],</span> 
</span><span id="simple_em_factory-508"><a href="#simple_em_factory-508"><span class="linenos">508</span></a>        <span class="n">interfaces</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span>
</span><span id="simple_em_factory-509"><a href="#simple_em_factory-509"><span class="linenos">509</span></a>                <span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> 
</span><span id="simple_em_factory-510"><a href="#simple_em_factory-510"><span class="linenos">510</span></a>                <span class="n">EntityArgsHolder</span><span class="p">,</span> 
</span><span id="simple_em_factory-511"><a href="#simple_em_factory-511"><span class="linenos">511</span></a>                <span class="n">Sequence</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="n">Type</span><span class="p">[</span><span class="n">EssenceInterface</span><span class="p">],</span> <span class="n">EntityArgsHolder</span><span class="p">]]</span>
</span><span id="simple_em_factory-512"><a href="#simple_em_factory-512"><span class="linenos">512</span></a>            <span class="p">]</span>
</span><span id="simple_em_factory-513"><a href="#simple_em_factory-513"><span class="linenos">513</span></a>    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">EssenceModel</span><span class="p">:</span>
</span><span id="simple_em_factory-514"><a href="#simple_em_factory-514"><span class="linenos">514</span></a>    <span class="n">model_instance</span><span class="p">:</span> <span class="n">EssenceModel</span> <span class="o">=</span> <span class="n">model</span><span class="p">()</span>
</span><span id="simple_em_factory-515"><a href="#simple_em_factory-515"><span class="linenos">515</span></a>    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">isinstance</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="nb">type</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interfaces</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">)):</span>
</span><span id="simple_em_factory-516"><a href="#simple_em_factory-516"><span class="linenos">516</span></a>        <span class="n">interfaces</span> <span class="o">=</span> <span class="p">(</span><span class="n">interfaces</span><span class="p">,)</span>
</span><span id="simple_em_factory-517"><a href="#simple_em_factory-517"><span class="linenos">517</span></a>    
</span><span id="simple_em_factory-518"><a href="#simple_em_factory-518"><span class="linenos">518</span></a>    <span class="k">for</span> <span class="n">interface</span> <span class="ow">in</span> <span class="n">interfaces</span><span class="p">:</span>
</span><span id="simple_em_factory-519"><a href="#simple_em_factory-519"><span class="linenos">519</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="nb">type</span><span class="p">):</span>
</span><span id="simple_em_factory-520"><a href="#simple_em_factory-520"><span class="linenos">520</span></a>            <span class="k">if</span> <span class="nb">issubclass</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EssenceInterface</span><span class="p">):</span>
</span><span id="simple_em_factory-521"><a href="#simple_em_factory-521"><span class="linenos">521</span></a>                <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span>
</span><span id="simple_em_factory-522"><a href="#simple_em_factory-522"><span class="linenos">522</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">interface</span><span class="p">,</span> <span class="n">EntityArgsHolder</span><span class="p">):</span>
</span><span id="simple_em_factory-523"><a href="#simple_em_factory-523"><span class="linenos">523</span></a>            <span class="n">model_instance</span><span class="o">.</span><span class="n">em_add_interface</span><span class="p">(</span><span class="o">*</span><span class="n">interface</span><span class="o">.</span><span class="n">entity_args_kwargs</span><span class="p">())</span>
</span><span id="simple_em_factory-524"><a href="#simple_em_factory-524"><span class="linenos">524</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="simple_em_factory-525"><a href="#simple_em_factory-525"><span class="linenos">525</span></a>            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong interface type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">interface</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="simple_em_factory-526"><a href="#simple_em_factory-526"><span class="linenos">526</span></a>
</span><span id="simple_em_factory-527"><a href="#simple_em_factory-527"><span class="linenos">527</span></a>    <span class="k">return</span> <span class="n">model_instance</span>
</span></pre></div>


    

                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>