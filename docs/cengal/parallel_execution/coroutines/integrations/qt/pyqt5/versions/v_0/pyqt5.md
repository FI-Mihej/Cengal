---
title: pyqt5
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.coroutines<wbr>.integrations<wbr>.qt<wbr>.pyqt5<wbr>.versions<wbr>.v_0<wbr>.pyqt5    </h1>

                
                        <input id="mod-pyqt5-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-pyqt5-view-source"><span>View Source</span></label>

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
</span><span id="L-19"><a href="#L-19"><span class="linenos"> 19</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos"> 20</span></a>    <span class="s1">&#39;WrongQtVersion&#39;</span><span class="p">,</span> 
</span><span id="L-21"><a href="#L-21"><span class="linenos"> 21</span></a>    <span class="s1">&#39;exec_app&#39;</span><span class="p">,</span> 
</span><span id="L-22"><a href="#L-22"><span class="linenos"> 22</span></a>    <span class="s1">&#39;execa&#39;</span><span class="p">,</span> 
</span><span id="L-23"><a href="#L-23"><span class="linenos"> 23</span></a>    <span class="s1">&#39;aemit_signal&#39;</span><span class="p">,</span> 
</span><span id="L-24"><a href="#L-24"><span class="linenos"> 24</span></a>    <span class="s1">&#39;aemit&#39;</span><span class="p">,</span> 
</span><span id="L-25"><a href="#L-25"><span class="linenos"> 25</span></a>    <span class="s1">&#39;by_coro&#39;</span><span class="p">,</span> 
</span><span id="L-26"><a href="#L-26"><span class="linenos"> 26</span></a>    <span class="s1">&#39;aby_coro&#39;</span><span class="p">,</span> 
</span><span id="L-27"><a href="#L-27"><span class="linenos"> 27</span></a>    <span class="s1">&#39;modal_blocking&#39;</span><span class="p">,</span> 
</span><span id="L-28"><a href="#L-28"><span class="linenos"> 28</span></a>    <span class="s1">&#39;amodal_blocking&#39;</span><span class="p">,</span> 
</span><span id="L-29"><a href="#L-29"><span class="linenos"> 29</span></a>    <span class="s1">&#39;block_main_loop&#39;</span><span class="p">,</span> 
</span><span id="L-30"><a href="#L-30"><span class="linenos"> 30</span></a>    <span class="s1">&#39;ablock_main_loop&#39;</span><span class="p">,</span> 
</span><span id="L-31"><a href="#L-31"><span class="linenos"> 31</span></a>    <span class="s1">&#39;modal&#39;</span><span class="p">,</span> 
</span><span id="L-32"><a href="#L-32"><span class="linenos"> 32</span></a>    <span class="s1">&#39;amodal&#39;</span><span class="p">,</span> 
</span><span id="L-33"><a href="#L-33"><span class="linenos"> 33</span></a>    <span class="s1">&#39;CoroSlot&#39;</span><span class="p">,</span> 
</span><span id="L-34"><a href="#L-34"><span class="linenos"> 34</span></a>    <span class="s1">&#39;CSlot&#39;</span><span class="p">,</span> 
</span><span id="L-35"><a href="#L-35"><span class="linenos"> 35</span></a>    <span class="s1">&#39;coro_slot_implicit&#39;</span><span class="p">,</span> 
</span><span id="L-36"><a href="#L-36"><span class="linenos"> 36</span></a>    <span class="s1">&#39;cslot_implicit&#39;</span><span class="p">,</span> 
</span><span id="L-37"><a href="#L-37"><span class="linenos"> 37</span></a>    <span class="s1">&#39;csloti&#39;</span><span class="p">,</span> 
</span><span id="L-38"><a href="#L-38"><span class="linenos"> 38</span></a>    <span class="s1">&#39;csi&#39;</span><span class="p">,</span> 
</span><span id="L-39"><a href="#L-39"><span class="linenos"> 39</span></a>    <span class="s1">&#39;coro_slot_gly_patched&#39;</span><span class="p">,</span> 
</span><span id="L-40"><a href="#L-40"><span class="linenos"> 40</span></a>    <span class="s1">&#39;cslot_gly_patched&#39;</span><span class="p">,</span> 
</span><span id="L-41"><a href="#L-41"><span class="linenos"> 41</span></a>    <span class="s1">&#39;cslotglyp&#39;</span><span class="p">,</span> 
</span><span id="L-42"><a href="#L-42"><span class="linenos"> 42</span></a>    <span class="s1">&#39;cslotgp&#39;</span><span class="p">,</span> 
</span><span id="L-43"><a href="#L-43"><span class="linenos"> 43</span></a>    <span class="s1">&#39;csgp&#39;</span><span class="p">,</span> 
</span><span id="L-44"><a href="#L-44"><span class="linenos"> 44</span></a>    <span class="s1">&#39;coro_slot_agly_patched&#39;</span><span class="p">,</span> 
</span><span id="L-45"><a href="#L-45"><span class="linenos"> 45</span></a>    <span class="s1">&#39;cslot_agly_patched&#39;</span><span class="p">,</span> 
</span><span id="L-46"><a href="#L-46"><span class="linenos"> 46</span></a>    <span class="s1">&#39;cslotaglyp&#39;</span><span class="p">,</span> 
</span><span id="L-47"><a href="#L-47"><span class="linenos"> 47</span></a>    <span class="s1">&#39;cslotagp&#39;</span><span class="p">,</span> 
</span><span id="L-48"><a href="#L-48"><span class="linenos"> 48</span></a>    <span class="s1">&#39;csagp&#39;</span><span class="p">,</span> 
</span><span id="L-49"><a href="#L-49"><span class="linenos"> 49</span></a>    <span class="s1">&#39;coro_slot_explicit&#39;</span><span class="p">,</span> 
</span><span id="L-50"><a href="#L-50"><span class="linenos"> 50</span></a>    <span class="s1">&#39;cslot_explicit&#39;</span><span class="p">,</span> 
</span><span id="L-51"><a href="#L-51"><span class="linenos"> 51</span></a>    <span class="s1">&#39;cslotex&#39;</span><span class="p">,</span> 
</span><span id="L-52"><a href="#L-52"><span class="linenos"> 52</span></a>    <span class="s1">&#39;csex&#39;</span><span class="p">,</span> 
</span><span id="L-53"><a href="#L-53"><span class="linenos"> 53</span></a>    <span class="s1">&#39;qt_exec_in_coro&#39;</span><span class="p">,</span> 
</span><span id="L-54"><a href="#L-54"><span class="linenos"> 54</span></a>    <span class="s1">&#39;aqt_exec_in_coro&#39;</span><span class="p">,</span> 
</span><span id="L-55"><a href="#L-55"><span class="linenos"> 55</span></a>    <span class="s1">&#39;CoroThreadWorker&#39;</span><span class="p">,</span> 
</span><span id="L-56"><a href="#L-56"><span class="linenos"> 56</span></a>    <span class="s1">&#39;CoroThreadWithWorker&#39;</span><span class="p">,</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos"> 57</span></a><span class="p">]</span>
</span><span id="L-58"><a href="#L-58"><span class="linenos"> 58</span></a>
</span><span id="L-59"><a href="#L-59"><span class="linenos"> 59</span></a>
</span><span id="L-60"><a href="#L-60"><span class="linenos"> 60</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos"> 61</span></a><span class="sd">Module Docstring</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos"> 62</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos"> 63</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos"> 64</span></a>
</span><span id="L-65"><a href="#L-65"><span class="linenos"> 65</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos"> 66</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos"> 67</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos"> 68</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos"> 69</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos"> 70</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos"> 71</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos"> 72</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos"> 73</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos"> 74</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos"> 75</span></a>
</span><span id="L-76"><a href="#L-76"><span class="linenos"> 76</span></a>
</span><span id="L-77"><a href="#L-77"><span class="linenos"> 77</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_scheduler</span> <span class="kn">import</span> <span class="n">CoroScheduler</span><span class="p">,</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">Coro</span><span class="p">,</span> <span class="n">AnyWorker</span><span class="p">,</span> <span class="n">current_interface</span><span class="p">,</span> <span class="n">current_coro_scheduler</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">,</span> <span class="n">cs_acoro</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos"> 78</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.loop_yield</span> <span class="kn">import</span> <span class="n">gly</span><span class="p">,</span> <span class="n">CoroPriority</span><span class="p">,</span> <span class="n">gly_patched</span><span class="p">,</span> <span class="n">agly_patched</span>
</span><span id="L-79"><a href="#L-79"><span class="linenos"> 79</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.run_coro</span> <span class="kn">import</span> <span class="n">RunCoro</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos"> 80</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.put_coro</span> <span class="kn">import</span> <span class="n">PutCoro</span>
</span><span id="L-81"><a href="#L-81"><span class="linenos"> 81</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop</span> <span class="kn">import</span> <span class="n">AsyncioLoopRequest</span>
</span><span id="L-82"><a href="#L-82"><span class="linenos"> 82</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus</span> <span class="kn">import</span> <span class="n">AsyncEventBusRequest</span><span class="p">,</span> <span class="n">try_send_async_event</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos"> 83</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.simple_yield</span> <span class="kn">import</span> <span class="n">Yield</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos"> 84</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop</span> <span class="kn">import</span> <span class="n">ShutdownLoop</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos"> 85</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_standard_services.instance</span> <span class="kn">import</span> <span class="n">InstanceRequest</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos"> 86</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.coro_tools.run_in_loop</span> <span class="kn">import</span> <span class="n">run_in_loop</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos"> 87</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.coroutines.integrations.qt.common.exceptions</span> <span class="kn">import</span> <span class="n">WrongQtVersion</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos"> 88</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values</span> <span class="kn">import</span> <span class="n">ValueHolder</span>
</span><span id="L-89"><a href="#L-89"><span class="linenos"> 89</span></a><span class="kn">from</span> <span class="nn">cengal.data_generation.id_generator</span> <span class="kn">import</span> <span class="n">IDGenerator</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos"> 90</span></a>
</span><span id="L-91"><a href="#L-91"><span class="linenos"> 91</span></a><span class="kn">from</span> <span class="nn">PyQt5.QtCore</span> <span class="kn">import</span> <span class="n">pyqtSlot</span><span class="p">,</span> <span class="n">QObject</span><span class="p">,</span> <span class="n">Qt</span><span class="p">,</span> <span class="n">QTimer</span><span class="p">,</span> <span class="n">pyqtSignal</span><span class="p">,</span> <span class="n">QThread</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos"> 92</span></a><span class="kn">from</span> <span class="nn">PyQt5.QtWidgets</span> <span class="kn">import</span> <span class="n">QApplication</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos"> 93</span></a>
</span><span id="L-94"><a href="#L-94"><span class="linenos"> 94</span></a><span class="kn">from</span> <span class="nn">inspect</span> <span class="kn">import</span> <span class="n">signature</span><span class="p">,</span> <span class="n">Signature</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos"> 95</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">contextmanager</span><span class="p">,</span> <span class="n">asynccontextmanager</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos"> 96</span></a><span class="kn">from</span> <span class="nn">functools</span> <span class="kn">import</span> <span class="n">wraps</span><span class="p">,</span> <span class="n">update_wrapper</span><span class="p">,</span> <span class="n">partial</span>
</span><span id="L-97"><a href="#L-97"><span class="linenos"> 97</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Any</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">Hashable</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos"> 98</span></a>
</span><span id="L-99"><a href="#L-99"><span class="linenos"> 99</span></a>
</span><span id="L-100"><a href="#L-100"><span class="linenos">100</span></a><span class="n">YIELD_ALLOWED_EVENT</span> <span class="o">=</span> <span class="s1">&#39;QT_yield_allowed_event&#39;</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos">101</span></a><span class="n">YIELD_IN_WORK_EVENT</span> <span class="o">=</span> <span class="s1">&#39;QT_yield_in_work_event&#39;</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos">102</span></a><span class="n">MODAL_RESULT_EVENT</span> <span class="o">=</span> <span class="s1">&#39;QT_modal_result_event&#39;</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos">103</span></a><span class="n">MODAL_COUNTER</span> <span class="o">=</span> <span class="n">IDGenerator</span><span class="p">()</span>
</span><span id="L-104"><a href="#L-104"><span class="linenos">104</span></a>
</span><span id="L-105"><a href="#L-105"><span class="linenos">105</span></a>
</span><span id="L-106"><a href="#L-106"><span class="linenos">106</span></a><span class="k">def</span> <span class="nf">exec_app</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos">107</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="L-108"><a href="#L-108"><span class="linenos">108</span></a>        <span class="k">raise</span> <span class="n">WrongQtVersion</span><span class="p">(</span><span class="s1">&#39;Qt version is not PyQt5&#39;</span><span class="p">)</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos">109</span></a>    
</span><span id="L-110"><a href="#L-110"><span class="linenos">110</span></a>    <span class="n">timer</span> <span class="o">=</span> <span class="n">QTimer</span><span class="p">()</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos">111</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos">112</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos">113</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos">114</span></a>    <span class="k">def</span> <span class="nf">yield_func</span><span class="p">():</span>
</span><span id="L-115"><a href="#L-115"><span class="linenos">115</span></a>        <span class="k">if</span> <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos">116</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos">117</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos">118</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos">119</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos">120</span></a>
</span><span id="L-121"><a href="#L-121"><span class="linenos">121</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-122"><a href="#L-122"><span class="linenos">122</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">,</span> <span class="n">yield_allowed</span><span class="p">))</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos">123</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">,</span> <span class="n">yield_in_work</span><span class="p">))</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos">124</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">timeout</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">yield_func</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos">125</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos">126</span></a>    <span class="k">def</span> <span class="nf">cleanup_callback</span><span class="p">():</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos">127</span></a>        <span class="n">timer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos">128</span></a>
</span><span id="L-129"><a href="#L-129"><span class="linenos">129</span></a>    <span class="n">app</span><span class="o">.</span><span class="n">aboutToQuit</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">cleanup_callback</span><span class="p">)</span>
</span><span id="L-130"><a href="#L-130"><span class="linenos">130</span></a>    <span class="k">return</span> <span class="n">app</span><span class="o">.</span><span class="n">exec</span><span class="p">()</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos">131</span></a>
</span><span id="L-132"><a href="#L-132"><span class="linenos">132</span></a>
</span><span id="L-133"><a href="#L-133"><span class="linenos">133</span></a><span class="n">execa</span> <span class="o">=</span> <span class="n">exec_app</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos">134</span></a>
</span><span id="L-135"><a href="#L-135"><span class="linenos">135</span></a>
</span><span id="L-136"><a href="#L-136"><span class="linenos">136</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aemit_signal</span><span class="p">(</span><span class="n">signal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos">137</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos">138</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-139"><a href="#L-139"><span class="linenos">139</span></a>        <span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos">140</span></a>    
</span><span id="L-141"><a href="#L-141"><span class="linenos">141</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="L-142"><a href="#L-142"><span class="linenos">142</span></a>
</span><span id="L-143"><a href="#L-143"><span class="linenos">143</span></a>
</span><span id="L-144"><a href="#L-144"><span class="linenos">144</span></a><span class="n">aemit</span> <span class="o">=</span> <span class="n">aemit_signal</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos">145</span></a>
</span><span id="L-146"><a href="#L-146"><span class="linenos">146</span></a>
</span><span id="L-147"><a href="#L-147"><span class="linenos">147</span></a><span class="k">def</span> <span class="nf">by_coro</span><span class="p">(</span><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos">148</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos">149</span></a>        <span class="nb">callable</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos">150</span></a>    
</span><span id="L-151"><a href="#L-151"><span class="linenos">151</span></a>    <span class="k">return</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos">152</span></a>
</span><span id="L-153"><a href="#L-153"><span class="linenos">153</span></a>
</span><span id="L-154"><a href="#L-154"><span class="linenos">154</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aby_coro</span><span class="p">(</span><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos">155</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-156"><a href="#L-156"><span class="linenos">156</span></a>        <span class="nb">callable</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos">157</span></a>    
</span><span id="L-158"><a href="#L-158"><span class="linenos">158</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="L-159"><a href="#L-159"><span class="linenos">159</span></a>
</span><span id="L-160"><a href="#L-160"><span class="linenos">160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos">161</span></a><span class="k">def</span> <span class="nf">stop_yield_to_main_loop</span><span class="p">():</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos">162</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos">163</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">))</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos">164</span></a>    <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos">165</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">))</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos">166</span></a>    <span class="k">while</span> <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos">167</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos">168</span></a>
</span><span id="L-169"><a href="#L-169"><span class="linenos">169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos">170</span></a><span class="nd">@contextmanager</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos">171</span></a><span class="k">def</span> <span class="nf">block_main_loop</span><span class="p">():</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos">172</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos">173</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">))</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos">174</span></a>    <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos">175</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">))</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos">176</span></a>    <span class="k">while</span> <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="L-177"><a href="#L-177"><span class="linenos">177</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos">178</span></a>    
</span><span id="L-179"><a href="#L-179"><span class="linenos">179</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos">180</span></a>        <span class="k">yield</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos">181</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-182"><a href="#L-182"><span class="linenos">182</span></a>        <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos">183</span></a>
</span><span id="L-184"><a href="#L-184"><span class="linenos">184</span></a>
</span><span id="L-185"><a href="#L-185"><span class="linenos">185</span></a><span class="nd">@asynccontextmanager</span>
</span><span id="L-186"><a href="#L-186"><span class="linenos">186</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">ablock_main_loop</span><span class="p">():</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos">187</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos">188</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">))</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos">189</span></a>    <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos">190</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">))</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos">191</span></a>    <span class="k">while</span> <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos">192</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos">193</span></a>    
</span><span id="L-194"><a href="#L-194"><span class="linenos">194</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos">195</span></a>        <span class="k">yield</span>
</span><span id="L-196"><a href="#L-196"><span class="linenos">196</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos">197</span></a>        <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos">198</span></a>
</span><span id="L-199"><a href="#L-199"><span class="linenos">199</span></a>
</span><span id="L-200"><a href="#L-200"><span class="linenos">200</span></a><span class="k">def</span> <span class="nf">modal_blocking</span><span class="p">(</span><span class="n">modal_obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos">201</span></a>    <span class="k">with</span> <span class="n">block_main_loop</span><span class="p">():</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos">202</span></a>        <span class="k">return</span> <span class="n">modal_obj</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-203"><a href="#L-203"><span class="linenos">203</span></a>
</span><span id="L-204"><a href="#L-204"><span class="linenos">204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos">205</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">amodal_blocking</span><span class="p">(</span><span class="n">modal_obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-206"><a href="#L-206"><span class="linenos">206</span></a>    <span class="k">async</span> <span class="k">with</span> <span class="n">ablock_main_loop</span><span class="p">():</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos">207</span></a>        <span class="k">return</span> <span class="n">modal_obj</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos">208</span></a>
</span><span id="L-209"><a href="#L-209"><span class="linenos">209</span></a>
</span><span id="L-210"><a href="#L-210"><span class="linenos">210</span></a><span class="k">def</span> <span class="nf">modal</span><span class="p">(</span><span class="n">callable_with_modal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos">211</span></a>    <span class="k">class</span> <span class="nc">ShowModal</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos">212</span></a>        <span class="n">signal</span> <span class="o">=</span> <span class="n">pyqtSignal</span><span class="p">()</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos">213</span></a>
</span><span id="L-214"><a href="#L-214"><span class="linenos">214</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="L-215"><a href="#L-215"><span class="linenos">215</span></a>            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos">216</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">cs</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">result_event</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">show_modal</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="L-219"><a href="#L-219"><span class="linenos">219</span></a>
</span><span id="L-220"><a href="#L-220"><span class="linenos">220</span></a>        <span class="nd">@pyqtSlot</span><span class="p">()</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos">221</span></a>        <span class="k">def</span> <span class="nf">show_modal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos">222</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">callable_with_modal</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos">223</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos">224</span></a>
</span><span id="L-225"><a href="#L-225"><span class="linenos">225</span></a>    <span class="n">event</span> <span class="o">=</span> <span class="p">(</span><span class="n">MODAL_RESULT_EVENT</span><span class="p">,</span> <span class="n">MODAL_COUNTER</span><span class="p">())</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos">226</span></a>    <span class="n">sm</span><span class="p">:</span> <span class="n">ShowModal</span> <span class="o">=</span> <span class="n">ShowModal</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="n">event</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos">227</span></a>    <span class="n">sm</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">()</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos">228</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos">229</span></a>    <span class="k">return</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">event</span><span class="p">))</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos">230</span></a>
</span><span id="L-231"><a href="#L-231"><span class="linenos">231</span></a>
</span><span id="L-232"><a href="#L-232"><span class="linenos">232</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">amodal</span><span class="p">(</span><span class="n">callable_with_modal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-233"><a href="#L-233"><span class="linenos">233</span></a>    <span class="k">class</span> <span class="nc">ShowModal</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos">234</span></a>        <span class="n">signal</span> <span class="o">=</span> <span class="n">pyqtSignal</span><span class="p">()</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos">235</span></a>
</span><span id="L-236"><a href="#L-236"><span class="linenos">236</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos">237</span></a>            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-238"><a href="#L-238"><span class="linenos">238</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">cs</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos">239</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">result_event</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos">240</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">show_modal</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos">241</span></a>
</span><span id="L-242"><a href="#L-242"><span class="linenos">242</span></a>        <span class="nd">@pyqtSlot</span><span class="p">()</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos">243</span></a>        <span class="k">def</span> <span class="nf">show_modal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos">244</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">callable_with_modal</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos">245</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos">246</span></a>
</span><span id="L-247"><a href="#L-247"><span class="linenos">247</span></a>    <span class="n">event</span> <span class="o">=</span> <span class="p">(</span><span class="n">MODAL_RESULT_EVENT</span><span class="p">,</span> <span class="n">MODAL_COUNTER</span><span class="p">())</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos">248</span></a>    <span class="n">sm</span><span class="p">:</span> <span class="n">ShowModal</span> <span class="o">=</span> <span class="n">ShowModal</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="n">event</span><span class="p">)</span>
</span><span id="L-249"><a href="#L-249"><span class="linenos">249</span></a>    <span class="n">sm</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">()</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos">250</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos">251</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">event</span><span class="p">))</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos">252</span></a>
</span><span id="L-253"><a href="#L-253"><span class="linenos">253</span></a>
</span><span id="L-254"><a href="#L-254"><span class="linenos">254</span></a><span class="c1"># class CoroSlot(QObject):</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos">255</span></a><span class="k">class</span> <span class="nc">CoroSlot</span><span class="p">:</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos">256</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos">257</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_types</span> <span class="o">=</span> <span class="n">types</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="o">=</span> <span class="n">name</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-261"><a href="#L-261"><span class="linenos">261</span></a>
</span><span id="L-262"><a href="#L-262"><span class="linenos">262</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">,</span> <span class="n">method</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos">263</span></a>        <span class="n">method</span> <span class="o">=</span> <span class="n">method</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos">264</span></a>        <span class="k">return</span> <span class="n">method</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos">265</span></a>
</span><span id="L-266"><a href="#L-266"><span class="linenos">266</span></a>    <span class="k">def</span> <span class="nf">implicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos">267</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos">268</span></a>
</span><span id="L-269"><a href="#L-269"><span class="linenos">269</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos">270</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos">271</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos">272</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">cs_coro</span><span class="p">(</span><span class="n">coro</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos">273</span></a>        
</span><span id="L-274"><a href="#L-274"><span class="linenos">274</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-275"><a href="#L-275"><span class="linenos">275</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos">276</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos">277</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos">278</span></a>    
</span><span id="L-279"><a href="#L-279"><span class="linenos">279</span></a>    <span class="k">def</span> <span class="nf">implicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos">280</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span><span class="p">)</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos">281</span></a>    
</span><span id="L-282"><a href="#L-282"><span class="linenos">282</span></a>    <span class="n">ic</span> <span class="o">=</span> <span class="n">implicit_coro</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos">283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos">284</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-285"><a href="#L-285"><span class="linenos">285</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">))</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos">286</span></a>
</span><span id="L-287"><a href="#L-287"><span class="linenos">287</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos">288</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos">289</span></a>    
</span><span id="L-290"><a href="#L-290"><span class="linenos">290</span></a>    <span class="n">glypf</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos">291</span></a>    <span class="n">gpf</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="L-292"><a href="#L-292"><span class="linenos">292</span></a>    <span class="n">gp</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="L-293"><a href="#L-293"><span class="linenos">293</span></a>
</span><span id="L-294"><a href="#L-294"><span class="linenos">294</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos">295</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">agly_patched</span><span class="p">(</span><span class="n">afunc</span><span class="p">))</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos">296</span></a>
</span><span id="L-297"><a href="#L-297"><span class="linenos">297</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-298"><a href="#L-298"><span class="linenos">298</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos">299</span></a>    
</span><span id="L-300"><a href="#L-300"><span class="linenos">300</span></a>    <span class="n">aglypf</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos">301</span></a>    <span class="n">agpf</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos">302</span></a>    <span class="n">agp</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos">303</span></a>
</span><span id="L-304"><a href="#L-304"><span class="linenos">304</span></a>    <span class="k">def</span> <span class="nf">explicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos">305</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos">306</span></a>
</span><span id="L-307"><a href="#L-307"><span class="linenos">307</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos">308</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos">309</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos">310</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos">311</span></a>        
</span><span id="L-312"><a href="#L-312"><span class="linenos">312</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos">313</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="L-314"><a href="#L-314"><span class="linenos">314</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">())[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos">315</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos">316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos">317</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos">318</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos">319</span></a>    
</span><span id="L-320"><a href="#L-320"><span class="linenos">320</span></a>    <span class="n">ec</span> <span class="o">=</span> <span class="n">explicit_coro</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos">321</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">explicit_coro</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos">322</span></a>    <span class="n">i</span> <span class="o">=</span> <span class="n">interface</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos">323</span></a>
</span><span id="L-324"><a href="#L-324"><span class="linenos">324</span></a>
</span><span id="L-325"><a href="#L-325"><span class="linenos">325</span></a><span class="n">CSlot</span> <span class="o">=</span> <span class="n">CoroSlot</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos">326</span></a>
</span><span id="L-327"><a href="#L-327"><span class="linenos">327</span></a>
</span><span id="L-328"><a href="#L-328"><span class="linenos">328</span></a><span class="k">def</span> <span class="nf">coro_slot_implicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos">329</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos">330</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">implicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos">331</span></a>    
</span><span id="L-332"><a href="#L-332"><span class="linenos">332</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos">333</span></a>
</span><span id="L-334"><a href="#L-334"><span class="linenos">334</span></a><span class="n">cslot_implicit</span> <span class="o">=</span> <span class="n">coro_slot_implicit</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos">335</span></a><span class="n">csloti</span> <span class="o">=</span> <span class="n">coro_slot_implicit</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos">336</span></a><span class="n">csi</span> <span class="o">=</span> <span class="n">coro_slot_implicit</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos">337</span></a>
</span><span id="L-338"><a href="#L-338"><span class="linenos">338</span></a>
</span><span id="L-339"><a href="#L-339"><span class="linenos">339</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos">340</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos">341</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos">342</span></a>    
</span><span id="L-343"><a href="#L-343"><span class="linenos">343</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos">344</span></a>
</span><span id="L-345"><a href="#L-345"><span class="linenos">345</span></a><span class="n">cslot_gly_patched</span> <span class="o">=</span> <span class="n">coro_slot_gly_patched</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos">346</span></a><span class="n">cslotglyp</span> <span class="o">=</span> <span class="n">coro_slot_gly_patched</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos">347</span></a><span class="n">cslotgp</span> <span class="o">=</span> <span class="n">coro_slot_gly_patched</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos">348</span></a><span class="n">csgp</span> <span class="o">=</span> <span class="n">coro_slot_gly_patched</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos">349</span></a>
</span><span id="L-350"><a href="#L-350"><span class="linenos">350</span></a>
</span><span id="L-351"><a href="#L-351"><span class="linenos">351</span></a><span class="k">def</span> <span class="nf">coro_slot_agly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos">352</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-353"><a href="#L-353"><span class="linenos">353</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">agly_patched_function</span><span class="p">()(</span><span class="n">afunc</span><span class="p">)</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos">354</span></a>    
</span><span id="L-355"><a href="#L-355"><span class="linenos">355</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos">356</span></a>
</span><span id="L-357"><a href="#L-357"><span class="linenos">357</span></a><span class="n">cslot_agly_patched</span> <span class="o">=</span> <span class="n">coro_slot_agly_patched</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos">358</span></a><span class="n">cslotaglyp</span> <span class="o">=</span> <span class="n">coro_slot_agly_patched</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos">359</span></a><span class="n">cslotagp</span> <span class="o">=</span> <span class="n">coro_slot_agly_patched</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos">360</span></a><span class="n">csagp</span> <span class="o">=</span> <span class="n">coro_slot_gly_patched</span>
</span><span id="L-361"><a href="#L-361"><span class="linenos">361</span></a>
</span><span id="L-362"><a href="#L-362"><span class="linenos">362</span></a>
</span><span id="L-363"><a href="#L-363"><span class="linenos">363</span></a><span class="k">def</span> <span class="nf">coro_slot_explicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos">364</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos">365</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">explicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos">366</span></a>    
</span><span id="L-367"><a href="#L-367"><span class="linenos">367</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos">368</span></a>
</span><span id="L-369"><a href="#L-369"><span class="linenos">369</span></a><span class="n">cslot_explicit</span> <span class="o">=</span> <span class="n">coro_slot_explicit</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos">370</span></a><span class="n">cslotex</span> <span class="o">=</span> <span class="n">coro_slot_explicit</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos">371</span></a><span class="n">csex</span> <span class="o">=</span> <span class="n">coro_slot_explicit</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos">372</span></a>
</span><span id="L-373"><a href="#L-373"><span class="linenos">373</span></a>
</span><span id="L-374"><a href="#L-374"><span class="linenos">374</span></a><span class="k">def</span> <span class="nf">qt_exec_in_coro</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-375"><a href="#L-375"><span class="linenos">375</span></a>    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-376"><a href="#L-376"><span class="linenos">376</span></a>    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos">377</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos">378</span></a>        <span class="n">cs</span><span class="o">.</span><span class="n">high_cpu_utilisation_mode</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos">379</span></a>        <span class="n">cs</span><span class="o">.</span><span class="n">use_internal_sleep</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-380"><a href="#L-380"><span class="linenos">380</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos">381</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">())</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos">382</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos">383</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos">384</span></a>
</span><span id="L-385"><a href="#L-385"><span class="linenos">385</span></a>        <span class="n">app_or_tuple</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos">386</span></a>        <span class="n">on_exit</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">ret</span><span class="p">:</span> <span class="n">ret</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos">387</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos">388</span></a>            <span class="n">app</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos">389</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos">390</span></a>            <span class="n">app</span><span class="p">,</span> <span class="n">on_exit</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos">391</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos">392</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">&quot;qt_exec_in_coro must return either QApplication or (QApplication, on_exit) tuple&quot;</span><span class="p">)</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos">393</span></a>        
</span><span id="L-394"><a href="#L-394"><span class="linenos">394</span></a>        <span class="c1"># Run the event loop</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos">395</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">execa</span><span class="p">),</span> <span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos">396</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">on_exit</span><span class="p">),</span> <span class="n">ret</span><span class="p">)</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos">397</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="L-398"><a href="#L-398"><span class="linenos">398</span></a>        <span class="k">return</span> <span class="n">ret</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos">399</span></a>    
</span><span id="L-400"><a href="#L-400"><span class="linenos">400</span></a>    <span class="k">return</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">wrapper</span><span class="p">)</span>
</span><span id="L-401"><a href="#L-401"><span class="linenos">401</span></a>
</span><span id="L-402"><a href="#L-402"><span class="linenos">402</span></a>
</span><span id="L-403"><a href="#L-403"><span class="linenos">403</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aqt_exec_in_coro</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="L-404"><a href="#L-404"><span class="linenos">404</span></a>    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos">405</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos">406</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos">407</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="L-408"><a href="#L-408"><span class="linenos">408</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos">409</span></a>
</span><span id="L-410"><a href="#L-410"><span class="linenos">410</span></a>        <span class="n">app_or_tuple</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos">411</span></a>        <span class="n">on_exit</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">ret</span><span class="p">:</span> <span class="n">ret</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos">412</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos">413</span></a>            <span class="n">app</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos">414</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos">415</span></a>            <span class="n">app</span><span class="p">,</span> <span class="n">on_exit</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos">416</span></a>        
</span><span id="L-417"><a href="#L-417"><span class="linenos">417</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">execa</span><span class="p">),</span> <span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos">418</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">on_exit</span><span class="p">),</span> <span class="n">ret</span><span class="p">)</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos">419</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos">420</span></a>        <span class="k">return</span> <span class="n">ret</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos">421</span></a>    
</span><span id="L-422"><a href="#L-422"><span class="linenos">422</span></a>    <span class="k">return</span> <span class="n">cs_acoro</span><span class="p">(</span><span class="n">wrapper</span><span class="p">)</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos">423</span></a>
</span><span id="L-424"><a href="#L-424"><span class="linenos">424</span></a>
</span><span id="L-425"><a href="#L-425"><span class="linenos">425</span></a><span class="k">class</span> <span class="nc">CoroThreadWorker</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos">426</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos">427</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos">428</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">:</span> <span class="n">AnyWorker</span> <span class="o">=</span> <span class="n">worker</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos">431</span></a>
</span><span id="L-432"><a href="#L-432"><span class="linenos">432</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos">433</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos">434</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">my_worker_wrapper</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">worker</span><span class="p">):</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos">435</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos">436</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">)</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos">437</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">worker</span><span class="p">)</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos">438</span></a>        
</span><span id="L-439"><a href="#L-439"><span class="linenos">439</span></a>        <span class="n">run_in_loop</span><span class="p">(</span><span class="n">my_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">)</span>
</span><span id="L-440"><a href="#L-440"><span class="linenos">440</span></a>    
</span><span id="L-441"><a href="#L-441"><span class="linenos">441</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos">442</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos">443</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos">444</span></a>
</span><span id="L-445"><a href="#L-445"><span class="linenos">445</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos">446</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span><span class="p">:</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos">447</span></a>            <span class="k">return</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos">448</span></a>
</span><span id="L-449"><a href="#L-449"><span class="linenos">449</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos">450</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos">451</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos">452</span></a>        
</span><span id="L-453"><a href="#L-453"><span class="linenos">453</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos">454</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="L-455"><a href="#L-455"><span class="linenos">455</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="L-456"><a href="#L-456"><span class="linenos">456</span></a>
</span><span id="L-457"><a href="#L-457"><span class="linenos">457</span></a>
</span><span id="L-458"><a href="#L-458"><span class="linenos">458</span></a><span class="k">class</span> <span class="nc">CoroThread</span><span class="p">(</span><span class="n">QThread</span><span class="p">):</span>
</span><span id="L-459"><a href="#L-459"><span class="linenos">459</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">CoroThreadWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-460"><a href="#L-460"><span class="linenos">460</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="L-461"><a href="#L-461"><span class="linenos">461</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">:</span> <span class="n">CoroThreadWorker</span> <span class="o">=</span> <span class="n">worker</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos">462</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="o">.</span><span class="n">moveToThread</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos">463</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">started</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="o">.</span><span class="n">run</span><span class="p">)</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos">464</span></a>    
</span><span id="L-465"><a href="#L-465"><span class="linenos">465</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-466"><a href="#L-466"><span class="linenos">466</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">quit</span><span class="p">()</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos">467</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos">468</span></a>
</span><span id="L-469"><a href="#L-469"><span class="linenos">469</span></a>
</span><span id="L-470"><a href="#L-470"><span class="linenos">470</span></a><span class="k">class</span> <span class="nc">CoroThreadWithWorker</span><span class="p">(</span><span class="n">CoroThreadWorker</span><span class="p">):</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos">471</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos">472</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">worker</span><span class="p">)</span>
</span><span id="L-473"><a href="#L-473"><span class="linenos">473</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="p">:</span> <span class="n">CoroThread</span> <span class="o">=</span> <span class="n">CoroThread</span><span class="p">(</span><span class="n">parent</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos">474</span></a>    
</span><span id="L-475"><a href="#L-475"><span class="linenos">475</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-476"><a href="#L-476"><span class="linenos">476</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos">477</span></a>    
</span><span id="L-478"><a href="#L-478"><span class="linenos">478</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos">479</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos">480</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span></pre></div>


            </section>
                <section id="WrongQtVersion">
                            <input id="WrongQtVersion-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">WrongQtVersion</span><wbr>(<span class="base">builtins.Exception</span>):

                <label class="view-source-button" for="WrongQtVersion-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#WrongQtVersion"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="WrongQtVersion-40"><a href="#WrongQtVersion-40"><span class="linenos">40</span></a><span class="k">class</span> <span class="nc">WrongQtVersion</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
</span><span id="WrongQtVersion-41"><a href="#WrongQtVersion-41"><span class="linenos">41</span></a>    <span class="k">pass</span>
</span></pre></div>


            <div class="docstring"><p>Common base class for all non-exit exceptions.</p>
</div>


                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>builtins.Exception</dt>
                                <dd id="WrongQtVersion.__init__" class="function">Exception</dd>

            </div>
            <div><dt>builtins.BaseException</dt>
                                <dd id="WrongQtVersion.with_traceback" class="function">with_traceback</dd>
                <dd id="WrongQtVersion.args" class="variable">args</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="exec_app">
                            <input id="exec_app-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">exec_app</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">app</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="exec_app-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#exec_app"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="exec_app-107"><a href="#exec_app-107"><span class="linenos">107</span></a><span class="k">def</span> <span class="nf">exec_app</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="exec_app-108"><a href="#exec_app-108"><span class="linenos">108</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="exec_app-109"><a href="#exec_app-109"><span class="linenos">109</span></a>        <span class="k">raise</span> <span class="n">WrongQtVersion</span><span class="p">(</span><span class="s1">&#39;Qt version is not PyQt5&#39;</span><span class="p">)</span>
</span><span id="exec_app-110"><a href="#exec_app-110"><span class="linenos">110</span></a>    
</span><span id="exec_app-111"><a href="#exec_app-111"><span class="linenos">111</span></a>    <span class="n">timer</span> <span class="o">=</span> <span class="n">QTimer</span><span class="p">()</span>
</span><span id="exec_app-112"><a href="#exec_app-112"><span class="linenos">112</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="exec_app-113"><a href="#exec_app-113"><span class="linenos">113</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="exec_app-114"><a href="#exec_app-114"><span class="linenos">114</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="exec_app-115"><a href="#exec_app-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">yield_func</span><span class="p">():</span>
</span><span id="exec_app-116"><a href="#exec_app-116"><span class="linenos">116</span></a>        <span class="k">if</span> <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="exec_app-117"><a href="#exec_app-117"><span class="linenos">117</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="exec_app-118"><a href="#exec_app-118"><span class="linenos">118</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="exec_app-119"><a href="#exec_app-119"><span class="linenos">119</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="exec_app-120"><a href="#exec_app-120"><span class="linenos">120</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="exec_app-121"><a href="#exec_app-121"><span class="linenos">121</span></a>
</span><span id="exec_app-122"><a href="#exec_app-122"><span class="linenos">122</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="exec_app-123"><a href="#exec_app-123"><span class="linenos">123</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">,</span> <span class="n">yield_allowed</span><span class="p">))</span>
</span><span id="exec_app-124"><a href="#exec_app-124"><span class="linenos">124</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">,</span> <span class="n">yield_in_work</span><span class="p">))</span>
</span><span id="exec_app-125"><a href="#exec_app-125"><span class="linenos">125</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">timeout</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">yield_func</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="exec_app-126"><a href="#exec_app-126"><span class="linenos">126</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="exec_app-127"><a href="#exec_app-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">cleanup_callback</span><span class="p">():</span>
</span><span id="exec_app-128"><a href="#exec_app-128"><span class="linenos">128</span></a>        <span class="n">timer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="exec_app-129"><a href="#exec_app-129"><span class="linenos">129</span></a>
</span><span id="exec_app-130"><a href="#exec_app-130"><span class="linenos">130</span></a>    <span class="n">app</span><span class="o">.</span><span class="n">aboutToQuit</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">cleanup_callback</span><span class="p">)</span>
</span><span id="exec_app-131"><a href="#exec_app-131"><span class="linenos">131</span></a>    <span class="k">return</span> <span class="n">app</span><span class="o">.</span><span class="n">exec</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="execa">
                            <input id="execa-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">execa</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">app</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="nb">int</span>:</span></span>

                <label class="view-source-button" for="execa-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#execa"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="execa-107"><a href="#execa-107"><span class="linenos">107</span></a><span class="k">def</span> <span class="nf">exec_app</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
</span><span id="execa-108"><a href="#execa-108"><span class="linenos">108</span></a>    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="execa-109"><a href="#execa-109"><span class="linenos">109</span></a>        <span class="k">raise</span> <span class="n">WrongQtVersion</span><span class="p">(</span><span class="s1">&#39;Qt version is not PyQt5&#39;</span><span class="p">)</span>
</span><span id="execa-110"><a href="#execa-110"><span class="linenos">110</span></a>    
</span><span id="execa-111"><a href="#execa-111"><span class="linenos">111</span></a>    <span class="n">timer</span> <span class="o">=</span> <span class="n">QTimer</span><span class="p">()</span>
</span><span id="execa-112"><a href="#execa-112"><span class="linenos">112</span></a>    <span class="n">ly</span> <span class="o">=</span> <span class="n">gly</span><span class="p">(</span><span class="n">default_priority</span><span class="p">)</span>
</span><span id="execa-113"><a href="#execa-113"><span class="linenos">113</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="execa-114"><a href="#execa-114"><span class="linenos">114</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">ValueHolder</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span> <span class="kc">True</span><span class="p">)</span>
</span><span id="execa-115"><a href="#execa-115"><span class="linenos">115</span></a>    <span class="k">def</span> <span class="nf">yield_func</span><span class="p">():</span>
</span><span id="execa-116"><a href="#execa-116"><span class="linenos">116</span></a>        <span class="k">if</span> <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="execa-117"><a href="#execa-117"><span class="linenos">117</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="execa-118"><a href="#execa-118"><span class="linenos">118</span></a>            <span class="n">ly</span><span class="p">()</span>
</span><span id="execa-119"><a href="#execa-119"><span class="linenos">119</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="execa-120"><a href="#execa-120"><span class="linenos">120</span></a>            <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="execa-121"><a href="#execa-121"><span class="linenos">121</span></a>
</span><span id="execa-122"><a href="#execa-122"><span class="linenos">122</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="execa-123"><a href="#execa-123"><span class="linenos">123</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">,</span> <span class="n">yield_allowed</span><span class="p">))</span>
</span><span id="execa-124"><a href="#execa-124"><span class="linenos">124</span></a>    <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">,</span> <span class="n">yield_in_work</span><span class="p">))</span>
</span><span id="execa-125"><a href="#execa-125"><span class="linenos">125</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">timeout</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">yield_func</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="execa-126"><a href="#execa-126"><span class="linenos">126</span></a>    <span class="n">timer</span><span class="o">.</span><span class="n">start</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="execa-127"><a href="#execa-127"><span class="linenos">127</span></a>    <span class="k">def</span> <span class="nf">cleanup_callback</span><span class="p">():</span>
</span><span id="execa-128"><a href="#execa-128"><span class="linenos">128</span></a>        <span class="n">timer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="execa-129"><a href="#execa-129"><span class="linenos">129</span></a>
</span><span id="execa-130"><a href="#execa-130"><span class="linenos">130</span></a>    <span class="n">app</span><span class="o">.</span><span class="n">aboutToQuit</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">cleanup_callback</span><span class="p">)</span>
</span><span id="execa-131"><a href="#execa-131"><span class="linenos">131</span></a>    <span class="k">return</span> <span class="n">app</span><span class="o">.</span><span class="n">exec</span><span class="p">()</span>
</span></pre></div>


    

                </section>
                <section id="aemit_signal">
                            <input id="aemit_signal-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aemit_signal</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">signal</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="aemit_signal-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aemit_signal"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aemit_signal-137"><a href="#aemit_signal-137"><span class="linenos">137</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aemit_signal</span><span class="p">(</span><span class="n">signal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="aemit_signal-138"><a href="#aemit_signal-138"><span class="linenos">138</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="aemit_signal-139"><a href="#aemit_signal-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="aemit_signal-140"><a href="#aemit_signal-140"><span class="linenos">140</span></a>        <span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="aemit_signal-141"><a href="#aemit_signal-141"><span class="linenos">141</span></a>    
</span><span id="aemit_signal-142"><a href="#aemit_signal-142"><span class="linenos">142</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="aemit">
                            <input id="aemit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aemit</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">signal</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="aemit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aemit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aemit-137"><a href="#aemit-137"><span class="linenos">137</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aemit_signal</span><span class="p">(</span><span class="n">signal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="aemit-138"><a href="#aemit-138"><span class="linenos">138</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="aemit-139"><a href="#aemit-139"><span class="linenos">139</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="aemit-140"><a href="#aemit-140"><span class="linenos">140</span></a>        <span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="aemit-141"><a href="#aemit-141"><span class="linenos">141</span></a>    
</span><span id="aemit-142"><a href="#aemit-142"><span class="linenos">142</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="by_coro">
                            <input id="by_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">by_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="by_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#by_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="by_coro-148"><a href="#by_coro-148"><span class="linenos">148</span></a><span class="k">def</span> <span class="nf">by_coro</span><span class="p">(</span><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="by_coro-149"><a href="#by_coro-149"><span class="linenos">149</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="by_coro-150"><a href="#by_coro-150"><span class="linenos">150</span></a>        <span class="nb">callable</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="by_coro-151"><a href="#by_coro-151"><span class="linenos">151</span></a>    
</span><span id="by_coro-152"><a href="#by_coro-152"><span class="linenos">152</span></a>    <span class="k">return</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="aby_coro">
                            <input id="aby_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aby_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="aby_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aby_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aby_coro-155"><a href="#aby_coro-155"><span class="linenos">155</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aby_coro</span><span class="p">(</span><span class="nb">callable</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="aby_coro-156"><a href="#aby_coro-156"><span class="linenos">156</span></a>    <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="aby_coro-157"><a href="#aby_coro-157"><span class="linenos">157</span></a>        <span class="nb">callable</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="aby_coro-158"><a href="#aby_coro-158"><span class="linenos">158</span></a>    
</span><span id="aby_coro-159"><a href="#aby_coro-159"><span class="linenos">159</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">current_interface</span><span class="p">()(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="modal_blocking">
                            <input id="modal_blocking-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">modal_blocking</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">modal_obj</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="modal_blocking-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#modal_blocking"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="modal_blocking-201"><a href="#modal_blocking-201"><span class="linenos">201</span></a><span class="k">def</span> <span class="nf">modal_blocking</span><span class="p">(</span><span class="n">modal_obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="modal_blocking-202"><a href="#modal_blocking-202"><span class="linenos">202</span></a>    <span class="k">with</span> <span class="n">block_main_loop</span><span class="p">():</span>
</span><span id="modal_blocking-203"><a href="#modal_blocking-203"><span class="linenos">203</span></a>        <span class="k">return</span> <span class="n">modal_obj</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="amodal_blocking">
                            <input id="amodal_blocking-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">amodal_blocking</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">modal_obj</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="amodal_blocking-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#amodal_blocking"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="amodal_blocking-206"><a href="#amodal_blocking-206"><span class="linenos">206</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">amodal_blocking</span><span class="p">(</span><span class="n">modal_obj</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="amodal_blocking-207"><a href="#amodal_blocking-207"><span class="linenos">207</span></a>    <span class="k">async</span> <span class="k">with</span> <span class="n">ablock_main_loop</span><span class="p">():</span>
</span><span id="amodal_blocking-208"><a href="#amodal_blocking-208"><span class="linenos">208</span></a>        <span class="k">return</span> <span class="n">modal_obj</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="block_main_loop">
                            <input id="block_main_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@contextmanager</div>

        <span class="def">def</span>
        <span class="name">block_main_loop</span><span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>

                <label class="view-source-button" for="block_main_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#block_main_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="block_main_loop-171"><a href="#block_main_loop-171"><span class="linenos">171</span></a><span class="nd">@contextmanager</span>
</span><span id="block_main_loop-172"><a href="#block_main_loop-172"><span class="linenos">172</span></a><span class="k">def</span> <span class="nf">block_main_loop</span><span class="p">():</span>
</span><span id="block_main_loop-173"><a href="#block_main_loop-173"><span class="linenos">173</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="block_main_loop-174"><a href="#block_main_loop-174"><span class="linenos">174</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">))</span>
</span><span id="block_main_loop-175"><a href="#block_main_loop-175"><span class="linenos">175</span></a>    <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="block_main_loop-176"><a href="#block_main_loop-176"><span class="linenos">176</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">))</span>
</span><span id="block_main_loop-177"><a href="#block_main_loop-177"><span class="linenos">177</span></a>    <span class="k">while</span> <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="block_main_loop-178"><a href="#block_main_loop-178"><span class="linenos">178</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="block_main_loop-179"><a href="#block_main_loop-179"><span class="linenos">179</span></a>    
</span><span id="block_main_loop-180"><a href="#block_main_loop-180"><span class="linenos">180</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="block_main_loop-181"><a href="#block_main_loop-181"><span class="linenos">181</span></a>        <span class="k">yield</span>
</span><span id="block_main_loop-182"><a href="#block_main_loop-182"><span class="linenos">182</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="block_main_loop-183"><a href="#block_main_loop-183"><span class="linenos">183</span></a>        <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                </section>
                <section id="ablock_main_loop">
                            <input id="ablock_main_loop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@asynccontextmanager</div>

        <span class="def">async def</span>
        <span class="name">ablock_main_loop</span><span class="signature pdoc-code condensed">(<span class="return-annotation">):</span></span>

                <label class="view-source-button" for="ablock_main_loop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#ablock_main_loop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="ablock_main_loop-186"><a href="#ablock_main_loop-186"><span class="linenos">186</span></a><span class="nd">@asynccontextmanager</span>
</span><span id="ablock_main_loop-187"><a href="#ablock_main_loop-187"><span class="linenos">187</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">ablock_main_loop</span><span class="p">():</span>
</span><span id="ablock_main_loop-188"><a href="#ablock_main_loop-188"><span class="linenos">188</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="ablock_main_loop-189"><a href="#ablock_main_loop-189"><span class="linenos">189</span></a>    <span class="n">yield_allowed</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_ALLOWED_EVENT</span><span class="p">))</span>
</span><span id="ablock_main_loop-190"><a href="#ablock_main_loop-190"><span class="linenos">190</span></a>    <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="ablock_main_loop-191"><a href="#ablock_main_loop-191"><span class="linenos">191</span></a>    <span class="n">yield_in_work</span><span class="p">:</span> <span class="n">ValueHolder</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">InstanceRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">YIELD_IN_WORK_EVENT</span><span class="p">))</span>
</span><span id="ablock_main_loop-192"><a href="#ablock_main_loop-192"><span class="linenos">192</span></a>    <span class="k">while</span> <span class="n">yield_in_work</span><span class="o">.</span><span class="n">value</span><span class="p">:</span>
</span><span id="ablock_main_loop-193"><a href="#ablock_main_loop-193"><span class="linenos">193</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">Yield</span><span class="p">)</span>
</span><span id="ablock_main_loop-194"><a href="#ablock_main_loop-194"><span class="linenos">194</span></a>    
</span><span id="ablock_main_loop-195"><a href="#ablock_main_loop-195"><span class="linenos">195</span></a>    <span class="k">try</span><span class="p">:</span>
</span><span id="ablock_main_loop-196"><a href="#ablock_main_loop-196"><span class="linenos">196</span></a>        <span class="k">yield</span>
</span><span id="ablock_main_loop-197"><a href="#ablock_main_loop-197"><span class="linenos">197</span></a>    <span class="k">finally</span><span class="p">:</span>
</span><span id="ablock_main_loop-198"><a href="#ablock_main_loop-198"><span class="linenos">198</span></a>        <span class="n">yield_allowed</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                </section>
                <section id="modal">
                            <input id="modal-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">modal</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">callable_with_modal</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="modal-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#modal"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="modal-211"><a href="#modal-211"><span class="linenos">211</span></a><span class="k">def</span> <span class="nf">modal</span><span class="p">(</span><span class="n">callable_with_modal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="modal-212"><a href="#modal-212"><span class="linenos">212</span></a>    <span class="k">class</span> <span class="nc">ShowModal</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="modal-213"><a href="#modal-213"><span class="linenos">213</span></a>        <span class="n">signal</span> <span class="o">=</span> <span class="n">pyqtSignal</span><span class="p">()</span>
</span><span id="modal-214"><a href="#modal-214"><span class="linenos">214</span></a>
</span><span id="modal-215"><a href="#modal-215"><span class="linenos">215</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="modal-216"><a href="#modal-216"><span class="linenos">216</span></a>            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="modal-217"><a href="#modal-217"><span class="linenos">217</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">cs</span>
</span><span id="modal-218"><a href="#modal-218"><span class="linenos">218</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">result_event</span>
</span><span id="modal-219"><a href="#modal-219"><span class="linenos">219</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">show_modal</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="modal-220"><a href="#modal-220"><span class="linenos">220</span></a>
</span><span id="modal-221"><a href="#modal-221"><span class="linenos">221</span></a>        <span class="nd">@pyqtSlot</span><span class="p">()</span>
</span><span id="modal-222"><a href="#modal-222"><span class="linenos">222</span></a>        <span class="k">def</span> <span class="nf">show_modal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="modal-223"><a href="#modal-223"><span class="linenos">223</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">callable_with_modal</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="modal-224"><a href="#modal-224"><span class="linenos">224</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="modal-225"><a href="#modal-225"><span class="linenos">225</span></a>
</span><span id="modal-226"><a href="#modal-226"><span class="linenos">226</span></a>    <span class="n">event</span> <span class="o">=</span> <span class="p">(</span><span class="n">MODAL_RESULT_EVENT</span><span class="p">,</span> <span class="n">MODAL_COUNTER</span><span class="p">())</span>
</span><span id="modal-227"><a href="#modal-227"><span class="linenos">227</span></a>    <span class="n">sm</span><span class="p">:</span> <span class="n">ShowModal</span> <span class="o">=</span> <span class="n">ShowModal</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="n">event</span><span class="p">)</span>
</span><span id="modal-228"><a href="#modal-228"><span class="linenos">228</span></a>    <span class="n">sm</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">()</span>
</span><span id="modal-229"><a href="#modal-229"><span class="linenos">229</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="modal-230"><a href="#modal-230"><span class="linenos">230</span></a>    <span class="k">return</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">event</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="amodal">
                            <input id="amodal-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">amodal</span><span class="signature pdoc-code condensed">(<span class="param"><span class="n">callable_with_modal</span>, </span><span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="amodal-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#amodal"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="amodal-233"><a href="#amodal-233"><span class="linenos">233</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">amodal</span><span class="p">(</span><span class="n">callable_with_modal</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="amodal-234"><a href="#amodal-234"><span class="linenos">234</span></a>    <span class="k">class</span> <span class="nc">ShowModal</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="amodal-235"><a href="#amodal-235"><span class="linenos">235</span></a>        <span class="n">signal</span> <span class="o">=</span> <span class="n">pyqtSignal</span><span class="p">()</span>
</span><span id="amodal-236"><a href="#amodal-236"><span class="linenos">236</span></a>
</span><span id="amodal-237"><a href="#amodal-237"><span class="linenos">237</span></a>        <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span><span class="p">,</span> <span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span><span class="p">):</span>
</span><span id="amodal-238"><a href="#amodal-238"><span class="linenos">238</span></a>            <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="amodal-239"><a href="#amodal-239"><span class="linenos">239</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">cs</span>
</span><span id="amodal-240"><a href="#amodal-240"><span class="linenos">240</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">:</span> <span class="n">Hashable</span> <span class="o">=</span> <span class="n">result_event</span>
</span><span id="amodal-241"><a href="#amodal-241"><span class="linenos">241</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">show_modal</span><span class="p">,</span> <span class="n">Qt</span><span class="o">.</span><span class="n">ConnectionType</span><span class="o">.</span><span class="n">QueuedConnection</span><span class="p">)</span>
</span><span id="amodal-242"><a href="#amodal-242"><span class="linenos">242</span></a>
</span><span id="amodal-243"><a href="#amodal-243"><span class="linenos">243</span></a>        <span class="nd">@pyqtSlot</span><span class="p">()</span>
</span><span id="amodal-244"><a href="#amodal-244"><span class="linenos">244</span></a>        <span class="k">def</span> <span class="nf">show_modal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="amodal-245"><a href="#amodal-245"><span class="linenos">245</span></a>            <span class="n">result</span> <span class="o">=</span> <span class="n">callable_with_modal</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="amodal-246"><a href="#amodal-246"><span class="linenos">246</span></a>            <span class="n">try_send_async_event</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">cs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">result_event</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span>
</span><span id="amodal-247"><a href="#amodal-247"><span class="linenos">247</span></a>
</span><span id="amodal-248"><a href="#amodal-248"><span class="linenos">248</span></a>    <span class="n">event</span> <span class="o">=</span> <span class="p">(</span><span class="n">MODAL_RESULT_EVENT</span><span class="p">,</span> <span class="n">MODAL_COUNTER</span><span class="p">())</span>
</span><span id="amodal-249"><a href="#amodal-249"><span class="linenos">249</span></a>    <span class="n">sm</span><span class="p">:</span> <span class="n">ShowModal</span> <span class="o">=</span> <span class="n">ShowModal</span><span class="p">(</span><span class="n">current_coro_scheduler</span><span class="p">(),</span> <span class="n">event</span><span class="p">)</span>
</span><span id="amodal-250"><a href="#amodal-250"><span class="linenos">250</span></a>    <span class="n">sm</span><span class="o">.</span><span class="n">signal</span><span class="o">.</span><span class="n">emit</span><span class="p">()</span>
</span><span id="amodal-251"><a href="#amodal-251"><span class="linenos">251</span></a>    <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="amodal-252"><a href="#amodal-252"><span class="linenos">252</span></a>    <span class="k">return</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncEventBusRequest</span><span class="p">()</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">event</span><span class="p">))</span>
</span></pre></div>


    

                </section>
                <section id="CoroSlot">
                            <input id="CoroSlot-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroSlot</span>:

                <label class="view-source-button" for="CoroSlot-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot-256"><a href="#CoroSlot-256"><span class="linenos">256</span></a><span class="k">class</span> <span class="nc">CoroSlot</span><span class="p">:</span>
</span><span id="CoroSlot-257"><a href="#CoroSlot-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroSlot-258"><a href="#CoroSlot-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_types</span> <span class="o">=</span> <span class="n">types</span>
</span><span id="CoroSlot-259"><a href="#CoroSlot-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="o">=</span> <span class="n">name</span>
</span><span id="CoroSlot-260"><a href="#CoroSlot-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="CoroSlot-261"><a href="#CoroSlot-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CoroSlot-262"><a href="#CoroSlot-262"><span class="linenos">262</span></a>
</span><span id="CoroSlot-263"><a href="#CoroSlot-263"><span class="linenos">263</span></a>    <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">,</span> <span class="n">method</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-264"><a href="#CoroSlot-264"><span class="linenos">264</span></a>        <span class="n">method</span> <span class="o">=</span> <span class="n">method</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span>
</span><span id="CoroSlot-265"><a href="#CoroSlot-265"><span class="linenos">265</span></a>        <span class="k">return</span> <span class="n">method</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot-266"><a href="#CoroSlot-266"><span class="linenos">266</span></a>
</span><span id="CoroSlot-267"><a href="#CoroSlot-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">implicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-268"><a href="#CoroSlot-268"><span class="linenos">268</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="CoroSlot-269"><a href="#CoroSlot-269"><span class="linenos">269</span></a>
</span><span id="CoroSlot-270"><a href="#CoroSlot-270"><span class="linenos">270</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="CoroSlot-271"><a href="#CoroSlot-271"><span class="linenos">271</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroSlot-272"><a href="#CoroSlot-272"><span class="linenos">272</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroSlot-273"><a href="#CoroSlot-273"><span class="linenos">273</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">cs_coro</span><span class="p">(</span><span class="n">coro</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="CoroSlot-274"><a href="#CoroSlot-274"><span class="linenos">274</span></a>        
</span><span id="CoroSlot-275"><a href="#CoroSlot-275"><span class="linenos">275</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot-276"><a href="#CoroSlot-276"><span class="linenos">276</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot-277"><a href="#CoroSlot-277"><span class="linenos">277</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="CoroSlot-278"><a href="#CoroSlot-278"><span class="linenos">278</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span><span id="CoroSlot-279"><a href="#CoroSlot-279"><span class="linenos">279</span></a>    
</span><span id="CoroSlot-280"><a href="#CoroSlot-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">implicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroSlot-281"><a href="#CoroSlot-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span><span class="p">)</span>
</span><span id="CoroSlot-282"><a href="#CoroSlot-282"><span class="linenos">282</span></a>    
</span><span id="CoroSlot-283"><a href="#CoroSlot-283"><span class="linenos">283</span></a>    <span class="n">ic</span> <span class="o">=</span> <span class="n">implicit_coro</span>
</span><span id="CoroSlot-284"><a href="#CoroSlot-284"><span class="linenos">284</span></a>
</span><span id="CoroSlot-285"><a href="#CoroSlot-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-286"><a href="#CoroSlot-286"><span class="linenos">286</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">))</span>
</span><span id="CoroSlot-287"><a href="#CoroSlot-287"><span class="linenos">287</span></a>
</span><span id="CoroSlot-288"><a href="#CoroSlot-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-289"><a href="#CoroSlot-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span><span id="CoroSlot-290"><a href="#CoroSlot-290"><span class="linenos">290</span></a>    
</span><span id="CoroSlot-291"><a href="#CoroSlot-291"><span class="linenos">291</span></a>    <span class="n">glypf</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="CoroSlot-292"><a href="#CoroSlot-292"><span class="linenos">292</span></a>    <span class="n">gpf</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="CoroSlot-293"><a href="#CoroSlot-293"><span class="linenos">293</span></a>    <span class="n">gp</span> <span class="o">=</span> <span class="n">gly_patched_function</span>
</span><span id="CoroSlot-294"><a href="#CoroSlot-294"><span class="linenos">294</span></a>
</span><span id="CoroSlot-295"><a href="#CoroSlot-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-296"><a href="#CoroSlot-296"><span class="linenos">296</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">agly_patched</span><span class="p">(</span><span class="n">afunc</span><span class="p">))</span>
</span><span id="CoroSlot-297"><a href="#CoroSlot-297"><span class="linenos">297</span></a>
</span><span id="CoroSlot-298"><a href="#CoroSlot-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-299"><a href="#CoroSlot-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span><span id="CoroSlot-300"><a href="#CoroSlot-300"><span class="linenos">300</span></a>    
</span><span id="CoroSlot-301"><a href="#CoroSlot-301"><span class="linenos">301</span></a>    <span class="n">aglypf</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="CoroSlot-302"><a href="#CoroSlot-302"><span class="linenos">302</span></a>    <span class="n">agpf</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="CoroSlot-303"><a href="#CoroSlot-303"><span class="linenos">303</span></a>    <span class="n">agp</span> <span class="o">=</span> <span class="n">agly_patched_function</span>
</span><span id="CoroSlot-304"><a href="#CoroSlot-304"><span class="linenos">304</span></a>
</span><span id="CoroSlot-305"><a href="#CoroSlot-305"><span class="linenos">305</span></a>    <span class="k">def</span> <span class="nf">explicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-306"><a href="#CoroSlot-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="CoroSlot-307"><a href="#CoroSlot-307"><span class="linenos">307</span></a>
</span><span id="CoroSlot-308"><a href="#CoroSlot-308"><span class="linenos">308</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="CoroSlot-309"><a href="#CoroSlot-309"><span class="linenos">309</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroSlot-310"><a href="#CoroSlot-310"><span class="linenos">310</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroSlot-311"><a href="#CoroSlot-311"><span class="linenos">311</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="CoroSlot-312"><a href="#CoroSlot-312"><span class="linenos">312</span></a>        
</span><span id="CoroSlot-313"><a href="#CoroSlot-313"><span class="linenos">313</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot-314"><a href="#CoroSlot-314"><span class="linenos">314</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot-315"><a href="#CoroSlot-315"><span class="linenos">315</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">())[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="CoroSlot-316"><a href="#CoroSlot-316"><span class="linenos">316</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span><span id="CoroSlot-317"><a href="#CoroSlot-317"><span class="linenos">317</span></a>
</span><span id="CoroSlot-318"><a href="#CoroSlot-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot-319"><a href="#CoroSlot-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span><span id="CoroSlot-320"><a href="#CoroSlot-320"><span class="linenos">320</span></a>    
</span><span id="CoroSlot-321"><a href="#CoroSlot-321"><span class="linenos">321</span></a>    <span class="n">ec</span> <span class="o">=</span> <span class="n">explicit_coro</span>
</span><span id="CoroSlot-322"><a href="#CoroSlot-322"><span class="linenos">322</span></a>    <span class="n">interface</span> <span class="o">=</span> <span class="n">explicit_coro</span>
</span><span id="CoroSlot-323"><a href="#CoroSlot-323"><span class="linenos">323</span></a>    <span class="n">i</span> <span class="o">=</span> <span class="n">interface</span>
</span></pre></div>


    

                            <div id="CoroSlot.__init__" class="classattr">
                                        <input id="CoroSlot.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CoroSlot</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span>)</span>

                <label class="view-source-button" for="CoroSlot.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.__init__-257"><a href="#CoroSlot.__init__-257"><span class="linenos">257</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroSlot.__init__-258"><a href="#CoroSlot.__init__-258"><span class="linenos">258</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_types</span> <span class="o">=</span> <span class="n">types</span>
</span><span id="CoroSlot.__init__-259"><a href="#CoroSlot.__init__-259"><span class="linenos">259</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="o">=</span> <span class="n">name</span>
</span><span id="CoroSlot.__init__-260"><a href="#CoroSlot.__init__-260"><span class="linenos">260</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_result</span> <span class="o">=</span> <span class="n">result</span>
</span><span id="CoroSlot.__init__-261"><a href="#CoroSlot.__init__-261"><span class="linenos">261</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.implicit_coro_impl" class="classattr">
                                        <input id="CoroSlot.implicit_coro_impl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">implicit_coro_impl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">greenlet</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Coroutine</span><span class="p">,</span> <span class="n">Generator</span><span class="p">,</span> <span class="n">AsyncGenerator</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.implicit_coro_impl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.implicit_coro_impl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.implicit_coro_impl-267"><a href="#CoroSlot.implicit_coro_impl-267"><span class="linenos">267</span></a>    <span class="k">def</span> <span class="nf">implicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.implicit_coro_impl-268"><a href="#CoroSlot.implicit_coro_impl-268"><span class="linenos">268</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="CoroSlot.implicit_coro_impl-269"><a href="#CoroSlot.implicit_coro_impl-269"><span class="linenos">269</span></a>
</span><span id="CoroSlot.implicit_coro_impl-270"><a href="#CoroSlot.implicit_coro_impl-270"><span class="linenos">270</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="CoroSlot.implicit_coro_impl-271"><a href="#CoroSlot.implicit_coro_impl-271"><span class="linenos">271</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroSlot.implicit_coro_impl-272"><a href="#CoroSlot.implicit_coro_impl-272"><span class="linenos">272</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroSlot.implicit_coro_impl-273"><a href="#CoroSlot.implicit_coro_impl-273"><span class="linenos">273</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">cs_coro</span><span class="p">(</span><span class="n">coro</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="CoroSlot.implicit_coro_impl-274"><a href="#CoroSlot.implicit_coro_impl-274"><span class="linenos">274</span></a>        
</span><span id="CoroSlot.implicit_coro_impl-275"><a href="#CoroSlot.implicit_coro_impl-275"><span class="linenos">275</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot.implicit_coro_impl-276"><a href="#CoroSlot.implicit_coro_impl-276"><span class="linenos">276</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot.implicit_coro_impl-277"><a href="#CoroSlot.implicit_coro_impl-277"><span class="linenos">277</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">()),</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="CoroSlot.implicit_coro_impl-278"><a href="#CoroSlot.implicit_coro_impl-278"><span class="linenos">278</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.implicit_coro" class="classattr">
                                        <input id="CoroSlot.implicit_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">implicit_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroSlot.implicit_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.implicit_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.implicit_coro-280"><a href="#CoroSlot.implicit_coro-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">implicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroSlot.implicit_coro-281"><a href="#CoroSlot.implicit_coro-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.ic" class="classattr">
                                        <input id="CoroSlot.ic-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ic</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroSlot.ic-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.ic"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.ic-280"><a href="#CoroSlot.ic-280"><span class="linenos">280</span></a>    <span class="k">def</span> <span class="nf">implicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroSlot.ic-281"><a href="#CoroSlot.ic-281"><span class="linenos">281</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">implicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.gly_patched_function_impl" class="classattr">
                                        <input id="CoroSlot.gly_patched_function_impl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly_patched_function_impl</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.gly_patched_function_impl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.gly_patched_function_impl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.gly_patched_function_impl-285"><a href="#CoroSlot.gly_patched_function_impl-285"><span class="linenos">285</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.gly_patched_function_impl-286"><a href="#CoroSlot.gly_patched_function_impl-286"><span class="linenos">286</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">gly_patched</span><span class="p">(</span><span class="n">func</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.gly_patched_function" class="classattr">
                                        <input id="CoroSlot.gly_patched_function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gly_patched_function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.gly_patched_function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.gly_patched_function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.gly_patched_function-288"><a href="#CoroSlot.gly_patched_function-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.gly_patched_function-289"><a href="#CoroSlot.gly_patched_function-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.glypf" class="classattr">
                                        <input id="CoroSlot.glypf-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">glypf</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.glypf-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.glypf"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.glypf-288"><a href="#CoroSlot.glypf-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.glypf-289"><a href="#CoroSlot.glypf-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.gpf" class="classattr">
                                        <input id="CoroSlot.gpf-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gpf</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.gpf-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.gpf"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.gpf-288"><a href="#CoroSlot.gpf-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.gpf-289"><a href="#CoroSlot.gpf-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.gp" class="classattr">
                                        <input id="CoroSlot.gp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">gp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.gp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.gp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.gp-288"><a href="#CoroSlot.gp-288"><span class="linenos">288</span></a>    <span class="k">def</span> <span class="nf">gly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.gp-289"><a href="#CoroSlot.gp-289"><span class="linenos">289</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">gly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.agly_patched_function_impl" class="classattr">
                                        <input id="CoroSlot.agly_patched_function_impl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agly_patched_function_impl</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.agly_patched_function_impl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.agly_patched_function_impl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.agly_patched_function_impl-295"><a href="#CoroSlot.agly_patched_function_impl-295"><span class="linenos">295</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.agly_patched_function_impl-296"><a href="#CoroSlot.agly_patched_function_impl-296"><span class="linenos">296</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="fm">__call__</span><span class="p">(</span><span class="n">agly_patched</span><span class="p">(</span><span class="n">afunc</span><span class="p">))</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.agly_patched_function" class="classattr">
                                        <input id="CoroSlot.agly_patched_function-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agly_patched_function</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.agly_patched_function-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.agly_patched_function"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.agly_patched_function-298"><a href="#CoroSlot.agly_patched_function-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.agly_patched_function-299"><a href="#CoroSlot.agly_patched_function-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.aglypf" class="classattr">
                                        <input id="CoroSlot.aglypf-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">aglypf</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.aglypf-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.aglypf"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.aglypf-298"><a href="#CoroSlot.aglypf-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.aglypf-299"><a href="#CoroSlot.aglypf-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.agpf" class="classattr">
                                        <input id="CoroSlot.agpf-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agpf</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.agpf-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.agpf"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.agpf-298"><a href="#CoroSlot.agpf-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.agpf-299"><a href="#CoroSlot.agpf-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.agp" class="classattr">
                                        <input id="CoroSlot.agp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">agp</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.agp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.agp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.agp-298"><a href="#CoroSlot.agp-298"><span class="linenos">298</span></a>    <span class="k">def</span> <span class="nf">agly_patched_function</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.agp-299"><a href="#CoroSlot.agp-299"><span class="linenos">299</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">agly_patched_function_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.explicit_coro_impl" class="classattr">
                                        <input id="CoroSlot.explicit_coro_impl-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">explicit_coro_impl</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">coro</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">greenlet</span><span class="o">.</span><span class="n">greenlet</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">,</span> <span class="n">Coroutine</span><span class="p">,</span> <span class="n">Generator</span><span class="p">,</span> <span class="n">AsyncGenerator</span><span class="p">,</span> <span class="n">Callable</span><span class="p">]</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.explicit_coro_impl-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.explicit_coro_impl"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.explicit_coro_impl-305"><a href="#CoroSlot.explicit_coro_impl-305"><span class="linenos">305</span></a>    <span class="k">def</span> <span class="nf">explicit_coro_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.explicit_coro_impl-306"><a href="#CoroSlot.explicit_coro_impl-306"><span class="linenos">306</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_coro</span> <span class="o">=</span> <span class="n">coro</span>
</span><span id="CoroSlot.explicit_coro_impl-307"><a href="#CoroSlot.explicit_coro_impl-307"><span class="linenos">307</span></a>
</span><span id="CoroSlot.explicit_coro_impl-308"><a href="#CoroSlot.explicit_coro_impl-308"><span class="linenos">308</span></a>        <span class="k">def</span> <span class="nf">func_wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="CoroSlot.explicit_coro_impl-309"><a href="#CoroSlot.explicit_coro_impl-309"><span class="linenos">309</span></a>            <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroSlot.explicit_coro_impl-310"><a href="#CoroSlot.explicit_coro_impl-310"><span class="linenos">310</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="n">cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroSlot.explicit_coro_impl-311"><a href="#CoroSlot.explicit_coro_impl-311"><span class="linenos">311</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="CoroSlot.explicit_coro_impl-312"><a href="#CoroSlot.explicit_coro_impl-312"><span class="linenos">312</span></a>        
</span><span id="CoroSlot.explicit_coro_impl-313"><a href="#CoroSlot.explicit_coro_impl-313"><span class="linenos">313</span></a>        <span class="n">coro_worker_sign</span><span class="p">:</span> <span class="n">Signature</span> <span class="o">=</span> <span class="n">signature</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot.explicit_coro_impl-314"><a href="#CoroSlot.explicit_coro_impl-314"><span class="linenos">314</span></a>        <span class="n">update_wrapper</span><span class="p">(</span><span class="n">func_wrapper</span><span class="p">,</span> <span class="n">coro</span><span class="p">)</span>
</span><span id="CoroSlot.explicit_coro_impl-315"><a href="#CoroSlot.explicit_coro_impl-315"><span class="linenos">315</span></a>        <span class="n">func_wrapper</span><span class="o">.</span><span class="n">__signature__</span> <span class="o">=</span> <span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">parameters</span><span class="o">=</span><span class="nb">tuple</span><span class="p">(</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">parameters</span><span class="o">.</span><span class="n">values</span><span class="p">())[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">return_annotation</span><span class="o">=</span><span class="n">coro_worker_sign</span><span class="o">.</span><span class="n">return_annotation</span><span class="p">)</span>
</span><span id="CoroSlot.explicit_coro_impl-316"><a href="#CoroSlot.explicit_coro_impl-316"><span class="linenos">316</span></a>        <span class="k">return</span> <span class="n">pyqtSlot</span><span class="p">(</span><span class="o">*</span><span class="bp">self</span><span class="o">.</span><span class="n">_types</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_result</span><span class="p">)(</span><span class="n">func_wrapper</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.explicit_coro" class="classattr">
                                        <input id="CoroSlot.explicit_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">explicit_coro</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.explicit_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.explicit_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.explicit_coro-318"><a href="#CoroSlot.explicit_coro-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.explicit_coro-319"><a href="#CoroSlot.explicit_coro-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.ec" class="classattr">
                                        <input id="CoroSlot.ec-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">ec</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.ec-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.ec"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.ec-318"><a href="#CoroSlot.ec-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.ec-319"><a href="#CoroSlot.ec-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.interface" class="classattr">
                                        <input id="CoroSlot.interface-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">interface</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.interface-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.interface"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.interface-318"><a href="#CoroSlot.interface-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.interface-319"><a href="#CoroSlot.interface-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroSlot.i" class="classattr">
                                        <input id="CoroSlot.i-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">i</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="n">Any</span>:</span></span>

                <label class="view-source-button" for="CoroSlot.i-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroSlot.i"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroSlot.i-318"><a href="#CoroSlot.i-318"><span class="linenos">318</span></a>    <span class="k">def</span> <span class="nf">explicit_coro</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="CoroSlot.i-319"><a href="#CoroSlot.i-319"><span class="linenos">319</span></a>        <span class="k">return</span> <span class="n">partial</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">method</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">explicit_coro_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="CSlot">
                    <div class="attr variable">
            <span class="name">CSlot</span>        =
<span class="default_value">&lt;class &#39;<a href="#CoroSlot">CoroSlot</a>&#39;&gt;</span>

        
    </div>
    <a class="headerlink" href="#CSlot"></a>
    
    

                </section>
                <section id="coro_slot_implicit">
                            <input id="coro_slot_implicit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">coro_slot_implicit</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="coro_slot_implicit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#coro_slot_implicit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="coro_slot_implicit-329"><a href="#coro_slot_implicit-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">coro_slot_implicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="coro_slot_implicit-330"><a href="#coro_slot_implicit-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="coro_slot_implicit-331"><a href="#coro_slot_implicit-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">implicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="coro_slot_implicit-332"><a href="#coro_slot_implicit-332"><span class="linenos">332</span></a>    
</span><span id="coro_slot_implicit-333"><a href="#coro_slot_implicit-333"><span class="linenos">333</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslot_implicit">
                            <input id="cslot_implicit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslot_implicit</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslot_implicit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslot_implicit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslot_implicit-329"><a href="#cslot_implicit-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">coro_slot_implicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslot_implicit-330"><a href="#cslot_implicit-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslot_implicit-331"><a href="#cslot_implicit-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">implicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="cslot_implicit-332"><a href="#cslot_implicit-332"><span class="linenos">332</span></a>    
</span><span id="cslot_implicit-333"><a href="#cslot_implicit-333"><span class="linenos">333</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="csloti">
                            <input id="csloti-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">csloti</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="csloti-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#csloti"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="csloti-329"><a href="#csloti-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">coro_slot_implicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="csloti-330"><a href="#csloti-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="csloti-331"><a href="#csloti-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">implicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="csloti-332"><a href="#csloti-332"><span class="linenos">332</span></a>    
</span><span id="csloti-333"><a href="#csloti-333"><span class="linenos">333</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="csi">
                            <input id="csi-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">csi</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="csi-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#csi"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="csi-329"><a href="#csi-329"><span class="linenos">329</span></a><span class="k">def</span> <span class="nf">coro_slot_implicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="csi-330"><a href="#csi-330"><span class="linenos">330</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="csi-331"><a href="#csi-331"><span class="linenos">331</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">implicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="csi-332"><a href="#csi-332"><span class="linenos">332</span></a>    
</span><span id="csi-333"><a href="#csi-333"><span class="linenos">333</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="coro_slot_gly_patched">
                            <input id="coro_slot_gly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">coro_slot_gly_patched</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="coro_slot_gly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#coro_slot_gly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="coro_slot_gly_patched-340"><a href="#coro_slot_gly_patched-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="coro_slot_gly_patched-341"><a href="#coro_slot_gly_patched-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="coro_slot_gly_patched-342"><a href="#coro_slot_gly_patched-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="coro_slot_gly_patched-343"><a href="#coro_slot_gly_patched-343"><span class="linenos">343</span></a>    
</span><span id="coro_slot_gly_patched-344"><a href="#coro_slot_gly_patched-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslot_gly_patched">
                            <input id="cslot_gly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslot_gly_patched</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslot_gly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslot_gly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslot_gly_patched-340"><a href="#cslot_gly_patched-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslot_gly_patched-341"><a href="#cslot_gly_patched-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslot_gly_patched-342"><a href="#cslot_gly_patched-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="cslot_gly_patched-343"><a href="#cslot_gly_patched-343"><span class="linenos">343</span></a>    
</span><span id="cslot_gly_patched-344"><a href="#cslot_gly_patched-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslotglyp">
                            <input id="cslotglyp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslotglyp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslotglyp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslotglyp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslotglyp-340"><a href="#cslotglyp-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslotglyp-341"><a href="#cslotglyp-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslotglyp-342"><a href="#cslotglyp-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="cslotglyp-343"><a href="#cslotglyp-343"><span class="linenos">343</span></a>    
</span><span id="cslotglyp-344"><a href="#cslotglyp-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslotgp">
                            <input id="cslotgp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslotgp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslotgp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslotgp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslotgp-340"><a href="#cslotgp-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslotgp-341"><a href="#cslotgp-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslotgp-342"><a href="#cslotgp-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="cslotgp-343"><a href="#cslotgp-343"><span class="linenos">343</span></a>    
</span><span id="cslotgp-344"><a href="#cslotgp-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="csgp">
                            <input id="csgp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">csgp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="csgp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#csgp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="csgp-340"><a href="#csgp-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="csgp-341"><a href="#csgp-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="csgp-342"><a href="#csgp-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="csgp-343"><a href="#csgp-343"><span class="linenos">343</span></a>    
</span><span id="csgp-344"><a href="#csgp-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="coro_slot_agly_patched">
                            <input id="coro_slot_agly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">coro_slot_agly_patched</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="coro_slot_agly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#coro_slot_agly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="coro_slot_agly_patched-352"><a href="#coro_slot_agly_patched-352"><span class="linenos">352</span></a><span class="k">def</span> <span class="nf">coro_slot_agly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="coro_slot_agly_patched-353"><a href="#coro_slot_agly_patched-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="coro_slot_agly_patched-354"><a href="#coro_slot_agly_patched-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">agly_patched_function</span><span class="p">()(</span><span class="n">afunc</span><span class="p">)</span>
</span><span id="coro_slot_agly_patched-355"><a href="#coro_slot_agly_patched-355"><span class="linenos">355</span></a>    
</span><span id="coro_slot_agly_patched-356"><a href="#coro_slot_agly_patched-356"><span class="linenos">356</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslot_agly_patched">
                            <input id="cslot_agly_patched-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslot_agly_patched</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslot_agly_patched-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslot_agly_patched"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslot_agly_patched-352"><a href="#cslot_agly_patched-352"><span class="linenos">352</span></a><span class="k">def</span> <span class="nf">coro_slot_agly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslot_agly_patched-353"><a href="#cslot_agly_patched-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslot_agly_patched-354"><a href="#cslot_agly_patched-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">agly_patched_function</span><span class="p">()(</span><span class="n">afunc</span><span class="p">)</span>
</span><span id="cslot_agly_patched-355"><a href="#cslot_agly_patched-355"><span class="linenos">355</span></a>    
</span><span id="cslot_agly_patched-356"><a href="#cslot_agly_patched-356"><span class="linenos">356</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslotaglyp">
                            <input id="cslotaglyp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslotaglyp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslotaglyp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslotaglyp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslotaglyp-352"><a href="#cslotaglyp-352"><span class="linenos">352</span></a><span class="k">def</span> <span class="nf">coro_slot_agly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslotaglyp-353"><a href="#cslotaglyp-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslotaglyp-354"><a href="#cslotaglyp-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">agly_patched_function</span><span class="p">()(</span><span class="n">afunc</span><span class="p">)</span>
</span><span id="cslotaglyp-355"><a href="#cslotaglyp-355"><span class="linenos">355</span></a>    
</span><span id="cslotaglyp-356"><a href="#cslotaglyp-356"><span class="linenos">356</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslotagp">
                            <input id="cslotagp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslotagp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslotagp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslotagp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslotagp-352"><a href="#cslotagp-352"><span class="linenos">352</span></a><span class="k">def</span> <span class="nf">coro_slot_agly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslotagp-353"><a href="#cslotagp-353"><span class="linenos">353</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">afunc</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslotagp-354"><a href="#cslotagp-354"><span class="linenos">354</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">agly_patched_function</span><span class="p">()(</span><span class="n">afunc</span><span class="p">)</span>
</span><span id="cslotagp-355"><a href="#cslotagp-355"><span class="linenos">355</span></a>    
</span><span id="cslotagp-356"><a href="#cslotagp-356"><span class="linenos">356</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="csagp">
                            <input id="csagp-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">csagp</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="csagp-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#csagp"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="csagp-340"><a href="#csagp-340"><span class="linenos">340</span></a><span class="k">def</span> <span class="nf">coro_slot_gly_patched</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="csagp-341"><a href="#csagp-341"><span class="linenos">341</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="csagp-342"><a href="#csagp-342"><span class="linenos">342</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">gly_patched_function</span><span class="p">()(</span><span class="n">func</span><span class="p">)</span>
</span><span id="csagp-343"><a href="#csagp-343"><span class="linenos">343</span></a>    
</span><span id="csagp-344"><a href="#csagp-344"><span class="linenos">344</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="coro_slot_explicit">
                            <input id="coro_slot_explicit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">coro_slot_explicit</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="coro_slot_explicit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#coro_slot_explicit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="coro_slot_explicit-364"><a href="#coro_slot_explicit-364"><span class="linenos">364</span></a><span class="k">def</span> <span class="nf">coro_slot_explicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="coro_slot_explicit-365"><a href="#coro_slot_explicit-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="coro_slot_explicit-366"><a href="#coro_slot_explicit-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">explicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="coro_slot_explicit-367"><a href="#coro_slot_explicit-367"><span class="linenos">367</span></a>    
</span><span id="coro_slot_explicit-368"><a href="#coro_slot_explicit-368"><span class="linenos">368</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslot_explicit">
                            <input id="cslot_explicit-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslot_explicit</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslot_explicit-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslot_explicit"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslot_explicit-364"><a href="#cslot_explicit-364"><span class="linenos">364</span></a><span class="k">def</span> <span class="nf">coro_slot_explicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslot_explicit-365"><a href="#cslot_explicit-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslot_explicit-366"><a href="#cslot_explicit-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">explicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="cslot_explicit-367"><a href="#cslot_explicit-367"><span class="linenos">367</span></a>    
</span><span id="cslot_explicit-368"><a href="#cslot_explicit-368"><span class="linenos">368</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="cslotex">
                            <input id="cslotex-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">cslotex</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="cslotex-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#cslotex"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="cslotex-364"><a href="#cslotex-364"><span class="linenos">364</span></a><span class="k">def</span> <span class="nf">coro_slot_explicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="cslotex-365"><a href="#cslotex-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="cslotex-366"><a href="#cslotex-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">explicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="cslotex-367"><a href="#cslotex-367"><span class="linenos">367</span></a>    
</span><span id="cslotex-368"><a href="#cslotex-368"><span class="linenos">368</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="csex">
                            <input id="csex-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">csex</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span>,</span><span class="param">	<span class="n">name</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">result</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="csex-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#csex"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="csex-364"><a href="#csex-364"><span class="linenos">364</span></a><span class="k">def</span> <span class="nf">coro_slot_explicit</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">:</span> <span class="nb">type</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="csex-365"><a href="#csex-365"><span class="linenos">365</span></a>    <span class="k">def</span> <span class="nf">decorator</span><span class="p">(</span><span class="n">coro</span><span class="p">:</span> <span class="n">Coro</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Any</span><span class="p">:</span>
</span><span id="csex-366"><a href="#csex-366"><span class="linenos">366</span></a>        <span class="k">return</span> <span class="n">CoroSlot</span><span class="p">(</span><span class="o">*</span><span class="n">types</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">result</span><span class="p">)</span><span class="o">.</span><span class="n">explicit_coro</span><span class="p">()(</span><span class="n">coro</span><span class="p">)</span>
</span><span id="csex-367"><a href="#csex-367"><span class="linenos">367</span></a>    
</span><span id="csex-368"><a href="#csex-368"><span class="linenos">368</span></a>    <span class="k">return</span> <span class="n">decorator</span>
</span></pre></div>


    

                </section>
                <section id="qt_exec_in_coro">
                            <input id="qt_exec_in_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">qt_exec_in_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">func</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="qt_exec_in_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#qt_exec_in_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="qt_exec_in_coro-375"><a href="#qt_exec_in_coro-375"><span class="linenos">375</span></a><span class="k">def</span> <span class="nf">qt_exec_in_coro</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="qt_exec_in_coro-376"><a href="#qt_exec_in_coro-376"><span class="linenos">376</span></a>    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-377"><a href="#qt_exec_in_coro-377"><span class="linenos">377</span></a>    <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="qt_exec_in_coro-378"><a href="#qt_exec_in_coro-378"><span class="linenos">378</span></a>        <span class="n">cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="qt_exec_in_coro-379"><a href="#qt_exec_in_coro-379"><span class="linenos">379</span></a>        <span class="n">cs</span><span class="o">.</span><span class="n">high_cpu_utilisation_mode</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="qt_exec_in_coro-380"><a href="#qt_exec_in_coro-380"><span class="linenos">380</span></a>        <span class="n">cs</span><span class="o">.</span><span class="n">use_internal_sleep</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="qt_exec_in_coro-381"><a href="#qt_exec_in_coro-381"><span class="linenos">381</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="qt_exec_in_coro-382"><a href="#qt_exec_in_coro-382"><span class="linenos">382</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">use_higher_level_sleep_manager</span><span class="p">())</span>
</span><span id="qt_exec_in_coro-383"><a href="#qt_exec_in_coro-383"><span class="linenos">383</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="qt_exec_in_coro-384"><a href="#qt_exec_in_coro-384"><span class="linenos">384</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="qt_exec_in_coro-385"><a href="#qt_exec_in_coro-385"><span class="linenos">385</span></a>
</span><span id="qt_exec_in_coro-386"><a href="#qt_exec_in_coro-386"><span class="linenos">386</span></a>        <span class="n">app_or_tuple</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-387"><a href="#qt_exec_in_coro-387"><span class="linenos">387</span></a>        <span class="n">on_exit</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">ret</span><span class="p">:</span> <span class="n">ret</span>
</span><span id="qt_exec_in_coro-388"><a href="#qt_exec_in_coro-388"><span class="linenos">388</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="qt_exec_in_coro-389"><a href="#qt_exec_in_coro-389"><span class="linenos">389</span></a>            <span class="n">app</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="qt_exec_in_coro-390"><a href="#qt_exec_in_coro-390"><span class="linenos">390</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">):</span>
</span><span id="qt_exec_in_coro-391"><a href="#qt_exec_in_coro-391"><span class="linenos">391</span></a>            <span class="n">app</span><span class="p">,</span> <span class="n">on_exit</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="qt_exec_in_coro-392"><a href="#qt_exec_in_coro-392"><span class="linenos">392</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="qt_exec_in_coro-393"><a href="#qt_exec_in_coro-393"><span class="linenos">393</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s2">&quot;qt_exec_in_coro must return either QApplication or (QApplication, on_exit) tuple&quot;</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-394"><a href="#qt_exec_in_coro-394"><span class="linenos">394</span></a>        
</span><span id="qt_exec_in_coro-395"><a href="#qt_exec_in_coro-395"><span class="linenos">395</span></a>        <span class="c1"># Run the event loop</span>
</span><span id="qt_exec_in_coro-396"><a href="#qt_exec_in_coro-396"><span class="linenos">396</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">execa</span><span class="p">),</span> <span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-397"><a href="#qt_exec_in_coro-397"><span class="linenos">397</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">on_exit</span><span class="p">),</span> <span class="n">ret</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-398"><a href="#qt_exec_in_coro-398"><span class="linenos">398</span></a>        <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="qt_exec_in_coro-399"><a href="#qt_exec_in_coro-399"><span class="linenos">399</span></a>        <span class="k">return</span> <span class="n">ret</span>
</span><span id="qt_exec_in_coro-400"><a href="#qt_exec_in_coro-400"><span class="linenos">400</span></a>    
</span><span id="qt_exec_in_coro-401"><a href="#qt_exec_in_coro-401"><span class="linenos">401</span></a>    <span class="k">return</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">wrapper</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="aqt_exec_in_coro">
                            <input id="aqt_exec_in_coro-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aqt_exec_in_coro</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">func</span><span class="p">:</span> <span class="n">Callable</span>,</span><span class="param">	<span class="n">default_priority</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_standard_services</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">loop_yield</span><span class="o">.</span><span class="n">CoroPriority</span> <span class="o">=</span> <span class="o">&lt;</span><span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span></span><span class="return-annotation">) -> <span class="n">Callable</span>:</span></span>

                <label class="view-source-button" for="aqt_exec_in_coro-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#aqt_exec_in_coro"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="aqt_exec_in_coro-404"><a href="#aqt_exec_in_coro-404"><span class="linenos">404</span></a><span class="k">async</span> <span class="k">def</span> <span class="nf">aqt_exec_in_coro</span><span class="p">(</span><span class="n">func</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">:</span> <span class="n">CoroPriority</span> <span class="o">=</span> <span class="n">CoroPriority</span><span class="o">.</span><span class="n">normal</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Callable</span><span class="p">:</span>
</span><span id="aqt_exec_in_coro-405"><a href="#aqt_exec_in_coro-405"><span class="linenos">405</span></a>    <span class="nd">@wraps</span><span class="p">(</span><span class="n">func</span><span class="p">)</span>
</span><span id="aqt_exec_in_coro-406"><a href="#aqt_exec_in_coro-406"><span class="linenos">406</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">wrapper</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
</span><span id="aqt_exec_in_coro-407"><a href="#aqt_exec_in_coro-407"><span class="linenos">407</span></a>        <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span> <span class="o">=</span> <span class="n">current_interface</span><span class="p">()</span>
</span><span id="aqt_exec_in_coro-408"><a href="#aqt_exec_in_coro-408"><span class="linenos">408</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="aqt_exec_in_coro-409"><a href="#aqt_exec_in_coro-409"><span class="linenos">409</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="aqt_exec_in_coro-410"><a href="#aqt_exec_in_coro-410"><span class="linenos">410</span></a>
</span><span id="aqt_exec_in_coro-411"><a href="#aqt_exec_in_coro-411"><span class="linenos">411</span></a>        <span class="n">app_or_tuple</span> <span class="o">=</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="aqt_exec_in_coro-412"><a href="#aqt_exec_in_coro-412"><span class="linenos">412</span></a>        <span class="n">on_exit</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">ret</span><span class="p">:</span> <span class="n">ret</span>
</span><span id="aqt_exec_in_coro-413"><a href="#aqt_exec_in_coro-413"><span class="linenos">413</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">app_or_tuple</span><span class="p">,</span> <span class="n">QApplication</span><span class="p">):</span>
</span><span id="aqt_exec_in_coro-414"><a href="#aqt_exec_in_coro-414"><span class="linenos">414</span></a>            <span class="n">app</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="aqt_exec_in_coro-415"><a href="#aqt_exec_in_coro-415"><span class="linenos">415</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="aqt_exec_in_coro-416"><a href="#aqt_exec_in_coro-416"><span class="linenos">416</span></a>            <span class="n">app</span><span class="p">,</span> <span class="n">on_exit</span> <span class="o">=</span> <span class="n">app_or_tuple</span>
</span><span id="aqt_exec_in_coro-417"><a href="#aqt_exec_in_coro-417"><span class="linenos">417</span></a>        
</span><span id="aqt_exec_in_coro-418"><a href="#aqt_exec_in_coro-418"><span class="linenos">418</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">execa</span><span class="p">),</span> <span class="n">app</span><span class="p">,</span> <span class="n">default_priority</span><span class="p">)</span>
</span><span id="aqt_exec_in_coro-419"><a href="#aqt_exec_in_coro-419"><span class="linenos">419</span></a>        <span class="n">ret</span> <span class="o">=</span> <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">cs_coro</span><span class="p">(</span><span class="n">on_exit</span><span class="p">),</span> <span class="n">ret</span><span class="p">)</span>
</span><span id="aqt_exec_in_coro-420"><a href="#aqt_exec_in_coro-420"><span class="linenos">420</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="aqt_exec_in_coro-421"><a href="#aqt_exec_in_coro-421"><span class="linenos">421</span></a>        <span class="k">return</span> <span class="n">ret</span>
</span><span id="aqt_exec_in_coro-422"><a href="#aqt_exec_in_coro-422"><span class="linenos">422</span></a>    
</span><span id="aqt_exec_in_coro-423"><a href="#aqt_exec_in_coro-423"><span class="linenos">423</span></a>    <span class="k">return</span> <span class="n">cs_acoro</span><span class="p">(</span><span class="n">wrapper</span><span class="p">)</span>
</span></pre></div>


    

                </section>
                <section id="CoroThreadWorker">
                            <input id="CoroThreadWorker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroThreadWorker</span><wbr>(<span class="base">PyQt5.QtCore.QObject</span>):

                <label class="view-source-button" for="CoroThreadWorker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWorker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWorker-426"><a href="#CoroThreadWorker-426"><span class="linenos">426</span></a><span class="k">class</span> <span class="nc">CoroThreadWorker</span><span class="p">(</span><span class="n">QObject</span><span class="p">):</span>
</span><span id="CoroThreadWorker-427"><a href="#CoroThreadWorker-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWorker-428"><a href="#CoroThreadWorker-428"><span class="linenos">428</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="CoroThreadWorker-429"><a href="#CoroThreadWorker-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">:</span> <span class="n">AnyWorker</span> <span class="o">=</span> <span class="n">worker</span>
</span><span id="CoroThreadWorker-430"><a href="#CoroThreadWorker-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CoroThreadWorker-431"><a href="#CoroThreadWorker-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="CoroThreadWorker-432"><a href="#CoroThreadWorker-432"><span class="linenos">432</span></a>
</span><span id="CoroThreadWorker-433"><a href="#CoroThreadWorker-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWorker-434"><a href="#CoroThreadWorker-434"><span class="linenos">434</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="CoroThreadWorker-435"><a href="#CoroThreadWorker-435"><span class="linenos">435</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">my_worker_wrapper</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">worker</span><span class="p">):</span>
</span><span id="CoroThreadWorker-436"><a href="#CoroThreadWorker-436"><span class="linenos">436</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroThreadWorker-437"><a href="#CoroThreadWorker-437"><span class="linenos">437</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">)</span>
</span><span id="CoroThreadWorker-438"><a href="#CoroThreadWorker-438"><span class="linenos">438</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">worker</span><span class="p">)</span>
</span><span id="CoroThreadWorker-439"><a href="#CoroThreadWorker-439"><span class="linenos">439</span></a>        
</span><span id="CoroThreadWorker-440"><a href="#CoroThreadWorker-440"><span class="linenos">440</span></a>        <span class="n">run_in_loop</span><span class="p">(</span><span class="n">my_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">)</span>
</span><span id="CoroThreadWorker-441"><a href="#CoroThreadWorker-441"><span class="linenos">441</span></a>    
</span><span id="CoroThreadWorker-442"><a href="#CoroThreadWorker-442"><span class="linenos">442</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="CoroThreadWorker-443"><a href="#CoroThreadWorker-443"><span class="linenos">443</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="CoroThreadWorker-444"><a href="#CoroThreadWorker-444"><span class="linenos">444</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span><span id="CoroThreadWorker-445"><a href="#CoroThreadWorker-445"><span class="linenos">445</span></a>
</span><span id="CoroThreadWorker-446"><a href="#CoroThreadWorker-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWorker-447"><a href="#CoroThreadWorker-447"><span class="linenos">447</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span><span class="p">:</span>
</span><span id="CoroThreadWorker-448"><a href="#CoroThreadWorker-448"><span class="linenos">448</span></a>            <span class="k">return</span>
</span><span id="CoroThreadWorker-449"><a href="#CoroThreadWorker-449"><span class="linenos">449</span></a>
</span><span id="CoroThreadWorker-450"><a href="#CoroThreadWorker-450"><span class="linenos">450</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="CoroThreadWorker-451"><a href="#CoroThreadWorker-451"><span class="linenos">451</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="CoroThreadWorker-452"><a href="#CoroThreadWorker-452"><span class="linenos">452</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="CoroThreadWorker-453"><a href="#CoroThreadWorker-453"><span class="linenos">453</span></a>        
</span><span id="CoroThreadWorker-454"><a href="#CoroThreadWorker-454"><span class="linenos">454</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWorker-455"><a href="#CoroThreadWorker-455"><span class="linenos">455</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroThreadWorker-456"><a href="#CoroThreadWorker-456"><span class="linenos">456</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>QObject(parent: typing.Optional[QObject] = None)</p>
</div>


                            <div id="CoroThreadWorker.__init__" class="classattr">
                                        <input id="CoroThreadWorker.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CoroThreadWorker</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">worker</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]]]</span></span>)</span>

                <label class="view-source-button" for="CoroThreadWorker.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWorker.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWorker.__init__-427"><a href="#CoroThreadWorker.__init__-427"><span class="linenos">427</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWorker.__init__-428"><a href="#CoroThreadWorker.__init__-428"><span class="linenos">428</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="CoroThreadWorker.__init__-429"><a href="#CoroThreadWorker.__init__-429"><span class="linenos">429</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">:</span> <span class="n">AnyWorker</span> <span class="o">=</span> <span class="n">worker</span>
</span><span id="CoroThreadWorker.__init__-430"><a href="#CoroThreadWorker.__init__-430"><span class="linenos">430</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="p">:</span> <span class="n">CoroSchedulerType</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="CoroThreadWorker.__init__-431"><a href="#CoroThreadWorker.__init__-431"><span class="linenos">431</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroThreadWorker.allowed_to_run" class="classattr">
                                <div class="attr variable">
            <span class="name">allowed_to_run</span>

        
    </div>
    <a class="headerlink" href="#CoroThreadWorker.allowed_to_run"></a>
    
    

                            </div>
                            <div id="CoroThreadWorker.run" class="classattr">
                                        <input id="CoroThreadWorker.run-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">run</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroThreadWorker.run-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWorker.run"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWorker.run-433"><a href="#CoroThreadWorker.run-433"><span class="linenos">433</span></a>    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWorker.run-434"><a href="#CoroThreadWorker.run-434"><span class="linenos">434</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="CoroThreadWorker.run-435"><a href="#CoroThreadWorker.run-435"><span class="linenos">435</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">my_worker_wrapper</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">,</span> <span class="n">worker</span><span class="p">):</span>
</span><span id="CoroThreadWorker.run-436"><a href="#CoroThreadWorker.run-436"><span class="linenos">436</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="o">=</span> <span class="n">current_coro_scheduler</span><span class="p">()</span>
</span><span id="CoroThreadWorker.run-437"><a href="#CoroThreadWorker.run-437"><span class="linenos">437</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">)</span>
</span><span id="CoroThreadWorker.run-438"><a href="#CoroThreadWorker.run-438"><span class="linenos">438</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">RunCoro</span><span class="p">,</span> <span class="n">worker</span><span class="p">)</span>
</span><span id="CoroThreadWorker.run-439"><a href="#CoroThreadWorker.run-439"><span class="linenos">439</span></a>        
</span><span id="CoroThreadWorker.run-440"><a href="#CoroThreadWorker.run-440"><span class="linenos">440</span></a>        <span class="n">run_in_loop</span><span class="p">(</span><span class="n">my_worker_wrapper</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_worker</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroThreadWorker.setup" class="classattr">
                                        <input id="CoroThreadWorker.setup-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">setup</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">i</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroThreadWorker.setup-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWorker.setup"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWorker.setup-442"><a href="#CoroThreadWorker.setup-442"><span class="linenos">442</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="CoroThreadWorker.setup-443"><a href="#CoroThreadWorker.setup-443"><span class="linenos">443</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">ensure_loop</span><span class="p">(</span><span class="n">interrupt_when_no_requests</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</span><span id="CoroThreadWorker.setup-444"><a href="#CoroThreadWorker.setup-444"><span class="linenos">444</span></a>        <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">AsyncioLoopRequest</span><span class="p">()</span><span class="o">.</span><span class="n">turn_on_loops_intercommunication</span><span class="p">())</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroThreadWorker.stop" class="classattr">
                                        <input id="CoroThreadWorker.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroThreadWorker.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWorker.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWorker.stop-446"><a href="#CoroThreadWorker.stop-446"><span class="linenos">446</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWorker.stop-447"><a href="#CoroThreadWorker.stop-447"><span class="linenos">447</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span><span class="p">:</span>
</span><span id="CoroThreadWorker.stop-448"><a href="#CoroThreadWorker.stop-448"><span class="linenos">448</span></a>            <span class="k">return</span>
</span><span id="CoroThreadWorker.stop-449"><a href="#CoroThreadWorker.stop-449"><span class="linenos">449</span></a>
</span><span id="CoroThreadWorker.stop-450"><a href="#CoroThreadWorker.stop-450"><span class="linenos">450</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">allowed_to_run</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="CoroThreadWorker.stop-451"><a href="#CoroThreadWorker.stop-451"><span class="linenos">451</span></a>        <span class="k">async</span> <span class="k">def</span> <span class="nf">coro</span><span class="p">(</span><span class="n">i</span><span class="p">:</span> <span class="n">Interface</span><span class="p">):</span>
</span><span id="CoroThreadWorker.stop-452"><a href="#CoroThreadWorker.stop-452"><span class="linenos">452</span></a>            <span class="k">await</span> <span class="n">i</span><span class="p">(</span><span class="n">ShutdownLoop</span><span class="p">)</span>
</span><span id="CoroThreadWorker.stop-453"><a href="#CoroThreadWorker.stop-453"><span class="linenos">453</span></a>        
</span><span id="CoroThreadWorker.stop-454"><a href="#CoroThreadWorker.stop-454"><span class="linenos">454</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWorker.stop-455"><a href="#CoroThreadWorker.stop-455"><span class="linenos">455</span></a>            <span class="n">service</span><span class="p">:</span> <span class="n">PutCoro</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cs</span><span class="o">.</span><span class="n">get_service_instance</span><span class="p">(</span><span class="n">PutCoro</span><span class="p">)</span>
</span><span id="CoroThreadWorker.stop-456"><a href="#CoroThreadWorker.stop-456"><span class="linenos">456</span></a>            <span class="k">return</span> <span class="n">service</span><span class="o">.</span><span class="n">_add_direct_request</span><span class="p">(</span><span class="n">coro</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>PyQt5.QtCore.QObject</dt>
                                <dd id="CoroThreadWorker.blockSignals" class="function">blockSignals</dd>
                <dd id="CoroThreadWorker.childEvent" class="function">childEvent</dd>
                <dd id="CoroThreadWorker.children" class="function">children</dd>
                <dd id="CoroThreadWorker.connectNotify" class="function">connectNotify</dd>
                <dd id="CoroThreadWorker.customEvent" class="function">customEvent</dd>
                <dd id="CoroThreadWorker.deleteLater" class="function">deleteLater</dd>
                <dd id="CoroThreadWorker.disconnect" class="function">disconnect</dd>
                <dd id="CoroThreadWorker.disconnectNotify" class="function">disconnectNotify</dd>
                <dd id="CoroThreadWorker.dumpObjectInfo" class="function">dumpObjectInfo</dd>
                <dd id="CoroThreadWorker.dumpObjectTree" class="function">dumpObjectTree</dd>
                <dd id="CoroThreadWorker.dynamicPropertyNames" class="function">dynamicPropertyNames</dd>
                <dd id="CoroThreadWorker.event" class="function">event</dd>
                <dd id="CoroThreadWorker.eventFilter" class="function">eventFilter</dd>
                <dd id="CoroThreadWorker.findChild" class="function">findChild</dd>
                <dd id="CoroThreadWorker.findChildren" class="function">findChildren</dd>
                <dd id="CoroThreadWorker.inherits" class="function">inherits</dd>
                <dd id="CoroThreadWorker.installEventFilter" class="function">installEventFilter</dd>
                <dd id="CoroThreadWorker.isSignalConnected" class="function">isSignalConnected</dd>
                <dd id="CoroThreadWorker.isWidgetType" class="function">isWidgetType</dd>
                <dd id="CoroThreadWorker.isWindowType" class="function">isWindowType</dd>
                <dd id="CoroThreadWorker.killTimer" class="function">killTimer</dd>
                <dd id="CoroThreadWorker.metaObject" class="function">metaObject</dd>
                <dd id="CoroThreadWorker.moveToThread" class="function">moveToThread</dd>
                <dd id="CoroThreadWorker.objectName" class="function">objectName</dd>
                <dd id="CoroThreadWorker.parent" class="function">parent</dd>
                <dd id="CoroThreadWorker.property" class="function">property</dd>
                <dd id="CoroThreadWorker.pyqtConfigure" class="function">pyqtConfigure</dd>
                <dd id="CoroThreadWorker.receivers" class="function">receivers</dd>
                <dd id="CoroThreadWorker.removeEventFilter" class="function">removeEventFilter</dd>
                <dd id="CoroThreadWorker.sender" class="function">sender</dd>
                <dd id="CoroThreadWorker.senderSignalIndex" class="function">senderSignalIndex</dd>
                <dd id="CoroThreadWorker.setObjectName" class="function">setObjectName</dd>
                <dd id="CoroThreadWorker.setParent" class="function">setParent</dd>
                <dd id="CoroThreadWorker.setProperty" class="function">setProperty</dd>
                <dd id="CoroThreadWorker.signalsBlocked" class="function">signalsBlocked</dd>
                <dd id="CoroThreadWorker.startTimer" class="function">startTimer</dd>
                <dd id="CoroThreadWorker.thread" class="function">thread</dd>
                <dd id="CoroThreadWorker.timerEvent" class="function">timerEvent</dd>
                <dd id="CoroThreadWorker.tr" class="function">tr</dd>
                <dd id="CoroThreadWorker.staticMetaObject" class="variable">staticMetaObject</dd>
                <dd id="CoroThreadWorker.objectNameChanged" class="function">objectNameChanged</dd>
                <dd id="CoroThreadWorker.destroyed" class="function">destroyed</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="CoroThreadWithWorker">
                            <input id="CoroThreadWithWorker-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">CoroThreadWithWorker</span><wbr>(<span class="base"><a href="#CoroThreadWorker">CoroThreadWorker</a></span>):

                <label class="view-source-button" for="CoroThreadWithWorker-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWithWorker"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWithWorker-471"><a href="#CoroThreadWithWorker-471"><span class="linenos">471</span></a><span class="k">class</span> <span class="nc">CoroThreadWithWorker</span><span class="p">(</span><span class="n">CoroThreadWorker</span><span class="p">):</span>
</span><span id="CoroThreadWithWorker-472"><a href="#CoroThreadWithWorker-472"><span class="linenos">472</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWithWorker-473"><a href="#CoroThreadWithWorker-473"><span class="linenos">473</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">worker</span><span class="p">)</span>
</span><span id="CoroThreadWithWorker-474"><a href="#CoroThreadWithWorker-474"><span class="linenos">474</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="p">:</span> <span class="n">CoroThread</span> <span class="o">=</span> <span class="n">CoroThread</span><span class="p">(</span><span class="n">parent</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span><span id="CoroThreadWithWorker-475"><a href="#CoroThreadWithWorker-475"><span class="linenos">475</span></a>    
</span><span id="CoroThreadWithWorker-476"><a href="#CoroThreadWithWorker-476"><span class="linenos">476</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWithWorker-477"><a href="#CoroThreadWithWorker-477"><span class="linenos">477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span><span id="CoroThreadWithWorker-478"><a href="#CoroThreadWithWorker-478"><span class="linenos">478</span></a>    
</span><span id="CoroThreadWithWorker-479"><a href="#CoroThreadWithWorker-479"><span class="linenos">479</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWithWorker-480"><a href="#CoroThreadWithWorker-480"><span class="linenos">480</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="CoroThreadWithWorker-481"><a href="#CoroThreadWithWorker-481"><span class="linenos">481</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>QObject(parent: typing.Optional[QObject] = None)</p>
</div>


                            <div id="CoroThreadWithWorker.__init__" class="classattr">
                                        <input id="CoroThreadWithWorker.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">CoroThreadWithWorker</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">parent</span>,</span><span class="param">	<span class="n">worker</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">ExplicitWorker</span><span class="p">,</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Any</span><span class="p">],</span> <span class="n">collections</span><span class="o">.</span><span class="n">abc</span><span class="o">.</span><span class="n">Callable</span><span class="p">[</span><span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">coroutines</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">coro_scheduler</span><span class="o">.</span><span class="n">Interface</span><span class="p">,</span> <span class="n">Awaitable</span><span class="p">[</span><span class="n">Any</span><span class="p">]]]</span></span>)</span>

                <label class="view-source-button" for="CoroThreadWithWorker.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWithWorker.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWithWorker.__init__-472"><a href="#CoroThreadWithWorker.__init__-472"><span class="linenos">472</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">,</span> <span class="n">worker</span><span class="p">:</span> <span class="n">AnyWorker</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="CoroThreadWithWorker.__init__-473"><a href="#CoroThreadWithWorker.__init__-473"><span class="linenos">473</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">worker</span><span class="p">)</span>
</span><span id="CoroThreadWithWorker.__init__-474"><a href="#CoroThreadWithWorker.__init__-474"><span class="linenos">474</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="p">:</span> <span class="n">CoroThread</span> <span class="o">=</span> <span class="n">CoroThread</span><span class="p">(</span><span class="n">parent</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroThreadWithWorker.start" class="classattr">
                                        <input id="CoroThreadWithWorker.start-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroThreadWithWorker.start-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWithWorker.start"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWithWorker.start-476"><a href="#CoroThreadWithWorker.start-476"><span class="linenos">476</span></a>    <span class="k">def</span> <span class="nf">start</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWithWorker.start-477"><a href="#CoroThreadWithWorker.start-477"><span class="linenos">477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="CoroThreadWithWorker.stop" class="classattr">
                                        <input id="CoroThreadWithWorker.stop-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">stop</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="CoroThreadWithWorker.stop-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#CoroThreadWithWorker.stop"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="CoroThreadWithWorker.stop-479"><a href="#CoroThreadWithWorker.stop-479"><span class="linenos">479</span></a>    <span class="k">def</span> <span class="nf">stop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="CoroThreadWithWorker.stop-480"><a href="#CoroThreadWithWorker.stop-480"><span class="linenos">480</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span><span id="CoroThreadWithWorker.stop-481"><a href="#CoroThreadWithWorker.stop-481"><span class="linenos">481</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_thread</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt><a href="#CoroThreadWorker">CoroThreadWorker</a></dt>
                                <dd id="CoroThreadWithWorker.allowed_to_run" class="variable"><a href="#CoroThreadWorker.allowed_to_run">allowed_to_run</a></dd>
                <dd id="CoroThreadWithWorker.run" class="function"><a href="#CoroThreadWorker.run">run</a></dd>
                <dd id="CoroThreadWithWorker.setup" class="function"><a href="#CoroThreadWorker.setup">setup</a></dd>

            </div>
            <div><dt>PyQt5.QtCore.QObject</dt>
                                <dd id="CoroThreadWithWorker.blockSignals" class="function">blockSignals</dd>
                <dd id="CoroThreadWithWorker.childEvent" class="function">childEvent</dd>
                <dd id="CoroThreadWithWorker.children" class="function">children</dd>
                <dd id="CoroThreadWithWorker.connectNotify" class="function">connectNotify</dd>
                <dd id="CoroThreadWithWorker.customEvent" class="function">customEvent</dd>
                <dd id="CoroThreadWithWorker.deleteLater" class="function">deleteLater</dd>
                <dd id="CoroThreadWithWorker.disconnect" class="function">disconnect</dd>
                <dd id="CoroThreadWithWorker.disconnectNotify" class="function">disconnectNotify</dd>
                <dd id="CoroThreadWithWorker.dumpObjectInfo" class="function">dumpObjectInfo</dd>
                <dd id="CoroThreadWithWorker.dumpObjectTree" class="function">dumpObjectTree</dd>
                <dd id="CoroThreadWithWorker.dynamicPropertyNames" class="function">dynamicPropertyNames</dd>
                <dd id="CoroThreadWithWorker.event" class="function">event</dd>
                <dd id="CoroThreadWithWorker.eventFilter" class="function">eventFilter</dd>
                <dd id="CoroThreadWithWorker.findChild" class="function">findChild</dd>
                <dd id="CoroThreadWithWorker.findChildren" class="function">findChildren</dd>
                <dd id="CoroThreadWithWorker.inherits" class="function">inherits</dd>
                <dd id="CoroThreadWithWorker.installEventFilter" class="function">installEventFilter</dd>
                <dd id="CoroThreadWithWorker.isSignalConnected" class="function">isSignalConnected</dd>
                <dd id="CoroThreadWithWorker.isWidgetType" class="function">isWidgetType</dd>
                <dd id="CoroThreadWithWorker.isWindowType" class="function">isWindowType</dd>
                <dd id="CoroThreadWithWorker.killTimer" class="function">killTimer</dd>
                <dd id="CoroThreadWithWorker.metaObject" class="function">metaObject</dd>
                <dd id="CoroThreadWithWorker.moveToThread" class="function">moveToThread</dd>
                <dd id="CoroThreadWithWorker.objectName" class="function">objectName</dd>
                <dd id="CoroThreadWithWorker.parent" class="function">parent</dd>
                <dd id="CoroThreadWithWorker.property" class="function">property</dd>
                <dd id="CoroThreadWithWorker.pyqtConfigure" class="function">pyqtConfigure</dd>
                <dd id="CoroThreadWithWorker.receivers" class="function">receivers</dd>
                <dd id="CoroThreadWithWorker.removeEventFilter" class="function">removeEventFilter</dd>
                <dd id="CoroThreadWithWorker.sender" class="function">sender</dd>
                <dd id="CoroThreadWithWorker.senderSignalIndex" class="function">senderSignalIndex</dd>
                <dd id="CoroThreadWithWorker.setObjectName" class="function">setObjectName</dd>
                <dd id="CoroThreadWithWorker.setParent" class="function">setParent</dd>
                <dd id="CoroThreadWithWorker.setProperty" class="function">setProperty</dd>
                <dd id="CoroThreadWithWorker.signalsBlocked" class="function">signalsBlocked</dd>
                <dd id="CoroThreadWithWorker.startTimer" class="function">startTimer</dd>
                <dd id="CoroThreadWithWorker.thread" class="function">thread</dd>
                <dd id="CoroThreadWithWorker.timerEvent" class="function">timerEvent</dd>
                <dd id="CoroThreadWithWorker.tr" class="function">tr</dd>
                <dd id="CoroThreadWithWorker.staticMetaObject" class="variable">staticMetaObject</dd>
                <dd id="CoroThreadWithWorker.objectNameChanged" class="function">objectNameChanged</dd>
                <dd id="CoroThreadWithWorker.destroyed" class="function">destroyed</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>