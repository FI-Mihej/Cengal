---
title: tcp_efficient_streams
---

<div>
    <main class="pdoc">
            <section class="module-info">
                    <h1 class="modulename">
cengal<wbr>.parallel_execution<wbr>.asyncio<wbr>.efficient_streams<wbr>.versions<wbr>.v_0<wbr>.tcp_efficient_streams    </h1>

                        <div class="docstring"><p>Module Docstring
Docstrings: <a href="http://www.python.org/dev/peps/pep-0257/">http://www.python.org/dev/peps/pep-0257/</a></p>
</div>

                        <input id="mod-tcp_efficient_streams-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">

                        <label class="view-source-button" for="mod-tcp_efficient_streams-view-source"><span>View Source</span></label>

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
</span><span id="L-18"><a href="#L-18"><span class="linenos">  18</span></a>
</span><span id="L-19"><a href="#L-19"><span class="linenos">  19</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-20"><a href="#L-20"><span class="linenos">  20</span></a><span class="sd">Module Docstring</span>
</span><span id="L-21"><a href="#L-21"><span class="linenos">  21</span></a><span class="sd">Docstrings: http://www.python.org/dev/peps/pep-0257/</span>
</span><span id="L-22"><a href="#L-22"><span class="linenos">  22</span></a><span class="sd">&quot;&quot;&quot;</span>
</span><span id="L-23"><a href="#L-23"><span class="linenos">  23</span></a>
</span><span id="L-24"><a href="#L-24"><span class="linenos">  24</span></a>
</span><span id="L-25"><a href="#L-25"><span class="linenos">  25</span></a><span class="n">__author__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-26"><a href="#L-26"><span class="linenos">  26</span></a><span class="n">__copyright__</span> <span class="o">=</span> <span class="s2">&quot;Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-27"><a href="#L-27"><span class="linenos">  27</span></a><span class="n">__credits__</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span><span class="p">,</span> <span class="p">]</span>
</span><span id="L-28"><a href="#L-28"><span class="linenos">  28</span></a><span class="n">__license__</span> <span class="o">=</span> <span class="s2">&quot;Apache License, Version 2.0&quot;</span>
</span><span id="L-29"><a href="#L-29"><span class="linenos">  29</span></a><span class="n">__version__</span> <span class="o">=</span> <span class="s2">&quot;4.4.1&quot;</span>
</span><span id="L-30"><a href="#L-30"><span class="linenos">  30</span></a><span class="n">__maintainer__</span> <span class="o">=</span> <span class="s2">&quot;ButenkoMS &lt;gtalk@butenkoms.space&gt;&quot;</span>
</span><span id="L-31"><a href="#L-31"><span class="linenos">  31</span></a><span class="n">__email__</span> <span class="o">=</span> <span class="s2">&quot;gtalk@butenkoms.space&quot;</span>
</span><span id="L-32"><a href="#L-32"><span class="linenos">  32</span></a><span class="c1"># __status__ = &quot;Prototype&quot;</span>
</span><span id="L-33"><a href="#L-33"><span class="linenos">  33</span></a><span class="n">__status__</span> <span class="o">=</span> <span class="s2">&quot;Development&quot;</span>
</span><span id="L-34"><a href="#L-34"><span class="linenos">  34</span></a><span class="c1"># __status__ = &quot;Production&quot;</span>
</span><span id="L-35"><a href="#L-35"><span class="linenos">  35</span></a>
</span><span id="L-36"><a href="#L-36"><span class="linenos">  36</span></a>
</span><span id="L-37"><a href="#L-37"><span class="linenos">  37</span></a><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;StreamType&#39;</span><span class="p">,</span> <span class="s1">&#39;GateSecurityPolicy&#39;</span><span class="p">,</span> <span class="s1">&#39;StreamManagerIOCoreMemoryManagement&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamManager&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamReaderProtocol&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]</span>
</span><span id="L-38"><a href="#L-38"><span class="linenos">  38</span></a>
</span><span id="L-39"><a href="#L-39"><span class="linenos">  39</span></a>
</span><span id="L-40"><a href="#L-40"><span class="linenos">  40</span></a><span class="kn">import</span> <span class="nn">warnings</span>
</span><span id="L-41"><a href="#L-41"><span class="linenos">  41</span></a><span class="kn">import</span> <span class="nn">asyncio</span>
</span><span id="L-42"><a href="#L-42"><span class="linenos">  42</span></a><span class="kn">from</span> <span class="nn">asyncio.exceptions</span> <span class="kn">import</span> <span class="n">IncompleteReadError</span><span class="p">,</span> <span class="n">LimitOverrunError</span>
</span><span id="L-43"><a href="#L-43"><span class="linenos">  43</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">streams</span>
</span><span id="L-44"><a href="#L-44"><span class="linenos">  44</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamWriter</span> <span class="k">as</span> <span class="n">OriginalStreamWriter</span>
</span><span id="L-45"><a href="#L-45"><span class="linenos">  45</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamReader</span> <span class="k">as</span> <span class="n">OriginalStreamReader</span>
</span><span id="L-46"><a href="#L-46"><span class="linenos">  46</span></a><span class="kn">from</span> <span class="nn">asyncio.streams</span> <span class="kn">import</span> <span class="n">StreamReaderProtocol</span> <span class="k">as</span> <span class="n">OriginalStreamReaderProtocol</span>
</span><span id="L-47"><a href="#L-47"><span class="linenos">  47</span></a><span class="kn">from</span> <span class="nn">asyncio.sslproto</span> <span class="kn">import</span> <span class="n">SSLProtocol</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span>
</span><span id="L-48"><a href="#L-48"><span class="linenos">  48</span></a><span class="kn">from</span> <span class="nn">asyncio.proactor_events</span> <span class="kn">import</span> <span class="n">_ProactorSocketTransport</span>
</span><span id="L-49"><a href="#L-49"><span class="linenos">  49</span></a><span class="kn">from</span> <span class="nn">asyncio.selector_events</span> <span class="kn">import</span> <span class="n">_SelectorSocketTransport</span>
</span><span id="L-50"><a href="#L-50"><span class="linenos">  50</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">events</span>
</span><span id="L-51"><a href="#L-51"><span class="linenos">  51</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">proactor_events</span>
</span><span id="L-52"><a href="#L-52"><span class="linenos">  52</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">selector_events</span>
</span><span id="L-53"><a href="#L-53"><span class="linenos">  53</span></a><span class="k">try</span><span class="p">:</span>
</span><span id="L-54"><a href="#L-54"><span class="linenos">  54</span></a>    <span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">unix_events</span>
</span><span id="L-55"><a href="#L-55"><span class="linenos">  55</span></a><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
</span><span id="L-56"><a href="#L-56"><span class="linenos">  56</span></a>    <span class="k">pass</span>
</span><span id="L-57"><a href="#L-57"><span class="linenos">  57</span></a>
</span><span id="L-58"><a href="#L-58"><span class="linenos">  58</span></a><span class="kn">from</span> <span class="nn">asyncio</span> <span class="kn">import</span> <span class="n">coroutines</span>
</span><span id="L-59"><a href="#L-59"><span class="linenos">  59</span></a><span class="kn">from</span> <span class="nn">asyncio.tasks</span> <span class="kn">import</span> <span class="n">sleep</span><span class="p">,</span> <span class="n">Task</span>
</span><span id="L-60"><a href="#L-60"><span class="linenos">  60</span></a><span class="kn">from</span> <span class="nn">asyncio.futures</span> <span class="kn">import</span> <span class="n">Future</span>
</span><span id="L-61"><a href="#L-61"><span class="linenos">  61</span></a><span class="kn">from</span> <span class="nn">copy</span> <span class="kn">import</span> <span class="n">copy</span>
</span><span id="L-62"><a href="#L-62"><span class="linenos">  62</span></a><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
</span><span id="L-63"><a href="#L-63"><span class="linenos">  63</span></a><span class="kn">from</span> <span class="nn">cengal.io.asock_io.versions.v_1.recv_buff_size_computer.recv_buff_size_computer__python</span> <span class="kn">import</span> <span class="n">RecvBuffSizeComputer</span>
</span><span id="L-64"><a href="#L-64"><span class="linenos">  64</span></a><span class="c1"># from cengal.io.asock_io.versions.v_1.base import IOCoreMemoryManagement</span>
</span><span id="L-65"><a href="#L-65"><span class="linenos">  65</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.atasks</span> <span class="kn">import</span> <span class="n">create_task</span>
</span><span id="L-66"><a href="#L-66"><span class="linenos">  66</span></a><span class="kn">from</span> <span class="nn">cengal.parallel_execution.asyncio.timed_yield</span> <span class="kn">import</span> <span class="n">TimedYield</span>
</span><span id="L-67"><a href="#L-67"><span class="linenos">  67</span></a><span class="kn">from</span> <span class="nn">cengal.hardware.cpu.info</span> <span class="kn">import</span> <span class="n">cpu_info</span>
</span><span id="L-68"><a href="#L-68"><span class="linenos">  68</span></a><span class="c1"># from cengal.data_containers.dynamic_list_of_pieces import DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-69"><a href="#L-69"><span class="linenos">  69</span></a><span class="c1"># from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl, FIFOIsEmpty</span>
</span><span id="L-70"><a href="#L-70"><span class="linenos">  70</span></a><span class="c1"># from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariable, FrontTriggerableVariableType</span>
</span><span id="L-71"><a href="#L-71"><span class="linenos">  71</span></a><span class="kn">from</span> <span class="nn">cengal.data_containers.dynamic_list_of_pieces.versions.v_1.dynamic_list_of_pieces__python</span> <span class="kn">import</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-72"><a href="#L-72"><span class="linenos">  72</span></a><span class="kn">from</span> <span class="nn">cengal.code_flow_control.smart_values.versions</span> <span class="kn">import</span> <span class="n">ValueExistence</span>
</span><span id="L-73"><a href="#L-73"><span class="linenos">  73</span></a><span class="kn">from</span> <span class="nn">cengal.data_manipulation.conversion.reinterpret_cast</span> <span class="kn">import</span> <span class="n">reinterpret_cast</span>
</span><span id="L-74"><a href="#L-74"><span class="linenos">  74</span></a><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">Sequence</span><span class="p">,</span> <span class="n">Tuple</span><span class="p">,</span> <span class="n">Type</span><span class="p">,</span> <span class="n">Set</span><span class="p">,</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Union</span><span class="p">,</span> <span class="n">List</span><span class="p">,</span> <span class="n">cast</span>
</span><span id="L-75"><a href="#L-75"><span class="linenos">  75</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_base_internal</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-76"><a href="#L-76"><span class="linenos">  76</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_base</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-77"><a href="#L-77"><span class="linenos">  77</span></a><span class="kn">from</span> <span class="nn">.efficient_streams_abstract</span> <span class="kn">import</span> <span class="o">*</span>
</span><span id="L-78"><a href="#L-78"><span class="linenos">  78</span></a>
</span><span id="L-79"><a href="#L-79"><span class="linenos">  79</span></a><span class="kn">from</span> <span class="nn">contextlib</span> <span class="kn">import</span> <span class="n">asynccontextmanager</span>
</span><span id="L-80"><a href="#L-80"><span class="linenos">  80</span></a>
</span><span id="L-81"><a href="#L-81"><span class="linenos">  81</span></a>
</span><span id="L-82"><a href="#L-82"><span class="linenos">  82</span></a><span class="k">class</span> <span class="nc">TcpStreamManager</span><span class="p">(</span><span class="n">StreamManagerAbstract</span><span class="p">):</span>
</span><span id="L-83"><a href="#L-83"><span class="linenos">  83</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-84"><a href="#L-84"><span class="linenos">  84</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">io_memory_management</span><span class="p">:</span> <span class="n">StreamManagerIOCoreMemoryManagement</span> <span class="o">=</span> <span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">()</span>
</span><span id="L-85"><a href="#L-85"><span class="linenos">  85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mf">10.0</span>
</span><span id="L-86"><a href="#L-86"><span class="linenos">  86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-87"><a href="#L-87"><span class="linenos">  87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="L-88"><a href="#L-88"><span class="linenos">  88</span></a>
</span><span id="L-89"><a href="#L-89"><span class="linenos">  89</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="L-90"><a href="#L-90"><span class="linenos">  90</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-91"><a href="#L-91"><span class="linenos">  91</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-92"><a href="#L-92"><span class="linenos">  92</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-93"><a href="#L-93"><span class="linenos">  93</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-94"><a href="#L-94"><span class="linenos">  94</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="L-95"><a href="#L-95"><span class="linenos">  95</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="L-96"><a href="#L-96"><span class="linenos">  96</span></a>
</span><span id="L-97"><a href="#L-97"><span class="linenos">  97</span></a><span class="sd">        The reader returned is a TcpStreamReader instance; the writer is a</span>
</span><span id="L-98"><a href="#L-98"><span class="linenos">  98</span></a><span class="sd">        TcpStreamWriter instance.</span>
</span><span id="L-99"><a href="#L-99"><span class="linenos">  99</span></a>
</span><span id="L-100"><a href="#L-100"><span class="linenos"> 100</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="L-101"><a href="#L-101"><span class="linenos"> 101</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="L-102"><a href="#L-102"><span class="linenos"> 102</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="L-103"><a href="#L-103"><span class="linenos"> 103</span></a>
</span><span id="L-104"><a href="#L-104"><span class="linenos"> 104</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="L-105"><a href="#L-105"><span class="linenos"> 105</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="L-106"><a href="#L-106"><span class="linenos"> 106</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="L-107"><a href="#L-107"><span class="linenos"> 107</span></a>
</span><span id="L-108"><a href="#L-108"><span class="linenos"> 108</span></a><span class="sd">        (If you want to customize the TcpStreamReader and/or</span>
</span><span id="L-109"><a href="#L-109"><span class="linenos"> 109</span></a><span class="sd">        TcpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="L-110"><a href="#L-110"><span class="linenos"> 110</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="L-111"><a href="#L-111"><span class="linenos"> 111</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-112"><a href="#L-112"><span class="linenos"> 112</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="L-113"><a href="#L-113"><span class="linenos"> 113</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="L-114"><a href="#L-114"><span class="linenos"> 114</span></a>        
</span><span id="L-115"><a href="#L-115"><span class="linenos"> 115</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-116"><a href="#L-116"><span class="linenos"> 116</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-117"><a href="#L-117"><span class="linenos"> 117</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-118"><a href="#L-118"><span class="linenos"> 118</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="L-119"><a href="#L-119"><span class="linenos"> 119</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="L-120"><a href="#L-120"><span class="linenos"> 120</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-121"><a href="#L-121"><span class="linenos"> 121</span></a>        
</span><span id="L-122"><a href="#L-122"><span class="linenos"> 122</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-123"><a href="#L-123"><span class="linenos"> 123</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-124"><a href="#L-124"><span class="linenos"> 124</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-125"><a href="#L-125"><span class="linenos"> 125</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="L-126"><a href="#L-126"><span class="linenos"> 126</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="L-127"><a href="#L-127"><span class="linenos"> 127</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-128"><a href="#L-128"><span class="linenos"> 128</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="L-129"><a href="#L-129"><span class="linenos"> 129</span></a>    
</span><span id="L-130"><a href="#L-130"><span class="linenos"> 130</span></a>    <span class="k">def</span> <span class="nf">bind_existing_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-131"><a href="#L-131"><span class="linenos"> 131</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-132"><a href="#L-132"><span class="linenos"> 132</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-133"><a href="#L-133"><span class="linenos"> 133</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-134"><a href="#L-134"><span class="linenos"> 134</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="L-135"><a href="#L-135"><span class="linenos"> 135</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="L-136"><a href="#L-136"><span class="linenos"> 136</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-137"><a href="#L-137"><span class="linenos"> 137</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-138"><a href="#L-138"><span class="linenos"> 138</span></a>        
</span><span id="L-139"><a href="#L-139"><span class="linenos"> 139</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="L-140"><a href="#L-140"><span class="linenos"> 140</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-141"><a href="#L-141"><span class="linenos"> 141</span></a>        
</span><span id="L-142"><a href="#L-142"><span class="linenos"> 142</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="L-143"><a href="#L-143"><span class="linenos"> 143</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="L-144"><a href="#L-144"><span class="linenos"> 144</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-145"><a href="#L-145"><span class="linenos"> 145</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="L-146"><a href="#L-146"><span class="linenos"> 146</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-147"><a href="#L-147"><span class="linenos"> 147</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="L-148"><a href="#L-148"><span class="linenos"> 148</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-149"><a href="#L-149"><span class="linenos"> 149</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-150"><a href="#L-150"><span class="linenos"> 150</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="L-151"><a href="#L-151"><span class="linenos"> 151</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-152"><a href="#L-152"><span class="linenos"> 152</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-153"><a href="#L-153"><span class="linenos"> 153</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-154"><a href="#L-154"><span class="linenos"> 154</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-155"><a href="#L-155"><span class="linenos"> 155</span></a>
</span><span id="L-156"><a href="#L-156"><span class="linenos"> 156</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="L-157"><a href="#L-157"><span class="linenos"> 157</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-158"><a href="#L-158"><span class="linenos"> 158</span></a>
</span><span id="L-159"><a href="#L-159"><span class="linenos"> 159</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="L-160"><a href="#L-160"><span class="linenos"> 160</span></a>
</span><span id="L-161"><a href="#L-161"><span class="linenos"> 161</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="L-162"><a href="#L-162"><span class="linenos"> 162</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-163"><a href="#L-163"><span class="linenos"> 163</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-164"><a href="#L-164"><span class="linenos"> 164</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-165"><a href="#L-165"><span class="linenos"> 165</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-166"><a href="#L-166"><span class="linenos"> 166</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-167"><a href="#L-167"><span class="linenos"> 167</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="L-168"><a href="#L-168"><span class="linenos"> 168</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="L-169"><a href="#L-169"><span class="linenos"> 169</span></a>
</span><span id="L-170"><a href="#L-170"><span class="linenos"> 170</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="L-171"><a href="#L-171"><span class="linenos"> 171</span></a><span class="sd">        client_reader, client_writer.  client_reader is a TcpStreamReader</span>
</span><span id="L-172"><a href="#L-172"><span class="linenos"> 172</span></a><span class="sd">        object, while client_writer is a TcpStreamWriter object.  This</span>
</span><span id="L-173"><a href="#L-173"><span class="linenos"> 173</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="L-174"><a href="#L-174"><span class="linenos"> 174</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="L-175"><a href="#L-175"><span class="linenos"> 175</span></a><span class="sd">        Task.</span>
</span><span id="L-176"><a href="#L-176"><span class="linenos"> 176</span></a>
</span><span id="L-177"><a href="#L-177"><span class="linenos"> 177</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="L-178"><a href="#L-178"><span class="linenos"> 178</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="L-179"><a href="#L-179"><span class="linenos"> 179</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="L-180"><a href="#L-180"><span class="linenos"> 180</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="L-181"><a href="#L-181"><span class="linenos"> 181</span></a>
</span><span id="L-182"><a href="#L-182"><span class="linenos"> 182</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="L-183"><a href="#L-183"><span class="linenos"> 183</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="L-184"><a href="#L-184"><span class="linenos"> 184</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="L-185"><a href="#L-185"><span class="linenos"> 185</span></a>
</span><span id="L-186"><a href="#L-186"><span class="linenos"> 186</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="L-187"><a href="#L-187"><span class="linenos"> 187</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="L-188"><a href="#L-188"><span class="linenos"> 188</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-189"><a href="#L-189"><span class="linenos"> 189</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-190"><a href="#L-190"><span class="linenos"> 190</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="L-191"><a href="#L-191"><span class="linenos"> 191</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-192"><a href="#L-192"><span class="linenos"> 192</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="L-193"><a href="#L-193"><span class="linenos"> 193</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="L-194"><a href="#L-194"><span class="linenos"> 194</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="L-195"><a href="#L-195"><span class="linenos"> 195</span></a>
</span><span id="L-196"><a href="#L-196"><span class="linenos"> 196</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="L-197"><a href="#L-197"><span class="linenos"> 197</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-198"><a href="#L-198"><span class="linenos"> 198</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-199"><a href="#L-199"><span class="linenos"> 199</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="L-200"><a href="#L-200"><span class="linenos"> 200</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-201"><a href="#L-201"><span class="linenos"> 201</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="L-202"><a href="#L-202"><span class="linenos"> 202</span></a>
</span><span id="L-203"><a href="#L-203"><span class="linenos"> 203</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="L-204"><a href="#L-204"><span class="linenos"> 204</span></a>
</span><span id="L-205"><a href="#L-205"><span class="linenos"> 205</span></a>    <span class="k">def</span> <span class="nf">bind_accepted_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> 
</span><span id="L-206"><a href="#L-206"><span class="linenos"> 206</span></a>                            <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="L-207"><a href="#L-207"><span class="linenos"> 207</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="L-208"><a href="#L-208"><span class="linenos"> 208</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-209"><a href="#L-209"><span class="linenos"> 209</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="L-210"><a href="#L-210"><span class="linenos"> 210</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="L-211"><a href="#L-211"><span class="linenos"> 211</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="L-212"><a href="#L-212"><span class="linenos"> 212</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="L-213"><a href="#L-213"><span class="linenos"> 213</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-214"><a href="#L-214"><span class="linenos"> 214</span></a>        
</span><span id="L-215"><a href="#L-215"><span class="linenos"> 215</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="L-216"><a href="#L-216"><span class="linenos"> 216</span></a>        <span class="n">client_connected_cb</span> <span class="o">=</span> <span class="n">protocol</span><span class="o">.</span><span class="n">_client_connected_cb</span>
</span><span id="L-217"><a href="#L-217"><span class="linenos"> 217</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="L-218"><a href="#L-218"><span class="linenos"> 218</span></a>        
</span><span id="L-219"><a href="#L-219"><span class="linenos"> 219</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="L-220"><a href="#L-220"><span class="linenos"> 220</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="L-221"><a href="#L-221"><span class="linenos"> 221</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-222"><a href="#L-222"><span class="linenos"> 222</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="L-223"><a href="#L-223"><span class="linenos"> 223</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-224"><a href="#L-224"><span class="linenos"> 224</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="L-225"><a href="#L-225"><span class="linenos"> 225</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-226"><a href="#L-226"><span class="linenos"> 226</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-227"><a href="#L-227"><span class="linenos"> 227</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="L-228"><a href="#L-228"><span class="linenos"> 228</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="L-229"><a href="#L-229"><span class="linenos"> 229</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="L-230"><a href="#L-230"><span class="linenos"> 230</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-231"><a href="#L-231"><span class="linenos"> 231</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-232"><a href="#L-232"><span class="linenos"> 232</span></a>
</span><span id="L-233"><a href="#L-233"><span class="linenos"> 233</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="L-234"><a href="#L-234"><span class="linenos"> 234</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="L-235"><a href="#L-235"><span class="linenos"> 235</span></a>
</span><span id="L-236"><a href="#L-236"><span class="linenos"> 236</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="L-237"><a href="#L-237"><span class="linenos"> 237</span></a>
</span><span id="L-238"><a href="#L-238"><span class="linenos"> 238</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-239"><a href="#L-239"><span class="linenos"> 239</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-240"><a href="#L-240"><span class="linenos"> 240</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-241"><a href="#L-241"><span class="linenos"> 241</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-242"><a href="#L-242"><span class="linenos"> 242</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="L-243"><a href="#L-243"><span class="linenos"> 243</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-244"><a href="#L-244"><span class="linenos"> 244</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-245"><a href="#L-245"><span class="linenos"> 245</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="L-246"><a href="#L-246"><span class="linenos"> 246</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="L-247"><a href="#L-247"><span class="linenos"> 247</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-248"><a href="#L-248"><span class="linenos"> 248</span></a>        
</span><span id="L-249"><a href="#L-249"><span class="linenos"> 249</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="L-250"><a href="#L-250"><span class="linenos"> 250</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="L-251"><a href="#L-251"><span class="linenos"> 251</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="L-252"><a href="#L-252"><span class="linenos"> 252</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-253"><a href="#L-253"><span class="linenos"> 253</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="L-254"><a href="#L-254"><span class="linenos"> 254</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="L-255"><a href="#L-255"><span class="linenos"> 255</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="L-256"><a href="#L-256"><span class="linenos"> 256</span></a>            <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="L-257"><a href="#L-257"><span class="linenos"> 257</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-258"><a href="#L-258"><span class="linenos"> 258</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-259"><a href="#L-259"><span class="linenos"> 259</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-260"><a href="#L-260"><span class="linenos"> 260</span></a>    
</span><span id="L-261"><a href="#L-261"><span class="linenos"> 261</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-262"><a href="#L-262"><span class="linenos"> 262</span></a>        <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="L-263"><a href="#L-263"><span class="linenos"> 263</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="L-264"><a href="#L-264"><span class="linenos"> 264</span></a>        <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="L-265"><a href="#L-265"><span class="linenos"> 265</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-266"><a href="#L-266"><span class="linenos"> 266</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-267"><a href="#L-267"><span class="linenos"> 267</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-268"><a href="#L-268"><span class="linenos"> 268</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="L-269"><a href="#L-269"><span class="linenos"> 269</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="L-270"><a href="#L-270"><span class="linenos"> 270</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-271"><a href="#L-271"><span class="linenos"> 271</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="L-272"><a href="#L-272"><span class="linenos"> 272</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="L-273"><a href="#L-273"><span class="linenos"> 273</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-274"><a href="#L-274"><span class="linenos"> 274</span></a>        
</span><span id="L-275"><a href="#L-275"><span class="linenos"> 275</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="L-276"><a href="#L-276"><span class="linenos"> 276</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="L-277"><a href="#L-277"><span class="linenos"> 277</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="L-278"><a href="#L-278"><span class="linenos"> 278</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="L-279"><a href="#L-279"><span class="linenos"> 279</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="L-280"><a href="#L-280"><span class="linenos"> 280</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-281"><a href="#L-281"><span class="linenos"> 281</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-282"><a href="#L-282"><span class="linenos"> 282</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-283"><a href="#L-283"><span class="linenos"> 283</span></a>
</span><span id="L-284"><a href="#L-284"><span class="linenos"> 284</span></a>
</span><span id="L-285"><a href="#L-285"><span class="linenos"> 285</span></a><span class="c1"># def classes_with_amax_size() -&gt; Tuple[Type]:</span>
</span><span id="L-286"><a href="#L-286"><span class="linenos"> 286</span></a><span class="c1">#     types = list()</span>
</span><span id="L-287"><a href="#L-287"><span class="linenos"> 287</span></a><span class="c1">#     try:</span>
</span><span id="L-288"><a href="#L-288"><span class="linenos"> 288</span></a><span class="c1">#         pass</span>
</span><span id="L-289"><a href="#L-289"><span class="linenos"> 289</span></a><span class="c1">#     except AttributeError:</span>
</span><span id="L-290"><a href="#L-290"><span class="linenos"> 290</span></a><span class="c1">#         pass</span>
</span><span id="L-291"><a href="#L-291"><span class="linenos"> 291</span></a>
</span><span id="L-292"><a href="#L-292"><span class="linenos"> 292</span></a>
</span><span id="L-293"><a href="#L-293"><span class="linenos"> 293</span></a><span class="c1"># class StreamReaderCopy(OriginalStreamReader):</span>
</span><span id="L-294"><a href="#L-294"><span class="linenos"> 294</span></a><span class="c1">#     # def __init__(self, limit: int, loop: events.AbstractEventLoop) -&gt; None:</span>
</span><span id="L-295"><a href="#L-295"><span class="linenos"> 295</span></a><span class="c1">#     #     self.stream_manager = None</span>
</span><span id="L-296"><a href="#L-296"><span class="linenos"> 296</span></a><span class="c1">#     #     super().__init__(limit, loop)</span>
</span><span id="L-297"><a href="#L-297"><span class="linenos"> 297</span></a>    
</span><span id="L-298"><a href="#L-298"><span class="linenos"> 298</span></a><span class="c1">#     def __init__(self, manager: TcpStreamManager, original_stream_reader: OriginalStreamReader) -&gt; None:</span>
</span><span id="L-299"><a href="#L-299"><span class="linenos"> 299</span></a><span class="c1">#         self._stream_manager = manager</span>
</span><span id="L-300"><a href="#L-300"><span class="linenos"> 300</span></a><span class="c1">#         self.recv_buff_size_computer = RecvBuffSizeComputer()</span>
</span><span id="L-301"><a href="#L-301"><span class="linenos"> 301</span></a><span class="c1">#         cpu_info_inst = cpu_info()</span>
</span><span id="L-302"><a href="#L-302"><span class="linenos"> 302</span></a><span class="c1">#         # self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="L-303"><a href="#L-303"><span class="linenos"> 303</span></a><span class="c1">#         # self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="L-304"><a href="#L-304"><span class="linenos"> 304</span></a><span class="c1">#         # self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="L-305"><a href="#L-305"><span class="linenos"> 305</span></a><span class="c1">#         # self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="L-306"><a href="#L-306"><span class="linenos"> 306</span></a><span class="c1">#         self.recv_buff_size_computer.max_recv_buff_size = 10 * 1024**2</span>
</span><span id="L-307"><a href="#L-307"><span class="linenos"> 307</span></a><span class="c1">#         # self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="L-308"><a href="#L-308"><span class="linenos"> 308</span></a><span class="c1">#         print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="L-309"><a href="#L-309"><span class="linenos"> 309</span></a><span class="c1">#         original_dict: dict = copy(original_stream_reader.__dict__)</span>
</span><span id="L-310"><a href="#L-310"><span class="linenos"> 310</span></a><span class="c1">#         original_dict.pop(&#39;feed_data&#39;, None)</span>
</span><span id="L-311"><a href="#L-311"><span class="linenos"> 311</span></a><span class="c1">#         original_dict.pop(&#39;_stream_manager&#39;, None)</span>
</span><span id="L-312"><a href="#L-312"><span class="linenos"> 312</span></a><span class="c1">#         self.__dict__.update(original_dict)</span>
</span><span id="L-313"><a href="#L-313"><span class="linenos"> 313</span></a>
</span><span id="L-314"><a href="#L-314"><span class="linenos"> 314</span></a><span class="c1">#     def feed_data(self, data):</span>
</span><span id="L-315"><a href="#L-315"><span class="linenos"> 315</span></a><span class="c1">#         assert not self._eof, &#39;feed_data after feed_eof&#39;</span>
</span><span id="L-316"><a href="#L-316"><span class="linenos"> 316</span></a>
</span><span id="L-317"><a href="#L-317"><span class="linenos"> 317</span></a><span class="c1">#         if not data:</span>
</span><span id="L-318"><a href="#L-318"><span class="linenos"> 318</span></a><span class="c1">#             return</span>
</span><span id="L-319"><a href="#L-319"><span class="linenos"> 319</span></a>
</span><span id="L-320"><a href="#L-320"><span class="linenos"> 320</span></a><span class="c1">#         data_len = len(data)</span>
</span><span id="L-321"><a href="#L-321"><span class="linenos"> 321</span></a><span class="c1">#         self.recv_buff_size_computer.calc_new_recv_buff_size(data_len)</span>
</span><span id="L-322"><a href="#L-322"><span class="linenos"> 322</span></a><span class="c1">#         self._buffer.extend(data)</span>
</span><span id="L-323"><a href="#L-323"><span class="linenos"> 323</span></a><span class="c1">#         self._wakeup_waiter()</span>
</span><span id="L-324"><a href="#L-324"><span class="linenos"> 324</span></a>
</span><span id="L-325"><a href="#L-325"><span class="linenos"> 325</span></a><span class="c1">#         if (self._transport is not None and</span>
</span><span id="L-326"><a href="#L-326"><span class="linenos"> 326</span></a><span class="c1">#                 not self._paused and</span>
</span><span id="L-327"><a href="#L-327"><span class="linenos"> 327</span></a><span class="c1">#                 len(self._buffer) &gt; 2 * self._limit):</span>
</span><span id="L-328"><a href="#L-328"><span class="linenos"> 328</span></a><span class="c1">#             try:</span>
</span><span id="L-329"><a href="#L-329"><span class="linenos"> 329</span></a><span class="c1">#                 self._transport.pause_reading()</span>
</span><span id="L-330"><a href="#L-330"><span class="linenos"> 330</span></a><span class="c1">#             except NotImplementedError:</span>
</span><span id="L-331"><a href="#L-331"><span class="linenos"> 331</span></a><span class="c1">#                 # The transport can&#39;t be paused.</span>
</span><span id="L-332"><a href="#L-332"><span class="linenos"> 332</span></a><span class="c1">#                 # We&#39;ll just have to buffer all data.</span>
</span><span id="L-333"><a href="#L-333"><span class="linenos"> 333</span></a><span class="c1">#                 # Forget the transport so we don&#39;t keep trying.</span>
</span><span id="L-334"><a href="#L-334"><span class="linenos"> 334</span></a><span class="c1">#                 self._transport = None</span>
</span><span id="L-335"><a href="#L-335"><span class="linenos"> 335</span></a><span class="c1">#             else:</span>
</span><span id="L-336"><a href="#L-336"><span class="linenos"> 336</span></a><span class="c1">#                 self._paused = True</span>
</span><span id="L-337"><a href="#L-337"><span class="linenos"> 337</span></a>
</span><span id="L-338"><a href="#L-338"><span class="linenos"> 338</span></a><span class="c1">#     def _maybe_resume_transport(self):</span>
</span><span id="L-339"><a href="#L-339"><span class="linenos"> 339</span></a><span class="c1">#         if isinstance(self._transport, (</span>
</span><span id="L-340"><a href="#L-340"><span class="linenos"> 340</span></a><span class="c1">#             proactor_events._ProactorDatagramTransport,</span>
</span><span id="L-341"><a href="#L-341"><span class="linenos"> 341</span></a><span class="c1">#             selector_events._SelectorTransport,</span>
</span><span id="L-342"><a href="#L-342"><span class="linenos"> 342</span></a><span class="c1">#             unix_events._UnixReadPipeTransport</span>
</span><span id="L-343"><a href="#L-343"><span class="linenos"> 343</span></a><span class="c1">#             )):</span>
</span><span id="L-344"><a href="#L-344"><span class="linenos"> 344</span></a><span class="c1">#             # if hasattr(self._transport, &#39;max_size&#39;):</span>
</span><span id="L-345"><a href="#L-345"><span class="linenos"> 345</span></a><span class="c1">#             try:</span>
</span><span id="L-346"><a href="#L-346"><span class="linenos"> 346</span></a><span class="c1">#                 self._transport.max_size = self.recv_buff_size_computer.recv_buff_size</span>
</span><span id="L-347"><a href="#L-347"><span class="linenos"> 347</span></a><span class="c1">#                 # print(f&#39;max_size: {self._transport.max_size}&#39;)</span>
</span><span id="L-348"><a href="#L-348"><span class="linenos"> 348</span></a><span class="c1">#             except AttributeError:</span>
</span><span id="L-349"><a href="#L-349"><span class="linenos"> 349</span></a><span class="c1">#                 pass</span>
</span><span id="L-350"><a href="#L-350"><span class="linenos"> 350</span></a><span class="c1">#         else:</span>
</span><span id="L-351"><a href="#L-351"><span class="linenos"> 351</span></a><span class="c1">#             print(f&#39;Unsupported transport: {type(self._transport)}&#39;)</span>
</span><span id="L-352"><a href="#L-352"><span class="linenos"> 352</span></a>        
</span><span id="L-353"><a href="#L-353"><span class="linenos"> 353</span></a><span class="c1">#         if self._paused and len(self._buffer) &lt;= self._limit:</span>
</span><span id="L-354"><a href="#L-354"><span class="linenos"> 354</span></a><span class="c1">#             self._paused = False</span>
</span><span id="L-355"><a href="#L-355"><span class="linenos"> 355</span></a><span class="c1">#             self._transport.resume_reading()</span>
</span><span id="L-356"><a href="#L-356"><span class="linenos"> 356</span></a>    
</span><span id="L-357"><a href="#L-357"><span class="linenos"> 357</span></a><span class="c1">#     async def read_with_counter(self):</span>
</span><span id="L-358"><a href="#L-358"><span class="linenos"> 358</span></a><span class="c1">#         if self._exception is not None:</span>
</span><span id="L-359"><a href="#L-359"><span class="linenos"> 359</span></a><span class="c1">#             raise self._exception</span>
</span><span id="L-360"><a href="#L-360"><span class="linenos"> 360</span></a>
</span><span id="L-361"><a href="#L-361"><span class="linenos"> 361</span></a><span class="c1">#         # This used to just loop creating a new waiter hoping to</span>
</span><span id="L-362"><a href="#L-362"><span class="linenos"> 362</span></a><span class="c1">#         # collect everything in self._buffer, but that would</span>
</span><span id="L-363"><a href="#L-363"><span class="linenos"> 363</span></a><span class="c1">#         # deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-364"><a href="#L-364"><span class="linenos"> 364</span></a><span class="c1">#         # bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-365"><a href="#L-365"><span class="linenos"> 365</span></a><span class="c1">#         blocks = []</span>
</span><span id="L-366"><a href="#L-366"><span class="linenos"> 366</span></a><span class="c1">#         counter = 0</span>
</span><span id="L-367"><a href="#L-367"><span class="linenos"> 367</span></a><span class="c1">#         while True:</span>
</span><span id="L-368"><a href="#L-368"><span class="linenos"> 368</span></a><span class="c1">#             block = await self.read(self._limit)</span>
</span><span id="L-369"><a href="#L-369"><span class="linenos"> 369</span></a><span class="c1">#             counter += 1</span>
</span><span id="L-370"><a href="#L-370"><span class="linenos"> 370</span></a><span class="c1">#             if not block:</span>
</span><span id="L-371"><a href="#L-371"><span class="linenos"> 371</span></a><span class="c1">#                 break</span>
</span><span id="L-372"><a href="#L-372"><span class="linenos"> 372</span></a><span class="c1">#             blocks.append(block)</span>
</span><span id="L-373"><a href="#L-373"><span class="linenos"> 373</span></a><span class="c1">#         return b&#39;&#39;.join(blocks), counter</span>
</span><span id="L-374"><a href="#L-374"><span class="linenos"> 374</span></a>
</span><span id="L-375"><a href="#L-375"><span class="linenos"> 375</span></a>
</span><span id="L-376"><a href="#L-376"><span class="linenos"> 376</span></a><span class="k">class</span> <span class="nc">TcpStreamReader</span><span class="p">(</span><span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">StreamReaderAbstract</span><span class="p">):</span>
</span><span id="L-377"><a href="#L-377"><span class="linenos"> 377</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-378"><a href="#L-378"><span class="linenos"> 378</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-379"><a href="#L-379"><span class="linenos"> 379</span></a>
</span><span id="L-380"><a href="#L-380"><span class="linenos"> 380</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-381"><a href="#L-381"><span class="linenos"> 381</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-382"><a href="#L-382"><span class="linenos"> 382</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="L-383"><a href="#L-383"><span class="linenos"> 383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="L-384"><a href="#L-384"><span class="linenos"> 384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">input_from_client_container_type</span><span class="p">(</span>
</span><span id="L-385"><a href="#L-385"><span class="linenos"> 385</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="L-386"><a href="#L-386"><span class="linenos"> 386</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="L-387"><a href="#L-387"><span class="linenos"> 387</span></a>        <span class="n">cpu_info_inst</span> <span class="o">=</span> <span class="n">cpu_info</span><span class="p">()</span>
</span><span id="L-388"><a href="#L-388"><span class="linenos"> 388</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="L-389"><a href="#L-389"><span class="linenos"> 389</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="L-390"><a href="#L-390"><span class="linenos"> 390</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="L-391"><a href="#L-391"><span class="linenos"> 391</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="L-392"><a href="#L-392"><span class="linenos"> 392</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">max_recv_buff_size</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span>
</span><span id="L-393"><a href="#L-393"><span class="linenos"> 393</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="L-394"><a href="#L-394"><span class="linenos"> 394</span></a>        <span class="c1"># print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="L-395"><a href="#L-395"><span class="linenos"> 395</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-396"><a href="#L-396"><span class="linenos"> 396</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-397"><a href="#L-397"><span class="linenos"> 397</span></a>    
</span><span id="L-398"><a href="#L-398"><span class="linenos"> 398</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-399"><a href="#L-399"><span class="linenos"> 399</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-400"><a href="#L-400"><span class="linenos"> 400</span></a>    
</span><span id="L-401"><a href="#L-401"><span class="linenos"> 401</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-402"><a href="#L-402"><span class="linenos"> 402</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-403"><a href="#L-403"><span class="linenos"> 403</span></a>    
</span><span id="L-404"><a href="#L-404"><span class="linenos"> 404</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-405"><a href="#L-405"><span class="linenos"> 405</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-406"><a href="#L-406"><span class="linenos"> 406</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-407"><a href="#L-407"><span class="linenos"> 407</span></a>
</span><span id="L-408"><a href="#L-408"><span class="linenos"> 408</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-409"><a href="#L-409"><span class="linenos"> 409</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-410"><a href="#L-410"><span class="linenos"> 410</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-411"><a href="#L-411"><span class="linenos"> 411</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-412"><a href="#L-412"><span class="linenos"> 412</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-413"><a href="#L-413"><span class="linenos"> 413</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-414"><a href="#L-414"><span class="linenos"> 414</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-415"><a href="#L-415"><span class="linenos"> 415</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="L-416"><a href="#L-416"><span class="linenos"> 416</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="L-417"><a href="#L-417"><span class="linenos"> 417</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-418"><a href="#L-418"><span class="linenos"> 418</span></a>                <span class="k">break</span>
</span><span id="L-419"><a href="#L-419"><span class="linenos"> 419</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-420"><a href="#L-420"><span class="linenos"> 420</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span><span id="L-421"><a href="#L-421"><span class="linenos"> 421</span></a>
</span><span id="L-422"><a href="#L-422"><span class="linenos"> 422</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-423"><a href="#L-423"><span class="linenos"> 423</span></a>        <span class="n">info</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">]</span>
</span><span id="L-424"><a href="#L-424"><span class="linenos"> 424</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="L-425"><a href="#L-425"><span class="linenos"> 425</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span><span class="si">}</span><span class="s1"> bytes&#39;</span><span class="p">)</span>
</span><span id="L-426"><a href="#L-426"><span class="linenos"> 426</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-427"><a href="#L-427"><span class="linenos"> 427</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;eof&#39;</span><span class="p">)</span>
</span><span id="L-428"><a href="#L-428"><span class="linenos"> 428</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span> <span class="o">!=</span> <span class="n">DEFAULT_LIMIT</span><span class="p">:</span>
</span><span id="L-429"><a href="#L-429"><span class="linenos"> 429</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;limit=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-430"><a href="#L-430"><span class="linenos"> 430</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="p">:</span>
</span><span id="L-431"><a href="#L-431"><span class="linenos"> 431</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;waiter=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-432"><a href="#L-432"><span class="linenos"> 432</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="p">:</span>
</span><span id="L-433"><a href="#L-433"><span class="linenos"> 433</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;exception=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-434"><a href="#L-434"><span class="linenos"> 434</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">:</span>
</span><span id="L-435"><a href="#L-435"><span class="linenos"> 435</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;transport=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-436"><a href="#L-436"><span class="linenos"> 436</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span><span class="p">:</span>
</span><span id="L-437"><a href="#L-437"><span class="linenos"> 437</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;paused&#39;</span><span class="p">)</span>
</span><span id="L-438"><a href="#L-438"><span class="linenos"> 438</span></a>        <span class="k">return</span> <span class="s1">&#39;&lt;</span><span class="si">{}</span><span class="s1">&gt;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">info</span><span class="p">))</span>
</span><span id="L-439"><a href="#L-439"><span class="linenos"> 439</span></a>
</span><span id="L-440"><a href="#L-440"><span class="linenos"> 440</span></a>    <span class="k">def</span> <span class="nf">_maybe_resume_transport</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-441"><a href="#L-441"><span class="linenos"> 441</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">,</span> <span class="p">(</span>
</span><span id="L-442"><a href="#L-442"><span class="linenos"> 442</span></a>            <span class="n">proactor_events</span><span class="o">.</span><span class="n">_ProactorDatagramTransport</span><span class="p">,</span>
</span><span id="L-443"><a href="#L-443"><span class="linenos"> 443</span></a>            <span class="n">selector_events</span><span class="o">.</span><span class="n">_SelectorTransport</span><span class="p">,</span>
</span><span id="L-444"><a href="#L-444"><span class="linenos"> 444</span></a>            <span class="n">unix_events</span><span class="o">.</span><span class="n">_UnixReadPipeTransport</span>
</span><span id="L-445"><a href="#L-445"><span class="linenos"> 445</span></a>            <span class="p">)):</span>
</span><span id="L-446"><a href="#L-446"><span class="linenos"> 446</span></a>            <span class="c1"># if hasattr(self._transport, &#39;max_size&#39;):</span>
</span><span id="L-447"><a href="#L-447"><span class="linenos"> 447</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-448"><a href="#L-448"><span class="linenos"> 448</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">max_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">recv_buff_size</span>
</span><span id="L-449"><a href="#L-449"><span class="linenos"> 449</span></a>                <span class="c1"># print(f&#39;max_size: {self._transport.max_size}&#39;)</span>
</span><span id="L-450"><a href="#L-450"><span class="linenos"> 450</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="L-451"><a href="#L-451"><span class="linenos"> 451</span></a>                <span class="k">pass</span>
</span><span id="L-452"><a href="#L-452"><span class="linenos"> 452</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-453"><a href="#L-453"><span class="linenos"> 453</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="L-454"><a href="#L-454"><span class="linenos"> 454</span></a>        
</span><span id="L-455"><a href="#L-455"><span class="linenos"> 455</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> \
</span><span id="L-456"><a href="#L-456"><span class="linenos"> 456</span></a>            <span class="ow">and</span> <span class="p">(</span>
</span><span id="L-457"><a href="#L-457"><span class="linenos"> 457</span></a>                <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="L-458"><a href="#L-458"><span class="linenos"> 458</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="L-459"><a href="#L-459"><span class="linenos"> 459</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="L-460"><a href="#L-460"><span class="linenos"> 460</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="L-461"><a href="#L-461"><span class="linenos"> 461</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
</span><span id="L-462"><a href="#L-462"><span class="linenos"> 462</span></a>            <span class="p">):</span>
</span><span id="L-463"><a href="#L-463"><span class="linenos"> 463</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-464"><a href="#L-464"><span class="linenos"> 464</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="L-465"><a href="#L-465"><span class="linenos"> 465</span></a>
</span><span id="L-466"><a href="#L-466"><span class="linenos"> 466</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-467"><a href="#L-467"><span class="linenos"> 467</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="L-468"><a href="#L-468"><span class="linenos"> 468</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-469"><a href="#L-469"><span class="linenos"> 469</span></a>
</span><span id="L-470"><a href="#L-470"><span class="linenos"> 470</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-471"><a href="#L-471"><span class="linenos"> 471</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="L-472"><a href="#L-472"><span class="linenos"> 472</span></a>
</span><span id="L-473"><a href="#L-473"><span class="linenos"> 473</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="L-474"><a href="#L-474"><span class="linenos"> 474</span></a>            <span class="k">return</span>
</span><span id="L-475"><a href="#L-475"><span class="linenos"> 475</span></a>
</span><span id="L-476"><a href="#L-476"><span class="linenos"> 476</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-477"><a href="#L-477"><span class="linenos"> 477</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="L-478"><a href="#L-478"><span class="linenos"> 478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-479"><a href="#L-479"><span class="linenos"> 479</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="L-480"><a href="#L-480"><span class="linenos"> 480</span></a>
</span><span id="L-481"><a href="#L-481"><span class="linenos"> 481</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="L-482"><a href="#L-482"><span class="linenos"> 482</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="L-483"><a href="#L-483"><span class="linenos"> 483</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="L-484"><a href="#L-484"><span class="linenos"> 484</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="L-485"><a href="#L-485"><span class="linenos"> 485</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="L-486"><a href="#L-486"><span class="linenos"> 486</span></a>                <span class="p">)):</span>
</span><span id="L-487"><a href="#L-487"><span class="linenos"> 487</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="L-488"><a href="#L-488"><span class="linenos"> 488</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="L-489"><a href="#L-489"><span class="linenos"> 489</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="L-490"><a href="#L-490"><span class="linenos"> 490</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="L-491"><a href="#L-491"><span class="linenos"> 491</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="L-492"><a href="#L-492"><span class="linenos"> 492</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="L-493"><a href="#L-493"><span class="linenos"> 493</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-494"><a href="#L-494"><span class="linenos"> 494</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-495"><a href="#L-495"><span class="linenos"> 495</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-496"><a href="#L-496"><span class="linenos"> 496</span></a>
</span><span id="L-497"><a href="#L-497"><span class="linenos"> 497</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-498"><a href="#L-498"><span class="linenos"> 498</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="L-499"><a href="#L-499"><span class="linenos"> 499</span></a>
</span><span id="L-500"><a href="#L-500"><span class="linenos"> 500</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="L-501"><a href="#L-501"><span class="linenos"> 501</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="L-502"><a href="#L-502"><span class="linenos"> 502</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="L-503"><a href="#L-503"><span class="linenos"> 503</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="L-504"><a href="#L-504"><span class="linenos"> 504</span></a>
</span><span id="L-505"><a href="#L-505"><span class="linenos"> 505</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="L-506"><a href="#L-506"><span class="linenos"> 506</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="L-507"><a href="#L-507"><span class="linenos"> 507</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="L-508"><a href="#L-508"><span class="linenos"> 508</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="L-509"><a href="#L-509"><span class="linenos"> 509</span></a>
</span><span id="L-510"><a href="#L-510"><span class="linenos"> 510</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-511"><a href="#L-511"><span class="linenos"> 511</span></a><span class="sd">        needed.</span>
</span><span id="L-512"><a href="#L-512"><span class="linenos"> 512</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-513"><a href="#L-513"><span class="linenos"> 513</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="L-514"><a href="#L-514"><span class="linenos"> 514</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-515"><a href="#L-515"><span class="linenos"> 515</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-516"><a href="#L-516"><span class="linenos"> 516</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="L-517"><a href="#L-517"><span class="linenos"> 517</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-518"><a href="#L-518"><span class="linenos"> 518</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="L-519"><a href="#L-519"><span class="linenos"> 519</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="L-520"><a href="#L-520"><span class="linenos"> 520</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="L-521"><a href="#L-521"><span class="linenos"> 521</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="L-522"><a href="#L-522"><span class="linenos"> 522</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-523"><a href="#L-523"><span class="linenos"> 523</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="L-524"><a href="#L-524"><span class="linenos"> 524</span></a>            
</span><span id="L-525"><a href="#L-525"><span class="linenos"> 525</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-526"><a href="#L-526"><span class="linenos"> 526</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="L-527"><a href="#L-527"><span class="linenos"> 527</span></a>        <span class="k">return</span> <span class="n">line</span>
</span><span id="L-528"><a href="#L-528"><span class="linenos"> 528</span></a>
</span><span id="L-529"><a href="#L-529"><span class="linenos"> 529</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="L-530"><a href="#L-530"><span class="linenos"> 530</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="L-531"><a href="#L-531"><span class="linenos"> 531</span></a>
</span><span id="L-532"><a href="#L-532"><span class="linenos"> 532</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="L-533"><a href="#L-533"><span class="linenos"> 533</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="L-534"><a href="#L-534"><span class="linenos"> 534</span></a><span class="sd">        separator at the end.</span>
</span><span id="L-535"><a href="#L-535"><span class="linenos"> 535</span></a>
</span><span id="L-536"><a href="#L-536"><span class="linenos"> 536</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="L-537"><a href="#L-537"><span class="linenos"> 537</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="L-538"><a href="#L-538"><span class="linenos"> 538</span></a><span class="sd">        separator.</span>
</span><span id="L-539"><a href="#L-539"><span class="linenos"> 539</span></a>
</span><span id="L-540"><a href="#L-540"><span class="linenos"> 540</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="L-541"><a href="#L-541"><span class="linenos"> 541</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="L-542"><a href="#L-542"><span class="linenos"> 542</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="L-543"><a href="#L-543"><span class="linenos"> 543</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="L-544"><a href="#L-544"><span class="linenos"> 544</span></a>
</span><span id="L-545"><a href="#L-545"><span class="linenos"> 545</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="L-546"><a href="#L-546"><span class="linenos"> 546</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="L-547"><a href="#L-547"><span class="linenos"> 547</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="L-548"><a href="#L-548"><span class="linenos"> 548</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-549"><a href="#L-549"><span class="linenos"> 549</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="L-550"><a href="#L-550"><span class="linenos"> 550</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-551"><a href="#L-551"><span class="linenos"> 551</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="L-552"><a href="#L-552"><span class="linenos"> 552</span></a>
</span><span id="L-553"><a href="#L-553"><span class="linenos"> 553</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-554"><a href="#L-554"><span class="linenos"> 554</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-555"><a href="#L-555"><span class="linenos"> 555</span></a>
</span><span id="L-556"><a href="#L-556"><span class="linenos"> 556</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="L-557"><a href="#L-557"><span class="linenos"> 557</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="L-558"><a href="#L-558"><span class="linenos"> 558</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="L-559"><a href="#L-559"><span class="linenos"> 559</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="L-560"><a href="#L-560"><span class="linenos"> 560</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="L-561"><a href="#L-561"><span class="linenos"> 561</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="L-562"><a href="#L-562"><span class="linenos"> 562</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="L-563"><a href="#L-563"><span class="linenos"> 563</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="L-564"><a href="#L-564"><span class="linenos"> 564</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="L-565"><a href="#L-565"><span class="linenos"> 565</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="L-566"><a href="#L-566"><span class="linenos"> 566</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="L-567"><a href="#L-567"><span class="linenos"> 567</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="L-568"><a href="#L-568"><span class="linenos"> 568</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="L-569"><a href="#L-569"><span class="linenos"> 569</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="L-570"><a href="#L-570"><span class="linenos"> 570</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="L-571"><a href="#L-571"><span class="linenos"> 571</span></a>        <span class="c1">#   messages :)</span>
</span><span id="L-572"><a href="#L-572"><span class="linenos"> 572</span></a>
</span><span id="L-573"><a href="#L-573"><span class="linenos"> 573</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="L-574"><a href="#L-574"><span class="linenos"> 574</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="L-575"><a href="#L-575"><span class="linenos"> 575</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="L-576"><a href="#L-576"><span class="linenos"> 576</span></a>
</span><span id="L-577"><a href="#L-577"><span class="linenos"> 577</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="L-578"><a href="#L-578"><span class="linenos"> 578</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="L-579"><a href="#L-579"><span class="linenos"> 579</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-580"><a href="#L-580"><span class="linenos"> 580</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-581"><a href="#L-581"><span class="linenos"> 581</span></a>
</span><span id="L-582"><a href="#L-582"><span class="linenos"> 582</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="L-583"><a href="#L-583"><span class="linenos"> 583</span></a>            <span class="c1"># fit.</span>
</span><span id="L-584"><a href="#L-584"><span class="linenos"> 584</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="L-585"><a href="#L-585"><span class="linenos"> 585</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="L-586"><a href="#L-586"><span class="linenos"> 586</span></a>
</span><span id="L-587"><a href="#L-587"><span class="linenos"> 587</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="L-588"><a href="#L-588"><span class="linenos"> 588</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="L-589"><a href="#L-589"><span class="linenos"> 589</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="L-590"><a href="#L-590"><span class="linenos"> 590</span></a>                    <span class="k">break</span>
</span><span id="L-591"><a href="#L-591"><span class="linenos"> 591</span></a>
</span><span id="L-592"><a href="#L-592"><span class="linenos"> 592</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="L-593"><a href="#L-593"><span class="linenos"> 593</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="L-594"><a href="#L-594"><span class="linenos"> 594</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="L-595"><a href="#L-595"><span class="linenos"> 595</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="L-596"><a href="#L-596"><span class="linenos"> 596</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="L-597"><a href="#L-597"><span class="linenos"> 597</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="L-598"><a href="#L-598"><span class="linenos"> 598</span></a>
</span><span id="L-599"><a href="#L-599"><span class="linenos"> 599</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="L-600"><a href="#L-600"><span class="linenos"> 600</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="L-601"><a href="#L-601"><span class="linenos"> 601</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="L-602"><a href="#L-602"><span class="linenos"> 602</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="L-603"><a href="#L-603"><span class="linenos"> 603</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-604"><a href="#L-604"><span class="linenos"> 604</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-605"><a href="#L-605"><span class="linenos"> 605</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="L-606"><a href="#L-606"><span class="linenos"> 606</span></a>
</span><span id="L-607"><a href="#L-607"><span class="linenos"> 607</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="L-608"><a href="#L-608"><span class="linenos"> 608</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="L-609"><a href="#L-609"><span class="linenos"> 609</span></a>
</span><span id="L-610"><a href="#L-610"><span class="linenos"> 610</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="L-611"><a href="#L-611"><span class="linenos"> 611</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="L-612"><a href="#L-612"><span class="linenos"> 612</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="L-613"><a href="#L-613"><span class="linenos"> 613</span></a>
</span><span id="L-614"><a href="#L-614"><span class="linenos"> 614</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="L-615"><a href="#L-615"><span class="linenos"> 615</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-616"><a href="#L-616"><span class="linenos"> 616</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span><span id="L-617"><a href="#L-617"><span class="linenos"> 617</span></a>
</span><span id="L-618"><a href="#L-618"><span class="linenos"> 618</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="L-619"><a href="#L-619"><span class="linenos"> 619</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="L-620"><a href="#L-620"><span class="linenos"> 620</span></a>
</span><span id="L-621"><a href="#L-621"><span class="linenos"> 621</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="L-622"><a href="#L-622"><span class="linenos"> 622</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="L-623"><a href="#L-623"><span class="linenos"> 623</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="L-624"><a href="#L-624"><span class="linenos"> 624</span></a>
</span><span id="L-625"><a href="#L-625"><span class="linenos"> 625</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="L-626"><a href="#L-626"><span class="linenos"> 626</span></a>
</span><span id="L-627"><a href="#L-627"><span class="linenos"> 627</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="L-628"><a href="#L-628"><span class="linenos"> 628</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="L-629"><a href="#L-629"><span class="linenos"> 629</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="L-630"><a href="#L-630"><span class="linenos"> 630</span></a><span class="sd">        object.</span>
</span><span id="L-631"><a href="#L-631"><span class="linenos"> 631</span></a>
</span><span id="L-632"><a href="#L-632"><span class="linenos"> 632</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-633"><a href="#L-633"><span class="linenos"> 633</span></a><span class="sd">        creation.</span>
</span><span id="L-634"><a href="#L-634"><span class="linenos"> 634</span></a>
</span><span id="L-635"><a href="#L-635"><span class="linenos"> 635</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-636"><a href="#L-636"><span class="linenos"> 636</span></a><span class="sd">        needed.</span>
</span><span id="L-637"><a href="#L-637"><span class="linenos"> 637</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-638"><a href="#L-638"><span class="linenos"> 638</span></a>
</span><span id="L-639"><a href="#L-639"><span class="linenos"> 639</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-640"><a href="#L-640"><span class="linenos"> 640</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-641"><a href="#L-641"><span class="linenos"> 641</span></a>
</span><span id="L-642"><a href="#L-642"><span class="linenos"> 642</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-643"><a href="#L-643"><span class="linenos"> 643</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-644"><a href="#L-644"><span class="linenos"> 644</span></a>
</span><span id="L-645"><a href="#L-645"><span class="linenos"> 645</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-646"><a href="#L-646"><span class="linenos"> 646</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-647"><a href="#L-647"><span class="linenos"> 647</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-648"><a href="#L-648"><span class="linenos"> 648</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-649"><a href="#L-649"><span class="linenos"> 649</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-650"><a href="#L-650"><span class="linenos"> 650</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-651"><a href="#L-651"><span class="linenos"> 651</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-652"><a href="#L-652"><span class="linenos"> 652</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-653"><a href="#L-653"><span class="linenos"> 653</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-654"><a href="#L-654"><span class="linenos"> 654</span></a>                    <span class="k">break</span>
</span><span id="L-655"><a href="#L-655"><span class="linenos"> 655</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-656"><a href="#L-656"><span class="linenos"> 656</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="L-657"><a href="#L-657"><span class="linenos"> 657</span></a>
</span><span id="L-658"><a href="#L-658"><span class="linenos"> 658</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-659"><a href="#L-659"><span class="linenos"> 659</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="L-660"><a href="#L-660"><span class="linenos"> 660</span></a>
</span><span id="L-661"><a href="#L-661"><span class="linenos"> 661</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="L-662"><a href="#L-662"><span class="linenos"> 662</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-663"><a href="#L-663"><span class="linenos"> 663</span></a>
</span><span id="L-664"><a href="#L-664"><span class="linenos"> 664</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-665"><a href="#L-665"><span class="linenos"> 665</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-666"><a href="#L-666"><span class="linenos"> 666</span></a>
</span><span id="L-667"><a href="#L-667"><span class="linenos"> 667</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="L-668"><a href="#L-668"><span class="linenos"> 668</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="L-669"><a href="#L-669"><span class="linenos"> 669</span></a>
</span><span id="L-670"><a href="#L-670"><span class="linenos"> 670</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="L-671"><a href="#L-671"><span class="linenos"> 671</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="L-672"><a href="#L-672"><span class="linenos"> 672</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="L-673"><a href="#L-673"><span class="linenos"> 673</span></a>
</span><span id="L-674"><a href="#L-674"><span class="linenos"> 674</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="L-675"><a href="#L-675"><span class="linenos"> 675</span></a>
</span><span id="L-676"><a href="#L-676"><span class="linenos"> 676</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="L-677"><a href="#L-677"><span class="linenos"> 677</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="L-678"><a href="#L-678"><span class="linenos"> 678</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="L-679"><a href="#L-679"><span class="linenos"> 679</span></a><span class="sd">        object.</span>
</span><span id="L-680"><a href="#L-680"><span class="linenos"> 680</span></a>
</span><span id="L-681"><a href="#L-681"><span class="linenos"> 681</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-682"><a href="#L-682"><span class="linenos"> 682</span></a><span class="sd">        creation.</span>
</span><span id="L-683"><a href="#L-683"><span class="linenos"> 683</span></a>
</span><span id="L-684"><a href="#L-684"><span class="linenos"> 684</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-685"><a href="#L-685"><span class="linenos"> 685</span></a><span class="sd">        needed.</span>
</span><span id="L-686"><a href="#L-686"><span class="linenos"> 686</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-687"><a href="#L-687"><span class="linenos"> 687</span></a>
</span><span id="L-688"><a href="#L-688"><span class="linenos"> 688</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-689"><a href="#L-689"><span class="linenos"> 689</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-690"><a href="#L-690"><span class="linenos"> 690</span></a>
</span><span id="L-691"><a href="#L-691"><span class="linenos"> 691</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-692"><a href="#L-692"><span class="linenos"> 692</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-693"><a href="#L-693"><span class="linenos"> 693</span></a>
</span><span id="L-694"><a href="#L-694"><span class="linenos"> 694</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-695"><a href="#L-695"><span class="linenos"> 695</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="L-696"><a href="#L-696"><span class="linenos"> 696</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="L-697"><a href="#L-697"><span class="linenos"> 697</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="L-698"><a href="#L-698"><span class="linenos"> 698</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="L-699"><a href="#L-699"><span class="linenos"> 699</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="L-700"><a href="#L-700"><span class="linenos"> 700</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="L-701"><a href="#L-701"><span class="linenos"> 701</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="L-702"><a href="#L-702"><span class="linenos"> 702</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="L-703"><a href="#L-703"><span class="linenos"> 703</span></a>                    <span class="k">break</span>
</span><span id="L-704"><a href="#L-704"><span class="linenos"> 704</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="L-705"><a href="#L-705"><span class="linenos"> 705</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="L-706"><a href="#L-706"><span class="linenos"> 706</span></a>
</span><span id="L-707"><a href="#L-707"><span class="linenos"> 707</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-708"><a href="#L-708"><span class="linenos"> 708</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="L-709"><a href="#L-709"><span class="linenos"> 709</span></a>
</span><span id="L-710"><a href="#L-710"><span class="linenos"> 710</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="L-711"><a href="#L-711"><span class="linenos"> 711</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-712"><a href="#L-712"><span class="linenos"> 712</span></a>
</span><span id="L-713"><a href="#L-713"><span class="linenos"> 713</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-714"><a href="#L-714"><span class="linenos"> 714</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-715"><a href="#L-715"><span class="linenos"> 715</span></a>
</span><span id="L-716"><a href="#L-716"><span class="linenos"> 716</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="L-717"><a href="#L-717"><span class="linenos"> 717</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="L-718"><a href="#L-718"><span class="linenos"> 718</span></a>
</span><span id="L-719"><a href="#L-719"><span class="linenos"> 719</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="L-720"><a href="#L-720"><span class="linenos"> 720</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="L-721"><a href="#L-721"><span class="linenos"> 721</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="L-722"><a href="#L-722"><span class="linenos"> 722</span></a>
</span><span id="L-723"><a href="#L-723"><span class="linenos"> 723</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="L-724"><a href="#L-724"><span class="linenos"> 724</span></a>
</span><span id="L-725"><a href="#L-725"><span class="linenos"> 725</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="L-726"><a href="#L-726"><span class="linenos"> 726</span></a><span class="sd">        creation.</span>
</span><span id="L-727"><a href="#L-727"><span class="linenos"> 727</span></a>
</span><span id="L-728"><a href="#L-728"><span class="linenos"> 728</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="L-729"><a href="#L-729"><span class="linenos"> 729</span></a><span class="sd">        needed.</span>
</span><span id="L-730"><a href="#L-730"><span class="linenos"> 730</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-731"><a href="#L-731"><span class="linenos"> 731</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-732"><a href="#L-732"><span class="linenos"> 732</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="L-733"><a href="#L-733"><span class="linenos"> 733</span></a>
</span><span id="L-734"><a href="#L-734"><span class="linenos"> 734</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-735"><a href="#L-735"><span class="linenos"> 735</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-736"><a href="#L-736"><span class="linenos"> 736</span></a>
</span><span id="L-737"><a href="#L-737"><span class="linenos"> 737</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-738"><a href="#L-738"><span class="linenos"> 738</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-739"><a href="#L-739"><span class="linenos"> 739</span></a>
</span><span id="L-740"><a href="#L-740"><span class="linenos"> 740</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-741"><a href="#L-741"><span class="linenos"> 741</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-742"><a href="#L-742"><span class="linenos"> 742</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-743"><a href="#L-743"><span class="linenos"> 743</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="L-744"><a href="#L-744"><span class="linenos"> 744</span></a>
</span><span id="L-745"><a href="#L-745"><span class="linenos"> 745</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="L-746"><a href="#L-746"><span class="linenos"> 746</span></a>
</span><span id="L-747"><a href="#L-747"><span class="linenos"> 747</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-748"><a href="#L-748"><span class="linenos"> 748</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-749"><a href="#L-749"><span class="linenos"> 749</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-750"><a href="#L-750"><span class="linenos"> 750</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-751"><a href="#L-751"><span class="linenos"> 751</span></a>
</span><span id="L-752"><a href="#L-752"><span class="linenos"> 752</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-753"><a href="#L-753"><span class="linenos"> 753</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-754"><a href="#L-754"><span class="linenos"> 754</span></a>    
</span><span id="L-755"><a href="#L-755"><span class="linenos"> 755</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="L-756"><a href="#L-756"><span class="linenos"> 756</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-757"><a href="#L-757"><span class="linenos"> 757</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="L-758"><a href="#L-758"><span class="linenos"> 758</span></a>
</span><span id="L-759"><a href="#L-759"><span class="linenos"> 759</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-760"><a href="#L-760"><span class="linenos"> 760</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="L-761"><a href="#L-761"><span class="linenos"> 761</span></a>
</span><span id="L-762"><a href="#L-762"><span class="linenos"> 762</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="L-763"><a href="#L-763"><span class="linenos"> 763</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="L-764"><a href="#L-764"><span class="linenos"> 764</span></a>
</span><span id="L-765"><a href="#L-765"><span class="linenos"> 765</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-766"><a href="#L-766"><span class="linenos"> 766</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="L-767"><a href="#L-767"><span class="linenos"> 767</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-768"><a href="#L-768"><span class="linenos"> 768</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="L-769"><a href="#L-769"><span class="linenos"> 769</span></a>
</span><span id="L-770"><a href="#L-770"><span class="linenos"> 770</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="L-771"><a href="#L-771"><span class="linenos"> 771</span></a>
</span><span id="L-772"><a href="#L-772"><span class="linenos"> 772</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="L-773"><a href="#L-773"><span class="linenos"> 773</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="L-774"><a href="#L-774"><span class="linenos"> 774</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-775"><a href="#L-775"><span class="linenos"> 775</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="L-776"><a href="#L-776"><span class="linenos"> 776</span></a>
</span><span id="L-777"><a href="#L-777"><span class="linenos"> 777</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="L-778"><a href="#L-778"><span class="linenos"> 778</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="L-779"><a href="#L-779"><span class="linenos"> 779</span></a>    
</span><span id="L-780"><a href="#L-780"><span class="linenos"> 780</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-781"><a href="#L-781"><span class="linenos"> 781</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="L-782"><a href="#L-782"><span class="linenos"> 782</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-783"><a href="#L-783"><span class="linenos"> 783</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span><span id="L-784"><a href="#L-784"><span class="linenos"> 784</span></a>    
</span><span id="L-785"><a href="#L-785"><span class="linenos"> 785</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="L-786"><a href="#L-786"><span class="linenos"> 786</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span>
</span><span id="L-787"><a href="#L-787"><span class="linenos"> 787</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="L-788"><a href="#L-788"><span class="linenos"> 788</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-789"><a href="#L-789"><span class="linenos"> 789</span></a>
</span><span id="L-790"><a href="#L-790"><span class="linenos"> 790</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="L-791"><a href="#L-791"><span class="linenos"> 791</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="L-792"><a href="#L-792"><span class="linenos"> 792</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="L-793"><a href="#L-793"><span class="linenos"> 793</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="L-794"><a href="#L-794"><span class="linenos"> 794</span></a>        
</span><span id="L-795"><a href="#L-795"><span class="linenos"> 795</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="L-796"><a href="#L-796"><span class="linenos"> 796</span></a>    
</span><span id="L-797"><a href="#L-797"><span class="linenos"> 797</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-798"><a href="#L-798"><span class="linenos"> 798</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-799"><a href="#L-799"><span class="linenos"> 799</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="L-800"><a href="#L-800"><span class="linenos"> 800</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="L-801"><a href="#L-801"><span class="linenos"> 801</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="L-802"><a href="#L-802"><span class="linenos"> 802</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="L-803"><a href="#L-803"><span class="linenos"> 803</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="L-804"><a href="#L-804"><span class="linenos"> 804</span></a>            <span class="k">pass</span>
</span><span id="L-805"><a href="#L-805"><span class="linenos"> 805</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="L-806"><a href="#L-806"><span class="linenos"> 806</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-807"><a href="#L-807"><span class="linenos"> 807</span></a>    
</span><span id="L-808"><a href="#L-808"><span class="linenos"> 808</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-809"><a href="#L-809"><span class="linenos"> 809</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-810"><a href="#L-810"><span class="linenos"> 810</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="L-811"><a href="#L-811"><span class="linenos"> 811</span></a>
</span><span id="L-812"><a href="#L-812"><span class="linenos"> 812</span></a>
</span><span id="L-813"><a href="#L-813"><span class="linenos"> 813</span></a><span class="c1"># class StreamReaderProtocolCopy(OriginalStreamReaderProtocol):</span>
</span><span id="L-814"><a href="#L-814"><span class="linenos"> 814</span></a><span class="c1">#     def __init__(self, manager: TcpStreamManager, original_stream_reader_protocol: OriginalStreamReaderProtocol) -&gt; None:</span>
</span><span id="L-815"><a href="#L-815"><span class="linenos"> 815</span></a><span class="c1">#         self._stream_manager = manager</span>
</span><span id="L-816"><a href="#L-816"><span class="linenos"> 816</span></a><span class="c1">#         original_dict: dict = copy(original_stream_reader_protocol.__dict__)</span>
</span><span id="L-817"><a href="#L-817"><span class="linenos"> 817</span></a><span class="c1">#         original_dict.pop(&#39;_stream_manager&#39;, None)</span>
</span><span id="L-818"><a href="#L-818"><span class="linenos"> 818</span></a><span class="c1">#         original_dict.pop(&#39;_client_connected_cb&#39;, None)</span>
</span><span id="L-819"><a href="#L-819"><span class="linenos"> 819</span></a><span class="c1">#         self.__dict__.update(original_dict)</span>
</span><span id="L-820"><a href="#L-820"><span class="linenos"> 820</span></a><span class="c1">#         self._original__client_connected_cb = None</span>
</span><span id="L-821"><a href="#L-821"><span class="linenos"> 821</span></a><span class="c1">#         self._client_connected_cb = original_stream_reader_protocol._client_connected_cb</span>
</span><span id="L-822"><a href="#L-822"><span class="linenos"> 822</span></a>    
</span><span id="L-823"><a href="#L-823"><span class="linenos"> 823</span></a><span class="c1">#     async def _wrapper__client_connected_cb(self, reader: OriginalStreamReader, writer: OriginalStreamWriter):</span>
</span><span id="L-824"><a href="#L-824"><span class="linenos"> 824</span></a><span class="c1">#         self._stream_writer = StreamWriterCopy(self._stream_manager, writer)</span>
</span><span id="L-825"><a href="#L-825"><span class="linenos"> 825</span></a><span class="c1">#         if self._original__client_connected_cb is not None:</span>
</span><span id="L-826"><a href="#L-826"><span class="linenos"> 826</span></a><span class="c1">#             await self._original__client_connected_cb(reader, self._stream_writer)</span>
</span><span id="L-827"><a href="#L-827"><span class="linenos"> 827</span></a>    
</span><span id="L-828"><a href="#L-828"><span class="linenos"> 828</span></a><span class="c1">#     @property</span>
</span><span id="L-829"><a href="#L-829"><span class="linenos"> 829</span></a><span class="c1">#     def _client_connected_cb(self):</span>
</span><span id="L-830"><a href="#L-830"><span class="linenos"> 830</span></a><span class="c1">#         if self._original__client_connected_cb is None:</span>
</span><span id="L-831"><a href="#L-831"><span class="linenos"> 831</span></a><span class="c1">#             return None</span>
</span><span id="L-832"><a href="#L-832"><span class="linenos"> 832</span></a><span class="c1">#         else:</span>
</span><span id="L-833"><a href="#L-833"><span class="linenos"> 833</span></a><span class="c1">#             return self._wrapper__client_connected_cb</span>
</span><span id="L-834"><a href="#L-834"><span class="linenos"> 834</span></a>    
</span><span id="L-835"><a href="#L-835"><span class="linenos"> 835</span></a><span class="c1">#     @_client_connected_cb.setter</span>
</span><span id="L-836"><a href="#L-836"><span class="linenos"> 836</span></a><span class="c1">#     def _client_connected_cb(self, value):</span>
</span><span id="L-837"><a href="#L-837"><span class="linenos"> 837</span></a><span class="c1">#         self._original__client_connected_cb = value</span>
</span><span id="L-838"><a href="#L-838"><span class="linenos"> 838</span></a>
</span><span id="L-839"><a href="#L-839"><span class="linenos"> 839</span></a>
</span><span id="L-840"><a href="#L-840"><span class="linenos"> 840</span></a><span class="k">class</span> <span class="nc">TcpStreamReaderProtocol</span><span class="p">(</span><span class="n">OriginalStreamReaderProtocol</span><span class="p">,</span> <span class="n">StreamReaderProtocolAbstract</span><span class="p">):</span>
</span><span id="L-841"><a href="#L-841"><span class="linenos"> 841</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-842"><a href="#L-842"><span class="linenos"> 842</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-843"><a href="#L-843"><span class="linenos"> 843</span></a>
</span><span id="L-844"><a href="#L-844"><span class="linenos"> 844</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-845"><a href="#L-845"><span class="linenos"> 845</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-846"><a href="#L-846"><span class="linenos"> 846</span></a>
</span><span id="L-847"><a href="#L-847"><span class="linenos"> 847</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="L-848"><a href="#L-848"><span class="linenos"> 848</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="L-849"><a href="#L-849"><span class="linenos"> 849</span></a>
</span><span id="L-850"><a href="#L-850"><span class="linenos"> 850</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="L-851"><a href="#L-851"><span class="linenos"> 851</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="L-852"><a href="#L-852"><span class="linenos"> 852</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="L-853"><a href="#L-853"><span class="linenos"> 853</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="L-854"><a href="#L-854"><span class="linenos"> 854</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="L-855"><a href="#L-855"><span class="linenos"> 855</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="L-856"><a href="#L-856"><span class="linenos"> 856</span></a>            <span class="p">}</span>
</span><span id="L-857"><a href="#L-857"><span class="linenos"> 857</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="L-858"><a href="#L-858"><span class="linenos"> 858</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="L-859"><a href="#L-859"><span class="linenos"> 859</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="L-860"><a href="#L-860"><span class="linenos"> 860</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="L-861"><a href="#L-861"><span class="linenos"> 861</span></a>            <span class="k">return</span>
</span><span id="L-862"><a href="#L-862"><span class="linenos"> 862</span></a>        
</span><span id="L-863"><a href="#L-863"><span class="linenos"> 863</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="L-864"><a href="#L-864"><span class="linenos"> 864</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="L-865"><a href="#L-865"><span class="linenos"> 865</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-866"><a href="#L-866"><span class="linenos"> 866</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="L-867"><a href="#L-867"><span class="linenos"> 867</span></a>
</span><span id="L-868"><a href="#L-868"><span class="linenos"> 868</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="L-869"><a href="#L-869"><span class="linenos"> 869</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-870"><a href="#L-870"><span class="linenos"> 870</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="L-871"><a href="#L-871"><span class="linenos"> 871</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="L-872"><a href="#L-872"><span class="linenos"> 872</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="L-873"><a href="#L-873"><span class="linenos"> 873</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="L-874"><a href="#L-874"><span class="linenos"> 874</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="L-875"><a href="#L-875"><span class="linenos"> 875</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="L-876"><a href="#L-876"><span class="linenos"> 876</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="L-877"><a href="#L-877"><span class="linenos"> 877</span></a>            
</span><span id="L-878"><a href="#L-878"><span class="linenos"> 878</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-879"><a href="#L-879"><span class="linenos"> 879</span></a>
</span><span id="L-880"><a href="#L-880"><span class="linenos"> 880</span></a>
</span><span id="L-881"><a href="#L-881"><span class="linenos"> 881</span></a><span class="c1"># class StreamWriterCopy(OriginalStreamWriter):</span>
</span><span id="L-882"><a href="#L-882"><span class="linenos"> 882</span></a><span class="c1">#     def __init__(self, manager: TcpStreamManager, original_stream_writer: OriginalStreamWriter) -&gt; None:</span>
</span><span id="L-883"><a href="#L-883"><span class="linenos"> 883</span></a><span class="c1">#         self._stream_manager = manager</span>
</span><span id="L-884"><a href="#L-884"><span class="linenos"> 884</span></a><span class="c1">#         self._output_to_client: DynamicListOfPiecesDequeWithLengthControl = self._stream_manager.output_to_client_container_type(</span>
</span><span id="L-885"><a href="#L-885"><span class="linenos"> 885</span></a><span class="c1">#             external_data_length=self._stream_manager.io_memory_management.global_out__data_full_size)</span>
</span><span id="L-886"><a href="#L-886"><span class="linenos"> 886</span></a><span class="c1">#         self.socket_write_fixed_buffer_size: ValueExistence = self._stream_manager.io_memory_management.socket_write_fixed_buffer_size</span>
</span><span id="L-887"><a href="#L-887"><span class="linenos"> 887</span></a><span class="c1">#         self._autonomous_writer_future: Task = None</span>
</span><span id="L-888"><a href="#L-888"><span class="linenos"> 888</span></a><span class="c1">#         self._autonomous_writer_future_stop_requessted: bool = False</span>
</span><span id="L-889"><a href="#L-889"><span class="linenos"> 889</span></a><span class="c1">#         self._autonomous_writer_drain_enough_futures: List[Future] = list()</span>
</span><span id="L-890"><a href="#L-890"><span class="linenos"> 890</span></a><span class="c1">#         original_dict: dict = copy(original_stream_writer.__dict__)</span>
</span><span id="L-891"><a href="#L-891"><span class="linenos"> 891</span></a><span class="c1">#         original_dict.pop(&#39;_stream_manager&#39;, None)</span>
</span><span id="L-892"><a href="#L-892"><span class="linenos"> 892</span></a><span class="c1">#         original_dict.pop(&#39;_output_to_client&#39;, None)</span>
</span><span id="L-893"><a href="#L-893"><span class="linenos"> 893</span></a><span class="c1">#         original_dict.pop(&#39;_autonomous_writer_future_stop_requessted&#39;, None)</span>
</span><span id="L-894"><a href="#L-894"><span class="linenos"> 894</span></a><span class="c1">#         self.__dict__.update(original_dict)</span>
</span><span id="L-895"><a href="#L-895"><span class="linenos"> 895</span></a>    
</span><span id="L-896"><a href="#L-896"><span class="linenos"> 896</span></a><span class="c1">#     def optimized_write(self, data):</span>
</span><span id="L-897"><a href="#L-897"><span class="linenos"> 897</span></a><span class="c1">#         # self._output_to_client.add_piece_of_data(data)</span>
</span><span id="L-898"><a href="#L-898"><span class="linenos"> 898</span></a><span class="c1">#         self.write(data)</span>
</span><span id="L-899"><a href="#L-899"><span class="linenos"> 899</span></a>
</span><span id="L-900"><a href="#L-900"><span class="linenos"> 900</span></a><span class="c1">#     def owrite(self, data):</span>
</span><span id="L-901"><a href="#L-901"><span class="linenos"> 901</span></a><span class="c1">#         return self.optimized_write(data)</span>
</span><span id="L-902"><a href="#L-902"><span class="linenos"> 902</span></a>
</span><span id="L-903"><a href="#L-903"><span class="linenos"> 903</span></a><span class="c1">#     async def partial_drain(self):</span>
</span><span id="L-904"><a href="#L-904"><span class="linenos"> 904</span></a><span class="c1">#         await self.drain()</span>
</span><span id="L-905"><a href="#L-905"><span class="linenos"> 905</span></a><span class="c1">#         # another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)</span>
</span><span id="L-906"><a href="#L-906"><span class="linenos"> 906</span></a><span class="c1">#         # while another_piece_of_data:</span>
</span><span id="L-907"><a href="#L-907"><span class="linenos"> 907</span></a><span class="c1">#         #     self.write(another_piece_of_data)</span>
</span><span id="L-908"><a href="#L-908"><span class="linenos"> 908</span></a><span class="c1">#         #     await self.drain()</span>
</span><span id="L-909"><a href="#L-909"><span class="linenos"> 909</span></a><span class="c1">#         #     another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)</span>
</span><span id="L-910"><a href="#L-910"><span class="linenos"> 910</span></a>
</span><span id="L-911"><a href="#L-911"><span class="linenos"> 911</span></a><span class="c1">#     async def pdrain(self):</span>
</span><span id="L-912"><a href="#L-912"><span class="linenos"> 912</span></a><span class="c1">#         return await self.partial_drain()</span>
</span><span id="L-913"><a href="#L-913"><span class="linenos"> 913</span></a>
</span><span id="L-914"><a href="#L-914"><span class="linenos"> 914</span></a><span class="c1">#     async def full_drain(self):</span>
</span><span id="L-915"><a href="#L-915"><span class="linenos"> 915</span></a><span class="c1">#         await self.pdrain()</span>
</span><span id="L-916"><a href="#L-916"><span class="linenos"> 916</span></a><span class="c1">#         rest_of_the_data_size = self._output_to_client.size()</span>
</span><span id="L-917"><a href="#L-917"><span class="linenos"> 917</span></a><span class="c1">#         if rest_of_the_data_size:</span>
</span><span id="L-918"><a href="#L-918"><span class="linenos"> 918</span></a><span class="c1">#             another_piece_of_data = self._output_to_client.get_data(rest_of_the_data_size)</span>
</span><span id="L-919"><a href="#L-919"><span class="linenos"> 919</span></a><span class="c1">#             self.write(another_piece_of_data)</span>
</span><span id="L-920"><a href="#L-920"><span class="linenos"> 920</span></a><span class="c1">#             await self.drain()</span>
</span><span id="L-921"><a href="#L-921"><span class="linenos"> 921</span></a>
</span><span id="L-922"><a href="#L-922"><span class="linenos"> 922</span></a><span class="c1">#     async def fdrain(self):</span>
</span><span id="L-923"><a href="#L-923"><span class="linenos"> 923</span></a><span class="c1">#         return await self.full_drain()</span>
</span><span id="L-924"><a href="#L-924"><span class="linenos"> 924</span></a>    
</span><span id="L-925"><a href="#L-925"><span class="linenos"> 925</span></a><span class="c1">#     def _release_autonomous_writer_waiters(self):</span>
</span><span id="L-926"><a href="#L-926"><span class="linenos"> 926</span></a><span class="c1">#         current_size = self._output_to_client.size()</span>
</span><span id="L-927"><a href="#L-927"><span class="linenos"> 927</span></a><span class="c1">#         autonomous_writer_drain_enough_futures_buff = self._autonomous_writer_drain_enough_futures</span>
</span><span id="L-928"><a href="#L-928"><span class="linenos"> 928</span></a><span class="c1">#         self._autonomous_writer_drain_enough_futures = type(autonomous_writer_drain_enough_futures_buff)()</span>
</span><span id="L-929"><a href="#L-929"><span class="linenos"> 929</span></a><span class="c1">#         for item in autonomous_writer_drain_enough_futures_buff:</span>
</span><span id="L-930"><a href="#L-930"><span class="linenos"> 930</span></a><span class="c1">#             lower_water_size, future = item</span>
</span><span id="L-931"><a href="#L-931"><span class="linenos"> 931</span></a><span class="c1">#             if current_size &lt; lower_water_size:</span>
</span><span id="L-932"><a href="#L-932"><span class="linenos"> 932</span></a><span class="c1">#                 if (not future.done()) and (not future.cancelled()):</span>
</span><span id="L-933"><a href="#L-933"><span class="linenos"> 933</span></a><span class="c1">#                     future.set_result(None)</span>
</span><span id="L-934"><a href="#L-934"><span class="linenos"> 934</span></a>
</span><span id="L-935"><a href="#L-935"><span class="linenos"> 935</span></a><span class="c1">#             if (not future.done()) and (not future.cancelled()):</span>
</span><span id="L-936"><a href="#L-936"><span class="linenos"> 936</span></a><span class="c1">#                 self._autonomous_writer_drain_enough_futures.append(item)</span>
</span><span id="L-937"><a href="#L-937"><span class="linenos"> 937</span></a>    
</span><span id="L-938"><a href="#L-938"><span class="linenos"> 938</span></a><span class="c1">#     async def _autonomous_writer_impl(self):</span>
</span><span id="L-939"><a href="#L-939"><span class="linenos"> 939</span></a><span class="c1">#         ty = TimedYield(0)</span>
</span><span id="L-940"><a href="#L-940"><span class="linenos"> 940</span></a><span class="c1">#         while not self._autonomous_writer_future_stop_requessted:</span>
</span><span id="L-941"><a href="#L-941"><span class="linenos"> 941</span></a><span class="c1">#             another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)</span>
</span><span id="L-942"><a href="#L-942"><span class="linenos"> 942</span></a><span class="c1">#             self._release_autonomous_writer_waiters()</span>
</span><span id="L-943"><a href="#L-943"><span class="linenos"> 943</span></a><span class="c1">#             while another_piece_of_data:</span>
</span><span id="L-944"><a href="#L-944"><span class="linenos"> 944</span></a><span class="c1">#                 self.write(another_piece_of_data)</span>
</span><span id="L-945"><a href="#L-945"><span class="linenos"> 945</span></a><span class="c1">#                 await self.drain()</span>
</span><span id="L-946"><a href="#L-946"><span class="linenos"> 946</span></a><span class="c1">#                 another_piece_of_data = self._output_to_client.get_data(self.socket_write_fixed_buffer_size.value)</span>
</span><span id="L-947"><a href="#L-947"><span class="linenos"> 947</span></a><span class="c1">#                 self._release_autonomous_writer_waiters()</span>
</span><span id="L-948"><a href="#L-948"><span class="linenos"> 948</span></a>            
</span><span id="L-949"><a href="#L-949"><span class="linenos"> 949</span></a><span class="c1">#             await ty()</span>
</span><span id="L-950"><a href="#L-950"><span class="linenos"> 950</span></a>    
</span><span id="L-951"><a href="#L-951"><span class="linenos"> 951</span></a><span class="c1">#     def start_autonomous_writer(self):</span>
</span><span id="L-952"><a href="#L-952"><span class="linenos"> 952</span></a><span class="c1">#         self._autonomous_writer_future = create_task(self._autonomous_writer_impl)</span>
</span><span id="L-953"><a href="#L-953"><span class="linenos"> 953</span></a>    
</span><span id="L-954"><a href="#L-954"><span class="linenos"> 954</span></a><span class="c1">#     def start_aw(self):</span>
</span><span id="L-955"><a href="#L-955"><span class="linenos"> 955</span></a><span class="c1">#         return self.start_autonomous_writer()</span>
</span><span id="L-956"><a href="#L-956"><span class="linenos"> 956</span></a>    
</span><span id="L-957"><a href="#L-957"><span class="linenos"> 957</span></a><span class="c1">#     async def stop_autonomous_writer(self, timeout: Optional[Union[int, float]] = 0):</span>
</span><span id="L-958"><a href="#L-958"><span class="linenos"> 958</span></a><span class="c1">#         &quot;&quot;&quot;_summary_</span>
</span><span id="L-959"><a href="#L-959"><span class="linenos"> 959</span></a>
</span><span id="L-960"><a href="#L-960"><span class="linenos"> 960</span></a><span class="c1">#         Args:</span>
</span><span id="L-961"><a href="#L-961"><span class="linenos"> 961</span></a><span class="c1">#             timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-962"><a href="#L-962"><span class="linenos"> 962</span></a>
</span><span id="L-963"><a href="#L-963"><span class="linenos"> 963</span></a><span class="c1">#         Returns:</span>
</span><span id="L-964"><a href="#L-964"><span class="linenos"> 964</span></a><span class="c1">#             _type_: _description_</span>
</span><span id="L-965"><a href="#L-965"><span class="linenos"> 965</span></a><span class="c1">#         &quot;&quot;&quot;</span>
</span><span id="L-966"><a href="#L-966"><span class="linenos"> 966</span></a><span class="c1">#         result = None</span>
</span><span id="L-967"><a href="#L-967"><span class="linenos"> 967</span></a><span class="c1">#         if timeout is None:</span>
</span><span id="L-968"><a href="#L-968"><span class="linenos"> 968</span></a><span class="c1">#             timeout = self._stream_manager.autonomous_writer_stop_default_timeout</span>
</span><span id="L-969"><a href="#L-969"><span class="linenos"> 969</span></a>        
</span><span id="L-970"><a href="#L-970"><span class="linenos"> 970</span></a><span class="c1">#         if self._autonomous_writer_future and (not self._autonomous_writer_future_stop_requessted):</span>
</span><span id="L-971"><a href="#L-971"><span class="linenos"> 971</span></a><span class="c1">#             self._autonomous_writer_future_stop_requessted = True</span>
</span><span id="L-972"><a href="#L-972"><span class="linenos"> 972</span></a><span class="c1">#             if timeout:</span>
</span><span id="L-973"><a href="#L-973"><span class="linenos"> 973</span></a><span class="c1">#                 result = await asyncio.wait_for(self._autonomous_writer_future, timeout)</span>
</span><span id="L-974"><a href="#L-974"><span class="linenos"> 974</span></a><span class="c1">#             else:</span>
</span><span id="L-975"><a href="#L-975"><span class="linenos"> 975</span></a><span class="c1">#                 result = await self._autonomous_writer_future</span>
</span><span id="L-976"><a href="#L-976"><span class="linenos"> 976</span></a>            
</span><span id="L-977"><a href="#L-977"><span class="linenos"> 977</span></a><span class="c1">#             self._autonomous_writer_future = None</span>
</span><span id="L-978"><a href="#L-978"><span class="linenos"> 978</span></a><span class="c1">#             self._autonomous_writer_future_stop_requessted = False</span>
</span><span id="L-979"><a href="#L-979"><span class="linenos"> 979</span></a>        
</span><span id="L-980"><a href="#L-980"><span class="linenos"> 980</span></a><span class="c1">#         return result</span>
</span><span id="L-981"><a href="#L-981"><span class="linenos"> 981</span></a>    
</span><span id="L-982"><a href="#L-982"><span class="linenos"> 982</span></a><span class="c1">#     def stop_aw(self, timeout: Optional[Union[int, float]] = 0):</span>
</span><span id="L-983"><a href="#L-983"><span class="linenos"> 983</span></a><span class="c1">#         &quot;&quot;&quot;_summary_</span>
</span><span id="L-984"><a href="#L-984"><span class="linenos"> 984</span></a>
</span><span id="L-985"><a href="#L-985"><span class="linenos"> 985</span></a><span class="c1">#         Args:</span>
</span><span id="L-986"><a href="#L-986"><span class="linenos"> 986</span></a><span class="c1">#             timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-987"><a href="#L-987"><span class="linenos"> 987</span></a>
</span><span id="L-988"><a href="#L-988"><span class="linenos"> 988</span></a><span class="c1">#         Returns:</span>
</span><span id="L-989"><a href="#L-989"><span class="linenos"> 989</span></a><span class="c1">#             _type_: _description_</span>
</span><span id="L-990"><a href="#L-990"><span class="linenos"> 990</span></a><span class="c1">#         &quot;&quot;&quot;</span>
</span><span id="L-991"><a href="#L-991"><span class="linenos"> 991</span></a><span class="c1">#         return self.stop_autonomous_writer(timeout)</span>
</span><span id="L-992"><a href="#L-992"><span class="linenos"> 992</span></a>    
</span><span id="L-993"><a href="#L-993"><span class="linenos"> 993</span></a><span class="c1">#     async def autonomous_writer_drain_enough(self, lower_water_size: Optional[int] = None):</span>
</span><span id="L-994"><a href="#L-994"><span class="linenos"> 994</span></a><span class="c1">#         if lower_water_size is None:</span>
</span><span id="L-995"><a href="#L-995"><span class="linenos"> 995</span></a><span class="c1">#             lower_water_size = self.socket_write_fixed_buffer_size.value * 2</span>
</span><span id="L-996"><a href="#L-996"><span class="linenos"> 996</span></a>        
</span><span id="L-997"><a href="#L-997"><span class="linenos"> 997</span></a><span class="c1">#         if lower_water_size &lt;= self._output_to_client.size():</span>
</span><span id="L-998"><a href="#L-998"><span class="linenos"> 998</span></a><span class="c1">#             future: Future = self._loop.create_future()</span>
</span><span id="L-999"><a href="#L-999"><span class="linenos"> 999</span></a><span class="c1">#             self._autonomous_writer_drain_enough_futures.append((lower_water_size, future))</span>
</span><span id="L-1000"><a href="#L-1000"><span class="linenos">1000</span></a><span class="c1">#             await future</span>
</span><span id="L-1001"><a href="#L-1001"><span class="linenos">1001</span></a>
</span><span id="L-1002"><a href="#L-1002"><span class="linenos">1002</span></a>    
</span><span id="L-1003"><a href="#L-1003"><span class="linenos">1003</span></a><span class="c1">#     async def aw_drain_enough(self):</span>
</span><span id="L-1004"><a href="#L-1004"><span class="linenos">1004</span></a><span class="c1">#         await self.autonomous_writer_drain_enough()</span>
</span><span id="L-1005"><a href="#L-1005"><span class="linenos">1005</span></a>
</span><span id="L-1006"><a href="#L-1006"><span class="linenos">1006</span></a>
</span><span id="L-1007"><a href="#L-1007"><span class="linenos">1007</span></a><span class="k">class</span> <span class="nc">TcpStreamWriter</span><span class="p">(</span><span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="n">StreamWriterAbstract</span><span class="p">):</span>
</span><span id="L-1008"><a href="#L-1008"><span class="linenos">1008</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1009"><a href="#L-1009"><span class="linenos">1009</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-1010"><a href="#L-1010"><span class="linenos">1010</span></a>
</span><span id="L-1011"><a href="#L-1011"><span class="linenos">1011</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1012"><a href="#L-1012"><span class="linenos">1012</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="L-1013"><a href="#L-1013"><span class="linenos">1013</span></a>
</span><span id="L-1014"><a href="#L-1014"><span class="linenos">1014</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_stream_manager</span>
</span><span id="L-1015"><a href="#L-1015"><span class="linenos">1015</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">output_to_client_container_type</span><span class="p">(</span>
</span><span id="L-1016"><a href="#L-1016"><span class="linenos">1016</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="L-1017"><a href="#L-1017"><span class="linenos">1017</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="L-1018"><a href="#L-1018"><span class="linenos">1018</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">:</span> <span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-1019"><a href="#L-1019"><span class="linenos">1019</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-1020"><a href="#L-1020"><span class="linenos">1020</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Future</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="L-1021"><a href="#L-1021"><span class="linenos">1021</span></a>
</span><span id="L-1022"><a href="#L-1022"><span class="linenos">1022</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-1023"><a href="#L-1023"><span class="linenos">1023</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-1024"><a href="#L-1024"><span class="linenos">1024</span></a>        <span class="c1"># self.write(data)</span>
</span><span id="L-1025"><a href="#L-1025"><span class="linenos">1025</span></a>
</span><span id="L-1026"><a href="#L-1026"><span class="linenos">1026</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-1027"><a href="#L-1027"><span class="linenos">1027</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-1028"><a href="#L-1028"><span class="linenos">1028</span></a>
</span><span id="L-1029"><a href="#L-1029"><span class="linenos">1029</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1030"><a href="#L-1030"><span class="linenos">1030</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-1031"><a href="#L-1031"><span class="linenos">1031</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="L-1032"><a href="#L-1032"><span class="linenos">1032</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-1033"><a href="#L-1033"><span class="linenos">1033</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-1034"><a href="#L-1034"><span class="linenos">1034</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-1035"><a href="#L-1035"><span class="linenos">1035</span></a>
</span><span id="L-1036"><a href="#L-1036"><span class="linenos">1036</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1037"><a href="#L-1037"><span class="linenos">1037</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span><span id="L-1038"><a href="#L-1038"><span class="linenos">1038</span></a>
</span><span id="L-1039"><a href="#L-1039"><span class="linenos">1039</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1040"><a href="#L-1040"><span class="linenos">1040</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="L-1041"><a href="#L-1041"><span class="linenos">1041</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-1042"><a href="#L-1042"><span class="linenos">1042</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="L-1043"><a href="#L-1043"><span class="linenos">1043</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="L-1044"><a href="#L-1044"><span class="linenos">1044</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-1045"><a href="#L-1045"><span class="linenos">1045</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-1046"><a href="#L-1046"><span class="linenos">1046</span></a>
</span><span id="L-1047"><a href="#L-1047"><span class="linenos">1047</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1048"><a href="#L-1048"><span class="linenos">1048</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="L-1049"><a href="#L-1049"><span class="linenos">1049</span></a>    
</span><span id="L-1050"><a href="#L-1050"><span class="linenos">1050</span></a>    <span class="k">def</span> <span class="nf">_release_autonomous_writer_waiters</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1051"><a href="#L-1051"><span class="linenos">1051</span></a>        <span class="n">current_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="L-1052"><a href="#L-1052"><span class="linenos">1052</span></a>        <span class="n">autonomous_writer_drain_enough_futures_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span>
</span><span id="L-1053"><a href="#L-1053"><span class="linenos">1053</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">)()</span>
</span><span id="L-1054"><a href="#L-1054"><span class="linenos">1054</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">:</span>
</span><span id="L-1055"><a href="#L-1055"><span class="linenos">1055</span></a>            <span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="L-1056"><a href="#L-1056"><span class="linenos">1056</span></a>            <span class="k">if</span> <span class="n">current_size</span> <span class="o">&lt;</span> <span class="n">lower_water_size</span><span class="p">:</span>
</span><span id="L-1057"><a href="#L-1057"><span class="linenos">1057</span></a>                <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-1058"><a href="#L-1058"><span class="linenos">1058</span></a>                    <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="L-1059"><a href="#L-1059"><span class="linenos">1059</span></a>
</span><span id="L-1060"><a href="#L-1060"><span class="linenos">1060</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="L-1061"><a href="#L-1061"><span class="linenos">1061</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="L-1062"><a href="#L-1062"><span class="linenos">1062</span></a>    
</span><span id="L-1063"><a href="#L-1063"><span class="linenos">1063</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_autonomous_writer_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1064"><a href="#L-1064"><span class="linenos">1064</span></a>        <span class="n">ty</span> <span class="o">=</span> <span class="n">TimedYield</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="L-1065"><a href="#L-1065"><span class="linenos">1065</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span>
</span><span id="L-1066"><a href="#L-1066"><span class="linenos">1066</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-1067"><a href="#L-1067"><span class="linenos">1067</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="L-1068"><a href="#L-1068"><span class="linenos">1068</span></a>            <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="L-1069"><a href="#L-1069"><span class="linenos">1069</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="L-1070"><a href="#L-1070"><span class="linenos">1070</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="L-1071"><a href="#L-1071"><span class="linenos">1071</span></a>                <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="L-1072"><a href="#L-1072"><span class="linenos">1072</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="L-1073"><a href="#L-1073"><span class="linenos">1073</span></a>            
</span><span id="L-1074"><a href="#L-1074"><span class="linenos">1074</span></a>            <span class="k">await</span> <span class="n">ty</span><span class="p">()</span>
</span><span id="L-1075"><a href="#L-1075"><span class="linenos">1075</span></a>    
</span><span id="L-1076"><a href="#L-1076"><span class="linenos">1076</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1077"><a href="#L-1077"><span class="linenos">1077</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span><span id="L-1078"><a href="#L-1078"><span class="linenos">1078</span></a>    
</span><span id="L-1079"><a href="#L-1079"><span class="linenos">1079</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1080"><a href="#L-1080"><span class="linenos">1080</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="L-1081"><a href="#L-1081"><span class="linenos">1081</span></a>    
</span><span id="L-1082"><a href="#L-1082"><span class="linenos">1082</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-1083"><a href="#L-1083"><span class="linenos">1083</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-1084"><a href="#L-1084"><span class="linenos">1084</span></a>
</span><span id="L-1085"><a href="#L-1085"><span class="linenos">1085</span></a><span class="sd">        Args:</span>
</span><span id="L-1086"><a href="#L-1086"><span class="linenos">1086</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-1087"><a href="#L-1087"><span class="linenos">1087</span></a>
</span><span id="L-1088"><a href="#L-1088"><span class="linenos">1088</span></a><span class="sd">        Returns:</span>
</span><span id="L-1089"><a href="#L-1089"><span class="linenos">1089</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-1090"><a href="#L-1090"><span class="linenos">1090</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-1091"><a href="#L-1091"><span class="linenos">1091</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-1092"><a href="#L-1092"><span class="linenos">1092</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1093"><a href="#L-1093"><span class="linenos">1093</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="L-1094"><a href="#L-1094"><span class="linenos">1094</span></a>        
</span><span id="L-1095"><a href="#L-1095"><span class="linenos">1095</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="L-1096"><a href="#L-1096"><span class="linenos">1096</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="L-1097"><a href="#L-1097"><span class="linenos">1097</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="L-1098"><a href="#L-1098"><span class="linenos">1098</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="L-1099"><a href="#L-1099"><span class="linenos">1099</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="L-1100"><a href="#L-1100"><span class="linenos">1100</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="L-1101"><a href="#L-1101"><span class="linenos">1101</span></a>            
</span><span id="L-1102"><a href="#L-1102"><span class="linenos">1102</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="L-1103"><a href="#L-1103"><span class="linenos">1103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="L-1104"><a href="#L-1104"><span class="linenos">1104</span></a>        
</span><span id="L-1105"><a href="#L-1105"><span class="linenos">1105</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="L-1106"><a href="#L-1106"><span class="linenos">1106</span></a>    
</span><span id="L-1107"><a href="#L-1107"><span class="linenos">1107</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="L-1108"><a href="#L-1108"><span class="linenos">1108</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="L-1109"><a href="#L-1109"><span class="linenos">1109</span></a>
</span><span id="L-1110"><a href="#L-1110"><span class="linenos">1110</span></a><span class="sd">        Args:</span>
</span><span id="L-1111"><a href="#L-1111"><span class="linenos">1111</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="L-1112"><a href="#L-1112"><span class="linenos">1112</span></a>
</span><span id="L-1113"><a href="#L-1113"><span class="linenos">1113</span></a><span class="sd">        Returns:</span>
</span><span id="L-1114"><a href="#L-1114"><span class="linenos">1114</span></a><span class="sd">            _type_: _description_</span>
</span><span id="L-1115"><a href="#L-1115"><span class="linenos">1115</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="L-1116"><a href="#L-1116"><span class="linenos">1116</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span><span id="L-1117"><a href="#L-1117"><span class="linenos">1117</span></a>    
</span><span id="L-1118"><a href="#L-1118"><span class="linenos">1118</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="L-1119"><a href="#L-1119"><span class="linenos">1119</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="L-1120"><a href="#L-1120"><span class="linenos">1120</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="L-1121"><a href="#L-1121"><span class="linenos">1121</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="L-1122"><a href="#L-1122"><span class="linenos">1122</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="L-1123"><a href="#L-1123"><span class="linenos">1123</span></a>        
</span><span id="L-1124"><a href="#L-1124"><span class="linenos">1124</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="L-1125"><a href="#L-1125"><span class="linenos">1125</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="L-1126"><a href="#L-1126"><span class="linenos">1126</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="L-1127"><a href="#L-1127"><span class="linenos">1127</span></a>            <span class="k">await</span> <span class="n">future</span>
</span><span id="L-1128"><a href="#L-1128"><span class="linenos">1128</span></a>    
</span><span id="L-1129"><a href="#L-1129"><span class="linenos">1129</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1130"><a href="#L-1130"><span class="linenos">1130</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span><span id="L-1131"><a href="#L-1131"><span class="linenos">1131</span></a>    
</span><span id="L-1132"><a href="#L-1132"><span class="linenos">1132</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-1133"><a href="#L-1133"><span class="linenos">1133</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="L-1134"><a href="#L-1134"><span class="linenos">1134</span></a>    
</span><span id="L-1135"><a href="#L-1135"><span class="linenos">1135</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-1136"><a href="#L-1136"><span class="linenos">1136</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-1137"><a href="#L-1137"><span class="linenos">1137</span></a>    
</span><span id="L-1138"><a href="#L-1138"><span class="linenos">1138</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="L-1139"><a href="#L-1139"><span class="linenos">1139</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="L-1140"><a href="#L-1140"><span class="linenos">1140</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
</span><span id="L-1141"><a href="#L-1141"><span class="linenos">1141</span></a>    
</span><span id="L-1142"><a href="#L-1142"><span class="linenos">1142</span></a>    <span class="nd">@asynccontextmanager</span>
</span><span id="L-1143"><a href="#L-1143"><span class="linenos">1143</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1144"><a href="#L-1144"><span class="linenos">1144</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="L-1145"><a href="#L-1145"><span class="linenos">1145</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="L-1146"><a href="#L-1146"><span class="linenos">1146</span></a>            <span class="k">yield</span>
</span><span id="L-1147"><a href="#L-1147"><span class="linenos">1147</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="L-1148"><a href="#L-1148"><span class="linenos">1148</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">()</span>
</span><span id="L-1149"><a href="#L-1149"><span class="linenos">1149</span></a>    
</span><span id="L-1150"><a href="#L-1150"><span class="linenos">1150</span></a>    <span class="n">aw</span> <span class="o">=</span> <span class="n">autonomous_writer</span>
</span><span id="L-1151"><a href="#L-1151"><span class="linenos">1151</span></a>
</span><span id="L-1152"><a href="#L-1152"><span class="linenos">1152</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="L-1153"><a href="#L-1153"><span class="linenos">1153</span></a>        <span class="k">pass</span>
</span><span id="L-1154"><a href="#L-1154"><span class="linenos">1154</span></a>
</span><span id="L-1155"><a href="#L-1155"><span class="linenos">1155</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc</span><span class="p">,</span> <span class="n">tb</span><span class="p">):</span>
</span><span id="L-1156"><a href="#L-1156"><span class="linenos">1156</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span></pre></div>


            </section>
                <section id="StreamType">
                            <input id="StreamType-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">StreamType</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="StreamType-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#StreamType"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="StreamType-49"><a href="#StreamType-49"><span class="linenos">49</span></a><span class="k">class</span> <span class="nc">StreamType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="StreamType-50"><a href="#StreamType-50"><span class="linenos">50</span></a>    <span class="n">general</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="StreamType-51"><a href="#StreamType-51"><span class="linenos">51</span></a>    <span class="n">message_based_anonymous</span> <span class="o">=</span> <span class="mi">1</span>
</span><span id="StreamType-52"><a href="#StreamType-52"><span class="linenos">52</span></a>    <span class="n">message_based_names</span> <span class="o">=</span> <span class="mi">2</span>
</span><span id="StreamType-53"><a href="#StreamType-53"><span class="linenos">53</span></a>    <span class="n">gate</span> <span class="o">=</span> <span class="mi">3</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="StreamType.general" class="classattr">
                                <div class="attr variable">
            <span class="name">general</span>        =
<span class="default_value">&lt;<a href="#StreamType.general">StreamType.general</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#StreamType.general"></a>
    
    

                            </div>
                            <div id="StreamType.message_based_anonymous" class="classattr">
                                <div class="attr variable">
            <span class="name">message_based_anonymous</span>        =
<span class="default_value">&lt;<a href="#StreamType.message_based_anonymous">StreamType.message_based_anonymous</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#StreamType.message_based_anonymous"></a>
    
    

                            </div>
                            <div id="StreamType.message_based_names" class="classattr">
                                <div class="attr variable">
            <span class="name">message_based_names</span>        =
<span class="default_value">&lt;<a href="#StreamType.message_based_names">StreamType.message_based_names</a>: 2&gt;</span>

        
    </div>
    <a class="headerlink" href="#StreamType.message_based_names"></a>
    
    

                            </div>
                            <div id="StreamType.gate" class="classattr">
                                <div class="attr variable">
            <span class="name">gate</span>        =
<span class="default_value">&lt;<a href="#StreamType.gate">StreamType.gate</a>: 3&gt;</span>

        
    </div>
    <a class="headerlink" href="#StreamType.gate"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="StreamType.name" class="variable">name</dd>
                <dd id="StreamType.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="GateSecurityPolicy">
                            <input id="GateSecurityPolicy-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">GateSecurityPolicy</span><wbr>(<span class="base">enum.Enum</span>):

                <label class="view-source-button" for="GateSecurityPolicy-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#GateSecurityPolicy"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="GateSecurityPolicy-56"><a href="#GateSecurityPolicy-56"><span class="linenos">56</span></a><span class="k">class</span> <span class="nc">GateSecurityPolicy</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
</span><span id="GateSecurityPolicy-57"><a href="#GateSecurityPolicy-57"><span class="linenos">57</span></a>    <span class="c1"># gate will allow only or ban selected stream names to conect to this gate</span>
</span><span id="GateSecurityPolicy-58"><a href="#GateSecurityPolicy-58"><span class="linenos">58</span></a>    <span class="n">allowed</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="GateSecurityPolicy-59"><a href="#GateSecurityPolicy-59"><span class="linenos">59</span></a>    <span class="n">disabled</span> <span class="o">=</span> <span class="mi">1</span>
</span></pre></div>


            <div class="docstring"><p>An enumeration.</p>
</div>


                            <div id="GateSecurityPolicy.allowed" class="classattr">
                                <div class="attr variable">
            <span class="name">allowed</span>        =
<span class="default_value">&lt;<a href="#GateSecurityPolicy.allowed">GateSecurityPolicy.allowed</a>: 0&gt;</span>

        
    </div>
    <a class="headerlink" href="#GateSecurityPolicy.allowed"></a>
    
    

                            </div>
                            <div id="GateSecurityPolicy.disabled" class="classattr">
                                <div class="attr variable">
            <span class="name">disabled</span>        =
<span class="default_value">&lt;<a href="#GateSecurityPolicy.disabled">GateSecurityPolicy.disabled</a>: 1&gt;</span>

        
    </div>
    <a class="headerlink" href="#GateSecurityPolicy.disabled"></a>
    
    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>enum.Enum</dt>
                                <dd id="GateSecurityPolicy.name" class="variable">name</dd>
                <dd id="GateSecurityPolicy.value" class="variable">value</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="StreamManagerIOCoreMemoryManagement">
                            <input id="StreamManagerIOCoreMemoryManagement-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">StreamManagerIOCoreMemoryManagement</span><wbr>(<span class="base">cengal.io.core.memory_management.versions.v_0.memory_management.IOCoreMemoryManagement</span>):

                <label class="view-source-button" for="StreamManagerIOCoreMemoryManagement-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#StreamManagerIOCoreMemoryManagement"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="StreamManagerIOCoreMemoryManagement-62"><a href="#StreamManagerIOCoreMemoryManagement-62"><span class="linenos">62</span></a><span class="k">class</span> <span class="nc">StreamManagerIOCoreMemoryManagement</span><span class="p">(</span><span class="n">IOCoreMemoryManagement</span><span class="p">):</span>
</span><span id="StreamManagerIOCoreMemoryManagement-63"><a href="#StreamManagerIOCoreMemoryManagement-63"><span class="linenos">63</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="StreamManagerIOCoreMemoryManagement-64"><a href="#StreamManagerIOCoreMemoryManagement-64"><span class="linenos">64</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="fm">__init__</span><span class="p">()</span>
</span><span id="StreamManagerIOCoreMemoryManagement-65"><a href="#StreamManagerIOCoreMemoryManagement-65"><span class="linenos">65</span></a>
</span><span id="StreamManagerIOCoreMemoryManagement-66"><a href="#StreamManagerIOCoreMemoryManagement-66"><span class="linenos">66</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span> <span class="o">=</span> <span class="n">ValueExistence</span><span class="p">(</span><span class="kc">True</span><span class="p">,</span>
</span><span id="StreamManagerIOCoreMemoryManagement-67"><a href="#StreamManagerIOCoreMemoryManagement-67"><span class="linenos">67</span></a>                                                             <span class="n">cpu_info</span><span class="p">()</span><span class="o">.</span><span class="n">l2_cache_size_per_virtual_core</span><span class="p">)</span>
</span><span id="StreamManagerIOCoreMemoryManagement-68"><a href="#StreamManagerIOCoreMemoryManagement-68"><span class="linenos">68</span></a>
</span><span id="StreamManagerIOCoreMemoryManagement-69"><a href="#StreamManagerIOCoreMemoryManagement-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="StreamManagerIOCoreMemoryManagement-70"><a href="#StreamManagerIOCoreMemoryManagement-70"><span class="linenos">70</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">link_to</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="StreamManagerIOCoreMemoryManagement-71"><a href="#StreamManagerIOCoreMemoryManagement-71"><span class="linenos">71</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="StreamManagerIOCoreMemoryManagement-72"><a href="#StreamManagerIOCoreMemoryManagement-72"><span class="linenos">72</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="StreamManagerIOCoreMemoryManagement-73"><a href="#StreamManagerIOCoreMemoryManagement-73"><span class="linenos">73</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="StreamManagerIOCoreMemoryManagement-74"><a href="#StreamManagerIOCoreMemoryManagement-74"><span class="linenos">74</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            <div id="StreamManagerIOCoreMemoryManagement.socket_write_fixed_buffer_size" class="classattr">
                                <div class="attr variable">
            <span class="name">socket_write_fixed_buffer_size</span>

        
    </div>
    <a class="headerlink" href="#StreamManagerIOCoreMemoryManagement.socket_write_fixed_buffer_size"></a>
    
    

                            </div>
                            <div id="StreamManagerIOCoreMemoryManagement.link_to" class="classattr">
                                        <input id="StreamManagerIOCoreMemoryManagement.link_to-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">link_to</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">parent</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="StreamManagerIOCoreMemoryManagement.link_to-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#StreamManagerIOCoreMemoryManagement.link_to"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="StreamManagerIOCoreMemoryManagement.link_to-69"><a href="#StreamManagerIOCoreMemoryManagement.link_to-69"><span class="linenos">69</span></a>    <span class="k">def</span> <span class="nf">link_to</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">parent</span><span class="p">):</span>
</span><span id="StreamManagerIOCoreMemoryManagement.link_to-70"><a href="#StreamManagerIOCoreMemoryManagement.link_to-70"><span class="linenos">70</span></a>        <span class="nb">super</span><span class="p">(</span><span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">link_to</span><span class="p">(</span><span class="n">parent</span><span class="p">)</span>
</span><span id="StreamManagerIOCoreMemoryManagement.link_to-71"><a href="#StreamManagerIOCoreMemoryManagement.link_to-71"><span class="linenos">71</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="StreamManagerIOCoreMemoryManagement.link_to-72"><a href="#StreamManagerIOCoreMemoryManagement.link_to-72"><span class="linenos">72</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span> <span class="o">=</span> <span class="n">parent</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="StreamManagerIOCoreMemoryManagement.link_to-73"><a href="#StreamManagerIOCoreMemoryManagement.link_to-73"><span class="linenos">73</span></a>        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="StreamManagerIOCoreMemoryManagement.link_to-74"><a href="#StreamManagerIOCoreMemoryManagement.link_to-74"><span class="linenos">74</span></a>            <span class="k">pass</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>cengal.io.core.memory_management.versions.v_0.memory_management.IOCoreMemoryManagement</dt>
                                <dd id="StreamManagerIOCoreMemoryManagement.global__data_size_limit" class="variable">global__data_size_limit</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global__data_full_size" class="variable">global__data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global__deletable_data_full_size" class="variable">global__deletable_data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_other__data_size_limit" class="variable">global_other__data_size_limit</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_other__data_full_size" class="variable">global_other__data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_other__deletable_data_full_size" class="variable">global_other__deletable_data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_in__data_size_limit" class="variable">global_in__data_size_limit</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_in__data_full_size" class="variable">global_in__data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_in__deletable_data_full_size" class="variable">global_in__deletable_data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_out__data_size_limit" class="variable">global_out__data_size_limit</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_out__data_full_size" class="variable">global_out__data_full_size</dd>
                <dd id="StreamManagerIOCoreMemoryManagement.global_out__deletable_data_full_size" class="variable">global_out__deletable_data_full_size</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TcpStreamManager">
                            <input id="TcpStreamManager-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TcpStreamManager</span><wbr>(<span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamManagerAbstract</span>):

                <label class="view-source-button" for="TcpStreamManager-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager-83"><a href="#TcpStreamManager-83"><span class="linenos"> 83</span></a><span class="k">class</span> <span class="nc">TcpStreamManager</span><span class="p">(</span><span class="n">StreamManagerAbstract</span><span class="p">):</span>
</span><span id="TcpStreamManager-84"><a href="#TcpStreamManager-84"><span class="linenos"> 84</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamManager-85"><a href="#TcpStreamManager-85"><span class="linenos"> 85</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">io_memory_management</span><span class="p">:</span> <span class="n">StreamManagerIOCoreMemoryManagement</span> <span class="o">=</span> <span class="n">StreamManagerIOCoreMemoryManagement</span><span class="p">()</span>
</span><span id="TcpStreamManager-86"><a href="#TcpStreamManager-86"><span class="linenos"> 86</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mf">10.0</span>
</span><span id="TcpStreamManager-87"><a href="#TcpStreamManager-87"><span class="linenos"> 87</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">output_to_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="TcpStreamManager-88"><a href="#TcpStreamManager-88"><span class="linenos"> 88</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">input_from_client_container_type</span> <span class="o">=</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span>
</span><span id="TcpStreamManager-89"><a href="#TcpStreamManager-89"><span class="linenos"> 89</span></a>
</span><span id="TcpStreamManager-90"><a href="#TcpStreamManager-90"><span class="linenos"> 90</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="TcpStreamManager-91"><a href="#TcpStreamManager-91"><span class="linenos"> 91</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager-92"><a href="#TcpStreamManager-92"><span class="linenos"> 92</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager-93"><a href="#TcpStreamManager-93"><span class="linenos"> 93</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-94"><a href="#TcpStreamManager-94"><span class="linenos"> 94</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-95"><a href="#TcpStreamManager-95"><span class="linenos"> 95</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager-96"><a href="#TcpStreamManager-96"><span class="linenos"> 96</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="TcpStreamManager-97"><a href="#TcpStreamManager-97"><span class="linenos"> 97</span></a>
</span><span id="TcpStreamManager-98"><a href="#TcpStreamManager-98"><span class="linenos"> 98</span></a><span class="sd">        The reader returned is a TcpStreamReader instance; the writer is a</span>
</span><span id="TcpStreamManager-99"><a href="#TcpStreamManager-99"><span class="linenos"> 99</span></a><span class="sd">        TcpStreamWriter instance.</span>
</span><span id="TcpStreamManager-100"><a href="#TcpStreamManager-100"><span class="linenos">100</span></a>
</span><span id="TcpStreamManager-101"><a href="#TcpStreamManager-101"><span class="linenos">101</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="TcpStreamManager-102"><a href="#TcpStreamManager-102"><span class="linenos">102</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="TcpStreamManager-103"><a href="#TcpStreamManager-103"><span class="linenos">103</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="TcpStreamManager-104"><a href="#TcpStreamManager-104"><span class="linenos">104</span></a>
</span><span id="TcpStreamManager-105"><a href="#TcpStreamManager-105"><span class="linenos">105</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="TcpStreamManager-106"><a href="#TcpStreamManager-106"><span class="linenos">106</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="TcpStreamManager-107"><a href="#TcpStreamManager-107"><span class="linenos">107</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="TcpStreamManager-108"><a href="#TcpStreamManager-108"><span class="linenos">108</span></a>
</span><span id="TcpStreamManager-109"><a href="#TcpStreamManager-109"><span class="linenos">109</span></a><span class="sd">        (If you want to customize the TcpStreamReader and/or</span>
</span><span id="TcpStreamManager-110"><a href="#TcpStreamManager-110"><span class="linenos">110</span></a><span class="sd">        TcpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="TcpStreamManager-111"><a href="#TcpStreamManager-111"><span class="linenos">111</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="TcpStreamManager-112"><a href="#TcpStreamManager-112"><span class="linenos">112</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamManager-113"><a href="#TcpStreamManager-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="TcpStreamManager-114"><a href="#TcpStreamManager-114"><span class="linenos">114</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-115"><a href="#TcpStreamManager-115"><span class="linenos">115</span></a>        
</span><span id="TcpStreamManager-116"><a href="#TcpStreamManager-116"><span class="linenos">116</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamManager-117"><a href="#TcpStreamManager-117"><span class="linenos">117</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="TcpStreamManager-118"><a href="#TcpStreamManager-118"><span class="linenos">118</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-119"><a href="#TcpStreamManager-119"><span class="linenos">119</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="TcpStreamManager-120"><a href="#TcpStreamManager-120"><span class="linenos">120</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="TcpStreamManager-121"><a href="#TcpStreamManager-121"><span class="linenos">121</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TcpStreamManager-122"><a href="#TcpStreamManager-122"><span class="linenos">122</span></a>        
</span><span id="TcpStreamManager-123"><a href="#TcpStreamManager-123"><span class="linenos">123</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager-124"><a href="#TcpStreamManager-124"><span class="linenos">124</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-125"><a href="#TcpStreamManager-125"><span class="linenos">125</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-126"><a href="#TcpStreamManager-126"><span class="linenos">126</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="TcpStreamManager-127"><a href="#TcpStreamManager-127"><span class="linenos">127</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="TcpStreamManager-128"><a href="#TcpStreamManager-128"><span class="linenos">128</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-129"><a href="#TcpStreamManager-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="TcpStreamManager-130"><a href="#TcpStreamManager-130"><span class="linenos">130</span></a>    
</span><span id="TcpStreamManager-131"><a href="#TcpStreamManager-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">bind_existing_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager-132"><a href="#TcpStreamManager-132"><span class="linenos">132</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager-133"><a href="#TcpStreamManager-133"><span class="linenos">133</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-134"><a href="#TcpStreamManager-134"><span class="linenos">134</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-135"><a href="#TcpStreamManager-135"><span class="linenos">135</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager-136"><a href="#TcpStreamManager-136"><span class="linenos">136</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="TcpStreamManager-137"><a href="#TcpStreamManager-137"><span class="linenos">137</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager-138"><a href="#TcpStreamManager-138"><span class="linenos">138</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-139"><a href="#TcpStreamManager-139"><span class="linenos">139</span></a>        
</span><span id="TcpStreamManager-140"><a href="#TcpStreamManager-140"><span class="linenos">140</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-141"><a href="#TcpStreamManager-141"><span class="linenos">141</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-142"><a href="#TcpStreamManager-142"><span class="linenos">142</span></a>        
</span><span id="TcpStreamManager-143"><a href="#TcpStreamManager-143"><span class="linenos">143</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="TcpStreamManager-144"><a href="#TcpStreamManager-144"><span class="linenos">144</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-145"><a href="#TcpStreamManager-145"><span class="linenos">145</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-146"><a href="#TcpStreamManager-146"><span class="linenos">146</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="TcpStreamManager-147"><a href="#TcpStreamManager-147"><span class="linenos">147</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-148"><a href="#TcpStreamManager-148"><span class="linenos">148</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-149"><a href="#TcpStreamManager-149"><span class="linenos">149</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-150"><a href="#TcpStreamManager-150"><span class="linenos">150</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-151"><a href="#TcpStreamManager-151"><span class="linenos">151</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-152"><a href="#TcpStreamManager-152"><span class="linenos">152</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-153"><a href="#TcpStreamManager-153"><span class="linenos">153</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-154"><a href="#TcpStreamManager-154"><span class="linenos">154</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-155"><a href="#TcpStreamManager-155"><span class="linenos">155</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-156"><a href="#TcpStreamManager-156"><span class="linenos">156</span></a>
</span><span id="TcpStreamManager-157"><a href="#TcpStreamManager-157"><span class="linenos">157</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="TcpStreamManager-158"><a href="#TcpStreamManager-158"><span class="linenos">158</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-159"><a href="#TcpStreamManager-159"><span class="linenos">159</span></a>
</span><span id="TcpStreamManager-160"><a href="#TcpStreamManager-160"><span class="linenos">160</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="TcpStreamManager-161"><a href="#TcpStreamManager-161"><span class="linenos">161</span></a>
</span><span id="TcpStreamManager-162"><a href="#TcpStreamManager-162"><span class="linenos">162</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="TcpStreamManager-163"><a href="#TcpStreamManager-163"><span class="linenos">163</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager-164"><a href="#TcpStreamManager-164"><span class="linenos">164</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager-165"><a href="#TcpStreamManager-165"><span class="linenos">165</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-166"><a href="#TcpStreamManager-166"><span class="linenos">166</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-167"><a href="#TcpStreamManager-167"><span class="linenos">167</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-168"><a href="#TcpStreamManager-168"><span class="linenos">168</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="TcpStreamManager-169"><a href="#TcpStreamManager-169"><span class="linenos">169</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="TcpStreamManager-170"><a href="#TcpStreamManager-170"><span class="linenos">170</span></a>
</span><span id="TcpStreamManager-171"><a href="#TcpStreamManager-171"><span class="linenos">171</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="TcpStreamManager-172"><a href="#TcpStreamManager-172"><span class="linenos">172</span></a><span class="sd">        client_reader, client_writer.  client_reader is a TcpStreamReader</span>
</span><span id="TcpStreamManager-173"><a href="#TcpStreamManager-173"><span class="linenos">173</span></a><span class="sd">        object, while client_writer is a TcpStreamWriter object.  This</span>
</span><span id="TcpStreamManager-174"><a href="#TcpStreamManager-174"><span class="linenos">174</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="TcpStreamManager-175"><a href="#TcpStreamManager-175"><span class="linenos">175</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="TcpStreamManager-176"><a href="#TcpStreamManager-176"><span class="linenos">176</span></a><span class="sd">        Task.</span>
</span><span id="TcpStreamManager-177"><a href="#TcpStreamManager-177"><span class="linenos">177</span></a>
</span><span id="TcpStreamManager-178"><a href="#TcpStreamManager-178"><span class="linenos">178</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="TcpStreamManager-179"><a href="#TcpStreamManager-179"><span class="linenos">179</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="TcpStreamManager-180"><a href="#TcpStreamManager-180"><span class="linenos">180</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="TcpStreamManager-181"><a href="#TcpStreamManager-181"><span class="linenos">181</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="TcpStreamManager-182"><a href="#TcpStreamManager-182"><span class="linenos">182</span></a>
</span><span id="TcpStreamManager-183"><a href="#TcpStreamManager-183"><span class="linenos">183</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="TcpStreamManager-184"><a href="#TcpStreamManager-184"><span class="linenos">184</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="TcpStreamManager-185"><a href="#TcpStreamManager-185"><span class="linenos">185</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="TcpStreamManager-186"><a href="#TcpStreamManager-186"><span class="linenos">186</span></a>
</span><span id="TcpStreamManager-187"><a href="#TcpStreamManager-187"><span class="linenos">187</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="TcpStreamManager-188"><a href="#TcpStreamManager-188"><span class="linenos">188</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="TcpStreamManager-189"><a href="#TcpStreamManager-189"><span class="linenos">189</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamManager-190"><a href="#TcpStreamManager-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamManager-191"><a href="#TcpStreamManager-191"><span class="linenos">191</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="TcpStreamManager-192"><a href="#TcpStreamManager-192"><span class="linenos">192</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-193"><a href="#TcpStreamManager-193"><span class="linenos">193</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="TcpStreamManager-194"><a href="#TcpStreamManager-194"><span class="linenos">194</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="TcpStreamManager-195"><a href="#TcpStreamManager-195"><span class="linenos">195</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TcpStreamManager-196"><a href="#TcpStreamManager-196"><span class="linenos">196</span></a>
</span><span id="TcpStreamManager-197"><a href="#TcpStreamManager-197"><span class="linenos">197</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="TcpStreamManager-198"><a href="#TcpStreamManager-198"><span class="linenos">198</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager-199"><a href="#TcpStreamManager-199"><span class="linenos">199</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-200"><a href="#TcpStreamManager-200"><span class="linenos">200</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="TcpStreamManager-201"><a href="#TcpStreamManager-201"><span class="linenos">201</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-202"><a href="#TcpStreamManager-202"><span class="linenos">202</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="TcpStreamManager-203"><a href="#TcpStreamManager-203"><span class="linenos">203</span></a>
</span><span id="TcpStreamManager-204"><a href="#TcpStreamManager-204"><span class="linenos">204</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="TcpStreamManager-205"><a href="#TcpStreamManager-205"><span class="linenos">205</span></a>
</span><span id="TcpStreamManager-206"><a href="#TcpStreamManager-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="nf">bind_accepted_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> 
</span><span id="TcpStreamManager-207"><a href="#TcpStreamManager-207"><span class="linenos">207</span></a>                            <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager-208"><a href="#TcpStreamManager-208"><span class="linenos">208</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager-209"><a href="#TcpStreamManager-209"><span class="linenos">209</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-210"><a href="#TcpStreamManager-210"><span class="linenos">210</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager-211"><a href="#TcpStreamManager-211"><span class="linenos">211</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager-212"><a href="#TcpStreamManager-212"><span class="linenos">212</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="TcpStreamManager-213"><a href="#TcpStreamManager-213"><span class="linenos">213</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager-214"><a href="#TcpStreamManager-214"><span class="linenos">214</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-215"><a href="#TcpStreamManager-215"><span class="linenos">215</span></a>        
</span><span id="TcpStreamManager-216"><a href="#TcpStreamManager-216"><span class="linenos">216</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-217"><a href="#TcpStreamManager-217"><span class="linenos">217</span></a>        <span class="n">client_connected_cb</span> <span class="o">=</span> <span class="n">protocol</span><span class="o">.</span><span class="n">_client_connected_cb</span>
</span><span id="TcpStreamManager-218"><a href="#TcpStreamManager-218"><span class="linenos">218</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-219"><a href="#TcpStreamManager-219"><span class="linenos">219</span></a>        
</span><span id="TcpStreamManager-220"><a href="#TcpStreamManager-220"><span class="linenos">220</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="TcpStreamManager-221"><a href="#TcpStreamManager-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-222"><a href="#TcpStreamManager-222"><span class="linenos">222</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-223"><a href="#TcpStreamManager-223"><span class="linenos">223</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="TcpStreamManager-224"><a href="#TcpStreamManager-224"><span class="linenos">224</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-225"><a href="#TcpStreamManager-225"><span class="linenos">225</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-226"><a href="#TcpStreamManager-226"><span class="linenos">226</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-227"><a href="#TcpStreamManager-227"><span class="linenos">227</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-228"><a href="#TcpStreamManager-228"><span class="linenos">228</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager-229"><a href="#TcpStreamManager-229"><span class="linenos">229</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager-230"><a href="#TcpStreamManager-230"><span class="linenos">230</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager-231"><a href="#TcpStreamManager-231"><span class="linenos">231</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-232"><a href="#TcpStreamManager-232"><span class="linenos">232</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-233"><a href="#TcpStreamManager-233"><span class="linenos">233</span></a>
</span><span id="TcpStreamManager-234"><a href="#TcpStreamManager-234"><span class="linenos">234</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="TcpStreamManager-235"><a href="#TcpStreamManager-235"><span class="linenos">235</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager-236"><a href="#TcpStreamManager-236"><span class="linenos">236</span></a>
</span><span id="TcpStreamManager-237"><a href="#TcpStreamManager-237"><span class="linenos">237</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span><span id="TcpStreamManager-238"><a href="#TcpStreamManager-238"><span class="linenos">238</span></a>
</span><span id="TcpStreamManager-239"><a href="#TcpStreamManager-239"><span class="linenos">239</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamManager-240"><a href="#TcpStreamManager-240"><span class="linenos">240</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager-241"><a href="#TcpStreamManager-241"><span class="linenos">241</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-242"><a href="#TcpStreamManager-242"><span class="linenos">242</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamManager-243"><a href="#TcpStreamManager-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamManager-244"><a href="#TcpStreamManager-244"><span class="linenos">244</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="TcpStreamManager-245"><a href="#TcpStreamManager-245"><span class="linenos">245</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-246"><a href="#TcpStreamManager-246"><span class="linenos">246</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="TcpStreamManager-247"><a href="#TcpStreamManager-247"><span class="linenos">247</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="TcpStreamManager-248"><a href="#TcpStreamManager-248"><span class="linenos">248</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamManager-249"><a href="#TcpStreamManager-249"><span class="linenos">249</span></a>        
</span><span id="TcpStreamManager-250"><a href="#TcpStreamManager-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="TcpStreamManager-251"><a href="#TcpStreamManager-251"><span class="linenos">251</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager-252"><a href="#TcpStreamManager-252"><span class="linenos">252</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager-253"><a href="#TcpStreamManager-253"><span class="linenos">253</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager-254"><a href="#TcpStreamManager-254"><span class="linenos">254</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="TcpStreamManager-255"><a href="#TcpStreamManager-255"><span class="linenos">255</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="TcpStreamManager-256"><a href="#TcpStreamManager-256"><span class="linenos">256</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="TcpStreamManager-257"><a href="#TcpStreamManager-257"><span class="linenos">257</span></a>            <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="TcpStreamManager-258"><a href="#TcpStreamManager-258"><span class="linenos">258</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="TcpStreamManager-259"><a href="#TcpStreamManager-259"><span class="linenos">259</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-260"><a href="#TcpStreamManager-260"><span class="linenos">260</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TcpStreamManager-261"><a href="#TcpStreamManager-261"><span class="linenos">261</span></a>    
</span><span id="TcpStreamManager-262"><a href="#TcpStreamManager-262"><span class="linenos">262</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamManager-263"><a href="#TcpStreamManager-263"><span class="linenos">263</span></a>        <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="TcpStreamManager-264"><a href="#TcpStreamManager-264"><span class="linenos">264</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="TcpStreamManager-265"><a href="#TcpStreamManager-265"><span class="linenos">265</span></a>        <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="TcpStreamManager-266"><a href="#TcpStreamManager-266"><span class="linenos">266</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager-267"><a href="#TcpStreamManager-267"><span class="linenos">267</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-268"><a href="#TcpStreamManager-268"><span class="linenos">268</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamManager-269"><a href="#TcpStreamManager-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamManager-270"><a href="#TcpStreamManager-270"><span class="linenos">270</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="TcpStreamManager-271"><a href="#TcpStreamManager-271"><span class="linenos">271</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager-272"><a href="#TcpStreamManager-272"><span class="linenos">272</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="TcpStreamManager-273"><a href="#TcpStreamManager-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="TcpStreamManager-274"><a href="#TcpStreamManager-274"><span class="linenos">274</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamManager-275"><a href="#TcpStreamManager-275"><span class="linenos">275</span></a>        
</span><span id="TcpStreamManager-276"><a href="#TcpStreamManager-276"><span class="linenos">276</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="TcpStreamManager-277"><a href="#TcpStreamManager-277"><span class="linenos">277</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager-278"><a href="#TcpStreamManager-278"><span class="linenos">278</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager-279"><a href="#TcpStreamManager-279"><span class="linenos">279</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager-280"><a href="#TcpStreamManager-280"><span class="linenos">280</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="TcpStreamManager-281"><a href="#TcpStreamManager-281"><span class="linenos">281</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="TcpStreamManager-282"><a href="#TcpStreamManager-282"><span class="linenos">282</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager-283"><a href="#TcpStreamManager-283"><span class="linenos">283</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            <div id="TcpStreamManager.io_memory_management" class="classattr">
                                <div class="attr variable">
            <span class="name">io_memory_management</span><span class="annotation">: <a href="#StreamManagerIOCoreMemoryManagement">StreamManagerIOCoreMemoryManagement</a></span>

        
    </div>
    <a class="headerlink" href="#TcpStreamManager.io_memory_management"></a>
    
    

                            </div>
                            <div id="TcpStreamManager.autonomous_writer_stop_default_timeout" class="classattr">
                                <div class="attr variable">
            <span class="name">autonomous_writer_stop_default_timeout</span><span class="annotation">: Union[int, float, NoneType]</span>

        
    </div>
    <a class="headerlink" href="#TcpStreamManager.autonomous_writer_stop_default_timeout"></a>
    
    

                            </div>
                            <div id="TcpStreamManager.output_to_client_container_type" class="classattr">
                                <div class="attr variable">
            <span class="name">output_to_client_container_type</span>

        
    </div>
    <a class="headerlink" href="#TcpStreamManager.output_to_client_container_type"></a>
    
    

                            </div>
                            <div id="TcpStreamManager.input_from_client_container_type" class="classattr">
                                <div class="attr variable">
            <span class="name">input_from_client_container_type</span>

        
    </div>
    <a class="headerlink" href="#TcpStreamManager.input_from_client_container_type"></a>
    
    

                            </div>
                            <div id="TcpStreamManager.open_connection" class="classattr">
                                        <input id="TcpStreamManager.open_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">open_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">host</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">port</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">) -> <span class="nb">tuple</span><span class="p">[</span><span class="n"><a href="#TcpStreamReader">TcpStreamReader</a></span><span class="p">,</span> <span class="n"><a href="#TcpStreamWriter">TcpStreamWriter</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TcpStreamManager.open_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.open_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.open_connection-90"><a href="#TcpStreamManager.open_connection-90"><span class="linenos"> 90</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">open_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="TcpStreamManager.open_connection-91"><a href="#TcpStreamManager.open_connection-91"><span class="linenos"> 91</span></a>                            <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager.open_connection-92"><a href="#TcpStreamManager.open_connection-92"><span class="linenos"> 92</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager.open_connection-93"><a href="#TcpStreamManager.open_connection-93"><span class="linenos"> 93</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.open_connection-94"><a href="#TcpStreamManager.open_connection-94"><span class="linenos"> 94</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.open_connection-95"><a href="#TcpStreamManager.open_connection-95"><span class="linenos"> 95</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager.open_connection-96"><a href="#TcpStreamManager.open_connection-96"><span class="linenos"> 96</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;A wrapper for create_connection() returning a (reader, writer) pair.</span>
</span><span id="TcpStreamManager.open_connection-97"><a href="#TcpStreamManager.open_connection-97"><span class="linenos"> 97</span></a>
</span><span id="TcpStreamManager.open_connection-98"><a href="#TcpStreamManager.open_connection-98"><span class="linenos"> 98</span></a><span class="sd">        The reader returned is a TcpStreamReader instance; the writer is a</span>
</span><span id="TcpStreamManager.open_connection-99"><a href="#TcpStreamManager.open_connection-99"><span class="linenos"> 99</span></a><span class="sd">        TcpStreamWriter instance.</span>
</span><span id="TcpStreamManager.open_connection-100"><a href="#TcpStreamManager.open_connection-100"><span class="linenos">100</span></a>
</span><span id="TcpStreamManager.open_connection-101"><a href="#TcpStreamManager.open_connection-101"><span class="linenos">101</span></a><span class="sd">        The arguments are all the usual arguments to create_connection()</span>
</span><span id="TcpStreamManager.open_connection-102"><a href="#TcpStreamManager.open_connection-102"><span class="linenos">102</span></a><span class="sd">        except protocol_factory; most common are positional host and port,</span>
</span><span id="TcpStreamManager.open_connection-103"><a href="#TcpStreamManager.open_connection-103"><span class="linenos">103</span></a><span class="sd">        with various optional keyword arguments following.</span>
</span><span id="TcpStreamManager.open_connection-104"><a href="#TcpStreamManager.open_connection-104"><span class="linenos">104</span></a>
</span><span id="TcpStreamManager.open_connection-105"><a href="#TcpStreamManager.open_connection-105"><span class="linenos">105</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="TcpStreamManager.open_connection-106"><a href="#TcpStreamManager.open_connection-106"><span class="linenos">106</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="TcpStreamManager.open_connection-107"><a href="#TcpStreamManager.open_connection-107"><span class="linenos">107</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="TcpStreamManager.open_connection-108"><a href="#TcpStreamManager.open_connection-108"><span class="linenos">108</span></a>
</span><span id="TcpStreamManager.open_connection-109"><a href="#TcpStreamManager.open_connection-109"><span class="linenos">109</span></a><span class="sd">        (If you want to customize the TcpStreamReader and/or</span>
</span><span id="TcpStreamManager.open_connection-110"><a href="#TcpStreamManager.open_connection-110"><span class="linenos">110</span></a><span class="sd">        TcpStreamReaderProtocol classes, just copy the code -- there&#39;s</span>
</span><span id="TcpStreamManager.open_connection-111"><a href="#TcpStreamManager.open_connection-111"><span class="linenos">111</span></a><span class="sd">        really nothing special here except some convenience.)</span>
</span><span id="TcpStreamManager.open_connection-112"><a href="#TcpStreamManager.open_connection-112"><span class="linenos">112</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamManager.open_connection-113"><a href="#TcpStreamManager.open_connection-113"><span class="linenos">113</span></a>        <span class="k">if</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">gate</span> <span class="o">==</span> <span class="n">stream_type</span><span class="p">:</span>
</span><span id="TcpStreamManager.open_connection-114"><a href="#TcpStreamManager.open_connection-114"><span class="linenos">114</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Wrong stream_type value: client can not be a &quot;gate&quot;.&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-115"><a href="#TcpStreamManager.open_connection-115"><span class="linenos">115</span></a>        
</span><span id="TcpStreamManager.open_connection-116"><a href="#TcpStreamManager.open_connection-116"><span class="linenos">116</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamManager.open_connection-117"><a href="#TcpStreamManager.open_connection-117"><span class="linenos">117</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="TcpStreamManager.open_connection-118"><a href="#TcpStreamManager.open_connection-118"><span class="linenos">118</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.open_connection-119"><a href="#TcpStreamManager.open_connection-119"><span class="linenos">119</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="TcpStreamManager.open_connection-120"><a href="#TcpStreamManager.open_connection-120"><span class="linenos">120</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="TcpStreamManager.open_connection-121"><a href="#TcpStreamManager.open_connection-121"><span class="linenos">121</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-122"><a href="#TcpStreamManager.open_connection-122"><span class="linenos">122</span></a>        
</span><span id="TcpStreamManager.open_connection-123"><a href="#TcpStreamManager.open_connection-123"><span class="linenos">123</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-124"><a href="#TcpStreamManager.open_connection-124"><span class="linenos">124</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-125"><a href="#TcpStreamManager.open_connection-125"><span class="linenos">125</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-126"><a href="#TcpStreamManager.open_connection-126"><span class="linenos">126</span></a>        <span class="n">transport</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_connection</span><span class="p">(</span>
</span><span id="TcpStreamManager.open_connection-127"><a href="#TcpStreamManager.open_connection-127"><span class="linenos">127</span></a>            <span class="k">lambda</span><span class="p">:</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-128"><a href="#TcpStreamManager.open_connection-128"><span class="linenos">128</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.open_connection-129"><a href="#TcpStreamManager.open_connection-129"><span class="linenos">129</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span></pre></div>


            <div class="docstring"><p>A wrapper for create_connection() returning a (reader, writer) pair.</p>

<p>The reader returned is a TcpStreamReader instance; the writer is a
TcpStreamWriter instance.</p>

<p>The arguments are all the usual arguments to create_connection()
except protocol_factory; most common are positional host and port,
with various optional keyword arguments following.</p>

<p>Additional optional keyword arguments are loop (to set the event loop
instance to use) and limit (to set the buffer limit passed to the
TcpStreamReader).</p>

<p>(If you want to customize the TcpStreamReader and/or
TcpStreamReaderProtocol classes, just copy the code -- there's
really nothing special here except some convenience.)</p>
</div>


                            </div>
                            <div id="TcpStreamManager.bind_existing_connection" class="classattr">
                                        <input id="TcpStreamManager.bind_existing_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bind_existing_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">streams</span><span class="o">.</span><span class="n">StreamReader</span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">streams</span><span class="o">.</span><span class="n">StreamWriter</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">) -> <span class="nb">tuple</span><span class="p">[</span><span class="n"><a href="#TcpStreamReader">TcpStreamReader</a></span><span class="p">,</span> <span class="n"><a href="#TcpStreamWriter">TcpStreamWriter</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TcpStreamManager.bind_existing_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.bind_existing_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.bind_existing_connection-131"><a href="#TcpStreamManager.bind_existing_connection-131"><span class="linenos">131</span></a>    <span class="k">def</span> <span class="nf">bind_existing_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_existing_connection-132"><a href="#TcpStreamManager.bind_existing_connection-132"><span class="linenos">132</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager.bind_existing_connection-133"><a href="#TcpStreamManager.bind_existing_connection-133"><span class="linenos">133</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_existing_connection-134"><a href="#TcpStreamManager.bind_existing_connection-134"><span class="linenos">134</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_existing_connection-135"><a href="#TcpStreamManager.bind_existing_connection-135"><span class="linenos">135</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager.bind_existing_connection-136"><a href="#TcpStreamManager.bind_existing_connection-136"><span class="linenos">136</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-137"><a href="#TcpStreamManager.bind_existing_connection-137"><span class="linenos">137</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-138"><a href="#TcpStreamManager.bind_existing_connection-138"><span class="linenos">138</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-139"><a href="#TcpStreamManager.bind_existing_connection-139"><span class="linenos">139</span></a>        
</span><span id="TcpStreamManager.bind_existing_connection-140"><a href="#TcpStreamManager.bind_existing_connection-140"><span class="linenos">140</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-141"><a href="#TcpStreamManager.bind_existing_connection-141"><span class="linenos">141</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-142"><a href="#TcpStreamManager.bind_existing_connection-142"><span class="linenos">142</span></a>        
</span><span id="TcpStreamManager.bind_existing_connection-143"><a href="#TcpStreamManager.bind_existing_connection-143"><span class="linenos">143</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="TcpStreamManager.bind_existing_connection-144"><a href="#TcpStreamManager.bind_existing_connection-144"><span class="linenos">144</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_existing_connection-145"><a href="#TcpStreamManager.bind_existing_connection-145"><span class="linenos">145</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-146"><a href="#TcpStreamManager.bind_existing_connection-146"><span class="linenos">146</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="TcpStreamManager.bind_existing_connection-147"><a href="#TcpStreamManager.bind_existing_connection-147"><span class="linenos">147</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-148"><a href="#TcpStreamManager.bind_existing_connection-148"><span class="linenos">148</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_existing_connection-149"><a href="#TcpStreamManager.bind_existing_connection-149"><span class="linenos">149</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-150"><a href="#TcpStreamManager.bind_existing_connection-150"><span class="linenos">150</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-151"><a href="#TcpStreamManager.bind_existing_connection-151"><span class="linenos">151</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_existing_connection-152"><a href="#TcpStreamManager.bind_existing_connection-152"><span class="linenos">152</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-153"><a href="#TcpStreamManager.bind_existing_connection-153"><span class="linenos">153</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-154"><a href="#TcpStreamManager.bind_existing_connection-154"><span class="linenos">154</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.bind_existing_connection-155"><a href="#TcpStreamManager.bind_existing_connection-155"><span class="linenos">155</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-156"><a href="#TcpStreamManager.bind_existing_connection-156"><span class="linenos">156</span></a>
</span><span id="TcpStreamManager.bind_existing_connection-157"><a href="#TcpStreamManager.bind_existing_connection-157"><span class="linenos">157</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-158"><a href="#TcpStreamManager.bind_existing_connection-158"><span class="linenos">158</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_existing_connection-159"><a href="#TcpStreamManager.bind_existing_connection-159"><span class="linenos">159</span></a>
</span><span id="TcpStreamManager.bind_existing_connection-160"><a href="#TcpStreamManager.bind_existing_connection-160"><span class="linenos">160</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamManager.start_server" class="classattr">
                                        <input id="TcpStreamManager.start_server-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">start_server</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">client_connected_cb</span>,</span><span class="param">	<span class="n">host</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">port</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">gate_security_policy</span><span class="p">:</span> <span class="n"><a href="#GateSecurityPolicy">GateSecurityPolicy</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#GateSecurityPolicy.disabled">GateSecurityPolicy.disabled</a></span><span class="p">:</span> <span class="mi">1</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamManager.start_server-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.start_server"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.start_server-162"><a href="#TcpStreamManager.start_server-162"><span class="linenos">162</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">start_server</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">host</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-163"><a href="#TcpStreamManager.start_server-163"><span class="linenos">163</span></a>                        <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-164"><a href="#TcpStreamManager.start_server-164"><span class="linenos">164</span></a>                        <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager.start_server-165"><a href="#TcpStreamManager.start_server-165"><span class="linenos">165</span></a>                        <span class="n">gate_security_policy</span><span class="p">:</span> <span class="n">GateSecurityPolicy</span> <span class="o">=</span> <span class="n">GateSecurityPolicy</span><span class="o">.</span><span class="n">disabled</span><span class="p">,</span> <span class="n">policy_managed_stream_names</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Set</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-166"><a href="#TcpStreamManager.start_server-166"><span class="linenos">166</span></a>                        <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-167"><a href="#TcpStreamManager.start_server-167"><span class="linenos">167</span></a>                        <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-168"><a href="#TcpStreamManager.start_server-168"><span class="linenos">168</span></a>                        <span class="o">**</span><span class="n">kwds</span><span class="p">):</span>
</span><span id="TcpStreamManager.start_server-169"><a href="#TcpStreamManager.start_server-169"><span class="linenos">169</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Start a socket server, call back for each client connected.</span>
</span><span id="TcpStreamManager.start_server-170"><a href="#TcpStreamManager.start_server-170"><span class="linenos">170</span></a>
</span><span id="TcpStreamManager.start_server-171"><a href="#TcpStreamManager.start_server-171"><span class="linenos">171</span></a><span class="sd">        The first parameter, `client_connected_cb`, takes two parameters:</span>
</span><span id="TcpStreamManager.start_server-172"><a href="#TcpStreamManager.start_server-172"><span class="linenos">172</span></a><span class="sd">        client_reader, client_writer.  client_reader is a TcpStreamReader</span>
</span><span id="TcpStreamManager.start_server-173"><a href="#TcpStreamManager.start_server-173"><span class="linenos">173</span></a><span class="sd">        object, while client_writer is a TcpStreamWriter object.  This</span>
</span><span id="TcpStreamManager.start_server-174"><a href="#TcpStreamManager.start_server-174"><span class="linenos">174</span></a><span class="sd">        parameter can either be a plain callback function or a coroutine;</span>
</span><span id="TcpStreamManager.start_server-175"><a href="#TcpStreamManager.start_server-175"><span class="linenos">175</span></a><span class="sd">        if it is a coroutine, it will be automatically converted into a</span>
</span><span id="TcpStreamManager.start_server-176"><a href="#TcpStreamManager.start_server-176"><span class="linenos">176</span></a><span class="sd">        Task.</span>
</span><span id="TcpStreamManager.start_server-177"><a href="#TcpStreamManager.start_server-177"><span class="linenos">177</span></a>
</span><span id="TcpStreamManager.start_server-178"><a href="#TcpStreamManager.start_server-178"><span class="linenos">178</span></a><span class="sd">        The rest of the arguments are all the usual arguments to</span>
</span><span id="TcpStreamManager.start_server-179"><a href="#TcpStreamManager.start_server-179"><span class="linenos">179</span></a><span class="sd">        loop.create_server() except protocol_factory; most common are</span>
</span><span id="TcpStreamManager.start_server-180"><a href="#TcpStreamManager.start_server-180"><span class="linenos">180</span></a><span class="sd">        positional host and port, with various optional keyword arguments</span>
</span><span id="TcpStreamManager.start_server-181"><a href="#TcpStreamManager.start_server-181"><span class="linenos">181</span></a><span class="sd">        following.  The return value is the same as loop.create_server().</span>
</span><span id="TcpStreamManager.start_server-182"><a href="#TcpStreamManager.start_server-182"><span class="linenos">182</span></a>
</span><span id="TcpStreamManager.start_server-183"><a href="#TcpStreamManager.start_server-183"><span class="linenos">183</span></a><span class="sd">        Additional optional keyword arguments are loop (to set the event loop</span>
</span><span id="TcpStreamManager.start_server-184"><a href="#TcpStreamManager.start_server-184"><span class="linenos">184</span></a><span class="sd">        instance to use) and limit (to set the buffer limit passed to the</span>
</span><span id="TcpStreamManager.start_server-185"><a href="#TcpStreamManager.start_server-185"><span class="linenos">185</span></a><span class="sd">        TcpStreamReader).</span>
</span><span id="TcpStreamManager.start_server-186"><a href="#TcpStreamManager.start_server-186"><span class="linenos">186</span></a>
</span><span id="TcpStreamManager.start_server-187"><a href="#TcpStreamManager.start_server-187"><span class="linenos">187</span></a><span class="sd">        The return value is the same as loop.create_server(), i.e. a</span>
</span><span id="TcpStreamManager.start_server-188"><a href="#TcpStreamManager.start_server-188"><span class="linenos">188</span></a><span class="sd">        Server object which can be used to stop the service.</span>
</span><span id="TcpStreamManager.start_server-189"><a href="#TcpStreamManager.start_server-189"><span class="linenos">189</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamManager.start_server-190"><a href="#TcpStreamManager.start_server-190"><span class="linenos">190</span></a>        <span class="k">if</span> <span class="n">loop</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamManager.start_server-191"><a href="#TcpStreamManager.start_server-191"><span class="linenos">191</span></a>            <span class="n">loop</span> <span class="o">=</span> <span class="n">events</span><span class="o">.</span><span class="n">get_event_loop</span><span class="p">()</span>
</span><span id="TcpStreamManager.start_server-192"><a href="#TcpStreamManager.start_server-192"><span class="linenos">192</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.start_server-193"><a href="#TcpStreamManager.start_server-193"><span class="linenos">193</span></a>            <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;The loop argument is deprecated since Python 3.8, &quot;</span>
</span><span id="TcpStreamManager.start_server-194"><a href="#TcpStreamManager.start_server-194"><span class="linenos">194</span></a>                        <span class="s2">&quot;and scheduled for removal in Python 3.10.&quot;</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-195"><a href="#TcpStreamManager.start_server-195"><span class="linenos">195</span></a>                        <span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</span><span id="TcpStreamManager.start_server-196"><a href="#TcpStreamManager.start_server-196"><span class="linenos">196</span></a>
</span><span id="TcpStreamManager.start_server-197"><a href="#TcpStreamManager.start_server-197"><span class="linenos">197</span></a>        <span class="k">def</span> <span class="nf">factory</span><span class="p">():</span>
</span><span id="TcpStreamManager.start_server-198"><a href="#TcpStreamManager.start_server-198"><span class="linenos">198</span></a>            <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager.start_server-199"><a href="#TcpStreamManager.start_server-199"><span class="linenos">199</span></a>            <span class="n">reader</span> <span class="o">=</span>  <span class="n">TcpStreamReader</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.start_server-200"><a href="#TcpStreamManager.start_server-200"><span class="linenos">200</span></a>            <span class="n">protocol</span> <span class="o">=</span> <span class="n">TcpStreamReaderProtocol</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span>
</span><span id="TcpStreamManager.start_server-201"><a href="#TcpStreamManager.start_server-201"><span class="linenos">201</span></a>                                            <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.start_server-202"><a href="#TcpStreamManager.start_server-202"><span class="linenos">202</span></a>            <span class="k">return</span> <span class="n">protocol</span>
</span><span id="TcpStreamManager.start_server-203"><a href="#TcpStreamManager.start_server-203"><span class="linenos">203</span></a>
</span><span id="TcpStreamManager.start_server-204"><a href="#TcpStreamManager.start_server-204"><span class="linenos">204</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="n">loop</span><span class="o">.</span><span class="n">create_server</span><span class="p">(</span><span class="n">factory</span><span class="p">,</span> <span class="n">host</span><span class="p">,</span> <span class="n">port</span><span class="p">,</span> <span class="o">**</span><span class="n">kwds</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Start a socket server, call back for each client connected.</p>

<p>The first parameter, <code>client_connected_cb</code>, takes two parameters:
client_reader, client_writer.  client_reader is a TcpStreamReader
object, while client_writer is a TcpStreamWriter object.  This
parameter can either be a plain callback function or a coroutine;
if it is a coroutine, it will be automatically converted into a
Task.</p>

<p>The rest of the arguments are all the usual arguments to
loop.create_server() except protocol_factory; most common are
positional host and port, with various optional keyword arguments
following.  The return value is the same as loop.create_server().</p>

<p>Additional optional keyword arguments are loop (to set the event loop
instance to use) and limit (to set the buffer limit passed to the
TcpStreamReader).</p>

<p>The return value is the same as loop.create_server(), i.e. a
Server object which can be used to stop the service.</p>
</div>


                            </div>
                            <div id="TcpStreamManager.bind_accepted_connection" class="classattr">
                                        <input id="TcpStreamManager.bind_accepted_connection-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">bind_accepted_connection</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">streams</span><span class="o">.</span><span class="n">StreamReader</span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">streams</span><span class="o">.</span><span class="n">StreamWriter</span>,</span><span class="param">	<span class="o">*</span>,</span><span class="param">	<span class="n">loop</span><span class="o">=</span><span class="kc">None</span>,</span><span class="param">	<span class="n">limit</span><span class="o">=</span><span class="mi">10485760</span>,</span><span class="param">	<span class="n">stream_type</span><span class="p">:</span> <span class="n"><a href="#StreamType">StreamType</a></span> <span class="o">=</span> <span class="o">&lt;</span><span class="n"><a href="#StreamType.general">StreamType.general</a></span><span class="p">:</span> <span class="mi">0</span><span class="o">&gt;</span>,</span><span class="param">	<span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>,</span><span class="param">	<span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwds</span></span><span class="return-annotation">) -> <span class="nb">tuple</span><span class="p">[</span><span class="n"><a href="#TcpStreamReader">TcpStreamReader</a></span><span class="p">,</span> <span class="n"><a href="#TcpStreamWriter">TcpStreamWriter</a></span><span class="p">]</span>:</span></span>

                <label class="view-source-button" for="TcpStreamManager.bind_accepted_connection-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.bind_accepted_connection"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.bind_accepted_connection-206"><a href="#TcpStreamManager.bind_accepted_connection-206"><span class="linenos">206</span></a>    <span class="k">def</span> <span class="nf">bind_accepted_connection</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> 
</span><span id="TcpStreamManager.bind_accepted_connection-207"><a href="#TcpStreamManager.bind_accepted_connection-207"><span class="linenos">207</span></a>                            <span class="n">reader</span><span class="p">:</span> <span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">DEFAULT_LIMIT</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_accepted_connection-208"><a href="#TcpStreamManager.bind_accepted_connection-208"><span class="linenos">208</span></a>                            <span class="n">stream_type</span><span class="p">:</span> <span class="n">StreamType</span> <span class="o">=</span> <span class="n">StreamType</span><span class="o">.</span><span class="n">general</span><span class="p">,</span> <span class="n">stream_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(),</span>
</span><span id="TcpStreamManager.bind_accepted_connection-209"><a href="#TcpStreamManager.bind_accepted_connection-209"><span class="linenos">209</span></a>                            <span class="n">protocol_greeting</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_accepted_connection-210"><a href="#TcpStreamManager.bind_accepted_connection-210"><span class="linenos">210</span></a>                            <span class="n">max_message_size_len</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
</span><span id="TcpStreamManager.bind_accepted_connection-211"><a href="#TcpStreamManager.bind_accepted_connection-211"><span class="linenos">211</span></a>                            <span class="o">**</span><span class="n">kwds</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Tuple</span><span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">]:</span>
</span><span id="TcpStreamManager.bind_accepted_connection-212"><a href="#TcpStreamManager.bind_accepted_connection-212"><span class="linenos">212</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReader</span><span class="p">,</span> <span class="n">reader</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-213"><a href="#TcpStreamManager.bind_accepted_connection-213"><span class="linenos">213</span></a>        <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">MessageProtocolSettings</span><span class="p">(</span><span class="n">protocol_greeting</span><span class="p">,</span> <span class="n">message_size_len</span><span class="p">,</span> <span class="n">max_message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-214"><a href="#TcpStreamManager.bind_accepted_connection-214"><span class="linenos">214</span></a>        <span class="n">reader</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-215"><a href="#TcpStreamManager.bind_accepted_connection-215"><span class="linenos">215</span></a>        
</span><span id="TcpStreamManager.bind_accepted_connection-216"><a href="#TcpStreamManager.bind_accepted_connection-216"><span class="linenos">216</span></a>        <span class="n">protocol</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamReaderProtocol</span><span class="p">,</span> <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-217"><a href="#TcpStreamManager.bind_accepted_connection-217"><span class="linenos">217</span></a>        <span class="n">client_connected_cb</span> <span class="o">=</span> <span class="n">protocol</span><span class="o">.</span><span class="n">_client_connected_cb</span>
</span><span id="TcpStreamManager.bind_accepted_connection-218"><a href="#TcpStreamManager.bind_accepted_connection-218"><span class="linenos">218</span></a>        <span class="n">protocol</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">message_protocol_settings</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">client_connected_cb</span><span class="p">,</span> <span class="n">loop</span><span class="o">=</span><span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-219"><a href="#TcpStreamManager.bind_accepted_connection-219"><span class="linenos">219</span></a>        
</span><span id="TcpStreamManager.bind_accepted_connection-220"><a href="#TcpStreamManager.bind_accepted_connection-220"><span class="linenos">220</span></a>        <span class="n">transport</span> <span class="o">=</span> <span class="n">writer</span><span class="o">.</span><span class="n">_transport</span>
</span><span id="TcpStreamManager.bind_accepted_connection-221"><a href="#TcpStreamManager.bind_accepted_connection-221"><span class="linenos">221</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SSLProtocolTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_accepted_connection-222"><a href="#TcpStreamManager.bind_accepted_connection-222"><span class="linenos">222</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SSLProtocolTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-223"><a href="#TcpStreamManager.bind_accepted_connection-223"><span class="linenos">223</span></a>            <span class="n">ssl_protocol</span><span class="p">:</span> <span class="n">SSLProtocol</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">_ssl_protocol</span>
</span><span id="TcpStreamManager.bind_accepted_connection-224"><a href="#TcpStreamManager.bind_accepted_connection-224"><span class="linenos">224</span></a>            <span class="n">ssl_protocol</span><span class="o">.</span><span class="n">_set_app_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-225"><a href="#TcpStreamManager.bind_accepted_connection-225"><span class="linenos">225</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_ProactorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_accepted_connection-226"><a href="#TcpStreamManager.bind_accepted_connection-226"><span class="linenos">226</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_ProactorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-227"><a href="#TcpStreamManager.bind_accepted_connection-227"><span class="linenos">227</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-228"><a href="#TcpStreamManager.bind_accepted_connection-228"><span class="linenos">228</span></a>        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="n">_SelectorSocketTransport</span><span class="p">):</span>
</span><span id="TcpStreamManager.bind_accepted_connection-229"><a href="#TcpStreamManager.bind_accepted_connection-229"><span class="linenos">229</span></a>            <span class="n">transport</span> <span class="o">=</span> <span class="n">cast</span><span class="p">(</span><span class="n">_SelectorSocketTransport</span><span class="p">,</span> <span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-230"><a href="#TcpStreamManager.bind_accepted_connection-230"><span class="linenos">230</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">set_protocol</span><span class="p">(</span><span class="n">protocol</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-231"><a href="#TcpStreamManager.bind_accepted_connection-231"><span class="linenos">231</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.bind_accepted_connection-232"><a href="#TcpStreamManager.bind_accepted_connection-232"><span class="linenos">232</span></a>            <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport type: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-233"><a href="#TcpStreamManager.bind_accepted_connection-233"><span class="linenos">233</span></a>
</span><span id="TcpStreamManager.bind_accepted_connection-234"><a href="#TcpStreamManager.bind_accepted_connection-234"><span class="linenos">234</span></a>        <span class="n">writer</span> <span class="o">=</span> <span class="n">reinterpret_cast</span><span class="p">(</span><span class="n">TcpStreamWriter</span><span class="p">,</span> <span class="n">writer</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-235"><a href="#TcpStreamManager.bind_accepted_connection-235"><span class="linenos">235</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">,</span> <span class="n">protocol</span><span class="p">,</span> <span class="n">reader</span><span class="p">,</span> <span class="n">loop</span><span class="p">)</span>
</span><span id="TcpStreamManager.bind_accepted_connection-236"><a href="#TcpStreamManager.bind_accepted_connection-236"><span class="linenos">236</span></a>
</span><span id="TcpStreamManager.bind_accepted_connection-237"><a href="#TcpStreamManager.bind_accepted_connection-237"><span class="linenos">237</span></a>        <span class="k">return</span> <span class="n">reader</span><span class="p">,</span> <span class="n">writer</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamManager.try_establish_message_protocol_server_side" class="classattr">
                                        <input id="TcpStreamManager.try_establish_message_protocol_server_side-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">try_establish_message_protocol_server_side</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n"><a href="#TcpStreamReader">TcpStreamReader</a></span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n"><a href="#TcpStreamWriter">TcpStreamWriter</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TcpStreamManager.try_establish_message_protocol_server_side-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.try_establish_message_protocol_server_side"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.try_establish_message_protocol_server_side-239"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-239"><span class="linenos">239</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_server_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-240"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-240"><span class="linenos">240</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-241"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-241"><span class="linenos">241</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-242"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-242"><span class="linenos">242</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-243"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-243"><span class="linenos">243</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-244"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-244"><span class="linenos">244</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-245"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-245"><span class="linenos">245</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-246"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-246"><span class="linenos">246</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-247"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-247"><span class="linenos">247</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-248"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-248"><span class="linenos">248</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-249"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-249"><span class="linenos">249</span></a>        
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-250"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-250"><span class="linenos">250</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-251"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-251"><span class="linenos">251</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-252"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-252"><span class="linenos">252</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-253"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-253"><span class="linenos">253</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-254"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-254"><span class="linenos">254</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-255"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-255"><span class="linenos">255</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-256"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-256"><span class="linenos">256</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-257"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-257"><span class="linenos">257</span></a>            <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-258"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-258"><span class="linenos">258</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-259"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-259"><span class="linenos">259</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_server_side-260"><a href="#TcpStreamManager.try_establish_message_protocol_server_side-260"><span class="linenos">260</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamManager.try_establish_message_protocol_client_side" class="classattr">
                                        <input id="TcpStreamManager.try_establish_message_protocol_client_side-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">try_establish_message_protocol_client_side</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="bp">self</span>,</span><span class="param">	<span class="n">reader</span><span class="p">:</span> <span class="n"><a href="#TcpStreamReader">TcpStreamReader</a></span>,</span><span class="param">	<span class="n">writer</span><span class="p">:</span> <span class="n"><a href="#TcpStreamWriter">TcpStreamWriter</a></span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TcpStreamManager.try_establish_message_protocol_client_side-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamManager.try_establish_message_protocol_client_side"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamManager.try_establish_message_protocol_client_side-262"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-262"><span class="linenos">262</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">try_establish_message_protocol_client_side</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">reader</span><span class="p">:</span> <span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">,</span> <span class="n">writer</span><span class="p">:</span> <span class="s1">&#39;TcpStreamWriter&#39;</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-263"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-263"><span class="linenos">263</span></a>        <span class="n">message</span> <span class="o">=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-264"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-264"><span class="linenos">264</span></a>        <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-265"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-265"><span class="linenos">265</span></a>        <span class="k">await</span> <span class="n">writer</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-266"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-266"><span class="linenos">266</span></a>        <span class="n">message_size_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-267"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-267"><span class="linenos">267</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-268"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-268"><span class="linenos">268</span></a>        <span class="n">can_be_established</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-269"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-269"><span class="linenos">269</span></a>        <span class="k">if</span> <span class="n">message_size_len</span> <span class="o">&lt;=</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">max_message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-270"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-270"><span class="linenos">270</span></a>            <span class="n">message_size_encoded</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">))[</span><span class="mi">1</span><span class="p">:]</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-271"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-271"><span class="linenos">271</span></a>            <span class="n">message_size</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_size_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-272"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-272"><span class="linenos">272</span></a>            <span class="n">message</span> <span class="o">=</span> <span class="p">(</span><span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readonly_exactly</span><span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_size</span><span class="p">))[</span><span class="mi">1</span> <span class="o">+</span> <span class="n">message_size_len</span><span class="p">:]</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-273"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-273"><span class="linenos">273</span></a>            <span class="k">if</span> <span class="n">message</span> <span class="o">==</span> <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">protocol_greeting</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-274"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-274"><span class="linenos">274</span></a>                <span class="n">can_be_established</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-275"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-275"><span class="linenos">275</span></a>        
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-276"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-276"><span class="linenos">276</span></a>        <span class="k">if</span> <span class="n">can_be_established</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-277"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-277"><span class="linenos">277</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-278"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-278"><span class="linenos">278</span></a>            <span class="n">writer</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span> <span class="o">=</span> <span class="n">message_size_len</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-279"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-279"><span class="linenos">279</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-280"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-280"><span class="linenos">280</span></a>            <span class="k">await</span> <span class="n">reader</span><span class="o">.</span><span class="n">read_message</span><span class="p">()</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-281"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-281"><span class="linenos">281</span></a>            <span class="k">return</span> <span class="kc">True</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-282"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-282"><span class="linenos">282</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamManager.try_establish_message_protocol_client_side-283"><a href="#TcpStreamManager.try_establish_message_protocol_client_side-283"><span class="linenos">283</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span></pre></div>


    

                            </div>
                </section>
                <section id="TcpStreamReader">
                            <input id="TcpStreamReader-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TcpStreamReader</span><wbr>(<span class="base">asyncio.streams.StreamReader</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamReaderAbstract</span>):

                <label class="view-source-button" for="TcpStreamReader-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader-377"><a href="#TcpStreamReader-377"><span class="linenos">377</span></a><span class="k">class</span> <span class="nc">TcpStreamReader</span><span class="p">(</span><span class="n">OriginalStreamReader</span><span class="p">,</span> <span class="n">StreamReaderAbstract</span><span class="p">):</span>
</span><span id="TcpStreamReader-378"><a href="#TcpStreamReader-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-379"><a href="#TcpStreamReader-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamReader-380"><a href="#TcpStreamReader-380"><span class="linenos">380</span></a>
</span><span id="TcpStreamReader-381"><a href="#TcpStreamReader-381"><span class="linenos">381</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-382"><a href="#TcpStreamReader-382"><span class="linenos">382</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamReader-383"><a href="#TcpStreamReader-383"><span class="linenos">383</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="TcpStreamReader-384"><a href="#TcpStreamReader-384"><span class="linenos">384</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="TcpStreamReader-385"><a href="#TcpStreamReader-385"><span class="linenos">385</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">input_from_client_container_type</span><span class="p">(</span>
</span><span id="TcpStreamReader-386"><a href="#TcpStreamReader-386"><span class="linenos">386</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="p">)</span>
</span><span id="TcpStreamReader-387"><a href="#TcpStreamReader-387"><span class="linenos">387</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span> <span class="o">=</span> <span class="n">RecvBuffSizeComputer</span><span class="p">()</span>
</span><span id="TcpStreamReader-388"><a href="#TcpStreamReader-388"><span class="linenos">388</span></a>        <span class="n">cpu_info_inst</span> <span class="o">=</span> <span class="n">cpu_info</span><span class="p">()</span>
</span><span id="TcpStreamReader-389"><a href="#TcpStreamReader-389"><span class="linenos">389</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size</span>
</span><span id="TcpStreamReader-390"><a href="#TcpStreamReader-390"><span class="linenos">390</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l2_cache_size_per_virtual_core</span>
</span><span id="TcpStreamReader-391"><a href="#TcpStreamReader-391"><span class="linenos">391</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = cpu_info_inst.l3_cache_size_per_virtual_core</span>
</span><span id="TcpStreamReader-392"><a href="#TcpStreamReader-392"><span class="linenos">392</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 3145728</span>
</span><span id="TcpStreamReader-393"><a href="#TcpStreamReader-393"><span class="linenos">393</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">max_recv_buff_size</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">*</span> <span class="mi">1024</span><span class="o">**</span><span class="mi">2</span>
</span><span id="TcpStreamReader-394"><a href="#TcpStreamReader-394"><span class="linenos">394</span></a>        <span class="c1"># self.recv_buff_size_computer.max_recv_buff_size = 1024</span>
</span><span id="TcpStreamReader-395"><a href="#TcpStreamReader-395"><span class="linenos">395</span></a>        <span class="c1"># print(f&#39;max_recv_buff_size: {self.recv_buff_size_computer.max_recv_buff_size}&#39;)</span>
</span><span id="TcpStreamReader-396"><a href="#TcpStreamReader-396"><span class="linenos">396</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamReader-397"><a href="#TcpStreamReader-397"><span class="linenos">397</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamReader-398"><a href="#TcpStreamReader-398"><span class="linenos">398</span></a>    
</span><span id="TcpStreamReader-399"><a href="#TcpStreamReader-399"><span class="linenos">399</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-400"><a href="#TcpStreamReader-400"><span class="linenos">400</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="TcpStreamReader-401"><a href="#TcpStreamReader-401"><span class="linenos">401</span></a>    
</span><span id="TcpStreamReader-402"><a href="#TcpStreamReader-402"><span class="linenos">402</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-403"><a href="#TcpStreamReader-403"><span class="linenos">403</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="TcpStreamReader-404"><a href="#TcpStreamReader-404"><span class="linenos">404</span></a>    
</span><span id="TcpStreamReader-405"><a href="#TcpStreamReader-405"><span class="linenos">405</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-406"><a href="#TcpStreamReader-406"><span class="linenos">406</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-407"><a href="#TcpStreamReader-407"><span class="linenos">407</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-408"><a href="#TcpStreamReader-408"><span class="linenos">408</span></a>
</span><span id="TcpStreamReader-409"><a href="#TcpStreamReader-409"><span class="linenos">409</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader-410"><a href="#TcpStreamReader-410"><span class="linenos">410</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader-411"><a href="#TcpStreamReader-411"><span class="linenos">411</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader-412"><a href="#TcpStreamReader-412"><span class="linenos">412</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader-413"><a href="#TcpStreamReader-413"><span class="linenos">413</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader-414"><a href="#TcpStreamReader-414"><span class="linenos">414</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TcpStreamReader-415"><a href="#TcpStreamReader-415"><span class="linenos">415</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader-416"><a href="#TcpStreamReader-416"><span class="linenos">416</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="TcpStreamReader-417"><a href="#TcpStreamReader-417"><span class="linenos">417</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TcpStreamReader-418"><a href="#TcpStreamReader-418"><span class="linenos">418</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader-419"><a href="#TcpStreamReader-419"><span class="linenos">419</span></a>                <span class="k">break</span>
</span><span id="TcpStreamReader-420"><a href="#TcpStreamReader-420"><span class="linenos">420</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader-421"><a href="#TcpStreamReader-421"><span class="linenos">421</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span><span id="TcpStreamReader-422"><a href="#TcpStreamReader-422"><span class="linenos">422</span></a>
</span><span id="TcpStreamReader-423"><a href="#TcpStreamReader-423"><span class="linenos">423</span></a>    <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-424"><a href="#TcpStreamReader-424"><span class="linenos">424</span></a>        <span class="n">info</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;TcpStreamReader&#39;</span><span class="p">]</span>
</span><span id="TcpStreamReader-425"><a href="#TcpStreamReader-425"><span class="linenos">425</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="TcpStreamReader-426"><a href="#TcpStreamReader-426"><span class="linenos">426</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span><span class="si">}</span><span class="s1"> bytes&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-427"><a href="#TcpStreamReader-427"><span class="linenos">427</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-428"><a href="#TcpStreamReader-428"><span class="linenos">428</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;eof&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-429"><a href="#TcpStreamReader-429"><span class="linenos">429</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span> <span class="o">!=</span> <span class="n">DEFAULT_LIMIT</span><span class="p">:</span>
</span><span id="TcpStreamReader-430"><a href="#TcpStreamReader-430"><span class="linenos">430</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;limit=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-431"><a href="#TcpStreamReader-431"><span class="linenos">431</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="p">:</span>
</span><span id="TcpStreamReader-432"><a href="#TcpStreamReader-432"><span class="linenos">432</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;waiter=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_waiter</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-433"><a href="#TcpStreamReader-433"><span class="linenos">433</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="p">:</span>
</span><span id="TcpStreamReader-434"><a href="#TcpStreamReader-434"><span class="linenos">434</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;exception=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_exception</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-435"><a href="#TcpStreamReader-435"><span class="linenos">435</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">:</span>
</span><span id="TcpStreamReader-436"><a href="#TcpStreamReader-436"><span class="linenos">436</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;transport=</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="si">!r}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-437"><a href="#TcpStreamReader-437"><span class="linenos">437</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span><span class="p">:</span>
</span><span id="TcpStreamReader-438"><a href="#TcpStreamReader-438"><span class="linenos">438</span></a>            <span class="n">info</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s1">&#39;paused&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-439"><a href="#TcpStreamReader-439"><span class="linenos">439</span></a>        <span class="k">return</span> <span class="s1">&#39;&lt;</span><span class="si">{}</span><span class="s1">&gt;&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">info</span><span class="p">))</span>
</span><span id="TcpStreamReader-440"><a href="#TcpStreamReader-440"><span class="linenos">440</span></a>
</span><span id="TcpStreamReader-441"><a href="#TcpStreamReader-441"><span class="linenos">441</span></a>    <span class="k">def</span> <span class="nf">_maybe_resume_transport</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-442"><a href="#TcpStreamReader-442"><span class="linenos">442</span></a>        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">,</span> <span class="p">(</span>
</span><span id="TcpStreamReader-443"><a href="#TcpStreamReader-443"><span class="linenos">443</span></a>            <span class="n">proactor_events</span><span class="o">.</span><span class="n">_ProactorDatagramTransport</span><span class="p">,</span>
</span><span id="TcpStreamReader-444"><a href="#TcpStreamReader-444"><span class="linenos">444</span></a>            <span class="n">selector_events</span><span class="o">.</span><span class="n">_SelectorTransport</span><span class="p">,</span>
</span><span id="TcpStreamReader-445"><a href="#TcpStreamReader-445"><span class="linenos">445</span></a>            <span class="n">unix_events</span><span class="o">.</span><span class="n">_UnixReadPipeTransport</span>
</span><span id="TcpStreamReader-446"><a href="#TcpStreamReader-446"><span class="linenos">446</span></a>            <span class="p">)):</span>
</span><span id="TcpStreamReader-447"><a href="#TcpStreamReader-447"><span class="linenos">447</span></a>            <span class="c1"># if hasattr(self._transport, &#39;max_size&#39;):</span>
</span><span id="TcpStreamReader-448"><a href="#TcpStreamReader-448"><span class="linenos">448</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader-449"><a href="#TcpStreamReader-449"><span class="linenos">449</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">max_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">recv_buff_size</span>
</span><span id="TcpStreamReader-450"><a href="#TcpStreamReader-450"><span class="linenos">450</span></a>                <span class="c1"># print(f&#39;max_size: {self._transport.max_size}&#39;)</span>
</span><span id="TcpStreamReader-451"><a href="#TcpStreamReader-451"><span class="linenos">451</span></a>            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span>
</span><span id="TcpStreamReader-452"><a href="#TcpStreamReader-452"><span class="linenos">452</span></a>                <span class="k">pass</span>
</span><span id="TcpStreamReader-453"><a href="#TcpStreamReader-453"><span class="linenos">453</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-454"><a href="#TcpStreamReader-454"><span class="linenos">454</span></a>            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Unsupported transport: </span><span class="si">{</span><span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="p">)</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-455"><a href="#TcpStreamReader-455"><span class="linenos">455</span></a>        
</span><span id="TcpStreamReader-456"><a href="#TcpStreamReader-456"><span class="linenos">456</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> \
</span><span id="TcpStreamReader-457"><a href="#TcpStreamReader-457"><span class="linenos">457</span></a>            <span class="ow">and</span> <span class="p">(</span>
</span><span id="TcpStreamReader-458"><a href="#TcpStreamReader-458"><span class="linenos">458</span></a>                <span class="p">((</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="TcpStreamReader-459"><a href="#TcpStreamReader-459"><span class="linenos">459</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="TcpStreamReader-460"><a href="#TcpStreamReader-460"><span class="linenos">460</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">))</span> \
</span><span id="TcpStreamReader-461"><a href="#TcpStreamReader-461"><span class="linenos">461</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="p">))</span> \
</span><span id="TcpStreamReader-462"><a href="#TcpStreamReader-462"><span class="linenos">462</span></a>                <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">))</span>
</span><span id="TcpStreamReader-463"><a href="#TcpStreamReader-463"><span class="linenos">463</span></a>            <span class="p">):</span>
</span><span id="TcpStreamReader-464"><a href="#TcpStreamReader-464"><span class="linenos">464</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamReader-465"><a href="#TcpStreamReader-465"><span class="linenos">465</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span><span id="TcpStreamReader-466"><a href="#TcpStreamReader-466"><span class="linenos">466</span></a>
</span><span id="TcpStreamReader-467"><a href="#TcpStreamReader-467"><span class="linenos">467</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-468"><a href="#TcpStreamReader-468"><span class="linenos">468</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-469"><a href="#TcpStreamReader-469"><span class="linenos">469</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamReader-470"><a href="#TcpStreamReader-470"><span class="linenos">470</span></a>
</span><span id="TcpStreamReader-471"><a href="#TcpStreamReader-471"><span class="linenos">471</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamReader-472"><a href="#TcpStreamReader-472"><span class="linenos">472</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="TcpStreamReader-473"><a href="#TcpStreamReader-473"><span class="linenos">473</span></a>
</span><span id="TcpStreamReader-474"><a href="#TcpStreamReader-474"><span class="linenos">474</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="TcpStreamReader-475"><a href="#TcpStreamReader-475"><span class="linenos">475</span></a>            <span class="k">return</span>
</span><span id="TcpStreamReader-476"><a href="#TcpStreamReader-476"><span class="linenos">476</span></a>
</span><span id="TcpStreamReader-477"><a href="#TcpStreamReader-477"><span class="linenos">477</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamReader-478"><a href="#TcpStreamReader-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="TcpStreamReader-479"><a href="#TcpStreamReader-479"><span class="linenos">479</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamReader-480"><a href="#TcpStreamReader-480"><span class="linenos">480</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="TcpStreamReader-481"><a href="#TcpStreamReader-481"><span class="linenos">481</span></a>
</span><span id="TcpStreamReader-482"><a href="#TcpStreamReader-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="TcpStreamReader-483"><a href="#TcpStreamReader-483"><span class="linenos">483</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="TcpStreamReader-484"><a href="#TcpStreamReader-484"><span class="linenos">484</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="TcpStreamReader-485"><a href="#TcpStreamReader-485"><span class="linenos">485</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="TcpStreamReader-486"><a href="#TcpStreamReader-486"><span class="linenos">486</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="TcpStreamReader-487"><a href="#TcpStreamReader-487"><span class="linenos">487</span></a>                <span class="p">)):</span>
</span><span id="TcpStreamReader-488"><a href="#TcpStreamReader-488"><span class="linenos">488</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader-489"><a href="#TcpStreamReader-489"><span class="linenos">489</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="TcpStreamReader-490"><a href="#TcpStreamReader-490"><span class="linenos">490</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="TcpStreamReader-491"><a href="#TcpStreamReader-491"><span class="linenos">491</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="TcpStreamReader-492"><a href="#TcpStreamReader-492"><span class="linenos">492</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="TcpStreamReader-493"><a href="#TcpStreamReader-493"><span class="linenos">493</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="TcpStreamReader-494"><a href="#TcpStreamReader-494"><span class="linenos">494</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamReader-495"><a href="#TcpStreamReader-495"><span class="linenos">495</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-496"><a href="#TcpStreamReader-496"><span class="linenos">496</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamReader-497"><a href="#TcpStreamReader-497"><span class="linenos">497</span></a>
</span><span id="TcpStreamReader-498"><a href="#TcpStreamReader-498"><span class="linenos">498</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-499"><a href="#TcpStreamReader-499"><span class="linenos">499</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="TcpStreamReader-500"><a href="#TcpStreamReader-500"><span class="linenos">500</span></a>
</span><span id="TcpStreamReader-501"><a href="#TcpStreamReader-501"><span class="linenos">501</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="TcpStreamReader-502"><a href="#TcpStreamReader-502"><span class="linenos">502</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="TcpStreamReader-503"><a href="#TcpStreamReader-503"><span class="linenos">503</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="TcpStreamReader-504"><a href="#TcpStreamReader-504"><span class="linenos">504</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="TcpStreamReader-505"><a href="#TcpStreamReader-505"><span class="linenos">505</span></a>
</span><span id="TcpStreamReader-506"><a href="#TcpStreamReader-506"><span class="linenos">506</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="TcpStreamReader-507"><a href="#TcpStreamReader-507"><span class="linenos">507</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="TcpStreamReader-508"><a href="#TcpStreamReader-508"><span class="linenos">508</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="TcpStreamReader-509"><a href="#TcpStreamReader-509"><span class="linenos">509</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="TcpStreamReader-510"><a href="#TcpStreamReader-510"><span class="linenos">510</span></a>
</span><span id="TcpStreamReader-511"><a href="#TcpStreamReader-511"><span class="linenos">511</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader-512"><a href="#TcpStreamReader-512"><span class="linenos">512</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader-513"><a href="#TcpStreamReader-513"><span class="linenos">513</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-514"><a href="#TcpStreamReader-514"><span class="linenos">514</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TcpStreamReader-515"><a href="#TcpStreamReader-515"><span class="linenos">515</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="TcpStreamReader-516"><a href="#TcpStreamReader-516"><span class="linenos">516</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader-517"><a href="#TcpStreamReader-517"><span class="linenos">517</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="TcpStreamReader-518"><a href="#TcpStreamReader-518"><span class="linenos">518</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="TcpStreamReader-519"><a href="#TcpStreamReader-519"><span class="linenos">519</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="TcpStreamReader-520"><a href="#TcpStreamReader-520"><span class="linenos">520</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="TcpStreamReader-521"><a href="#TcpStreamReader-521"><span class="linenos">521</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="TcpStreamReader-522"><a href="#TcpStreamReader-522"><span class="linenos">522</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="TcpStreamReader-523"><a href="#TcpStreamReader-523"><span class="linenos">523</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-524"><a href="#TcpStreamReader-524"><span class="linenos">524</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="TcpStreamReader-525"><a href="#TcpStreamReader-525"><span class="linenos">525</span></a>            
</span><span id="TcpStreamReader-526"><a href="#TcpStreamReader-526"><span class="linenos">526</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-527"><a href="#TcpStreamReader-527"><span class="linenos">527</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="TcpStreamReader-528"><a href="#TcpStreamReader-528"><span class="linenos">528</span></a>        <span class="k">return</span> <span class="n">line</span>
</span><span id="TcpStreamReader-529"><a href="#TcpStreamReader-529"><span class="linenos">529</span></a>
</span><span id="TcpStreamReader-530"><a href="#TcpStreamReader-530"><span class="linenos">530</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="TcpStreamReader-531"><a href="#TcpStreamReader-531"><span class="linenos">531</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="TcpStreamReader-532"><a href="#TcpStreamReader-532"><span class="linenos">532</span></a>
</span><span id="TcpStreamReader-533"><a href="#TcpStreamReader-533"><span class="linenos">533</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="TcpStreamReader-534"><a href="#TcpStreamReader-534"><span class="linenos">534</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="TcpStreamReader-535"><a href="#TcpStreamReader-535"><span class="linenos">535</span></a><span class="sd">        separator at the end.</span>
</span><span id="TcpStreamReader-536"><a href="#TcpStreamReader-536"><span class="linenos">536</span></a>
</span><span id="TcpStreamReader-537"><a href="#TcpStreamReader-537"><span class="linenos">537</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="TcpStreamReader-538"><a href="#TcpStreamReader-538"><span class="linenos">538</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="TcpStreamReader-539"><a href="#TcpStreamReader-539"><span class="linenos">539</span></a><span class="sd">        separator.</span>
</span><span id="TcpStreamReader-540"><a href="#TcpStreamReader-540"><span class="linenos">540</span></a>
</span><span id="TcpStreamReader-541"><a href="#TcpStreamReader-541"><span class="linenos">541</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="TcpStreamReader-542"><a href="#TcpStreamReader-542"><span class="linenos">542</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="TcpStreamReader-543"><a href="#TcpStreamReader-543"><span class="linenos">543</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="TcpStreamReader-544"><a href="#TcpStreamReader-544"><span class="linenos">544</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="TcpStreamReader-545"><a href="#TcpStreamReader-545"><span class="linenos">545</span></a>
</span><span id="TcpStreamReader-546"><a href="#TcpStreamReader-546"><span class="linenos">546</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="TcpStreamReader-547"><a href="#TcpStreamReader-547"><span class="linenos">547</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="TcpStreamReader-548"><a href="#TcpStreamReader-548"><span class="linenos">548</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="TcpStreamReader-549"><a href="#TcpStreamReader-549"><span class="linenos">549</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-550"><a href="#TcpStreamReader-550"><span class="linenos">550</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="TcpStreamReader-551"><a href="#TcpStreamReader-551"><span class="linenos">551</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-552"><a href="#TcpStreamReader-552"><span class="linenos">552</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-553"><a href="#TcpStreamReader-553"><span class="linenos">553</span></a>
</span><span id="TcpStreamReader-554"><a href="#TcpStreamReader-554"><span class="linenos">554</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-555"><a href="#TcpStreamReader-555"><span class="linenos">555</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-556"><a href="#TcpStreamReader-556"><span class="linenos">556</span></a>
</span><span id="TcpStreamReader-557"><a href="#TcpStreamReader-557"><span class="linenos">557</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="TcpStreamReader-558"><a href="#TcpStreamReader-558"><span class="linenos">558</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="TcpStreamReader-559"><a href="#TcpStreamReader-559"><span class="linenos">559</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="TcpStreamReader-560"><a href="#TcpStreamReader-560"><span class="linenos">560</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="TcpStreamReader-561"><a href="#TcpStreamReader-561"><span class="linenos">561</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="TcpStreamReader-562"><a href="#TcpStreamReader-562"><span class="linenos">562</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="TcpStreamReader-563"><a href="#TcpStreamReader-563"><span class="linenos">563</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="TcpStreamReader-564"><a href="#TcpStreamReader-564"><span class="linenos">564</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="TcpStreamReader-565"><a href="#TcpStreamReader-565"><span class="linenos">565</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="TcpStreamReader-566"><a href="#TcpStreamReader-566"><span class="linenos">566</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="TcpStreamReader-567"><a href="#TcpStreamReader-567"><span class="linenos">567</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="TcpStreamReader-568"><a href="#TcpStreamReader-568"><span class="linenos">568</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="TcpStreamReader-569"><a href="#TcpStreamReader-569"><span class="linenos">569</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="TcpStreamReader-570"><a href="#TcpStreamReader-570"><span class="linenos">570</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="TcpStreamReader-571"><a href="#TcpStreamReader-571"><span class="linenos">571</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="TcpStreamReader-572"><a href="#TcpStreamReader-572"><span class="linenos">572</span></a>        <span class="c1">#   messages :)</span>
</span><span id="TcpStreamReader-573"><a href="#TcpStreamReader-573"><span class="linenos">573</span></a>
</span><span id="TcpStreamReader-574"><a href="#TcpStreamReader-574"><span class="linenos">574</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="TcpStreamReader-575"><a href="#TcpStreamReader-575"><span class="linenos">575</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="TcpStreamReader-576"><a href="#TcpStreamReader-576"><span class="linenos">576</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TcpStreamReader-577"><a href="#TcpStreamReader-577"><span class="linenos">577</span></a>
</span><span id="TcpStreamReader-578"><a href="#TcpStreamReader-578"><span class="linenos">578</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="TcpStreamReader-579"><a href="#TcpStreamReader-579"><span class="linenos">579</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="TcpStreamReader-580"><a href="#TcpStreamReader-580"><span class="linenos">580</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader-581"><a href="#TcpStreamReader-581"><span class="linenos">581</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamReader-582"><a href="#TcpStreamReader-582"><span class="linenos">582</span></a>
</span><span id="TcpStreamReader-583"><a href="#TcpStreamReader-583"><span class="linenos">583</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="TcpStreamReader-584"><a href="#TcpStreamReader-584"><span class="linenos">584</span></a>            <span class="c1"># fit.</span>
</span><span id="TcpStreamReader-585"><a href="#TcpStreamReader-585"><span class="linenos">585</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="TcpStreamReader-586"><a href="#TcpStreamReader-586"><span class="linenos">586</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="TcpStreamReader-587"><a href="#TcpStreamReader-587"><span class="linenos">587</span></a>
</span><span id="TcpStreamReader-588"><a href="#TcpStreamReader-588"><span class="linenos">588</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="TcpStreamReader-589"><a href="#TcpStreamReader-589"><span class="linenos">589</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="TcpStreamReader-590"><a href="#TcpStreamReader-590"><span class="linenos">590</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="TcpStreamReader-591"><a href="#TcpStreamReader-591"><span class="linenos">591</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader-592"><a href="#TcpStreamReader-592"><span class="linenos">592</span></a>
</span><span id="TcpStreamReader-593"><a href="#TcpStreamReader-593"><span class="linenos">593</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="TcpStreamReader-594"><a href="#TcpStreamReader-594"><span class="linenos">594</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="TcpStreamReader-595"><a href="#TcpStreamReader-595"><span class="linenos">595</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="TcpStreamReader-596"><a href="#TcpStreamReader-596"><span class="linenos">596</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="TcpStreamReader-597"><a href="#TcpStreamReader-597"><span class="linenos">597</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="TcpStreamReader-598"><a href="#TcpStreamReader-598"><span class="linenos">598</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="TcpStreamReader-599"><a href="#TcpStreamReader-599"><span class="linenos">599</span></a>
</span><span id="TcpStreamReader-600"><a href="#TcpStreamReader-600"><span class="linenos">600</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="TcpStreamReader-601"><a href="#TcpStreamReader-601"><span class="linenos">601</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="TcpStreamReader-602"><a href="#TcpStreamReader-602"><span class="linenos">602</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="TcpStreamReader-603"><a href="#TcpStreamReader-603"><span class="linenos">603</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="TcpStreamReader-604"><a href="#TcpStreamReader-604"><span class="linenos">604</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-605"><a href="#TcpStreamReader-605"><span class="linenos">605</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader-606"><a href="#TcpStreamReader-606"><span class="linenos">606</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TcpStreamReader-607"><a href="#TcpStreamReader-607"><span class="linenos">607</span></a>
</span><span id="TcpStreamReader-608"><a href="#TcpStreamReader-608"><span class="linenos">608</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="TcpStreamReader-609"><a href="#TcpStreamReader-609"><span class="linenos">609</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-610"><a href="#TcpStreamReader-610"><span class="linenos">610</span></a>
</span><span id="TcpStreamReader-611"><a href="#TcpStreamReader-611"><span class="linenos">611</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="TcpStreamReader-612"><a href="#TcpStreamReader-612"><span class="linenos">612</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="TcpStreamReader-613"><a href="#TcpStreamReader-613"><span class="linenos">613</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="TcpStreamReader-614"><a href="#TcpStreamReader-614"><span class="linenos">614</span></a>
</span><span id="TcpStreamReader-615"><a href="#TcpStreamReader-615"><span class="linenos">615</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="TcpStreamReader-616"><a href="#TcpStreamReader-616"><span class="linenos">616</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-617"><a href="#TcpStreamReader-617"><span class="linenos">617</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span><span id="TcpStreamReader-618"><a href="#TcpStreamReader-618"><span class="linenos">618</span></a>
</span><span id="TcpStreamReader-619"><a href="#TcpStreamReader-619"><span class="linenos">619</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="TcpStreamReader-620"><a href="#TcpStreamReader-620"><span class="linenos">620</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="TcpStreamReader-621"><a href="#TcpStreamReader-621"><span class="linenos">621</span></a>
</span><span id="TcpStreamReader-622"><a href="#TcpStreamReader-622"><span class="linenos">622</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="TcpStreamReader-623"><a href="#TcpStreamReader-623"><span class="linenos">623</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="TcpStreamReader-624"><a href="#TcpStreamReader-624"><span class="linenos">624</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="TcpStreamReader-625"><a href="#TcpStreamReader-625"><span class="linenos">625</span></a>
</span><span id="TcpStreamReader-626"><a href="#TcpStreamReader-626"><span class="linenos">626</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="TcpStreamReader-627"><a href="#TcpStreamReader-627"><span class="linenos">627</span></a>
</span><span id="TcpStreamReader-628"><a href="#TcpStreamReader-628"><span class="linenos">628</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="TcpStreamReader-629"><a href="#TcpStreamReader-629"><span class="linenos">629</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="TcpStreamReader-630"><a href="#TcpStreamReader-630"><span class="linenos">630</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="TcpStreamReader-631"><a href="#TcpStreamReader-631"><span class="linenos">631</span></a><span class="sd">        object.</span>
</span><span id="TcpStreamReader-632"><a href="#TcpStreamReader-632"><span class="linenos">632</span></a>
</span><span id="TcpStreamReader-633"><a href="#TcpStreamReader-633"><span class="linenos">633</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader-634"><a href="#TcpStreamReader-634"><span class="linenos">634</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader-635"><a href="#TcpStreamReader-635"><span class="linenos">635</span></a>
</span><span id="TcpStreamReader-636"><a href="#TcpStreamReader-636"><span class="linenos">636</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader-637"><a href="#TcpStreamReader-637"><span class="linenos">637</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader-638"><a href="#TcpStreamReader-638"><span class="linenos">638</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-639"><a href="#TcpStreamReader-639"><span class="linenos">639</span></a>
</span><span id="TcpStreamReader-640"><a href="#TcpStreamReader-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-641"><a href="#TcpStreamReader-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-642"><a href="#TcpStreamReader-642"><span class="linenos">642</span></a>
</span><span id="TcpStreamReader-643"><a href="#TcpStreamReader-643"><span class="linenos">643</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-644"><a href="#TcpStreamReader-644"><span class="linenos">644</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader-645"><a href="#TcpStreamReader-645"><span class="linenos">645</span></a>
</span><span id="TcpStreamReader-646"><a href="#TcpStreamReader-646"><span class="linenos">646</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-647"><a href="#TcpStreamReader-647"><span class="linenos">647</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader-648"><a href="#TcpStreamReader-648"><span class="linenos">648</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader-649"><a href="#TcpStreamReader-649"><span class="linenos">649</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader-650"><a href="#TcpStreamReader-650"><span class="linenos">650</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader-651"><a href="#TcpStreamReader-651"><span class="linenos">651</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader-652"><a href="#TcpStreamReader-652"><span class="linenos">652</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader-653"><a href="#TcpStreamReader-653"><span class="linenos">653</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader-654"><a href="#TcpStreamReader-654"><span class="linenos">654</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader-655"><a href="#TcpStreamReader-655"><span class="linenos">655</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader-656"><a href="#TcpStreamReader-656"><span class="linenos">656</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader-657"><a href="#TcpStreamReader-657"><span class="linenos">657</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="TcpStreamReader-658"><a href="#TcpStreamReader-658"><span class="linenos">658</span></a>
</span><span id="TcpStreamReader-659"><a href="#TcpStreamReader-659"><span class="linenos">659</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-660"><a href="#TcpStreamReader-660"><span class="linenos">660</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-661"><a href="#TcpStreamReader-661"><span class="linenos">661</span></a>
</span><span id="TcpStreamReader-662"><a href="#TcpStreamReader-662"><span class="linenos">662</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="TcpStreamReader-663"><a href="#TcpStreamReader-663"><span class="linenos">663</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader-664"><a href="#TcpStreamReader-664"><span class="linenos">664</span></a>
</span><span id="TcpStreamReader-665"><a href="#TcpStreamReader-665"><span class="linenos">665</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-666"><a href="#TcpStreamReader-666"><span class="linenos">666</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="TcpStreamReader-667"><a href="#TcpStreamReader-667"><span class="linenos">667</span></a>
</span><span id="TcpStreamReader-668"><a href="#TcpStreamReader-668"><span class="linenos">668</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="TcpStreamReader-669"><a href="#TcpStreamReader-669"><span class="linenos">669</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="TcpStreamReader-670"><a href="#TcpStreamReader-670"><span class="linenos">670</span></a>
</span><span id="TcpStreamReader-671"><a href="#TcpStreamReader-671"><span class="linenos">671</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="TcpStreamReader-672"><a href="#TcpStreamReader-672"><span class="linenos">672</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="TcpStreamReader-673"><a href="#TcpStreamReader-673"><span class="linenos">673</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="TcpStreamReader-674"><a href="#TcpStreamReader-674"><span class="linenos">674</span></a>
</span><span id="TcpStreamReader-675"><a href="#TcpStreamReader-675"><span class="linenos">675</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="TcpStreamReader-676"><a href="#TcpStreamReader-676"><span class="linenos">676</span></a>
</span><span id="TcpStreamReader-677"><a href="#TcpStreamReader-677"><span class="linenos">677</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="TcpStreamReader-678"><a href="#TcpStreamReader-678"><span class="linenos">678</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="TcpStreamReader-679"><a href="#TcpStreamReader-679"><span class="linenos">679</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="TcpStreamReader-680"><a href="#TcpStreamReader-680"><span class="linenos">680</span></a><span class="sd">        object.</span>
</span><span id="TcpStreamReader-681"><a href="#TcpStreamReader-681"><span class="linenos">681</span></a>
</span><span id="TcpStreamReader-682"><a href="#TcpStreamReader-682"><span class="linenos">682</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader-683"><a href="#TcpStreamReader-683"><span class="linenos">683</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader-684"><a href="#TcpStreamReader-684"><span class="linenos">684</span></a>
</span><span id="TcpStreamReader-685"><a href="#TcpStreamReader-685"><span class="linenos">685</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader-686"><a href="#TcpStreamReader-686"><span class="linenos">686</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader-687"><a href="#TcpStreamReader-687"><span class="linenos">687</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-688"><a href="#TcpStreamReader-688"><span class="linenos">688</span></a>
</span><span id="TcpStreamReader-689"><a href="#TcpStreamReader-689"><span class="linenos">689</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-690"><a href="#TcpStreamReader-690"><span class="linenos">690</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-691"><a href="#TcpStreamReader-691"><span class="linenos">691</span></a>
</span><span id="TcpStreamReader-692"><a href="#TcpStreamReader-692"><span class="linenos">692</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-693"><a href="#TcpStreamReader-693"><span class="linenos">693</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader-694"><a href="#TcpStreamReader-694"><span class="linenos">694</span></a>
</span><span id="TcpStreamReader-695"><a href="#TcpStreamReader-695"><span class="linenos">695</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-696"><a href="#TcpStreamReader-696"><span class="linenos">696</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader-697"><a href="#TcpStreamReader-697"><span class="linenos">697</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader-698"><a href="#TcpStreamReader-698"><span class="linenos">698</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader-699"><a href="#TcpStreamReader-699"><span class="linenos">699</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader-700"><a href="#TcpStreamReader-700"><span class="linenos">700</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader-701"><a href="#TcpStreamReader-701"><span class="linenos">701</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader-702"><a href="#TcpStreamReader-702"><span class="linenos">702</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader-703"><a href="#TcpStreamReader-703"><span class="linenos">703</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader-704"><a href="#TcpStreamReader-704"><span class="linenos">704</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader-705"><a href="#TcpStreamReader-705"><span class="linenos">705</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader-706"><a href="#TcpStreamReader-706"><span class="linenos">706</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="TcpStreamReader-707"><a href="#TcpStreamReader-707"><span class="linenos">707</span></a>
</span><span id="TcpStreamReader-708"><a href="#TcpStreamReader-708"><span class="linenos">708</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-709"><a href="#TcpStreamReader-709"><span class="linenos">709</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-710"><a href="#TcpStreamReader-710"><span class="linenos">710</span></a>
</span><span id="TcpStreamReader-711"><a href="#TcpStreamReader-711"><span class="linenos">711</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="TcpStreamReader-712"><a href="#TcpStreamReader-712"><span class="linenos">712</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader-713"><a href="#TcpStreamReader-713"><span class="linenos">713</span></a>
</span><span id="TcpStreamReader-714"><a href="#TcpStreamReader-714"><span class="linenos">714</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-715"><a href="#TcpStreamReader-715"><span class="linenos">715</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="TcpStreamReader-716"><a href="#TcpStreamReader-716"><span class="linenos">716</span></a>
</span><span id="TcpStreamReader-717"><a href="#TcpStreamReader-717"><span class="linenos">717</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="TcpStreamReader-718"><a href="#TcpStreamReader-718"><span class="linenos">718</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="TcpStreamReader-719"><a href="#TcpStreamReader-719"><span class="linenos">719</span></a>
</span><span id="TcpStreamReader-720"><a href="#TcpStreamReader-720"><span class="linenos">720</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="TcpStreamReader-721"><a href="#TcpStreamReader-721"><span class="linenos">721</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="TcpStreamReader-722"><a href="#TcpStreamReader-722"><span class="linenos">722</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="TcpStreamReader-723"><a href="#TcpStreamReader-723"><span class="linenos">723</span></a>
</span><span id="TcpStreamReader-724"><a href="#TcpStreamReader-724"><span class="linenos">724</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="TcpStreamReader-725"><a href="#TcpStreamReader-725"><span class="linenos">725</span></a>
</span><span id="TcpStreamReader-726"><a href="#TcpStreamReader-726"><span class="linenos">726</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader-727"><a href="#TcpStreamReader-727"><span class="linenos">727</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader-728"><a href="#TcpStreamReader-728"><span class="linenos">728</span></a>
</span><span id="TcpStreamReader-729"><a href="#TcpStreamReader-729"><span class="linenos">729</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader-730"><a href="#TcpStreamReader-730"><span class="linenos">730</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader-731"><a href="#TcpStreamReader-731"><span class="linenos">731</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader-732"><a href="#TcpStreamReader-732"><span class="linenos">732</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-733"><a href="#TcpStreamReader-733"><span class="linenos">733</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-734"><a href="#TcpStreamReader-734"><span class="linenos">734</span></a>
</span><span id="TcpStreamReader-735"><a href="#TcpStreamReader-735"><span class="linenos">735</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-736"><a href="#TcpStreamReader-736"><span class="linenos">736</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-737"><a href="#TcpStreamReader-737"><span class="linenos">737</span></a>
</span><span id="TcpStreamReader-738"><a href="#TcpStreamReader-738"><span class="linenos">738</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-739"><a href="#TcpStreamReader-739"><span class="linenos">739</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader-740"><a href="#TcpStreamReader-740"><span class="linenos">740</span></a>
</span><span id="TcpStreamReader-741"><a href="#TcpStreamReader-741"><span class="linenos">741</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader-742"><a href="#TcpStreamReader-742"><span class="linenos">742</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-743"><a href="#TcpStreamReader-743"><span class="linenos">743</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader-744"><a href="#TcpStreamReader-744"><span class="linenos">744</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader-745"><a href="#TcpStreamReader-745"><span class="linenos">745</span></a>
</span><span id="TcpStreamReader-746"><a href="#TcpStreamReader-746"><span class="linenos">746</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-747"><a href="#TcpStreamReader-747"><span class="linenos">747</span></a>
</span><span id="TcpStreamReader-748"><a href="#TcpStreamReader-748"><span class="linenos">748</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader-749"><a href="#TcpStreamReader-749"><span class="linenos">749</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader-750"><a href="#TcpStreamReader-750"><span class="linenos">750</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-751"><a href="#TcpStreamReader-751"><span class="linenos">751</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader-752"><a href="#TcpStreamReader-752"><span class="linenos">752</span></a>
</span><span id="TcpStreamReader-753"><a href="#TcpStreamReader-753"><span class="linenos">753</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-754"><a href="#TcpStreamReader-754"><span class="linenos">754</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="TcpStreamReader-755"><a href="#TcpStreamReader-755"><span class="linenos">755</span></a>    
</span><span id="TcpStreamReader-756"><a href="#TcpStreamReader-756"><span class="linenos">756</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="TcpStreamReader-757"><a href="#TcpStreamReader-757"><span class="linenos">757</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-758"><a href="#TcpStreamReader-758"><span class="linenos">758</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-759"><a href="#TcpStreamReader-759"><span class="linenos">759</span></a>
</span><span id="TcpStreamReader-760"><a href="#TcpStreamReader-760"><span class="linenos">760</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader-761"><a href="#TcpStreamReader-761"><span class="linenos">761</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader-762"><a href="#TcpStreamReader-762"><span class="linenos">762</span></a>
</span><span id="TcpStreamReader-763"><a href="#TcpStreamReader-763"><span class="linenos">763</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader-764"><a href="#TcpStreamReader-764"><span class="linenos">764</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader-765"><a href="#TcpStreamReader-765"><span class="linenos">765</span></a>
</span><span id="TcpStreamReader-766"><a href="#TcpStreamReader-766"><span class="linenos">766</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader-767"><a href="#TcpStreamReader-767"><span class="linenos">767</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader-768"><a href="#TcpStreamReader-768"><span class="linenos">768</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader-769"><a href="#TcpStreamReader-769"><span class="linenos">769</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader-770"><a href="#TcpStreamReader-770"><span class="linenos">770</span></a>
</span><span id="TcpStreamReader-771"><a href="#TcpStreamReader-771"><span class="linenos">771</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-772"><a href="#TcpStreamReader-772"><span class="linenos">772</span></a>
</span><span id="TcpStreamReader-773"><a href="#TcpStreamReader-773"><span class="linenos">773</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader-774"><a href="#TcpStreamReader-774"><span class="linenos">774</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader-775"><a href="#TcpStreamReader-775"><span class="linenos">775</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-776"><a href="#TcpStreamReader-776"><span class="linenos">776</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader-777"><a href="#TcpStreamReader-777"><span class="linenos">777</span></a>
</span><span id="TcpStreamReader-778"><a href="#TcpStreamReader-778"><span class="linenos">778</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader-779"><a href="#TcpStreamReader-779"><span class="linenos">779</span></a>        <span class="k">return</span> <span class="n">data</span>
</span><span id="TcpStreamReader-780"><a href="#TcpStreamReader-780"><span class="linenos">780</span></a>    
</span><span id="TcpStreamReader-781"><a href="#TcpStreamReader-781"><span class="linenos">781</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-782"><a href="#TcpStreamReader-782"><span class="linenos">782</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamReader-783"><a href="#TcpStreamReader-783"><span class="linenos">783</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-784"><a href="#TcpStreamReader-784"><span class="linenos">784</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span><span id="TcpStreamReader-785"><a href="#TcpStreamReader-785"><span class="linenos">785</span></a>    
</span><span id="TcpStreamReader-786"><a href="#TcpStreamReader-786"><span class="linenos">786</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamReader-787"><a href="#TcpStreamReader-787"><span class="linenos">787</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span>
</span><span id="TcpStreamReader-788"><a href="#TcpStreamReader-788"><span class="linenos">788</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamReader-789"><a href="#TcpStreamReader-789"><span class="linenos">789</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TcpStreamReader-790"><a href="#TcpStreamReader-790"><span class="linenos">790</span></a>
</span><span id="TcpStreamReader-791"><a href="#TcpStreamReader-791"><span class="linenos">791</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamReader-792"><a href="#TcpStreamReader-792"><span class="linenos">792</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader-793"><a href="#TcpStreamReader-793"><span class="linenos">793</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="TcpStreamReader-794"><a href="#TcpStreamReader-794"><span class="linenos">794</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TcpStreamReader-795"><a href="#TcpStreamReader-795"><span class="linenos">795</span></a>        
</span><span id="TcpStreamReader-796"><a href="#TcpStreamReader-796"><span class="linenos">796</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span><span id="TcpStreamReader-797"><a href="#TcpStreamReader-797"><span class="linenos">797</span></a>    
</span><span id="TcpStreamReader-798"><a href="#TcpStreamReader-798"><span class="linenos">798</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-799"><a href="#TcpStreamReader-799"><span class="linenos">799</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader-800"><a href="#TcpStreamReader-800"><span class="linenos">800</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="TcpStreamReader-801"><a href="#TcpStreamReader-801"><span class="linenos">801</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="TcpStreamReader-802"><a href="#TcpStreamReader-802"><span class="linenos">802</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="TcpStreamReader-803"><a href="#TcpStreamReader-803"><span class="linenos">803</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="TcpStreamReader-804"><a href="#TcpStreamReader-804"><span class="linenos">804</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="TcpStreamReader-805"><a href="#TcpStreamReader-805"><span class="linenos">805</span></a>            <span class="k">pass</span>
</span><span id="TcpStreamReader-806"><a href="#TcpStreamReader-806"><span class="linenos">806</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader-807"><a href="#TcpStreamReader-807"><span class="linenos">807</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamReader-808"><a href="#TcpStreamReader-808"><span class="linenos">808</span></a>    
</span><span id="TcpStreamReader-809"><a href="#TcpStreamReader-809"><span class="linenos">809</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader-810"><a href="#TcpStreamReader-810"><span class="linenos">810</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamReader-811"><a href="#TcpStreamReader-811"><span class="linenos">811</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span></pre></div>


    

                            <div id="TcpStreamReader.__init__" class="classattr">
                                        <input id="TcpStreamReader.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TcpStreamReader</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">manager</span><span class="p">:</span> <span class="n"><a href="#TcpStreamManager">TcpStreamManager</a></span>,</span><span class="param">	<span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">asyncio</span><span class="o">.</span><span class="n">efficient_streams</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">efficient_streams_base_internal</span><span class="o">.</span><span class="n">MessageProtocolSettings</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="TcpStreamReader.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.__init__-378"><a href="#TcpStreamReader.__init__-378"><span class="linenos">378</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.__init__-379"><a href="#TcpStreamReader.__init__-379"><span class="linenos">379</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.read_max" class="classattr">
                                        <input id="TcpStreamReader.read_max-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_max</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read_max-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read_max"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read_max-399"><a href="#TcpStreamReader.read_max-399"><span class="linenos">399</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.read_max-400"><a href="#TcpStreamReader.read_max-400"><span class="linenos">400</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.read_nearly_max" class="classattr">
                                        <input id="TcpStreamReader.read_nearly_max-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_nearly_max</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read_nearly_max-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read_nearly_max"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read_nearly_max-402"><a href="#TcpStreamReader.read_nearly_max-402"><span class="linenos">402</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly_max</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.read_nearly_max-403"><a href="#TcpStreamReader.read_nearly_max-403"><span class="linenos">403</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.read_with_counter" class="classattr">
                                        <input id="TcpStreamReader.read_with_counter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_with_counter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read_with_counter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read_with_counter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read_with_counter-405"><a href="#TcpStreamReader.read_with_counter-405"><span class="linenos">405</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_with_counter</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.read_with_counter-406"><a href="#TcpStreamReader.read_with_counter-406"><span class="linenos">406</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_with_counter-407"><a href="#TcpStreamReader.read_with_counter-407"><span class="linenos">407</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.read_with_counter-408"><a href="#TcpStreamReader.read_with_counter-408"><span class="linenos">408</span></a>
</span><span id="TcpStreamReader.read_with_counter-409"><a href="#TcpStreamReader.read_with_counter-409"><span class="linenos">409</span></a>        <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader.read_with_counter-410"><a href="#TcpStreamReader.read_with_counter-410"><span class="linenos">410</span></a>        <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader.read_with_counter-411"><a href="#TcpStreamReader.read_with_counter-411"><span class="linenos">411</span></a>        <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader.read_with_counter-412"><a href="#TcpStreamReader.read_with_counter-412"><span class="linenos">412</span></a>        <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader.read_with_counter-413"><a href="#TcpStreamReader.read_with_counter-413"><span class="linenos">413</span></a>        <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader.read_with_counter-414"><a href="#TcpStreamReader.read_with_counter-414"><span class="linenos">414</span></a>        <span class="n">counter</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TcpStreamReader.read_with_counter-415"><a href="#TcpStreamReader.read_with_counter-415"><span class="linenos">415</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_with_counter-416"><a href="#TcpStreamReader.read_with_counter-416"><span class="linenos">416</span></a>            <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_max</span><span class="p">()</span>
</span><span id="TcpStreamReader.read_with_counter-417"><a href="#TcpStreamReader.read_with_counter-417"><span class="linenos">417</span></a>            <span class="n">counter</span> <span class="o">+=</span> <span class="mi">1</span>
</span><span id="TcpStreamReader.read_with_counter-418"><a href="#TcpStreamReader.read_with_counter-418"><span class="linenos">418</span></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_with_counter-419"><a href="#TcpStreamReader.read_with_counter-419"><span class="linenos">419</span></a>                <span class="k">break</span>
</span><span id="TcpStreamReader.read_with_counter-420"><a href="#TcpStreamReader.read_with_counter-420"><span class="linenos">420</span></a>            <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_with_counter-421"><a href="#TcpStreamReader.read_with_counter-421"><span class="linenos">421</span></a>        <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">),</span> <span class="n">counter</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.at_eof" class="classattr">
                                        <input id="TcpStreamReader.at_eof-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">at_eof</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.at_eof-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.at_eof"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.at_eof-467"><a href="#TcpStreamReader.at_eof-467"><span class="linenos">467</span></a>    <span class="k">def</span> <span class="nf">at_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.at_eof-468"><a href="#TcpStreamReader.at_eof-468"><span class="linenos">468</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Return True if the buffer is empty and &#39;feed_eof&#39; was called.&quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.at_eof-469"><a href="#TcpStreamReader.at_eof-469"><span class="linenos">469</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Return True if the buffer is empty and 'feed_eof' was called.</p>
</div>


                            </div>
                            <div id="TcpStreamReader.feed_data" class="classattr">
                                        <input id="TcpStreamReader.feed_data-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">feed_data</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.feed_data-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.feed_data"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.feed_data-471"><a href="#TcpStreamReader.feed_data-471"><span class="linenos">471</span></a>    <span class="k">def</span> <span class="nf">feed_data</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamReader.feed_data-472"><a href="#TcpStreamReader.feed_data-472"><span class="linenos">472</span></a>        <span class="k">assert</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">,</span> <span class="s1">&#39;feed_data after feed_eof&#39;</span>
</span><span id="TcpStreamReader.feed_data-473"><a href="#TcpStreamReader.feed_data-473"><span class="linenos">473</span></a>
</span><span id="TcpStreamReader.feed_data-474"><a href="#TcpStreamReader.feed_data-474"><span class="linenos">474</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span>
</span><span id="TcpStreamReader.feed_data-475"><a href="#TcpStreamReader.feed_data-475"><span class="linenos">475</span></a>            <span class="k">return</span>
</span><span id="TcpStreamReader.feed_data-476"><a href="#TcpStreamReader.feed_data-476"><span class="linenos">476</span></a>
</span><span id="TcpStreamReader.feed_data-477"><a href="#TcpStreamReader.feed_data-477"><span class="linenos">477</span></a>        <span class="n">data_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamReader.feed_data-478"><a href="#TcpStreamReader.feed_data-478"><span class="linenos">478</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">recv_buff_size_computer</span><span class="o">.</span><span class="n">calc_new_recv_buff_size</span><span class="p">(</span><span class="n">data_len</span><span class="p">)</span>
</span><span id="TcpStreamReader.feed_data-479"><a href="#TcpStreamReader.feed_data-479"><span class="linenos">479</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamReader.feed_data-480"><a href="#TcpStreamReader.feed_data-480"><span class="linenos">480</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_wakeup_waiter</span><span class="p">()</span>
</span><span id="TcpStreamReader.feed_data-481"><a href="#TcpStreamReader.feed_data-481"><span class="linenos">481</span></a>
</span><span id="TcpStreamReader.feed_data-482"><a href="#TcpStreamReader.feed_data-482"><span class="linenos">482</span></a>        <span class="k">if</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span>
</span><span id="TcpStreamReader.feed_data-483"><a href="#TcpStreamReader.feed_data-483"><span class="linenos">483</span></a>                <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> 
</span><span id="TcpStreamReader.feed_data-484"><a href="#TcpStreamReader.feed_data-484"><span class="linenos">484</span></a>                <span class="ow">and</span> <span class="p">(</span>
</span><span id="TcpStreamReader.feed_data-485"><a href="#TcpStreamReader.feed_data-485"><span class="linenos">485</span></a>                    <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">)</span>
</span><span id="TcpStreamReader.feed_data-486"><a href="#TcpStreamReader.feed_data-486"><span class="linenos">486</span></a>                    <span class="ow">or</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">limit_by_global_in__data_size_limit</span> <span class="ow">and</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_full_size</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_in__data_size_limit</span><span class="o">.</span><span class="n">value</span><span class="p">)))</span>
</span><span id="TcpStreamReader.feed_data-487"><a href="#TcpStreamReader.feed_data-487"><span class="linenos">487</span></a>                <span class="p">)):</span>
</span><span id="TcpStreamReader.feed_data-488"><a href="#TcpStreamReader.feed_data-488"><span class="linenos">488</span></a>            <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader.feed_data-489"><a href="#TcpStreamReader.feed_data-489"><span class="linenos">489</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="TcpStreamReader.feed_data-490"><a href="#TcpStreamReader.feed_data-490"><span class="linenos">490</span></a>            <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="TcpStreamReader.feed_data-491"><a href="#TcpStreamReader.feed_data-491"><span class="linenos">491</span></a>                <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="TcpStreamReader.feed_data-492"><a href="#TcpStreamReader.feed_data-492"><span class="linenos">492</span></a>                <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="TcpStreamReader.feed_data-493"><a href="#TcpStreamReader.feed_data-493"><span class="linenos">493</span></a>                <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="TcpStreamReader.feed_data-494"><a href="#TcpStreamReader.feed_data-494"><span class="linenos">494</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamReader.feed_data-495"><a href="#TcpStreamReader.feed_data-495"><span class="linenos">495</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader.feed_data-496"><a href="#TcpStreamReader.feed_data-496"><span class="linenos">496</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.readline" class="classattr">
                                        <input id="TcpStreamReader.readline-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readline</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.readline-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.readline"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.readline-498"><a href="#TcpStreamReader.readline-498"><span class="linenos">498</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readline</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.readline-499"><a href="#TcpStreamReader.readline-499"><span class="linenos">499</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read chunk of data from the stream until newline (b&#39;\n&#39;) is found.</span>
</span><span id="TcpStreamReader.readline-500"><a href="#TcpStreamReader.readline-500"><span class="linenos">500</span></a>
</span><span id="TcpStreamReader.readline-501"><a href="#TcpStreamReader.readline-501"><span class="linenos">501</span></a><span class="sd">        On success, return chunk that ends with newline. If only partial</span>
</span><span id="TcpStreamReader.readline-502"><a href="#TcpStreamReader.readline-502"><span class="linenos">502</span></a><span class="sd">        line can be read due to EOF, return incomplete line without</span>
</span><span id="TcpStreamReader.readline-503"><a href="#TcpStreamReader.readline-503"><span class="linenos">503</span></a><span class="sd">        terminating newline. When EOF was reached while no bytes read, empty</span>
</span><span id="TcpStreamReader.readline-504"><a href="#TcpStreamReader.readline-504"><span class="linenos">504</span></a><span class="sd">        bytes object is returned.</span>
</span><span id="TcpStreamReader.readline-505"><a href="#TcpStreamReader.readline-505"><span class="linenos">505</span></a>
</span><span id="TcpStreamReader.readline-506"><a href="#TcpStreamReader.readline-506"><span class="linenos">506</span></a><span class="sd">        If limit is reached, ValueError will be raised. In that case, if</span>
</span><span id="TcpStreamReader.readline-507"><a href="#TcpStreamReader.readline-507"><span class="linenos">507</span></a><span class="sd">        newline was found, complete line including newline will be removed</span>
</span><span id="TcpStreamReader.readline-508"><a href="#TcpStreamReader.readline-508"><span class="linenos">508</span></a><span class="sd">        from internal buffer. Else, internal buffer will be cleared. Limit is</span>
</span><span id="TcpStreamReader.readline-509"><a href="#TcpStreamReader.readline-509"><span class="linenos">509</span></a><span class="sd">        compared against part of the line without newline.</span>
</span><span id="TcpStreamReader.readline-510"><a href="#TcpStreamReader.readline-510"><span class="linenos">510</span></a>
</span><span id="TcpStreamReader.readline-511"><a href="#TcpStreamReader.readline-511"><span class="linenos">511</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader.readline-512"><a href="#TcpStreamReader.readline-512"><span class="linenos">512</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader.readline-513"><a href="#TcpStreamReader.readline-513"><span class="linenos">513</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.readline-514"><a href="#TcpStreamReader.readline-514"><span class="linenos">514</span></a>        <span class="n">sep</span> <span class="o">=</span> <span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span>
</span><span id="TcpStreamReader.readline-515"><a href="#TcpStreamReader.readline-515"><span class="linenos">515</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="TcpStreamReader.readline-516"><a href="#TcpStreamReader.readline-516"><span class="linenos">516</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader.readline-517"><a href="#TcpStreamReader.readline-517"><span class="linenos">517</span></a>            <span class="n">line</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readuntil</span><span class="p">(</span><span class="n">sep</span><span class="p">)</span>
</span><span id="TcpStreamReader.readline-518"><a href="#TcpStreamReader.readline-518"><span class="linenos">518</span></a>        <span class="k">except</span> <span class="n">IncompleteReadError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="TcpStreamReader.readline-519"><a href="#TcpStreamReader.readline-519"><span class="linenos">519</span></a>            <span class="k">return</span> <span class="n">e</span><span class="o">.</span><span class="n">partial</span>
</span><span id="TcpStreamReader.readline-520"><a href="#TcpStreamReader.readline-520"><span class="linenos">520</span></a>        <span class="k">except</span> <span class="n">LimitOverrunError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
</span><span id="TcpStreamReader.readline-521"><a href="#TcpStreamReader.readline-521"><span class="linenos">521</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">sep</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">consumed</span><span class="p">):</span>
</span><span id="TcpStreamReader.readline-522"><a href="#TcpStreamReader.readline-522"><span class="linenos">522</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">consumed</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="TcpStreamReader.readline-523"><a href="#TcpStreamReader.readline-523"><span class="linenos">523</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader.readline-524"><a href="#TcpStreamReader.readline-524"><span class="linenos">524</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
</span><span id="TcpStreamReader.readline-525"><a href="#TcpStreamReader.readline-525"><span class="linenos">525</span></a>            
</span><span id="TcpStreamReader.readline-526"><a href="#TcpStreamReader.readline-526"><span class="linenos">526</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.readline-527"><a href="#TcpStreamReader.readline-527"><span class="linenos">527</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</span><span id="TcpStreamReader.readline-528"><a href="#TcpStreamReader.readline-528"><span class="linenos">528</span></a>        <span class="k">return</span> <span class="n">line</span>
</span></pre></div>


            <div class="docstring"><p>Read chunk of data from the stream until newline (b'
') is found.</p>

<pre><code>    On success, return chunk that ends with newline. If only partial
    line can be read due to EOF, return incomplete line without
    terminating newline. When EOF was reached while no bytes read, empty
    bytes object is returned.

    If limit is reached, ValueError will be raised. In that case, if
    newline was found, complete line including newline will be removed
    from internal buffer. Else, internal buffer will be cleared. Limit is
    compared against part of the line without newline.

    If stream was paused, this function will automatically resume it if
    needed.
</code></pre>
</div>


                            </div>
                            <div id="TcpStreamReader.readuntil" class="classattr">
                                        <input id="TcpStreamReader.readuntil-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readuntil</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.readuntil-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.readuntil"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.readuntil-530"><a href="#TcpStreamReader.readuntil-530"><span class="linenos">530</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readuntil</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">separator</span><span class="o">=</span><span class="sa">b</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">):</span>
</span><span id="TcpStreamReader.readuntil-531"><a href="#TcpStreamReader.readuntil-531"><span class="linenos">531</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read data from the stream until ``separator`` is found.</span>
</span><span id="TcpStreamReader.readuntil-532"><a href="#TcpStreamReader.readuntil-532"><span class="linenos">532</span></a>
</span><span id="TcpStreamReader.readuntil-533"><a href="#TcpStreamReader.readuntil-533"><span class="linenos">533</span></a><span class="sd">        On success, the data and separator will be removed from the</span>
</span><span id="TcpStreamReader.readuntil-534"><a href="#TcpStreamReader.readuntil-534"><span class="linenos">534</span></a><span class="sd">        internal buffer (consumed). Returned data will include the</span>
</span><span id="TcpStreamReader.readuntil-535"><a href="#TcpStreamReader.readuntil-535"><span class="linenos">535</span></a><span class="sd">        separator at the end.</span>
</span><span id="TcpStreamReader.readuntil-536"><a href="#TcpStreamReader.readuntil-536"><span class="linenos">536</span></a>
</span><span id="TcpStreamReader.readuntil-537"><a href="#TcpStreamReader.readuntil-537"><span class="linenos">537</span></a><span class="sd">        Configured stream limit is used to check result. Limit sets the</span>
</span><span id="TcpStreamReader.readuntil-538"><a href="#TcpStreamReader.readuntil-538"><span class="linenos">538</span></a><span class="sd">        maximal length of data that can be returned, not counting the</span>
</span><span id="TcpStreamReader.readuntil-539"><a href="#TcpStreamReader.readuntil-539"><span class="linenos">539</span></a><span class="sd">        separator.</span>
</span><span id="TcpStreamReader.readuntil-540"><a href="#TcpStreamReader.readuntil-540"><span class="linenos">540</span></a>
</span><span id="TcpStreamReader.readuntil-541"><a href="#TcpStreamReader.readuntil-541"><span class="linenos">541</span></a><span class="sd">        If an EOF occurs and the complete separator is still not found,</span>
</span><span id="TcpStreamReader.readuntil-542"><a href="#TcpStreamReader.readuntil-542"><span class="linenos">542</span></a><span class="sd">        an IncompleteReadError exception will be raised, and the internal</span>
</span><span id="TcpStreamReader.readuntil-543"><a href="#TcpStreamReader.readuntil-543"><span class="linenos">543</span></a><span class="sd">        buffer will be reset.  The IncompleteReadError.partial attribute</span>
</span><span id="TcpStreamReader.readuntil-544"><a href="#TcpStreamReader.readuntil-544"><span class="linenos">544</span></a><span class="sd">        may contain the separator partially.</span>
</span><span id="TcpStreamReader.readuntil-545"><a href="#TcpStreamReader.readuntil-545"><span class="linenos">545</span></a>
</span><span id="TcpStreamReader.readuntil-546"><a href="#TcpStreamReader.readuntil-546"><span class="linenos">546</span></a><span class="sd">        If the data cannot be read because of over limit, a</span>
</span><span id="TcpStreamReader.readuntil-547"><a href="#TcpStreamReader.readuntil-547"><span class="linenos">547</span></a><span class="sd">        LimitOverrunError exception  will be raised, and the data</span>
</span><span id="TcpStreamReader.readuntil-548"><a href="#TcpStreamReader.readuntil-548"><span class="linenos">548</span></a><span class="sd">        will be left in the internal buffer, so it can be read again.</span>
</span><span id="TcpStreamReader.readuntil-549"><a href="#TcpStreamReader.readuntil-549"><span class="linenos">549</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.readuntil-550"><a href="#TcpStreamReader.readuntil-550"><span class="linenos">550</span></a>        <span class="n">seplen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">separator</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-551"><a href="#TcpStreamReader.readuntil-551"><span class="linenos">551</span></a>        <span class="k">if</span> <span class="n">seplen</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-552"><a href="#TcpStreamReader.readuntil-552"><span class="linenos">552</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;Separator should be at least one-byte string&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-553"><a href="#TcpStreamReader.readuntil-553"><span class="linenos">553</span></a>
</span><span id="TcpStreamReader.readuntil-554"><a href="#TcpStreamReader.readuntil-554"><span class="linenos">554</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-555"><a href="#TcpStreamReader.readuntil-555"><span class="linenos">555</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.readuntil-556"><a href="#TcpStreamReader.readuntil-556"><span class="linenos">556</span></a>
</span><span id="TcpStreamReader.readuntil-557"><a href="#TcpStreamReader.readuntil-557"><span class="linenos">557</span></a>        <span class="c1"># Consume whole buffer except last bytes, which length is</span>
</span><span id="TcpStreamReader.readuntil-558"><a href="#TcpStreamReader.readuntil-558"><span class="linenos">558</span></a>        <span class="c1"># one less than seplen. Let&#39;s check corner cases with</span>
</span><span id="TcpStreamReader.readuntil-559"><a href="#TcpStreamReader.readuntil-559"><span class="linenos">559</span></a>        <span class="c1"># separator=&#39;SEPARATOR&#39;:</span>
</span><span id="TcpStreamReader.readuntil-560"><a href="#TcpStreamReader.readuntil-560"><span class="linenos">560</span></a>        <span class="c1"># * we have received almost complete separator (without last</span>
</span><span id="TcpStreamReader.readuntil-561"><a href="#TcpStreamReader.readuntil-561"><span class="linenos">561</span></a>        <span class="c1">#   byte). i.e buffer=&#39;some textSEPARATO&#39;. In this case we</span>
</span><span id="TcpStreamReader.readuntil-562"><a href="#TcpStreamReader.readuntil-562"><span class="linenos">562</span></a>        <span class="c1">#   can safely consume len(separator) - 1 bytes.</span>
</span><span id="TcpStreamReader.readuntil-563"><a href="#TcpStreamReader.readuntil-563"><span class="linenos">563</span></a>        <span class="c1"># * last byte of buffer is first byte of separator, i.e.</span>
</span><span id="TcpStreamReader.readuntil-564"><a href="#TcpStreamReader.readuntil-564"><span class="linenos">564</span></a>        <span class="c1">#   buffer=&#39;abcdefghijklmnopqrS&#39;. We may safely consume</span>
</span><span id="TcpStreamReader.readuntil-565"><a href="#TcpStreamReader.readuntil-565"><span class="linenos">565</span></a>        <span class="c1">#   everything except that last byte, but this require to</span>
</span><span id="TcpStreamReader.readuntil-566"><a href="#TcpStreamReader.readuntil-566"><span class="linenos">566</span></a>        <span class="c1">#   analyze bytes of buffer that match partial separator.</span>
</span><span id="TcpStreamReader.readuntil-567"><a href="#TcpStreamReader.readuntil-567"><span class="linenos">567</span></a>        <span class="c1">#   This is slow and/or require FSM. For this case our</span>
</span><span id="TcpStreamReader.readuntil-568"><a href="#TcpStreamReader.readuntil-568"><span class="linenos">568</span></a>        <span class="c1">#   implementation is not optimal, since require rescanning</span>
</span><span id="TcpStreamReader.readuntil-569"><a href="#TcpStreamReader.readuntil-569"><span class="linenos">569</span></a>        <span class="c1">#   of data that is known to not belong to separator. In</span>
</span><span id="TcpStreamReader.readuntil-570"><a href="#TcpStreamReader.readuntil-570"><span class="linenos">570</span></a>        <span class="c1">#   real world, separator will not be so long to notice</span>
</span><span id="TcpStreamReader.readuntil-571"><a href="#TcpStreamReader.readuntil-571"><span class="linenos">571</span></a>        <span class="c1">#   performance problems. Even when reading MIME-encoded</span>
</span><span id="TcpStreamReader.readuntil-572"><a href="#TcpStreamReader.readuntil-572"><span class="linenos">572</span></a>        <span class="c1">#   messages :)</span>
</span><span id="TcpStreamReader.readuntil-573"><a href="#TcpStreamReader.readuntil-573"><span class="linenos">573</span></a>
</span><span id="TcpStreamReader.readuntil-574"><a href="#TcpStreamReader.readuntil-574"><span class="linenos">574</span></a>        <span class="c1"># `offset` is the number of bytes from the beginning of the buffer</span>
</span><span id="TcpStreamReader.readuntil-575"><a href="#TcpStreamReader.readuntil-575"><span class="linenos">575</span></a>        <span class="c1"># where there is no occurrence of `separator`.</span>
</span><span id="TcpStreamReader.readuntil-576"><a href="#TcpStreamReader.readuntil-576"><span class="linenos">576</span></a>        <span class="n">offset</span> <span class="o">=</span> <span class="mi">0</span>
</span><span id="TcpStreamReader.readuntil-577"><a href="#TcpStreamReader.readuntil-577"><span class="linenos">577</span></a>
</span><span id="TcpStreamReader.readuntil-578"><a href="#TcpStreamReader.readuntil-578"><span class="linenos">578</span></a>        <span class="c1"># Loop until we find `separator` in the buffer, exceed the buffer size,</span>
</span><span id="TcpStreamReader.readuntil-579"><a href="#TcpStreamReader.readuntil-579"><span class="linenos">579</span></a>        <span class="c1"># or an EOF has happened.</span>
</span><span id="TcpStreamReader.readuntil-580"><a href="#TcpStreamReader.readuntil-580"><span class="linenos">580</span></a>        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-581"><a href="#TcpStreamReader.readuntil-581"><span class="linenos">581</span></a>            <span class="n">buflen</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamReader.readuntil-582"><a href="#TcpStreamReader.readuntil-582"><span class="linenos">582</span></a>
</span><span id="TcpStreamReader.readuntil-583"><a href="#TcpStreamReader.readuntil-583"><span class="linenos">583</span></a>            <span class="c1"># Check if we now have enough data in the buffer for `separator` to</span>
</span><span id="TcpStreamReader.readuntil-584"><a href="#TcpStreamReader.readuntil-584"><span class="linenos">584</span></a>            <span class="c1"># fit.</span>
</span><span id="TcpStreamReader.readuntil-585"><a href="#TcpStreamReader.readuntil-585"><span class="linenos">585</span></a>            <span class="k">if</span> <span class="n">buflen</span> <span class="o">-</span> <span class="n">offset</span> <span class="o">&gt;=</span> <span class="n">seplen</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-586"><a href="#TcpStreamReader.readuntil-586"><span class="linenos">586</span></a>                <span class="n">isep</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="n">separator</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-587"><a href="#TcpStreamReader.readuntil-587"><span class="linenos">587</span></a>
</span><span id="TcpStreamReader.readuntil-588"><a href="#TcpStreamReader.readuntil-588"><span class="linenos">588</span></a>                <span class="k">if</span> <span class="n">isep</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-589"><a href="#TcpStreamReader.readuntil-589"><span class="linenos">589</span></a>                    <span class="c1"># `separator` is in the buffer. `isep` will be used later</span>
</span><span id="TcpStreamReader.readuntil-590"><a href="#TcpStreamReader.readuntil-590"><span class="linenos">590</span></a>                    <span class="c1"># to retrieve the data.</span>
</span><span id="TcpStreamReader.readuntil-591"><a href="#TcpStreamReader.readuntil-591"><span class="linenos">591</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader.readuntil-592"><a href="#TcpStreamReader.readuntil-592"><span class="linenos">592</span></a>
</span><span id="TcpStreamReader.readuntil-593"><a href="#TcpStreamReader.readuntil-593"><span class="linenos">593</span></a>                <span class="c1"># see upper comment for explanation.</span>
</span><span id="TcpStreamReader.readuntil-594"><a href="#TcpStreamReader.readuntil-594"><span class="linenos">594</span></a>                <span class="n">offset</span> <span class="o">=</span> <span class="n">buflen</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">-</span> <span class="n">seplen</span>
</span><span id="TcpStreamReader.readuntil-595"><a href="#TcpStreamReader.readuntil-595"><span class="linenos">595</span></a>                <span class="k">if</span> <span class="n">offset</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-596"><a href="#TcpStreamReader.readuntil-596"><span class="linenos">596</span></a>                    <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="TcpStreamReader.readuntil-597"><a href="#TcpStreamReader.readuntil-597"><span class="linenos">597</span></a>                        <span class="s1">&#39;Separator is not found, and chunk exceed the limit&#39;</span><span class="p">,</span>
</span><span id="TcpStreamReader.readuntil-598"><a href="#TcpStreamReader.readuntil-598"><span class="linenos">598</span></a>                        <span class="n">offset</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-599"><a href="#TcpStreamReader.readuntil-599"><span class="linenos">599</span></a>
</span><span id="TcpStreamReader.readuntil-600"><a href="#TcpStreamReader.readuntil-600"><span class="linenos">600</span></a>            <span class="c1"># Complete message (with full separator) may be present in buffer</span>
</span><span id="TcpStreamReader.readuntil-601"><a href="#TcpStreamReader.readuntil-601"><span class="linenos">601</span></a>            <span class="c1"># even when EOF flag is set. This may happen when the last chunk</span>
</span><span id="TcpStreamReader.readuntil-602"><a href="#TcpStreamReader.readuntil-602"><span class="linenos">602</span></a>            <span class="c1"># adds data which makes separator be found. That&#39;s why we check for</span>
</span><span id="TcpStreamReader.readuntil-603"><a href="#TcpStreamReader.readuntil-603"><span class="linenos">603</span></a>            <span class="c1"># EOF *ater* inspecting the buffer.</span>
</span><span id="TcpStreamReader.readuntil-604"><a href="#TcpStreamReader.readuntil-604"><span class="linenos">604</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-605"><a href="#TcpStreamReader.readuntil-605"><span class="linenos">605</span></a>                <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader.readuntil-606"><a href="#TcpStreamReader.readuntil-606"><span class="linenos">606</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">chunk</span><span class="p">,</span> <span class="kc">None</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-607"><a href="#TcpStreamReader.readuntil-607"><span class="linenos">607</span></a>
</span><span id="TcpStreamReader.readuntil-608"><a href="#TcpStreamReader.readuntil-608"><span class="linenos">608</span></a>            <span class="c1"># _wait_for_data() will resume reading if stream was paused.</span>
</span><span id="TcpStreamReader.readuntil-609"><a href="#TcpStreamReader.readuntil-609"><span class="linenos">609</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readuntil&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-610"><a href="#TcpStreamReader.readuntil-610"><span class="linenos">610</span></a>
</span><span id="TcpStreamReader.readuntil-611"><a href="#TcpStreamReader.readuntil-611"><span class="linenos">611</span></a>        <span class="k">if</span> <span class="n">isep</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">:</span>
</span><span id="TcpStreamReader.readuntil-612"><a href="#TcpStreamReader.readuntil-612"><span class="linenos">612</span></a>            <span class="k">raise</span> <span class="n">LimitOverrunError</span><span class="p">(</span>
</span><span id="TcpStreamReader.readuntil-613"><a href="#TcpStreamReader.readuntil-613"><span class="linenos">613</span></a>                <span class="s1">&#39;Separator is found, but chunk is longer than limit&#39;</span><span class="p">,</span> <span class="n">isep</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-614"><a href="#TcpStreamReader.readuntil-614"><span class="linenos">614</span></a>
</span><span id="TcpStreamReader.readuntil-615"><a href="#TcpStreamReader.readuntil-615"><span class="linenos">615</span></a>        <span class="n">chunk</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">isep</span> <span class="o">+</span> <span class="n">seplen</span><span class="p">)</span>
</span><span id="TcpStreamReader.readuntil-616"><a href="#TcpStreamReader.readuntil-616"><span class="linenos">616</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.readuntil-617"><a href="#TcpStreamReader.readuntil-617"><span class="linenos">617</span></a>        <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">chunk</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>Read data from the stream until <code>separator</code> is found.</p>

<p>On success, the data and separator will be removed from the
internal buffer (consumed). Returned data will include the
separator at the end.</p>

<p>Configured stream limit is used to check result. Limit sets the
maximal length of data that can be returned, not counting the
separator.</p>

<p>If an EOF occurs and the complete separator is still not found,
an IncompleteReadError exception will be raised, and the internal
buffer will be reset.  The IncompleteReadError.partial attribute
may contain the separator partially.</p>

<p>If the data cannot be read because of over limit, a
LimitOverrunError exception  will be raised, and the data
will be left in the internal buffer, so it can be read again.</p>
</div>


                            </div>
                            <div id="TcpStreamReader.read" class="classattr">
                                        <input id="TcpStreamReader.read-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span><span class="o">=-</span><span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read-619"><a href="#TcpStreamReader.read-619"><span class="linenos">619</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="TcpStreamReader.read-620"><a href="#TcpStreamReader.read-620"><span class="linenos">620</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="TcpStreamReader.read-621"><a href="#TcpStreamReader.read-621"><span class="linenos">621</span></a>
</span><span id="TcpStreamReader.read-622"><a href="#TcpStreamReader.read-622"><span class="linenos">622</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="TcpStreamReader.read-623"><a href="#TcpStreamReader.read-623"><span class="linenos">623</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="TcpStreamReader.read-624"><a href="#TcpStreamReader.read-624"><span class="linenos">624</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="TcpStreamReader.read-625"><a href="#TcpStreamReader.read-625"><span class="linenos">625</span></a>
</span><span id="TcpStreamReader.read-626"><a href="#TcpStreamReader.read-626"><span class="linenos">626</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="TcpStreamReader.read-627"><a href="#TcpStreamReader.read-627"><span class="linenos">627</span></a>
</span><span id="TcpStreamReader.read-628"><a href="#TcpStreamReader.read-628"><span class="linenos">628</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="TcpStreamReader.read-629"><a href="#TcpStreamReader.read-629"><span class="linenos">629</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="TcpStreamReader.read-630"><a href="#TcpStreamReader.read-630"><span class="linenos">630</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="TcpStreamReader.read-631"><a href="#TcpStreamReader.read-631"><span class="linenos">631</span></a><span class="sd">        object.</span>
</span><span id="TcpStreamReader.read-632"><a href="#TcpStreamReader.read-632"><span class="linenos">632</span></a>
</span><span id="TcpStreamReader.read-633"><a href="#TcpStreamReader.read-633"><span class="linenos">633</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader.read-634"><a href="#TcpStreamReader.read-634"><span class="linenos">634</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader.read-635"><a href="#TcpStreamReader.read-635"><span class="linenos">635</span></a>
</span><span id="TcpStreamReader.read-636"><a href="#TcpStreamReader.read-636"><span class="linenos">636</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader.read-637"><a href="#TcpStreamReader.read-637"><span class="linenos">637</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader.read-638"><a href="#TcpStreamReader.read-638"><span class="linenos">638</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.read-639"><a href="#TcpStreamReader.read-639"><span class="linenos">639</span></a>
</span><span id="TcpStreamReader.read-640"><a href="#TcpStreamReader.read-640"><span class="linenos">640</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-641"><a href="#TcpStreamReader.read-641"><span class="linenos">641</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.read-642"><a href="#TcpStreamReader.read-642"><span class="linenos">642</span></a>
</span><span id="TcpStreamReader.read-643"><a href="#TcpStreamReader.read-643"><span class="linenos">643</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-644"><a href="#TcpStreamReader.read-644"><span class="linenos">644</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader.read-645"><a href="#TcpStreamReader.read-645"><span class="linenos">645</span></a>
</span><span id="TcpStreamReader.read-646"><a href="#TcpStreamReader.read-646"><span class="linenos">646</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-647"><a href="#TcpStreamReader.read-647"><span class="linenos">647</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader.read-648"><a href="#TcpStreamReader.read-648"><span class="linenos">648</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader.read-649"><a href="#TcpStreamReader.read-649"><span class="linenos">649</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader.read-650"><a href="#TcpStreamReader.read-650"><span class="linenos">650</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader.read-651"><a href="#TcpStreamReader.read-651"><span class="linenos">651</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader.read-652"><a href="#TcpStreamReader.read-652"><span class="linenos">652</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-653"><a href="#TcpStreamReader.read-653"><span class="linenos">653</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader.read-654"><a href="#TcpStreamReader.read-654"><span class="linenos">654</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-655"><a href="#TcpStreamReader.read-655"><span class="linenos">655</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader.read-656"><a href="#TcpStreamReader.read-656"><span class="linenos">656</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader.read-657"><a href="#TcpStreamReader.read-657"><span class="linenos">657</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="TcpStreamReader.read-658"><a href="#TcpStreamReader.read-658"><span class="linenos">658</span></a>
</span><span id="TcpStreamReader.read-659"><a href="#TcpStreamReader.read-659"><span class="linenos">659</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader.read-660"><a href="#TcpStreamReader.read-660"><span class="linenos">660</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.read-661"><a href="#TcpStreamReader.read-661"><span class="linenos">661</span></a>
</span><span id="TcpStreamReader.read-662"><a href="#TcpStreamReader.read-662"><span class="linenos">662</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="TcpStreamReader.read-663"><a href="#TcpStreamReader.read-663"><span class="linenos">663</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader.read-664"><a href="#TcpStreamReader.read-664"><span class="linenos">664</span></a>
</span><span id="TcpStreamReader.read-665"><a href="#TcpStreamReader.read-665"><span class="linenos">665</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.read-666"><a href="#TcpStreamReader.read-666"><span class="linenos">666</span></a>        <span class="k">return</span> <span class="n">data</span>
</span></pre></div>


            <div class="docstring"><p>Read up to <code>n</code> bytes from the stream.</p>

<p>If n is not provided, or set to -1, read until EOF and return all read
bytes. If the EOF was received and the internal buffer is empty, return
an empty bytes object.</p>

<p>If n is zero, return empty bytes object immediately.</p>

<p>If n is positive, this function try to read <code>n</code> bytes, and may return
less or equal bytes than requested, but at least one byte. If EOF was
received before any byte is read, this function returns empty byte
object.</p>

<p>Returned value is not limited with limit, configured at stream
creation.</p>

<p>If stream was paused, this function will automatically resume it if
needed.</p>
</div>


                            </div>
                            <div id="TcpStreamReader.read_nearly" class="classattr">
                                        <input id="TcpStreamReader.read_nearly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_nearly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span><span class="o">=-</span><span class="mi">1</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read_nearly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read_nearly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read_nearly-668"><a href="#TcpStreamReader.read_nearly-668"><span class="linenos">668</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_nearly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="o">=-</span><span class="mi">1</span><span class="p">):</span>
</span><span id="TcpStreamReader.read_nearly-669"><a href="#TcpStreamReader.read_nearly-669"><span class="linenos">669</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read up to `n` bytes from the stream.</span>
</span><span id="TcpStreamReader.read_nearly-670"><a href="#TcpStreamReader.read_nearly-670"><span class="linenos">670</span></a>
</span><span id="TcpStreamReader.read_nearly-671"><a href="#TcpStreamReader.read_nearly-671"><span class="linenos">671</span></a><span class="sd">        If n is not provided, or set to -1, read until EOF and return all read</span>
</span><span id="TcpStreamReader.read_nearly-672"><a href="#TcpStreamReader.read_nearly-672"><span class="linenos">672</span></a><span class="sd">        bytes. If the EOF was received and the internal buffer is empty, return</span>
</span><span id="TcpStreamReader.read_nearly-673"><a href="#TcpStreamReader.read_nearly-673"><span class="linenos">673</span></a><span class="sd">        an empty bytes object.</span>
</span><span id="TcpStreamReader.read_nearly-674"><a href="#TcpStreamReader.read_nearly-674"><span class="linenos">674</span></a>
</span><span id="TcpStreamReader.read_nearly-675"><a href="#TcpStreamReader.read_nearly-675"><span class="linenos">675</span></a><span class="sd">        If n is zero, return empty bytes object immediately.</span>
</span><span id="TcpStreamReader.read_nearly-676"><a href="#TcpStreamReader.read_nearly-676"><span class="linenos">676</span></a>
</span><span id="TcpStreamReader.read_nearly-677"><a href="#TcpStreamReader.read_nearly-677"><span class="linenos">677</span></a><span class="sd">        If n is positive, this function try to read `n` bytes, and may return</span>
</span><span id="TcpStreamReader.read_nearly-678"><a href="#TcpStreamReader.read_nearly-678"><span class="linenos">678</span></a><span class="sd">        less or equal bytes than requested, but at least one byte. If EOF was</span>
</span><span id="TcpStreamReader.read_nearly-679"><a href="#TcpStreamReader.read_nearly-679"><span class="linenos">679</span></a><span class="sd">        received before any byte is read, this function returns empty byte</span>
</span><span id="TcpStreamReader.read_nearly-680"><a href="#TcpStreamReader.read_nearly-680"><span class="linenos">680</span></a><span class="sd">        object.</span>
</span><span id="TcpStreamReader.read_nearly-681"><a href="#TcpStreamReader.read_nearly-681"><span class="linenos">681</span></a>
</span><span id="TcpStreamReader.read_nearly-682"><a href="#TcpStreamReader.read_nearly-682"><span class="linenos">682</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader.read_nearly-683"><a href="#TcpStreamReader.read_nearly-683"><span class="linenos">683</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader.read_nearly-684"><a href="#TcpStreamReader.read_nearly-684"><span class="linenos">684</span></a>
</span><span id="TcpStreamReader.read_nearly-685"><a href="#TcpStreamReader.read_nearly-685"><span class="linenos">685</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader.read_nearly-686"><a href="#TcpStreamReader.read_nearly-686"><span class="linenos">686</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader.read_nearly-687"><a href="#TcpStreamReader.read_nearly-687"><span class="linenos">687</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.read_nearly-688"><a href="#TcpStreamReader.read_nearly-688"><span class="linenos">688</span></a>
</span><span id="TcpStreamReader.read_nearly-689"><a href="#TcpStreamReader.read_nearly-689"><span class="linenos">689</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-690"><a href="#TcpStreamReader.read_nearly-690"><span class="linenos">690</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.read_nearly-691"><a href="#TcpStreamReader.read_nearly-691"><span class="linenos">691</span></a>
</span><span id="TcpStreamReader.read_nearly-692"><a href="#TcpStreamReader.read_nearly-692"><span class="linenos">692</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-693"><a href="#TcpStreamReader.read_nearly-693"><span class="linenos">693</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader.read_nearly-694"><a href="#TcpStreamReader.read_nearly-694"><span class="linenos">694</span></a>
</span><span id="TcpStreamReader.read_nearly-695"><a href="#TcpStreamReader.read_nearly-695"><span class="linenos">695</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-696"><a href="#TcpStreamReader.read_nearly-696"><span class="linenos">696</span></a>            <span class="c1"># This used to just loop creating a new waiter hoping to</span>
</span><span id="TcpStreamReader.read_nearly-697"><a href="#TcpStreamReader.read_nearly-697"><span class="linenos">697</span></a>            <span class="c1"># collect everything in self._buffer, but that would</span>
</span><span id="TcpStreamReader.read_nearly-698"><a href="#TcpStreamReader.read_nearly-698"><span class="linenos">698</span></a>            <span class="c1"># deadlock if the subprocess sends more than self.limit</span>
</span><span id="TcpStreamReader.read_nearly-699"><a href="#TcpStreamReader.read_nearly-699"><span class="linenos">699</span></a>            <span class="c1"># bytes.  So just call self.read(self._limit) until EOF.</span>
</span><span id="TcpStreamReader.read_nearly-700"><a href="#TcpStreamReader.read_nearly-700"><span class="linenos">700</span></a>            <span class="n">blocks</span> <span class="o">=</span> <span class="p">[]</span>
</span><span id="TcpStreamReader.read_nearly-701"><a href="#TcpStreamReader.read_nearly-701"><span class="linenos">701</span></a>            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-702"><a href="#TcpStreamReader.read_nearly-702"><span class="linenos">702</span></a>                <span class="n">block</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">read_nearly</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_limit</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()))</span>
</span><span id="TcpStreamReader.read_nearly-703"><a href="#TcpStreamReader.read_nearly-703"><span class="linenos">703</span></a>                <span class="k">if</span> <span class="ow">not</span> <span class="n">block</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-704"><a href="#TcpStreamReader.read_nearly-704"><span class="linenos">704</span></a>                    <span class="k">break</span>
</span><span id="TcpStreamReader.read_nearly-705"><a href="#TcpStreamReader.read_nearly-705"><span class="linenos">705</span></a>                <span class="n">blocks</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">block</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_nearly-706"><a href="#TcpStreamReader.read_nearly-706"><span class="linenos">706</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">blocks</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_nearly-707"><a href="#TcpStreamReader.read_nearly-707"><span class="linenos">707</span></a>
</span><span id="TcpStreamReader.read_nearly-708"><a href="#TcpStreamReader.read_nearly-708"><span class="linenos">708</span></a>        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="ow">and</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader.read_nearly-709"><a href="#TcpStreamReader.read_nearly-709"><span class="linenos">709</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;read&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_nearly-710"><a href="#TcpStreamReader.read_nearly-710"><span class="linenos">710</span></a>
</span><span id="TcpStreamReader.read_nearly-711"><a href="#TcpStreamReader.read_nearly-711"><span class="linenos">711</span></a>        <span class="c1"># This will work right even if buffer is less than n bytes</span>
</span><span id="TcpStreamReader.read_nearly-712"><a href="#TcpStreamReader.read_nearly-712"><span class="linenos">712</span></a>        <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data_nearly</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_nearly-713"><a href="#TcpStreamReader.read_nearly-713"><span class="linenos">713</span></a>
</span><span id="TcpStreamReader.read_nearly-714"><a href="#TcpStreamReader.read_nearly-714"><span class="linenos">714</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.read_nearly-715"><a href="#TcpStreamReader.read_nearly-715"><span class="linenos">715</span></a>        <span class="k">return</span> <span class="n">data</span>
</span></pre></div>


            <div class="docstring"><p>Read up to <code>n</code> bytes from the stream.</p>

<p>If n is not provided, or set to -1, read until EOF and return all read
bytes. If the EOF was received and the internal buffer is empty, return
an empty bytes object.</p>

<p>If n is zero, return empty bytes object immediately.</p>

<p>If n is positive, this function try to read <code>n</code> bytes, and may return
less or equal bytes than requested, but at least one byte. If EOF was
received before any byte is read, this function returns empty byte
object.</p>

<p>Returned value is not limited with limit, configured at stream
creation.</p>

<p>If stream was paused, this function will automatically resume it if
needed.</p>
</div>


                            </div>
                            <div id="TcpStreamReader.readexactly" class="classattr">
                                        <input id="TcpStreamReader.readexactly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readexactly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.readexactly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.readexactly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.readexactly-717"><a href="#TcpStreamReader.readexactly-717"><span class="linenos">717</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="TcpStreamReader.readexactly-718"><a href="#TcpStreamReader.readexactly-718"><span class="linenos">718</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;Read exactly `n` bytes.</span>
</span><span id="TcpStreamReader.readexactly-719"><a href="#TcpStreamReader.readexactly-719"><span class="linenos">719</span></a>
</span><span id="TcpStreamReader.readexactly-720"><a href="#TcpStreamReader.readexactly-720"><span class="linenos">720</span></a><span class="sd">        Raise an IncompleteReadError if EOF is reached before `n` bytes can be</span>
</span><span id="TcpStreamReader.readexactly-721"><a href="#TcpStreamReader.readexactly-721"><span class="linenos">721</span></a><span class="sd">        read. The IncompleteReadError.partial attribute of the exception will</span>
</span><span id="TcpStreamReader.readexactly-722"><a href="#TcpStreamReader.readexactly-722"><span class="linenos">722</span></a><span class="sd">        contain the partial read bytes.</span>
</span><span id="TcpStreamReader.readexactly-723"><a href="#TcpStreamReader.readexactly-723"><span class="linenos">723</span></a>
</span><span id="TcpStreamReader.readexactly-724"><a href="#TcpStreamReader.readexactly-724"><span class="linenos">724</span></a><span class="sd">        if n is zero, return empty bytes object.</span>
</span><span id="TcpStreamReader.readexactly-725"><a href="#TcpStreamReader.readexactly-725"><span class="linenos">725</span></a>
</span><span id="TcpStreamReader.readexactly-726"><a href="#TcpStreamReader.readexactly-726"><span class="linenos">726</span></a><span class="sd">        Returned value is not limited with limit, configured at stream</span>
</span><span id="TcpStreamReader.readexactly-727"><a href="#TcpStreamReader.readexactly-727"><span class="linenos">727</span></a><span class="sd">        creation.</span>
</span><span id="TcpStreamReader.readexactly-728"><a href="#TcpStreamReader.readexactly-728"><span class="linenos">728</span></a>
</span><span id="TcpStreamReader.readexactly-729"><a href="#TcpStreamReader.readexactly-729"><span class="linenos">729</span></a><span class="sd">        If stream was paused, this function will automatically resume it if</span>
</span><span id="TcpStreamReader.readexactly-730"><a href="#TcpStreamReader.readexactly-730"><span class="linenos">730</span></a><span class="sd">        needed.</span>
</span><span id="TcpStreamReader.readexactly-731"><a href="#TcpStreamReader.readexactly-731"><span class="linenos">731</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamReader.readexactly-732"><a href="#TcpStreamReader.readexactly-732"><span class="linenos">732</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-733"><a href="#TcpStreamReader.readexactly-733"><span class="linenos">733</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readexactly-734"><a href="#TcpStreamReader.readexactly-734"><span class="linenos">734</span></a>
</span><span id="TcpStreamReader.readexactly-735"><a href="#TcpStreamReader.readexactly-735"><span class="linenos">735</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-736"><a href="#TcpStreamReader.readexactly-736"><span class="linenos">736</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.readexactly-737"><a href="#TcpStreamReader.readexactly-737"><span class="linenos">737</span></a>
</span><span id="TcpStreamReader.readexactly-738"><a href="#TcpStreamReader.readexactly-738"><span class="linenos">738</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-739"><a href="#TcpStreamReader.readexactly-739"><span class="linenos">739</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader.readexactly-740"><a href="#TcpStreamReader.readexactly-740"><span class="linenos">740</span></a>
</span><span id="TcpStreamReader.readexactly-741"><a href="#TcpStreamReader.readexactly-741"><span class="linenos">741</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-742"><a href="#TcpStreamReader.readexactly-742"><span class="linenos">742</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-743"><a href="#TcpStreamReader.readexactly-743"><span class="linenos">743</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader.readexactly-744"><a href="#TcpStreamReader.readexactly-744"><span class="linenos">744</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader.readexactly-745"><a href="#TcpStreamReader.readexactly-745"><span class="linenos">745</span></a>
</span><span id="TcpStreamReader.readexactly-746"><a href="#TcpStreamReader.readexactly-746"><span class="linenos">746</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readexactly-747"><a href="#TcpStreamReader.readexactly-747"><span class="linenos">747</span></a>
</span><span id="TcpStreamReader.readexactly-748"><a href="#TcpStreamReader.readexactly-748"><span class="linenos">748</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-749"><a href="#TcpStreamReader.readexactly-749"><span class="linenos">749</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader.readexactly-750"><a href="#TcpStreamReader.readexactly-750"><span class="linenos">750</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader.readexactly-751"><a href="#TcpStreamReader.readexactly-751"><span class="linenos">751</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader.readexactly-752"><a href="#TcpStreamReader.readexactly-752"><span class="linenos">752</span></a>
</span><span id="TcpStreamReader.readexactly-753"><a href="#TcpStreamReader.readexactly-753"><span class="linenos">753</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.readexactly-754"><a href="#TcpStreamReader.readexactly-754"><span class="linenos">754</span></a>        <span class="k">return</span> <span class="n">data</span>
</span></pre></div>


            <div class="docstring"><p>Read exactly <code>n</code> bytes.</p>

<p>Raise an IncompleteReadError if EOF is reached before <code>n</code> bytes can be
read. The IncompleteReadError.partial attribute of the exception will
contain the partial read bytes.</p>

<p>if n is zero, return empty bytes object.</p>

<p>Returned value is not limited with limit, configured at stream
creation.</p>

<p>If stream was paused, this function will automatically resume it if
needed.</p>
</div>


                            </div>
                            <div id="TcpStreamReader.readonly_exactly" class="classattr">
                                        <input id="TcpStreamReader.readonly_exactly-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">readonly_exactly</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">n</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.readonly_exactly-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.readonly_exactly"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.readonly_exactly-756"><a href="#TcpStreamReader.readonly_exactly-756"><span class="linenos">756</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">readonly_exactly</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
</span><span id="TcpStreamReader.readonly_exactly-757"><a href="#TcpStreamReader.readonly_exactly-757"><span class="linenos">757</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-758"><a href="#TcpStreamReader.readonly_exactly-758"><span class="linenos">758</span></a>            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">&#39;readexactly size can not be less than zero&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readonly_exactly-759"><a href="#TcpStreamReader.readonly_exactly-759"><span class="linenos">759</span></a>
</span><span id="TcpStreamReader.readonly_exactly-760"><a href="#TcpStreamReader.readonly_exactly-760"><span class="linenos">760</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-761"><a href="#TcpStreamReader.readonly_exactly-761"><span class="linenos">761</span></a>            <span class="k">raise</span> <span class="bp">self</span><span class="o">.</span><span class="n">_exception</span>
</span><span id="TcpStreamReader.readonly_exactly-762"><a href="#TcpStreamReader.readonly_exactly-762"><span class="linenos">762</span></a>
</span><span id="TcpStreamReader.readonly_exactly-763"><a href="#TcpStreamReader.readonly_exactly-763"><span class="linenos">763</span></a>        <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-764"><a href="#TcpStreamReader.readonly_exactly-764"><span class="linenos">764</span></a>            <span class="k">return</span> <span class="sa">b</span><span class="s1">&#39;&#39;</span>
</span><span id="TcpStreamReader.readonly_exactly-765"><a href="#TcpStreamReader.readonly_exactly-765"><span class="linenos">765</span></a>
</span><span id="TcpStreamReader.readonly_exactly-766"><a href="#TcpStreamReader.readonly_exactly-766"><span class="linenos">766</span></a>        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-767"><a href="#TcpStreamReader.readonly_exactly-767"><span class="linenos">767</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_eof</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-768"><a href="#TcpStreamReader.readonly_exactly-768"><span class="linenos">768</span></a>                <span class="n">incomplete</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader.readonly_exactly-769"><a href="#TcpStreamReader.readonly_exactly-769"><span class="linenos">769</span></a>                <span class="k">raise</span> <span class="n">IncompleteReadError</span><span class="p">(</span><span class="n">incomplete</span><span class="p">,</span> <span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader.readonly_exactly-770"><a href="#TcpStreamReader.readonly_exactly-770"><span class="linenos">770</span></a>
</span><span id="TcpStreamReader.readonly_exactly-771"><a href="#TcpStreamReader.readonly_exactly-771"><span class="linenos">771</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_wait_for_data</span><span class="p">(</span><span class="s1">&#39;readexactly&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.readonly_exactly-772"><a href="#TcpStreamReader.readonly_exactly-772"><span class="linenos">772</span></a>
</span><span id="TcpStreamReader.readonly_exactly-773"><a href="#TcpStreamReader.readonly_exactly-773"><span class="linenos">773</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">==</span> <span class="n">n</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-774"><a href="#TcpStreamReader.readonly_exactly-774"><span class="linenos">774</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">())</span>
</span><span id="TcpStreamReader.readonly_exactly-775"><a href="#TcpStreamReader.readonly_exactly-775"><span class="linenos">775</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader.readonly_exactly-776"><a href="#TcpStreamReader.readonly_exactly-776"><span class="linenos">776</span></a>            <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">read_data</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
</span><span id="TcpStreamReader.readonly_exactly-777"><a href="#TcpStreamReader.readonly_exactly-777"><span class="linenos">777</span></a>
</span><span id="TcpStreamReader.readonly_exactly-778"><a href="#TcpStreamReader.readonly_exactly-778"><span class="linenos">778</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_maybe_resume_transport</span><span class="p">()</span>
</span><span id="TcpStreamReader.readonly_exactly-779"><a href="#TcpStreamReader.readonly_exactly-779"><span class="linenos">779</span></a>        <span class="k">return</span> <span class="n">data</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.read_message" class="classattr">
                                        <input id="TcpStreamReader.read_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">read_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.read_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.read_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.read_message-781"><a href="#TcpStreamReader.read_message-781"><span class="linenos">781</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">read_message</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.read_message-782"><a href="#TcpStreamReader.read_message-782"><span class="linenos">782</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_message-783"><a href="#TcpStreamReader.read_message-783"><span class="linenos">783</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.read_message-784"><a href="#TcpStreamReader.read_message-784"><span class="linenos">784</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">readexactly</span><span class="p">(</span><span class="n">message_len</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.message_awailable" class="classattr">
                                        <input id="TcpStreamReader.message_awailable-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">message_awailable</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">) -> <span class="nb">bool</span>:</span></span>

                <label class="view-source-button" for="TcpStreamReader.message_awailable-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.message_awailable"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.message_awailable-786"><a href="#TcpStreamReader.message_awailable-786"><span class="linenos">786</span></a>    <span class="k">def</span> <span class="nf">message_awailable</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
</span><span id="TcpStreamReader.message_awailable-787"><a href="#TcpStreamReader.message_awailable-787"><span class="linenos">787</span></a>        <span class="n">message_size_len</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span>
</span><span id="TcpStreamReader.message_awailable-788"><a href="#TcpStreamReader.message_awailable-788"><span class="linenos">788</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">message_size_len</span><span class="p">:</span>
</span><span id="TcpStreamReader.message_awailable-789"><a href="#TcpStreamReader.message_awailable-789"><span class="linenos">789</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TcpStreamReader.message_awailable-790"><a href="#TcpStreamReader.message_awailable-790"><span class="linenos">790</span></a>
</span><span id="TcpStreamReader.message_awailable-791"><a href="#TcpStreamReader.message_awailable-791"><span class="linenos">791</span></a>        <span class="n">message_len_encoded</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">message_size_len</span><span class="p">)</span>
</span><span id="TcpStreamReader.message_awailable-792"><a href="#TcpStreamReader.message_awailable-792"><span class="linenos">792</span></a>        <span class="n">message_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><span class="n">message_len_encoded</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReader.message_awailable-793"><a href="#TcpStreamReader.message_awailable-793"><span class="linenos">793</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_smart_buffer</span><span class="o">.</span><span class="n">size</span><span class="p">()</span> <span class="o">&lt;</span> <span class="p">(</span><span class="n">message_size_len</span> <span class="o">+</span> <span class="n">message_len</span><span class="p">):</span>
</span><span id="TcpStreamReader.message_awailable-794"><a href="#TcpStreamReader.message_awailable-794"><span class="linenos">794</span></a>            <span class="k">return</span> <span class="kc">False</span>
</span><span id="TcpStreamReader.message_awailable-795"><a href="#TcpStreamReader.message_awailable-795"><span class="linenos">795</span></a>        
</span><span id="TcpStreamReader.message_awailable-796"><a href="#TcpStreamReader.message_awailable-796"><span class="linenos">796</span></a>        <span class="k">return</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.transport_pause_reading" class="classattr">
                                        <input id="TcpStreamReader.transport_pause_reading-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">transport_pause_reading</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.transport_pause_reading-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.transport_pause_reading"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.transport_pause_reading-798"><a href="#TcpStreamReader.transport_pause_reading-798"><span class="linenos">798</span></a>    <span class="k">def</span> <span class="nf">transport_pause_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.transport_pause_reading-799"><a href="#TcpStreamReader.transport_pause_reading-799"><span class="linenos">799</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamReader.transport_pause_reading-800"><a href="#TcpStreamReader.transport_pause_reading-800"><span class="linenos">800</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">pause_reading</span><span class="p">()</span>
</span><span id="TcpStreamReader.transport_pause_reading-801"><a href="#TcpStreamReader.transport_pause_reading-801"><span class="linenos">801</span></a>        <span class="k">except</span> <span class="ne">NotImplementedError</span><span class="p">:</span>
</span><span id="TcpStreamReader.transport_pause_reading-802"><a href="#TcpStreamReader.transport_pause_reading-802"><span class="linenos">802</span></a>            <span class="c1"># The transport can&#39;t be paused.</span>
</span><span id="TcpStreamReader.transport_pause_reading-803"><a href="#TcpStreamReader.transport_pause_reading-803"><span class="linenos">803</span></a>            <span class="c1"># We&#39;ll just have to buffer all data.</span>
</span><span id="TcpStreamReader.transport_pause_reading-804"><a href="#TcpStreamReader.transport_pause_reading-804"><span class="linenos">804</span></a>            <span class="c1"># Forget the transport so we don&#39;t keep trying.</span>
</span><span id="TcpStreamReader.transport_pause_reading-805"><a href="#TcpStreamReader.transport_pause_reading-805"><span class="linenos">805</span></a>            <span class="k">pass</span>
</span><span id="TcpStreamReader.transport_pause_reading-806"><a href="#TcpStreamReader.transport_pause_reading-806"><span class="linenos">806</span></a>        <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamReader.transport_pause_reading-807"><a href="#TcpStreamReader.transport_pause_reading-807"><span class="linenos">807</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">True</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReader.transport_resume_reading" class="classattr">
                                        <input id="TcpStreamReader.transport_resume_reading-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">transport_resume_reading</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReader.transport_resume_reading-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReader.transport_resume_reading"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReader.transport_resume_reading-809"><a href="#TcpStreamReader.transport_resume_reading-809"><span class="linenos">809</span></a>    <span class="k">def</span> <span class="nf">transport_resume_reading</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamReader.transport_resume_reading-810"><a href="#TcpStreamReader.transport_resume_reading-810"><span class="linenos">810</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_paused</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamReader.transport_resume_reading-811"><a href="#TcpStreamReader.transport_resume_reading-811"><span class="linenos">811</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span><span class="o">.</span><span class="n">resume_reading</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.streams.StreamReader</dt>
                                <dd id="TcpStreamReader.exception" class="function">exception</dd>
                <dd id="TcpStreamReader.set_exception" class="function">set_exception</dd>
                <dd id="TcpStreamReader.set_transport" class="function">set_transport</dd>
                <dd id="TcpStreamReader.feed_eof" class="function">feed_eof</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TcpStreamReaderProtocol">
                            <input id="TcpStreamReaderProtocol-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TcpStreamReaderProtocol</span><wbr>(<span class="base">asyncio.streams.StreamReaderProtocol</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamReaderProtocolAbstract</span>):

                <label class="view-source-button" for="TcpStreamReaderProtocol-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReaderProtocol"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReaderProtocol-841"><a href="#TcpStreamReaderProtocol-841"><span class="linenos">841</span></a><span class="k">class</span> <span class="nc">TcpStreamReaderProtocol</span><span class="p">(</span><span class="n">OriginalStreamReaderProtocol</span><span class="p">,</span> <span class="n">StreamReaderProtocolAbstract</span><span class="p">):</span>
</span><span id="TcpStreamReaderProtocol-842"><a href="#TcpStreamReaderProtocol-842"><span class="linenos">842</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-843"><a href="#TcpStreamReaderProtocol-843"><span class="linenos">843</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-844"><a href="#TcpStreamReaderProtocol-844"><span class="linenos">844</span></a>
</span><span id="TcpStreamReaderProtocol-845"><a href="#TcpStreamReaderProtocol-845"><span class="linenos">845</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-846"><a href="#TcpStreamReaderProtocol-846"><span class="linenos">846</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-847"><a href="#TcpStreamReaderProtocol-847"><span class="linenos">847</span></a>
</span><span id="TcpStreamReaderProtocol-848"><a href="#TcpStreamReaderProtocol-848"><span class="linenos">848</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span> <span class="o">=</span> <span class="n">manager</span>
</span><span id="TcpStreamReaderProtocol-849"><a href="#TcpStreamReaderProtocol-849"><span class="linenos">849</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span> <span class="o">=</span> <span class="n">message_protocol_settings</span>
</span><span id="TcpStreamReaderProtocol-850"><a href="#TcpStreamReaderProtocol-850"><span class="linenos">850</span></a>
</span><span id="TcpStreamReaderProtocol-851"><a href="#TcpStreamReaderProtocol-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="TcpStreamReaderProtocol-852"><a href="#TcpStreamReaderProtocol-852"><span class="linenos">852</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-853"><a href="#TcpStreamReaderProtocol-853"><span class="linenos">853</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TcpStreamReaderProtocol-854"><a href="#TcpStreamReaderProtocol-854"><span class="linenos">854</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="TcpStreamReaderProtocol-855"><a href="#TcpStreamReaderProtocol-855"><span class="linenos">855</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="TcpStreamReaderProtocol-856"><a href="#TcpStreamReaderProtocol-856"><span class="linenos">856</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-857"><a href="#TcpStreamReaderProtocol-857"><span class="linenos">857</span></a>            <span class="p">}</span>
</span><span id="TcpStreamReaderProtocol-858"><a href="#TcpStreamReaderProtocol-858"><span class="linenos">858</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-859"><a href="#TcpStreamReaderProtocol-859"><span class="linenos">859</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="TcpStreamReaderProtocol-860"><a href="#TcpStreamReaderProtocol-860"><span class="linenos">860</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-861"><a href="#TcpStreamReaderProtocol-861"><span class="linenos">861</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="TcpStreamReaderProtocol-862"><a href="#TcpStreamReaderProtocol-862"><span class="linenos">862</span></a>            <span class="k">return</span>
</span><span id="TcpStreamReaderProtocol-863"><a href="#TcpStreamReaderProtocol-863"><span class="linenos">863</span></a>        
</span><span id="TcpStreamReaderProtocol-864"><a href="#TcpStreamReaderProtocol-864"><span class="linenos">864</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="TcpStreamReaderProtocol-865"><a href="#TcpStreamReaderProtocol-865"><span class="linenos">865</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="TcpStreamReaderProtocol-866"><a href="#TcpStreamReaderProtocol-866"><span class="linenos">866</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-867"><a href="#TcpStreamReaderProtocol-867"><span class="linenos">867</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-868"><a href="#TcpStreamReaderProtocol-868"><span class="linenos">868</span></a>
</span><span id="TcpStreamReaderProtocol-869"><a href="#TcpStreamReaderProtocol-869"><span class="linenos">869</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="TcpStreamReaderProtocol-870"><a href="#TcpStreamReaderProtocol-870"><span class="linenos">870</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol-871"><a href="#TcpStreamReaderProtocol-871"><span class="linenos">871</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol-872"><a href="#TcpStreamReaderProtocol-872"><span class="linenos">872</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol-873"><a href="#TcpStreamReaderProtocol-873"><span class="linenos">873</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-874"><a href="#TcpStreamReaderProtocol-874"><span class="linenos">874</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol-875"><a href="#TcpStreamReaderProtocol-875"><span class="linenos">875</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-876"><a href="#TcpStreamReaderProtocol-876"><span class="linenos">876</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="TcpStreamReaderProtocol-877"><a href="#TcpStreamReaderProtocol-877"><span class="linenos">877</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol-878"><a href="#TcpStreamReaderProtocol-878"><span class="linenos">878</span></a>            
</span><span id="TcpStreamReaderProtocol-879"><a href="#TcpStreamReaderProtocol-879"><span class="linenos">879</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Helper class to adapt between Protocol and StreamReader.</p>

<p>(This is a helper class instead of making StreamReader itself a
Protocol subclass, because the StreamReader has other potential
uses, and to prevent the user of the StreamReader to accidentally
call inappropriate methods of the protocol.)</p>
</div>


                            <div id="TcpStreamReaderProtocol.__init__" class="classattr">
                                        <input id="TcpStreamReaderProtocol.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TcpStreamReaderProtocol</span><span class="signature pdoc-code multiline">(<span class="param">	<span class="n">manager</span><span class="p">:</span> <span class="n"><a href="#TcpStreamManager">TcpStreamManager</a></span>,</span><span class="param">	<span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">cengal</span><span class="o">.</span><span class="n">parallel_execution</span><span class="o">.</span><span class="n">asyncio</span><span class="o">.</span><span class="n">efficient_streams</span><span class="o">.</span><span class="n">versions</span><span class="o">.</span><span class="n">v_0</span><span class="o">.</span><span class="n">efficient_streams_base_internal</span><span class="o">.</span><span class="n">MessageProtocolSettings</span>,</span><span class="param">	<span class="o">*</span><span class="n">args</span>,</span><span class="param">	<span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="TcpStreamReaderProtocol.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReaderProtocol.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReaderProtocol.__init__-842"><a href="#TcpStreamReaderProtocol.__init__-842"><span class="linenos">842</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">:</span> <span class="n">MessageProtocolSettings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol.__init__-843"><a href="#TcpStreamReaderProtocol.__init__-843"><span class="linenos">843</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="n">manager</span><span class="p">,</span> <span class="n">message_protocol_settings</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamReaderProtocol.connection_made" class="classattr">
                                        <input id="TcpStreamReaderProtocol.connection_made-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">connection_made</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">transport</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamReaderProtocol.connection_made-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamReaderProtocol.connection_made"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamReaderProtocol.connection_made-851"><a href="#TcpStreamReaderProtocol.connection_made-851"><span class="linenos">851</span></a>    <span class="k">def</span> <span class="nf">connection_made</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">transport</span><span class="p">):</span>
</span><span id="TcpStreamReaderProtocol.connection_made-852"><a href="#TcpStreamReaderProtocol.connection_made-852"><span class="linenos">852</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_reject_connection</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol.connection_made-853"><a href="#TcpStreamReaderProtocol.connection_made-853"><span class="linenos">853</span></a>            <span class="n">context</span> <span class="o">=</span> <span class="p">{</span>
</span><span id="TcpStreamReaderProtocol.connection_made-854"><a href="#TcpStreamReaderProtocol.connection_made-854"><span class="linenos">854</span></a>                <span class="s1">&#39;message&#39;</span><span class="p">:</span> <span class="p">(</span><span class="s1">&#39;An open stream was garbage collected prior to &#39;</span>
</span><span id="TcpStreamReaderProtocol.connection_made-855"><a href="#TcpStreamReaderProtocol.connection_made-855"><span class="linenos">855</span></a>                            <span class="s1">&#39;establishing network connection; &#39;</span>
</span><span id="TcpStreamReaderProtocol.connection_made-856"><a href="#TcpStreamReaderProtocol.connection_made-856"><span class="linenos">856</span></a>                            <span class="s1">&#39;call &quot;stream.close()&quot; explicitly.&#39;</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-857"><a href="#TcpStreamReaderProtocol.connection_made-857"><span class="linenos">857</span></a>            <span class="p">}</span>
</span><span id="TcpStreamReaderProtocol.connection_made-858"><a href="#TcpStreamReaderProtocol.connection_made-858"><span class="linenos">858</span></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol.connection_made-859"><a href="#TcpStreamReaderProtocol.connection_made-859"><span class="linenos">859</span></a>                <span class="n">context</span><span class="p">[</span><span class="s1">&#39;source_traceback&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_source_traceback</span>
</span><span id="TcpStreamReaderProtocol.connection_made-860"><a href="#TcpStreamReaderProtocol.connection_made-860"><span class="linenos">860</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">call_exception_handler</span><span class="p">(</span><span class="n">context</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-861"><a href="#TcpStreamReaderProtocol.connection_made-861"><span class="linenos">861</span></a>            <span class="n">transport</span><span class="o">.</span><span class="n">abort</span><span class="p">()</span>
</span><span id="TcpStreamReaderProtocol.connection_made-862"><a href="#TcpStreamReaderProtocol.connection_made-862"><span class="linenos">862</span></a>            <span class="k">return</span>
</span><span id="TcpStreamReaderProtocol.connection_made-863"><a href="#TcpStreamReaderProtocol.connection_made-863"><span class="linenos">863</span></a>        
</span><span id="TcpStreamReaderProtocol.connection_made-864"><a href="#TcpStreamReaderProtocol.connection_made-864"><span class="linenos">864</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_transport</span> <span class="o">=</span> <span class="n">transport</span>
</span><span id="TcpStreamReaderProtocol.connection_made-865"><a href="#TcpStreamReaderProtocol.connection_made-865"><span class="linenos">865</span></a>        <span class="n">reader</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_reader</span>
</span><span id="TcpStreamReaderProtocol.connection_made-866"><a href="#TcpStreamReaderProtocol.connection_made-866"><span class="linenos">866</span></a>        <span class="k">if</span> <span class="n">reader</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol.connection_made-867"><a href="#TcpStreamReaderProtocol.connection_made-867"><span class="linenos">867</span></a>            <span class="n">reader</span><span class="o">.</span><span class="n">set_transport</span><span class="p">(</span><span class="n">transport</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-868"><a href="#TcpStreamReaderProtocol.connection_made-868"><span class="linenos">868</span></a>
</span><span id="TcpStreamReaderProtocol.connection_made-869"><a href="#TcpStreamReaderProtocol.connection_made-869"><span class="linenos">869</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_over_ssl</span> <span class="o">=</span> <span class="n">transport</span><span class="o">.</span><span class="n">get_extra_info</span><span class="p">(</span><span class="s1">&#39;sslcontext&#39;</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
</span><span id="TcpStreamReaderProtocol.connection_made-870"><a href="#TcpStreamReaderProtocol.connection_made-870"><span class="linenos">870</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamReaderProtocol.connection_made-871"><a href="#TcpStreamReaderProtocol.connection_made-871"><span class="linenos">871</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span> <span class="o">=</span> <span class="n">TcpStreamWriter</span><span class="p">(</span><span class="n">transport</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol.connection_made-872"><a href="#TcpStreamReaderProtocol.connection_made-872"><span class="linenos">872</span></a>                                               <span class="n">reader</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol.connection_made-873"><a href="#TcpStreamReaderProtocol.connection_made-873"><span class="linenos">873</span></a>                                               <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-874"><a href="#TcpStreamReaderProtocol.connection_made-874"><span class="linenos">874</span></a>            <span class="n">res</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client_connected_cb</span><span class="p">(</span><span class="n">reader</span><span class="p">,</span>
</span><span id="TcpStreamReaderProtocol.connection_made-875"><a href="#TcpStreamReaderProtocol.connection_made-875"><span class="linenos">875</span></a>                                            <span class="bp">self</span><span class="o">.</span><span class="n">_stream_writer</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-876"><a href="#TcpStreamReaderProtocol.connection_made-876"><span class="linenos">876</span></a>            <span class="k">if</span> <span class="n">coroutines</span><span class="o">.</span><span class="n">iscoroutine</span><span class="p">(</span><span class="n">res</span><span class="p">):</span>
</span><span id="TcpStreamReaderProtocol.connection_made-877"><a href="#TcpStreamReaderProtocol.connection_made-877"><span class="linenos">877</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_task</span><span class="p">(</span><span class="n">res</span><span class="p">)</span>
</span><span id="TcpStreamReaderProtocol.connection_made-878"><a href="#TcpStreamReaderProtocol.connection_made-878"><span class="linenos">878</span></a>            
</span><span id="TcpStreamReaderProtocol.connection_made-879"><a href="#TcpStreamReaderProtocol.connection_made-879"><span class="linenos">879</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_strong_reader</span> <span class="o">=</span> <span class="kc">None</span>
</span></pre></div>


            <div class="docstring"><p>Called when a connection is made.</p>

<p>The argument is the transport representing the pipe connection.
To receive data, wait for data_received() calls.
When the connection is closed, connection_lost() is called.</p>
</div>


                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.streams.StreamReaderProtocol</dt>
                                <dd id="TcpStreamReaderProtocol.connection_lost" class="function">connection_lost</dd>
                <dd id="TcpStreamReaderProtocol.data_received" class="function">data_received</dd>
                <dd id="TcpStreamReaderProtocol.eof_received" class="function">eof_received</dd>

            </div>
            <div><dt>asyncio.streams.FlowControlMixin</dt>
                                <dd id="TcpStreamReaderProtocol.pause_writing" class="function">pause_writing</dd>
                <dd id="TcpStreamReaderProtocol.resume_writing" class="function">resume_writing</dd>

            </div>
                                </dl>
                            </div>
                </section>
                <section id="TcpStreamWriter">
                            <input id="TcpStreamWriter-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr class">
            
    <span class="def">class</span>
    <span class="name">TcpStreamWriter</span><wbr>(<span class="base">asyncio.streams.StreamWriter</span>, <span class="base">cengal.parallel_execution.asyncio.efficient_streams.versions.v_0.efficient_streams_abstract.StreamWriterAbstract</span>):

                <label class="view-source-button" for="TcpStreamWriter-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter-1008"><a href="#TcpStreamWriter-1008"><span class="linenos">1008</span></a><span class="k">class</span> <span class="nc">TcpStreamWriter</span><span class="p">(</span><span class="n">OriginalStreamWriter</span><span class="p">,</span> <span class="n">StreamWriterAbstract</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1009"><a href="#TcpStreamWriter-1009"><span class="linenos">1009</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1010"><a href="#TcpStreamWriter-1010"><span class="linenos">1010</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1011"><a href="#TcpStreamWriter-1011"><span class="linenos">1011</span></a>
</span><span id="TcpStreamWriter-1012"><a href="#TcpStreamWriter-1012"><span class="linenos">1012</span></a>    <span class="k">def</span> <span class="nf">_bind_to_stream_manager</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1013"><a href="#TcpStreamWriter-1013"><span class="linenos">1013</span></a>        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1014"><a href="#TcpStreamWriter-1014"><span class="linenos">1014</span></a>
</span><span id="TcpStreamWriter-1015"><a href="#TcpStreamWriter-1015"><span class="linenos">1015</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="p">:</span> <span class="n">TcpStreamManager</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_stream_manager</span>
</span><span id="TcpStreamWriter-1016"><a href="#TcpStreamWriter-1016"><span class="linenos">1016</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="p">:</span> <span class="n">DynamicListOfPiecesDequeWithLengthControl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">output_to_client_container_type</span><span class="p">(</span>
</span><span id="TcpStreamWriter-1017"><a href="#TcpStreamWriter-1017"><span class="linenos">1017</span></a>            <span class="n">external_data_length</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">global_out__data_full_size</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1018"><a href="#TcpStreamWriter-1018"><span class="linenos">1018</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="p">:</span> <span class="n">ValueExistence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">io_memory_management</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span>
</span><span id="TcpStreamWriter-1019"><a href="#TcpStreamWriter-1019"><span class="linenos">1019</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">:</span> <span class="n">Task</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamWriter-1020"><a href="#TcpStreamWriter-1020"><span class="linenos">1020</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamWriter-1021"><a href="#TcpStreamWriter-1021"><span class="linenos">1021</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="p">:</span> <span class="n">List</span><span class="p">[</span><span class="n">Future</span><span class="p">]</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1022"><a href="#TcpStreamWriter-1022"><span class="linenos">1022</span></a>
</span><span id="TcpStreamWriter-1023"><a href="#TcpStreamWriter-1023"><span class="linenos">1023</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1024"><a href="#TcpStreamWriter-1024"><span class="linenos">1024</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1025"><a href="#TcpStreamWriter-1025"><span class="linenos">1025</span></a>        <span class="c1"># self.write(data)</span>
</span><span id="TcpStreamWriter-1026"><a href="#TcpStreamWriter-1026"><span class="linenos">1026</span></a>
</span><span id="TcpStreamWriter-1027"><a href="#TcpStreamWriter-1027"><span class="linenos">1027</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1028"><a href="#TcpStreamWriter-1028"><span class="linenos">1028</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1029"><a href="#TcpStreamWriter-1029"><span class="linenos">1029</span></a>
</span><span id="TcpStreamWriter-1030"><a href="#TcpStreamWriter-1030"><span class="linenos">1030</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1031"><a href="#TcpStreamWriter-1031"><span class="linenos">1031</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1032"><a href="#TcpStreamWriter-1032"><span class="linenos">1032</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1033"><a href="#TcpStreamWriter-1033"><span class="linenos">1033</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1034"><a href="#TcpStreamWriter-1034"><span class="linenos">1034</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1035"><a href="#TcpStreamWriter-1035"><span class="linenos">1035</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1036"><a href="#TcpStreamWriter-1036"><span class="linenos">1036</span></a>
</span><span id="TcpStreamWriter-1037"><a href="#TcpStreamWriter-1037"><span class="linenos">1037</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1038"><a href="#TcpStreamWriter-1038"><span class="linenos">1038</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1039"><a href="#TcpStreamWriter-1039"><span class="linenos">1039</span></a>
</span><span id="TcpStreamWriter-1040"><a href="#TcpStreamWriter-1040"><span class="linenos">1040</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1041"><a href="#TcpStreamWriter-1041"><span class="linenos">1041</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1042"><a href="#TcpStreamWriter-1042"><span class="linenos">1042</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1043"><a href="#TcpStreamWriter-1043"><span class="linenos">1043</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1044"><a href="#TcpStreamWriter-1044"><span class="linenos">1044</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1045"><a href="#TcpStreamWriter-1045"><span class="linenos">1045</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1046"><a href="#TcpStreamWriter-1046"><span class="linenos">1046</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1047"><a href="#TcpStreamWriter-1047"><span class="linenos">1047</span></a>
</span><span id="TcpStreamWriter-1048"><a href="#TcpStreamWriter-1048"><span class="linenos">1048</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1049"><a href="#TcpStreamWriter-1049"><span class="linenos">1049</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1050"><a href="#TcpStreamWriter-1050"><span class="linenos">1050</span></a>    
</span><span id="TcpStreamWriter-1051"><a href="#TcpStreamWriter-1051"><span class="linenos">1051</span></a>    <span class="k">def</span> <span class="nf">_release_autonomous_writer_waiters</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1052"><a href="#TcpStreamWriter-1052"><span class="linenos">1052</span></a>        <span class="n">current_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1053"><a href="#TcpStreamWriter-1053"><span class="linenos">1053</span></a>        <span class="n">autonomous_writer_drain_enough_futures_buff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span>
</span><span id="TcpStreamWriter-1054"><a href="#TcpStreamWriter-1054"><span class="linenos">1054</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span> <span class="o">=</span> <span class="nb">type</span><span class="p">(</span><span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">)()</span>
</span><span id="TcpStreamWriter-1055"><a href="#TcpStreamWriter-1055"><span class="linenos">1055</span></a>        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">autonomous_writer_drain_enough_futures_buff</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1056"><a href="#TcpStreamWriter-1056"><span class="linenos">1056</span></a>            <span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span> <span class="o">=</span> <span class="n">item</span>
</span><span id="TcpStreamWriter-1057"><a href="#TcpStreamWriter-1057"><span class="linenos">1057</span></a>            <span class="k">if</span> <span class="n">current_size</span> <span class="o">&lt;</span> <span class="n">lower_water_size</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1058"><a href="#TcpStreamWriter-1058"><span class="linenos">1058</span></a>                <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="TcpStreamWriter-1059"><a href="#TcpStreamWriter-1059"><span class="linenos">1059</span></a>                    <span class="n">future</span><span class="o">.</span><span class="n">set_result</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1060"><a href="#TcpStreamWriter-1060"><span class="linenos">1060</span></a>
</span><span id="TcpStreamWriter-1061"><a href="#TcpStreamWriter-1061"><span class="linenos">1061</span></a>            <span class="k">if</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">done</span><span class="p">())</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="n">future</span><span class="o">.</span><span class="n">cancelled</span><span class="p">()):</span>
</span><span id="TcpStreamWriter-1062"><a href="#TcpStreamWriter-1062"><span class="linenos">1062</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1063"><a href="#TcpStreamWriter-1063"><span class="linenos">1063</span></a>    
</span><span id="TcpStreamWriter-1064"><a href="#TcpStreamWriter-1064"><span class="linenos">1064</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">_autonomous_writer_impl</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1065"><a href="#TcpStreamWriter-1065"><span class="linenos">1065</span></a>        <span class="n">ty</span> <span class="o">=</span> <span class="n">TimedYield</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1066"><a href="#TcpStreamWriter-1066"><span class="linenos">1066</span></a>        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1067"><a href="#TcpStreamWriter-1067"><span class="linenos">1067</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1068"><a href="#TcpStreamWriter-1068"><span class="linenos">1068</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1069"><a href="#TcpStreamWriter-1069"><span class="linenos">1069</span></a>            <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1070"><a href="#TcpStreamWriter-1070"><span class="linenos">1070</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1071"><a href="#TcpStreamWriter-1071"><span class="linenos">1071</span></a>                <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1072"><a href="#TcpStreamWriter-1072"><span class="linenos">1072</span></a>                <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1073"><a href="#TcpStreamWriter-1073"><span class="linenos">1073</span></a>                <span class="bp">self</span><span class="o">.</span><span class="n">_release_autonomous_writer_waiters</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1074"><a href="#TcpStreamWriter-1074"><span class="linenos">1074</span></a>            
</span><span id="TcpStreamWriter-1075"><a href="#TcpStreamWriter-1075"><span class="linenos">1075</span></a>            <span class="k">await</span> <span class="n">ty</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1076"><a href="#TcpStreamWriter-1076"><span class="linenos">1076</span></a>    
</span><span id="TcpStreamWriter-1077"><a href="#TcpStreamWriter-1077"><span class="linenos">1077</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1078"><a href="#TcpStreamWriter-1078"><span class="linenos">1078</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1079"><a href="#TcpStreamWriter-1079"><span class="linenos">1079</span></a>    
</span><span id="TcpStreamWriter-1080"><a href="#TcpStreamWriter-1080"><span class="linenos">1080</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1081"><a href="#TcpStreamWriter-1081"><span class="linenos">1081</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1082"><a href="#TcpStreamWriter-1082"><span class="linenos">1082</span></a>    
</span><span id="TcpStreamWriter-1083"><a href="#TcpStreamWriter-1083"><span class="linenos">1083</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1084"><a href="#TcpStreamWriter-1084"><span class="linenos">1084</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="TcpStreamWriter-1085"><a href="#TcpStreamWriter-1085"><span class="linenos">1085</span></a>
</span><span id="TcpStreamWriter-1086"><a href="#TcpStreamWriter-1086"><span class="linenos">1086</span></a><span class="sd">        Args:</span>
</span><span id="TcpStreamWriter-1087"><a href="#TcpStreamWriter-1087"><span class="linenos">1087</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="TcpStreamWriter-1088"><a href="#TcpStreamWriter-1088"><span class="linenos">1088</span></a>
</span><span id="TcpStreamWriter-1089"><a href="#TcpStreamWriter-1089"><span class="linenos">1089</span></a><span class="sd">        Returns:</span>
</span><span id="TcpStreamWriter-1090"><a href="#TcpStreamWriter-1090"><span class="linenos">1090</span></a><span class="sd">            _type_: _description_</span>
</span><span id="TcpStreamWriter-1091"><a href="#TcpStreamWriter-1091"><span class="linenos">1091</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamWriter-1092"><a href="#TcpStreamWriter-1092"><span class="linenos">1092</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamWriter-1093"><a href="#TcpStreamWriter-1093"><span class="linenos">1093</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1094"><a href="#TcpStreamWriter-1094"><span class="linenos">1094</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="TcpStreamWriter-1095"><a href="#TcpStreamWriter-1095"><span class="linenos">1095</span></a>        
</span><span id="TcpStreamWriter-1096"><a href="#TcpStreamWriter-1096"><span class="linenos">1096</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1097"><a href="#TcpStreamWriter-1097"><span class="linenos">1097</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamWriter-1098"><a href="#TcpStreamWriter-1098"><span class="linenos">1098</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1099"><a href="#TcpStreamWriter-1099"><span class="linenos">1099</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1100"><a href="#TcpStreamWriter-1100"><span class="linenos">1100</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1101"><a href="#TcpStreamWriter-1101"><span class="linenos">1101</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="TcpStreamWriter-1102"><a href="#TcpStreamWriter-1102"><span class="linenos">1102</span></a>            
</span><span id="TcpStreamWriter-1103"><a href="#TcpStreamWriter-1103"><span class="linenos">1103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamWriter-1104"><a href="#TcpStreamWriter-1104"><span class="linenos">1104</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamWriter-1105"><a href="#TcpStreamWriter-1105"><span class="linenos">1105</span></a>        
</span><span id="TcpStreamWriter-1106"><a href="#TcpStreamWriter-1106"><span class="linenos">1106</span></a>        <span class="k">return</span> <span class="n">result</span>
</span><span id="TcpStreamWriter-1107"><a href="#TcpStreamWriter-1107"><span class="linenos">1107</span></a>    
</span><span id="TcpStreamWriter-1108"><a href="#TcpStreamWriter-1108"><span class="linenos">1108</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1109"><a href="#TcpStreamWriter-1109"><span class="linenos">1109</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="TcpStreamWriter-1110"><a href="#TcpStreamWriter-1110"><span class="linenos">1110</span></a>
</span><span id="TcpStreamWriter-1111"><a href="#TcpStreamWriter-1111"><span class="linenos">1111</span></a><span class="sd">        Args:</span>
</span><span id="TcpStreamWriter-1112"><a href="#TcpStreamWriter-1112"><span class="linenos">1112</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="TcpStreamWriter-1113"><a href="#TcpStreamWriter-1113"><span class="linenos">1113</span></a>
</span><span id="TcpStreamWriter-1114"><a href="#TcpStreamWriter-1114"><span class="linenos">1114</span></a><span class="sd">        Returns:</span>
</span><span id="TcpStreamWriter-1115"><a href="#TcpStreamWriter-1115"><span class="linenos">1115</span></a><span class="sd">            _type_: _description_</span>
</span><span id="TcpStreamWriter-1116"><a href="#TcpStreamWriter-1116"><span class="linenos">1116</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamWriter-1117"><a href="#TcpStreamWriter-1117"><span class="linenos">1117</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1118"><a href="#TcpStreamWriter-1118"><span class="linenos">1118</span></a>    
</span><span id="TcpStreamWriter-1119"><a href="#TcpStreamWriter-1119"><span class="linenos">1119</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1120"><a href="#TcpStreamWriter-1120"><span class="linenos">1120</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1121"><a href="#TcpStreamWriter-1121"><span class="linenos">1121</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="TcpStreamWriter-1122"><a href="#TcpStreamWriter-1122"><span class="linenos">1122</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="TcpStreamWriter-1123"><a href="#TcpStreamWriter-1123"><span class="linenos">1123</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="TcpStreamWriter-1124"><a href="#TcpStreamWriter-1124"><span class="linenos">1124</span></a>        
</span><span id="TcpStreamWriter-1125"><a href="#TcpStreamWriter-1125"><span class="linenos">1125</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="TcpStreamWriter-1126"><a href="#TcpStreamWriter-1126"><span class="linenos">1126</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1127"><a href="#TcpStreamWriter-1127"><span class="linenos">1127</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="TcpStreamWriter-1128"><a href="#TcpStreamWriter-1128"><span class="linenos">1128</span></a>            <span class="k">await</span> <span class="n">future</span>
</span><span id="TcpStreamWriter-1129"><a href="#TcpStreamWriter-1129"><span class="linenos">1129</span></a>    
</span><span id="TcpStreamWriter-1130"><a href="#TcpStreamWriter-1130"><span class="linenos">1130</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1131"><a href="#TcpStreamWriter-1131"><span class="linenos">1131</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1132"><a href="#TcpStreamWriter-1132"><span class="linenos">1132</span></a>    
</span><span id="TcpStreamWriter-1133"><a href="#TcpStreamWriter-1133"><span class="linenos">1133</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1134"><a href="#TcpStreamWriter-1134"><span class="linenos">1134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1135"><a href="#TcpStreamWriter-1135"><span class="linenos">1135</span></a>    
</span><span id="TcpStreamWriter-1136"><a href="#TcpStreamWriter-1136"><span class="linenos">1136</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1137"><a href="#TcpStreamWriter-1137"><span class="linenos">1137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1138"><a href="#TcpStreamWriter-1138"><span class="linenos">1138</span></a>    
</span><span id="TcpStreamWriter-1139"><a href="#TcpStreamWriter-1139"><span class="linenos">1139</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1140"><a href="#TcpStreamWriter-1140"><span class="linenos">1140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter-1141"><a href="#TcpStreamWriter-1141"><span class="linenos">1141</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1142"><a href="#TcpStreamWriter-1142"><span class="linenos">1142</span></a>    
</span><span id="TcpStreamWriter-1143"><a href="#TcpStreamWriter-1143"><span class="linenos">1143</span></a>    <span class="nd">@asynccontextmanager</span>
</span><span id="TcpStreamWriter-1144"><a href="#TcpStreamWriter-1144"><span class="linenos">1144</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1145"><a href="#TcpStreamWriter-1145"><span class="linenos">1145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1146"><a href="#TcpStreamWriter-1146"><span class="linenos">1146</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1147"><a href="#TcpStreamWriter-1147"><span class="linenos">1147</span></a>            <span class="k">yield</span>
</span><span id="TcpStreamWriter-1148"><a href="#TcpStreamWriter-1148"><span class="linenos">1148</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="TcpStreamWriter-1149"><a href="#TcpStreamWriter-1149"><span class="linenos">1149</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">()</span>
</span><span id="TcpStreamWriter-1150"><a href="#TcpStreamWriter-1150"><span class="linenos">1150</span></a>    
</span><span id="TcpStreamWriter-1151"><a href="#TcpStreamWriter-1151"><span class="linenos">1151</span></a>    <span class="n">aw</span> <span class="o">=</span> <span class="n">autonomous_writer</span>
</span><span id="TcpStreamWriter-1152"><a href="#TcpStreamWriter-1152"><span class="linenos">1152</span></a>
</span><span id="TcpStreamWriter-1153"><a href="#TcpStreamWriter-1153"><span class="linenos">1153</span></a>    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1154"><a href="#TcpStreamWriter-1154"><span class="linenos">1154</span></a>        <span class="k">pass</span>
</span><span id="TcpStreamWriter-1155"><a href="#TcpStreamWriter-1155"><span class="linenos">1155</span></a>
</span><span id="TcpStreamWriter-1156"><a href="#TcpStreamWriter-1156"><span class="linenos">1156</span></a>    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc</span><span class="p">,</span> <span class="n">tb</span><span class="p">):</span>
</span><span id="TcpStreamWriter-1157"><a href="#TcpStreamWriter-1157"><span class="linenos">1157</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</span></pre></div>


            <div class="docstring"><p>Wraps a Transport.</p>

<p>This exposes write(), writelines(), [can_]write_eof(),
get_extra_info() and close().  It adds drain() which returns an
optional Future on which you can wait for flow control.  It also
adds a transport property which references the Transport
directly.</p>
</div>


                            <div id="TcpStreamWriter.__init__" class="classattr">
                                        <input id="TcpStreamWriter.__init__-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="name">TcpStreamWriter</span><span class="signature pdoc-code condensed">(<span class="param"><span class="o">*</span><span class="n">args</span>, </span><span class="param"><span class="o">**</span><span class="n">kwargs</span></span>)</span>

                <label class="view-source-button" for="TcpStreamWriter.__init__-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.__init__"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.__init__-1009"><a href="#TcpStreamWriter.__init__-1009"><span class="linenos">1009</span></a>    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter.__init__-1010"><a href="#TcpStreamWriter.__init__-1010"><span class="linenos">1010</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_bind_to_stream_manager</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.optimized_write" class="classattr">
                                        <input id="TcpStreamWriter.optimized_write-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">optimized_write</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.optimized_write-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.optimized_write"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.optimized_write-1023"><a href="#TcpStreamWriter.optimized_write-1023"><span class="linenos">1023</span></a>    <span class="k">def</span> <span class="nf">optimized_write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter.optimized_write-1024"><a href="#TcpStreamWriter.optimized_write-1024"><span class="linenos">1024</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">add_piece_of_data</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter.optimized_write-1025"><a href="#TcpStreamWriter.optimized_write-1025"><span class="linenos">1025</span></a>        <span class="c1"># self.write(data)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.owrite" class="classattr">
                                        <input id="TcpStreamWriter.owrite-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">owrite</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.owrite-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.owrite"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.owrite-1027"><a href="#TcpStreamWriter.owrite-1027"><span class="linenos">1027</span></a>    <span class="k">def</span> <span class="nf">owrite</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter.owrite-1028"><a href="#TcpStreamWriter.owrite-1028"><span class="linenos">1028</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.partial_drain" class="classattr">
                                        <input id="TcpStreamWriter.partial_drain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">partial_drain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.partial_drain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.partial_drain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.partial_drain-1030"><a href="#TcpStreamWriter.partial_drain-1030"><span class="linenos">1030</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">partial_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.partial_drain-1031"><a href="#TcpStreamWriter.partial_drain-1031"><span class="linenos">1031</span></a>        <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span><span id="TcpStreamWriter.partial_drain-1032"><a href="#TcpStreamWriter.partial_drain-1032"><span class="linenos">1032</span></a>        <span class="k">while</span> <span class="n">another_piece_of_data</span><span class="p">:</span>
</span><span id="TcpStreamWriter.partial_drain-1033"><a href="#TcpStreamWriter.partial_drain-1033"><span class="linenos">1033</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="TcpStreamWriter.partial_drain-1034"><a href="#TcpStreamWriter.partial_drain-1034"><span class="linenos">1034</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span><span id="TcpStreamWriter.partial_drain-1035"><a href="#TcpStreamWriter.partial_drain-1035"><span class="linenos">1035</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.pdrain" class="classattr">
                                        <input id="TcpStreamWriter.pdrain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">pdrain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.pdrain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.pdrain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.pdrain-1037"><a href="#TcpStreamWriter.pdrain-1037"><span class="linenos">1037</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">pdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.pdrain-1038"><a href="#TcpStreamWriter.pdrain-1038"><span class="linenos">1038</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">partial_drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.full_drain" class="classattr">
                                        <input id="TcpStreamWriter.full_drain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">full_drain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.full_drain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.full_drain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.full_drain-1040"><a href="#TcpStreamWriter.full_drain-1040"><span class="linenos">1040</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">full_drain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.full_drain-1041"><a href="#TcpStreamWriter.full_drain-1041"><span class="linenos">1041</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">pdrain</span><span class="p">()</span>
</span><span id="TcpStreamWriter.full_drain-1042"><a href="#TcpStreamWriter.full_drain-1042"><span class="linenos">1042</span></a>        <span class="n">rest_of_the_data_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">()</span>
</span><span id="TcpStreamWriter.full_drain-1043"><a href="#TcpStreamWriter.full_drain-1043"><span class="linenos">1043</span></a>        <span class="k">if</span> <span class="n">rest_of_the_data_size</span><span class="p">:</span>
</span><span id="TcpStreamWriter.full_drain-1044"><a href="#TcpStreamWriter.full_drain-1044"><span class="linenos">1044</span></a>            <span class="n">another_piece_of_data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">get_data</span><span class="p">(</span><span class="n">rest_of_the_data_size</span><span class="p">)</span>
</span><span id="TcpStreamWriter.full_drain-1045"><a href="#TcpStreamWriter.full_drain-1045"><span class="linenos">1045</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">another_piece_of_data</span><span class="p">)</span>
</span><span id="TcpStreamWriter.full_drain-1046"><a href="#TcpStreamWriter.full_drain-1046"><span class="linenos">1046</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.fdrain" class="classattr">
                                        <input id="TcpStreamWriter.fdrain-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">fdrain</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.fdrain-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.fdrain"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.fdrain-1048"><a href="#TcpStreamWriter.fdrain-1048"><span class="linenos">1048</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">fdrain</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.fdrain-1049"><a href="#TcpStreamWriter.fdrain-1049"><span class="linenos">1049</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">full_drain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.start_autonomous_writer" class="classattr">
                                        <input id="TcpStreamWriter.start_autonomous_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_autonomous_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.start_autonomous_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.start_autonomous_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.start_autonomous_writer-1077"><a href="#TcpStreamWriter.start_autonomous_writer-1077"><span class="linenos">1077</span></a>    <span class="k">def</span> <span class="nf">start_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.start_autonomous_writer-1078"><a href="#TcpStreamWriter.start_autonomous_writer-1078"><span class="linenos">1078</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="n">create_task</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_impl</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.start_aw" class="classattr">
                                        <input id="TcpStreamWriter.start_aw-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">start_aw</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.start_aw-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.start_aw"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.start_aw-1080"><a href="#TcpStreamWriter.start_aw-1080"><span class="linenos">1080</span></a>    <span class="k">def</span> <span class="nf">start_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.start_aw-1081"><a href="#TcpStreamWriter.start_aw-1081"><span class="linenos">1081</span></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.stop_autonomous_writer" class="classattr">
                                        <input id="TcpStreamWriter.stop_autonomous_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">stop_autonomous_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.stop_autonomous_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.stop_autonomous_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.stop_autonomous_writer-1083"><a href="#TcpStreamWriter.stop_autonomous_writer-1083"><span class="linenos">1083</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1084"><a href="#TcpStreamWriter.stop_autonomous_writer-1084"><span class="linenos">1084</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1085"><a href="#TcpStreamWriter.stop_autonomous_writer-1085"><span class="linenos">1085</span></a>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1086"><a href="#TcpStreamWriter.stop_autonomous_writer-1086"><span class="linenos">1086</span></a><span class="sd">        Args:</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1087"><a href="#TcpStreamWriter.stop_autonomous_writer-1087"><span class="linenos">1087</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1088"><a href="#TcpStreamWriter.stop_autonomous_writer-1088"><span class="linenos">1088</span></a>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1089"><a href="#TcpStreamWriter.stop_autonomous_writer-1089"><span class="linenos">1089</span></a><span class="sd">        Returns:</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1090"><a href="#TcpStreamWriter.stop_autonomous_writer-1090"><span class="linenos">1090</span></a><span class="sd">            _type_: _description_</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1091"><a href="#TcpStreamWriter.stop_autonomous_writer-1091"><span class="linenos">1091</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1092"><a href="#TcpStreamWriter.stop_autonomous_writer-1092"><span class="linenos">1092</span></a>        <span class="n">result</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1093"><a href="#TcpStreamWriter.stop_autonomous_writer-1093"><span class="linenos">1093</span></a>        <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1094"><a href="#TcpStreamWriter.stop_autonomous_writer-1094"><span class="linenos">1094</span></a>            <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_stream_manager</span><span class="o">.</span><span class="n">autonomous_writer_stop_default_timeout</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1095"><a href="#TcpStreamWriter.stop_autonomous_writer-1095"><span class="linenos">1095</span></a>        
</span><span id="TcpStreamWriter.stop_autonomous_writer-1096"><a href="#TcpStreamWriter.stop_autonomous_writer-1096"><span class="linenos">1096</span></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="ow">and</span> <span class="p">(</span><span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span><span class="p">):</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1097"><a href="#TcpStreamWriter.stop_autonomous_writer-1097"><span class="linenos">1097</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">True</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1098"><a href="#TcpStreamWriter.stop_autonomous_writer-1098"><span class="linenos">1098</span></a>            <span class="k">if</span> <span class="n">timeout</span><span class="p">:</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1099"><a href="#TcpStreamWriter.stop_autonomous_writer-1099"><span class="linenos">1099</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">wait_for</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span><span class="p">,</span> <span class="n">timeout</span><span class="p">)</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1100"><a href="#TcpStreamWriter.stop_autonomous_writer-1100"><span class="linenos">1100</span></a>            <span class="k">else</span><span class="p">:</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1101"><a href="#TcpStreamWriter.stop_autonomous_writer-1101"><span class="linenos">1101</span></a>                <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1102"><a href="#TcpStreamWriter.stop_autonomous_writer-1102"><span class="linenos">1102</span></a>            
</span><span id="TcpStreamWriter.stop_autonomous_writer-1103"><a href="#TcpStreamWriter.stop_autonomous_writer-1103"><span class="linenos">1103</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future</span> <span class="o">=</span> <span class="kc">None</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1104"><a href="#TcpStreamWriter.stop_autonomous_writer-1104"><span class="linenos">1104</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_future_stop_requessted</span> <span class="o">=</span> <span class="kc">False</span>
</span><span id="TcpStreamWriter.stop_autonomous_writer-1105"><a href="#TcpStreamWriter.stop_autonomous_writer-1105"><span class="linenos">1105</span></a>        
</span><span id="TcpStreamWriter.stop_autonomous_writer-1106"><a href="#TcpStreamWriter.stop_autonomous_writer-1106"><span class="linenos">1106</span></a>        <span class="k">return</span> <span class="n">result</span>
</span></pre></div>


            <div class="docstring"><p>_summary_</p>

<p>Args:
    timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="TcpStreamWriter.stop_aw" class="classattr">
                                        <input id="TcpStreamWriter.stop_aw-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">stop_aw</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.stop_aw-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.stop_aw"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.stop_aw-1108"><a href="#TcpStreamWriter.stop_aw-1108"><span class="linenos">1108</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">stop_aw</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">]]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
</span><span id="TcpStreamWriter.stop_aw-1109"><a href="#TcpStreamWriter.stop_aw-1109"><span class="linenos">1109</span></a><span class="w">        </span><span class="sd">&quot;&quot;&quot;_summary_</span>
</span><span id="TcpStreamWriter.stop_aw-1110"><a href="#TcpStreamWriter.stop_aw-1110"><span class="linenos">1110</span></a>
</span><span id="TcpStreamWriter.stop_aw-1111"><a href="#TcpStreamWriter.stop_aw-1111"><span class="linenos">1111</span></a><span class="sd">        Args:</span>
</span><span id="TcpStreamWriter.stop_aw-1112"><a href="#TcpStreamWriter.stop_aw-1112"><span class="linenos">1112</span></a><span class="sd">            timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</span>
</span><span id="TcpStreamWriter.stop_aw-1113"><a href="#TcpStreamWriter.stop_aw-1113"><span class="linenos">1113</span></a>
</span><span id="TcpStreamWriter.stop_aw-1114"><a href="#TcpStreamWriter.stop_aw-1114"><span class="linenos">1114</span></a><span class="sd">        Returns:</span>
</span><span id="TcpStreamWriter.stop_aw-1115"><a href="#TcpStreamWriter.stop_aw-1115"><span class="linenos">1115</span></a><span class="sd">            _type_: _description_</span>
</span><span id="TcpStreamWriter.stop_aw-1116"><a href="#TcpStreamWriter.stop_aw-1116"><span class="linenos">1116</span></a><span class="sd">        &quot;&quot;&quot;</span>
</span><span id="TcpStreamWriter.stop_aw-1117"><a href="#TcpStreamWriter.stop_aw-1117"><span class="linenos">1117</span></a>        <span class="k">return</span> <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
</span></pre></div>


            <div class="docstring"><p>_summary_</p>

<p>Args:
    timeout (Optional[Union[int, float]], optional): _description_. Defaults to 0. 0 - infinit timeout; None - default timeout</p>

<p>Returns:
    _type_: _description_</p>
</div>


                            </div>
                            <div id="TcpStreamWriter.autonomous_writer_drain_enough" class="classattr">
                                        <input id="TcpStreamWriter.autonomous_writer_drain_enough-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">autonomous_writer_drain_enough</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Union</span><span class="p">[</span><span class="nb">int</span><span class="p">,</span> <span class="n">NoneType</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.autonomous_writer_drain_enough-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.autonomous_writer_drain_enough"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1119"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1119"><span class="linenos">1119</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">lower_water_size</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1120"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1120"><span class="linenos">1120</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1121"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1121"><span class="linenos">1121</span></a>            <span class="n">lower_water_size</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket_write_fixed_buffer_size</span><span class="o">.</span><span class="n">value</span> <span class="o">*</span> <span class="mi">3</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1122"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1122"><span class="linenos">1122</span></a>            <span class="c1"># print(f&#39;lower_water_size: {lower_water_size}&#39;)</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1123"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1123"><span class="linenos">1123</span></a>            <span class="c1"># lower_water_size = cpu_info().l3_cache_size</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1124"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1124"><span class="linenos">1124</span></a>        
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1125"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1125"><span class="linenos">1125</span></a>        <span class="k">if</span> <span class="n">lower_water_size</span> <span class="o">&lt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_output_to_client</span><span class="o">.</span><span class="n">size</span><span class="p">():</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1126"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1126"><span class="linenos">1126</span></a>            <span class="n">future</span><span class="p">:</span> <span class="n">Future</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_loop</span><span class="o">.</span><span class="n">create_future</span><span class="p">()</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1127"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1127"><span class="linenos">1127</span></a>            <span class="bp">self</span><span class="o">.</span><span class="n">_autonomous_writer_drain_enough_futures</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">lower_water_size</span><span class="p">,</span> <span class="n">future</span><span class="p">))</span>
</span><span id="TcpStreamWriter.autonomous_writer_drain_enough-1128"><a href="#TcpStreamWriter.autonomous_writer_drain_enough-1128"><span class="linenos">1128</span></a>            <span class="k">await</span> <span class="n">future</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.aw_drain_enough" class="classattr">
                                        <input id="TcpStreamWriter.aw_drain_enough-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">aw_drain_enough</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.aw_drain_enough-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.aw_drain_enough"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.aw_drain_enough-1130"><a href="#TcpStreamWriter.aw_drain_enough-1130"><span class="linenos">1130</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">aw_drain_enough</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.aw_drain_enough-1131"><a href="#TcpStreamWriter.aw_drain_enough-1131"><span class="linenos">1131</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">autonomous_writer_drain_enough</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.optimized_write_message" class="classattr">
                                        <input id="TcpStreamWriter.optimized_write_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">optimized_write_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.optimized_write_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.optimized_write_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.optimized_write_message-1133"><a href="#TcpStreamWriter.optimized_write_message-1133"><span class="linenos">1133</span></a>    <span class="k">def</span> <span class="nf">optimized_write_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter.optimized_write_message-1134"><a href="#TcpStreamWriter.optimized_write_message-1134"><span class="linenos">1134</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_protocol</span><span class="o">.</span><span class="n">_message_protocol_settings</span><span class="o">.</span><span class="n">message_size_len</span><span class="p">,</span> <span class="s1">&#39;little&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.owrite_message" class="classattr">
                                        <input id="TcpStreamWriter.owrite_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">def</span>
        <span class="name">owrite_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.owrite_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.owrite_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.owrite_message-1136"><a href="#TcpStreamWriter.owrite_message-1136"><span class="linenos">1136</span></a>    <span class="k">def</span> <span class="nf">owrite_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter.owrite_message-1137"><a href="#TcpStreamWriter.owrite_message-1137"><span class="linenos">1137</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.send_message" class="classattr">
                                        <input id="TcpStreamWriter.send_message-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
            
        <span class="def">async def</span>
        <span class="name">send_message</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span>, </span><span class="param"><span class="n">data</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.send_message-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.send_message"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.send_message-1139"><a href="#TcpStreamWriter.send_message-1139"><span class="linenos">1139</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">):</span>
</span><span id="TcpStreamWriter.send_message-1140"><a href="#TcpStreamWriter.send_message-1140"><span class="linenos">1140</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">optimized_write_message</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
</span><span id="TcpStreamWriter.send_message-1141"><a href="#TcpStreamWriter.send_message-1141"><span class="linenos">1141</span></a>        <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">fdrain</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.autonomous_writer" class="classattr">
                                        <input id="TcpStreamWriter.autonomous_writer-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@asynccontextmanager</div>

        <span class="def">async def</span>
        <span class="name">autonomous_writer</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.autonomous_writer-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.autonomous_writer"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.autonomous_writer-1143"><a href="#TcpStreamWriter.autonomous_writer-1143"><span class="linenos">1143</span></a>    <span class="nd">@asynccontextmanager</span>
</span><span id="TcpStreamWriter.autonomous_writer-1144"><a href="#TcpStreamWriter.autonomous_writer-1144"><span class="linenos">1144</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.autonomous_writer-1145"><a href="#TcpStreamWriter.autonomous_writer-1145"><span class="linenos">1145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="TcpStreamWriter.autonomous_writer-1146"><a href="#TcpStreamWriter.autonomous_writer-1146"><span class="linenos">1146</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamWriter.autonomous_writer-1147"><a href="#TcpStreamWriter.autonomous_writer-1147"><span class="linenos">1147</span></a>            <span class="k">yield</span>
</span><span id="TcpStreamWriter.autonomous_writer-1148"><a href="#TcpStreamWriter.autonomous_writer-1148"><span class="linenos">1148</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="TcpStreamWriter.autonomous_writer-1149"><a href="#TcpStreamWriter.autonomous_writer-1149"><span class="linenos">1149</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div id="TcpStreamWriter.aw" class="classattr">
                                        <input id="TcpStreamWriter.aw-view-source" class="view-source-toggle-state" type="checkbox" aria-hidden="true" tabindex="-1">
<div class="attr function">
                    <div class="decorator">@asynccontextmanager</div>

        <span class="def">async def</span>
        <span class="name">aw</span><span class="signature pdoc-code condensed">(<span class="param"><span class="bp">self</span></span><span class="return-annotation">):</span></span>

                <label class="view-source-button" for="TcpStreamWriter.aw-view-source"><span>View Source</span></label>

    </div>
    <a class="headerlink" href="#TcpStreamWriter.aw"></a>
            <div class="pdoc-code codehilite"><pre><span></span><span id="TcpStreamWriter.aw-1143"><a href="#TcpStreamWriter.aw-1143"><span class="linenos">1143</span></a>    <span class="nd">@asynccontextmanager</span>
</span><span id="TcpStreamWriter.aw-1144"><a href="#TcpStreamWriter.aw-1144"><span class="linenos">1144</span></a>    <span class="k">async</span> <span class="k">def</span> <span class="nf">autonomous_writer</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
</span><span id="TcpStreamWriter.aw-1145"><a href="#TcpStreamWriter.aw-1145"><span class="linenos">1145</span></a>        <span class="bp">self</span><span class="o">.</span><span class="n">start_autonomous_writer</span><span class="p">()</span>
</span><span id="TcpStreamWriter.aw-1146"><a href="#TcpStreamWriter.aw-1146"><span class="linenos">1146</span></a>        <span class="k">try</span><span class="p">:</span>
</span><span id="TcpStreamWriter.aw-1147"><a href="#TcpStreamWriter.aw-1147"><span class="linenos">1147</span></a>            <span class="k">yield</span>
</span><span id="TcpStreamWriter.aw-1148"><a href="#TcpStreamWriter.aw-1148"><span class="linenos">1148</span></a>        <span class="k">finally</span><span class="p">:</span>
</span><span id="TcpStreamWriter.aw-1149"><a href="#TcpStreamWriter.aw-1149"><span class="linenos">1149</span></a>            <span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="n">stop_autonomous_writer</span><span class="p">()</span>
</span></pre></div>


    

                            </div>
                            <div class="inherited">
                                <h5>Inherited Members</h5>
                                <dl>
                                    <div><dt>asyncio.streams.StreamWriter</dt>
                                <dd id="TcpStreamWriter.transport" class="variable">transport</dd>
                <dd id="TcpStreamWriter.write" class="function">write</dd>
                <dd id="TcpStreamWriter.writelines" class="function">writelines</dd>
                <dd id="TcpStreamWriter.write_eof" class="function">write_eof</dd>
                <dd id="TcpStreamWriter.can_write_eof" class="function">can_write_eof</dd>
                <dd id="TcpStreamWriter.close" class="function">close</dd>
                <dd id="TcpStreamWriter.is_closing" class="function">is_closing</dd>
                <dd id="TcpStreamWriter.wait_closed" class="function">wait_closed</dd>
                <dd id="TcpStreamWriter.get_extra_info" class="function">get_extra_info</dd>
                <dd id="TcpStreamWriter.drain" class="function">drain</dd>

            </div>
                                </dl>
                            </div>
                </section>
    </main>


<style>pre{line-height:125%;}span.linenos{color:inherit; background-color:transparent; padding-left:5px; padding-right:20px;}.pdoc-code .hll{background-color:#ffffcc}.pdoc-code{background:#f8f8f8;}.pdoc-code .c{color:#3D7B7B; font-style:italic}.pdoc-code .err{border:1px solid #FF0000}.pdoc-code .k{color:#008000; font-weight:bold}.pdoc-code .o{color:#666666}.pdoc-code .ch{color:#3D7B7B; font-style:italic}.pdoc-code .cm{color:#3D7B7B; font-style:italic}.pdoc-code .cp{color:#9C6500}.pdoc-code .cpf{color:#3D7B7B; font-style:italic}.pdoc-code .c1{color:#3D7B7B; font-style:italic}.pdoc-code .cs{color:#3D7B7B; font-style:italic}.pdoc-code .gd{color:#A00000}.pdoc-code .ge{font-style:italic}.pdoc-code .gr{color:#E40000}.pdoc-code .gh{color:#000080; font-weight:bold}.pdoc-code .gi{color:#008400}.pdoc-code .go{color:#717171}.pdoc-code .gp{color:#000080; font-weight:bold}.pdoc-code .gs{font-weight:bold}.pdoc-code .gu{color:#800080; font-weight:bold}.pdoc-code .gt{color:#0044DD}.pdoc-code .kc{color:#008000; font-weight:bold}.pdoc-code .kd{color:#008000; font-weight:bold}.pdoc-code .kn{color:#008000; font-weight:bold}.pdoc-code .kp{color:#008000}.pdoc-code .kr{color:#008000; font-weight:bold}.pdoc-code .kt{color:#B00040}.pdoc-code .m{color:#666666}.pdoc-code .s{color:#BA2121}.pdoc-code .na{color:#687822}.pdoc-code .nb{color:#008000}.pdoc-code .nc{color:#0000FF; font-weight:bold}.pdoc-code .no{color:#880000}.pdoc-code .nd{color:#AA22FF}.pdoc-code .ni{color:#717171; font-weight:bold}.pdoc-code .ne{color:#CB3F38; font-weight:bold}.pdoc-code .nf{color:#0000FF}.pdoc-code .nl{color:#767600}.pdoc-code .nn{color:#0000FF; font-weight:bold}.pdoc-code .nt{color:#008000; font-weight:bold}.pdoc-code .nv{color:#19177C}.pdoc-code .ow{color:#AA22FF; font-weight:bold}.pdoc-code .w{color:#bbbbbb}.pdoc-code .mb{color:#666666}.pdoc-code .mf{color:#666666}.pdoc-code .mh{color:#666666}.pdoc-code .mi{color:#666666}.pdoc-code .mo{color:#666666}.pdoc-code .sa{color:#BA2121}.pdoc-code .sb{color:#BA2121}.pdoc-code .sc{color:#BA2121}.pdoc-code .dl{color:#BA2121}.pdoc-code .sd{color:#BA2121; font-style:italic}.pdoc-code .s2{color:#BA2121}.pdoc-code .se{color:#AA5D1F; font-weight:bold}.pdoc-code .sh{color:#BA2121}.pdoc-code .si{color:#A45A77; font-weight:bold}.pdoc-code .sx{color:#008000}.pdoc-code .sr{color:#A45A77}.pdoc-code .s1{color:#BA2121}.pdoc-code .ss{color:#19177C}.pdoc-code .bp{color:#008000}.pdoc-code .fm{color:#0000FF}.pdoc-code .vc{color:#19177C}.pdoc-code .vg{color:#19177C}.pdoc-code .vi{color:#19177C}.pdoc-code .vm{color:#19177C}.pdoc-code .il{color:#666666}</style>
<style>:root{--pdoc-background:#fff;}.pdoc{--text:#212529;--muted:#6c757d;--link:#3660a5;--link-hover:#1659c5;--code:#f8f8f8;--active:#fff598;--accent:#eee;--accent2:#c1c1c1;--nav-hover:rgba(255, 255, 255, 0.5);--name:#0066BB;--def:#008800;--annotation:#007020;}</style>
<style>.pdoc{color:var(--text);box-sizing:border-box;line-height:1.5;background:none;}.pdoc .pdoc-button{cursor:pointer;display:inline-block;border:solid black 1px;border-radius:2px;font-size:.75rem;padding:calc(0.5em - 1px) 1em;transition:100ms all;}.pdoc .pdoc-alert{padding:1rem 1rem 1rem calc(1.5rem + 24px);border:1px solid transparent;border-radius:.25rem;background-repeat:no-repeat;background-position:1rem center;margin-bottom:1rem;}.pdoc .pdoc-alert > *:last-child{margin-bottom:0;}.pdoc .pdoc-alert-note {color:#084298;background-color:#cfe2ff;border-color:#b6d4fe;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23084298%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8%2016A8%208%200%201%200%208%200a8%208%200%200%200%200%2016zm.93-9.412-1%204.705c-.07.34.029.533.304.533.194%200%20.487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703%200-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381%202.29-.287zM8%205.5a1%201%200%201%201%200-2%201%201%200%200%201%200%202z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-warning{color:#664d03;background-color:#fff3cd;border-color:#ffecb5;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23664d03%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M8.982%201.566a1.13%201.13%200%200%200-1.96%200L.165%2013.233c-.457.778.091%201.767.98%201.767h13.713c.889%200%201.438-.99.98-1.767L8.982%201.566zM8%205c.535%200%20.954.462.9.995l-.35%203.507a.552.552%200%200%201-1.1%200L7.1%205.995A.905.905%200%200%201%208%205zm.002%206a1%201%200%201%201%200%202%201%201%200%200%201%200-2z%22/%3E%3C/svg%3E");}.pdoc .pdoc-alert-danger{color:#842029;background-color:#f8d7da;border-color:#f5c2c7;background-image:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2224%22%20height%3D%2224%22%20fill%3D%22%23842029%22%20viewBox%3D%220%200%2016%2016%22%3E%3Cpath%20d%3D%22M5.52.359A.5.5%200%200%201%206%200h4a.5.5%200%200%201%20.474.658L8.694%206H12.5a.5.5%200%200%201%20.395.807l-7%209a.5.5%200%200%201-.873-.454L6.823%209.5H3.5a.5.5%200%200%201-.48-.641l2.5-8.5z%22/%3E%3C/svg%3E");}.pdoc .visually-hidden{position:absolute !important;width:1px !important;height:1px !important;padding:0 !important;margin:-1px !important;overflow:hidden !important;clip:rect(0, 0, 0, 0) !important;white-space:nowrap !important;border:0 !important;}.pdoc h1, .pdoc h2, .pdoc h3{font-weight:300;margin:.3em 0;padding:.2em 0;}.pdoc > section:not(.module-info) h1{font-size:1.5rem;font-weight:500;}.pdoc > section:not(.module-info) h2{font-size:1.4rem;font-weight:500;}.pdoc > section:not(.module-info) h3{font-size:1.3rem;font-weight:500;}.pdoc > section:not(.module-info) h4{font-size:1.2rem;}.pdoc > section:not(.module-info) h5{font-size:1.1rem;}.pdoc a{text-decoration:none;color:var(--link);}.pdoc a:hover{color:var(--link-hover);}.pdoc blockquote{margin-left:2rem;}.pdoc pre{border-top:1px solid var(--accent2);border-bottom:1px solid var(--accent2);margin-top:0;margin-bottom:1em;padding:.5rem 0 .5rem .5rem;overflow-x:auto;background-color:var(--code);}.pdoc code{color:var(--text);padding:.2em .4em;margin:0;font-size:85%;background-color:var(--accent);border-radius:6px;}.pdoc a > code{color:inherit;}.pdoc pre > code{display:inline-block;font-size:inherit;background:none;border:none;padding:0;}.pdoc > section:not(.module-info){margin-bottom:1.5rem;}.pdoc .modulename{margin-top:0;font-weight:bold;}.pdoc .modulename a{color:var(--link);transition:100ms all;}.pdoc .git-button{float:right;border:solid var(--link) 1px;}.pdoc .git-button:hover{background-color:var(--link);color:var(--pdoc-background);}.view-source-toggle-state,.view-source-toggle-state ~ .pdoc-code{display:none;}.view-source-toggle-state:checked ~ .pdoc-code{display:block;}.view-source-button{display:inline-block;float:right;font-size:.75rem;line-height:1.5rem;color:var(--muted);padding:0 .4rem 0 1.3rem;cursor:pointer;text-indent:-2px;}.view-source-button > span{visibility:hidden;}.module-info .view-source-button{float:none;display:flex;justify-content:flex-end;margin:-1.2rem .4rem -.2rem 0;}.view-source-button::before{position:absolute;content:"View Source";display:list-item;list-style-type:disclosure-closed;}.view-source-toggle-state:checked ~ .attr .view-source-button::before,.view-source-toggle-state:checked ~ .view-source-button::before{list-style-type:disclosure-open;}.pdoc .docstring{margin-bottom:1.5rem;}.pdoc section:not(.module-info) .docstring{margin-left:clamp(0rem, 5vw - 2rem, 1rem);}.pdoc .docstring .pdoc-code{margin-left:1em;margin-right:1em;}.pdoc h1:target,.pdoc h2:target,.pdoc h3:target,.pdoc h4:target,.pdoc h5:target,.pdoc h6:target,.pdoc .pdoc-code > pre > span:target{background-color:var(--active);box-shadow:-1rem 0 0 0 var(--active);}.pdoc .pdoc-code > pre > span:target{display:block;}.pdoc div:target > .attr,.pdoc section:target > .attr,.pdoc dd:target > a{background-color:var(--active);}.pdoc *{scroll-margin:2rem;}.pdoc .pdoc-code .linenos{user-select:none;}.pdoc .attr:hover{filter:contrast(0.95);}.pdoc section, .pdoc .classattr{position:relative;}.pdoc .headerlink{--width:clamp(1rem, 3vw, 2rem);position:absolute;top:0;left:calc(0rem - var(--width));transition:all 100ms ease-in-out;opacity:0;}.pdoc .headerlink::before{content:"#";display:block;text-align:center;width:var(--width);height:2.3rem;line-height:2.3rem;font-size:1.5rem;}.pdoc .attr:hover ~ .headerlink,.pdoc *:target > .headerlink,.pdoc .headerlink:hover{opacity:1;}.pdoc .attr{display:block;margin:.5rem 0 .5rem;padding:.4rem .4rem .4rem 1rem;background-color:var(--accent);overflow-x:auto;}.pdoc .classattr{margin-left:2rem;}.pdoc .name{color:var(--name);font-weight:bold;}.pdoc .def{color:var(--def);font-weight:bold;}.pdoc .signature{background-color:transparent;}.pdoc .param, .pdoc .return-annotation{white-space:pre;}.pdoc .signature.multiline .param{display:block;}.pdoc .signature.condensed .param{display:inline-block;}.pdoc .annotation{color:var(--annotation);}.pdoc .view-value-toggle-state,.pdoc .view-value-toggle-state ~ .default_value{display:none;}.pdoc .view-value-toggle-state:checked ~ .default_value{display:inherit;}.pdoc .view-value-button{font-size:.5rem;vertical-align:middle;border-style:dashed;margin-top:-0.1rem;}.pdoc .view-value-button:hover{background:white;}.pdoc .view-value-button::before{content:"show";text-align:center;width:2.2em;display:inline-block;}.pdoc .view-value-toggle-state:checked ~ .view-value-button::before{content:"hide";}.pdoc .inherited{margin-left:2rem;}.pdoc .inherited dt{font-weight:700;}.pdoc .inherited dt, .pdoc .inherited dd{display:inline;margin-left:0;margin-bottom:.5rem;}.pdoc .inherited dd:not(:last-child):after{content:", ";}.pdoc .inherited .class:before{content:"class ";}.pdoc .inherited .function a:after{content:"()";}.pdoc .search-result .docstring{overflow:auto;max-height:25vh;}.pdoc .search-result.focused > .attr{background-color:var(--active);}.pdoc .attribution{margin-top:2rem;display:block;opacity:0.5;transition:all 200ms;filter:grayscale(100%);}.pdoc .attribution:hover{opacity:1;filter:grayscale(0%);}.pdoc .attribution img{margin-left:5px;height:35px;vertical-align:middle;width:70px;transition:all 200ms;}.pdoc table{display:block;width:max-content;max-width:100%;overflow:auto;margin-bottom:1rem;}.pdoc table th{font-weight:600;}.pdoc table th, .pdoc table td{padding:6px 13px;border:1px solid var(--accent2);}</style></div>